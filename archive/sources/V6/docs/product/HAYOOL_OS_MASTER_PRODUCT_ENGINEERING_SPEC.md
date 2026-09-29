# Hayool OS — Master Product & Engineering Specification
Version: 6.0
Status: Canonical Product & Engineering Source of Truth
Primary launch locale: Iran / fa-IR + en
Product owner: Hayool

---

# 0. Execution Contract

This specification defines the product boundary.

Implementation agents MUST also obey:
- `CLAUDE.md`
- `AGENTS.md`
- `docs/engineering/AI_ENGINEERING_CONSTITUTION.md`
- `docs/engineering/ENGINEERING_GUARDRAILS.md`
- `docs/engineering/AUTONOMOUS_SDLC_CONTROL_PLANE_SPEC.md`

When behavior changes:
REQ first.

Architecture changes:
ADR first.

No chat-only requirement is authoritative.

# 1. Product Definition

Hayool OS is:

> An AI-native extensible Business Operating Platform that converts intent and business goals into structured work/transactions, coordinates the right people + AI + suppliers + assets, executes outcomes, manages economics, and lets customers/community developers add new industries and capabilities without modifying the protected core.

Hayool OS is NOT positioned merely as:
- ERP
- ATS
- freelancer marketplace
- project manager
- AI chatbot.

Those are subsystems.

# 2. Product Loops

## 2.1 Business loop
Goal
→ Capability
→ Work
→ Workforce
→ Execution
→ Finance
→ Outcome
→ Learning.

## 2.2 Client project loop
Lead
→ Discovery
→ Requirements
→ Scope
→ Estimate
→ Price
→ Contract
→ Project
→ Team
→ Delivery
→ Acceptance
→ Invoice
→ Collection
→ Support
→ Retrospective.

## 2.3 Workforce loop
Need
→ Work/position design
→ Source
→ Screen
→ Assess
→ Select
→ Engage
→ Onboard
→ Assign
→ Observe outcomes
→ Grow/remediate/reassign.

## 2.4 Product intelligence loop
Decision
→ Action
→ Outcome
→ Evidence
→ Evaluation
→ Candidate policy
→ Shadow
→ Promotion.

# 3. Market Wedge

Initial ICP:
project-based digital/professional service companies.

Examples:
software, web/mobile, AI, design, branding, marketing, SEO, consulting, implementation.

Architecture remains extensible to other verticals.

Do not broaden commercial positioning before retention in initial ICP.

# 4. Core Domain Model

## 4.1 Organization
Tenant
→ Legal Entity
→ Branch
→ Department
→ Team
→ Cost Center.

## 4.2 Work Graph
Goal
→ Capability
→ Process
→ Work Unit
→ Skill/Constraint
→ Execution Strategy
→ Resource
→ Assignment
→ Outcome.

Detailed source:
`docs/data/WORK_GRAPH_AND_CAPABILITY_ONTOLOGY_SPEC.md`

## 4.3 Resource types
- employee
- candidate
- freelancer
- contractor
- internal team
- managed team
- external vendor/company
- digital worker / AI agent
- deterministic automation.

Human and digital resources share planning concepts but NEVER share legal/personhood semantics.

# 5. Architecture Principles

1. Modular monolith first.
2. PostgreSQL authoritative relational core.
3. Multi-tenant from first migration.
4. Cloud/Dedicated/On-Prem from one codebase.
5. API/application-service boundaries.
6. AI behind provider-neutral control plane.
7. Decision intelligence behind provider-neutral interface.
8. Deterministic authority for money, permission and legal state.
9. Durable workflows for long-running business processes.
10. Auditability.
11. Versioned rules.
12. Explainability.
13. Privacy/data minimization.
14. Progressive complexity: introduce additional databases/services only on evidence.

# 6. Preferred V1 Technical Direction

M0 validates current stable versions/licenses.

Preferred:
- TypeScript monorepo
- Next.js web applications
- NestJS backend
- PostgreSQL
- Valkey
- Temporal
- S3-compatible object storage
- OpenBao-compatible secret management
- OpenTelemetry
- self-hosted LLM observability behind adapter
- Engineering/Product AI Gateways
- Docker Compose
- Ubuntu LTS
- GitHub.

Avoid defaulting to:
- Kubernetes
- graph DB
- data lake
- custom ML serving cluster
before measured need.

Search:
prefer PostgreSQL capabilities initially; evaluate dedicated search only when needed.

Vectors:
prefer minimal provider-neutral strategy; pgvector may be evaluated before adding another datastore.

Analytics:
begin with read models/replica-friendly queries; move heavy analytics to columnar warehouse when justified.

# 7. Deployment Modes

## Hayool Cloud
Managed multi-tenant SaaS.

## Dedicated Cloud
Tenant-isolated managed deployment.

## On-Premise
Customer-controlled deployment.

Optional central connector:
- outbound-only where possible
- licensing/update/network
- explicit consent
- no direct central DB access.

On-Prem may disable:
- Shared Network
- external AI
- telemetry.

Core product must remain functional.

# 8. Identity and Access

Global identity may have multiple tenant memberships.

