# Source coverage and preservation map

61/61 original V6/V7 files were read and preserved verbatim in `archive/sources/`, with identifiers and original Drive links in `SOURCE_MANIFEST.json`. The complete V7.1 predecessor ZIP is retained separately in `archive/V7.1/`; it is not counted among the 61 original files. Adopted V6 and V7.1 details remain normative below explicit V7.2 resolutions, even when a REQ family row is shorter. A source action prompt or old release number is provenance, not execution authority. Rows below provide family trace; release and test proof are in `REQUIREMENTS_CATALOG.md` and `RELEASE_ROADMAP.md`. No compliance/vendor research note is treated as current applicable law.

## V6 master §0–120 crosswalk

| Original sections | Preserved family / disposition |
|---|---|
| §0–8 | GOV, PLAT, TRU, WRK, FIN-018–021; deployment modes retained, phased V1.9. |
| §9–14 | TAL, GLB, AI; workforce/network/grades/ATS/managed/matching retained. |
| §15–18 | WRK-001–008/019–022/024–026/030; delivery, requirement, time, capacity, incident and meeting V1.0. |
| §19–25 | FIN, TAL; price, compensation, rate, engagement, HR, payroll; legal activation separate. |
| §26–35 | WRK-010–016/019/020/023–025/029/030, FIN-018–024, TRU-011/013; CRM, service packages, contracts, ledger/budget/centers, Iran, portal, support/SLA/health, commission, meeting, independently owned asset/vault. |
| §36–44 | AI, EXT; twin, AI governance/credits/agents, Jev optional, knowledge, automation, integration. |
| §45–56 | FIN, TRU, AI, GLB; payments, trust, learning/analytics/forecast, cross-tenant, employment AI, UI/search/security/privacy/DR. |
| §57–66 | PLAT, GOV, TRU; entitlement, revenue models, install/upgrade, reuse, autonomous engineering; old M0/V1 execution instructions superseded by roadmap. |
| §67–77 | FIN-018–023, WRK-019/026–028, TRU-012/014/016, UNI-015; recurring billing, procurement, interaction, OKR, eval, incident, data import/export, onboarding, white label, analytics and optionality. |
| §78–90 | WRK, AI, EXT, FIN, TRU; dashboards, copilots, software integration, automation, custom fields, SDK, FX, retention, translation, process intelligence, self-host preference. |
| §91–100 | UNI, EXT, GLB, AI; universal kernel, Studio, orchestration, physical/industrial/agriculture/CMS, interoperability, industry/solver. |
| §101–110 | UNI, GLB, FIN, EXT, UX; experience, banking boundary, accounting, master data, edge, developer/community. |
| §111–120 | AI, FIN, EXT, TRU; rational AI/economics/pricing/experiments, clean core, consent/portability/ecosystem/extended commercial model and product promise. V1 means family; no deletion. |

Every group contains the indicated inclusive integers, hence all §0–120. V6 additional source-level subtleties remain in adopted docs, not replaced by this crosswalk. V7 Master instructions A–S map respectively to authority/reality (GOV/PLAT), repository/bootstrapping (GOV), SOT (all families), global (GLB/TAL), clean Core (EXT/UNI), golden journey (WRK/FIN), Studio (EXT), AI (AI), finance (FIN), security (TRU), outcome release/autonomy/debug/update/evidence (GOV/release/testing), stop/acceptance (OWNER_DECISIONS and gates).

Auditable special cases: §36 -> REQ-AI-015 (scenario divergence, V1.5); §75 -> REQ-PLAT-014 (login/domain/theme/favicon/document/email, V1.1); §76 -> REQ-AI-016 (product activation/adoption and opt-out, V1.1); §104 -> REQ-PLAT-013 (master IDs/lineage/merge/unmerge, V1.1); §105 -> REQ-UNI-012/014 (edge replay and barcode/camera/scanner/printer adapters, V1.8 with deeper device work Post). Foundation Studio §83/92 -> REQ-EXT-013 (schema/package/ACL V1.1), with full builder proof REQ-EXT-002/003/007 V1.7. This mapping supplements, rather than narrows, adopted detail.

## Original file inventory and disposition

`Adopted` means a corresponding detail exists in `docs/`, subject to explicit conflicts; `Archive` means kept as provenance/template/research only; `Rebased` means the V7 proposal was incorporated in final topic docs rather than treated as live authority. All rows retain their exact original under `archive/sources/`.

