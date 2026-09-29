# Hayool OS — Universal Business Kernel, Studio & Extension Platform
Version: 6.0
Status: Canonical architecture
Purpose: Make Hayool OS broadly adaptable without turning the core into an unmaintainable generic database

---

## 1. Product principle

Hayool OS must be capable of serving radically different businesses while preserving a coherent, upgradeable core.

The correct model is:

**Strong typed universal kernel + modular domain packs + governed customization + extension SDK.**

Do NOT attempt to encode every future industry directly into the core.

Do NOT make the core a free-form EAV database.

Do NOT force every tenant to see every module.

---

## 2. Universal kernel concepts

The kernel defines stable concepts reusable across industries.

### Identity / Party
- Person
- Organization
- Household where a pack needs it
- Membership
- Role
- Relationship
- Contact Point

### Organization
- Tenant
- Legal Entity
- Branch
- Department
- Team
- Cost Center
- Profit Center
- Business Unit

### Place
- Address
- Geo Point
- Service Area
- Site
- Facility
- Store
- Warehouse
- Farm/Field through industry extension
- Work Center through industry extension

### Offer / Catalog
- Product
- Service
- Bundle
- Variant
- Price List
- Offer
- Availability
- Terms

### Resource
- Human
- Team
- Vendor
- Asset
- Equipment
- Vehicle
- Inventory
- Digital Worker
- Deterministic Automation
- Capacity

### Work
- Goal
- Capability
- Process
- Work Unit
- Project
- Task
- Service Request
- Case
- Job
- Work Order
- Assignment
- Deliverable
- Outcome

### Commercial transaction
- Intent / Request
- Requirement
- Quote
- Bid/Offer where allowed
- Contract
- Order
- Commitment
- Fulfillment
- Shipment
- Delivery
- Return
- Refund
- Dispute

### Finance
- Monetary Amount
- Currency
- Financial Event
- Invoice
- Payment
- Settlement
- Journal
- Budget
- Cost
- Revenue
- Tax determination result

### Physical flow
- Item
- Stock Unit
- Lot/Batch
- Serial
- Container
- Movement
- Transformation
- Measurement
- Condition
- Custody

### Knowledge / content
- Document
- Attachment
- Content Item
- Page
- Conversation
- Meeting
- Decision
- Requirement
- Evidence

### Governance
- Policy
- Approval
- Rule Version
- Autonomy Policy
- Permission
- Data Classification
- Retention Policy
- Jurisdiction Profile

### Time
- Schedule
- Availability
- Reservation
- Calendar
- SLA
- Recurrence

### Device/event
- Device
- Sensor
- Telemetry Event
- Business Event
- Integration Event

---

## 3. Typed core vs extension data

Core financial, security, tenant, identity and high-volume operational entities must be strongly modeled.

Tenant-specific customization is handled through an Extension Data Platform.

Permitted extension strategies include:
- versioned custom fields on approved core entities;
- custom object definitions;
- typed relationships;
- forms/views;
- computed fields;
- validation;
- controlled JSON-schema-backed flexible attributes;
- materialized/indexed projections for heavy queries.

The implementation team must select the physical storage strategy through an ADR.

Rules:
- no unvalidated arbitrary blobs for important business data;
- custom objects must have schema/version/permission/audit;
- core domain invariants cannot be bypassed through a custom object;
- extension data must export/import cleanly;
- indexes/search policies must be configurable;
- migration/rollback must be supported.

---

## 4. Hayool Studio

Hayool Studio is a first-class V1 capability.

Authorized tenant admins/builders can customize without coding.

Studio capabilities:

### Data
- create custom object
- create custom field
- relationship
- enum/choice
- validation
- formula/computed value
- indexes/searchability where allowed

### UX
- forms
- lists
- kanban
- calendar
- map
- dashboard
- detail page layout
- portal page
- quick actions
- mobile action layout

### Process
- workflow
- approval
- trigger/action automation
- SLA
- notification
- scheduled job
- form/intake flow

### Intelligence
- AI assistant configuration
- agent/tool binding
- decision policy selection
- report/metric
- knowledge source

### Documents
- PDF/report template
- email/SMS template
- contract/doc template

---

## 5. AI App Builder

A user may describe:

> "I run a repair shop. I need customers, devices, repair tickets, parts, technician assignments, warranties, invoices and SMS notifications."

AI App Builder proposes:

- domain objects;
- fields;
- relationships;
- roles;
- forms;
- workflows;
- dashboards;
- reports;
- permissions;
- automations.

