# Complete testing and evidence strategy

All tests below are specified, not executed product tests. Each REQ has the stable planned contract `TEST-<REQ-ID>` (for example `TEST-REQ-FIN-005`), with its proof oracle and suite in the REQ catalog/JSON mirror. Implementation decomposes that contract into positive, negative, concurrency and failure cases where applicable; an empty evidence record cannot pass.

## Test layers and oracles

Domain unit/property tests for deterministic rules; integration against actual PostgreSQL/runtime RLS role and workflow/cache/blob adapters; provider contract tests against fakes then provider sandbox; browser E2E on isolated staging; manual accessibility and independent security/finance/legal review; restore/upgrade and real internal/design-partner outcome proof. Critical oracle derives from approved REQ and independent fixture, not copied implementation. Golden expected money/eligibility values independently reviewed. Synthetic cases never substitute for market/legal evidence.

| Suite | Required cases | Pass oracle | Evidence |
|---|---|---|---|
| TEN | API/FK/cache/jobs/files/search/facets/RAG/websocket/export/restore A vs B | zero unauthorized result or existence leak, writes unchanged | runtime-role reports and denied audit refs |
| AUTH | role/entity/field/app/revocation/delegation/support grant | unauthorized side effects zero; installer privilege never inherited | permission matrix execution |
| FIN | balance/rounding/FX/period lock/reversal/idempotency/partial payment/refund/chargeback/fixed-asset schedule/disposal | exact independent totals; closed/posted immutable; depreciation/COGS tie to journal | fixtures + journal/reconciliation output |
| BUD | original/approved/revised by hierarchy, cost/profit center, period/currency, concurrent commitments, actual/forecast, thresholds, variance | budget never substitutes journal; actual equals independently posted ledger, no double consumption or split-approval bypass | versioned plan + dimension/commitment/journal/approval trace |
| PAY | duplicate/reordered/spoofed callback/timeout/unknown result/concurrency | no duplicate charge/posting; unknown queued | sandbox attempt and settlement trace |
| POL | domestic/regional/allowlist/global/missing/conflict/expired/subnational/revoked/queued policy, counterparties | eligibility before pool or transaction; no pending side effect | context+rule+decision snapshots |
| AI | AI-off/injection/ACL/cost race/unknown model/fallback/eval drift; copilot and Project Architect distinct drafts | deterministic authority intact, caps preserved, rejected drafts never mutate | eval versions/usage ledger |
| WORK | scope change/time overlap/capacity race/acceptance/commission reversal/SLA clock | approved inputs only; dependency/state integrity | golden loop trace |
| INC | operational severity/impact/timeline/owner/comms/mitigation/resolution/RCA/postmortem/follow-up, cross-links | distinct incident/risk/issue/ticket states and scoped customer evidence | timeline and approved postmortem |
| AST | asset class, provider/owner/project/entity/cost/purchase/renew/expiry/warranty/reminders/transfers | lifecycle auditable; never raw secret in register | asset snapshots/reminder/audit trace |
| VLT | scoped capability, environment, rotate/revoke, emergency and sentinel egress | revoked capability denied, no plaintext in asset/AI/browser/log/export | vault grant/rotation and leak scan |
| MEET | policy/consent, audio/video import/manual, local/external transcription, fa/en, source segments, draft approval, rights | denied capture no transfer, AI-off path works, stale draft cannot commit | source hashes, approvals and derivative/retention trace |
| CRM | account/lead/opportunity attribution and source-backed discovery handoff | stage/owner/provenance exact, client isolation | opportunity trace |
| SUP | ticket intake/routing/comms/reopen and outage retry | one scoped customer response, no silent closure | support trace |
| SLA | business calendar/DST/start/pause/breach/reopen across ticket/incident link | independently recomputed clock and escalation | rule/clock event trace |
| SEC | restricted security-incident evidence, classification/minimization, key rotation/restore, sink redaction, containment, notification applicability | ordinary user sees only minimal incident link; wrong key/tenant denied; no sentinel egress | chain of custody, key/restore trace and reviewer decision |
| EXT | independent Studio schema/record, form/view and pure-rule/workflow permissions; install/scope expansion/egress/uninstall/upgrade/signature/abandonment | no Core patch or unauthorized data, version survival; accessible builder outcome | 3 app dossiers and TEST-REQ-EXT-002/018/019 traces |
| DATA | import dry-run/duplicates/mapping/completed-batch correction, export retention/hold exception disclosure, deletion restore | correction preserves posted truth; report complete; erased data not resurrected | import/compensation and rights/exception reports |
| OPS | crash after commit/queue restart/network loss/recovery/migration, readiness/backup-age/lag/dead-letter fault | recoverable states, measured RTO/RPO and truthful correlated alert without cross-tenant/secret leak | backup restore + upgrade logs + independent TEST-REQ-PLAT-018 telemetry trace |
| PHYS | stock race/stocktake/valuation/COGS/lot recall/offline replay/partial shipment/commerce dispute/compensation | quantities/valuation conserved, held dispute not settled, no unsafe OT effect | movement/count/journal and order-dispute traces |
| UX | fa-IR/en/keyboard/screen reader/zoom/mobile/error/offline | all critical outcomes operable with zero blockers | automated reports + human protocol |
| PERF | declared dataset/concurrency/hardware/long export/noisy tenant | target latency and bounded resource use | p50/p95/p99, error/CPU/DB reports |
| AUTO | stale SHA/writer/test weakening/injection/caps/kill switch | every seeded blocker halts | ENG-RUN audit + shadow comparison |

