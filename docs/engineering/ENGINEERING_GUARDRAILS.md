> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Engineering Guardrails
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping
Applies to: Human developers, Claude Code, Codex, ChatGPT Work, CI/CD agents, automation agents and release tooling

---

# 0. Purpose

This document translates the Hayool OS Engineering Constitution into concrete, testable, enforceable engineering constraints.

The Constitution defines principles.
The Guardrails define operational boundaries and measurable checks.

A change that violates a mandatory guardrail MUST NOT be merged or deployed merely because an AI agent or developer considers it convenient.

When a guardrail conflicts with a product requirement:
1. stop,
2. create/update an ADR or requirement,
3. document the conflict,
4. obtain the required approval,
5. update the guardrail only through an explicit reviewed change.

---

# 1. Guardrail severity

Every guardrail is one of:

- **BLOCKER** — merge/deploy must be prevented.
- **REQUIRED** — must be satisfied before feature/milestone completion.
- **ADVISORY** — may be temporarily waived with documented rationale.

CI and GitHub Rules should mechanically enforce BLOCKER rules wherever technically possible.

---

# 2. Source-of-Truth Guardrails

## GR-SOT-001 — Requirement traceability [BLOCKER]

Any material user-visible behavior or business rule must map to a `REQ-*` requirement.

A feature must not exist only in:
- chat history,
- an issue comment,
- a commit message,
- an AI prompt.

Required trace:

REQ
→ implementation issue/task
→ PR
→ tests
→ release.

## GR-SOT-002 — Architecture change requires ADR [BLOCKER]

Any change to:
- module boundaries,
- database ownership,
- tenant model,
- security model,
- deployment architecture,
- public API contract,
- AI provider abstraction,
- workflow engine,
- accounting architecture

requires an `ADR-*`.

## GR-SOT-003 — Repository beats chat memory [BLOCKER]

If chat memory and repository Source of Truth disagree, repository state wins unless an approved change updates the repository first.

---

# 3. Git and Pull Request Guardrails

## GR-GIT-001 — No direct work on protected `main` [BLOCKER]

All material changes go through:
branch → PR → required checks → review → merge.

## GR-GIT-002 — No force push to protected branches [BLOCKER]

Force push is prohibited for protected branches.

## GR-GIT-003 — Small reviewable PRs [REQUIRED]

Prefer one coherent concern per PR.

Large PRs must be split unless splitting would create an unsafe partial migration.

## GR-GIT-004 — No self-approval for high-risk change [BLOCKER]

A coding agent must not be the only reviewer of its own change for:
- finance,
- payroll,
- auth,
- tenancy,
- permissions,
- payment,
- secrets,
- production infrastructure,
- destructive migration,
- AI autonomy escalation.

Independent human or independent-model review is required according to release policy.

---

# 4. Test Integrity Guardrails

## GR-TEST-001 — Tests cannot be weakened to obtain green CI [BLOCKER]

It is forbidden to:
- delete a valid failing test merely to pass CI,
- mark a valid test skipped without an approved reason,
- reduce assertions solely to make a failure disappear,
- hard-code production logic to one test fixture.

## GR-TEST-002 — Bug fix requires regression coverage [REQUIRED]

Every reproducible defect fixed in critical business logic must receive a regression test where technically feasible.

## GR-TEST-003 — Financial invariants [BLOCKER]

At minimum:
- total debit == total credit,
- duplicate payment webhooks cannot create duplicate money movement,
- partial settlement remains correct,
- posted journal entries are not silently mutated,
- reversal behavior is deterministic,
- historical rule versions remain reproducible.

## GR-TEST-004 — Tenant isolation tests [BLOCKER]

Every tenant-owned module must have automated tests proving:
- no cross-tenant read,
- no cross-tenant write,
- no cross-tenant search result leakage,
- no cross-tenant AI/RAG context leakage.

## GR-TEST-005 — Permission negative tests [BLOCKER]

Sensitive actions must have tests for both:
- permitted actor,
- denied actor.

---

# 5. Database and Migration Guardrails

## GR-DB-001 — No destructive migration without explicit plan [BLOCKER]

