# Construction Management System for ERPNext v15+
# 🏗️ ConstructionOS — Construction Management System for ERPNext v15+
A comprehensive, production-ready Construction Management System built on the Frappe Framework.
> A comprehensive, production-ready Construction Management System built on the **Frappe Framework** and **ERPNext v15+**.  
> Designed for Project Managers, Site Engineers, Procurement Officers, QA/QC Inspectors, Safety Officers, and Finance Teams.
## Features
- Project Management
- Site Management
- Contractor & Subcontractor Tracking
- Estimation & Budgeting
- Quality Control & Safety Management
- Progress Tracking & Billing
---
## 📋 Table of Contents
- [Features & Modules](#-features--modules)
- [Architecture Overview](#-architecture-overview)
- [Installation](#-installation)
- [User Roles](#-user-roles)
- [DocType Reference](#-doctype-reference)
- [Scheduled Tasks](#-scheduled-tasks)
- [API & Hooks](#-api--hooks)
- [Changelog](#-changelog)
- [License](#-license)
---
## 🚀 Features & Modules
### Module 1 — Project Management
- Create and manage construction projects with unique project codes, clients, and sites
- Set start/end dates, project types (Residential, Commercial, Industrial, Infrastructure), and budgets
- **Auto-create linked Cost Center in Accounting** upon project submission
- Track completion percentage via weighted Work Order aggregation
- Budget overrun alerts at 10% and hard blocks for non-PMs at 15%
### Module 2 — Site Management
- Daily Site Diary for capturing weather, workers on site, work carried out, and materials delivered
- Track site visitors (name, organisation, purpose)
- **Automated daily email digest** summarising all site diaries sent to Project Managers
### Module 3 — Contractor & Subcontractor Management
- Full contractor onboarding: type, trade category, registration, insurance, performance rating
- **Expired insurance validation** — system flags contractors with lapsed insurance during Subcontract creation
- Subcontract agreements with milestone payment stages, scope definitions, and **default 5% retention**
- Tracks `amount_paid` and `amount_retained` auto-updated from Progress Claims
### Module 4 — Procurement & Materials
- Material Requests linked to projects and work orders
- Purchase Orders with multi-stage status workflow: Draft → Pending Approval → Approved → Received
- **Budget guard**: PO validation blocks amounts exceeding project budget by >15% (PM override warning)
- Real-time `actual_cost_to_date` auto-update on Project after PO submission/cancellation
### Module 5 — Quality Control
- Structured Quality Inspections with configurable checklists (Pass/Fail/N/A per item)
- Inspection types: Routine, Pre-pour, Structural, Finishes, Final, Client Walkthrough
- **Work Order status propagation**: Pass → marks WO as Completed (100%). Fail → keeps WO In Progress with desk alert
### Module 6 — Safety Management
- Full incident reporting: Near Miss, First Aid, Lost Time Injury (LTI), Fatality
- Corrective action tracking and authority reporting compliance flag
- **Dual escalation routing**: Safety Officer for all incidents; **Operations Head (Project Managers & Admins) instantly alerted for LTI/Fatality**
### Module 7 — Billing & Progress Claims
- Full claims calculation engine:
  - **Gross Claim** = Completion % × Contract Value
  - **Previous Claims** = Sum of all prior submitted claims
  - **Net Claim** = Gross − Previous
  - **Retention** = Net × Retention % (from linked Subcontract, defaulting to 5%)
  - **Amount Due** = Net − Retention
- Auto-updates Subcontract `amount_retained` and `amount_paid` balances
### Module 8 — Reports & Analytics
- **Project Cost Analysis** — Contract vs Budget vs Actual
- **Resource Utilization** — Labour & Equipment hours
- **Safety Incident Report** — Frequency & severity tracking
- **Budget vs Actual** — Line-item variance
- Live Dashboard with 4 KPI charts: Active Projects by Phase, Monthly Progress, Project Cost Trend, Procurement Spend
---
## 🏛️ Architecture Overview
```
construction/
├── construction/               # Main Frappe app module
│   ├── doctype/                # 17 DocTypes
│   │   ├── project/            # Core project controller with Cost Center integration
│   │   ├── work_order/         # Work order with resource costing
│   │   ├── subcontract/        # Subcontract with insurance & retention logic
│   │   ├── purchase_order/     # PO with budget guard & actual cost rollup
│   │   ├── quality_inspection/ # QC with Work Order state transitions
│   │   ├── safety_incident/    # Incident alerts with dual escalation
│   │   ├── progress_claim/     # Full billing calculation engine
│   │   ├── site_diary/         # Daily site logging
│   │   ├── material_request/   # Procurement requests
│   │   ├── contractor/         # Contractor onboarding & compliance
│   │   └── ...                 # Masters: Phase, Site, Trade Category, BOQ
│   ├── utils/
│   │   └── scheduler.py        # Hourly/Daily/Weekly automated tasks
│   ├── setup/
│   │   ├── install.py          # Post-install: roles, module def, permissions
│   │   ├── seed_data.py        # Demo data seeder
│   │   └── uninstall.py
│   ├── workspace/              # Construction workspace JSON
│   ├── dashboard/              # Dashboard definition
│   └── dashboard_chart/        # 4 chart definitions
├── hooks.py                    # App-level hooks, fixtures, scheduler config
├── CONSTRUCTION_SOP.md         # Full Standard Operating Procedure
└── setup.py
```
---
## ⚙️ Installation
### Prerequisites
- ERPNext v15+
- Frappe Bench
### Steps
```bash
# 1. Add the app to your bench
bench get-app https://github.com/nick200555/Construction.git
# 2. Install on your site
bench --site your-site.local install-app construction
# 3. Migrate database
bench --site your-site.local migrate
# 4. Reload
bench --site your-site.local clear-cache
bench restart
```
> **Tip:** To seed demo data (sites, projects, work orders, etc.), run:
> ```bash
> bench --site your-site.local execute construction.construction.setup.seed_data.execute
> ```
---
## 👤 User Roles
| Role | Responsibilities |
|---|---|
| **Construction Project Manager** | Full project control, budget approvals, PO overrides |
| **Site Engineer** | Site diaries, work order execution, material requests |
| **Construction Procurement Officer** | Material requests, PO creation and management |
| **QA/QC Inspector** | Quality inspections and checklist management |
| **Safety Officer** | Incident reporting, safety audits, PPE compliance tracking |
| **Finance Manager** | Progress claims, retention tracking, cost analysis |
---
## 📑 DocType Reference
| DocType | Auto-name | Submittable | Key Fields |
|---|---|---|---|
| **Project** | `PROJ-{YY}-{####}` | ✅ | project_code, client, construction_site, budget_total, actual_cost_to_date |
| **Work Order** | `WO-{YY}-{####}` | ✅ | project, assigned_contractor, completion_percentage, weightage |
| **Subcontract** | `SC-{YY}-{####}` | ✅ | contractor, retention_percentage, milestones, amount_retained, amount_paid |
| **Purchase Order** | `PO-{YY}-{####}` | ✅ | project, supplier, total_amount, status |
| **Quality Inspection** | `QI-{YY}-{####}` | ✅ | work_order, checklist, overall_result |
| **Safety Incident** | Frappe default | ✅ | incident_type, severity, corrective_action, reported_to_authorities |
| **Progress Claim** | `PC-{project}-{####}` | ✅ | gross_claim, net_claim, retention_amount, amount_due |
| **Site Diary** | Frappe default | ❌ | diary_date, weather, workers_on_site, work_carried_out |
| **Material Request** | Frappe default | ✅ | project, required_by, status |
| **Contractor** | `CONT-{YY}-{####}` | ❌ | contractor_type, trade_category, insurance_expiry, is_approved |
| **Construction Site** | Frappe default | ❌ | site_code, city, country |
| **Construction Phase** | Frappe default | ❌ | phase_code, sequence_no |
| **Trade Category** | Frappe default | ❌ | category_code |
| **BOQ Item** | Frappe default | ❌ | item, quantity, unit, rate |
---
## ⏰ Scheduled Tasks
| Frequency | Task | Description |
|---|---|---|
| **Hourly** | `check_overdue_milestones` | Marks subcontract milestones past due date as 'Overdue' |
| **Hourly** | `check_budget_overruns` | Pushes real-time budget overrun notifications for active projects |
| **Daily** | `send_milestone_reminders` | Emails PM 7 days before milestone due dates |
| **Daily** | `update_project_progress` | Recalculates weighted completion % for all active projects |
| **Daily** | `generate_daily_site_summary` | Compiles all site diaries and emails a summary to Project Managers |
| **Weekly** | `generate_weekly_project_report` | Generates a full weekly project health digest |
---
## 🔗 API & Hooks
Key hooks registered in `hooks.py`:
```python
required_apps = ["erpnext"]
after_install = "construction.construction.setup.install.after_install"
before_uninstall = "construction.construction.setup.uninstall.before_uninstall"
fixtures = [
    "Custom DocPerm",
    {"dt": "Role", "filters": [["name", "in", [
        "Construction Project Manager", "Site Engineer",
        "Construction Procurement Officer", "QA/QC Inspector", "Safety Officer"
    ]]]},
    {"dt": "Workflow", "filters": [["document_type", "in", [
        "Project", "Purchase Order", "Subcontract", "Work Order"
    ]]]},
    {"dt": "Notification", "filters": [["document_type", "in", [
        "Project", "Safety Incident", "Subcontract", "Purchase Order"
    ]]]}
]
```
---
## 📝 Changelog
### v1.1.0 — Backend Logic Completion (2026-05)
**7 files changed, 194 insertions(+)**
| File | Change |
|---|---|
| `project.py` | Auto-creates linked **Cost Center** in Accounting on project submission |
| `subcontract.py` | Validates **contractor insurance expiry**; auto-defaults retention to 5% |
| `purchase_order.py` | Enforces **15% budget overrun guard** with role-based override; updates `actual_cost_to_date` in real-time |
| `quality_inspection.py` | Propagates **Pass → Work Order Completed** / **Fail → Work Order In Progress** |
| `progress_claim.py` | Full **billing calculation engine** — Gross Claim, Net Claim, Retention, Amount Due + Subcontract balance sync |
| `safety_incident.py` | **Dual escalation routing** — Safety Officer for all; Project Managers instantly alerted for LTI/Fatality |
| `scheduler.py` | Completed **daily site diary email summary** to all Project Managers |
### v1.0.0 — Initial Release
- Full DocType schema for all 14 DocTypes
- Workspace, Dashboard, and 4 chart definitions
- Installation setup with role and master data creation
- Seed data for demo environments
---
## 📄 License
MIT — see [license.txt](license.txt)
---
*Built with ❤️ for the Construction Industry on ERPNext v15 by the ConstructionOS Team.*
