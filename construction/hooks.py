app_name = "construction"
app_title = "Construction Management"
app_publisher = "Construction Team"
app_description = "Comprehensive Construction Management System for ERPNext v15+"
app_email = "admin@construction.org"
app_license = "mit"

# DocTypes to be exported as fixtures
fixtures = [
    {"dt": "Custom Field", "filters": [["name","in",["Construction-Custom Fields"]]]},
    {"dt": "Role", "filters": [["name","in",[
        "Construction Project Manager",
        "Site Engineer",
        "Construction Procurement Officer",
        "QA/QC Inspector",
        "Safety Officer"
    ]]]},
    {"dt": "Workflow", "filters": [["document_type","in",[
        "Project","Purchase Order","Subcontract","Work Order"
    ]]]},
    {"dt": "Notification", "filters": [["document_type","in",[
        "Project","Safety Incident","Subcontract","Purchase Order"
    ]]]},
    {"dt": "Workspace", "filters": [["name","in",["Construction"]]]},
    {"dt": "Dashboard", "filters": [["name","in",["Construction Dashboard"]]]},
    {"dt": "Dashboard Chart", "filters": [["chart_name","in",[
        "Active Projects by Phase","Monthly Progress",
        "Project Cost Trend","Procurement Spend"
    ]]]},
]

# Hook on document events
doc_events = {
    "Project": {
        "on_submit": "construction.construction.doctype.project.project.on_submit",
        "validate": "construction.construction.doctype.project.project.validate"
    },
    "Work Order": {
        "validate": "construction.construction.doctype.work_order.work_order.validate",
        "on_submit": "construction.construction.doctype.work_order.work_order.on_submit"
    },
    "Purchase Order": {
        "validate": "construction.construction.doctype.purchase_order.purchase_order.validate",
        "on_submit": "construction.construction.doctype.purchase_order.purchase_order.on_submit"
    },
    "Subcontract": {
        "validate": "construction.construction.doctype.subcontract.subcontract.validate",
        "on_submit": "construction.construction.doctype.subcontract.subcontract.on_submit"
    },
    "Safety Incident": {
        "on_submit": "construction.construction.doctype.safety_incident.safety_incident.on_submit"
    },
    "Quality Inspection": {
        "on_submit": "construction.construction.doctype.quality_inspection.quality_inspection.on_submit"
    }
}

# Scheduled Tasks
scheduler_events = {
    "hourly": [
        "construction.construction.utils.scheduler.check_overdue_milestones",
        "construction.construction.utils.scheduler.check_budget_overruns"
    ],
    "daily": [
        "construction.construction.utils.scheduler.send_milestone_reminders",
        "construction.construction.utils.scheduler.update_project_progress",
        "construction.construction.utils.scheduler.generate_daily_site_summary"
    ],
    "weekly": [
        "construction.construction.utils.scheduler.generate_weekly_project_report"
    ]
}

required_apps = ["erpnext"]
after_install = "construction.construction.setup.install.after_install"
before_uninstall = "construction.construction.setup.uninstall.before_uninstall"