Actors:
- platform admin
- tenant owner
- CEO/manager
- finance
- HR/recruiter
- PM
- sales
- marketer
- employee
- freelancer
- contractor
- candidate
- client
- support
- auditor
- service identity
- AI agent identity.

Use RBAC + contextual policy where needed.

Server-side authorization mandatory.

Prepare for:
- MFA
- OIDC
- SAML
- SCIM
depending plan/enterprise maturity.

# 9. Workforce Architect

Conversationally discover:
- business model
- goals
- processes
- current team
- workload
- constraints
- budget
- growth
- physical presence
- security/compliance.

Generate:
- capability map
- work inventory
- gaps
- org/team scenarios
- positions/work packages
- Build/Buy/Automate/Hire
- human/AI mix
- cost/capacity/time/risk.

Manager can edit all outputs.

No automated organizational restructuring without approved policy.

# 10. Talent Network

Structured profile:
- skills
- evidence
- portfolio
- experience
- availability
- desired engagement
- rates/salary expectations
- assessments
- project history
- performance dimensions
- languages/location.

PDF resume is import/export, not primary truth.

Private tenant pools + optional Hayool Shared Network.

Shared data is explicit and governed.

# 11. Grade and Skill

Separate:
Professional Grade
from
per-skill proficiency.

Grade reflects:
autonomy, scope, reliability, communication, leadership, maturity.

Skill reflects actual competence in a specific area.

Changes are evidence-backed and auditable.

# 12. Recruiting / ATS

Pipeline:
Application
→ screening
→ AI/structured clarification
→ assessment
→ interview
→ shortlist
→ offer
→ engagement/onboarding.

AI conversational interviews supported.

Use structured rubrics/evidence.

No unexplained single AI score.

High-impact hiring decisions default to human review.

Country policy may further restrict automation.

# 13. Managed Marketplace

No uncontrolled low-price bidding.

Work package visibility:
- Direct Invite
- Invite Pool
- Network Open.

Talent applies against platform compensation corridor.

Client price hidden from unauthorized talent.

Talent compensation hidden from unauthorized client.

Detailed Trust/Safety:
`docs/product/TRUST_SAFETY_AND_MARKETPLACE_INTEGRITY_SPEC.md`

# 14. Matching / Team Builder

Matching is:
constraints first
→ multi-objective ranking/optimization.

Consider:
- skill evidence
- grade
- capacity
- total expected delivery cost
- quality
- reliability
- risk
- team collaboration
- continuity
- growth
- fair exposure/exploration.

Provide scenarios, not merely one score:
- quality optimized
- balanced
- cost/time optimized
- low risk.

Explain why.

# 15. Project Delivery

Entities:
- Portfolio
- Project
- Phase
- Milestone
- Work Package
- Task
- Dependency
- Deliverable
- Acceptance
- Change Request
- Risk
- Issue
- Decision
- Meeting
- Time Entry
- Incident.

Support:
Kanban where useful, timeline, capacity, client visibility, attachments and dependencies.

# 16. Requirements / Source of Truth

Project requirement IDs.
Change Requests.
Acceptance criteria.
Decision records.

Trace:
Requirement
→ Task
→ PR/code where applicable
→ Test
→ Deliverable
→ Acceptance.

Meeting Intelligence may create draft requirements/tasks but must link them to source and approval state.

# 17. Time / Effort

Each task:
- optimistic
- expected
- pessimistic
- confidence
- approved effort
- tracked time
- accepted billable time
- variance reason.

Tracked time is not automatically payable time.

Avoid invasive surveillance by default.

# 18. Capacity / Resource Planning

Track:
- contractual capacity
- availability
- leave
- reservation
- utilization
- future capacity
- overload
- skill scarcity.

Portfolio optimizer considers opportunity cost.

# 19. Pricing Engine

Inputs:
- labor
- review
- QA
- PM
- infrastructure
- AI/tools
- payment cost
- commission
- support
- overhead
- risk
- rework
- contingency.

Support:
- target-margin
- cost-plus
- fixed package
- value component
- hourly
- milestone
- retainer
- recurring
- manual.

Client package scenarios:
Lean / Balanced / Accelerated / Custom.

No hard-coded VAT.

# 20. Compensation Engine

Separate from client pricing.

Support:
- employee
- freelancer fixed
- freelancer hourly
- milestone
- project contractor
- retainer
- commission
- hybrid.

Outputs:
- floor
- recommended
- max without approval
- rationale.

Inputs:
Grade, skill, difficulty, standard effort, scarcity, urgency, evidence, law/company fair-rate policy.

No public underbidding auction.

# 21. Rate Book

Versioned by:
country/currency/tenant/skill/grade/engagement/effective date.

Store:
- internal cost
- compensation band
- billable rate
- fair/legal floors.

Historical data retains policy version.

# 22. Continuous Workforce Intelligence

Evaluate work-relevant evidence.

No universal opaque worker score.

Dimensions + uncertainty + sample size + recency + evidence.

Normalize for context/task difficulty where material.

Remediation before replacement when appropriate.

Employee termination protected by default.

# 23. Engagement Modes

Explicit:

A. Software Only
B. Marketplace / Introduction
C. Managed Contractor
D. Managed Team / Outcome
E. EOR/AOR where legally enabled.

