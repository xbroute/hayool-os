# Hayool OS V7 — Global Jurisdiction, Eligibility, Mobility & Country Pack Specification

## 1. Goal

Hayool must operate globally without assuming that one country's rules, providers, banks, payment rails, labor model, privacy rules, AI rules or marketplace eligibility apply everywhere.

The core principle is:

**Global Core + Jurisdiction Context + Policy Packs + Provider Registry + Eligibility Decision.**

## 2. Why a Country Pack alone is insufficient

A single transaction may involve:

- tenant headquarters in Country A;
- legal entity in Country B;
- worker resident in Country C;
- worker physically performing work in Country D;
- client in Country E;
- payment provider in Country F;
- data hosted in Region G;
- AI provider processing in Region H;
- an industry-specific regulator.

Therefore the engine must resolve a **Jurisdiction Context**, not merely `tenant.country`.

## 3. Jurisdiction Context

Minimum fields:

- tenant country
- legal entity country/subnational jurisdiction
- branch/worksite
- payer jurisdiction
- payee jurisdiction
- worker citizenship where legally relevant
- worker residence
- physical work location
- client/customer location
- service/delivery location
- contract governing-law profile
- engagement mode
- data-subject location
- data-controller/entity
- processing/storage region
- external processor/provider regions
- payment corridor
- product/service category
- regulated-industry profile
- transaction currency
- sales/tax nexus facts where relevant.

The engine records which fields were known, inferred from authoritative account configuration, or missing.

No legal decision may be based on guessed location.

## 4. Policy precedence

Recommended precedence:

1. Platform safety / prohibited capability
2. Binding sanctions/export/security restriction
3. Mandatory supranational/federal/national rule
4. Mandatory subnational/local rule
5. Regulated-industry rule
6. Contractual/legal-entity policy
7. Tenant policy
8. Department/project policy
9. User preference.

Policy merge is typed, not arbitrary text merging.

For eligibility states use:

- `DENY`
- `ALLOW_WITH_LEGAL_REVIEW`
- `ALLOW_WITH_APPROVAL`
- `ALLOW_WITH_CONTROLS`
- `ALLOW`
- `MANUAL_ONLY`
- `UNKNOWN_BLOCKED_PENDING_DATA`

A less authoritative policy cannot weaken a more authoritative restriction.

## 5. Country Pack schema

Every Country Pack includes:

### Identity and locale
- ISO country/subdivision mappings
- locale/language defaults
- scripts/RTL/LTR
- address schema
- phone format
- national/business identifiers
- timezone/calendar presentation
- public holidays.

### Currency and finance
- legal/accounting currency conventions
- supported transaction currencies
- currency precision/minor-unit policy
- FX source policy
- tax/VAT/GST/sales-tax hooks
- fiscal year conventions
- invoice/e-invoice rules
- chart/reporting pack hooks
- withholding rules where applicable.

### Banking and payments
- bank-account identifier formats
- local bank transfer rails
- open-banking interfaces where available
- card/payment providers
- settlement/refund/chargeback behavior
- provider availability
- manual/file fallback
- reconciliation mappings.

### Payroll and employment
- payroll rule pack
- employer obligations
- statutory deductions/contributions
- leave/holiday hooks
- employment agreement templates/hooks
- contractor classification controls
- notice/termination workflow hooks
- mandatory human-review controls.

### Workforce sourcing and mobility
- domestic sourcing policy
- cross-border sourcing policy
- work authorization checks
- remote-work restrictions
- contractor/EOR/AOR availability
- prohibited/allowed corridors
- regulated-role licensing
- sanctions/export controls
- payment feasibility
- data-transfer feasibility.

### Privacy/data
- legal basis/consent profile
- retention
- data-subject rights
- cross-border transfer
- data localization/residency
- processor/subprocessor requirements
- breach/notification hooks
- sensitive-data classes.

### AI/automation
- prohibited/restricted use cases
- AI notice/transparency
- automated decision rights
- high-impact decision review
- risk-assessment/DPIA hooks
- audit/evaluation requirements
- external AI provider eligibility.

### Accessibility
- target standards
- country-specific procurement/legal accessibility profile
- required evidence.

### Commerce
- consumer disclosures
- refunds/returns
- subscription renewal/notice
- pricing/discount disclosure
- restricted goods/services.

### Provider availability
- cloud
- email/SMS
- identity
- AI
- payments
- banking
- tax invoice
- signature
- maps/geocoding
- source control
- object storage.

Every provider entry has availability, legal basis/terms status, region, fallback and last-verified date.

## 6. Workforce sourcing policy

Create `WorkforceSourcingPolicy`.

Modes:

