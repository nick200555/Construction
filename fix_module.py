import frappe

def execute():
    # Check if the Module Def 'Construction' exists
    if not frappe.db.exists("Module Def", "Construction"):
        # Create it with exact capitalization
        doc = frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "Construction",
            "app_name": "construction",
            "custom": 0
        })
        doc.insert(ignore_permissions=True, ignore_if_duplicate=True)
        frappe.db.commit()
        print("Successfully created 'Construction' Module Def.")
    else:
        print("'Construction' Module Def already exists.")

    # Just to be completely safe, also create lowercase if it's looking for that
    if not frappe.db.exists("Module Def", "construction"):
        doc = frappe.get_doc({
            "doctype": "Module Def",
            "module_name": "construction",
            "app_name": "construction",
            "custom": 0
        })
        doc.insert(ignore_permissions=True, ignore_if_duplicate=True)
        frappe.db.commit()
        print("Successfully created 'construction' (lowercase) Module Def.")