Store:
- legal counterparty
- payer/payee
- tax responsibility
- benefits/insurance responsibility
- jurisdiction
- IP/confidentiality
- invoice/payment path
- dispute path.

# 24. HR

- employee file
- org position
- contract
- grade
- salary
- benefits
- leave
- attendance integration
- reviews
- performance
- training
- OKR
- offboarding.

Sensitive permissions required.

# 25. Payroll

Rule/version driven.

Iran country pack first.

Never encode yearly rules irreversibly in domain logic.

Payroll run:
reproducible, reviewable, deterministic, accounting-posted.

# 26. CRM / Sales

- leads
- contacts
- companies
- opportunities
- activity
- follow-up
- proposals
- quote
- client lifecycle
- attribution.

Client 360:
projects, contracts, tickets, finance, services, assets, docs, conversations, health, profitability.

# 27. Service Package Builder / Discounts

Packages:
- service
- add-ons
- limits
- support
- SLA
- recurring items
- target margin.

Discount guardrails:
role limits
+ minimum margins
+ exclusions
+ approval.

# 28. Contracts / Documents / Correspondence

Contracts:
client, employee, freelancer, vendor, marketer, NDA, SLA, amendment.

Versioning/approval/signature hooks.

Document center:
version, classification, confidentiality, entity links.

Correspondence:
incoming/outgoing/internal + registry numbering.

# 29. Finance

Real double-entry foundation.

- Chart of Accounts
- journals
- lines
- fiscal periods
- opening/closing
- reversal
- adjustments
- AR/AP
- cash/bank
- cost centers
- project dimensions.

Invariant:
Debit = Credit.

Posted entries not silently edited.

AI may assist classification, never authoritative arithmetic/posting.

# 30. Iran Country Pack

- fa-IR
- RTL
- Jalali UX
- Gregorian canonical timestamps
- IRR authoritative unit
- optional Toman presentation
- national/company identifiers
- Sheba
- postal/mobile
- VAT rules versioned
- payroll rules versioned
- tax-invoice provider abstraction
- Persian document templates.

Current law verified before release.

# 31. Client Portal

- projects
- milestones
- deliverables
- approvals
- CRs
- meetings
- docs
- contracts
- invoices/payments
- recurring services
- tickets/SLA
- exposed assets
- AI assistant.

AI answers grounded in authorized project knowledge and escalates uncertainty.

# 32. Support / SLA / Customer Health

Ticketing with severity, business hours, SLA and escalation.

Customer Health is multi-dimensional:
payment, support, satisfaction, renewal, usage, project stability, profitability.

No opaque single number without components.

# 33. Marketing / Marketer Network

Strategy, campaign, channel, budget, content, SEO, attribution.

Trace:
Campaign
→ Lead
→ Opportunity
→ Contract
→ Collected Revenue
→ Contribution Margin.

Commission Engine policy-based:
collected cash, margin, renewal, milestone, hybrid.

Support clawback.

# 34. Meeting Intelligence

Recording/transcript where lawful/consented.

Transcript
→ Summary
→ Decisions
→ Tasks
→ Requirements
→ Risks
→ Follow-up.

Everything references source meeting.

# 35. Asset / Secret Management

Assets:
domains, hosting, servers, repos, DNS, SSL, licenses, APIs, gateways, AI accounts.

Asset contains secret reference, not raw secret.

AI receives capability, not plaintext credential.

# 36. Business Digital Twin

Simulate:
- org design
- hiring
- outsourcing
- AI agents
- staffing
- project portfolio
- pricing
- marketing
- infrastructure
- cash/margin.

No live mutation until explicit apply/approval.

# 37. AI Control Plane

Product AI Gateway:
- providers
- models
- routing
- budget
- fallback
- usage
- data policy.

Provider types:
OpenAI-compatible, native providers, custom HTTP, local models.

Model registry:
capabilities, context, cost, latency, privacy.

No domain module directly binds to vendor.

# 38. AI Credits

Hayool-owned metering unit.

Track:
provider raw cost
→ platform cost
→ credits charged
→ margin.

Support:
plan included credits, prepaid packs, budget caps, alerts, BYOK.

Do not represent third-party raw credits as Hayool service resale where prohibited.

# 39. AI Agents / Digital Workers

Registry:
- purpose
- owner
- permissions
- tools
- knowledge scope
- model policy
- autonomy
- budget
- SLO
- evaluation
- version.

Examples:
CEO/CFO/PM/Recruiter/Pricing/Sales/Marketing/Support/Developer/QA.

# 40. AI Autonomy

Per action:
Manual
Assist
Approval
Guarded Auto
Full Auto.

Also Shadow Mode.

Protected defaults:
- money movement
- payroll
- final employee hiring/termination
- tax submission
- production deployment
- permission escalation
- destructive deletion
- secret exposure.

Confidence never grants permission.

# 41. Decision Intelligence / Jev

Use Jev for narrow semantic decisions.

Behind:
`DecisionEngineProvider`.

Appropriate:
intent, semantic complexity, risk signal, evidence relevance, support severity, talent-fit components.

Not authoritative:
money, arithmetic, dates, ledger, payroll, VAT, permissions, legal identity.

