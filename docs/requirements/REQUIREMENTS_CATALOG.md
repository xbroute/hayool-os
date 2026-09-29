# Hayool OS V7.2 — Requirements catalog

Status: specified/design baseline, 2026-09-26. No row asserts implementation, legal clearance or market readiness. All 138 V7.1 IDs remain present; 37 broad rows were refined and 56 new IDs added, with explicit mapping in `GRANULARITY_REVIEW.md`. `REQ` IDs are immutable; a changed obligation gets a revision and impact review. Source pointers refer to the preserved V6 master (`M§`) or V7 proposal (`V7/NN`) and adopted detail, with explicit overrides in `CONFLICT_RESOLUTIONS.md`. `R` is release outcome target, not a promise of general availability. `Post` means preserved beyond V1.10. Every row inherits the command, state, auth, idempotency, audit, data lifecycle, error and positive/negative/concurrency/failure acceptance contracts in `DOMAIN_CONTRACTS.md`, `TESTING_STRATEGY.md` and relevant adopted source. Its stable planned test-contract ID is `TEST-<REQ-ID>`; the parenthesized suites in the proof column are blocking suites, and the prose is the independently reviewable oracle. Executed EVID records must attach at the relevant gate. Unknown facts fail closed for consequential actions. No feature is waived by a later target. **Any external AI use in any earlier release must first pass REQ-AI-003–007 and ODR-006 for that exact processor, data class and jurisdiction; otherwise the manual/AI-off path is mandatory.**

## Governance and engineering (owner: Engineering/Policy; ADR-001–005, 023–026)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-GOV-001 | Maintain versioned authority, conflict ledger, source coverage, decisions and claims; never promote an inherited assertion to fact. | Change trace to original and approval; stale claim rejected (AUTO). | M0.1 | V7/01,09; M§0 |
| REQ-GOV-002 | Carry independent readiness states for specified/design/code/test/security/a11y/staging/jurisdiction/market/production/deploy. | Missing evidence remains pending (AUTO). | M0.1 | V7/09,14 |
| REQ-GOV-003 | Require owner signature for irreversible legal/commercial/capital/market policy; technical ADR cannot grant it. | Unauthorized activation blocked (AUTO,POL). | M0.1 | V7/09 |
| REQ-GOV-004 | Bind each implementation PR to REQ, ADR, test, migration, risk and evidence links. | Untraceable PR fails gate (AUTO). | M0.0 | V7/03,09 |
| REQ-GOV-005 | Use protected repo, isolated writer, read-only independent reviews and exact SHA checks. | Stale SHA or reviewer write stops merge (AUTO). | M0.0 | V7/03; M§61 |
| REQ-GOV-006 | Bound repair iterations, time and cost; preserve failing tests and secrets; support kill switch. | Seeded budget/secret/test violation halts (AUTO). | M0.0 | V7/03; M§61 |
| REQ-GOV-007 | Validate one shadow PR end to end before autonomous merge/deploy authority. | Full ENG-RUN trace; no product action without gate (AUTO). | M0.0 | V7/03 |
| REQ-GOV-008 | Monitor dependencies, CVEs, provider/model/terms, jurisdiction sources and compatibility; propose reviewable changes only. | Changed term opens candidate, no live policy drift (AUTO). | M0.0, ongoing | V7/03 |
| REQ-GOV-009 | Conduct exact repository-SHA architecture/REQ/ADR/guardrail review and close blockers. | Independent review on same SHA; M0.2 pass only then (AUTO). | M0.2 | V7/03,14 |
| REQ-GOV-010 | Preserve threat/risk/decision/evidence provenance and revalidate on affected change. | Expired proof cannot pass release (AUTO). | all | V7/09,14 |

## Identity, tenancy, permission and operations (owner: Identity/Organization/Operations; ADR-005–009)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-PLAT-001 | Model tenant and actor/service/app identities, memberships, roles and scoped delegation. | Cross-tenant/expired delegated action denied (TEN,AUTH). | V1.0 | M§4,8 |
| REQ-PLAT-002 | Authenticate with secure sessions/MFA for privileged roles, recovery and revocation. | Revoked session/action denied (AUTH). | V1.0 | M§8,54 |
| REQ-PLAT-003 | Enforce application auth plus composite tenant foreign keys and FORCE RLS with non-bypass runtime role. | A cannot read/write B even via FK/SQL (TEN). | V1.0 | M§8,54; V7/04 |
| REQ-PLAT-004 | Derive transaction-scoped tenant context from verified membership; reset on pooled connection. | Absent/stale context denies access (TEN). | V1.0 | V7/04 |
| REQ-PLAT-005 | Apply isolation to jobs, cache, object grants, search, counts, snippets, RAG, analytics, realtime, export, logs and restore. | Side channel yields no B existence (TEN). | V1.0 | M§53,54,73; V7/04 |
| REQ-PLAT-006 | Enforce field/action/row scopes before search or AI and recheck current access on download. | Consent/membership revocation immediate (AUTH,TEN). | V1.0 | M§8,42,53 |
| REQ-PLAT-007 | Keep global authentication subject minimal; private tenant HR/contact data stays tenant-owned. | Dual-membership has no implicit cross-tenant join (TEN). | V1.0 | M§8,10 |
| REQ-PLAT-008 | Support Cloud, Dedicated and On-Prem deployment with same contracts and isolated administration. | Mode-specific isolation/upgrade/export (OPS,TEN). | V1.9 | M§7,59 |
| REQ-PLAT-009 | Provide signed offline license with explicit grace/read-only/export semantics, not data destruction on expiry. | Renewal after expiry recovers data (OPS). | V1.9 | M§57,59 |
| REQ-PLAT-010 | Provision tenant, verified domain, scoped admin, entitlement and onboarding workflow without privilege bleed. | Second tenant starts independent journey (GJ-02,AUTH). | V1.1 | M§74,75 |
| REQ-PLAT-011 | Version plans, entitlements, usage and restrictions centrally; reconcile feature grants to contracted plan. | Expiry/retry cannot create unauthorized grant (AUTH,FIN). | V1.6 | M§57,74 |
| REQ-PLAT-012 | Provide backup and point-in-time compatible restore across transactional, blob, config and privacy tombstone state. | Restore meets declared RPO/RTO profile and reconciles ledger/rights (OPS,DATA). | V1.0 | M§56,59 |
| REQ-PLAT-013 | Govern master party/item/resource identifiers, deduplication candidates, reference-data lineage and reversible merge/unmerge. | Duplicate import resolves without lost links; conflicting source produces review and provenance (DATA,TEN). | V1.1 | M§104 |
| REQ-PLAT-014 | Tenant branding covers verified domain, login, theme presets, favicon and approved document/email templates with accessible fallback. | Tenant A's mark never appears in B's portal/email; broken theme falls back (UX,TEN). | V1.1 | M§75 |
| REQ-PLAT-015 | Support/operations access is separately granted with reason, limited entity/field scope, expiry, recording and revocation. | Expired/revoked support principal cannot view tenant data or derived export (AUTH,TEN). | V1.1 | M§8,56 |
| REQ-PLAT-016 | Versioned application/schema upgrade uses migration plan, staged rollout, compatibility test and rollback/forward repair. | GJ-02 upgrade preserves finance, permissions, custom schema and restored tenant data (OPS,EXT). | V1.1 | M§59 |
| REQ-PLAT-017 | Organization owns effective-dated legal entities, branches, departments and teams with lawful scoped membership, separate from financial center ownership. | Reparented team cannot gain cross-entity data or retroactively rewrite budget/ledger (TEN,AUTH). | V1.0 | M§4 |
| REQ-PLAT-018 | Independently monitor service health and operational telemetry across API, workflows, providers, queues, storage, financial side effects and backup; redact sensitive context and keep local diagnostics in On-Prem mode. | Fault injection triggers scoped readiness/lag/dead-letter/backup-age alerts and correlated redacted traces without secret or other-tenant disclosure (OPS,SEC). | V1.0 | M§56,59; V7/04 |

