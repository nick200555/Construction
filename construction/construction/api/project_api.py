import frappe
@frappe.whitelist()
def get_project_summary(project):
    doc = frappe.get_doc('Project', project)
    work_orders = frappe.get_all('Work Order', filters={'project': project, 'docstatus': 1})
    return {
        'project_name': doc.project_name,
        'completion_percentage': doc.completion_percentage,
        'status': doc.status
    }