Dropping/renaming/retyping production data requires:
- migration plan,
- data preservation plan,
- rollback/forward-fix plan,
- staging rehearsal,
- explicit high-risk approval.

## GR-DB-002 — Money never uses floating point [BLOCKER]

Use exact decimal/integer representations with explicit currency/unit.

## GR-DB-003 — Historical rule versioning [BLOCKER]

Financial, payroll, commission, pricing and tax records must retain the effective rule/policy/version used at creation.

## GR-DB-004 — Referential integrity [REQUIRED]

Use foreign keys and database constraints where practical rather than relying only on application code.

## GR-DB-005 — No hidden JSON schema escape hatch [REQUIRED]

Do not use arbitrary JSON columns to avoid proper relational/domain modeling.

JSON is allowed for genuinely flexible metadata with validation/versioning.

---

# 6. Financial and Business-Rule Guardrails

## GR-FIN-001 — Deterministic finance [BLOCKER]

AI/Jev must not authoritatively calculate:
- VAT,
- payroll,
- commission,
- invoice totals,
- accepted billable time,
- ledger debit/credit,
- account balance,
- tax due,
- payment settlement.

AI may suggest/classify/explain, while deterministic code performs authoritative calculations.

## GR-FIN-002 — No silent accounting edits [BLOCKER]

Posted accounting events are corrected through reversal/adjustment workflows, not casual mutation.

## GR-FIN-003 — Client pricing != talent compensation [BLOCKER]

Client commercial pricing and specialist compensation are separate domains.

Unauthorized users must not infer one from the other.

## GR-FIN-004 — Margin and markup are distinct [REQUIRED]

UI, reports and pricing engine must not conflate markup with gross margin.

## GR-FIN-005 — Currency/unit clarity [BLOCKER]

No screen, API or report may ambiguously mix IRR and Toman.

Currency and unit must be explicit in authoritative storage and interfaces.

---

# 7. Security Guardrails

## GR-SEC-001 — No secrets in Git [BLOCKER]

No:
- API key,
- private key,
- database password,
- production token,
- payment secret,
- vault root token

may enter Git history.

## GR-SEC-002 — AI never receives raw production credentials [BLOCKER]

AI agents receive capabilities/tools, not plaintext secrets.

Secret retrieval happens server-side inside trusted tool execution.

## GR-SEC-003 — Server-side authorization [BLOCKER]

UI hiding is not authorization.

All sensitive operations require server-side permission checks.

## GR-SEC-004 — Untrusted input remains untrusted [BLOCKER]

Documents, emails, resumes, web pages, support tickets, RAG passages and client content cannot grant themselves instructions/tool permissions.

## GR-SEC-005 — Upload validation [BLOCKER]

Uploaded files require:
- type validation,
- size limits,
- safe storage,
- executable blocking,
- malware scanning integration where practical,
- permission-aware download.

## GR-SEC-006 — Production access separation [BLOCKER]

Development AI agents must not have unrestricted production shell/database credentials by default.

Production actions use scoped deployment identities and approval gates.

---

# 8. AI Autonomy Guardrails

## GR-AI-001 — Autonomy is action-specific [BLOCKER]

An agent's global “autonomous” status does not authorize every action.

Autonomy is evaluated per:
- tenant,
- workflow,
- action,
- data scope,
- risk level.

## GR-AI-002 — Protected actions [BLOCKER]

The following default to human/explicit approval unless an approved policy explicitly states otherwise:

- money movement,
- payroll approval,
- final employment termination/hiring,
- production deployment,
- tax submission,
- permission elevation,
- destructive deletion,
- high-value pricing override,
- secret access expansion.

## GR-AI-003 — Confidence is not permission [BLOCKER]

A model confidence score cannot bypass:
- authorization,
- policy,
- data scope,
- approval,
- legal rule.

## GR-AI-004 — AI action audit [BLOCKER]

Every material AI action records:
- agent,
- model/provider,
- policy/prompt version,
- context references,
- tool requested,
- validation result,
- approval,
- final result,
- cost,
- latency,
- errors/retries.

## GR-AI-005 — Shadow before sensitive automation [REQUIRED]

