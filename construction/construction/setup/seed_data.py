import frappe
from frappe.utils import add_days, nowdate, today, getdate

def execute():
    frappe.logger().info("Starting Construction App Data Seeding...")
    print("Starting Construction App Data Seeding...")

    frappe.flags.in_import = True
    
    # 1. Ensure basic Frappe Master Data
    ensure_basic_frappe_masters()

    # 2. Construction Master Data
    seed_trade_categories()
    seed_construction_phases()
    seed_construction_sites()
    seed_contractors()

    # 3. Transactional Data
    seed_projects()
    seed_work_orders()
    seed_subcontracts()
    seed_material_requests()
    seed_purchase_orders()
    seed_site_diaries()
    seed_quality_inspections()
    seed_safety_incidents()
    seed_progress_claims()

    frappe.db.commit()
    print("Seeding completed successfully!")

def ensure_basic_frappe_masters():
    # Customer
    for cust in ["Acme Corp", "Global Industries", "City Council"]:
        if not frappe.db.exists("Customer", cust):
            frappe.get_doc({
                "doctype": "Customer",
                "customer_name": cust,
                "customer_type": "Company",
                "customer_group": "Commercial" if frappe.db.exists("Customer Group", "Commercial") else "All Customer Groups",
                "territory": "All Territories"
            }).insert(ignore_permissions=True)
            
    # Supplier
    for supp in ["BuildPro Supplies", "Steel Co", "Cement World"]:
        if not frappe.db.exists("Supplier", supp):
            frappe.get_doc({
                "doctype": "Supplier",
                "supplier_name": supp,
                "supplier_type": "Company",
                "supplier_group": "Local" if frappe.db.exists("Supplier Group", "Local") else "All Supplier Groups"
            }).insert(ignore_permissions=True)

def seed_trade_categories():
    categories = [
        {"category_name": "Civil", "category_code": "TC-CIV"},
        {"category_name": "Electrical", "category_code": "TC-ELE"},
        {"category_name": "Plumbing", "category_code": "TC-PLU"},
        {"category_name": "HVAC", "category_code": "TC-HVA"},
        {"category_name": "Interior", "category_code": "TC-INT"}
    ]
    for cat in categories:
        if not frappe.db.exists("Trade Category", cat["category_name"]):
            frappe.get_doc({"doctype": "Trade Category", **cat}).insert(ignore_permissions=True)

def seed_construction_phases():
    phases = [
        {"phase_name": "Planning", "phase_code": "PH-01", "sequence_no": 1},
        {"phase_name": "Excavation", "phase_code": "PH-02", "sequence_no": 2},
        {"phase_name": "Structural", "phase_code": "PH-03", "sequence_no": 3},
        {"phase_name": "Finishing", "phase_code": "PH-04", "sequence_no": 4},
        {"phase_name": "Handover", "phase_code": "PH-05", "sequence_no": 5}
    ]
    for ph in phases:
        if not frappe.db.exists("Construction Phase", ph["phase_name"]):
            frappe.get_doc({"doctype": "Construction Phase", **ph}).insert(ignore_permissions=True)

def seed_construction_sites():
    sites = [
        {"site_name": "Bangalore Tech Park Tower A", "site_code": "BLR-TPA", "city": "Bangalore", "country": "India"},
        {"site_name": "Hyderabad IT Campus", "site_code": "HYD-ITC", "city": "Hyderabad", "country": "India"},
        {"site_name": "Chennai Commercial Hub", "site_code": "CHN-CH", "city": "Chennai", "country": "India"}
    ]
    for s in sites:
        if not frappe.db.exists("Construction Site", {"site_name": s["site_name"]}):
            frappe.get_doc({"doctype": "Construction Site", **s}).insert(ignore_permissions=True)

