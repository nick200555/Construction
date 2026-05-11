import frappe
from frappe.model.document import Document

class SafetyIncident(Document):
    def on_submit(self):
        if self.incident_type in ['Lost Time Injury', 'Fatality'] and not self.reported_to_authorities:
            frappe.msgprint(
                'Warning: Serious incident must be reported to regulatory authorities',
                alert=True, indicator='red')
        self.notify_safety_officer()

    def notify_safety_officer(self):
        subject = f'Safety Incident Reported: {self.incident_type} - {self.project}'
        message = f'<p>A {self.incident_type} has been reported on project {self.project}.</p>'
        message += f'<p>Severity: {self.severity}</p>'
        safety_officers = frappe.get_all('Has Role',
            filters={'role': 'Safety Officer', 'parenttype': 'User'},
            fields=['parent'])
        for so in safety_officers:
            user = frappe.get_doc('User', so.parent)
            if user.email:
                frappe.sendmail(recipients=[user.email], subject=subject, message=message)