New high-impact automated policies must normally pass:
offline evaluation → shadow mode → limited rollout → active.

---

# 9. TypeSafe/Jev Guardrails

## GR-JEV-001 — Jev is a decision provider, not an authority engine [BLOCKER]

Jev may produce typed semantic judgments.

It must not become authoritative for:
- arithmetic,
- financial posting,
- dates,
- tax calculations,
- payroll,
- permissions,
- legal identity validation,
- money movement.

## GR-JEV-002 — Provider abstraction [BLOCKER]

Business modules may not directly depend on TypeSafe SDK.

They use Hayool's `DecisionEngineProvider`.

## GR-JEV-003 — Versioned decision policy [BLOCKER]

Every production Jev decision policy must version:
- decision key,
- question(s),
- criteria,
- state builder,
- provider,
- pinned model,
- threshold,
- deterministic composition,
- autonomy policy,
- evaluation dataset.

## GR-JEV-004 — Persian evaluation [BLOCKER]

A Jev policy used on Persian content requires Persian evaluation data before production automation.

## GR-JEV-005 — No arbitrary threshold [BLOCKER]

Thresholds must come from evaluation evidence, not intuition.

## GR-JEV-006 — Fallback/degradation [BLOCKER]

Core correctness must survive TypeSafe outage/unavailability.

Fallback may be:
- rule-based,
- structured LLM,
- local provider,
- manual review.

## GR-JEV-007 — Commercial boundary [BLOCKER]

Do not expose/resell raw Jev as a standalone service unless current TypeSafe terms explicitly permit it.

Hayool AI Credits meter Hayool platform capability, not raw provider credits.

---

# 10. Multi-Tenancy Guardrails

## GR-TEN-001 — Tenant ownership explicit [BLOCKER]

Tenant-owned records must carry explicit tenant/legal-entity ownership where appropriate.

## GR-TEN-002 — Query scoping [BLOCKER]

Application data access must use approved tenant-scoped repositories/services.

Ad-hoc unscoped queries in tenant-sensitive code are prohibited.

## GR-TEN-003 — RAG/search isolation [BLOCKER]

Search index, embeddings and retrieved knowledge must preserve tenant/document ACL boundaries before model context construction.

## GR-TEN-004 — Shared Talent Network is opt-in [BLOCKER]

Private talent data does not enter shared network visibility without explicit policy/consent.

---

# 11. API and Integration Guardrails

## GR-API-001 — Idempotency for externally retried writes [BLOCKER]

Payment, webhook, external event and retried workflow handlers must be idempotent.

## GR-API-002 — Verify provider callbacks [BLOCKER]

Webhook signature/authenticity verification is mandatory where supported.

## GR-API-003 — Adapter boundary [REQUIRED]

External providers must sit behind Hayool interfaces where provider replacement is foreseeable.

## GR-API-004 — No provider-specific domain leakage [REQUIRED]

Domain models should not contain vendor-specific fields unless isolated to an integration adapter/configuration.

---

# 12. Workflow and Reliability Guardrails

## GR-REL-001 — Durable long-running workflows [BLOCKER]

Multi-hour/day workflows must persist state and resume after worker/process restart.

## GR-REL-002 — Retry is bounded [BLOCKER]

Retries require:
- bounded attempt policy,
- backoff,
- idempotency,
- dead-letter/escalation path.

## GR-REL-003 — No silent partial transaction [BLOCKER]

Critical multi-step financial/business operations must either fully succeed or leave a recoverable/explicitly incomplete state.

## GR-REL-004 — External outage degrades locally [REQUIRED]

Failure of AI/payment/email/SMS/search provider must not corrupt authoritative core state.

---

# 13. Observability Guardrails

## GR-OBS-001 — Correlation ID [REQUIRED]

Important cross-service/workflow actions carry a correlation ID.

## GR-OBS-002 — Structured logs [REQUIRED]

Production logs must be machine searchable and must not contain secrets.

## GR-OBS-003 — Critical path telemetry [REQUIRED]

At minimum observe:
- auth failures,
- workflow failures,
- payment/provider failures,
- queue lag,
- DB health,
- AI provider health/cost,
- error rate,
- latency.