## Work, clients and collaboration (owner: CRM/Commercial/Work/Knowledge; ADR-004,007,008)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-WRK-001 | Capture discovery, client need and source-backed requirements with draft/approved distinction. | GJ-01A scope links sources; conflicting input opens revision (WORK). | V1.0 | M§16,26 |
| REQ-WRK-002 | Version scope, assumptions, change requests, acceptance and client signoff. | Changed work cannot inherit stale acceptance (WORK). | V1.0 | M§15,16 |
| REQ-WRK-003 | Represent goal, capability, project, work unit, dependency, owner and auditable state in Work Graph. | Cyclic dependency denied, accepted outcome traced (WORK). | V1.0 | M§4,15 |
| REQ-WRK-004 | Estimate and quote approved scope with versioned price/rule/currency snapshot and expiry. | Recompute original quote; edited estimate requires new approval (WORK,FIN). | V1.0 | M§19,27 |
| REQ-WRK-005 | Distinguish tracked/submitted/approved/billable/payable time with calendar and overlap rules. | Only approved quantities feed invoice/payroll (WORK,FIN). | V1.0 | M§17 |
| REQ-WRK-006 | Reserve capacity with calendar/time zone/leave and atomic competing requests. | Infeasible plan explained; no double allocation (WORK). | V1.0 | M§18 |
| REQ-WRK-007 | Manage delivery review, evidence-based acceptance and client dispute with scoped authority. | Client dispute retains original acceptance and audited revision (WORK). | V1.0 | M§15 |
| REQ-WRK-008 | Keep versioned risk register, triggers, owner and mitigation linked to work and KPI. | Unowned/stale risk cannot show resolved (WORK). | V1.0 | M§15,70,72 |
| REQ-WRK-009 | Govern KPI metric definitions, baselines, measurement windows, sources and outcome comparison. | Metric version and freshness reconstruct; no invented improvement (WORK). | V1.0 | M§24,70 |
| REQ-WRK-010 | Orchestrate Meeting -> policy/consent -> authorized media or manual notes -> transcript/summary -> decision/task/requirement/risk/follow-up draft -> human approval -> source-linked outcome. | AI-off fa/en meeting completes end to end; no draft becomes authoritative without configured approval (MEET,WORK). | V1.0 manual; AI gated | M§34 |
| REQ-WRK-011 | Support client portal for scoped status, deliverables, approvals, invoices and ticket exchange. | Client A cannot infer client B; approve/reject audited (AUTH,UX). | V1.1 | M§31 |
| REQ-WRK-012 | Support ticket intake, severity, assignment, customer communication, resolution and reopen are scoped and auditable. | Ticket routing/reopen works after outage, wrong client sees nothing (SUP,AUTH). | V1.1 | M§32 |
| REQ-WRK-013 | Customer Health shows dimensional payment, delivery, support and renewal facts with freshness. | Missing input reads unknown/stale, not healthy (WORK,AI). | V1.1 | M§32 |
| REQ-WRK-014 | Service packages define limits, add-ons, exclusions, recurrence and SLA with approved quote snapshot. | Package amendment never retroactively alters contract (FIN,WORK). | V1.0 | M§27 |
| REQ-WRK-015 | Reconcile attribution and marketer commission to collected cash, reversals and scoped approvals. | Refund produces clawback; no duplicate payout (FIN). | V1.1 | M§33 |
| REQ-WRK-016 | Conversation threads retain participants, visibility, consent and versioned source links. | Revoked participant cannot retrieve old or new thread content (AUTH,WORK). | V1.1 | M§69 |
| REQ-WRK-017 | Role dashboards and executive command center link metrics to authorized underlying facts. | No false aggregate/tenant leak (TEN,AI). | V1.5 | M§78 |
| REQ-WRK-018 | Process intelligence identifies bottleneck/variance from timestamped evidence. | Counterfactual recommendation labeled and reviewable (AI,WORK). | V1.5 | M§88 |
| REQ-WRK-019 | Incident Management records severity, affected customers/services/assets, timeline, owner, communications, mitigation, resolution, root cause, postmortem, follow-up and project/asset/ticket/security links; distinct from risk and issue. | Cross-client outage produces complete scoped evidence and independent state transitions (INC,AUTH). | V1.0 | M§72 |
| REQ-WRK-020 | CRM/Sales manages lead, account, contact, opportunity, stage, attribution and handoff to scoped discovery/quote. | Won/lost opportunity and client handoff retain provenance; no cross-client leak (CRM,AUTH). | V1.0 | M§26,33 |
| REQ-WRK-021 | Issue register handles actual work defects/blockers, severity, owner, fix verification and linked risk/incident. | Closing issue never closes linked incident or risk (WORK). | V1.0 | M§15 |
| REQ-WRK-022 | Change control versions scope/impact/cost/approval and invalidates affected quote, plan or acceptance. | Unauthorized changed requirement cannot inherit prior signoff (WORK,FIN). | V1.0 | M§15,16 |
| REQ-WRK-023 | SLA policy defines service calendar, start/pause/resume, breach/escalation and version per customer/service. | Boundary/DST/late-event clock independently recomputed from evidence (SLA,WORK). | V1.1 | M§32 |
| REQ-WRK-024 | Meeting capture/import handles country policy and consent per participant, audio/video/manual paths, optional timestamped speaker transcription and ACL. | Denied/withdrawn capture sends no media to processor; unknown speaker/timing labeled (MEET,POL). | V1.0 manual; provider gated | M§34 |
| REQ-WRK-025 | Meeting-derived summary, decisions, tasks, requirements, risks and follow-up are source-linked drafts with version-bound review/approval. | Stale transcript or rejected draft creates no authoritative Work command (MEET,WORK). | V1.0 manual; AI gated | M§16,34 |
| REQ-WRK-026 | OKR aligns objectives, key results, owner, review cycle and approved KPI references without rewriting historical goals. | Revised key result retains baseline and evidence; no KPI score fabricates achievement (WORK). | V1.0 | M§24,70 |
| REQ-WRK-027 | Form engine versions schema, validation, submission, field ACL and approval workflow. | Old form submission migrates or stays readable; sensitive field denied (AUTH,WORK). | V1.1 | M§69 |
| REQ-WRK-028 | Notification engine versions templates, recipient preference/consent, retry and delivery evidence. | Duplicate event sends at most one permitted notice, failure visible (WORK,OPS). | V1.1 | M§69 |
| REQ-WRK-029 | Meeting transcription/semantic adapters are provider-neutral with local/private route, AI-off fallback, fa/en support, retention/deletion and derivative revalidation. | Provider outage/consent revocation uses manual path; deleted media does not reappear after restore (MEET,DATA). | First AI use gated; broad V1.5 | M§34,37,55 |
| REQ-WRK-030 | Contract/signature lifecycle preserves counterparty, scope, approval, signature evidence, amendment and obligation snapshot independent of quote. | Ambiguous signature stays pending; changed quote cannot inherit signed contract (WORK,FIN). | V1.0 | M§28 |

