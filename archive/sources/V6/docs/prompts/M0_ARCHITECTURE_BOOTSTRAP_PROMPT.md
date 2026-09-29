# M0 v4 — Autopilot Bootstrap + Architecture Gate Prompt

Run from branch:

```text
m0/autopilot-architecture
```

Paste the following complete prompt into the primary coding agent:

```text
You are the primary M0 bootstrap and architecture agent for Hayool OS V6.

The repository is the source of truth.

READ FIRST, IN ORDER:
1. CLAUDE.md
2. AGENTS.md
3. docs/engineering/AI_ENGINEERING_CONSTITUTION.md
4. docs/engineering/ENGINEERING_GUARDRAILS.md
5. docs/engineering/AUTONOMOUS_SDLC_CONTROL_PLANE_SPEC.md
6. docs/product/HAYOOL_OS_MASTER_PRODUCT_ENGINEERING_SPEC.md
7. docs/product/HAYOOL_OS_EXECUTIVE_STRATEGIC_REVIEW_FA.md
8. docs/product/HAYOOL_OS_COMPREHENSIVE_BUSINESS_PLAN_FA.md
9. docs/product/HAYOOL_WORKFORCE_BUSINESS_STRATEGY.md
10. docs/product/OWNER_DECISION_SHEET.md
11. docs/data/WORK_GRAPH_AND_CAPABILITY_ONTOLOGY_SPEC.md
12. docs/product/TRUST_SAFETY_AND_MARKETPLACE_INTEGRITY_SPEC.md
13. docs/product/GO_TO_MARKET_BRAND_MONETIZATION_SPEC.md
14. docs/product/UNIT_ECONOMICS_FINANCIAL_MODEL_SPEC.md
15. docs/product/STRATEGIC_RISK_REGISTER.md
16. docs/product/RELEASE_TRAIN_MARKET_READINESS_GATES.md
17. docs/ai/JEV_DECISION_ENGINE_SPEC.md
18. docs/data/LEARNING_INTELLIGENCE_FLYWHEEL_SPEC.md
19. docs/compliance/EMPLOYMENT_AI_GOVERNANCE_SPEC.md
20. docs/market/MARKET_REGULATORY_RESEARCH_REFERENCES.md
21. current git status, branch, recent log and current GitHub PR/issue state if available.

Treat the market/reference file as evidence context, not an immutable requirement.
Re-verify current external versions/licenses/regulation from authoritative sources before relying on them.

M0 has three sub-phases.
DO NOT implement ordinary CRM/Finance/HR/Marketplace business features during M0.

==================================================
M0.0 — TRUST / AUTOPILOT BOOTSTRAP
==================================================

Build the smallest safe Engineering Autopilot necessary for M0 itself.

Required:
- EngineeringModelGateway abstraction
- optional 9Router/other gateway adapter, never domain lock-in
- model-role registry
- requested alias + effective provider/model audit
- Engineering Run schema and immutable run ID
- one scoped writer role
- independent read-only review roles
- deterministic PR risk baseline
- review finding schema
- exact-SHA review binding
- deterministic hard-gate framework
- bounded repair loop
- maximum repair iterations
- maximum elapsed time
- maximum model spend
- kill switch
- GitHub event triggers
- baseline CI
- secret isolation
- no production credentials
- evidence/artifact storage
- Autopilot Shadow Mode for merge/release authority
- protected critical test strategy
- untrusted-PR/runner secret policy.

Do NOT build an over-engineered distributed platform to bootstrap M0.
Use the simplest robust GitHub Actions/scripts/workflow implementation first.
Document an ADR for when it evolves into a durable orchestration service.

If 9Router or another gateway is used:
- verify current docs/security/data handling/licensing
- record actual effective model/provider
- do not treat compatibility model-name spoofing as authoritative identity
- enforce source-code privacy policy
- enforce spend limits
- preserve direct-provider/alternate-gateway fallback.

Jev:
- only narrow semantic decisions
- always behind DecisionEngineProvider
- never permission/release/financial authority
- deterministic gates remain authoritative.

Before moving from M0.0:
exercise at least one test PR and prove:
- branch protection
- run audit
- kill switch
- bounded loop
- provider/model identity logging
- deterministic blocker behavior.

==================================================
M0.1 — PRODUCT / ARCHITECTURE SOURCE OF TRUTH
==================================================

Create/complete:
- PRODUCT_VISION
- PRD
- uniquely identified REQ-* catalog
- ADR-* decisions
- DOMAIN_MODEL
- MODULE_CATALOG
- architecture diagrams/text
- ERD
- tenancy model
- permission model
- security/threat model
- data classification
- Work Graph / Capability ontology
- resource types including human/team/vendor/digital worker
- Workforce Architect / Company Builder
- Talent Network
- matching architecture: constraints first + multi-objective optimization
- cold-start/fair-exposure/exploration policy
- Trust & Safety domain
- engagement modes and legal/economic/payment boundaries
- project delivery
- time/capacity
- pricing/compensation/rate book
- Finance/double-entry
- Iran Country Pack
- Payroll
- CRM/Sales
- marketing/commission
- Client Portal/support/SLA
- asset/vault
- AI Control Plane
- AI Credits
- Decision Intelligence/Jev
- Learning Intelligence Flywheel
- Decision Registry/Ledger
- Ask Your Company semantic analytics
- forecasting
- Digital Twin
- cross-tenant learning boundary
- employment AI governance
- UI/UX information architecture
- design system
- accessibility
- Cloud/Dedicated/On-Prem architecture
- installer/upgrader
- observability
- backup/DR
- licensing/entitlements
- SaaS/AI/managed-workforce unit economics
- GTM/productization assumptions
- release train / market-readiness gates
- test strategy
- release strategy
- ROADMAP
- RISKS
- ASSUMPTIONS
- CHANGELOG.

V6 NON-NEGOTIABLE PRODUCT PRINCIPLES:
- Work/Capability before static Job Title.
- Human and Digital Workers can share planning abstractions but not legal/personhood semantics.
- No public race-to-the-bottom bidding.
- Matching is constraint-first, multi-objective and has cold-start/fair-exposure strategy.
- No opaque universal worker score.
- No invasive worker surveillance by default.
- Cross-tenant raw learning off by default.
- Trust & Safety before marketplace scale.
- Financial truth deterministic.
- High-impact employment actions human-review by default.
- Engagement modes legally/economically distinct.
- Initial GTM remains project-based digital/professional-service companies.
- Architecture may be broad; marketing/launch scope stays focused.
- Do not introduce Graph DB, Kubernetes, custom ML serving or large data-lake complexity without measured need.
- Prefer expand/contract database migration strategy.
- Revenue-stream P&L must separately measure SaaS, AI Credits and managed workforce.
- Core product must remain usable if external AI/Jev provider is unavailable.

TECHNOLOGY:
Validate current stable versions/licenses from authoritative sources.
Do not blindly copy version numbers from prompts.

==================================================
M0.2 — AUTONOMOUS ARCHITECTURE GATE
==================================================

When the M0 PR is ready:

1. Freeze exact target commit SHA.
2. Run deterministic checks.
3. Invoke independent review roles with isolated first-pass context.
4. Normalize findings.
5. Use Jev only for narrow evidence/risk classification where useful.
6. Evaluate deterministic Gate Policy.
7. If repair is allowed:
   - writer verifies findings
   - fixes valid issues
   - updates REQ/ADR
   - runs tests
   - pushes a NEW SHA
   - all affected reviews/gates rerun.
8. Stop at configured repair/cost/time limit.
9. Escalate unresolved product/legal/security deadlock.

Do not self-merge M0.

PRODUCE:
- ARCHITECTURE_GATE_REPORT.md
- AUTOPILOT_BOOTSTRAP_REPORT.md
- MODEL_PROVIDER_AUDIT.md
- DEPENDENCY_LICENSE_REPORT.md
- SECURITY_THREAT_MODEL.md
- DATA_INTELLIGENCE_ARCHITECTURE.md
- WORK_GRAPH_ARCHITECTURE.md
- TRUST_SAFETY_ARCHITECTURE.md
- WORKFORCE_DECISION_GOVERNANCE.md
- UNIT_ECONOMICS_ARCHITECTURE.md
- unresolved owner decisions
- exact checks executed
- current Autopilot maturity level
- recommendation whether M1 may start.

GIT:
- work only on m0/autopilot-architecture
- no direct main push
- no force push
- focused commits
- one M0 PR
- do not merge it yourself.

ASK PRODUCT OWNER ONLY WHEN:
- legally sensitive
- financially irreversible
- destructive
- security critical
- materially changes business model
- conflicts with an Owner Decision
- bounded autonomous review cannot resolve a high-impact ambiguity.

For safe reversible engineering choices:
record ADR and proceed.

Continue autonomously until M0 gate is ready or a stop condition is reached.
```