## GR-OBS-004 — Audit != debug log [BLOCKER]

Security/business audit history is a separate authoritative record and must not depend only on ephemeral application logs.

---

# 14. UI/UX Guardrails

## GR-UX-001 — Persian RTL and English LTR are first-class [BLOCKER]

New core UI must not be considered complete if only one direction/language works.

## GR-UX-002 — State completeness [REQUIRED]

Every major interactive view covers:
- loading,
- empty,
- success,
- validation error,
- server error,
- permission denied,
- slow operation.

## GR-UX-003 — No arbitrary tenant JavaScript [BLOCKER]

Tenant theming/configuration may not inject arbitrary JS in V1.

## GR-UX-004 — Safe theming [REQUIRED]

Customization uses approved design tokens/components and must preserve accessibility/RTL/upgrade safety.

## GR-UX-005 — Browser verification [BLOCKER for milestone-critical UI]

Critical milestone flows require staging browser E2E evidence before milestone completion.

## GR-UX-006 — Accessibility [REQUIRED]

Target WCAG 2.2 AA where reasonably applicable; keyboard/focus behavior must be tested for critical flows.

---

# 15. Performance Guardrails

## GR-PERF-001 — No unbounded list loading [BLOCKER]

Large datasets require pagination/cursoring/virtualization as appropriate.

## GR-PERF-002 — N+1 prevention [REQUIRED]

Common list/detail flows must be reviewed for N+1 database access.

## GR-PERF-003 — Expensive AI work is asynchronous when appropriate [REQUIRED]

Long-running AI/analysis tasks should not block normal HTTP request lifetimes.

## GR-PERF-004 — Performance regression evidence [REQUIRED]

High-traffic/core flows get baseline measurements before major performance-sensitive changes.

---

# 16. Dependency and Supply-Chain Guardrails

## GR-DEP-001 — License review [BLOCKER]

A dependency/project with unclear or commercially incompatible licensing cannot be adopted.

## GR-DEP-002 — Dependency health [REQUIRED]

Evaluate:
- maintenance,
- releases,
- known vulnerabilities,
- transitive risk,
- replacement path.

## GR-DEP-003 — SBOM [REQUIRED before production release]

Generate and retain a software bill of materials for release artifacts.

## GR-DEP-004 — Pin/reproducibility [REQUIRED]

Use lockfiles and reproducible build/container versions.

---

# 17. Deployment Guardrails

## GR-DEPLOY-001 — Dev/staging != production [BLOCKER]

The development VPS must not silently become production.

## GR-DEPLOY-002 — Production release gate [BLOCKER]

Production requires:
- successful CI,
- staging verification,
- migration review,
- backup/recovery readiness,
- production approval,
- rollback/forward-fix plan.

## GR-DEPLOY-003 — Dedicated / On-Prem parity [REQUIRED]

Supported deployment modes use the same versioned product release, not divergent hand-edited codebases.

## GR-DEPLOY-004 — Health checks after deploy [BLOCKER]

Deployment is not successful until smoke/health checks pass.

---

# 18. Backup and Recovery Guardrails

## GR-BACKUP-001 — Backup is not validated until restored [BLOCKER before production]

A backup process without a successful restore test is not considered ready.

## GR-BACKUP-002 — Off-host copy [REQUIRED]

Production backups require at least one copy outside the primary host/failure domain.

## GR-BACKUP-003 — Recovery documentation [REQUIRED]

Document restore ownership, sequence, secret/key requirements and expected RTO/RPO.

---

# 19. Completion and Communication Guardrails

## GR-DONE-001 — No false “Done” [BLOCKER]

An agent/developer may not claim a feature/milestone is complete when:
- required tests were not run,
- known blocker exists,
- migration failed,
- staging critical flow was not checked,
- required source-of-truth docs are stale.

## GR-DONE-002 — Known limitations disclosed [REQUIRED]

Completion reports include:
- checks run,
- checks not run,
- known limitations,
- risks,
- follow-up work.

## GR-DONE-003 — Evidence over confidence [REQUIRED]

Statements such as:
- “secure,”
- “production ready,”
- “tested,”
- “compatible”

