import frappe
from frappe import _

@frappe.whitelist()
def execute(filters=None):
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {"fieldname": "name", "label": _("Incident ID"), "fieldtype": "Link", "options": "Safety Incident", "width": 130},
        {"fieldname": "project", "label": _("Project"), "fieldtype": "Link", "options": "Project", "width": 150},
        {"fieldname": "incident_date", "label": _("Date"), "fieldtype": "Date", "width": 110},
        {"fieldname": "incident_type", "label": _("Type"), "fieldtype": "Data", "width": 150},
        {"fieldname": "severity", "label": _("Severity"), "fieldtype": "Data", "width": 100},
        {"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 110}
    ]

def get_data(filters):
    conditions = ' WHERE docstatus=1'
    if filters.get('project'):
        conditions += f" AND project = '{filters['project']}'"
    if filters.get('from_date'):
        conditions += f" AND incident_date >= '{filters['from_date']}'"
    if filters.get('to_date'):
        conditions += f" AND incident_date <= '{filters['to_date']}'"
    return frappe.db.sql(f'SELECT name, project, incident_date, incident_type, severity, status FROM `tabSafety Incident` {conditions} ORDER BY incident_date DESC', as_dict=True)
