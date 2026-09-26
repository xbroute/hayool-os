> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Industry Pack Architecture & Capability Matrix
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping

---

## 1. Why packs

The platform must be broad without forcing one giant UI/domain model on every customer.

Universal kernel handles reusable primitives.

Industry packs add:
- objects
- workflows
- terminology
- dashboards
- AI agents
- reports
- integrations
- compliance policies
- templates.

---

## 2. Maturity levels

### KERNEL
Universal capability production-grade.

### STARTER
Usable industry template built from universal capability.

### VERIFIED
Tested with design partners in that industry.

### CERTIFIED/REGULATED
Requires formal industry/regulatory readiness.

### PARTNER
Delivered through certified partner/integration.

### FUTURE
Architectural extension point only.

Marketing must show the true maturity level.

---

## 3. V1 cross-industry kernel

V1 platform kernel should include:
- identity/tenancy
- CRM
- sales/order
- procurement
- finance
- HR/ATS/talent
- projects/work
- documents
- forms/workflows
- approval
- inventory baseline
- assets/maintenance baseline
- service/ticket/case
- website/CMS/eCommerce baseline
- marketing
- analytics
- AI/automation
- localization
- Studio/custom objects
- integration SDK
- marketplace/provider registry.

---

## 4. Initial first-party packs

### Professional Services / Software / Agency — VERIFIED TARGET
- lead/project intake
- proposals/contracts
- project delivery
- talent
- time
- profitability
- recurring service
- support
- client portal
- marketing.

### Retail / eCommerce — STARTER
- catalog
- price
- sales
- POS
- inventory
- promotion
- website
- delivery
- returns.

### Wholesale / Distribution — STARTER
- procurement
- supplier
- sales orders
- warehouses
- lots
- transfer
- carrier
- receivable/payable.

### Field Service / Repair — STARTER
- assets
- service requests
- dispatch
- technician
- parts
- SLA
- customer signoff
- invoice.

### Light Manufacturing — STARTER
- BOM
- routing
- production order
- material consumption
- output
- QC
- maintenance.

### Agriculture / Food — STARTER/BETA
- farm/field
- crop cycle
- inputs
- harvest
- lot/expiry
- traceability
- storage
- delivery.

### Generic Enterprise Operations — STARTER
- HR
- procurement
- assets
- projects
- service management
- documents
- approvals.

---

## 5. Expansion packs

Architectural targets:

- construction/project contracting
- hospitality
- education/training
- healthcare operations
- banking/financial-services operations
- insurance operations
- public sector
- nonprofit
- real estate/property management
- fleet/transport
- energy/utilities
- maintenance-intensive industry
- professional/legal/accounting firms
- franchise/multi-branch businesses.

These should reuse kernel objects before inventing new ones.

---

## 6. Regulated core systems boundary

Do not advertise starter packs as replacing specialized systems requiring deep certification.

Examples:
- core banking
- clinical EHR
- pharmacy dispensing
- medical device control
- industrial safety control
- air traffic control.

Hayool may orchestrate/integrate around them until a separate verified product exists.

---

## 7. Pack Builder

Hayool Studio + AI can generate a tenant-specific pack from discovery.

Example:
"car detailing company"
→ Customer
→ Vehicle
→ Service package
→ Appointment
→ Work order
→ Technician
→ Consumables
→ Invoice
→ Follow-up.

AI starts from reusable templates instead of inventing an entirely custom app every time.

---

## 8. Pack economics

Packs may be:
- included in plan
- premium module
- one-time implementation
- subscription
- partner marketplace item.

Track support burden and upgrade compatibility per pack.

---

## 9. Pack certification

First-party/partner pack release checklist:
- UX
- permission
- tenant isolation
- data model
- migration
- export
- automation
- localization
- security
- test coverage
- supported versions
- docs
- rollback
- licensing.

Regulated packs require additional compliance evidence.


## 10. Pack ownership

A Pack may be:
- first-party
- certified partner
- community
- private tenant
- regulated specialist.

Hayool does not need to first-party implement every Pack.

## 11. Complex/regulated systems

A specialist developer/partner may build highly complex systems on Hayool using public extension boundaries and their own remote services/data stores.

Examples:
- specialized clinical workflow
- specialized banking module
- industrial engineering app.

The Marketplace must accurately state who owns compliance/certification.

Technical extensibility is broader than Hayool's first-party product claims.