must be backed by concrete evidence appropriate to the claim.

---

# 20. Mechanical Enforcement Matrix

The repository MUST progressively map important guardrails to controls.

Examples:

| Guardrail family | Mechanical enforcement |
|---|---|
| No direct main | GitHub Ruleset |
| CI must pass | Required status checks |
| Sensitive ownership | CODEOWNERS |
| No secret in Git | Secret scanning / CI |
| Test integrity | Required test jobs + review |
| Tenant isolation | Dedicated CI test suite |
| Permission checks | Dedicated CI tests |
| Migration safety | Migration-check workflow |
| Supply chain | dependency/license/SBOM scan |
| Production gate | Protected deployment environment |
| UI quality | Playwright + visual/accessibility checks |
| Financial invariants | domain invariant tests |
| Jev policies | eval/shadow evidence + path checks |
| Source of Truth | PR template + traceability check |
| Staging validation | required staging/e2e check for release |

M0 must turn this matrix into actual repository controls once exact paths/job names are known.

---

# 21. Waiver process

A REQUIRED or ADVISORY guardrail may be temporarily waived only with:

- waiver ID,
- affected guardrail,
- reason,
- risk,
- owner,
- expiry date,
- mitigation,
- follow-up issue.

A BLOCKER guardrail can only be changed by updating the guardrail itself through an explicitly reviewed high-risk PR.

No “temporary” undocumented bypass.


# 22. Autonomous SDLC Guardrails

## GR-AUTO-001 — Single writer [BLOCKER]
Only one agent may write to a given repair branch at a time.

## GR-AUTO-002 — Reviewer is read-only [BLOCKER]
A reviewer may not modify the implementation branch while acting as reviewer.

## GR-AUTO-003 — SHA-bound approval [BLOCKER]
A gate result applies only to the exact reviewed commit SHA.

## GR-AUTO-004 — Bounded repair [BLOCKER]
Auto-repair requires max iteration, max elapsed time and max cost.

## GR-AUTO-005 — Kill switch [BLOCKER]
Owner can disable autonomous writes/merge/deploy/external-model calls without losing manual operation.

## GR-AUTO-006 — Model identity [BLOCKER]
Requested alias and effective provider/model must both be auditable.

## GR-AUTO-007 — Deterministic failure outranks council [BLOCKER]
Model consensus cannot waive a failing mandatory CI/security/financial/tenancy check.

## GR-AUTO-008 — Governance changes are high risk [BLOCKER]
Changes to CLAUDE.md, AGENTS.md, Constitution, Guardrails, CODEOWNERS, release gates or Autopilot policy require special review.

## GR-AUTO-009 — No high-risk auto-merge without shadow evidence [BLOCKER]
R3/R4 and equivalent sensitive changes cannot become fully automatic merely by configuration convenience.

# 23. Learning Intelligence Guardrails

## GR-LEARN-001 — No silent self-modification [BLOCKER]
Production decision policy/model/threshold cannot change itself directly from live feedback.

## GR-LEARN-002 — Outcome provenance [REQUIRED]
Training/evaluation labels retain source/provenance.

## GR-LEARN-003 — Cross-tenant learning is governed [BLOCKER]
No raw confidential tenant data is reused across tenants without explicit approved policy/legal basis.

## GR-LEARN-004 — High-impact fairness evaluation [BLOCKER]
Employment-related policies require fairness/bias evaluation appropriate to jurisdiction/use case before production automation.

## GR-LEARN-005 — Metric definitions are governed [BLOCKER]
Natural-language BI cannot redefine authoritative finance/operations metrics ad hoc.

# 24. Workforce Decision Guardrails

## GR-WORK-001 — No universal opaque human score [BLOCKER]
Worker performance must remain multidimensional and explainable.

## GR-WORK-002 — Difficulty/context normalization [REQUIRED]
Performance comparison should account for task/role context where material.

## GR-WORK-003 — Employee termination is protected [BLOCKER]
AI may recommend; final termination remains human/approved unless a jurisdiction-specific policy explicitly establishes a lawful alternative.

