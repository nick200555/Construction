import frappe
from frappe import _

def execute(filters=None):
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {"fieldname": "name", "label": _("ID"), "fieldtype": "Link", "options": "Purchase Order", "width": 120},
        {"fieldname": "project", "label": _("Project"), "fieldtype": "Link", "options": "Project", "width": 150},
        {"fieldname": "supplier", "label": _("Supplier"), "fieldtype": "Link", "options": "Supplier", "width": 150},
        {"fieldname": "total_amount", "label": _("Amount"), "fieldtype": "Currency", "width": 120}
    ]

def get_data(filters):
    return frappe.get_all("Purchase Order", fields=["name", "project", "supplier", "total_amount"], filters={"docstatus": 1})
