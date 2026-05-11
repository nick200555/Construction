import frappe
from frappe import _

@frappe.whitelist()
def execute(filters=None):
    return get_columns(), get_data(filters)

def get_columns():
    return [
        {"fieldname": "project", "label": _("Project"), "fieldtype": "Link", "options": "Project", "width": 150},
        {"fieldname": "resource_type", "label": _("Resource Type"), "fieldtype": "Data", "width": 120},
        {"fieldname": "description", "label": _("Description"), "fieldtype": "Data", "width": 200},
        {"fieldname": "total_quantity", "label": _("Total Qty"), "fieldtype": "Float", "width": 100},
        {"fieldname": "total_cost", "label": _("Total Cost"), "fieldtype": "Currency", "width": 130}
    ]

def get_data(filters):
    conditions = ''
    if filters.get('project'):
        conditions += f" AND wo.project = '{filters['project']}'"
    query = f'''
        SELECT wo.project, r.resource_type, r.description,
               SUM(r.quantity) as total_quantity, SUM(r.total_cost) as total_cost
        FROM `tabWork Order Resource` r
        JOIN `tabWork Order` wo ON wo.name = r.parent
        WHERE wo.docstatus=1 {conditions}
        GROUP BY wo.project, r.resource_type, r.description
        ORDER BY wo.project, r.resource_type
    '''
    return frappe.db.sql(query, as_dict=True)
