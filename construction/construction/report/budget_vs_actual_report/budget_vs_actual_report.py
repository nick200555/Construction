import frappe
from frappe import _

def execute(filters=None):
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {"fieldname": "project", "label": _("Project"), "fieldtype": "Link", "options": "Project", "width": 150},
        {"fieldname": "budget_total", "label": _("Budget"), "fieldtype": "Currency", "width": 140},
        {"fieldname": "actual_cost", "label": _("Actual Cost"), "fieldtype": "Currency", "width": 140},
        {"fieldname": "variance", "label": _("Variance"), "fieldtype": "Currency", "width": 140}
    ]

def get_data(filters):
    return frappe.db.sql('''SELECT name as project, budget_total, actual_cost_to_date as actual_cost, (budget_total - actual_cost_to_date) as variance FROM `tabProject` WHERE docstatus=1''', as_dict=True)
