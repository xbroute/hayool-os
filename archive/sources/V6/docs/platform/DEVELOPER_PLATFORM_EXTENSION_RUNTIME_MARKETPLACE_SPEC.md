# Hayool OS — Developer Platform, Extension Runtime & Marketplace Specification
Version: 6.0
Status: Canonical platform architecture
Purpose: Make Hayool OS extensible enough that industries, workflows and complex customer requirements can be built by customers, partners and community developers without modifying the protected core.

---

## 0. Strategic principle

Hayool OS must not try to first-party-build every industry-specific system.

The platform must instead make new capability cheap, safe and distributable.

The extension model is therefore a core product capability, not an afterthought.

The target is:

**Clean Core + Open Extension Surface + Governed Marketplace + Strong Developer Experience.**

This is how Hayool can address a very broad market without turning its own codebase into an unmaintainable collection of vertical features.

---

# 1. Four levels of extensibility

Every requirement should be solved at the lowest safe level.

## Level 0 — Configuration

No new schema or code.

Examples:
- terminology
- statuses
- numbering
- permissions
- approval thresholds
- themes
- dashboards
- notification preferences
- price/rate policies.

## Level 1 — No-code / Hayool Studio

For business builders and non-programmers.

Capabilities:
- custom objects
- custom fields
- relationships
- forms
- views
- dashboards
- reports
- workflow
- approval
- validation
- document templates
- portal pages
- knowledge sources
- basic agent configuration.

## Level 2 — Low-code

For advanced builders.

Capabilities:
- safe formula/expression language
- workflow expressions
- typed functions
- reusable components
- API connector builder
- mapping/transformation
- event actions
- limited scripts only inside a restricted sandbox if/when M0 architecture approves one.

Arbitrary server-side JavaScript/Python is NOT the default low-code mechanism.

## Level 3 — Pro-code Extension

For developers and partners.

Capabilities:
- app manifest
- extension SDK
- backend service
- event subscriptions
- webhooks
- UI extension points
- custom workflow activities
- custom AI tools
- connector/provider adapters
- custom reports
- specialized data services
- own external database/storage if needed.

## Level 4 — Native Core Module

Reserved for first-party capabilities whose correctness/performance/security requires direct core ownership.

Examples:
- tenancy
- authorization
- finance ledger
- core billing
- core inventory transaction engine
- audit
- platform licensing.

Third-party developers do not modify protected core code.

---

# 2. Extension execution models

Hayool supports several execution models.

## 2.1 Declarative Solution Package

Contains metadata only:
- schema definitions
- forms/views
- workflows
- reports
- templates
- permissions
- translations
- configuration.

Safest and easiest to upgrade.

Preferred for most community customization.

## 2.2 Remote App

The developer hosts their own service.

Hayool communicates through:
- OAuth/OIDC
- signed webhooks
- public API
- event subscriptions
- extension UI protocol.

The app may keep its own database.

Best for:
- heavy custom compute
- regulated vertical systems
- specialized algorithms
- external SaaS integrations
- apps requiring independent release cadence.

## 2.3 Managed Extension Runtime

Future/advanced platform capability.

Hayool may offer hosted isolated compute for approved apps.

Possible isolation technology must be selected by ADR after security/performance evaluation.

Requirements:
- resource quotas
- no host filesystem access
- no cross-tenant memory
- scoped network egress
- scoped secrets
- timeouts
- CPU/memory limits
- immutable base images/runtime
- security patching
- per-app observability.

Do not execute untrusted third-party code inside the main API process.

## 2.4 First-party Module

Runs inside protected application runtime and follows core engineering governance.

Only Hayool-maintained modules or exceptionally reviewed partner modules may qualify.

---

# 3. Extension Manifest

Every installable package/app has a manifest.

Minimum fields:

- app_id
- name
- vendor
- version
- minimum_platform_version
- maximum_tested_platform_version
- extension type
- dependencies
- requested scopes
- requested data classes
- requested egress domains
- webhooks/events
- UI extension points
- workflow actions
- settings schema
- migrations
- install hooks
- uninstall policy
- retention policy
- data residency declarations
- AI providers/processors used
- license
- billing model
- support contact
- privacy policy
- security contact.

Manifest changes affecting scopes/data/egress are treated as major permission changes.

Tenant admins must re-approve material permission expansion.

---

# 4. Permission model for apps

Apps operate as scoped principals.

