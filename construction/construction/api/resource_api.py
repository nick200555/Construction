import frappe
@frappe.whitelist()
def get_resource_allocation(project):
    return frappe.get_all('Work Order Resource', filters={'parent': ['in', frappe.get_all('Work Order', filters={'project': project}, pluck='name')]})
