# Global jurisdiction and country architecture

ADR-010/012/031. Universal schema applies to every jurisdiction; no unsupported country is implicitly enabled. A pack is not a legal opinion. All launch capability matrices begin unverified.

## Context

Context contains tenant HQ, contracting legal entity/subdivision, branch/worksite, payer/payee, customer/service/delivery location, worker residence and physical work location, citizenship only where legally relevant, governing-law profile, engagement mode, data-subject/controller/processing/storage/backup regions, external subprocessors, payment corridor/currency, product restrictions, tax nexus facts and regulated-industry profile. Each fact has provenance, verification state, valid interval and recorded-at. IP is a risk hint, never authoritative legal location. Missing irrelevant facts do not block unrelated locale/read-only operations; a capability's required-facts schema decides relevance.

## Evaluation and composition

1. Authenticate actor/app and establish resource scope.
2. Load current approved policy snapshot and capability-specific required facts.
3. Apply immutable platform prohibitions and applicable binding restrictions.
4. Intersect allowed countries, corridors, provider regions, data classes and scopes; union required controls/notices/approvals. Tenant/user settings may tighten only.
5. Any explicit prohibition => DENY. Missing necessary facts, expired policy or incompatible binding obligations => BLOCKED_PENDING_REVIEW. No casual selection of federal/local/foreign law to resolve legal conflict.
6. If legal approval, human approval or control evidence missing => PENDING, executable=false. MANUAL_ONLY specifies execution channel, not a bypass. If every obligation satisfied => ALLOW_WITH_CONTROLS or ALLOW.
7. Persist decision_id, allowed/executable, reasons, required_facts, obligations, reviewers, context hash, rule versions, evidence refs, expiry and policy epoch.
8. Recheck at enqueue, assignment, contract acceptance, external data dispatch and financial side effect. A changed fact/policy/approval invalidates old execution eligibility.

Source precedence is typed by domain and applicable law, not arbitrary total ordering of jurisdictions. Legal conflict resolution itself is a reviewed policy artifact. The evaluator is deterministic over approved rules, never asks a model to decide law.

## Pack contract

pack_id, country/subdivision/supranational scopes, semver, schema_version, dependencies, issuer, signatures, source citations, source publication/retrieval dates, applicability predicate, effective_from/to, reviewed_at, next_review, qualified_reviewer, review_status, supersedes, tests, support owner, rollout/withdrawal plan.

Components: locale/calendar/address/identifier/holidays; currency/rounding/FX; tax/withholding/e-invoice/chart/reporting; bank/statement/rail/payment; payroll/leave/employment; sourcing/work authorization/classification/regulated role; privacy/rights/residency/transfer/processor; AI notices/prohibitions/review; accessibility; consumer/renewal/refunds; restricted goods/services. Pure rule modules use governed deterministic expressions or audited adapters, not arbitrary third-party Core code.

Country pack activation is capability-specific. An approved locale pack does not activate payroll, banking, employment AI or regulated commerce. Country ISO mapping is reference data, not a list of markets Hayool may serve.

## Workforce policy

Modes: DISABLED, DOMESTIC_ONLY, ALLOWLIST_COUNTRIES, REGIONAL, GLOBAL_IF_ELIGIBLE, GLOBAL_WITH_APPROVAL. `DOMESTIC_ONLY` is an owner-selected **product restriction**; Core does not encode a universal domestic legal definition. For each operation, the approved Country/Subnational Pack declares `required_facts` (typed name, scope, verifier/provenance, freshness and applicability), `domestic_evaluator_version`, permitted country/region/allowlist, work/engagement/corridor restrictions, policy evidence and reviewer. Candidate facts may include residence, physical work location, legal work authorization, engaging entity or others where the applicable pack requires them. Core evaluates the signed pack deterministically and denies/pends when it is unavailable, expired or required facts unknown. Neither nationality nor IP alone is a domestic proof.

For Iran the **owner's default mode remains DOMESTIC_ONLY**. A conservative synthetic fixture can require engaging entity, residence and physical work in Iran to test fail-closed behavior, but those fields are not a hard-coded legal definition or a production activation decision. A qualified, reviewed Iran pack must declare the real required fact schema, applicable controls and evidence before live sourcing. With no such validated pack, even a seemingly local candidate is not rankable for live sourcing. A foreign citizen is not automatically excluded nor an Iranian national abroad automatically eligible: the applicable approved evaluator decides, subject to product mode and other obligations. A reviewed exception to the mode needs owner approval and cannot override a binding prohibition.

