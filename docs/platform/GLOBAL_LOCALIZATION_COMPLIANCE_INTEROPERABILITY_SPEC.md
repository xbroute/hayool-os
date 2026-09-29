> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Global Localization, Compliance & Interoperability Architecture
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping

---

## 1. Principle

Hayool OS is globally adaptable but never assumes one country's rules apply everywhere.

Architecture:

Global Core
+ Locale
+ Country Pack
+ Subnational Pack when required
+ Industry Pack
+ Tenant Policy
+ Integration Adapter.

Mandatory jurisdiction rules outrank tenant preferences.

---

## 2. Country Pack

A Country Pack may provide:
- language/locale defaults
- address/identity formats
- currency/tender
- tax
- e-invoicing
- payroll
- social insurance
- employment rules
- holidays
- banking/payment conventions
- document templates
- retention
- privacy/AI requirements
- consumer rules
- industry restrictions.

Rules are effective-dated and source-referenced.

---

## 3. Regulatory Capability Matrix

For every country/module/feature:

- Supported
- Supported with external provider
- Beta
- Manual workflow only
- Not available
- Requires legal/partner review.

UI must not imply legal support where none exists.

---

## 4. Locale

Use Unicode/CLDR-compatible locale data for:
- dates
- numbers
- plural rules
- currency display
- units
- calendars
- collation.

Persist canonical machine values separately from presentation.

---

## 5. Country / currency identifiers

Use standardized country/currency codes where appropriate.

Currency object supports:
- ISO code
- precision/minor unit
- exchange-rate source/version
- presentation unit
- legal/accounting unit.

Never hard-code 2 decimal places globally.

---

## 6. Calendar / timezone

Store timestamps in robust canonical form.

Display in user timezone/calendar.

Support calendars through locale/country pack while preserving canonical ordering/computation.

---

## 7. Units

Global UOM service supports SI and customary/local units.

Conversions are deterministic and precision-aware.

Domain pack can add specialized units.

---

## 8. Multilingual

Requirements:
- UI translation catalogs
- tenant terminology
- translated catalog/content
- multilingual search normalization
- RTL/LTR
- language fallback.

AI translation creates drafts; legal/financial texts can require human approval.

---

## 9. Accessibility

Target WCAG 2.2 AA for web surfaces where reasonably applicable.

Accessibility is not only legal compliance; it is global usability.

---

## 10. Data residency

Tenant/deployment policies may define:
- allowed storage regions
- external processors
- AI provider restrictions
- backup region
- telemetry
- cross-border transfer.

On-Prem may operate with external AI/network disabled.

---

## 11. Data subject / privacy operations

Platform primitives:
- consent
- purpose
- data classification
- retention
- access request
- export
- correction
- deletion/restriction where legally applicable
- audit.

Country packs map legal requirements.

---

## 12. E-invoicing / procurement interoperability

Use adapters.

Support Peppol-style e-invoicing/e-procurement networks where applicable.

Iran remains a dedicated tax/e-invoice pack.

Do not build one hard-coded global invoice format.

---

## 13. Financial messaging

For integrations with banks/financial institutions, support ISO 20022-compatible adapters where applicable.

This does not make Hayool a core banking system.

---

## 14. Product / logistics standards

Support mappings/adapters for GS1 identifiers and EPCIS-style traceability.

Do not force GS1 on micro-businesses that do not need it.

---

## 15. Workforce standards

Use mapping layers for standard occupation/skill taxonomies.

Candidates include:
- ISCO
- ESCO
- country-specific classifications.

Hayool's internal ontology remains independent and maps to external IDs.

---

## 16. Manufacturing interoperability

Use ISA-95 concepts to define ERP/MOM boundaries.

Industrial connectors can use OPC UA/MQTT where appropriate.

---

## 17. API interoperability

Public HTTP APIs should be OpenAPI-described.

Event interfaces should be AsyncAPI-described where practical.

AI/tool integrations should be designed for MCP-compatible exposure where safe, without making MCP the only internal tool protocol.

---

## 18. Open commerce

Intent/fulfillment architecture may integrate with open commerce networks such as Beckn/ONDC-like ecosystems when jurisdiction and business case justify it.

Hayool core remains network-neutral.

---

## 19. Banking/regulated-sector boundary

Hayool may serve banks as:
- workforce/HR
- procurement
- project/portfolio
- service/case management
- documents
- asset/vendor
- analytics
- customer/business workflow orchestration

and integrate with core systems.

A generic Hayool release must not claim to replace a regulated core banking ledger/payment clearing platform without a separately engineered/certified Banking Core Pack.

Same principle applies to:
- clinical EHR
- safety-critical industrial control
- aviation/medical device safety systems.

---

## 20. Global readiness gate

A country/industry is commercially "supported" only when:
- localization tested
- legal/accounting rules validated
- required integrations available
- documents/workflows tested
- support process exists
- data/privacy policy confirmed.

Architecture capability alone is not market readiness.


## 21. Country-pack developer ecosystem

Country packs may be developed by:
- Hayool first-party
- certified local partner
- accounting/payroll specialist
- regulated provider.

A country pack is not accepted merely because it compiles.

Release evidence should include:
- authoritative legal/accounting references;
- effective dates;
- test cases;
- sample documents/calculations;
- reviewer identity/qualification;
- supported jurisdiction/subnational region;
- update ownership.

Country-pack marketplace status must distinguish:
- Community
- Verified
- Official/Certified where such certification is meaningful.

## 22. Global developer documentation

Developer docs must explain:
- locale-safe dates/numbers;
- currency precision;
- units;
- translation keys;
- address schemas;
- data residency;
- country-pack extension points.

Extensions must not hard-code one country's formatting/rules.

