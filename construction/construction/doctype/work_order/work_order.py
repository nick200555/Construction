import frappe
from frappe.model.document import Document
class WorkOrder(Document):
	def on_submit(self):
		pass
	def validate(self):
		pass
