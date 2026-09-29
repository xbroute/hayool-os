> Historical V7 proposal: retained for provenance; current authority is docs/SOURCE_OF_TRUTH_INDEX.md.

# Hayool OS V7 — Platform Architecture Completeness Specification

## 1. Architecture objective

Design the full capability surface before material implementation while keeping runtime complexity proportional to proven need.

**Complete contracts now. Progressive implementation later.**

## 2. Core architectural style

Default:
- modular monolith
- TypeScript monorepo
- explicit domain/application boundaries
- PostgreSQL authoritative OLTP
- durable workflow abstraction
- provider adapters
- event outbox
- audit/evidence ledger
- API-first internal service boundaries
- one codebase for Cloud/Dedicated/On-Prem where feasible.

No microservice split without an ADR based on concrete scale, isolation, deployability or team-boundary evidence.

## 3. Domain ownership

Every authoritative entity has one owning module.

Cross-domain operations occur through:
- application services
- commands/queries
- domain events
- public/internal contracts.

No module mutates another module's tables directly.

## 4. Universal Kernel

Required conceptual domains:
- Identity/Party
- Organization
- Place
- Catalog/Offer
- Resource
- Work
- Commercial Commitment
- Fulfillment
- Finance
- Physical Flow
- Knowledge/Content
- Governance/Policy
- Time/Schedule
- Device/Event
- Outcome/Evidence.

## 5. Typed Core vs configurable data

Strongly typed:
- tenants
- identities
- permissions
- financial ledger
- payment state
- authoritative inventory movement
- audit
- entitlements
- legal entities
- core policy/version references.

Configurable:
- approved custom fields
- custom objects
- relations
- forms/views
- workflows
- reports
- templates
- portal surfaces.

No arbitrary unvalidated JSON for critical truth.

## 6. Solution Package model

Every Studio/extension customization is versioned as a package with:
- ID
- version
- dependencies
- schemas
- permissions
- migrations
- UI
- workflows
- reports
- translations
- seed/reference data
- install/update/uninstall rules
- rollback behavior
- compatibility range
- signature.

## 7. Extension execution hierarchy

1. Declarative package
2. Remote App
3. Managed isolated runtime only after security maturity
4. First-party module.

Third-party code does not execute inside the main API process by default.

## 8. Public API

Public API is capability-oriented, not database-oriented.

Requirements:
- explicit version/state: experimental/preview/stable/deprecated
- tenant context
- scoped auth
- idempotency
- pagination
- standardized errors
- rate limits
- audit/correlation
- OpenAPI machine-readable contract
- compatibility CI
- changelog and migration guide.

Pin the exact OpenAPI feature line/tooling supported by the codebase through ADR; do not blindly track latest.

## 9. Event API

Requirements:
- stable public events
- schema version
- tenant scope
- delivery semantics
- idempotency
- replay policy
- privacy classification
- AsyncAPI or equivalent contract
- compatibility checks.

## 10. App principal

Every app is a first-class principal.

It receives only explicit:
- object
- field
- tenant/legal entity
- workflow action
- event
- file
- protected-data
- egress
- secret-capability scopes.

App privileges are not inherited from the installing admin.

## 11. Data architecture

### Operational plane
Normalized transactional truth.

### Event plane
Outbox/domain events.

### Analytical plane
Read models first; warehouse/columnar store only when justified.

### Knowledge plane
Documents, search, embeddings/RAG with ACL-before-retrieval.

### Decision plane
Decision Registry/Ledger, evaluation artifacts.

### Extension plane
Versioned extension schemas/data ownership with export/uninstall semantics.

## 12. Search

Permission-aware and tenant-safe.

Must prevent existence leakage.

Support multilingual normalization including Persian/Arabic character normalization where relevant.

## 13. Durable workflows

Use a workflow abstraction for:
- long-running approvals
- external provider calls
- retries/backoff
- timeouts
- human tasks
- compensation
- escalation
- scheduled waits.

The first implementation may use a durable workflow engine if justified. Business modules depend on Hayool workflow contracts, not vendor-specific code.

## 14. Finance architecture

Double-entry ledger.

Posted records immutable except explicit reversal/adjustment.

Money uses exact representation.

Support:
- multi-currency
- functional/transaction currency
- rate source/date
- accounting dimensions
- multi-entity
- intercompany hooks
- consolidation-ready read models
- fixed assets/cost accounting hooks.

Country/accounting packs own local reporting specifics.

## 15. Inventory architecture

Authoritative movement ledger.

Derived:
on-hand, available, reserved, incoming, outgoing.

Lot/serial/expiry conditional by item policy.

Operational transaction and accounting valuation remain reproducible.

## 16. Human and digital workers

Share:
- capability
- assignment
- capacity
- cost
- SLO/quality evidence.

Do not share:
- legal personhood
- employment rights
- payroll
- sensitive HR data
- authentication semantics
- disciplinary logic.

## 17. Algorithm fabric

Each production algorithm has:
- ID/version
- owner
- engine class
- input/output schema
- hard constraints
- objective
- prohibited inputs
- fallback
- evaluation
- fairness/privacy
- autonomy.

Classes:
Rules / Retrieval / Solver / Predictive / Semantic Decision / Generative Agent.

## 18. AI Control Plane

Provider-neutral registry:
- provider
- model
- region
- capabilities
- cost
- latency
- privacy profile
- tool/vision/structured-output support
- fallback
- evaluation status.

Core modules depend on Hayool contracts.

## 19. Deployment

One release artifact strategy where practical.

Modes:
- Cloud
- Dedicated
- On-Prem.

On-Prem supports:
- external AI off
- telemetry off
- offline license/update workflow where required
- manual provider configuration
- signed extension package import.

## 20. Edge/offline

Optional Edge Gateway for factories/warehouses/farms/field operations.

Rules:
- store-and-forward
- local identity/device certificate
- bounded local rules
- no unrestricted AI control of safety-critical systems
- explicit conflict/idempotency policy
- authoritative finalization rules.

## 21. Observability

OpenTelemetry-compatible strategy.

Correlate:
user/action
→ API
→ workflow
→ provider
→ domain event
→ decision
→ financial/business outcome.

Sensitive values are redacted.

## 22. Backup/DR

Back up:
- DB
- object storage
- configuration
- critical encryption/key recovery metadata according to secure procedure.

A backup is unproven until restore rehearsal succeeds.

## 23. Migration

Prefer expand/contract:
1. additive schema
2. compatible application
3. backfill
4. cutover
5. delayed cleanup.

Destructive cleanup is separately reviewed.

## 24. Architecture completion gate

Architecture is complete enough to implement when:
- domain owners are named;
- critical invariants are testable;
- public/extension contracts are bounded;
- jurisdiction policy integration points exist;
- failure modes/fallbacks exist;
- data ownership exists;
- migration/upgrade path exists;
- no future vertical requires bypassing protected Core for ordinary customization.