## Talent, engagement and people (owner: People/Network/Policy; ADR-010–012,016)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-TAL-001 | Separate private talent HR data from purpose-limited, consented, revocable public Network projection. | Opt-out removes visibility; restore does not resurrect (TEN,DATA). | V1.2 | M§10,50 |
| REQ-TAL-002 | Verify capabilities, grades, evidence, availability and claims without universal person score. | Unverified capability labeled; correction path (POL,AI). | V1.2 | M§11,12,52 |
| REQ-TAL-003 | Recruit through intake, screening, consent, review, appeal and documented decisions. | Candidate sees applicable decision; prohibited inference denied (POL,UX). | V1.2 | M§12,51 |
| REQ-TAL-004 | Resolve sourcing eligibility before candidate discovery, count, ranking, contact or invitation. | Ineligible/unknown omitted, including facets (POL,TEN). | V1.2 | V7/02; M§10,14 |
| REQ-TAL-005 | Iran product sourcing mode defaults to DOMESTIC_ONLY; the approved Country/Jurisdiction Pack declares its own required facts and domestic evaluator, with unknown facts pending and excluded before discovery. | No pack/no required fact yields no rankable candidate; nationality/IP shortcut denied; no legal conclusion inferred (POL). | V1.2 | V7/02; owner V7.2 clarification |
| REQ-TAL-006 | Other approved packs explicitly choose DOMESTIC_ONLY, REGIONAL, ALLOWLIST_COUNTRIES or GLOBAL_IF_ELIGIBLE sourcing subject to pack-declared facts and all corridor obligations. | Synthetic countries show distinct pools; missing required facts never enter facets or rank (POL). | V1.2, V1.9 | V7/02 |
| REQ-TAL-007 | Matching explains hard eligibility, capabilities, availability, conflicts, price and uncertainty with human review. | Fair exposure/appeal and no disallowed candidate (POL,AI). | V1.2 | M§14,50,51 |
| REQ-TAL-008 | Team builder solves skill/time/cost/constraints with infeasibility explanation and approvals. | Solver repeatability and feasible reservation (WORK,AI). | V1.3 | M§9,14 |
| REQ-TAL-009 | Workforce architect models role/team plan, utilization, grade gap, hiring and scenario without auto-firing/hiring. | Scenario comparison traces assumptions (AI,WORK). | V1.3 | M§9,22 |
| REQ-TAL-010 | Explicitly select employment/contractor/managed/outcome engagement and responsible employer, payer and IP party. | Unsupported jurisdiction/mode cannot contract (POL). | V1.4 | M§23; V7/02 |
| REQ-TAL-011 | Compensation rules and floors are independent of client price and AI score; legal/fair minimum cannot be overridden. | Below-floor proposal blocked (FIN,POL). | V1.4 | M§20 |
| REQ-TAL-012 | Payroll uses approved entitlement/rules and authorized review before posting/payment. | Tracked time alone pays nobody; replay exact (FIN,POL). | V1.4 | M§24,25 |
| REQ-TAL-013 | Managed marketplace governs delivery evidence, dispute and settlement hold/release under approved opt-in terms and assigned liability. | Disputed work cannot silently settle; decision/reversal cites responsible party and evidence (WORK,FIN). | V1.4 | M§13 |
| REQ-TAL-014 | Employment-AI candidate changes use offline evaluation, bias review, shadow/limited rollout and appeal; deterministic/human path remains available. | Adverse subgroup/rights blocker stops AI activation; no external AI without ODR-006 and AI controls (AI,POL). | V1.2 governance; AI gated | M§51; V7/07 |
| REQ-TAL-015 | ATS assessments/interviews/tests have consent, scoring rubric, reviewer, accommodation, appeal, evidence and version independently of general applicant stages. | Candidate can contest/review an assessment; AI-off and inaccessible test fallback work (POL,UX). | V1.2 | M§12,51 |
| REQ-TAL-016 | Managed-network vetting independently verifies scoped qualifications, evidence, consent, reviewer and revocation before assignment. | Unvetted/revoked talent cannot accept managed work; reviewer decision and appeal trace persist (POL,AUTH). | V1.4 | M§13 |
| REQ-TAL-017 | Managed-work replacement independently records trigger, worker/client notice, approval, handoff and liability/compensation allocation under reviewed terms. | Replaced work keeps both parties' evidence and approved responsibility; no duplicate bill or pay (WORK,FIN). | V1.4 | M§13 |