def seed_contractors():
    contractors = [
        {"contractor_name": "ABC Civil Contractors", "contractor_type": "Main Contractor", "trade_category": "Civil", "phone": "1234567890"},
        {"contractor_name": "Skyline Infrastructure", "contractor_type": "Main Contractor", "trade_category": "Civil", "phone": "1234567891"},
        {"contractor_name": "Volt Electricals", "contractor_type": "Specialist", "trade_category": "Electrical", "phone": "1234567892"},
        {"contractor_name": "Aqua Pipes", "contractor_type": "Subcontractor", "trade_category": "Plumbing", "phone": "1234567893"}
    ]
    for c in contractors:
        if not frappe.db.exists("Contractor", {"contractor_name": c["contractor_name"]}):
            frappe.get_doc({"doctype": "Contractor", **c}).insert(ignore_permissions=True)

def seed_projects():
    projects = [
        {
            "project_name": "Office Tower Construction", "project_code": "PRJ-001",
            "client": "Acme Corp", "construction_site": get_site("Bangalore Tech Park Tower A"),
            "project_type": "Commercial", "contract_value": 5000000,
            "start_date": add_days(today(), -30), "end_date": add_days(today(), 300),
            "project_manager": "Administrator", "current_phase": "Excavation", "status": "Active"
        },
        {
            "project_name": "Luxury Apartment Complex", "project_code": "PRJ-002",
            "client": "Global Industries", "construction_site": get_site("Hyderabad IT Campus"),
            "project_type": "Residential", "contract_value": 8500000,
            "start_date": add_days(today(), -60), "end_date": add_days(today(), 200),
            "project_manager": "Administrator", "current_phase": "Structural", "status": "Active"
        },
        {
            "project_name": "Industrial Warehouse Project", "project_code": "PRJ-003",
            "client": "City Council", "construction_site": get_site("Chennai Commercial Hub"),
            "project_type": "Industrial", "contract_value": 1200000,
            "start_date": add_days(today(), 10), "end_date": add_days(today(), 100),
            "project_manager": "Administrator", "current_phase": "Planning", "status": "Draft"
        }
    ]
    for p in projects:
        if not frappe.db.exists("Project", {"project_code": p["project_code"]}):
            doc = frappe.get_doc({"doctype": "Project", **p})
            doc.insert(ignore_permissions=True)
            if doc.status == "Active":
                doc.submit()

def seed_work_orders():
    projects = frappe.get_all("Project", fields=["name", "construction_site"], limit=3)
    if not projects: return
    
    contractors = frappe.get_all("Contractor", fields=["name", "trade_category"], limit=2)
    if not contractors: return

    for i in range(3):
        p = projects[i % len(projects)]
        c = contractors[i % len(contractors)]
        
        doc = frappe.get_doc({
            "doctype": "Work Order",
            "project": p.name,
            "trade_category": c.trade_category,
            "assigned_contractor": c.name,
            "start_date": add_days(today(), -5),
            "end_date": add_days(today(), 15),
            "description": f"Work Order {i+1} Description",
            "estimated_cost": 50000 * (i+1),
            "status": "In Progress",
            "resources": [
                {
                    "resource_type": "Labour",
                    "description": "General Workers",
                    "quantity": 10,
                    "unit_cost": 1000
                },
                {
                    "resource_type": "Material",
                    "description": "Cement Bags",
                    "quantity": 100,
                    "unit_cost": 400
                }
            ]
        })
        try:
            doc.insert(ignore_permissions=True)
            doc.submit()
        except Exception as e:
            frappe.logger().error(f"Failed to create Work Order: {e}")