Persian policies require Persian evaluation.

Thresholds evidence-calibrated.

Provider outage must not break core correctness.

# 42. Knowledge / RAG

Sources:
contracts, requirements, meetings, SOPs, tickets, docs, project knowledge.

ACL before retrieval/context.

No cross-tenant context leakage.

Retrieved content untrusted for tool authority.

# 43. Automation

Durable workflows:
Temporal-compatible preferred architecture.

Support:
retry/backoff
timeouts
signals
human tasks
approval
idempotency
compensation
dead-letter/escalation.

# 44. Integration Hub

Interfaces:
AI, Payment, Bank, SMS, Email, Storage, SourceControl, Calendar, TaxInvoice, Signature, Notification.

Provider-specific logic stays in adapters.

# 45. Payments

Rial/international/crypto providers where lawful.

- verified webhooks
- idempotency
- reconciliation
- refund
- settlement.

Do not implement custodial/escrow claims without legal/payment readiness.

# 46. Trust & Safety

Mandatory before public network scaling.

See:
`docs/product/TRUST_SAFETY_AND_MARKETPLACE_INTEGRITY_SPEC.md`

# 47. Learning Intelligence

See:
`docs/data/LEARNING_INTELLIGENCE_FLYWHEEL_SPEC.md`

Controlled learning:
outcome evidence → evaluation → shadow → promotion.

No silent self-modification.

# 48. Ask Your Company / Analytics

Permission
→ governed semantic metric
→ safe query plan
→ analytical read model
→ verified answer/provenance.

No unrestricted model-generated production SQL.

# 49. Forecasting

Versioned forecast:
target, horizon, features, uncertainty, error vs baseline.

No production model without baseline comparison.

# 50. Cross-Tenant Learning

Default:
raw tenant data isolated.

Possible opt-in:
aggregated benchmark
privacy-preserving learning
specific contractual sharing.

No silent cross-company model training.

# 51. Employment AI Governance

See:
`docs/compliance/EMPLOYMENT_AI_GOVERNANCE_SPEC.md`

Decision inventory, notice, fairness, human review, contestability and jurisdiction packs.

# 52. UI/UX

Premium, calm, clear.

Persian RTL + English LTR first class.

Desktop primary; mobile usable.

Progressive disclosure.

Admin customization:
logo, accent, light/dark, density, dashboard, login/docs branding, custom domain by plan.

No arbitrary tenant JS.
No unrestricted CSS by default.

Target WCAG 2.2 AA where applicable.

# 53. Search

Permission-aware global search.

Normalize Persian/Arabic forms.

No existence leakage across tenant/confidentiality.

# 54. Security

- MFA architecture
- SSO-ready
- server auth
- tenant isolation
- secure uploads
- rate limiting
- webhook verification
- secret vault
- encryption strategy
- audit
- dependency/secret/container scans
- SBOM
- data classification
- retention
- incident response.

Architecture should not block future SOC2/ISO27001 efforts.

# 55. Privacy / Residency

Tenant policy:
- data region
- external AI allowed?
- shared network allowed?
- telemetry allowed?
- retention.

External providers receive minimized data.

Subprocessor registry required for enterprise maturity.

# 56. Observability / DR

OpenTelemetry-based architecture.

Correlation IDs across business flows.

Backups:
DB + object storage + config/key recovery.

Validated only after restore rehearsal.

Off-host production backup.

# 57. Licensing / Entitlements

Annual license + modules + usage.

Data-driven entitlements.

No scattered `if plan == premium`.

Expiry:
grace/restricted/read-only, no destructive data lockout.

# 58. Commercial Models

See:
- `docs/product/GO_TO_MARKET_BRAND_MONETIZATION_SPEC.md`
- `docs/product/UNIT_ECONOMICS_FINANCIAL_MODEL_SPEC.md`

# 59. Installation / Upgrade

CLI + safe web wizard.

Cloud/Dedicated/On-Prem.

Preflight:
CPU/RAM/storage/domain/TLS/DB/cache/storage/workflow/mail/AI/payment/license/backups.

Upgrade:
backup
→ compatibility
→ expand migration
→ rollout
→ smoke
→ contract cleanup later.

Prefer expand/contract DB migrations.

# 60. Open Source Reuse

Allowed for development after:
license
security
maintenance
architecture fit
upgrade path.

SBOM required.

Do not turn Hayool into incompatible pasted repositories.

# 61. Autonomous Engineering

See:
`docs/engineering/AUTONOMOUS_SDLC_CONTROL_PLANE_SPEC.md`

M0:
M0.0 Trust/Autopilot bootstrap
→ M0.1 architecture
→ M0.2 autonomous gate.

Single writer, independent reviewers, exact SHA, hard deterministic gates, bounded repair.

# 62. V1 Release Train

See:
`docs/product/RELEASE_TRAIN_MARKET_READINESS_GATES.md`

- V1.0 Internal Alpha
- V1.1 Design Partner Beta
- V1.2 Talent Network Beta
- V1.3 Workforce Architect Beta
- V1.4 Managed Workforce Beta
- V1.5 Intelligence Beta
- V1.6 Commercial GA.