## GR-WORK-004 — No invasive surveillance by default [BLOCKER]
Keylogging, webcam monitoring, continuous screenshots or off-hours surveillance require separate explicit product/legal decision and are not default features.

## GR-WORK-005 — Engagement mode explicit [BLOCKER]
Software-only, marketplace, managed contractor, managed outcome/team and EOR/AOR relationships must not be conflated.


# 25. Marketplace Integrity Guardrails

## GR-MKT-001 — No price race [BLOCKER]
Public underbidding auction is not a default talent-allocation mechanism.

## GR-MKT-002 — Fair exposure [REQUIRED]
Matching must have a documented cold-start/exploration strategy so historical winners do not monopolize opportunities.

## GR-MKT-003 — Dispute before scale [BLOCKER]
Shared/public network scale requires dispute, abuse-report and appeal workflows.

## GR-MKT-004 — Engagement legality [BLOCKER]
Managed contractor/team/EOR modes cannot activate in a jurisdiction without approved commercial/legal configuration.

# 26. Analytics Guardrails

## GR-DATA-001 — Governed metrics [BLOCKER]
AI cannot invent or redefine authoritative business metrics ad hoc.

## GR-DATA-002 — No unrestricted production SQL [BLOCKER]
General AI analyst agents must query through approved semantic/query interfaces.

## GR-DATA-003 — Prediction uncertainty [REQUIRED]
Material forecasts expose horizon, version and uncertainty/limitations.

## GR-DATA-004 — Baseline test [REQUIRED]
Predictive models should be compared with appropriate simple baselines before production.

# 27. Worker Dignity Guardrails

## GR-HUMAN-001 — Purpose limitation [BLOCKER]
Worker/candidate evidence cannot be silently repurposed into unrelated high-impact decisions.

## GR-HUMAN-002 — No hidden permanent blacklist [BLOCKER]
High-impact restrictions must have evidence, policy, appropriate notice/review and appeal mechanisms where applicable.

## GR-HUMAN-003 — No opaque universal score [BLOCKER]
Human evaluation remains multidimensional with context and uncertainty.

# 28. Critical Test Protection

## GR-TEST-006 — Protected guard tests [BLOCKER]
High-risk invariant/tenant/security/release tests cannot be weakened in the same change without explicit independent review.


# 25. Universal Platform Guardrails

## GR-PLAT-001 — Core stays typed [BLOCKER]
Do not turn core finance/identity/tenant/order/inventory primitives into generic EAV entities to gain flexibility.

## GR-PLAT-002 — Custom schema is governed [BLOCKER]
Custom objects/fields require schema, version, permission, validation and audit.

## GR-PLAT-003 — Industry maturity truth [BLOCKER]
A pack cannot be marketed as production-ready in a regulated industry merely because generic objects exist.

## GR-PLAT-004 — Extension isolation [BLOCKER]
Third-party extensions cannot directly mutate protected core tables, secrets or cross-tenant data.

## GR-PLAT-005 — Studio publish gate [REQUIRED]
High-impact Studio changes use draft/test/approval before production publish.

# 26. Physical Operations Guardrails

## GR-OPS-001 — Inventory movements are auditable [BLOCKER]
Stock changes require explicit movement/adjustment records; no silent quantity overwrite.

## GR-OPS-002 — Reservation/idempotency [BLOCKER]
Order/fulfillment reservation and provider callbacks must prevent duplicate commitment.

## GR-OPS-003 — Multi-provider compensation path [BLOCKER]
A workflow that commits external side effects must define cancellation/refund/compensation behavior.

## GR-OPS-004 — Regulated goods eligibility [BLOCKER]
Restricted product/service categories require explicit jurisdiction/provider eligibility.

## GR-OPS-005 — OT safety boundary [BLOCKER]
Generic Hayool/AI agents cannot directly control safety-critical industrial equipment without a separately approved architecture.

# 27. Algorithm Selection Guardrails

## GR-ALG-001 — Correct engine class [BLOCKER]
Do not use LLM/Jev as an authoritative substitute for deterministic arithmetic, permissions or mathematical optimization.

## GR-ALG-002 — Solver constraint integrity [BLOCKER]
Hard business/legal/safety constraints remain hard constraints; do not convert them to soft preference weights for convenience.