## Global policy, providers and interoperability (owner: Policy; ADR-010–012)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-GLB-001 | Resolve Jurisdiction Context from all relevant parties, entity, worker location, service, data route, currency and provider. | Tenant country alone cannot authorize (POL). | V1.0 | V7/02 |
| REQ-GLB-002 | Compose Global, Country/Subnational, industry, provider and tenant constraints restrictively. | Conflict/unknown blocks affected action with obligations (POL). | V1.0 | V7/02,04 |
| REQ-GLB-003 | Return typed executable/blocked/pending decision with policy and fact versions, reasons and expiry. | Pending never interpreted as allow (POL). | V1.0 | V7/02 |
| REQ-GLB-004 | Re-evaluate eligibility at dispatch after approval and on queued/retry operations. | Revoked policy stops previously queued action (POL,OPS). | V1.0 | V7/02 |
| REQ-GLB-005 | Country pack covers entity/work/tax/payroll/banking/payment/AI/data/commerce/localization/accessibility and evidence. | Empty jurisdiction remains unavailable, not green (POL). | V1.2 | V7/02,07 |
| REQ-GLB-006 | Provider registry binds capability, country/corridor, terms, residency, currency, status, owner, expiry and fallback. | Ineligible fallback denied; outage state visible (POL,OPS). | V1.2 | V7/02 |
| REQ-GLB-007 | Separate pack design maturity, publisher/support ownership and runtime eligibility. | Documented pack not executable until reviewed (POL). | V1.2 | V7/02 |
| REQ-GLB-008 | Translate/localize legal content with reviewed version and effective scope; support Jalali presentation and explicit IRR/Toman. | Wrong calendar/unit cannot silently enter contract (UX,FIN). | V1.0, V1.9 | M§30,87,85 |
| REQ-GLB-009 | Govern cross-system data interoperability with schema mapping, provenance, identifier matching and versioned contract; import/export and public API have separate owners. | Cross-system round trip declares nonportable fields and retains source lineage (DATA,EXT). | V1.1, V1.9 | M§73,98 |
| REQ-GLB-010 | Screen transaction/engagement counterparties and restricted corridors against current approved applicable policy, with scoped review and appeal; data-transfer controls are separately governed by REQ-TRU-005. | Unknown/flagged counterparty blocks affected transaction with evidence, qualified review and no inferred legal blanket claim (POL). | V1.4, V1.9 | V7/02,07 |
| REQ-GLB-011 | Each Country/Jurisdiction Pack declares sourcing modes, required fact schemas and versioned domestic/region/allowlist evaluator; Core interprets typed policy results, never fixes a country's legal definition. | Missing pack/fact fails pending before count/rank; revised pack changes synthetic eligibility with audit (POL,TEN). | V1.2 | V7/02; V7.2 owner clarification |