| # | Source path | Family / status |
|---|---|---|
| 01 | `V6/CLAUDE.md` | GOV Archive |
| 02 | `V6/AGENTS.md` | GOV Archive |
| 03 | `V6/BOOTSTRAP_README.md` | GOV Archive |
| 04 | `V6/docs/prompts/M0_ARCHITECTURE_BOOTSTRAP_PROMPT.md` | GOV Archive |
| 05 | `V6/docs/prompts/M0_INDEPENDENT_ARCHITECTURE_GATE_PROMPT.md` | GOV Archive |
| 06 | `V6/docs/product/HAYOOL_OS_MASTER_PRODUCT_ENGINEERING_SPEC.md` | all Adopted |
| 07 | `V6/docs/product/GO_TO_MARKET_BRAND_MONETIZATION_SPEC.md` | MARKET/TRU/FIN Adopted, canonical synthesis in `docs/market/` |
| 08 | `V6/docs/product/HAYOOL_OS_START_HERE_RUNBOOK.md` | GOV Archive |
| 09 | `V6/docs/product/HAYOOL_OS_EXECUTIVE_STRATEGIC_REVIEW_FA.md` | GOV Archive |
| 10 | `V6/docs/product/HAYOOL_WORKFORCE_BUSINESS_STRATEGY.md` | MARKET/WRK/TAL Adopted |
| 11 | `V6/docs/product/STRATEGIC_RISK_REGISTER.md` | GOV Adopted |
| 12 | `V6/docs/product/TRUST_SAFETY_AND_MARKETPLACE_INTEGRITY_SPEC.md` | TRU Adopted |
| 13 | `V6/docs/product/V6_REBASELINE_CHANGELOG.md` | GOV Archive |
| 14 | `V6/docs/product/RELEASE_TRAIN_MARKET_READINESS_GATES.md` | GOV Adopted |
| 15 | `V6/docs/product/OWNER_DECISION_SHEET.md` | OWNER Adopted |
| 16 | `V6/docs/product/HAYOOL_OS_COMPREHENSIVE_BUSINESS_PLAN_FA.md` | MARKET/FIN/EXT Adopted |
| 17 | `V6/docs/product/GLOBAL_PRODUCT_EXPERIENCE_AND_PERSONA_WORKSPACES_SPEC.md` | UX Adopted |
| 18 | `V6/docs/product/UNIT_ECONOMICS_FINANCIAL_MODEL_SPEC.md` | FIN Adopted |
| 19 | `V6/docs/product/ECOSYSTEM_COMMUNITY_PARTNER_STRATEGY.md` | MARKET/EXT Adopted |
| 20 | `V6/docs/product/HAYOOL_OS_V6_STRATEGIC_REVIEW_FA.md` | GOV Archive |
| 21 | `V6/docs/product/PRICING_PROFIT_OPTIMIZATION_EXPERIMENTATION_SPEC.md` | FIN Adopted |
| 22 | `V6/docs/product/HAYOOL_OS_V5_STRATEGIC_REBASELINE_FA.md` | GOV Archive |
| 23 | `V6/docs/product/V4_REBASELINE_CHANGELOG.md` | GOV Archive |
| 24 | `V6/docs/platform/GLOBAL_LOCALIZATION_COMPLIANCE_INTEROPERABILITY_SPEC.md` | GLB Adopted |
| 25 | `V6/docs/platform/INTENT_TO_OUTCOME_ORCHESTRATION_SPEC.md` | UNI Adopted |
| 26 | `V6/docs/platform/INDUSTRY_PACK_ARCHITECTURE_AND_CAPABILITY_MATRIX.md` | UNI/EXT Adopted |
| 27 | `V6/docs/platform/UNIVERSAL_BUSINESS_KERNEL_AND_STUDIO_SPEC.md` | EXT Adopted |
| 28 | `V6/docs/platform/DEVELOPER_PLATFORM_EXTENSION_RUNTIME_MARKETPLACE_SPEC.md` | EXT Adopted |
| 29 | `V6/docs/market/MARKET_REGULATORY_RESEARCH_REFERENCES.md` | RESEARCH Archive |
| 30 | `V6/docs/engineering/AI_ENGINEERING_CONSTITUTION.md` | GOV Adopted |
| 31 | `V6/docs/engineering/AUTONOMOUS_SDLC_CONTROL_PLANE_SPEC.md` | GOV Adopted |
| 32 | `V6/docs/engineering/ENGINEERING_GUARDRAILS.md` | GOV Adopted |
| 33 | `V6/docs/domains/AGRICULTURE_FOOD_TRACEABILITY_PACK_SPEC.md` | UNI Adopted |
| 34 | `V6/docs/domains/BANKING_FINANCIAL_SERVICES_BOUNDARY_SPEC.md` | UNI Adopted |
| 35 | `V6/docs/domains/COMMERCE_PROCUREMENT_INVENTORY_LOGISTICS_SPEC.md` | UNI Adopted |
| 36 | `V6/docs/domains/MANUFACTURING_ASSET_IOT_EDGE_SPEC.md` | UNI Adopted |
| 37 | `V6/docs/domains/WEBSITE_CMS_COMMERCE_SEO_SPEC.md` | UNI Adopted |
| 38 | `V6/docs/data/WORK_GRAPH_AND_CAPABILITY_ONTOLOGY_SPEC.md` | AI Adopted |
| 39 | `V6/docs/data/LEARNING_INTELLIGENCE_FLYWHEEL_SPEC.md` | AI Adopted |
| 40 | `V6/docs/compliance/EMPLOYMENT_AI_GOVERNANCE_SPEC.md` | TAL/AI Adopted |
| 41 | `V6/docs/ai/JEV_DECISION_ENGINE_SPEC.md` | AI Adopted |
| 42 | `V6/docs/ai/ALGORITHM_SOLVER_DECISION_FABRIC_SPEC.md` | AI Adopted |
| 43 | `V6/docs/ai/AI_USE_COST_GOVERNANCE_SPEC.md` | AI Adopted |
| 44 | `V6/docs/SOURCE_OF_TRUTH_INDEX.md` | GOV Archive |
| 45 | `V6/.github/PULL_REQUEST_TEMPLATE.md` | GOV Archive |
| 46 | `V7/00_README_V7.md` | GOV Rebased |
| 47 | `V7/01_V7_EXECUTIVE_REBASELINE.md` | GOV Rebased |
| 48 | `V7/02_GLOBAL_JURISDICTION_ELIGIBILITY_AND_COUNTRY_PACK_SPEC.md` | GLB/TAL Rebased |
| 49 | `V7/03_OUTCOME_RELEASE_TRAIN_AND_AUTONOMOUS_SDLC_SPEC.md` | GOV Rebased |
| 50 | `V7/04_PLATFORM_ARCHITECTURE_COMPLETENESS_SPEC.md` | PLAT/AI Rebased |
| 51 | `V7/05_MARKET_BRAND_PSYCHOLOGY_VALUE_GTM_SPEC.md` | MARKET/TRU/FIN Rebased into `docs/market/MARKET_BRAND_PSYCHOLOGY_VALUE_GTM_FINAL.md` |
| 52 | `V7/06_FINANCE_ECONOMICS_PRICING_AND_CAPITAL_SPEC.md` | FIN Rebased |
| 53 | `V7/07_SECURITY_PRIVACY_ACCESSIBILITY_COMPLIANCE_SPEC.md` | TRU Rebased |
| 54 | `V7/08_ECOSYSTEM_DEVELOPER_PLATFORM_TRUST_COMPACT.md` | EXT Rebased |
| 55 | `V7/09_REQUIREMENTS_ADR_TRACEABILITY_AND_EVIDENCE_SPEC.md` | GOV Rebased |
| 56 | `V7/10_CHATGPT_WORK_MASTER_BUILD_PROMPT.md` | GOV Rebased |
| 57 | `V7/11_PROJECT_STATE_TEMPLATE.md` | GOV Archive |
| 58 | `V7/12_NEXT_ACTIONS_TEMPLATE.md` | GOV Archive |
| 59 | `V7/13_V7_REBASELINE_CHANGELOG.md` | GOV Rebased |
| 60 | `V7/14_V7_SCORECARD_AND_ACCEPTANCE_GATES.md` | GOV Rebased |
| 61 | `V7/manifest.json` | GOV Archive |