All belong to V1 vision.

# 63. Product Stage Principles

Do not expand target industry before initial ICP proves:
- recurring use
- meaningful retention
- time-to-value
- reliable finance/project data.

Do not scale marketplace before Trust/Safety/liquidity evidence.

Do not activate EOR/AOR before legal readiness.

Do not automate employment high-impact decisions merely because technology allows it.

# 64. Definition of Done

Feature Done requires as applicable:
REQ
permission
validation
audit
localization
RTL/LTR
error/loading/empty states
unit
integration
tenant/permission tests
E2E
security
observability
docs
migration/recovery
UX review.

No false “Done.”

# 65. M0 Required Deliverables

M0 must create/validate:
- PRD
- REQ catalog
- ADRs
- domain boundaries
- ERD
- Work Graph model
- tenancy
- permission
- finance
- Iran pack
- pricing/compensation
- trust/safety
- AI/control plane
- data/learning
- analytics
- employment AI
- UI design system
- deployment/installer
- CI/tests
- commercial architecture.

No broad business feature build before architecture gate.

# 66. Canonical Strategic Principle

Every major design choice should support this loop:

> Understand work → compose human + AI capacity → execute → measure economics/outcomes → learn safely.

If a new feature does not strengthen this loop, justify why it belongs in core.


# 67. Billing, Invoicing and Recurring Services

Support:
- quote
- proposal
- proforma
- commercial invoice
- tax invoice metadata/integration abstraction
- credit/debit note
- receipt
- partial payment
- refund
- settlement.

Internal document number and official tax-system identifiers are distinct.

Recurring services:
- hosting
- server
- domain
- maintenance
- support
- subscription
- SMS/communications
- other tenant-defined services.

Track:
next billing, next renewal, expiry, cost, selling price, margin, reminder, provider and client.

Do not auto-create/send legally binding invoices without configured authority.

# 68. Expenses, Procurement and Vendors

Support:
- supplier/vendor profile
- purchase
- expense
- recurring expense
- bill/payable
- payment
- project/cost-center allocation
- receipt/document
- VAT/tax metadata.

Vendor examples:
hosting, cloud, domain, SMS, software, office, subcontractor.

Project profitability consumes these actual costs.

# 69. Shared Interaction Engines

## Conversation Engine
Reusable for:
- client chat
- candidate interview
- support
- project discussion
- internal discussion
- AI chat.

Each conversation has ACL, retention, linked entities and AI participation policy.

## Form Engine
Reusable versioned forms for:
- project intake
- job application
- interview
- assessment
- survey
- change request
- approval
- structured data collection.

## Notification Engine
Channels:
- in-app
- email
- SMS
- webhook
- future Telegram/push.

Support preferences, digest, escalation, scheduling and localization.

# 70. OKR / KPI

Support objectives/key results at:
tenant, legal entity, department, team and individual.

Where possible KPI values resolve to governed Semantic Metrics.

Do not reward vanity metrics that produce Goodhart behavior.

# 71. AI Evaluation Lab

Before promoting significant:
- prompt
- model
- agent
- routing policy
- Jev decision policy

run versioned evaluation.

Store:
- dataset version
- metrics
- cost
- latency
- failure modes
- comparison with current champion.

Employment/high-impact policies require additional fairness/governance checks.

# 72. Incidents

Dedicated incident management:
- severity
- affected customers/services/assets
- timeline
- owner
- communications
- mitigation
- resolution
- root cause
- postmortem
- follow-up.

Incident evidence feeds reliability learning but not unrelated worker scoring.

# 73. Import / Export / Portability

Support safe import where appropriate:
- customers
- products/services
- talent data
- opening balances
- selected configuration.

Support export:
- business records
- reports
- customer/talent data subject to permissions
- tenant offboarding archive.

Validate before commit.

Data portability reduces artificial lock-in.

# 74. Purchase, Provisioning and Tenant Onboarding

Buyer flow:
account
→ organization
→ deployment mode
→ plan
→ modules
→ user/branch/legal-entity capacity
→ AI credit pack
→ support tier
→ country pack
→ network policy
→ payment
→ provisioning
→ guided onboarding.

Provisioning differs by:
Cloud / Dedicated / On-Prem.

# 75. White Label / Tenant Branding

Plan-controlled:
- logo
- favicon
- brand/accent tokens
- login branding
- document/email branding
- custom domain
- supported theme presets.

No arbitrary tenant JavaScript in V1.

# 76. Product Analytics

Separate from customer business analytics.

Measure:
- activation
- onboarding funnel
- workflow completion
- feature adoption
- retention
- support friction
- performance.

Observe privacy and deployment-mode telemetry policy.

Do not send On-Prem telemetry when tenant policy disables it.


# 77. Future Optionality Hooks

Architecture should not block future:
- Hayool Work API / MCP for AI-to-human work sourcing
- B2B Capacity Exchange
- Verified Outcome Credentials
- Workforce Academy
- Vertical Operating Packs
- Benchmark Intelligence
- Managed Outcome Marketplace
- governed Digital Worker marketplace.

These are NOT automatic V1 implementation commitments unless included by explicit REQ/roadmap.

Design extension points without pre-building unused complexity.


