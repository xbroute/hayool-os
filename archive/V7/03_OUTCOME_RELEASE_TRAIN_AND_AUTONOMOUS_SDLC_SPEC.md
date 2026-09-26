> Historical V7 proposal: retained for provenance; current authority is docs/SOURCE_OF_TRUTH_INDEX.md.

# Hayool OS V7 — Outcome Release Train & Autonomous SDLC Specification

## 1. Governing rule

**A milestone is an outcome proof, not a module count.**

A release can contain many features and still fail if the intended business outcome cannot be completed safely and repeatably.

## 2. Two parallel trains

### Product Release Train
Proves user/business outcomes.

### Engineering Autonomy Train
Proves that AI can safely implement, test, review, debug, update and release increasingly broad classes of changes.

Neither train may claim maturity from documentation alone.

## 3. M0.0 — Trustworthy Engineering Bootstrap

Outcome proof:
> Can an AI engineering system make a bounded change through branch → tests → independent review → staging without bypassing governance?

Required evidence:
- protected main
- PR-only change
- baseline CI
- exact-SHA review
- one writer
- read-only reviewers
- immutable Engineering Run ID
- risk classification
- model/provider identity logging
- cost/time/iteration limits
- kill switch
- secret isolation
- untrusted-PR policy
- deterministic blocker behavior
- evidence store
- one complete test PR.

No production auto-deploy.

## 4. M0.1 — Architecture & Source-of-Truth Closure

Outcome proof:
> Can an implementation agent determine what to build without inventing product rules?

Required:
- Source-of-Truth index
- `PROJECT_STATE.md`
- `NEXT_ACTIONS.md`
- REQ catalog
- ADR index
- domain ownership
- data classification
- permission model
- tenancy model
- global jurisdiction model
- extension contract model
- deterministic financial invariants
- AI/algorithm contracts
- UX/design-system architecture
- deployment/backup/upgrade model
- release evidence model
- risk register
- acceptance tests for golden journeys.

## 5. M0.2 — Independent Architecture Gate

Outcome proof:
> Does the proposed architecture preserve product breadth while preventing unsafe complexity, regulatory overclaim and Core sprawl?

Freeze SHA.

Run deterministic checks before model review.

Independent reviews:
- architecture
- security/tenancy
- data/privacy
- finance
- AI/decision intelligence
- employment/workforce
- global jurisdiction
- developer ecosystem
- accessibility/UX
- operability/DR
- market/GTM/unit economics.

Findings are structured and tied to exact evidence.

Repair loop is bounded.

M0 is not self-merged.

## 6. V1.0 — Internal Alpha: Project Company Golden Loop

Outcome proof:
> Can Hayool itself run a real project-based service workflow from client need to project profitability?

Must prove:
- identity/tenant/permissions
- client/CRM foundation
- requirements/scope
- proposal/contract
- project/work/tasks
- people/talent basics
- time/capacity
- finance foundation
- project cost/revenue/profitability
- approvals/audit
- documents/conversations/notifications baseline
- RTL/LTR
- backup + restore rehearsal
- no known P0/P1.

Success is real internal use, not seeded demo data.

## 7. V1.1 — Design Partner Beta

Outcome proof:
> Can a second company onboard and complete the golden loop without Hayool engineers manually fixing its data or code?

Prove:
- isolation
- onboarding
- import/export
- entitlements
- tenant branding
- support workflow
- diagnostics
- upgrade path
- time-to-first-value instrumentation.

Measure actual use and support burden.

## 8. V1.2 — Talent Network + Jurisdiction-aware Sourcing

Outcome proof:
> Can eligible talent be discovered and matched fairly without exposing restricted or ineligible supply?

Prove:
- structured profiles/evidence
- sourcing policy
- jurisdiction/corridor eligibility
- compensation corridors
- constraint-first matching
- multi-objective options
- fair exposure/cold-start
- invite/apply
- trust/safety
- dispute/appeal
- privacy boundaries.

Include domestic-only and global-if-eligible tests.

## 9. V1.3 — Workforce Architect

Outcome proof:
> Can Hayool turn business goals into a useful editable capability/work/resource plan?

Prove:
- discovery
- capability map
- work inventory
- capacity gaps
- build/buy/automate/hire options
- human/AI/vendor scenarios
- cost/time/risk comparison
- manager edit/approval
- shadow evaluation.

## 10. V1.4 — Managed Workforce Beta

Outcome proof:
> Can Hayool safely act as the defined commercial/operational party for a bounded supported engagement mode?

Blocked without:
- current legal approval
- contract model
- payment/payout
- worker classification process
- working-capital policy
- dispute handling
- insurance/partner responsibility
- jurisdiction support state.

