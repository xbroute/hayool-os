# Hayool OS — Banking & Financial Services Boundary Specification
Version: 6.0
Status: Industry architecture boundary

---

## 1. Goal

Hayool OS should be useful to banks and financial institutions without making unsupported claims that the generic platform is a core banking system.

---

## 2. Native enterprise capabilities useful to banks

- HR/workforce
- recruitment
- procurement
- vendor management
- contracts
- projects/PMO
- branch operations workflows
- service desk
- case management
- document/records
- asset management
- internal approvals
- compliance task management
- marketing/CRM where policy allows
- analytics
- AI knowledge
- meeting/action management.

---

## 3. Financial-institution integration layer

Adapters may connect to:
- core banking
- payment systems
- KYC/identity providers
- AML/fraud systems
- card processors
- CRM
- document archives
- regulatory reporting tools.

Use stable APIs/events, not direct core DB mutation.

---

## 4. ISO 20022

Bank/payment adapters may use ISO 20022 message definitions where applicable.

Hayool should support mapping/validation/transformation as an integration capability.

---

## 5. Core banking boundary

Generic Hayool Finance Ledger is an enterprise accounting ledger.

It is NOT automatically:
- deposit ledger
- loan core
- card ledger
- payment clearing system
- securities book of record.

Those require a separately engineered Banking Core Pack or certified integration.

---

## 6. High-risk controls

Financial institution deployments require stronger options:
- data residency
- customer-managed keys where supported
- strict SSO/MFA
- segregation of duties
- immutable audit
- environment isolation
- change approvals
- enhanced logging
- private/on-prem deployment
- model/provider restrictions.

---

## 7. AI

External AI may be disabled for regulated data.

Local/private model routing must be possible.

No model receives account/customer secrets unless explicit approved policy/provider exists.

---

## 8. Market approach

Sell operational/workforce/orchestration capabilities to financial institutions first.

Do not lead with "replace your core banking system."