Permissions may include:
- object read/write
- specific fields
- specific legal entity/branch
- workflow action
- event subscription
- file access
- user profile access
- protected HR data
- financial data
- customer personal data
- outbound network
- secret reference use.

Use least privilege.

Apps do not inherit installer/admin permissions automatically.

---

# 5. Protected data

Create explicit protected-data classes.

Examples:
- contact data
- candidate data
- payroll
- financial
- health/regulated extension data
- government IDs
- secrets
- private documents.

Apps requesting protected data receive:
- additional review requirement
- clear admin disclosure
- data minimization test
- retention declaration
- DPA/privacy requirements where applicable.

A marketplace app cannot request “all tenant data” for convenience.

---

# 6. UI extension architecture

Third-party UI should integrate naturally without gaining unrestricted DOM/session control.

Supported patterns:
- approved component schema
- platform-hosted extension surface
- sandboxed iframe where necessary
- action/menu slot
- record panel
- dashboard widget
- page
- command/action
- portal block.

UI extension receives only scoped context.

Do not expose raw authentication cookies.

---

# 7. Events

Public event catalog should cover stable domain events.

Examples:
- customer.created
- order.confirmed
- payment.received
- project.created
- task.completed
- talent.applied
- inventory.moved
- shipment.delivered
- invoice.posted.

Events:
- versioned
- schema-documented
- idempotent to consume
- replay policy defined
- tenant scoped.

Use AsyncAPI or equivalent machine-readable contracts where practical.

---

# 8. Public API

Developer API principles:
- stable versioning
- explicit auth/scopes
- tenant context
- pagination
- rate limit
- idempotency
- error codes
- change log
- SDK generation
- test environment
- OpenAPI schema.

Core APIs must expose capabilities rather than database internals.

---

# 9. Developer Portal

A serious ecosystem requires a first-class developer experience.

Developer Portal includes:
- guides
- API reference
- OpenAPI/AsyncAPI
- extension manifest reference
- SDK docs
- CLI docs
- event catalog
- UI extension docs
- sample apps
- recipes
- security guide
- marketplace guide
- compatibility policy
- deprecation policy
- changelog
- migration guides
- troubleshooting.

Search and AI documentation assistant may help developers, but canonical docs remain authoritative.

---

# 10. Developer CLI

Proposed command experience:

```text
hayool dev login
hayool app create
hayool app dev
hayool app test
hayool app lint
hayool app package
hayool app publish
hayool app installations
hayool app logs
```

M0 chooses exact implementation.

CLI should support:
- local config validation
- manifest linting
- API type generation
- development tenant
- log streaming
- package signing
- compatibility test.

---

# 11. Local developer experience

Target:

A competent developer should be able to go from zero to a working example app in under 30 minutes using documentation.

Provide:
- Docker/dev container
- test tenant
- fake data
- webhook tunnel
- SDK
- starter templates
- extension simulator
- fixtures.

Measure time-to-first-extension.

Developer Experience is a product KPI.

---

# 12. Testing SDK

Extension developers receive:
- contract test kit
- auth/permission test helpers
- event fixtures
- fake tenant
- API mock
- browser extension harness
- accessibility test helpers
- marketplace validation CLI.

Apps should be testable without real production tenants.

---

# 13. App lifecycle

Lifecycle:

Draft
→ Development
→ Private Test
→ Submitted
→ Reviewed
→ Published
→ Updated
→ Deprecated
→ Retired.

Install lifecycle:
Install
→ Configure
→ Active
→ Upgrade
→ Suspended
→ Uninstall.

Uninstall must define:
- retained data
- deleted data
- external data notice
- export.

---

# 14. Versioning

Use semantic compatibility principles.

### Patch
Bug fix, no new permission.

### Minor
Backward-compatible capability.

### Major
Breaking API change or material new permission/data/egress.

Major updates requiring broader permission do not silently auto-install.

Tenant admin must approve where required.

---

# 15. API stability

Public APIs are classified:
- Experimental
- Preview
- Stable
- Deprecated.

Stable APIs receive a defined deprecation window.

Breaking changes require:
- replacement path
- migration guide
- telemetry of affected apps
- developer notice.

Do not promise infinite support.

---

# 16. Clean Core

Customer and partner customizations must not modify protected core tables or source code.

Preferred order:
1. configuration
2. Studio
3. public APIs/events
4. remote/managed extension
5. new first-party core capability only if broadly justified.

This preserves upgradeability.

---

# 17. Extension data ownership

App data can live:
- in approved Hayool custom objects
- app-owned platform storage
- developer-owned remote storage.

