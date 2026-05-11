import frappe
@frappe.whitelist()
def get_dashboard_stats():
    return {
        'active_projects': frappe.db.count('Project', {'status': 'Active'}),
        'open_safety_incidents': frappe.db.count('Safety Incident', {'status': 'Open'})
    }
