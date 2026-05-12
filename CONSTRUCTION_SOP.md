# 📘 ConstructionOS — Standard Operating Procedure (SOP)
### Functional Guide for Enterprise Construction Operations

---

> **Document Version:** 1.0  
> **Application:** ConstructionOS on ERPNext v15  
> **Audience:** Project Managers, Site Engineers, Procurement Officers, Safety Officers, Finance Teams  
> **Support:** support@constructionos.io

---

## 📋 Table of Contents

1. [Getting Started — First Login](#1-getting-started--first-login)
2. [Module 1 — Project Management](#2-module-1--project-management)
3. [Module 2 — Site Management](#3-module-2--site-management)
4. [Module 3 — Contractor & Subcontractor Management](#4-module-3--contractor--subcontractor-management)
5. [Module 4 — Procurement & Materials](#5-module-4--procurement--materials)
6. [Module 5 — Quality Control](#6-module-5--quality-control)
7. [Module 6 — Safety Management](#7-module-6--safety-management)
8. [Module 7 — Billing & Progress Claims](#8-module-7--billing--progress-claims)
9. [Module 8 — Reports & Analytics](#9-module-8--reports--analytics)
10. [Daily / Weekly / Monthly Operational Checklist](#10-daily--weekly--monthly-operational-checklist)
11. [User Roles & Responsibilities](#11-user-roles--responsibilities)
12. [Frequently Asked Questions](#12-frequently-asked-questions)
13. [Support & Contact](#13-support--contact)

---

## 1. Getting Started — First Login

### 1.1 Access the Application

1. Open your browser and navigate to your ConstructionOS URL:  
   `https://construction.yourcompany.com`
2. Login with your ERPNext credentials provided by the IT department.
3. On the left sidebar, locate and click the **Construction** workspace.
4. You will land on the **Construction Dashboard** showing 4 critical KPIs:
   - 🏗️ Active Projects by Phase
   - 📈 Monthly Progress Trend
   - 💰 Project Cost vs Budget
   - 🛒 Procurement Spend Analysis

---

### 1.2 Initial System Setup (One-Time — Admin Only)

> **Who does this:** System Administrator or Operations Head

| Step | Action | Navigation Path |
|---|---|---|
| 1 | Create Construction Sites | Construction → Masters → Construction Site |
| 2 | Define Construction Phases | Construction → Masters → Construction Phase |
| 3 | Setup Trade Categories | Construction → Masters → Trade Category |
| 4 | Configure Workflows | Setup → Workflow → Workflow List |
| 5 | Load BOQ Templates | Construction → Project Management → BOQ Item |

---

### 1.3 Assign User Roles

> **Who does this:** Administrator

Assign the following roles to team members via **Users → [User Name] → Roles**:

| Role | Responsibility |
|---|---|
| **Construction Project Manager** | Overall project health, budget approvals, and scheduling. |
| **Site Engineer** | Daily site logs, progress updates, and resource allocation. |
| **Construction Procurement Officer** | Material requests, PO generation, and supplier management. |
| **QA/QC Inspector** | Quality checks, checklist validation, and snag lists. |
| **Safety Officer** | Incident reporting, safety audits, and PPE compliance. |
| **Finance Manager** | Progress claims, retention tracking, and cost analysis. |

---

## 2. Module 1 — Project Management

> **Purpose:** Centralize project execution, from planning and milestone setting to real-time progress tracking and budget management.

---

### 2.1 SOP — Create a New Construction Project

**Who:** Project Manager  
**When:** Upon contract award or project initiation

| Step | Action |
|---|---|
| 1 | Navigate to **Construction → Project → + New** |
| 2 | Enter **Project Name** and unique **Project Code** |
| 3 | Link the **Client** (Customer) and **Construction Site** |
| 4 | Select **Project Type** (Residential/Commercial/Industrial) |
| 5 | Set **Start Date**, **End Date**, and **Contract Value** |
| 6 | Assign the **Project Manager** |
| 7 | Enter the **Total Budget** (defaults to Contract Value if not specified) |
| 8 | **Save** and **Submit** |

✅ **Expected Result:** Project status moves to "Active". A Project Cost Centre is automatically created in Accounting.

---

### 2.2 SOP — Milestone & Phase Management

**Who:** Project Manager / Site Engineer  
**When:** During project planning or phase transitions

1. Open the **Project** record.
2. Navigate to the **Phases** section (linked to Construction Phases).
3. Set the **Current Phase** (e.g., Foundation, Structure, Fit-Out).
4. Update the **Completion Percentage** manually or allow the system to auto-calculate based on Work Orders.

---

### 2.3 SOP — Manage Project Budgets

**Who:** Project Manager / Finance Manager  
**When:** Monthly review or when variation orders are issued

| Step | Action |
|---|---|
| 1 | Open the **Project** record |
| 2 | Review **Actual Cost to Date** vs **Total Budget** |
| 3 | If variance exceeds 10%, a system warning will appear |
| 4 | To update budget, create a **Budget Revision** (via custom action) |

> **Warning:** System prevents submission of transactions that exceed the allocated project budget by more than 15% without PM override.

---

## 3. Module 2 — Site Management

> **Purpose:** Track daily on-site activities, weather conditions, workforce attendance, and visitor logs to maintain a digital "Black Box" of site operations.

---

### 3.1 SOP — Create a Site Diary (Daily Log)

**Who:** Site Engineer  
**When:** Daily (End of shift)

| Step | Action |
|---|---|
| 1 | Go to **Construction → Site Diary → + New** |
| 2 | Select the **Project** (Date defaults to today) |
| 3 | Choose **Weather** condition (Sunny/Rainy/etc.) |
| 4 | Enter **Workers on Site** (total count) |
| 5 | Use **Work Carried Out** (Rich Text) to detail daily progress |
| 6 | Note **Materials Delivered** and **Issues Encountered** |
| 7 | Attach **Photos** of the site progress |
| 8 | **Save** |

✅ **Expected Result:** Site Diary appears in the Project dashboard. Daily summary email is sent to the Project Manager.

---

### 3.2 SOP — Track Site Visitors

**Who:** Site Engineer / Security  
**When:** Any external party visits the site

1. Open the **Site Diary** for the day.
2. In the **Visitors** field, record Name, Organization, and Purpose of visit.
3. Save the record.

---

## 4. Module 3 — Contractor & Subcontractor Management

> **Purpose:** Manage vendor onboarding, subcontract agreements, trade mapping, and performance evaluation.

---

### 4.1 SOP — Onboard a New Contractor

**Who:** Procurement Officer / Contractor Coordinator  
**When:** Before issuing any work order or subcontract

| Step | Action |
|---|---|
| 1 | Go to **Construction → Contractor → + New** |
| 2 | Enter **Contractor Name** and **Contractor Type** (Main/Sub/Specialist) |
| 3 | Link **Trade Category** (e.g., Civil Works, Electrical) |
| 4 | Enter **Insurance Policy No** and **Insurance Expiry** |
| 5 | Attach Registration and Tax documents |
| 6 | **Save** |

> **Tip:** System will flag contractors with expired insurance during the Subcontract creation process.

---

### 4.2 SOP — Create a Subcontract Agreement

**Who:** Project Manager / Procurement Officer  
**When:** After tender finalization

| Step | Action |
|---|---|
| 1 | Navigate to **Construction → Subcontract → + New** |
| 2 | Select **Project**, **Contractor**, and **Trade Category** |
| 3 | Enter **Contract Value** and **Retention Percentage** (default 5%) |
| 4 | Define **Scope of Work** in the editor |
| 5 | In the **Milestones** table, add payment stages (Name, Due Date, Payment %) |
| 6 | **Save** and **Submit** |

✅ **Expected Result:** Subcontract status becomes "Active". Milestone alerts are scheduled for the PM.

---

## 5. Module 4 — Procurement & Materials

> **Purpose:** Streamline the construction supply chain — from site requests to purchase orders and goods receipt.

---

### 5.1 SOP — Raise a Material Request

**Who:** Site Engineer  
**When:** Materials are needed for upcoming work orders

| Step | Action |
|---|---|
| 1 | Go to **Construction → Material Request → + New** |
| 2 | Link the **Project** and **Work Order** |
| 3 | Add items, quantities, and required by date |
| 4 | **Save** and **Submit** |

---

### 5.2 SOP — Generate and Approve Purchase Orders

**Who:** Procurement Officer (Create) / Project Manager (Approve)  
**When:** After vendor selection

| Step | Action |
|---|---|
| 1 | Open the **Material Request** → Click **Create → Purchase Order** |
| 2 | Select the **Supplier** and verify rates |
| 3 | **Save** (Status: Draft) |
| 4 | Click **Submit for Approval** (Status: Pending Approval) |
| 5 | PM reviews and clicks **Approve** (Status: Approved) |

✅ **Expected Result:** PO is emailed to the supplier. Inventory ledger is updated with "Ordered Quantity".

---

## 6. Module 5 — Quality Control

> **Purpose:** Ensure all construction work meets technical specifications via standardized inspections and defect tracking.

---

### 6.1 SOP — Execute a Quality Inspection

**Who:** QA/QC Inspector  
**When:** Upon completion of a work order phase or milestone

| Step | Action |
|---|---|
| 1 | Go to **Construction → Quality Inspection → + New** |
| 2 | Link **Project** and **Work Order** |
| 3 | Select **Inspection Type** (Pre-pour/Structural/Finishes) |
| 4 | Fill the **Checklist Items** table (Pass/Fail/NA) |
| 5 | Set **Overall Result** (Pass/Fail/Conditional Pass) |
| 6 | Attach **Photos** of inspected work |
| 7 | **Save** and **Submit** |

✅ **Expected Result:** If "Fail", a snag list is generated. If "Pass", the linked Work Order can be marked as "Completed".

---

## 7. Module 6 — Safety Management

> **Purpose:** Maintain a Zero-Harm environment by logging incidents, conducting toolbox talks, and enforcing PPE compliance.

---

### 7.1 SOP — Report a Safety Incident

**Who:** Safety Officer / Site Engineer  
**When:** Immediately after any incident or near-miss

| Step | Action |
|---|---|
| 1 | Go to **Construction → Safety Incident → + New** |
| 2 | Select **Project** and **Incident Date/Time** |
| 3 | Choose **Incident Type** (Near Miss/Lost Time Injury/etc.) |
| 4 | Describe the incident and identify the **Root Cause** |
| 5 | Specify **Corrective Action** taken |
| 6 | Tick **Reported to Authorities** if applicable |
| 7 | **Save** and **Submit** |

> **Critical:** Serious incidents (LTI/Fatality) trigger an immediate high-priority email alert to the Operations Head.

---

## 8. Module 7 — Billing & Progress Claims

> **Purpose:** Manage client billing through progress claims, retention handling, and payment reconciliation.

---

### 8.1 SOP — Submit a Progress Claim

**Who:** Project Manager / Finance Manager  
**When:** Monthly billing cycle (e.g., 25th of each month)

| Step | Action |
|---|---|
| 1 | Go to **Construction → Progress Claim → + New** |
| 2 | Select the **Project** and **Claim Period** |
| 3 | Enter **Completion % to Date** |
| 4 | System calculates **Gross Claim** and **Net Claim** (Less Previous Claims) |
| 5 | System auto-deducts **Retention Amount** |
| 6 | **Save** and **Submit** for Client approval |

✅ **Expected Result:** Progress Claim PDF is generated. Once approved, it can be converted to a Sales Invoice.

---

## 9. Module 8 — Reports & Analytics

> **Purpose:** Data-driven decision making using real-time project metrics.

### 9.1 Key Operational Reports

| Report | Data Provided | Use Case |
|---|---|---|
| **Project Cost Analysis** | Contract vs Budget vs Actual | Financial Health Check |
| **Resource Utilization** | Labour & Equipment hours | Efficiency Monitoring |
| **Safety Incident Report** | Incident frequency & severity | Compliance Audit |
| **Budget vs Actual** | Line-item variance tracking | Cost Control |

---

## 10. Daily / Weekly / Monthly Operational Checklist

### 10.1 Daily (15 minutes)

| Task | Who | Where |
|---|---|---|
| ☐ Submit Site Diary | Site Engineer | Site Diary |
| ☐ Approve urgent Purchase Orders | PM | Purchase Order |
| ☐ Log Safety Toolbox Talk | Safety Officer | Safety Log |

### 10.2 Weekly (1 hour)

| Task | Who | Where |
|---|---|---|
| ☐ Review Work Order progress | PM | Work Order |
| ☐ Conduct Site Quality Audit | QA/QC | Quality Inspection |
| ☐ Update Project Completion % | PM | Project |

### 10.3 Monthly (Half Day)

| Task | Who | Where |
|---|---|---|
| ☐ Generate Progress Claims | Finance | Progress Claim |
| ☐ Review Budget Overruns | PM | Cost Analysis Report |
| ☐ Contractor Performance Rating | PM | Contractor |

---

## 11. User Roles & Responsibilities

| DocType | Project Manager | Site Engineer | Procurement | QA/QC | Safety |
|---|---|---|---|---|---|
| **Project** | ✅ CRUD + S | 👁️ Read | 👁️ Read | 👁️ Read | 👁️ Read |
| **Work Order** | ✅ CRUD + S | ✅ CRUD + S | 👁️ Read | 👁️ Read | ❌ |
| **Site Diary** | 👁️ Read | ✅ CRUD | ❌ | ❌ | ❌ |
| **Purchase Order** | ✅ Approve | 👁️ Read | ✅ CRUD + S | ❌ | ❌ |
| **Quality Insp.** | 👁️ Read | 👁️ Read | ❌ | ✅ CRUD + S | ❌ |
| **Safety Incident**| 👁️ Read | ✅ Create | ❌ | ❌ | ✅ CRUD + S |

---

## 12. Frequently Asked Questions

**Q1: How is Project Completion % calculated?**  
A: It is a weighted average of all submitted Work Orders linked to the project. You can override this manually in the Project record.

**Q2: I can't submit a Purchase Order. Why?**  
A: Check if the PO exceeds the project budget. If it does, you need a PM approval or a budget revision. Also, ensure the Vendor is marked as "Approved".

**Q3: How do I handle a failed quality inspection?**  
A: Mark the inspection as "Fail", describe the snags, and assign a new Work Order to the contractor to rectify the issue. Re-inspect once the new Work Order is completed.

**Q4: Where do I see the Retention balance for a contractor?**  
A: Go to the **Subcontract** record. The **Amount Retained** field shows the total retention held across all progress claims for that contract.

---

## 13. Support & Contact

- **Technical Support:** it-support@constructionos.io
- **Process Queries:** operations-help@constructionos.io
- **Emergency Safety Hotline:** +91-99999-SAFETY

---
*Created with ❤️ for the Construction Industry by the ERPNext v15 Team.*
