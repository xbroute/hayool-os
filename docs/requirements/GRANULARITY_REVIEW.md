# Requirement granularity audit — every V7.1 ID

V7.2, 2026-09-26. Exactly 138 original active requirement records from the attached V7.1 JSON were inspected for a distinct owner, lifecycle, permission/risk boundary and independent test oracle. Their IDs are preserved. A row marked `Split/refined` keeps its primary obligation and links newly independent contracts; it is not deleted or silently narrowed. Other rows retain one cohesive domain invariant or protocol/aggregate contract whose subcases remain in adopted details and the TEST-REQ ID. No extra ID was created merely to raise the count. All new IDs are in the V7.2 catalog/JSON and have independent planned test contracts; no product tests have run.

| V7.1 ID | Disposition | V7.2 linked contracts | Granularity finding / retained primary behavior |
|---|---|---|---|
| REQ-GOV-001 | Retained | TEST-REQ-GOV-001 | cohesive Governance and engineering authority/oracle: Maintain versioned authority, conflict ledger, source coverage, decisions and cl... |
| REQ-GOV-002 | Retained | TEST-REQ-GOV-002 | cohesive Governance and engineering authority/oracle: Carry independent readiness states for specified/design/code/test/security/a11y/... |
| REQ-GOV-003 | Retained | TEST-REQ-GOV-003 | cohesive Governance and engineering authority/oracle: Require owner signature for irreversible legal/commercial/capital/market policy;... |
| REQ-GOV-004 | Retained | TEST-REQ-GOV-004 | cohesive Governance and engineering authority/oracle: Bind each implementation PR to REQ, ADR, test, migration, risk and evidence links. |
| REQ-GOV-005 | Retained | TEST-REQ-GOV-005 | cohesive Governance and engineering authority/oracle: Use protected repo, isolated writer, read-only independent reviews and exact SHA... |
| REQ-GOV-006 | Retained | TEST-REQ-GOV-006 | cohesive Governance and engineering authority/oracle: Bound repair iterations, time and cost; preserve failing tests and secrets; supp... |
| REQ-GOV-007 | Retained | TEST-REQ-GOV-007 | cohesive Governance and engineering authority/oracle: Validate one shadow PR end to end before autonomous merge/deploy authority. |
| REQ-GOV-008 | Retained | TEST-REQ-GOV-008 | cohesive Governance and engineering authority/oracle: Monitor dependencies, CVEs, provider/model/terms, jurisdiction sources and compa... |
| REQ-GOV-009 | Retained | TEST-REQ-GOV-009 | cohesive Governance and engineering authority/oracle: Conduct exact repository-SHA architecture/REQ/ADR/guardrail review and close blo... |
| REQ-GOV-010 | Retained | TEST-REQ-GOV-010 | cohesive Governance and engineering authority/oracle: Preserve threat/risk/decision/evidence provenance and revalidate on affected cha... |
| REQ-PLAT-001 | Split/refined | REQ-PLAT-017 | identity/membership vs organization hierarchy; original: Model tenants, legal entities, branches, teams, roles, memberships, service/app ... |
| REQ-PLAT-002 | Retained | TEST-REQ-PLAT-002 | cohesive Identity, tenancy, permission and operations authority/oracle: Authenticate with secure sessions/MFA for privileged roles, recovery and revocat... |
| REQ-PLAT-003 | Retained | TEST-REQ-PLAT-003 | cohesive Identity, tenancy, permission and operations authority/oracle: Enforce application auth plus composite tenant foreign keys and FORCE RLS with n... |
| REQ-PLAT-004 | Retained | TEST-REQ-PLAT-004 | cohesive Identity, tenancy, permission and operations authority/oracle: Derive transaction-scoped tenant context from verified membership; reset on pool... |
| REQ-PLAT-005 | Retained | TEST-REQ-PLAT-005 | cohesive Identity, tenancy, permission and operations authority/oracle: Apply isolation to jobs, cache, object grants, search, counts, snippets, RAG, an... |
| REQ-PLAT-006 | Retained | TEST-REQ-PLAT-006 | cohesive Identity, tenancy, permission and operations authority/oracle: Enforce field/action/row scopes before search or AI and recheck current access o... |
| REQ-PLAT-007 | Retained | TEST-REQ-PLAT-007 | cohesive Identity, tenancy, permission and operations authority/oracle: Keep global authentication subject minimal; private tenant HR/contact data stays... |
| REQ-PLAT-008 | Retained | TEST-REQ-PLAT-008 | cohesive Identity, tenancy, permission and operations authority/oracle: Support Cloud, Dedicated and On-Prem deployment with same contracts and isolated... |
| REQ-PLAT-009 | Retained | TEST-REQ-PLAT-009 | cohesive Identity, tenancy, permission and operations authority/oracle: Provide signed offline license with explicit grace/read-only/export semantics, n... |
| REQ-PLAT-010 | Retained | TEST-REQ-PLAT-010 | cohesive Identity, tenancy, permission and operations authority/oracle: Provision tenant, verified domain, scoped admin, entitlement and onboarding work... |
| REQ-PLAT-011 | Retained | TEST-REQ-PLAT-011 | cohesive Identity, tenancy, permission and operations authority/oracle: Version plans, entitlements, usage and restrictions centrally; reconcile feature... |
| REQ-PLAT-012 | Split/refined | REQ-PLAT-015/016/018 | backup/restore vs support grant vs upgrade vs independent health/operational telemetry; original: Provide backup, restore, upgrade/rollback, health, telemetry and support access ... |
| REQ-PLAT-013 | Retained | TEST-REQ-PLAT-013 | cohesive Identity, tenancy, permission and operations authority/oracle: Govern master party/item/resource identifiers, deduplication candidates, referen... |
| REQ-PLAT-014 | Retained | TEST-REQ-PLAT-014 | cohesive Identity, tenancy, permission and operations authority/oracle: Tenant branding covers verified domain, login, theme presets, favicon and approv... |
| REQ-WRK-001 | Split/refined | REQ-WRK-020 | client discovery/requirements vs CRM pipeline; original: Capture lead, discovery, client need and source-backed requirements with draft/a... |
| REQ-WRK-002 | Retained | TEST-REQ-WRK-002 | cohesive Work, clients and collaboration authority/oracle: Version scope, assumptions, change requests, acceptance and client signoff. |
| REQ-WRK-003 | Retained | TEST-REQ-WRK-003 | cohesive Work, clients and collaboration authority/oracle: Represent goal, capability, project, work unit, dependency, owner and auditable ... |
| REQ-WRK-004 | Split/refined | REQ-WRK-030 | quote price snapshot vs contract/signature; original: Estimate, quote, contract, amend and retain signed commercial snapshot. |
| REQ-WRK-005 | Retained | TEST-REQ-WRK-005 | cohesive Work, clients and collaboration authority/oracle: Distinguish tracked/submitted/approved/billable/payable time with calendar and o... |
| REQ-WRK-006 | Retained | TEST-REQ-WRK-006 | cohesive Work, clients and collaboration authority/oracle: Reserve capacity with calendar/time zone/leave and atomic competing requests. |
| REQ-WRK-007 | Split/refined | REQ-WRK-019/021/022; REQ-WRK-008 | acceptance vs incident, issue, change and existing risk; original: Manage delivery review, acceptance, issue, risk, change and incident with actor/... |
| REQ-WRK-008 | Retained | TEST-REQ-WRK-008 | cohesive Work, clients and collaboration authority/oracle: Keep versioned risk register, triggers, owner and mitigation linked to work and ... |
| REQ-WRK-009 | Split/refined | REQ-WRK-026 | KPI measurement vs OKR outcome lifecycle; original: Govern OKR/KPI definitions, measurement windows, provenance and outcome comparison. |
| REQ-WRK-010 | Split/refined | REQ-WRK-024/025/029 | meeting orchestration vs consent/media, derivative approval and provider/retention; original: Capture meeting consent, manual notes or authorized transcript, decision and sou... |
| REQ-WRK-011 | Retained | TEST-REQ-WRK-011 | cohesive Work, clients and collaboration authority/oracle: Support client portal for scoped status, deliverables, approvals, invoices and t... |
| REQ-WRK-012 | Split/refined | REQ-WRK-023 | support ticket vs independent SLA clock; original: Ticket severity, calendar/business-hours SLA, pause, escalation and reopen seman... |
| REQ-WRK-013 | Retained | TEST-REQ-WRK-013 | cohesive Work, clients and collaboration authority/oracle: Customer Health shows dimensional payment, delivery, support and renewal facts w... |
| REQ-WRK-014 | Retained | TEST-REQ-WRK-014 | cohesive Work, clients and collaboration authority/oracle: Service packages define limits, add-ons, exclusions, recurrence and SLA with app... |
| REQ-WRK-015 | Retained | TEST-REQ-WRK-015 | cohesive Work, clients and collaboration authority/oracle: Reconcile attribution and marketer commission to collected cash, reversals and s... |
| REQ-WRK-016 | Split/refined | REQ-WRK-027/028 | conversation vs forms and notifications; original: Conversation, form and notification engines are reusable, permissioned and versi... |
| REQ-WRK-017 | Retained | TEST-REQ-WRK-017 | cohesive Work, clients and collaboration authority/oracle: Role dashboards and executive command center link metrics to authorized underlyi... |
| REQ-WRK-018 | Retained | TEST-REQ-WRK-018 | cohesive Work, clients and collaboration authority/oracle: Process intelligence identifies bottleneck/variance from timestamped evidence. |
| REQ-TAL-001 | Retained | TEST-REQ-TAL-001 | cohesive Talent, engagement and people authority/oracle: Separate private talent HR data from purpose-limited, consented, revocable publi... |
| REQ-TAL-002 | Retained | TEST-REQ-TAL-002 | cohesive Talent, engagement and people authority/oracle: Verify capabilities, grades, evidence, availability and claims without universal... |
| REQ-TAL-003 | Split/refined | REQ-TAL-015 | ATS workflow vs assessment/interview review; original: Recruit through intake, screening, consent, review, appeal and documented decisi... |
| REQ-TAL-004 | Retained | TEST-REQ-TAL-004 | cohesive Talent, engagement and people authority/oracle: Resolve sourcing eligibility before candidate discovery, count, ranking, contact... |
| REQ-TAL-005 | Split/refined | REQ-GLB-011; ADR-031 | owner IR product mode preserved, required facts moved to pack; original: Iran default domestic eligibility requires verified engaging entity, residence a... |
| REQ-TAL-006 | Retained | TEST-REQ-TAL-006 | cohesive Talent, engagement and people authority/oracle: Other packs explicitly choose domestic/regional/global sourcing subject to all c... |
| REQ-TAL-007 | Retained | TEST-REQ-TAL-007 | cohesive Talent, engagement and people authority/oracle: Matching explains hard eligibility, capabilities, availability, conflicts, price... |
| REQ-TAL-008 | Retained | TEST-REQ-TAL-008 | cohesive Talent, engagement and people authority/oracle: Team builder solves skill/time/cost/constraints with infeasibility explanation a... |
| REQ-TAL-009 | Retained | TEST-REQ-TAL-009 | cohesive Talent, engagement and people authority/oracle: Workforce architect models role/team plan, utilization, grade gap, hiring and sc... |
| REQ-TAL-010 | Retained | TEST-REQ-TAL-010 | cohesive Talent, engagement and people authority/oracle: Explicitly select employment/contractor/managed/outcome engagement and responsib... |
| REQ-TAL-011 | Retained | TEST-REQ-TAL-011 | cohesive Talent, engagement and people authority/oracle: Compensation rules and floors are independent of client price and AI score; lega... |
| REQ-TAL-012 | Retained | TEST-REQ-TAL-012 | cohesive Talent, engagement and people authority/oracle: Payroll uses approved entitlement/rules and authorized review before posting/pay... |
| REQ-TAL-013 | Split/refined | REQ-TAL-016/017 | managed dispute/evidence/settlement remains primary; vetting and replacement/liability handoff have distinct owners/oracles; original: Managed marketplace governs vetting, evidence, dispute, replacement, liability and settlement... |
| REQ-TAL-014 | Retained | TEST-REQ-TAL-014 | cohesive Talent, engagement and people authority/oracle: Employment-AI candidate changes use offline evaluation, bias review, shadow/limi... |
| REQ-GLB-001 | Retained | TEST-REQ-GLB-001 | cohesive Global policy, providers and interoperability authority/oracle: Resolve Jurisdiction Context from all relevant parties, entity, worker location,... |
| REQ-GLB-002 | Retained | TEST-REQ-GLB-002 | cohesive Global policy, providers and interoperability authority/oracle: Compose Global, Country/Subnational, industry, provider and tenant constraints r... |
| REQ-GLB-003 | Retained | TEST-REQ-GLB-003 | cohesive Global policy, providers and interoperability authority/oracle: Return typed executable/blocked/pending decision with policy and fact versions, ... |
| REQ-GLB-004 | Retained | TEST-REQ-GLB-004 | cohesive Global policy, providers and interoperability authority/oracle: Re-evaluate eligibility at dispatch after approval and on queued/retry operations. |
| REQ-GLB-005 | Retained | TEST-REQ-GLB-005 | cohesive Global policy, providers and interoperability authority/oracle: Country pack covers entity/work/tax/payroll/banking/payment/AI/data/commerce/loc... |
| REQ-GLB-006 | Retained | TEST-REQ-GLB-006 | cohesive Global policy, providers and interoperability authority/oracle: Provider registry binds capability, country/corridor, terms, residency, currency... |
| REQ-GLB-007 | Retained | TEST-REQ-GLB-007 | cohesive Global policy, providers and interoperability authority/oracle: Separate pack design maturity, publisher/support ownership and runtime eligibility. |
| REQ-GLB-008 | Retained | TEST-REQ-GLB-008 | cohesive Global policy, providers and interoperability authority/oracle: Translate/localize legal content with reviewed version and effective scope; supp... |
| REQ-GLB-009 | Split/refined | REQ-TRU-012/016; REQ-EXT-004/014 | interoperability vs import/export/API/events; original: Provide import/export and standards-based APIs with provenance, mapping, dry-run... |
| REQ-GLB-010 | Split/refined | REQ-TRU-005 | counterparty/corridor screening remains transaction policy; data transfer has distinct privacy owner and oracle; original: Verify sanctioned/restricted counterparties and cross-border transfer requirements... |
| REQ-FIN-001 | Retained | TEST-REQ-FIN-001 | cohesive Financial, pricing and commercial authority/oracle: Keep legal-entity/book double-entry journals balanced in exact decimal functiona... |
| REQ-FIN-002 | Retained | TEST-REQ-FIN-002 | cohesive Financial, pricing and commercial authority/oracle: Freeze posted lines; corrections are linked reversal/adjustment and closed perio... |
| REQ-FIN-003 | Split/refined | REQ-FIN-026 | rounding vs FX rate provenance; original: Version rounding, currency exponent, FX source and pricing/tax rule snapshot. |
| REQ-FIN-004 | Split/refined | REQ-FIN-023 | AR vs AP lifecycle; original: Model AR/AP, invoice type, payment allocation, partial receipt, overpayment, ref... |
| REQ-FIN-005 | Retained | TEST-REQ-FIN-005 | cohesive Financial, pricing and commercial authority/oracle: Deduplicate provider attempts/webhooks; ambiguous payment remains reconciliation... |
| REQ-FIN-006 | Retained | TEST-REQ-FIN-006 | cohesive Financial, pricing and commercial authority/oracle: Reconcile external settlement, provider fees and ledger; differences create case... |
| REQ-FIN-007 | Retained | TEST-REQ-FIN-007 | cohesive Financial, pricing and commercial authority/oracle: Calculate quote cost waterfall, gross/contribution/fully-loaded margin with expl... |
| REQ-FIN-008 | Split/refined | REQ-FIN-024 | business price floor vs worker compensation floor; original: Enforce non-overridable legal/fair compensation floor and approved scoped busine... |
| REQ-FIN-009 | Split/refined | REQ-FIN-022 | rate book vs discount guardrails; original: Govern rate books, discounts, approval and grandfathered contract terms. |
| REQ-FIN-010 | Retained | TEST-REQ-FIN-010 | cohesive Financial, pricing and commercial authority/oracle: Govern recurring billing, plan change, proration, credit, refund and collection ... |
| REQ-FIN-011 | Retained | TEST-REQ-FIN-011 | cohesive Financial, pricing and commercial authority/oracle: Distinguish tenant operating books, Hayool product economics and corporate statu... |
| REQ-FIN-012 | Retained | TEST-REQ-FIN-012 | cohesive Financial, pricing and commercial authority/oracle: Maintain 36-month conservative/base/upside operating and liquidity scenarios wit... |
| REQ-FIN-013 | Retained | TEST-REQ-FIN-013 | cohesive Financial, pricing and commercial authority/oracle: Pricing Lab pre-registers cohorts, guardrails, stop criteria and owner approval ... |
| REQ-FIN-014 | Retained | TEST-REQ-FIN-014 | cohesive Financial, pricing and commercial authority/oracle: AI credits reserve/reconcile/release atomically, attribute actual provider/model... |
| REQ-FIN-015 | Split/refined | REQ-FIN-025 | stream economics vs principal/agent basis; original: Separate marketplace/managed/SaaS/AI/implementation stream economics and princip... |
| REQ-FIN-016 | Split/refined | REQ-FIN-018–021; REQ-UNI-015 | procurement/expense vs independent V1.0 budget and purchasing commitment; original: Procurement/expense/vendor approvals produce controlled payable and cost-center/... |
| REQ-FIN-017 | Split/refined | REQ-FIN-027–029 | enterprise boundary vs intercompany, tax/e-invoice, revenue recognition; original: Enterprise accounting extensions include intercompany, tax/e-invoice and recogni... |
| REQ-AI-001 | Retained | TEST-REQ-AI-001 | cohesive AI, data and outcomes authority/oracle: Route work to deterministic, retrieval, solver, predictive, semantic or generati... |
| REQ-AI-002 | Retained | TEST-REQ-AI-002 | cohesive AI, data and outcomes authority/oracle: Keep core product usable when all external AI disabled; degrade explicitly. |
| REQ-AI-003 | Retained | TEST-REQ-AI-003 | cohesive AI, data and outcomes authority/oracle: Govern provider/model allowlist, data classes, region, terms, cost, fallback and... |
| REQ-AI-004 | Retained | TEST-REQ-AI-004 | cohesive AI, data and outcomes authority/oracle: Enforce retrieval ACL before context; treat retrieved text, tool results and app... |
| REQ-AI-005 | Retained | TEST-REQ-AI-005 | cohesive AI, data and outcomes authority/oracle: Trace prompt/template/algorithm/knowledge/policy versions, evidence, confidence ... |
| REQ-AI-006 | Retained | TEST-REQ-AI-006 | cohesive AI, data and outcomes authority/oracle: Evaluate high-impact change offline, shadow, limited and active with rollback an... |
| REQ-AI-007 | Retained | TEST-REQ-AI-007 | cohesive AI, data and outcomes authority/oracle: Cost reserve/provider selection respects tenant/project/user/agent caps and user... |
| REQ-AI-008 | Retained | TEST-REQ-AI-008 | cohesive AI, data and outcomes authority/oracle: Build governed Work Graph and capability ontology with versioned typed edges and... |
| REQ-AI-009 | Retained | TEST-REQ-AI-009 | cohesive AI, data and outcomes authority/oracle: Outcome learning uses consented, minimized, aggregated signals with quality/bias... |
| REQ-AI-010 | Split/refined | REQ-AI-017 | permission-scoped personal copilot vs project-scope/resource/economics architect have distinct user action and acceptance; original: Personal copilot and AI project architect produce cited draft plans/actions... |
| REQ-AI-011 | Retained | TEST-REQ-AI-011 | cohesive AI, data and outcomes authority/oracle: Forecasts label horizon, calibration, uncertainty, data quality and version; das... |
| REQ-AI-012 | Retained | TEST-REQ-AI-012 | cohesive AI, data and outcomes authority/oracle: Digital workers and agents receive scoped identity, budget, tool allowlist, appr... |
| REQ-AI-013 | Retained | TEST-REQ-AI-013 | cohesive AI, data and outcomes authority/oracle: Jev/TypeSafe is optional semantic adapter; benchmark and approved terms before use. |
| REQ-AI-014 | Retained | TEST-REQ-AI-014 | cohesive AI, data and outcomes authority/oracle: Cross-tenant learning is separately consented and privacy-reviewed, with no raw ... |
| REQ-AI-015 | Retained | TEST-REQ-AI-015 | cohesive AI, data and outcomes authority/oracle: Business Digital Twin maintains typed, versioned scenario state tied to real Wor... |
| REQ-AI-016 | Retained | TEST-REQ-AI-016 | cohesive AI, data and outcomes authority/oracle: Product analytics captures consented activation/adoption/retention/error funnels... |
| REQ-EXT-001 | Retained | TEST-REQ-EXT-001 | cohesive Studio, developer and marketplace authority/oracle: Route variability configuration -> Studio -> low-code -> Remote pro-code -> Core... |
| REQ-EXT-002 | Split/refined | REQ-EXT-018/019 | Studio schema/record ownership remains primary; form/view authoring and pure rule/workflow execution get independent permissions and oracles; original: Studio defines versioned bounded schemas, records, forms, views, pure rules, workflows and permissions... |
| REQ-EXT-003 | Retained | TEST-REQ-EXT-003 | cohesive Studio, developer and marketplace authority/oracle: AI App Builder creates draft only: describe, preview, validate, simulate, human ... |
| REQ-EXT-004 | Split/refined | REQ-EXT-014/015 | public API vs signed events/webhooks and SDK/CLI; original: Offer stable tenant-scoped public API, event/webhook, SDK and capability contrac... |
| REQ-EXT-005 | Retained | TEST-REQ-EXT-005 | cohesive Studio, developer and marketplace authority/oracle: Apps have separate principal, declared field/action/egress/data scopes, signing ... |
| REQ-EXT-006 | Retained | TEST-REQ-EXT-006 | cohesive Studio, developer and marketplace authority/oracle: Remote execution isolates credentials, callback authenticity, quotas, replay and... |
| REQ-EXT-007 | Split/refined | REQ-EXT-017 | upgrade vs uninstall/export/revocation; original: Install, upgrade, migration, uninstall and export preserve tenant data and publi... |
| REQ-EXT-008 | Split/refined | REQ-EXT-016 | listing/security review vs marketplace billing/disputes; original: Marketplace listing has provenance, security/privacy review, version/support pol... |
| REQ-EXT-009 | Retained | TEST-REQ-EXT-009 | cohesive Studio, developer and marketplace authority/oracle: Partner/industry apps use same policy and cannot gain Core privilege through cer... |
| REQ-EXT-010 | Retained | TEST-REQ-EXT-010 | cohesive Studio, developer and marketplace authority/oracle: Developer portal provides docs, changelog, sandbox, examples, test harness, depr... |
| REQ-EXT-011 | Retained | TEST-REQ-EXT-011 | cohesive Studio, developer and marketplace authority/oracle: Public contract separates backward compatibility from re-consent on any new priv... |
| REQ-EXT-012 | Retained | TEST-REQ-EXT-012 | cohesive Studio, developer and marketplace authority/oracle: Abandoned provider/app revocation and recovery preserve export and tenant contin... |
| REQ-EXT-013 | Retained | TEST-REQ-EXT-013 | cohesive Studio, developer and marketplace authority/oracle: Establish early tenant-scoped custom-field/schema/package version/auth foundatio... |
| REQ-UNI-001 | Retained | TEST-REQ-UNI-001 | cohesive Universal/industry capability contracts authority/oracle: Govern party, catalog, order, inventory, fulfillment, resource and transaction t... |
| REQ-UNI-002 | Retained | TEST-REQ-UNI-002 | cohesive Universal/industry capability contracts authority/oracle: Intent-to-Outcome decomposes plan DAG, permissions, cost, approvals, rollback an... |
| REQ-UNI-003 | Split/refined | REQ-UNI-022 | quantity/lot/movement and reservation vs count/valuation/COGS and posted-journal reconciliation; original: Inventory tracks units, lot/serial, movements, reservations, returns, stocktake and valuation... |
| REQ-UNI-004 | Split/refined | REQ-UNI-015–017/021 | commerce order vs procurement, warehouse, logistics and independent order dispute; original: Procurement/commerce/warehouse/logistics manage partial shipment, dispute and se... |
| REQ-UNI-005 | Split/refined | REQ-UNI-018 | manufacturing vs physical EAM; original: Manufacturing MRP/BOM/routing and EAM/maintenance use controlled asset/history a... |
| REQ-UNI-006 | Split/refined | REQ-UNI-020 | agriculture operations vs food lot recall authority; original: Agriculture/food uses provenance, lot trace, recall, yield and policy-bound claims. |
| REQ-UNI-007 | Split/refined | REQ-UNI-019 | CMS authoring vs domain/publication/rollback; original: Website builder/CMS provides safe blocks, headless API, multisite, translation, ... |
| REQ-UNI-008 | Retained | TEST-REQ-UNI-008 | cohesive Universal/industry capability contracts authority/oracle: Commerce site adds catalog, cart/checkout, order, tax/fulfillment/refund through... |
| REQ-UNI-009 | Retained | TEST-REQ-UNI-009 | cohesive Universal/industry capability contracts authority/oracle: SEO metadata/sitemap/canonical/redirect controls are testable; no search ranking... |
| REQ-UNI-010 | Retained | TEST-REQ-UNI-010 | cohesive Universal/industry capability contracts authority/oracle: Industry packs declare dependencies, data types, workflows, permissions, policy ... |
| REQ-UNI-011 | Retained | TEST-REQ-UNI-011 | cohesive Universal/industry capability contracts authority/oracle: Banking integration is bounded to licensed partner APIs; no unlicensed core bank... |
| REQ-UNI-012 | Retained | TEST-REQ-UNI-012 | cohesive Universal/industry capability contracts authority/oracle: Edge/offline device replay uses signed identity, bounded queue, conflict policy ... |
| REQ-UNI-013 | Retained | TEST-REQ-UNI-013 | cohesive Universal/industry capability contracts authority/oracle: Advanced WMS/TMS, industrial control and specialist regulated systems remain par... |
| REQ-UNI-014 | Retained | TEST-REQ-UNI-014 | cohesive Universal/industry capability contracts authority/oracle: Device adapters cover barcode, scanner, camera and printer via declared capabili... |
| REQ-TRU-001 | Split/refined | REQ-TRU-019/020 | classification/minimization remains primary; customer-data encryption/key lifecycle and cross-sink egress redaction independently tested; original: Classify data/flows, minimize collection, encrypt secrets/data, rotate keys and forbid plaintext prompts/logs... |
| REQ-TRU-002 | Split/refined | REQ-TRU-014 | threat/supply chain vs restricted security incident; original: Maintain threat model, supply-chain/SBOM, vulnerability triage and incident resp... |
| REQ-TRU-003 | Split/refined | REQ-TRU-015 | rights/consent vs retention/hold/deletion; original: Purpose/consent/retention/rights/hold records drive deletion, export and downstr... |
| REQ-TRU-004 | Retained | TEST-REQ-TRU-004 | cohesive Security, privacy, accessibility and market truth authority/oracle: Keep minimal immutable audit envelope separately from erasable personal payload,... |
| REQ-TRU-005 | Retained | TEST-REQ-TRU-005 | cohesive Security, privacy, accessibility and market truth authority/oracle: Residency and cross-border processing use policy-bound location and processor ev... |
| REQ-TRU-006 | Retained | TEST-REQ-TRU-006 | cohesive Security, privacy, accessibility and market truth authority/oracle: Target WCAG 2.2 AA across relevant web journeys; keyboard, screen reader, zoom, ... |
| REQ-TRU-007 | Retained | TEST-REQ-TRU-007 | cohesive Security, privacy, accessibility and market truth authority/oracle: Persian RTL/English LTR and accessible number, date, money and bidirectional tex... |
| REQ-TRU-008 | Retained | TEST-REQ-TRU-008 | cohesive Security, privacy, accessibility and market truth authority/oracle: Marketing/website claims carry dated substantiation, scope and expiry; no undocu... |
| REQ-TRU-009 | Retained | TEST-REQ-TRU-009 | cohesive Security, privacy, accessibility and market truth authority/oracle: GTM protects initial ICP, onboarding, retention and buyer/user outcome evidence;... |
| REQ-TRU-010 | Split/refined | REQ-TRU-017/018 | fraud/abuse vs dispute/appeal and network integrity; original: Trust/safety handles fraud, dispute, report/appeal, network integrity and propor... |
| REQ-TRU-011 | Split/refined | REQ-TRU-013; REQ-FIN-030 | asset lifecycle vs independent Vault and separate Finance depreciation/ledger schedule; original: Preserve assets, warranty/depreciation/ownership and scoped secret references in... |
| REQ-TRU-012 | Split/refined | REQ-TRU-016 | import with completed-batch reversible correction vs export/portability with legal-retention exception disclosure; original: Import/export/portability include data mapping, preview, reversibility and legal... |