# 78. Executive Command Center & Role Dashboards

Management home answers:
1. What is happening?
2. What needs attention?
3. What action has highest expected value?

Include:
- cash/bank
- receivables/payables
- revenue/profit/margin
- project risk
- deadlines
- capacity
- hiring need
- sales pipeline
- renewals
- incidents
- SLA
- AI recommendations
- approvals.

Role dashboards:
Finance, HR, PM, Sales, Marketer, Employee, Freelancer, Client.

Marketer dashboard includes:
pending/earned/paid commission, attributable collections and pipeline.

# 79. Personal Work Copilot / Next Best Action

Each authorized user may receive a role-aware assistant.

Capabilities:
- summarize today's work
- prioritize tasks
- explain how to perform assigned work
- identify blockers
- propose next actions
- surface approvals/deadlines.

Suggestions must respect permission/context.

For marketers/sales:
lead follow-up and campaign next actions.

For PM:
risk/blocker/team-capacity actions.

For talent:
task context, acceptance criteria and growth guidance.

# 80. AI Project Architect / Project Manager

Project Architect:
discovery → requirements → assumptions → scope → architecture/skills → phases → milestones → tasks → estimates → risks → team needs.

AI Project Manager:
- daily/periodic status
- async stand-up
- blocker collection
- dependency monitoring
- schedule-risk detection
- resource/capacity suggestions
- client-update drafts.

Material schedule/budget/scope change follows Autonomy/Approval policy.

# 81. Software Delivery Integration

For software projects support integration with source-control/CI systems.

Link:
Requirement
→ Task
→ Repository
→ Branch
→ Commit
→ PR
→ Test
→ Deployment
→ Release.

Support:
- GitHub first adapter
- repository assets
- PR/review status
- release/deployment evidence
- incident links.

Client/talent permissions remain scoped.

No customer production secret is exposed to general project AI.

# 82. Automation Builder

Automation Engine should gain a safe visual/configuration layer.

Concept:
Event
→ Conditions
→ Actions
→ Wait/Approval
→ Branch
→ Result.

Admin can compose approved actions without code.

Actions are typed and permissioned.

No arbitrary shell/JavaScript execution for tenant users in V1.

# 83. Custom Fields / Configurable Business Metadata

Tenants may need domain-specific fields.

Provide governed custom fields:
- typed
- validated
- permission aware
- searchable where appropriate
- schema/version aware.

Do not turn all core domain modeling into unstructured metadata.

# 84. Extension SDK / Plugin Boundary

Provide documented extension interfaces for:
- AI
- Payment
- SMS
- Email
- Tax
- Bank
- Storage
- Signature
- Source control
- Calendar
- Notification.

First-party adapters use the same contracts where practical.

Future third-party plugins require:
- manifest
- permissions
- compatibility
- signing/review
- isolation.

Do not allow arbitrary untrusted server code execution by default.

# 85. Multi-Currency / FX Architecture

Finance core must support:
- legal entity functional currency
- transaction currency
- explicit exchange rate source/date
- converted reporting amount
- realized/unrealized treatment as required by country/accounting pack.

Iran launch may use IRR as authoritative local unit with Toman presentation.

# 86. Retention / Legal Hold / Data Lifecycle

Support policy-driven:
- retention
- archival
- deletion
- legal hold
- candidate retention
- AI trace retention
- recording retention.

Deletion must account for legally required immutable records.

# 87. Translation / Multilingual Content Workflow

Platform UI uses translation catalogs.

AI may draft translations for:
- custom content
- templates
- knowledge.

Legal/financial/contractual text requires approved/versioned translation where material.

Never silently auto-translate authoritative contract terms and treat them as legally equivalent.

# 88. Process Intelligence

V1.5 intelligence architecture may analyze workflow/event history to identify:
- bottlenecks
- excessive approvals
- handoff delays
- repeated rework
- automation candidates
- SLA risk.

Recommendations require evidence and simulation/approval before material process redesign.

# 89. Self-Host-First Dependency Preference

When functionality is strategically important and a mature self-hosted/open-source option is operationally reasonable, prefer ownership/control and provider abstraction.

Do not choose self-hosting dogmatically when it creates disproportionate reliability/security/maintenance burden.

Dependency decisions require ADR with:
cost, license, maturity, security, operational burden and exit path.


# 90. Product Surfaces

V1 product architecture should support distinct surfaces from shared domain/API:

## Internal / Tenant App
Management, finance, HR, projects, sales, operations.

## Client Portal
Client-facing projects, approvals, documents, billing, support and AI.

## Talent / Candidate Portal
Profile, opportunities, applications, assessments, interviews, assignments, payments/earnings where applicable, growth/evidence.

## Public Network / Intake
Public company/project intake, talent registration and approved opportunity discovery.

## Platform Admin
Tenants, licenses, plans, providers, country packs, support, platform risk and operations.

The exact deployment may share Next.js applications/routes where simpler, but permissions and UX boundaries remain explicit.


# 91. Universal Platform Rebaseline

The universal-platform baseline broadens architectural scope from Work & Workforce OS to Universal Business / Work / Resource Platform.

Market entry remains narrow.

