# Hayool OS — Final Pre-code Source of Truth

Version 7.2 • hardening 2026-09-26 (original V6/V7 source snapshot 2026-09-22) • Scope: pre-code design baseline, not an implementation or launch approval. **M0.1 DOCUMENTATION GATE = PASS** for documentation/source consistency only; **M0.0 = PENDING; M0.2 = PENDING**. Product implementation, security assessment, legal applicability and market readiness remain unproven.

## Authority

The owner's current instruction authorizes this documentation hardening and prohibits product coding or entering phase two. Within that scope: (1) current explicit owner instruction and separately approved owner decisions, (2) engineering Constitution and Guardrails for safety, (3) this index and `CONFLICT_RESOLUTIONS.md`, (4) final architecture/contracts, REQ/ADR catalogs and canonical market document, (5) adopted domain details. A proposed owner default is not an approved decision. An unresolved conflict stops only the affected action. No document can authorize a legal exception, spending, production deployment or bypass of a hard gate.

V7.2 is the current design baseline. The attached V7.1 ZIP is retained under `archive/V7.1/` as immutable predecessor; all its capabilities remain valid except explicit refinements and splits in this package. Original 61 V6/V7 files remain immutable provenance in `archive/sources/`; adopted details in `docs/product`, `platform`, `domains`, `data`, `ai`, `compliance`, and `engineering` remain normative except explicit resolutions. Inherited vendor, regulatory, release-version and competitor assertions are historical research candidates, not current evidence or activation authorization.

V1 means the entire V1.0–V1.10 release family. It never means all capabilities ship at V1.0. Every major capability retains a contract now and a release/proof target. Beyond-V1 capabilities are retained explicitly, not silently removed.

## Read order

1. `../README_FA.md`, `../PROJECT_STATE.md`, `../NEXT_ACTIONS.md`.
2. This file and `CONFLICT_RESOLUTIONS.md`.
3. `engineering/AI_ENGINEERING_CONSTITUTION.md`, `engineering/ENGINEERING_GUARDRAILS.md`.
4. `architecture/FINAL_ARCHITECTURE.md`, `architecture/DOMAIN_CONTRACTS.md`.
5. `requirements/REQUIREMENTS_CATALOG.md`, `adr/ADR_CATALOG.md`.
6. `market/MARKET_BRAND_PSYCHOLOGY_VALUE_GTM_FINAL.md`, `releases/RELEASE_ROADMAP.md`, `testing/TESTING_STRATEGY.md`.
7. `engineering/AUTONOMOUS_ENGINEERING_PLAN.md`.
8. `country-packs/GLOBAL_JURISDICTION_ARCHITECTURE.md`.
9. `security/SECURITY_PRIVACY_COMPLIANCE.md`, `finance/FINANCIAL_BUSINESS_REQUIREMENTS.md`.
10. `platform/DEVELOPER_STUDIO_MARKETPLACE_ARCHITECTURE.md`, `platform/STUDIO_BUILDERS_EXECUTION_CONTRACT.md`, `ai/AI_DATA_OUTCOME_ARCHITECTURE.md`, `ux/ACCESSIBILITY_DESIGN_SYSTEM.md`, `operations/DEPLOYMENT_RECOVERY.md`, `operations/OPERATIONAL_HEALTH_TELEMETRY_CONTRACT.md`.
11. `finance/FIXED_ASSET_ACCOUNTING_CONTRACT.md`, `domains/COMMERCE_ORDER_DISPUTE_CONTRACT.md`, `domains/INVENTORY_STOCKTAKE_VALUATION_CONTRACT.md`, `domains/MANAGED_NETWORK_VETTING_REPLACEMENT_CONTRACT.md`, `data/PORTABILITY_IMPORT_REVERSAL_CONTRACT.md`, `security/DATA_CLASSIFICATION_KEY_EGRESS_CONTRACT.md` and relevant adopted detail.
12. `audit/MULTIDIMENSIONAL_DESIGN_AUDIT.md`, `requirements/GRANULARITY_REVIEW.md`; `evidence/EVIDENCE_INDEX.md`, `OWNER_DECISIONS.md`, `RISK_REGISTER.md`.

## Definitive objects

REQ catalog is the normative delivery catalog; JSON is its machine-readable mirror, generated from the same records. Acceptance obligations compose: specific REQ + source sections + shared test/security/accessibility contract. Source text is not discarded merely because an abbreviated catalog row omits a detail. `requirements/SOURCE_COVERAGE.md` maps every source section to retained requirement families and explicit exceptions. `requirements/GRANULARITY_REVIEW.md` records disposition of each V7.1 ID. ADR catalog owns engineering decisions, not commercial approval. Market final document owns current messaging/claim design, not brand clearance. Roadmap owns release sequence, not a feature deletion.

`SOURCE_MANIFEST.json` inventories all 61 source files. `PACKAGE_MANIFEST.json` binds delivered files to hashes. A snapshot hash review is a document review, not an exact-commit Git/CI gate. Formal M0.2 must be repeated on the imported repository SHA.

## Readiness vocabulary

specified / designed / implemented / unit-tested / integration-tested / security-reviewed / accessibility-reviewed / staging-verified / jurisdiction-verified / market-validated / production-ready / deployed are independent fields. Null means not observed, never pass. No global 9.5 score is assigned to an unbuilt product. Evidence expires on relevant code, policy, provider, jurisdiction or assumption change.
