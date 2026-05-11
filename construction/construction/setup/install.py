import frappe
def after_install():
    create_roles()
    create_default_data()

def create_roles():
    roles = ["Construction Project Manager", "Site Engineer", "Construction Procurement Officer", "QA/QC Inspector", "Safety Officer"]
    for role in roles:
        if not frappe.db.exists('Role', role):
            doc = frappe.new_doc('Role')
            doc.role_name = role
            doc.desk_access = 1
            doc.insert()

def create_default_data():
    phases = [
        {"phase_name": "Pre-Construction", "phase_code": "PC", "sequence_no": 1},
        {"phase_name": "Foundation", "phase_code": "FND", "sequence_no": 2},
        {"phase_name": "Structure", "phase_code": "STR", "sequence_no": 3}
    ]
    for p in phases:
        if not frappe.db.exists('Construction Phase', p['phase_name']):
            doc = frappe.new_doc('Construction Phase')
            for k, v in p.items(): setattr(doc, k, v)
            doc.insert()