Architecture must support:
- service businesses
- commerce
- inventory
- procurement
- warehouses
- field operations
- logistics
- manufacturing
- agriculture
- regulated-enterprise operations

through a universal kernel and Industry Packs.

# 92. Universal Business Kernel & Studio

Canonical source:

`docs/platform/UNIVERSAL_BUSINESS_KERNEL_AND_STUDIO_SPEC.md`

V1 MUST include:
- governed custom fields
- custom objects
- forms/views
- workflow/approval builder
- dashboard/report builder
- solution packaging
- AI-assisted solution drafting.

Do not implement all variability as EAV or unvalidated JSON.

# 93. Intent-to-Outcome

Canonical source:

`docs/platform/INTENT_TO_OUTCOME_ORCHESTRATION_SPEC.md`

Hayool supports intent-driven planning:

Intent
→ Need
→ Plan
→ Discovery
→ Options
→ Approval
→ Fulfillment
→ Settlement
→ Outcome.

This applies across labor, services, products, procurement and delivery.

# 94. Physical Commerce & Supply Chain

Canonical source:

`docs/domains/COMMERCE_PROCUREMENT_INVENTORY_LOGISTICS_SPEC.md`

V1 kernel/domain packs add:
- item master
- sales order
- purchase order
- inventory
- lot/serial
- warehouse/location
- shipment/delivery
- return/refund
- traceability foundation.

# 95. Manufacturing / Asset / IoT

Canonical source:

`docs/domains/MANUFACTURING_ASSET_IOT_EDGE_SPEC.md`

Hayool supports business/MRP/EAM operations and safe industrial integration.

It must not claim to be a safety-certified industrial-control system.

# 96. Agriculture

Canonical source:

`docs/domains/AGRICULTURE_FOOD_TRACEABILITY_PACK_SPEC.md`

Agriculture reuses universal:
workforce + inventory + assets + procurement + sales + traceability.

# 97. Website / CMS / Commerce

Canonical source:

`docs/domains/WEBSITE_CMS_COMMERCE_SEO_SPEC.md`

V1 includes an integrated professional website/eCommerce baseline plus headless APIs.

# 98. Global Interoperability

Canonical source:

`docs/platform/GLOBAL_LOCALIZATION_COMPLIANCE_INTEROPERABILITY_SPEC.md`

Architecture supports mappings/adapters for:
- ISO country/currency
- CLDR locale
- GS1/EPCIS
- Peppol where applicable
- ISO 20022 where applicable
- ISA-95
- OPC UA/MQTT
- OpenAPI/AsyncAPI
- MCP-safe tool exposure
- ISCO/ESCO mappings.

Standards are integration aids, not blanket legal certification.

# 99. Industry Packs

Canonical source:

`docs/platform/INDUSTRY_PACK_ARCHITECTURE_AND_CAPABILITY_MATRIX.md`

Industry maturity MUST be explicit:
Kernel / Starter / Verified / Certified-Regulated / Partner / Future.

Marketing cannot claim a regulated vertical is ready because generic primitives exist.

# 100. Algorithm / Solver Fabric

Canonical source:

`docs/ai/ALGORITHM_SOLVER_DECISION_FABRIC_SPEC.md`

Every computational problem chooses the correct engine class:
deterministic rules / optimization / prediction / semantic decision / generative agent.

LLMs MUST NOT replace deterministic mathematics or mathematical optimization without justification.

# 101. Product Experience

Canonical source:

`docs/product/GLOBAL_PRODUCT_EXPERIENCE_AND_PERSONA_WORKSPACES_SPEC.md`

The UI exposes breadth through:
- intent-first interaction
- role/persona workspaces
- progressive disclosure
- responsive/offline field experiences.

A large module catalog must not become a large cognitive load.

# 102. Banking boundary

Canonical source:

`docs/domains/BANKING_FINANCIAL_SERVICES_BOUNDARY_SPEC.md`

Banks may use Hayool for enterprise/workforce/workflow/operations and integration.

Generic Hayool Finance does not claim core banking capability.

# 103. Enterprise Accounting Expansion

Enterprise finance architecture must account for:
- multi-entity
- multi-currency
- multi-book/reporting basis where required
- consolidation read models
- intercompany
- elimination hooks
- fixed assets/depreciation
- inventory valuation
- cost accounting
- budgets/forecasts.

Country/industry packs determine exact regulatory reporting.

# 104. Data / Master Data Governance

The platform adds explicit Master Data Management concerns:
- duplicate party
- item master
- location
- supplier
- customer
- identifier mapping
- reference-data versioning
- lineage
- import/reconciliation.

# 105. Edge / Offline / Hardware

For warehouses/farms/factories/field teams V1 architecture supports:
- barcode/camera
- printer/scanner adapters
- mobile offline queue
- sync conflict policy
- Edge Gateway
- IoT connector.

Do not require permanent broadband for every operational workflow.

# 106. V1 breadth principle

V1 is broad at the platform/kernel level.

It is NOT required to be equally mature in every industry.

Quality is protected by Industry Pack maturity gates.

The first GA commercial claims remain aligned with actually verified packs.


# 107. V6 Extensibility Rebaseline

V6 makes the extension platform a first-class product requirement.