The owner/location must be transparent.

On uninstall, the tenant must understand what remains.

---

# 18. Secrets

Apps declare secret needs.

Secrets:
- stored in vault
- never shown to other apps
- never exposed in client UI
- accessed by reference/capability.

A remote app normally owns its own external-service secrets.

---

# 19. Marketplace

Marketplace categories:
- industry packs
- country packs
- connectors
- workflows
- themes
- reports
- AI agents
- assessments
- websites
- extensions/apps.

Listing states:
- Community
- Verified
- Enterprise Ready
- Regulated/Certified Partner
- First-party.

Badges represent actual review scope, not vague quality claims.

---

# 20. Marketplace review

Review dimensions:
- malware/security
- permissions
- data minimization
- privacy
- license
- functionality
- UX
- accessibility
- performance
- billing transparency
- support contact
- upgrade/uninstall behavior.

Protected data/regulated apps receive stronger review.

---

# 21. Marketplace economics

Developer may choose:
- free
- open source
- paid one-time
- subscription
- usage-based
- enterprise quote.

Hayool may charge:
- marketplace revenue share
- payment processing pass-through
- hosting/runtime usage
- certification
- premium distribution.

Final take rates are pricing experiments, not hard-coded product assumptions.

Developer revenue must be transparent and reconcilable.

---

# 22. Community request loop

Create Capability Request Board.

Tenant can say:
> I need veterinary herd management.

Possible outcome:
- Studio template generated
- partner accepts bounty
- community developer builds pack
- Hayool first-party team decides it belongs in core
- existing extension recommended.

This prevents Hayool from becoming the bottleneck for every industry request.

---

# 23. Bounties and sponsorship

Future capability:
- company posts requested extension
- budget/bounty
- developer/partner proposes solution
- milestone/acceptance
- marketplace publication optionally allows developer to resell.

This can create a self-expanding ecosystem.

---

# 24. Partner program

Partner types:
- implementation
- developer
- localization
- accounting/payroll
- industry specialist
- integration
- managed hosting.

Partner certification should test real capability.

Do not create pay-to-win certification.

---

# 25. Community governance

Potential:
- public RFCs for API changes
- developer advisory group
- public changelog
- beta program
- issue/request voting
- community examples
- open SDK repositories.

Core product source may remain private while SDKs/specs/examples are public.

---

# 26. Open-source strategy

Recommended:
- client SDKs: permissive license
- CLI: consider open source
- example apps: open source
- extension schemas/specs: public
- selected connectors: open source when strategic.

Benefits:
- trust
- faster ecosystem growth
- easier debugging
- community contribution.

Core commercial product does not need to be open source.

---

# 27. Regulated extensions

Hayool technically permits developers to build highly complex systems such as:
- specialized banking modules
- clinical workflows
- industrial systems
- laboratory systems.

But marketplace maturity status must state:
- who owns regulatory responsibility
- certifications
- supported jurisdictions
- deployment requirements
- audit evidence.

“Can be built on Hayool” is not the same claim as “Hayool core is certified for this use.”

---

# 28. Extension marketplace safety

Required:
- kill/suspend app
- revoke permissions
- security advisory
- forced uninstall in extreme malicious cases
- vulnerable version warning
- signed package
- publisher verification
- incident reporting.

---

# 29. App observability

Platform gives developers scoped:
- logs
- traces
- errors
- invocation metrics
- rate-limit metrics
- installation health.

Tenant admins can see:
- app status
- data access
- recent errors
- external egress
- usage.

---

# 30. App billing

Marketplace billing should support:
- tenant subscription
- usage meter
- seat
- branch
- transaction
- one-time.

Entitlement engine enforces app access.

Third-party pricing changes require clear renewal/notice policy.

---

# 31. AI-generated extensions

AI may scaffold:
- manifest
- schema
- forms
- workflows
- tests
- API client
- docs.

Generated pro-code still passes normal code review/security/tests.

AI does not gain special marketplace trust.

---

# 32. V1 commitments

V1 must ship enough ecosystem foundation that community expansion can begin.

Required:
- stable initial public API
- events
- app manifest
- developer portal
- SDK
- CLI baseline
- development/test tenant
- declarative solution packages
- private apps
- partner apps
- basic marketplace/registry
- permissions/scopes
- version/update lifecycle
- signed packages
- Studio.

Advanced untrusted hosted-code runtime can follow after security maturity.

The ecosystem must not depend on Hayool building every industry feature itself.