## Financial, pricing and commercial (owner: Finance/Pricing/Subscription; ADR-014–015)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-FIN-001 | Keep legal-entity/book double-entry journals balanced in exact decimal functional currency. | Independent trial balance equals zero (FIN). | V1.0 | M§29,67 |
| REQ-FIN-002 | Freeze posted lines; corrections are linked reversal/adjustment and closed period stays locked. | Update/delete/repost rejected (FIN). | V1.0 | M§29 |
| REQ-FIN-003 | Version money precision, currency exponent and rounding boundary/method in authoritative financial rule snapshots. | Original money result reproduces exactly across retry and reversal (FIN). | V1.0 | M§19,85 |
| REQ-FIN-004 | Model client invoice/receivable, allocation, partial receipt, overpayment, credit/refund, chargeback and aging. | AR matches exact ledger and settlement after out-of-order events (FIN,PAY). | V1.0 | M§29,45,67 |
| REQ-FIN-005 | Deduplicate provider attempts/webhooks; ambiguous payment remains reconciliation-pending before retry. | Timeout after capture makes one charge only (PAY). | V1.0 | M§45 |
| REQ-FIN-006 | Reconcile external settlement, provider fees and ledger; differences create cases, not hidden postings. | Partial refund and fee discrepancy visible (FIN,PAY). | V1.0 | M§29,45 |
| REQ-FIN-007 | Calculate quote cost waterfall, gross/contribution/fully-loaded margin with explicit zero-denominator behavior. | Independent scenario recomputes (FIN). | V1.0 | M§19,113 |
| REQ-FIN-008 | Enforce versioned client business price floor and scoped management exception without changing contracted terms. | AI/unauthorized user cannot override; below-floor quote blocked without valid exception (FIN,AUTH). | V1.0 | M§19,113 |
| REQ-FIN-009 | Govern rate-book currencies, units, effective dates and grandfathered contract terms. | Retroactive rate change rejected; original quote reproducible (FIN). | V1.0 | M§21,27 |
| REQ-FIN-010 | Govern recurring billing, plan change, proration, credit, refund and collection independently of client delivery revenue. | Contract/usage/invoice reconcile (FIN). | V1.6 | M§57,67 |
| REQ-FIN-011 | Distinguish tenant operating books, Hayool product economics and corporate statutory books. | GMV not counted as platform revenue (FIN). | V1.6 | V7/06 |
| REQ-FIN-012 | Maintain 36-month conservative/base/upside operating and liquidity scenarios with dated sourced inputs. | Sensitivity, runway and collection delay reproducible (FIN). | V1.6 | V7/06 |
| REQ-FIN-013 | Pricing Lab pre-registers cohorts, guardrails, stop criteria and owner approval before experiment. | Harm/guardrail stop works; no live unknown-price change (FIN,AI). | V1.5 | M§114 |
| REQ-FIN-014 | AI credits reserve/reconcile/release atomically, attribute actual provider/model/tool usage and honor cap. | Parallel jobs never overspend or double charge (FIN,AI). | V1.5 | M§38,112 |
| REQ-FIN-015 | Separate marketplace/managed/SaaS/AI/implementation stream economics, funded payout reserves and cash bridge. | Stream contribution and liability reconcile to cash (FIN). | V1.4, V1.6 | M§58,119; V7/06 |
| REQ-FIN-016 | Procurement/expense/vendor approvals produce controlled payable and cost-center/project attribution. | Unapproved expense cannot post as paid (FIN). | V1.7 | M§68 |
| REQ-FIN-017 | Enterprise accounting expansion is activated per reviewed legal entity, book and jurisdiction, with no implicit statutory reporting claim. | Unsupported accounting mode remains unavailable (FIN,POL). | V1.9 | M§103 |
| REQ-FIN-018 | BudgetPlan by legal entity/branch/department/team/project/cost center, period/currency and original/approved/revised version is independently authorized. | Recreate all baselines; cross-entity or stale revision denied (BUD,AUTH). | V1.0 | M§4,29; V7.2 owner |
| REQ-FIN-019 | Cost Center and Profit Center hierarchies, assignment, effective date and ledger/project accounting dimensions are governed separately from budget values. | Reassignment never rewrites old posted dimensions; roll-up does not double count (BUD,FIN). | V1.0 | M§4,29 |
| REQ-FIN-020 | Budget consumption distinguishes committed, ledger-backed actual and separately versioned forecast, with release/reconciliation and currency/period mapping. | Concurrent reservations and partial invoice/refund conserve budget; actual reconciles to posted journal (BUD,FIN). | V1.0 | M§29,68; V7.2 owner |
| REQ-FIN-021 | Variance against approved/revised baseline triggers versioned thresholds, approvals, escalation and project profitability drilldown. | Split purchase/stale approval cannot evade threshold; variance and margin trace to sources (BUD,FIN). | V1.0 | M§19,29; V7.2 owner |
| REQ-FIN-022 | Discount Guardrails use versioned eligibility, threshold, non-stacking rules, expiration, approvals and protected margin/compensation constraints. | Concurrent discounts or channel split cannot undercut floor; exception leaves audit and original contract intact (FIN,AUTH). | V1.0 | M§27,113 |
| REQ-FIN-023 | Vendor payable/expense lifecycle records obligation, invoice, approval, payment allocation, credit and aging separately from receivables. | AP posting and supplier refund reconcile to ledger; unapproved obligation cannot pay (FIN). | V1.0 foundation; V1.7 breadth | M§29,68 |
| REQ-FIN-024 | Worker compensation floor and approved rate policy are independent of client price, margin and business-floor exception. | Underfloor offer denied despite client discount approval; original rate reproducible (FIN,POL). | V1.2/1.4 | M§20 |
| REQ-FIN-025 | Principal/agent revenue recognition basis is explicitly reviewed per stream/jurisdiction before gross/net reporting. | GMV/take-rate and payout never inflate recognized Hayool revenue (FIN,POL). | V1.4/1.6 | M§58,119; V7/06 |
| REQ-FIN-026 | FX source, rate type/effective time, currency conversion and remeasurement policy are versioned separately from rounding. | Historical cross-currency journal reproduces from recorded rate, missing rate blocks (FIN). | V1.0 | M§85 |
| REQ-FIN-027 | Intercompany accounting creates paired entity transactions with elimination mapping and separate approvals. | Both books balance; orphan side flagged, not hidden by consolidation (FIN). | V1.9 | M§103 |
| REQ-FIN-028 | Tax/e-invoice pack owns official identifiers/numbering, validation, submission and correction with qualified jurisdiction review. | Failed submission remains pending; void/reissue never reuses number (FIN,POL). | V1.9 | M§103 |
| REQ-FIN-029 | Revenue recognition policy distinguishes performance obligation, accrual, deferral and principal/agent basis per stream. | Contract amendment and partial delivery produce reproducible schedule (FIN,POL). | V1.9 | M§103 |
| REQ-FIN-030 | Fixed-asset accounting independently links qualified Asset records to capitalization, depreciation/amortization schedule, impairment and disposal with posted ledger truth. | Schedule/revision/disposal reproduce independent journal lines; asset metadata never posts or rewrites accounting history by itself (FIN,AST). | V1.9 | M§35,103 |