## Required golden scenarios

GJ-01A (V1.0) Client intake/CRM -> approved scope -> independently reproducible quote -> contract -> feasible team -> tracked and accepted effort -> delivered/accepted work -> partial invoice collection -> posted cost/revenue -> budget committed/actual/forecast/variance and cost/profit center -> reconciled project contribution. Include an operational incident linked to project/asset/risk/issue with full postmortem, an expiring domain/certificate asset, revoked Vault capability, and consented AI-off meeting from manual notes through approved source-linked decisions/tasks/requirements/risks/follow-up. Run Persian and English roles, rejected permissions, duplicate payment, scope change, provider outage and refund variant. Actual approved internal project required for V1.0, synthetic rehearsals before live operation. GJ-01B (V1.1) extends the same preserved client/project trace through attributed commission/refund clawback, support ticket/SLA escalation and incident link, customer health and portal acceptance. Neither variant grants external AI use before first-use governance.

GJ-02 second company installs/onboards/imports with completed-batch correction/uses/exports with retention-exception disclosure/upgrades without engineers repairing data. GJ-03 Iran DOMESTIC_ONLY product mode with no approved pack yields zero live rankable candidates; synthetic pack-declared required facts and alternative domestic/regional/allowlist/global policies yield distinct pools, unknown/ineligible/appeal and revocation before facets/rank. GJ-04 independent builder makes accessible Studio schema/form/view/rule/workflow repair app + remote supplier extension + re-consent + upgrade + export/uninstall. GJ-05 procurement commitment -> receipt/lot -> reserve/pick -> stocktake/valuation/COGS -> ship/partial order dispute -> return/refund -> inventory/AP/AR/budget/finance reconciliation and separate EAM maintenance. GJ-06 backup loss simulation -> compatible restore with correct key -> privacy tombstones -> Vault revocation -> payment reconciliation -> reopen.

## Fixtures, determinism and failure injection

At least tenants A/B, entity A1/A2, client/talent/developer/service actors, revoked membership, secret sentinel, IRR/Toman and 0/2/3 minor-unit synthetic currencies, DST gap/fold and Jalali presentation, two approved and one expired policy, healthy-but-ineligible provider, deterministic clock/seed. Scrubbed synthetic data only in CI. Inject process death before/after DB commit, duplicate event, timeout after external acceptance, partial provider failure, dead-letter, stale policy and storage interruption. Time windows are simulated, no long sleeps.

Property-based tests cover ledger balance, bounded refund/credit use, dimensional units, idempotent replay, scope monotonicity and inventory conservation. Fuzz parsers/uploads/expressions/policy schemas/webhooks. Critical regression oracle changes require separate independent review. Flaky test quarantine is visible with owner/expiry and replacement evidence; a required blocker test cannot be simply skipped for release.

## CI selection and blocking policy

Every PR: trace/schema/docs checks, relevant unit/type/lint/build/secrets. Critical paths: full finance/tenant/auth/policy suites and specialist review. Public contracts: compatibility/SDK/sample apps. Significant UI: staging browser RTL/LTR/accessibility. Release: all required suites, migration/restore/upgrade/provenance/SBOM/licenses, accepted residual risks and current country/provider evidence. A missing check is pending; deterministic fail outranks model consensus. Test results bind exact SHA/build/policy/fixture/tool version. Nightly breadth adds robustness but cannot repair a failed merge gate by scheduling it later.

## Acceptance and coverage policy

100% REQ-to-test-contract linkage required; behavioral code coverage numeric target is diagnostic, not correctness proof. Critical invariants must all have positive/negative/concurrency/failure cases; changed finance/auth/tenancy branches require meaningful coverage review. No arbitrary '95% coverage therefore safe' claim. All milestone-mandatory acceptance tests pass; zero known P0/P1; documented evidence supports every readiness dimension. Performance/a11y/manual/legal evidence separately recorded, not inferred from unit tests.

## Evidence envelope

EVID-ID, REQ/test IDs, exact SHA/release/build digest, environment/data profile, policy/provider/pack versions, timestamp, tool version, command/procedure, expected/actual, result, artifact hash/location, reviewer identity, limitations, expiry and revalidation trigger. Protect reports against overwrite and sensitive disclosure. A markdown description of a future test stays PLANNED. Formal gate report lists executed/not-executed/blockers separately.