- `DOMESTIC_ONLY`
- `ALLOWLIST_COUNTRIES`
- `REGIONAL`
- `GLOBAL_IF_ELIGIBLE`
- `GLOBAL_WITH_APPROVAL`
- `DISABLED`.

Pipeline:

Candidate pool
→ country/corridor eligibility
→ legal/work authorization
→ engagement-mode eligibility
→ sanctions/export controls
→ payment feasibility
→ data-processing eligibility
→ regulated-role license
→ tenant hard constraints
→ candidate preferences
→ matching/optimization.

Matching never sees legally ineligible candidates as rankable options.

### Iran working default

V7 should encode the owner's requested **product default** for the Iran pack as:

`DOMESTIC_ONLY`

until an explicit reviewed policy version permits a defined cross-border exception.

This is a product/compliance default, **not a claim that Iranian law universally forbids cross-border talent**.

### Open/global markets

For jurisdictions where global sourcing is permitted, the default can be:

`GLOBAL_IF_ELIGIBLE`

with tenant priorities such as language, timezone, cost, quality, continuity and preferred countries applied **after** hard eligibility checks.

Do not use a vague binary concept such as “free country” in code. Use explicit effective-dated policy.

## 7. Engagement modes

Every engagement has a declared mode:

- Employee
- Local contractor
- Cross-border contractor
- Freelancer marketplace
- Managed contractor
- Managed team/outcome
- Vendor/company
- EOR/AOR
- Partner-provided labor.

Each mode defines:
- legal counterparty
- payer/payee
- tax responsibility
- benefits/insurance responsibility
- IP/confidentiality
- worker-classification checks
- invoice/payroll path
- dispute path
- jurisdiction support state.

If a mode is not legally/operationally supported in the jurisdiction context, the UI does not pretend it is available.

## 8. Banking architecture

Do not hard-code one global bank API.

Use:

`BankingProvider`
`PaymentRailProvider`
`BankStatementProvider`
`OpenBankingProvider`
`ReconciliationProvider`.

A country can support:
- direct bank API
- open-banking aggregator
- ISO-20022 mapping
- local proprietary API
- statement file import
- manual reconciliation.

The authoritative finance ledger is provider-neutral.

## 9. Provider Availability Matrix

Every external provider has:

- provider
- capability
- countries/regions
- denied/restricted jurisdictions
- supported currencies
- data-processing regions
- sanctions/export review status
- DPA/terms status
- outage/fallback policy
- BYOK/customer-contract option
- last verified
- evidence source
- owner.

Provider availability is an input to routing, not documentation only.

## 10. Global data rules

Use standardized identifiers and locale/reference data where practical:
- ISO country/subdivision codes
- ISO currency codes
- Unicode/CLDR locale behavior
- IANA timezone identifiers
- localized units/number/date display.

Canonical data is stored independently from presentation.

Never assume:
- two currency decimals;
- Gregorian-only UX;
- Latin-only names/addresses;
- one surname format;
- one phone format;
- one tax model.

## 11. Regulatory policy lifecycle

Every legal policy rule has:

- policy ID
- jurisdiction
- domain
- source authority
- source reference
- effective date
- expiry/review date
- interpretation note
- tests
- reviewer
- legal-review status
- version
- rollback/supersession path.

Lifecycle:

Observed Change
→ Research Draft
→ Source Verification
→ Legal/Qualified Review where required
→ Test Cases
→ Shadow/Simulation
→ Approved
→ Effective
→ Monitored
→ Superseded.

AI may discover or summarize changes. AI cannot unilaterally activate a high-impact legal rule.

## 12. Country support maturity

Per capability and jurisdiction:

- `ARCHITECTED`
- `COMMUNITY`
- `BETA`
- `VERIFIED`
- `OFFICIAL`
- `PARTNER`
- `MANUAL_ONLY`
- `NOT_AVAILABLE`.

Marketing uses the real status.

## 13. Country Pack certification evidence

A verified/official country capability requires:
- authoritative references;
- effective dates;
- calculation/workflow tests;
- sample documents;
- provider integration evidence;
- reviewer identity/qualification;
- change owner;
- support process;
- incident/update path.

## 14. Globalization acceptance tests

At minimum:
- RTL/LTR
- locale-specific date/number/currency
- variable currency precision
- multi-timezone
- multilingual names/addresses
- data residency routing
- provider unavailable fallback
- domestic-only sourcing
- global-if-eligible sourcing
- blocked payment corridor
- blocked AI provider
- subnational override
- policy effective-date transition.

## 15. Global promise

Hayool can be **globally adaptable from architecture day one**.

A country is commercially supported only when its actual capability matrix passes the evidence gate.