Start with a narrow corridor.

## 11. V1.5 — Intelligence Beta

Outcome proof:
> Can governed analytics/prediction improve decisions without inventing metrics or hiding uncertainty?

Prove:
- semantic metrics
- read models
- provenance
- Decision Registry/Ledger
- baseline forecast
- challenger comparison
- uncertainty
- permissions
- no unrestricted production SQL
- controlled promotion.

## 12. V1.6 — Commercial GA for Initial ICP

Outcome proof:
> Can Hayool be sold, onboarded, supported, upgraded, restored and billed for the initial ICP with predictable economics and truthful claims?

Prove:
- security hardening
- incident process
- current legal/privacy artifacts
- DR restore
- upgrade
- Cloud deployment
- Dedicated deployment path
- On-Prem packaging path
- billing/licensing
- AI Credits accounting
- observability
- offboarding/export
- SLA/support operations
- financial model updated from real COGS/support data
- design partner evidence.

## 13. V1.7 — Universal Operations / Studio Proof

Outcome proof:
> Can a materially different business domain be created without editing protected Core?

Prove:
- Studio custom object
- forms/views
- workflow/approval
- reports/dashboard
- Solution Package lifecycle
- publish/rollback
- permissions
- import/export
- at least one non-professional-services solution.

## 14. V1.8 — Physical Operations / Industry Proof

Outcome proof:
> Can the platform safely handle physical resources and fulfillment while preserving deterministic inventory/finance state?

Prove:
- sales/procurement
- inventory movement
- lot/serial where required
- shipment/delivery
- assets/maintenance
- offline/mobile/barcode baseline
- one starter manufacturing/agriculture/field-service proof
- industrial boundary tests.

No safety-critical control claim.

## 15. V1.9 — Global Platform Proof

Outcome proof:
> Can the same codebase adapt to materially different jurisdictions without Core forks?

Prove:
- Country Pack lifecycle
- subnational override
- provider availability routing
- data residency
- local banking/payment adapters
- local tax/e-invoice/payroll hooks
- domestic-only vs global sourcing policies
- locale/accessibility
- offline/manual fallbacks
- country capability matrix.

At least two materially different jurisdictions should be validated before calling the architecture globally proven.

## 16. V1.10 — Developer Platform & Ecosystem GA

Outcome proof:
> Can an external developer independently build, test, install, upgrade, monetize and support an app without persistent Hayool engineering intervention?

Prove:
- Developer Portal
- stable public API policy
- events
- SDK
- CLI
- test tenant
- private app
- Remote App
- manifest/scopes
- protected data disclosure
- permission re-consent
- signed package
- install/update/uninstall
- compatibility CI
- app health/logs
- billing/entitlements
- marketplace registry
- publisher verification
- capability request/bounty baseline.

Minimum evidence:
- three non-Core apps;
- one platform-upgrade compatibility survival;
- one permission-expansion reapproval;
- one uninstall/data-portability proof.

## 17. Engineering Autonomy Levels

### AE0 Manual
AI advisory only.

### AE1 Agentic Implementation
AI creates branch/code/tests/PR. Human controls review/merge.

### AE2 Automated Review & Repair
Independent AI council + bounded repair. Human merge.

### AE3 Guarded Low-Risk Merge
Only after shadow evidence. R0/R1 only.

### AE4 Guarded Release
Low-risk staging/canary/release with policy-based rollback.

### AE5 Controlled Self-Optimizing Factory
Routing/review policies improve through offline eval → shadow → limited promotion.

Never jump levels by declaration.

## 18. Autonomous debugging loop

Incident/Test Failure
→ collect deterministic evidence
→ reproduce
→ minimize failing case
→ classify domain/risk
→ create regression test
→ root-cause hypothesis
→ fix on branch
→ deterministic test suite
→ independent review
→ staging replay
→ gate
→ merge/release according to risk.

AI must never “fix” a bug by deleting the failing oracle.

## 19. Autonomous update loop

Dependency/provider/standard/legal change
→ watcher creates candidate change event
→ impact analysis
→ REQ/ADR/policy delta
→ test updates
→ compatibility simulation
→ security/license/legal review as applicable
→ staged rollout
→ monitor
→ rollback/supersede.

High-impact legal policy and financial rules require qualified review before activation.

## 20. Release evidence

Every milestone has an `EVIDENCE_INDEX` with:
- commit/release SHA
- test reports
- security reports
- SBOM/license reports
- browser traces/screenshots
- restore/upgrade results
- jurisdiction policy versions
- model/provider versions
- performance results
- unresolved risks
- customer/market evidence where applicable.

No evidence, no claim.