## AI, data and outcomes (owner: Analytics/AI; ADR-016–017)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-AI-001 | Route work to deterministic, retrieval, solver, predictive, semantic or generative engine based on task contract. | Money/auth/tax never delegated to LLM (AI). | V1.0 | V7/04; M§100,111 |
| REQ-AI-002 | Keep core product usable when all external AI disabled; degrade explicitly. | GJ-01A succeeds AI-off (AI,WORK). | V1.0 | M§37,111 |
| REQ-AI-003 | Govern provider/model allowlist, data classes, region, terms, cost, fallback and effective version. | Missing DPA/eligibility denies call (AI,POL). | First external AI call; broad V1.5 | M§37,112; V7/07 |
| REQ-AI-004 | Enforce retrieval ACL before context; treat retrieved text, tool results and app output as untrusted. | Injection cannot grant scope/secrets (AI,AUTH). | First external AI call; broad V1.5 | M§42,54 |
| REQ-AI-005 | Trace prompt/template/algorithm/knowledge/policy versions, evidence, confidence and human decision. | Replay decision provenance; cannot invent citation (AI). | First external AI call; broad V1.5 | M§41,47 |
| REQ-AI-006 | Evaluate high-impact change offline, shadow, limited and active with rollback and drift stop. | Failing fairness/safety metric blocks promotion (AI). | First relevant AI activation; broad V1.5 | M§40,51,71 |
| REQ-AI-007 | Cost reserve/provider selection respects tenant/project/user/agent caps and user-visible consumption. | Race/timeout reconciled without cap bypass (AI,FIN). | First external AI call; broad V1.5 | M§38,112 |
| REQ-AI-008 | Build governed Work Graph and capability ontology with versioned typed edges and authoritative source refs. | No inferred edge grants permission/payment (AI,TEN). | V1.3 | M§4; data spec |
| REQ-AI-009 | Outcome learning uses consented, minimized, aggregated signals with quality/bias/drift checks. | Withdrawal removes contribution as policy permits (AI,DATA). | V1.5 | M§47,50 |
| REQ-AI-010 | Personal copilot proposes source-cited, permission-scoped user tasks/next actions as drafts with explicit approval and AI-off fallback. | Revoked source or rejected suggestion cannot mutate Work, leak hidden facts or silently reappear (AI,WORK). | V1.5 | M§79 |
| REQ-AI-011 | Forecasts label horizon, calibration, uncertainty, data quality and version; dashboard drilldown. | Stale or weak data not confident forecast (AI). | V1.5 | M§48,49 |
| REQ-AI-012 | Digital workers and agents receive scoped identity, budget, tool allowlist, approval threshold and suspension. | App cannot perform privileged cross-tenant action (AI,AUTH). | V1.5 | M§39,40 |
| REQ-AI-013 | Jev/TypeSafe is optional semantic adapter; benchmark and approved terms before use. | Equivalent task routes with Jev absent (AI). | V1.5 | M§41; V7/04 |
| REQ-AI-014 | Cross-tenant learning is separately consented and privacy-reviewed, with no raw private pooling. | Tenant revocation stops future use (AI,DATA). | V1.9 | M§50 |
| REQ-AI-015 | Business Digital Twin maintains typed, versioned scenario state tied to real Work/Resource/Transaction facts, with simulated assumptions distinguished from authority. | Replayed scenario explains divergence; simulation cannot post money or work (AI,FIN). | V1.5 | M§36 |
| REQ-AI-016 | Product analytics captures consented activation/adoption/retention/error funnels separately from customer business metrics, with opt-out and privacy budget. | Opt-out stops nonessential telemetry; cohort metric reconstructs source events (AI,DATA). | V1.1 | M§76 |
| REQ-AI-017 | AI Project Architect proposes cited scope, dependency, resource and economics scenarios as drafts under versioned budget/capacity/policy constraints. | Infeasible or stale proposal is labeled and rejected; no plan, assignment, spend or authoritative requirement appears before approval (AI,WORK). | V1.5 | M§80 |

## Studio, developer and marketplace (owner: Studio/Extensions; ADR-018–020)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-EXT-001 | Route variability configuration -> Studio -> low-code -> Remote pro-code -> Core only by integrity test. | New tenant workflow works without Core fork (EXT). | V1.0, V1.7 | M§92,115; V7/08 |
| REQ-EXT-002 | Studio owns bounded versioned custom schemas and records with field permission, quota, migration and tenant isolation. | A schema revision preserves authorized records and denies protected Core mutation or other-tenant access (EXT,TEN). | V1.7 | M§92; V7/08 |
| REQ-EXT-003 | AI App Builder creates draft only: describe, preview, validate, simulate, human review, publish, observe, rollback. | Invalid draft cannot publish (EXT,AI). | V1.7 | V7/08 |
| REQ-EXT-004 | Offer stable tenant-scoped public API with auth, versioned capability schema, pagination, quotas and idempotent commands. | Sample remote app calls public API only; incompatible change denied (EXT,AUTH). | V1.1, V1.7 | M§84,109 |
| REQ-EXT-005 | Apps have separate principal, declared field/action/egress/data scopes, signing and consent version. | Permission expansion blocks until re-consent (EXT,AUTH). | V1.1, V1.7 | M§116; V7/08 |
| REQ-EXT-006 | Remote execution isolates credentials, callback authenticity, quotas, replay and sandbox from API process. | App crash/compromise cannot read Core DB (EXT,TEN). | V1.7 | M§84,109 |
| REQ-EXT-007 | App install and upgrade/migration preserve tenant data, consent and public API compatibility. | One app survives platform upgrade; failed migration rolls back or forward-repairs (EXT,OPS). | V1.7 | M§59,117,118 |
| REQ-EXT-008 | Marketplace listing governs publisher provenance, security/privacy review, compatibility, version/support, disclosure and suspension. | Three non-Core apps approved with independent review dossiers (EXT). | V1.10 | M§110,118 |
| REQ-EXT-009 | Partner/industry apps use same policy and cannot gain Core privilege through certification label. | Suspended app loses tokens and webhooks (EXT,AUTH). | V1.10 | M§109,110 |
| REQ-EXT-010 | Developer portal provides docs, changelog, sandbox, examples, test harness, deprecation and conformance. | Independent partner completes install/upgrade (EXT). | V1.10 | M§109 |
| REQ-EXT-011 | Public contract separates backward compatibility from re-consent on any new privilege, egress or billing. | Minor API change still requires consent when scope grows (EXT). | V1.1 | M§116 |
| REQ-EXT-012 | Abandoned provider/app revocation and recovery preserve export and tenant continuity. | Forced removal leaves documented recoverable state (EXT,OPS). | V1.10 | V7/08 |
| REQ-EXT-013 | Establish early tenant-scoped custom-field/schema/package version/auth foundation without protected-domain mutation. | V1.1 private package upgrades schema and preserves field ACL/data across tenants (EXT,TEN). | V1.1 | M§83,92; V7/08 |
| REQ-EXT-014 | Public event/webhook lifecycle includes signed delivery, schema versions, replay bounds, recipient scope and revocation. | Duplicate/reordered event or revoked app never leaks tenant data (EXT,AUTH). | V1.1, V1.7 | M§44,84,109 |
| REQ-EXT-015 | SDK/CLI, docs, synthetic test tenant and conformance harness enable independent developer build and debug. | External developer reproduces install and diagnostics from docs (EXT,UX). | V1.7/1.10 | M§109 |
| REQ-EXT-016 | Marketplace billing, refund, payout, dispute and merchant-role terms are a separate approved financial lifecycle. | Failed app charge/refund reconciles and cannot pay unsupported publisher (EXT,FIN). | V1.10 | M§110,119 |
| REQ-EXT-017 | App uninstall/export/revocation handles retention, remote processor acknowledgment and tenant continuity independently of upgrade. | Uninstall revokes events/tokens and exports app-owned data without deleting other tenant records (EXT,DATA). | V1.7 | M§117,118 |
| REQ-EXT-018 | Studio form/view builder authors accessible, versioned data entry and role-specific views with validation, field ACL and preview/publish lifecycle. | Independent builder creates usable fa/en form and view; wrong role cannot read/write hidden field, old submission stays reconstructible (EXT,UX). | V1.7 | M§92; V7/08 |
| REQ-EXT-019 | Studio pure-rule and workflow engine versions bounded expressions, transition/approval authority, idempotency and rollback/forward correction without arbitrary Core I/O. | Unbounded expression fails, unauthorized approval denied, duplicate/reordered event leaves one correct state after migration (EXT,AUTH). | V1.7 | M§92; V7/08 |

