# Copyright (c) 2025, Construction Team and contributors
import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate, date_diff

class Project(Document):
    def validate(self):
        if self.start_date and self.end_date:
            if getdate(self.end_date) <= getdate(self.start_date):
                frappe.throw('End Date must be after Start Date')
        if self.budget_total and self.actual_cost_to_date:
            if self.actual_cost_to_date > self.budget_total * 1.1:
                frappe.msgprint('Warning: Actual cost exceeds budget by more than 10%', alert=True)

    def on_submit(self):
        self.status = 'Active'
        self.db_set('status', 'Active')

    def update_completion(self):
        work_orders = frappe.get_all('Work Order',
            filters={'project': self.name, 'docstatus': 1},
            fields=['completion_percentage', 'weightage'])
        if work_orders:
            total_weight = sum(w.weightage or 1 for w in work_orders)
            weighted_progress = sum((w.completion_percentage or 0) * (w.weightage or 1) for w in work_orders)
            self.completion_percentage = weighted_progress / total_weight
            self.save()
