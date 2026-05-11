import frappe
from frappe.utils import today, add_days

def check_overdue_milestones():
    milestones = frappe.db.sql('''SELECT m.name FROM `tabSubcontract Milestone` m JOIN `tabSubcontract` s ON s.name = m.parent WHERE m.status = 'Pending' AND m.due_date < CURDATE() AND s.docstatus=1''', as_dict=True)
    for m in milestones: frappe.db.set_value('Subcontract Milestone', m.name, 'status', 'Overdue')
    frappe.db.commit()

def check_budget_overruns():
    projects = frappe.get_all('Project', filters={'status': 'Active', 'docstatus': 1}, fields=['name', 'project_name', 'budget_total', 'actual_cost_to_date'])
    for p in projects:
        if p.budget_total and p.actual_cost_to_date > p.budget_total:
            frappe.publish_realtime('budget_overrun', {'project': p.project_name, 'overrun': p.actual_cost_to_date - p.budget_total})

def send_milestone_reminders():
    due_date = add_days(today(), 7)
    milestones = frappe.db.sql('''SELECT m.parent as subcontract, m.milestone_name FROM `tabSubcontract Milestone` m WHERE m.status = 'Pending' AND m.due_date = %s''', (due_date,), as_dict=True)
    for m in milestones:
        frappe.sendmail(recipients=frappe.get_all('Has Role', filters={'role': 'Construction Project Manager'}, pluck='parent'), subject=f'Milestone Due: {m.milestone_name}', message=f'Milestone {m.milestone_name} is due on {due_date}')

def update_project_progress():
    for p in frappe.get_all('Project', filters={'status': 'Active', 'docstatus': 1}):
        frappe.get_doc('Project', p.name).update_completion()

def generate_daily_site_summary():
    pass