## Universal/industry capability contracts (owner: specialist module or extension; ADR-003–004,020)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-UNI-001 | Govern party, catalog, order, inventory, fulfillment, resource and transaction typed primitives. | One no-code vertical uses primitives without Core fork (EXT,PHYS). | V1.7 | M§91–94 |
| REQ-UNI-002 | Intent-to-Outcome decomposes plan DAG, permissions, cost, approvals, rollback and observed proof. | Partial external failure has explicit recovery (PHYS,OPS). | V1.7 | M§93 |
| REQ-UNI-003 | Inventory movement and reservations track units, lot/serial, receipts, returns, transfers and quantity availability with scoped authority. | Concurrent reservations, duplicate return and wrong-lot dispatch conserve eligible quantities (PHYS). | V1.8 | M§94 |
| REQ-UNI-004 | Commerce order/fulfillment tracks partial confirmation, delivery, return/refund and settlement using policy-bound adapters. | GJ-05 reconciles returned order and explicit recovery (PHYS,FIN). | V1.8 | M§94 |
| REQ-UNI-005 | Manufacturing BOM/MRP/routing and production movement use approved version and safe external OT boundary. | Production quantity/cost reconcile; no unsafe control command (PHYS,FIN). | V1.8 / Post depth | M§95 |
| REQ-UNI-006 | Agriculture/food uses provenance, lot trace, recall, yield and policy-bound claims. | Recall identifies affected lots with no invented certification (PHYS). | V1.8 / Post depth | M§96 |
| REQ-UNI-007 | Website builder/CMS provides safe content blocks, versioned headless API, multisite and translation/editorial workflow. | Approved content version can publish in fa/en without tenant leak (EXT,UX). | V1.7 | M§97 |
| REQ-UNI-008 | Commerce site adds catalog, cart/checkout, order, tax/fulfillment/refund through eligible providers. | Purchase-to-return balances; unsupported corridor blocks checkout (PHYS,PAY). | V1.8 | M§97 |
| REQ-UNI-009 | SEO metadata/sitemap/canonical/redirect controls are testable; no search ranking guarantee. | Crawlable artifact and redirect checks (UX). | V1.7 | M§97 |
| REQ-UNI-010 | Industry packs declare dependencies, data types, workflows, permissions, policy and conformance/version. | Two different packs coexist without tenant bleed (EXT,POL). | V1.7 | M§99 |
| REQ-UNI-011 | Banking integration is bounded to licensed partner APIs; no unlicensed core banking/custody claim. | Unsupported regulated action denied (POL,FIN). | V1.9 / Post | M§102 |
| REQ-UNI-012 | Edge/offline device replay uses signed identity, bounded queue, conflict policy and no silent money/control actuation. | Offline duplicate converges or escalates (PHYS,OPS). | V1.8 / Post | M§105 |
| REQ-UNI-013 | Advanced WMS/TMS, industrial control and specialist regulated systems remain partner/future contracts with exit/portability. | Capability mapped, no false GA (EXT,POL). | Post | M§77,94–96,102,105 |
| REQ-UNI-014 | Device adapters cover barcode, scanner, camera and printer via declared capability, permission, offline queue and failure handling. | Duplicate scan does not double movement; denied device cannot print sensitive label (PHYS,AUTH). | V1.8 / Post device depth | M§105 |
| REQ-UNI-015 | Procurement RFQ, purchase order, supplier approval and commitment/receipt lifecycle is separate from customer order. | Canceled/partial PO releases budget commitment and matches AP/receipt (PHYS,BUD). | V1.7/1.8 | M§68,94 |
| REQ-UNI-016 | Warehouse operations own bin, lot/serial, pick/pack/stocktake and inventory movement authority. | Wrong-lot/duplicate pick denied; quantity and valuation reconcile (PHYS). | V1.8 | M§94 |
| REQ-UNI-017 | Logistics/shipment tracks carrier, handoff, partial delivery, exception, proof and return independently of stock ledger. | Lost parcel/partial shipment produces bounded recovery and customer evidence (PHYS). | V1.8 | M§94 |
| REQ-UNI-018 | EAM owns physical asset maintenance schedule, work order, inspection and retirement with safety/OT boundary. | Overdue maintenance blocks configured unsafe use; digital asset register remains distinct (PHYS,OPS). | V1.8 / Post depth | M§95 |
| REQ-UNI-019 | Site publication owns verified domains, preview, approval, schedule, rollback and public rendering isolation. | Invalid publish keeps prior site; lead links CRM with tenant provenance (EXT,UX). | V1.7 | M§97 |
| REQ-UNI-020 | Agriculture/food lot trace and recall notification has a separate authority and source lineage from yield/planning. | Recalled lot identifies affected deliveries and freezes configured movement without certification claim (PHYS,POL). | V1.8 / Post depth | M§96 |
| REQ-UNI-021 | Commerce order dispute independently governs buyer/seller claim, evidence, scoped adjudication, settlement hold, decision, appeal and refund/reversal. | Partial delivery dispute preserves evidence and blocks premature settlement; authorized adjudication reconciles refund and ledger without deleting order history (PHYS,FIN). | V1.8 | M§94 |
| REQ-UNI-022 | Stocktake adjustment and inventory valuation/COGS independently version counting evidence, cost method, period and journal reconciliation. | Count variance requires approval; receipt/return/revaluation posts balanced corrections and ledger value matches independently computed inventory roll-forward (PHYS,FIN). | V1.8 | M§94,103 |