V6 additional architecture obligations:

- Rebaseline the domain around Universal Business Kernel + Work/Resource/Transaction graphs.
- Design Hayool Studio: custom objects/fields/forms/views/workflows/reports/solution packages.
- Design Intent-to-Outcome Plan Graph and universal Provider/Capability Registry.
- Design procurement/inventory/WMS/logistics baseline.
- Design manufacturing/MRP/EAM boundaries and ISA-95/OPC-UA/MQTT integration architecture.
- Design agriculture/food starter pack and traceability.
- Design website/CMS/eCommerce/SEO integration.
- Design Country Pack + Industry Pack + Regulatory Capability Matrix.
- Design multi-entity/multi-currency/intercompany/consolidation-ready finance.
- Design Algorithm/Solver Fabric; explicitly separate rules, optimization, forecasting, Jev and generative LLM.
- Design offline/edge/mobile/barcode workflow architecture.
- Design OpenAPI/AsyncAPI/MCP exposure and connector contracts.
- Design global standards mapping strategy (CLDR/ISO/GS1/Peppol/ISO20022/ISCO/ESCO as applicable).
- Produce Industry Capability Matrix with Kernel/Starter/Verified/Regulated/Partner/Future maturity.
- Do not claim core banking, EHR or safety-critical industrial control in generic V1.


V6 ecosystem obligations:

- Design a Clean-Core extension model.
- Design four-level extensibility: configuration, no-code, low-code, pro-code.
- Define app manifest, scopes, protected data, egress and permission re-approval.
- Define public API/event contracts and API lifecycle.
- Define Developer Portal, CLI, SDK, test tenant and extension test kit.
- Define declarative Solution Packages.
- Define Remote App architecture.
- Evaluate but do not prematurely implement untrusted hosted code runtime.
- Define Marketplace review, signing, publisher verification, billing and app lifecycle.
- Define Capability Request/bounty flow.
- Define partner/community governance.
- Define AI Necessity Gate and fully loaded AI cost ledger.
- Define Pricing Lab with configured margin floors and manager-selected optimization objective.
- Add public API/event compatibility checks to CI architecture.

M0 must demonstrate at least:
1. one no-code custom app draft flow architecture;
2. one private pro-code extension "hello world" flow architecture;
3. one version/permission upgrade scenario;
4. one pricing/AI cost example with margin-floor math.

Do not implement dozens of first-party vertical features to prove extensibility.

