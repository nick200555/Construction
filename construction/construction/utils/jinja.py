import frappe
def get_project_progress_status(project_name):
    proj = frappe.get_doc('Project', project_name)
    pct = proj.completion_percentage or 0
    return f'{pct}%'