Hayool MUST NOT become the sole implementation bottleneck for every industry.

Preferred solution order:

Configuration
→ Studio / no-code
→ Low-code
→ Pro-code extension
→ First-party Core only when broad/core-critical.

Canonical source:

`docs/platform/DEVELOPER_PLATFORM_EXTENSION_RUNTIME_MARKETPLACE_SPEC.md`

The developer ecosystem is part of the V1 platform foundation.

# 108. First-party Core Build Policy

A capability belongs in protected Core only if at least one applies:

- it is required for platform integrity/security;
- it is a cross-industry primitive used broadly;
- deterministic correctness requires central ownership;
- performance/transaction integrity requires core coupling;
- marketplace/extension implementation would create unacceptable risk.

A capability should remain an extension/pack when:

- it is customer-specific;
- industry-specific;
- experimental;
- independently releasable;
- maintained by a specialist partner;
- requires a specialized external system.

This policy prevents feature-sprawl.

# 109. Developer Platform

V1 requires:

- public API contracts;
- event catalog;
- scoped app permissions;
- app manifest;
- SDK;
- CLI baseline;
- developer portal;
- test tenant;
- sample apps;
- private apps;
- declarative solution packages;
- versioning/update lifecycle;
- app observability;
- signed packages;
- partner/community registry.

Third-party code MUST NOT execute inside the main API process by default.

# 110. Community / Marketplace

Canonical source:

`docs/product/ECOSYSTEM_COMMUNITY_PARTNER_STRATEGY.md`

Hayool ecosystem may distribute:

- apps
- industry packs
- country packs
- connectors
- workflows
- reports
- website themes
- AI agents
- assessment packs.

Capability Request / bounty mechanisms should allow customer demand to fund ecosystem development rather than requiring the Core team to implement every request.

# 111. Rational AI Use

Canonical source:

`docs/ai/AI_USE_COST_GOVERNANCE_SPEC.md`

Hayool is AI-native, not AI-maximalist.

Before adding AI, evaluate whether deterministic rules, retrieval, mathematical optimization or statistical methods are superior.

Major core modules must remain useful with external AI disabled.

Every metered AI operation must be cost-attributed.

# 112. AI Economics

AI costs are part of product COGS.

Track fully loaded AI cost including:

- provider/model
- gateway
- search/embedding
- storage
- tools
- retries
- orchestration compute
- relevant platform overhead.

AI Credits and plan packaging must protect configured margin floors.

# 113. Pricing & Profit Optimization

Canonical source:

`docs/product/PRICING_PROFIT_OPTIMIZATION_EXPERIMENTATION_SPEC.md`

Management configures:

- minimum gross margin;
- minimum contribution margin;
- target fully-loaded operating margin;
- minimum AI margin;
- discount limits;
- experiment bounds.

Pricing AI cannot silently breach hard floors.

The system must distinguish accounting net profit from estimated fully-loaded transaction/product profitability.

# 114. Pricing Lab

V1 includes a controlled price/package experimentation framework.

Experiments require:
- hypothesis;
- control;
- variant;
- target population;
- success metrics;
- guardrail metrics;
- result;
- documented decision.

Optimize for the business objective chosen by management, not an AI-invented objective.

# 115. Clean-Core Extension Rule

Customer/partner customizations MUST use:

- approved configuration;
- Studio;
- public API/events;
- extension runtime/remote app.

Direct patching of protected Core or core database tables is unsupported.

This is essential for safe upgrades across Cloud, Dedicated and On-Premise deployments.

# 116. Extension Permission Re-approval

An installed extension that requests materially broader:

- data scopes;
- API scopes;
- external egress;
- protected data;
- privileged actions

requires tenant-admin approval according to policy before those new permissions become active.

# 117. Platform Data Portability

Extensibility must not become vendor lock-in.

Provide:
- data export;
- app/solution export where licensing permits;
- public APIs;
- documented schemas/contracts;
- uninstall lifecycle;
- app-owned data disclosure.

# 118. V1 Ecosystem Readiness

V1 platform is ecosystem-ready when:

- a non-programmer can build a meaningful custom workflow/app through Studio;
- a developer can build/test a private extension from documentation;
- a partner can distribute a versioned package;
- permissions/data access are visible to admins;
- extension update/uninstall is safe;
- platform upgrade does not require editing custom customer code.

# 119. Extended Commercial Model

Revenue architecture includes:

- Annual License
- AI Credits
- Cloud / Dedicated / On-Premise
- support/SLA
- modules
- first-party packs
- marketplace revenue share
- extension hosting/runtime
- partner/certification services
- implementation
- managed workforce/outcome
- transaction orchestration.

Each revenue stream maintains its own unit economics.

# 120. Product Promise Hierarchy

The product must communicate different promises to different audiences without changing the underlying platform.

### General user
Tell Hayool what you need; it helps coordinate the outcome.

### Small / medium business
Run core operations in one configurable system.

### Enterprise
A governed, extensible operating platform with deployment, security, audit, integration and localization controls.

### Developer / Partner
Build industry-specific capability once and distribute it safely across Hayool customers.

The marketing site must not expose internal architectural complexity to ordinary users.

