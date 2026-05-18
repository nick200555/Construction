import frappe
def after_install():
    ensure_module_def()
    create_roles()
    create_default_data()
    ensure_custom_permissions()

def ensure_module_def():
    if not frappe.db.exists("Module Def", "Construction"):
        doc = frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "Construction",
            "app_name": "construction",
            "custom": 0
        })
        doc.insert(ignore_permissions=True, ignore_if_duplicate=True)

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

def ensure_custom_permissions():
    try:
        from frappe.permissions import add_permission
        for dt in ['Project', 'Purchase Order', 'Work Order', 'Safety Incident']:
            try:
                add_permission(dt, 'Construction Project Manager', 0)
                add_permission(dt, 'Site Engineer', 0)
                
                # explicitly set report and read properties
                perms = frappe.get_all('Custom DocPerm', filters={'parent': dt, 'role': ['in', ['Construction Project Manager', 'Site Engineer']]}, fields=['name'])
                for p in perms:
                    frappe.db.set_value('Custom DocPerm', p.name, 'report', 1)
                    frappe.db.set_value('Custom DocPerm', p.name, 'read', 1)
            except Exception as e:
                pass
    except ImportError:
        pass
