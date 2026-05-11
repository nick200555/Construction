import frappe
@frappe.whitelist()
def get_billing_summary(project):
    return frappe.get_all('Progress Claim', filters={'project': project}, fields=['claim_date', 'net_claim', 'status'])
