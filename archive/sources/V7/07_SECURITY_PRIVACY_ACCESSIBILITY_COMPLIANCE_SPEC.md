# Hayool OS V7 — Security, Privacy, Accessibility & Compliance Specification

## 1. Principle

Security, privacy, accessibility and compliance are product architecture, not launch checklists.

## 2. Security architecture

Mandatory:
- tenant isolation
- server-side authorization
- least privilege
- MFA-ready
- SSO/OIDC/SAML/SCIM paths by maturity
- secure session/token lifecycle
- secret vault references
- encryption strategy
- upload scanning
- webhook verification
- rate limits
- audit
- dependency scanning
- secret scanning
- container/IaC scanning where applicable
- SBOM
- provenance/attestation path
- incident response.

Cross-tenant leakage is a release blocker.

## 3. Zero-trust extension boundary

Apps:
- separate principal
- least privilege
- protected-data declaration
- explicit egress
- scoped secrets
- install/update consent
- observable access
- kill/suspend/revoke capability.

No arbitrary tenant JavaScript in trusted product surfaces by default.

## 4. Privacy architecture

Primitives:
- data classification
- purpose
- lawful-basis/consent metadata where applicable
- controller/processor roles
- retention
- legal hold
- access/export/correction/deletion/restriction workflows
- residency
- transfer mechanism
- subprocessor registry
- incident/breach workflow.

Derived data and AI traces inherit purpose/retention constraints.

## 5. Purpose limitation

Data collected for one domain is not automatically usable in another.

Examples:
- HR health data cannot feed marketplace ranking.
- support-ticket tone cannot become promotion evidence.
- candidate data cannot silently train unrelated cross-tenant models.

Cross-purpose use requires an explicit policy and legal basis.

## 6. Employment AI

Maintain:
- decision inventory
- jurisdiction applicability
- data used/prohibited
- human review
- notice
- contestability
- fairness evaluation
- language/locality slices
- model/policy version
- retention
- override.

High-impact employment outcomes default to meaningful human review.

## 7. AI transparency

Where required by jurisdiction or product policy:
- identify AI interaction
- label/generated-content state as required
- distinguish draft/recommendation/prediction from authoritative fact
- expose model/policy provenance to authorized users.

## 8. EU readiness

The compliance pack must track current effective dates rather than hard-code old timelines.

As of the V7 research date, EU AI Act transparency requirements are already relevant in 2026, while Annex III high-risk rules including employment follow their current later application date.

The Cyber Resilience Act reporting obligations that began in September 2026 must be represented in product-security incident operations where Hayool is in scope.

Exact applicability requires current legal review.

## 9. U.S. state/local AI readiness

Policy framework must support state/local variation.

Examples of configuration hooks:
- automated-decision notices
- access/opt-out rights
- risk assessments
- correction rights
- bias audits
- public audit summaries
- human review.

Do not implement “US law” as one policy.

## 10. Vulnerability management

Maintain:
- security contact
- disclosure policy
- triage
- severity
- affected versions
- CVE/CNA strategy if applicable
- customer notification
- patch SLA
- forced extension suspension path
- regulatory reporting hooks
- postmortem.

## 11. Accessibility baseline

Target current WCAG 2.2 AA for relevant web surfaces.

Also map jurisdiction-specific accessibility obligations separately.

Design-system requirements:
- keyboard
- focus visibility/order
- semantic labels
- screen-reader state
- color-independent status
- contrast
- zoom/reflow
- touch targets
- reduced motion
- error identification
- accessible authentication
- captions/transcripts where relevant
- RTL/LTR
- locale-aware text expansion.

## 12. Accessibility testing

Automated:
- lint/static rules
- axe-like browser checks
- keyboard route tests
- contrast/token checks
- component stories.

Manual/assisted:
- screen reader
- keyboard-only
- zoom/reflow
- RTL usability
- mobile touch.

Automated checks alone cannot certify accessibility.

## 13. Low bandwidth and resilience

Global accessibility includes:
- optimized bundles/images
- progressive loading
- retry/resume
- degraded/offline flows
- clear sync state
- no hidden data loss.

## 14. Product security release gate

Block release on:
- known critical exploitable vulnerability
- tenant-isolation failure
- permission bypass
- secret leak
- failed critical dependency/license policy
- unreviewed destructive migration
- invalid signed package/provenance
- unresolved P0/P1 security incident.

## 15. Compliance evidence

Every supported regulated capability stores:
- policy version
- source references
- effective date
- tests
- review/approval
- evidence artifact
- supported jurisdiction
- known limitations.

Do not display a “compliant” badge without defining the exact scope.

