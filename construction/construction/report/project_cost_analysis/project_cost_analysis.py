import frappe
from frappe import _

@frappe.whitelist()
def execute(filters=None):
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {"fieldname": "project", "label": _("Project"), "fieldtype": "Link", "options": "Project", "width": 160},
        {"fieldname": "project_type", "label": _("Type"), "fieldtype": "Data", "width": 120},
        {"fieldname": "contract_value", "label": _("Contract Value"), "fieldtype": "Currency", "width": 140},
        {"fieldname": "budget_total", "label": _("Budget"), "fieldtype": "Currency", "width": 140},
        {"fieldname": "actual_cost", "label": _("Actual Cost"), "fieldtype": "Currency", "width": 140},
        {"fieldname": "variance", "label": _("Variance"), "fieldtype": "Currency", "width": 140},
        {"fieldname": "completion", "label": _("Completion %"), "fieldtype": "Percent", "width": 110},
        {"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100}
    ]

def get_data(filters):
    conditions = ''
    if filters.get('project_type'):
        conditions += f" AND project_type = '{filters['project_type']}'"
    if filters.get('status'):
        conditions += f" AND status = '{filters['status']}'"
    query = f'''
        SELECT name as project, project_type, contract_value,
               budget_total, actual_cost_to_date as actual_cost,
               (budget_total - actual_cost_to_date) as variance,
               completion_percentage as completion, status
        FROM `tabProject` WHERE docstatus=1 {conditions}
        ORDER BY project_name ASC
    '''
    return frappe.db.sql(query, as_dict=True)
