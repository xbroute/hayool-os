> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Trust, Safety & Marketplace Integrity Specification
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping

## 1. Purpose
A managed workforce marketplace fails if participants cannot trust identity, work evidence, payments, confidentiality and dispute handling.

Trust & Safety is a core domain, not an afterthought.

## 2. Threat categories

### Identity and account abuse
- duplicate accounts
- impersonation
- stolen identity
- account takeover

### Talent fraud
- fabricated resume
- copied portfolio
- fake experience
- credential fraud
- assessment cheating

### Client abuse
- unpaid work
- malicious scope expansion
- harassment
- abusive communication
- attempts to bypass platform protections

### Marketplace manipulation
- collusion
- fake reviews
- rating rings
- referral abuse
- application spam
- deliberate price manipulation

### Work/time abuse
- fabricated timesheets
- low-effort output
- plagiarism
- unauthorized subcontracting

### Platform/data abuse
- malicious upload
- prompt injection
- secret extraction
- cross-tenant exfiltration
- scraping
- credential theft

## 3. Trust signals
Signals may include:
- identity verification state
- verified work evidence
- payment history
- accepted work outcomes
- dispute outcomes
- assessment evidence
- account age
- device/account linkage where lawful
- security incidents
- behavior anomalies.

Signals are evidence, not automatic guilt.

## 4. Trust profile
Do not expose one public trust score.

Maintain internal dimensions with evidence and uncertainty.

User-facing badges may include:
- identity verified
- skill assessed
- project verified
- reliable payer

without revealing sensitive fraud models.

## 5. Enforcement lifecycle
Signal -> review/automated triage -> temporary safeguards if necessary -> evidence review -> decision -> notice where appropriate -> appeal -> resolution.

High-impact account restrictions require human/policy review.

## 6. Dispute management
Dispute file includes:
- contract/work package snapshot
- requirements
- deliverables
- messages
- accepted changes
- time evidence
- payment state
- reviewers
- decision.

## 7. Payment protection
V1 should prefer licensed payment providers and non-custodial flows.

Do not claim escrow unless legal/payment infrastructure supports true escrow.

A platform accounting hold is not automatically legal escrow.

## 8. Confidentiality/IP
Work engagement records:
- NDA/confidentiality
- permitted disclosure
- code/IP ownership
- portfolio-display permission
- data-access scope
- subcontracting policy.

## 9. Talent poaching / off-platform
Do not rely only on punitive lock-in.

Reduce bypass by making the platform valuable:
- reliable payment
- dispute protection
- repeat work
- reputation/evidence
- project tools
- AI assistance
- insurance/partner services later.

Contractual non-circumvention must be jurisdiction reviewed.

## 10. New talent fairness
Fraud protection must not become a permanent barrier to newcomers.

Use verification, assessments, probationary work and bounded exposure rather than requiring years of platform history.

## 11. Abuse reporting
Clients and talent can report:
- harassment
- fraud
- IP misuse
- payment problem
- data misuse
- unsafe behavior.

Reports are permission protected and audited.

## 12. AI moderation
AI/Jev may triage reports and risk signals.

It must not silently impose irreversible sanctions from an opaque score.

## 13. Metrics
- dispute rate
- fraud-confirmation rate
- false-positive restriction rate
- appeal overturn rate
- time to resolution
- payment failure
- off-platform leakage
- assessment integrity.

## 14. Marketplace launch gate
Public network scale is blocked until:
- dispute process works
- payment state machine works
- identity/evidence workflow exists
- abuse reporting exists
- appeals exist
- privacy controls exist
- matching exposure fairness exists.

