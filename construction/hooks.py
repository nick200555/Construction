app_name = "construction"
app_title = "Construction Management"
app_publisher = "Construction Team"
app_description = "Comprehensive Construction Management System for ERPNext v15+"
app_email = "admin@construction.org"
app_license = "mit"

# Bundle includes
# (Removed to prevent esbuild crashing on empty files)

# DocTypes to be exported as fixtures
fixtures = [
    "Custom DocPerm",
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
    ]]]}
]

# Hook on document events
doc_events = {}

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