## Security, privacy, accessibility and market truth (owner: Security/Privacy/UX/Product; ADR-009,012–013,021–022)

| ID | Normative behavior | Outcome proof and suite | R | Source |
|---|---|---|---|---|
| REQ-TRU-001 | Classify every data category and processing flow by purpose, sensitivity, retention and approved minimum fields before collection. | Forbidden/unnecessary field is rejected at intake and excluded from derived export; classification changes are versioned (DATA,AUTH). | V1.0 | M§54,55; V7/07 |
| REQ-TRU-002 | Maintain threat model, SBOM/license/supply-chain controls and vulnerability triage with current applicability review. | P0/P1 vulnerability blocks release, provenance reconstructs (OPS,AUTO). | V1.0 | M§54; V7/07 |
| REQ-TRU-003 | Purpose/consent and data-subject rights govern scoped access, correction, export and downstream processor actions. | Withdrawal/rights request propagates without cross-tenant exposure (DATA,AUTH). | V1.0 | M§55,86 |
| REQ-TRU-004 | Keep minimal immutable audit envelope separately from erasable personal payload, access and retention controls. | Erasure does not break accounting evidence or reappear (DATA,FIN). | V1.0 | M§54,55,86 |
| REQ-TRU-005 | Residency and cross-border processing use policy-bound location and processor evidence, including backup/support/AI. | Disallowed processor route denied (POL,DATA). | V1.2 | M§55,98; V7/07 |
| REQ-TRU-006 | Target WCAG 2.2 AA across relevant web journeys; keyboard, screen reader, zoom, contrast and errors. | Human + automation critical flows zero blockers (UX). | V1.0 onward | M§52; V7/07 |
| REQ-TRU-007 | Persian RTL/English LTR and accessible number, date, money and bidirectional text are tested. | GJ-01A completion both languages (UX). | V1.0 | M§52,87 |
| REQ-TRU-008 | Marketing/website claims carry dated substantiation, scope and expiry; no undocumented ROI, law or ready country. | Unsupported claim cannot publish (AUTO). | V1.6 | V7/05,09 |
| REQ-TRU-009 | GTM protects initial ICP, onboarding, retention and buyer/user outcome evidence; pricing/brand owner approved. | Real partner evidence before commercial GA (WORK). | V1.6 | M§3,58; V7/05 |
| REQ-TRU-010 | Trust/safety detects and triages suspected fraud/abuse with proportionate scoped enforcement and audit. | Suspicious activity throttle does not expose reporter or unrelated tenant (POL,AUTH). | V1.2 | M§46 |
| REQ-TRU-011 | Asset Management independently tracks domains/hosting/servers/repos/DNS/certificates/licenses/APIs/devices, owner/provider/client/project/entity/cost/purchase/renewal/expiry/warranty/lifecycle/reminders/audit. | Each asset class survives transfer/expiry with scoped reminders; asset has secret reference, never value (AST,AUTH). | V1.0 | M§35 |
| REQ-TRU-012 | Import validates mapping, duplicates, scope, preview/dry-run, atomic/recoverable batches, reconciliation and reversible correction of a completed import without deleting posted truth. | Bad row does not corrupt tenant; a completed bad import can be undone or compensated with audit and independent ledger reconciliation (DATA,TEN). | V1.1 | M§73 |
| REQ-TRU-013 | Secrets Vault separately enforces reference-only assets, least-privilege scoped capability access, environment isolation, rotation/revocation/expiry, audit and emergency rotation. | Sentinel never in general AI/browser/log/export; revoked/wrong-env capability denied (VLT,AUTH). | V1.0 | M§35,54 |
| REQ-TRU-014 | Security incident response separately governs restricted evidence, containment, notification applicability, recovery and review linked to operational incident without exposing secret detail. | Simulated breach keeps chain-of-custody; unauthorized status cannot declare report complete (SEC,OPS). | V1.0 | M§54,72; V7/07 |
| REQ-TRU-015 | Retention, deletion, lawful hold and restore tombstones have versioned policy distinct from consent/rights intake. | Expired media and derivative erased; lawful hold reviewed; restore does not resurrect (DATA,OPS). | V1.0 | M§55,86 |
| REQ-TRU-016 | Export/portability provides authorized machine-readable scoped data, source refs and explicit legal-retention/hold exception disclosure independently of import. | Round-trip where defined; retained or excluded fields and their reviewable basis are disclosed without leaking restricted data (DATA,EXT). | V1.1 | M§73,117 |
| REQ-TRU-017 | Report/dispute/appeal lifecycle provides notice, reviewer separation, contestability and reversible proportionate remedy. | False positive restored with evidence; disputant cannot self-approve (POL,AUTH). | V1.2 | M§46 |
| REQ-TRU-018 | Network integrity detects duplicate/fake profile and consent manipulation without cross-tenant raw pooling. | Duplicate candidate review does not silently expose private HR data (POL,TEN). | V1.2 | M§46 |
| REQ-TRU-019 | Encrypt customer data in transit/at rest with scoped key management, environment/tenant separation, authorized rotation, revocation and restore procedure independently of Vault secret grants. | Wrong-region/key principal cannot decrypt; rotation and backup restore preserve authorized access without plaintext log or permanent key loss (SEC,OPS). | V1.0 | M§54,55; V7/07 |
| REQ-TRU-020 | Redact and control sensitive data egress to logs, prompts, traces, browser, support export and external processors by approved data class and purpose. | Secret and personal-data sentinels never reach disallowed sink even on exception, retry, diagnostic dump or AI-off fallback (SEC,AI). | V1.0 | M§54,55; V7/07 |

## Coverage and change rules

The V6 master sections §0–120 are mapped in `SOURCE_COVERAGE.md` including later §120 promise hierarchy; all other source documents are inventoried in `SOURCE_MANIFEST.json` and retained under `archive/sources`. Adopted detail is binding at the matched REQ family unless superseded by an explicit conflict row/ADR. High-level table phrases do not cancel source-level subfeatures. Every implementation issue must decompose these family contracts into small versioned acceptance cases with an independent oracle, owner and release, without silently narrowing them. Numeric targets in architecture are design hypotheses until measured. Country/provider/legal/financial activation has separate evidence and owner gates.
