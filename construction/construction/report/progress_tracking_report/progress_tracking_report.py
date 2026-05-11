import frappe
from frappe import _

def execute(filters=None):
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {"fieldname": "project", "label": _("Project"), "fieldtype": "Link", "options": "Project", "width": 150},
        {"fieldname": "completion", "label": _("Completion %"), "fieldtype": "Percent", "width": 110},
        {"fieldname": "end_date", "label": _("End Date"), "fieldtype": "Date", "width": 110}
    ]

def get_data(filters):
    return frappe.get_all("Project", fields=["name as project", "completion_percentage as completion", "end_date"], filters={"docstatus": 1})