def seed_subcontracts():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    contractors = frappe.get_all("Contractor", fields=["name", "trade_category"], limit=2)
    if not projects or not contractors: return

    for i in range(3):
        p = projects[i % len(projects)]
        c = contractors[i % len(contractors)]

        doc = frappe.get_doc({
            "doctype": "Subcontract",
            "project": p.name,
            "contractor": c.name,
            "trade_category": c.trade_category,
            "contract_value": 200000 * (i+1),
            "start_date": add_days(today(), -10),
            "end_date": add_days(today(), 50),
            "status": "Active",
            "milestones": [
                {"milestone_name": "Mobilization", "due_date": add_days(today(), 5), "payment_percentage": 10},
                {"milestone_name": "Mid Completion", "due_date": add_days(today(), 25), "payment_percentage": 40},
                {"milestone_name": "Final Handover", "due_date": add_days(today(), 50), "payment_percentage": 50}
            ]
        })
        try:
            doc.insert(ignore_permissions=True)
            doc.submit()
        except Exception as e:
            frappe.logger().error(f"Failed to create Subcontract: {e}")

def seed_material_requests():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    if not projects: return
    for i in range(4):
        doc = frappe.get_doc({
            "doctype": "Material Request",
            "project": projects[i % len(projects)].name,
            "request_date": today(),
            "required_by": add_days(today(), 7),
            "status": "Pending Approval"
        })
        try:
            doc.insert(ignore_permissions=True)
        except Exception as e:
            pass

def seed_purchase_orders():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    if not projects: return
    suppliers = ["BuildPro Supplies", "Steel Co", "Cement World"]
    for i in range(3):
        doc = frappe.get_doc({
            "doctype": "Purchase Order",
            "project": projects[i % len(projects)].name,
            "supplier": suppliers[i % len(suppliers)],
            "po_date": today(),
            "total_amount": 50000 * (i+1),
            "status": "Approved"
        })
        try:
            doc.insert(ignore_permissions=True)
            doc.submit()
        except Exception as e:
            pass

def seed_site_diaries():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    if not projects: return
    for i in range(4):
        doc = frappe.get_doc({
            "doctype": "Site Diary",
            "project": projects[i % len(projects)].name,
            "diary_date": add_days(today(), -i),
            "site_engineer": "Administrator",
            "weather": "Sunny",
            "workers_on_site": 25 + i,
            "work_carried_out": f"Routine site works day {i}",
            "materials_delivered": "100 bags cement" if i % 2 == 0 else ""
        })
        try:
            doc.insert(ignore_permissions=True)
        except Exception as e:
            pass

def seed_quality_inspections():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    if not projects: return
    for i in range(3):
        doc = frappe.get_doc({
            "doctype": "Quality Inspection",
            "project": projects[i % len(projects)].name,
            "inspection_date": today(),
            "inspector": "Administrator",
            "inspection_type": "Routine",
            "overall_result": "Pass" if i != 2 else "Fail",
            "checklist": [
                {"item": "Structural Strength", "result": "Pass"},
                {"item": "Electrical Safety", "result": "Pass" if i != 2 else "Fail"}
            ]
        })
        try:
            doc.insert(ignore_permissions=True)
            doc.submit()
        except Exception as e:
            pass

def seed_safety_incidents():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    if not projects: return
    for i in range(2):
        doc = frappe.get_doc({
            "doctype": "Safety Incident",
            "project": projects[i % len(projects)].name,
            "incident_date": today(),
            "incident_type": "Near Miss" if i == 0 else "First Aid",
            "severity": "Low",
            "description": f"Minor safety incident {i}",
            "status": "Open"
        })
        try:
            doc.insert(ignore_permissions=True)
            # Submit only if it was designed to be submittable and we want it closed, but keep it open
        except Exception as e:
            pass

def seed_progress_claims():
    projects = frappe.get_all("Project", fields=["name"], limit=2)
    if not projects: return
    for i in range(2):
        doc = frappe.get_doc({
            "doctype": "Progress Claim",
            "project": projects[i % len(projects)].name,
            "claim_date": today(),
            "claim_period_from": add_days(today(), -30),
            "claim_period_to": today(),
            "gross_claim": 100000,
            "completion_percentage": 20,
            "status": "Approved"
        })
        try:
            doc.insert(ignore_permissions=True)
            doc.submit()
        except Exception as e:
            pass

def get_site(name):
    site = frappe.get_value("Construction Site", {"site_name": name})
    return site

