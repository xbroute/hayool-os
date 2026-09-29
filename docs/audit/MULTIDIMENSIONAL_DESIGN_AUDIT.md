# V7.2 multidimensional design audit — 25 dimensions

2026-09-26. Scope is the **pre-code design** and its source trace; strengths below mean specified contracts, never executed proof. Risks are remaining design/implementation/market uncertainty, not accepted residual operational risk. Resolved gaps identify V7.2 changes; later evidence is a gate obligation. Two independent document reviewers verified consistency on a shared digest. Design Readiness aspiration may exceed 9.5/10 after future rubric and evidence, but **no numeric Design or Evidence Readiness score is assigned here**. **M0.1 DOCUMENTATION GATE = PASS** for pre-code source completeness/consistency only, never implementation, security assessment, legal applicability or market readiness; **M0.0 = PENDING; M0.2 = PENDING**.

| Dimension | Design strengths | Resolved V7.2 gap | Remaining risk | Evidence required later |
|---|---|---|---|---|
| Product | Initial ICP golden loop and universal contracts coexist. | Budget/incident/asset/vault/meeting made explicit. | Breadth can slow usable flow. | Internal and design-partner task completion/retention. |
| Technical | Modular monolith, exact data/event contracts. | Separate owners, health/telemetry and specialized suites. | Version/licensing/runtime choices untested. | Pinned dependency/CI/fault/load inventory at M0.0. |
| Architecture | Clean Core, Studio, remote apps, typed boundaries. | Budget/Incident/Asset/Vault owner separation. | Boundary cycles/integration complexity. | Module dependency tests and upgrade replay. |
| UX | Role surfaces, progressive disclosure, AI-off. | Meeting and budget/incident journeys named. | Complexity can overwhelm ordinary user. | Observed tasks/time/errors with distinct personas. |
| Accessibility | WCAG 2.2 AA design target, RTL/LTR. | Media correction/meeting and budget UI included. | Automated tools miss assistive-tech failures. | Human screen-reader/keyboard/zoom tests on GJ. |
| Security | Tenant/FK/RLS, app principals, least privilege. | Independent Vault and restricted incident case. | Secret/derived-surface exfiltration. | Attack suite, threat review, secret sentinel, SBOM. |
| Privacy | Classification, deletion/hold/tombstones, purpose. | Meeting media/derivative retention and capture consent. | Cross-processor rights handling/restore. | Rights request, deletion and processor ack drills. |
| AI | Engine selection, optional providers, eval/caps. | Meeting local/private and AI-off approval contract. | Transcription hallucination/bias and cost. | fa/en groundedness, first-use DPA/cost/eval proof. |
| Autonomous engineering | Exact SHA, independent review, caps, kill switch. | Review digest process exercised for docs. | No real protected repo/ENG-RUN yet. | M0.0 shadow PR and seeded blocker proof. |
| Finance | Exact double entry and reconciliation. | Independent V1.0 Budget/Cost/Profit Center BUD and later fixed-asset schedule. | Wrong accounting mappings/thresholds/depreciation. | Accountant review and ledger-backed BUD/depreciation fixtures. |
| Unit economics | Stream-separated cash/contribution scenarios. | Market/pricing psychology tied to model. | No real CAC/COGS/retention data. | Reconciled actuals and sensitivity from cohorts. |
| Market | Narrow initial ICP and outcome proof gates. | Canonical market synthesis replaces fragmented narrative. | PMF/segment size unknown. | Buyer interviews, alternatives, repeat use, willingness to pay. |
| Branding | Hayool masterbrand and proof hierarchy. | Personality, architecture and trademark gate. | Naming conflicts/local interpretation. | Qualified clearance by target market, message research. |
| Psychology | Buyer/user/enterprise/developer/worker anxieties. | Explicit testable persona hypotheses. | Interview bias/manipulative adoption design. | Ethically gathered qualitative/behavioral evidence. |
| Value | Intent→Outcome loop and economic truth. | Added Budget and incident/meeting source proof. | Differentiation versus alternatives unvalidated. | Side-by-side buyer workflow and cost comparisons. |
| Business | Founder-led partner and land-expand paths. | Claims/activation and pricing psychology clarified. | Cash, support and sales-cycle risk. | Partner agreements and funded scenario approvals. |
| Legal/compliance architecture | Pack/applicability/reviewer, blocked unknown. | Domestic evaluator moved from Core to Country Pack. | No qualified live opinion or provider terms. | Signed per-capability/corridor applicability packs. |
| Global adaptability | Context includes all material parties/data/routes. | Domestic/regional/allowlist/global pack fact schema. | Country/subnational conflicts and stale rules. | Two real different jurisdictions plus boundary fixtures. |
| Ecosystem/developer | Public API, consent, Remote Apps, upgrade proof. | API/webhook/SDK, install/uninstall, billing split. | Cold start, abandoned apps, partner IP distrust. | Three independent apps, one upgrade, developer study. |
| Future readiness | Typed industry/physical contracts and partner boundary. | Procurement/WMS/logistics/manufacturing/EAM split. | Specialist regulated depth and edge safety. | Conformance per vertical; no premature GA. |
| Maintainability | Module owner, REQ/ADR and source trace. | 138-row granularity disposition and split map. | New contracts may drift from source. | Automated trace checks and owner review per PR. |
| Testability | Independent oracle and full negative/failure matrix. | BUD/INC/AST/VLT/MEET/CRM/SLA/SUP suites. | Planned test text is not executed evidence. | Exact-SHA CI, sandbox and human review outputs. |
| Upgradeability | Additive schemas, migration/restore gates. | App lifecycle, asset/vault tombstone and budget versions. | Unreconciled old data/permission expansion. | Upgrade+rollback/forward repair on live-like fixture. |
| Debuggability | Correlation, event envelopes, evidence, run limits. | Incident timeline/RCA and source-linked meeting drafts. | Provider ambiguity/flaky tests. | Fault injection, minimized regression and staging replay. |
| Portability | Export/API, deployment modes, provider ports. | Import/export distinct contract and country fact schema. | On-Prem license/provider support and rights exceptions. | Round-trip tenant/app data; Cloud/Dedicated/On-Prem restore. |

## Audit outcome and remaining decision boundaries

Every dimension has a specified contract and later evidence gate. The 61 original sources and V7.1 predecessor are retained; no capability has been declared production ready by documentation. Open risks are registered in `RISK_REGISTER.md` and owner decisions in `OWNER_DECISIONS.md`. M0.0 implementation and M0.2 exact-Git-SHA architecture review remain pending. A passed M0.1 design gate can authorize a planning baseline only; it cannot waive an R3/R4 hard test, legal applicability review, commercial approval or real customer outcome.