## GR-ALG-003 — Prediction uncertainty [REQUIRED]
Forecast/prediction shown to users includes horizon/uncertainty/data-quality context.

# 28. Globalization Guardrails

## GR-GLOB-001 — Country readiness [BLOCKER]
A country feature is market-ready only after relevant country-pack validation.

## GR-GLOB-002 — Locale != law [BLOCKER]
Translating UI or formatting currency is not legal/tax/payroll localization.

## GR-GLOB-003 — Standard != certification [BLOCKER]
Supporting ISO/GS1/Peppol/ISA mappings does not imply regulatory certification.

# 29. Offline / Edge Guardrails

## GR-EDGE-001 — Offline actions are classified [BLOCKER]
Financial finalization, permission-sensitive or legally authoritative actions may require online server validation.

## GR-EDGE-002 — Sync conflict policy [BLOCKER]
Offline-writable entities require documented conflict/idempotency behavior.

## GR-EDGE-003 — Edge credentials scoped [BLOCKER]
Edge gateways use scoped device identity/credentials and cannot receive tenant-wide master secrets.


# 30. Extension Platform Guardrails

## GR-EXT-001 — Clean core [BLOCKER]
Customer/third-party extensions MUST NOT patch protected core source or directly mutate protected core tables.

## GR-EXT-002 — Untrusted code isolation [BLOCKER]
Untrusted third-party code cannot execute inside the main API process.

## GR-EXT-003 — Scoped app identity [BLOCKER]
Every extension operates as its own scoped principal; it does not inherit installer privileges.

## GR-EXT-004 — Permission expansion approval [BLOCKER]
Material new scopes, protected data or egress require re-approval according to tenant policy.

## GR-EXT-005 — Manifest/version [BLOCKER]
Installable extensions require identity, version, dependencies, permissions, data/egress declarations and compatibility metadata.

## GR-EXT-006 — Stable public contracts [REQUIRED]
Partner code uses public API/event/SDK surfaces rather than internal implementation details.

## GR-EXT-007 — Safe uninstall [REQUIRED]
App uninstall defines retained/deleted data and cannot silently destroy unrelated tenant records.

## GR-EXT-008 — Marketplace data transparency [BLOCKER]
An app must disclose the data/processors/egress it uses before installation.

## GR-EXT-009 — Protected data review [BLOCKER]
Apps requesting high-sensitivity HR/financial/identity/regulated data receive elevated review.

# 31. Rational AI Use Guardrails

## GR-AICOST-001 — AI necessity [REQUIRED]
New metered AI calls require a documented reason why deterministic/search/solver/statistical alternatives are insufficient.

## GR-AICOST-002 — Cost attribution [BLOCKER for paid AI]
Metered AI usage must be attributable to feature/tenant/provider/model and cost.

## GR-AICOST-003 — Core without AI [BLOCKER]
Failure/disablement of external AI must not prevent essential accounting, order, inventory, HR records or core workflow operation.

## GR-AICOST-004 — AI budget [REQUIRED]
Tenant/platform AI budgets and hard caps are enforceable.

## GR-AICOST-005 — Quality/cost routing [REQUIRED]
Model choice should use measured evaluation/cost rather than prestige/defaulting to the most expensive model.

# 32. Pricing Guardrails

## GR-PRICE-001 — Margin floors [BLOCKER]
Automatic pricing/discounting cannot breach configured hard margin/price floors.

## GR-PRICE-002 — Margin definitions [BLOCKER]
Do not label transaction-level estimated margin as accounting net profit.

## GR-PRICE-003 — Experiment scope [BLOCKER]
Price experiments require defined cohort, hypothesis, metrics and bounds.

## GR-PRICE-004 — Sensitive personalized pricing [BLOCKER]
Protected/sensitive personal traits cannot be used for hidden individualized price optimization.

## GR-PRICE-005 — Price version audit [REQUIRED]
Material price changes retain price/cost/policy/experiment version and approval history.

## GR-PRICE-006 — AI cannot invent objective [BLOCKER]
The optimization objective and minimum profitability constraints are set by management policy.