For other countries, no automatic 'free/open' classification. Approved DOMESTIC_ONLY, REGIONAL, ALLOWLIST_COUNTRIES or GLOBAL_IF_ELIGIBLE modes still filter every candidate/corridor before discovery, counts, facets, ranking or optimizer input. Manual invites and imports use the same eligibility checks. A scoped exception must identify corridor/mode/limits/expiry, legal review and owner policy approval; it cannot override applicable prohibition. Recheck when work location changes or engagement renews.

## Provider contract and replaceability

ProviderRegistry entries: provider_id/capability/adapter_version, contracting entity, allowed/denied jurisdictions/corridors/currencies, processing regions/subprocessors, data classes, terms/DPA/license status, evidence/source, verified_at/review_due, health, limits, secret reference, sandbox status, fallback candidates, BYOK eligibility and support owner. Separate operational health from contractual/legal eligibility.

Ports: AI, Decision, Optimization, BankStatement, Banking, PaymentRail, TaxInvoice, Payroll, Signature, Identity, Email, SMS, Storage, Calendar, Maps, SourceControl. Request includes context and idempotency; result includes external reference, status, reconciliation capability, evidence. Fallback reruns full eligibility; neither BYOK nor a local proxy circumvents terms/residency. If no eligible provider, retain safe draft/manual preparation; do not pretend payment/tax submission succeeded.

## Initial capability matrix

| Scope | Locale design | Sourcing policy design | Regulated finance/payroll/AI processing | Publisher/support | Runtime |
|---|---|---|---|---|---|
| IR | fa-IR/RTL/Jalali UX, IRR explicit | DOMESTIC_ONLY | Unverified; no live rules activated | Hayool proposed first-party | simulation only |
| US + state/local | en/LTR and pack overrides | approved mode only; synthetic global fixture | Unverified; no nationwide single tax/labor rule | unassigned | blocked pending pack evidence |
| EU + member/subnational | locale-specific | approved corridor mode only | Unverified; controller/use-case applicability required | unassigned | blocked pending pack evidence |
| Every other country/territory | schema supports reference locale | DISABLED until approved pack | Unverified | unassigned | locale-only/demo or blocked capability |

Maturity={ARCHITECTED,IMPLEMENTED,TESTED,VERIFIED}; distribution={FIRST_PARTY,PARTNER,COMMUNITY,PRIVATE}; execution={DISABLED,SIMULATION,MANUAL,ENABLED}; certification is a separate evidence record with issuer/scope/expiry, never a maturity adjective.

## Regulatory lifecycle and tests

Watcher observation -> verified primary source -> applicability draft -> qualified review -> fixtures/simulation -> signed approval -> future effective activation -> monitoring -> supersession. Urgent protective disable may occur under incident policy; it cannot manufacture a new legal rule. Rollback must not reactivate expired/revoked law: freeze affected side effects and forward-fix when necessary.

Required fixtures: IR DOMESTIC_ONLY with no approved pack (zero rankable); synthetic IR pack requiring declared entity/residence/work facts; one required fact unknown; Iranian national abroad; legally eligible foreign resident under a hypothetical approved evaluator; other synthetic country packs with domestic, regional, allowlist and global modes and changing required-facts versions; US entity/worker in different subdivision; EU data in forbidden backup region; global candidate on blocked payment corridor; provider healthy but terms expired; fallback/BYOK denied; policy revoked while queued; conflicting binding policies; locale known but payroll unknown; effective-date boundary; consent withdrawal before event replay. Fixtures are synthetic engineering cases, never legal validation.

## Evidence package per live country capability

Authoritative sources + effective dates + applicability memo + qualified reviewer + signed policy + deterministic boundary tests + sample outputs + provider sandbox/live authorization evidence + support/update ownership + incident/withdrawal plan. Only then may a particular capability be described as verified. Two materially different validated jurisdiction deployments required for V1.9 global proof, while every other country's state stays explicit.