## V7.2 hardening trace

Budget/Cost Center/Profit Center: REQ-FIN-018–021, independent BUD and finance contract, M§4/29/68. Operational incident: REQ-WRK-019, M§72, independent INC; security case REQ-TRU-014. Asset and Vault: REQ-TRU-011/013, M§35/54, separate AST/VLT; fixed-asset depreciation FIN-030, M§35/103, independent ledger schedule. Meeting: REQ-WRK-010/024/025/029, M§34 and V7 AI governance, MEET. Health/telemetry from original PLAT-012 is PLAT-018, M§56/59. Commerce order dispute is UNI-021, M§94; inventory stocktake/valuation is UNI-022. Import correction and export retention disclosure are TRU-012/016, M§73. Studio schema/form/workflow are EXT-002/018/019; data classification/encryption/egress are TRU-001/019/020; managed vetting/replacement/dispute are TAL-016/017/013. Iran/domestic semantics: REQ-TAL-005/006 and GLB-011, V7/02; superseded ADR-011 -> ADR-031. Market final: V6 source rows 07/10/16/19 and V7 row 51. The 138-ID V7.1 disposition and new independently testable IDs appear in `GRANULARITY_REVIEW.md`.

## Exceptions and verification

C-001–031 in `docs/CONFLICT_RESOLUTIONS.md` enumerate supersession. Especially old V4/V5/V6 runbooks, stale provider/legal research and proposed owner defaults cannot authorize code, legal operations or launch. Future additions to a source require an impact row, REQ family/acceptance update and versioned ADR if architecture changes. `SOURCE_MANIFEST.json` preserves fetched size/modified time; `PACKAGE_MANIFEST.json` binds local hash. Document coverage verifies specified breadth, not implemented quality.