## Mandatory capability verification

Each entry names independently traceable REQ(s), planned test-contract(s) with the same IDs prefixed `TEST-`, and the release proof. The suite-level/negative cases are in `TESTING_STRATEGY.md` and dedicated domain contracts.

| Capability | REQ and planned test-contract IDs | Outcome proof |
|---|---|---|
| Meeting Intelligence | WRK-010/024/025/029 | MEET end-to-end, AI-off V1.0; provider gated |
| Time Tracking | WRK-005 | approved vs billable/payable time V1.0 |
| Capacity Planning | WRK-006 | competing reservation V1.0 |
| Risk Register | WRK-008 | owner/trigger/mitigation V1.0 |
| Incident Management | WRK-019; TRU-014 security link | INC severity-to-postmortem V1.0 |
| SLA | WRK-023 | independent SLA clock V1.1 |
| Support/Ticketing | WRK-012 | SUP scoped reopen V1.1 |
| Customer Health | WRK-013 | dimensional freshness V1.1 |
| Commission Engine | WRK-015 | cash/refund clawback V1.1 |
| Service Package Builder | WRK-014 | versioned scope/add-ons V1.0 |
| Discount Guardrails | FIN-022/008 | no below-floor unauthorized discount V1.0 |
| Budget | FIN-018/020/021 | BUD version/consumption/variance V1.0 |
| Cost/Profit Center | FIN-019 | dimension effective date/ledger link V1.0 |
| OKR and KPI | WRK-026 and WRK-009 | separate objective and metric provenance V1.0 |
| Asset Management | TRU-011; FIN-030 separate accounting | AST lifecycle/renewal V1.0; depreciation V1.9 |
| Secrets Vault | TRU-013 | VLT scope/rotation/leak sentinel V1.0 |
| CRM/Sales | WRK-020/001/004 | CRM lead-to-quote V1.0 |
| Finance | FIN-001–009/018–030 | ledger/payment/BUD exact V1.0; reviewed enterprise/fixed-asset depth V1.9 |
| Payroll | TAL-012 | rule snapshot/approval/ledger V1.4 |
| Talent/ATS | TAL-001–007/015 | eligibility/assessment/appeal V1.2 |
| Workforce Architect | TAL-008/009 | feasible team and scenario V1.3 |
| Managed Workforce | TAL-010–013/016/017 | distinct vetting/replacement/dispute/settlement under approved corridor V1.4 |
| Client Portal | WRK-011 | scoped approval V1.1 |
| AI Control Plane | AI-001–007/010/012/017 | AI-off, eligible route/caps and separate copilot/architect drafts, V1.5 broad |
| Studio | EXT-001–003/007/013/018/019 | early schema and separately tested form/view/rule/workflow V1.7 |
| Developer Platform | EXT-004/005/014/015 | API/events/SDK/consent V1.1–1.10 |
| Marketplace | EXT-008–010/016 | independent listing and payout V1.10 |
| Country/Jurisdiction Packs | GLB-001–011, TAL-005/006 | pack facts/modes, pending/no pack V1.2 |
| Website/CMS/eCommerce | UNI-007–009/019 | CMS/publication V1.7 and checkout V1.8 |
| Procurement/Inventory/Logistics | UNI-003/004/015–017/021/022 | GJ-05 commitment/stocktake/valuation/shipment/order-dispute V1.8 |
| Manufacturing/EAM | UNI-005/018 | production vs maintenance V1.8/Post |
| Agriculture/Food | UNI-006/020 | yield and distinct lot recall V1.8/Post |
| Digital Twin | AI-015 | simulation never posts truth V1.5 |
| Import/Export (data) | TRU-012/016, GLB-009 | dry-run/completed-import correction and portable round-trip with retention exception V1.1 |
| Cloud/Dedicated/On-Prem | PLAT-008/009/012/016/018 | mode isolation/local diagnostics/restore/upgrade V1.9 |

`TEST-` plus each complete REQ ID is the stable planned contract; for example `TEST-REQ-FIN-018`. “Import/Export” here means business-data portability; no customs/import trade readiness is inferred. Where an advanced variant is Post, the V1 family retains its typed contract and stated initial outcome. Test execution, legal pack verification and market adoption remain pending.