It creates a **Draft Solution**, never silently mutating production configuration.

Lifecycle:

Describe
→ Generate Draft
→ Preview
→ Validate
→ Simulate/Test
→ Admin Review
→ Publish
→ Observe
→ Rollback if needed.

---

## 6. Solution Package

All customizations are packaged.

A Solution Package may contain:
- custom objects
- custom fields
- UI definitions
- workflows
- reports
- dashboards
- permissions
- templates
- translations
- agent configuration
- connector bindings
- seed/reference data

Lifecycle:
Draft → Test → Approved → Published → Deprecated → Retired.

Packages are:
- versioned;
- dependency-aware;
- exportable;
- importable;
- tenant-scoped;
- digitally signed for marketplace distribution.

---

## 7. Extension SDK

For requirements Studio cannot satisfy, provide a pro-code SDK.

Extension points:
- UI slot
- backend capability
- event subscriber
- workflow activity
- provider adapter
- report function
- AI tool
- validation
- integration connector

Rules:
- stable public APIs only;
- no direct core-table mutation from external extensions;
- declared permissions;
- resource quotas;
- semantic versioning;
- compatibility tests;
- signing/certification for marketplace distribution.

---

## 8. Extension isolation

Third-party extensions MUST NOT:
- access another tenant;
- access secrets directly;
- bypass authorization;
- mutate posted financial journals;
- alter payroll/tax policy without approved APIs;
- execute unrestricted system commands;
- load arbitrary JS into another tenant's session.

Use capability-based permissions and sandboxing appropriate to deployment model.

---

## 9. Module Registry

Every module declares:
- ID
- version
- dependencies
- migrations
- permissions
- entitlements
- navigation
- events
- APIs
- UI capabilities
- country/industry restrictions
- install/uninstall behavior
- upgrade compatibility.

Admin can enable/disable modules according to entitlement and dependency rules.

Disabling a module does not silently destroy data.

---

## 10. Capability Pack Marketplace

Future commercial marketplace supports:
- industry packs;
- country packs;
- workflow packs;
- connector packs;
- AI agents;
- report packs;
- website themes;
- assessment packs;
- document packs.

Hayool may:
- publish first-party packs;
- certify partners;
- revenue-share;
- enforce security/license review.

This is a strategic ecosystem business, not a V1 dependency for correctness.

---

## 11. Personalization hierarchy

Configuration precedence:

Platform safe defaults
→ deployment policy
→ country/industry mandatory policy
→ tenant policy
→ legal entity/branch
→ role/workspace
→ user preference.

Tenant configuration cannot weaken mandatory security/legal controls.

---

## 12. Customization debt control

Customization is a product risk.

Track:
- number of custom objects;
- overridden screens;
- custom workflows;
- external extensions;
- deprecated APIs;
- upgrade impact.

Provide an Upgrade Readiness report.

---

## 13. No-code does not mean no governance

Studio changes affecting:
- finance;
- payroll;
- permission;
- external payment;
- regulated workflow;
- production data deletion

must go through approval/testing policy.

For important changes:
Draft → Test environment → Publish.

---

## 14. Competitive design principle

The target is the adaptability of platforms such as Odoo Studio, Microsoft Dataverse/Power Apps and ServiceNow App Engine, while retaining a stronger integrated Work/Resource/AI/Finance model and first-class Cloud/Dedicated/On-Prem deployment.

Do not copy their internal designs blindly.

---

## 15. V1 acceptance

V1 must have:
- custom fields;
- basic custom objects;
- forms/views;
- workflow/approval builder;
- dashboard/report builder;
- solution package versioning;
- safe publish/rollback;
- permission/audit;
- AI-assisted draft builder.

V1 must include the extension/registry foundations required for community and partner development. Public commercial marketplace rollout may be phased by security/certification maturity, but developer extensibility itself is not deferred.


## 16. Extension platform relationship

Detailed pro-code and marketplace behavior is canonical in:

`docs/platform/DEVELOPER_PLATFORM_EXTENSION_RUNTIME_MARKETPLACE_SPEC.md`

Studio and Developer Platform are two paths over the same governed capability model.

No-code customizations and pro-code extensions should share:
- permissions
- solution/package lifecycle
- audit
- versioning
- compatibility rules
- dependency metadata.

## 17. Builder escalation path

When a tenant request cannot be solved in Studio:

1. search existing Marketplace/registry;
2. propose compatible app/pack;
3. allow Capability Request;
4. allow private developer app;
5. consider first-party Core only if broadly justified.

The Core roadmap is not the only path to customer-specific capability.

