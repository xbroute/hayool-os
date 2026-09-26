# Pull Request

## Requirement / scope
- Related REQ(s):
- Related issue(s):
- Related ADR(s), if architecture changed:

## What changed
Describe the smallest coherent change in this PR.

## Why
Explain the user/business/technical reason.

## Risk classification
- [ ] Low
- [ ] Medium
- [ ] High-risk area (finance/payroll/auth/tenancy/permissions/payment/secrets/production/AI autonomy/destructive migration)

## Source of Truth
- [ ] Relevant REQ updated or no behavior change occurred.
- [ ] ADR updated/created if architecture changed.
- [ ] PROJECT_STATE/NEXT_ACTIONS updated if milestone state changed.

## Security / tenancy
- [ ] Authorization checked.
- [ ] Tenant isolation considered/tested.
- [ ] No secret or credential added to Git/logs.
- [ ] External/untrusted data handling considered.
- [ ] AI tool/action permissions reviewed if applicable.

## Deterministic business logic
- [ ] Financial/payroll/tax/billing/commission/permission logic remains deterministic.
- [ ] AI is not used as the authoritative calculator/rule engine.
- [ ] Automated decision is explainable/versioned if applicable.

## TypeSafe/Jev
- [ ] Not applicable.
- [ ] Decision policy is behind DecisionEngineProvider.
- [ ] Questions/criteria/threshold/model/state-builder are versioned.
- [ ] Evaluation/Shadow Mode evidence exists before production automation.
- [ ] No arithmetic/date/accounting authority delegated to Jev.

## Tests
- [ ] Unit/domain tests.
- [ ] Integration tests.
- [ ] Permission/tenant tests.
- [ ] Regression test for bug, if applicable.
- [ ] Relevant tests were not deleted/weakened merely to pass CI.

Commands/results:

```text
paste concise evidence
```

## UI/UX
- [ ] Not applicable.
- [ ] Persian RTL reviewed.
- [ ] English LTR reviewed.
- [ ] Loading/error/empty/permission states covered.
- [ ] Responsive behavior reviewed.
- [ ] Accessibility/keyboard behavior reviewed.
- [ ] Browser E2E/staging evidence available.

## Migration / rollback
- Migration impact:
- Rollback/recovery plan:

## Screenshots / staging
Add links/evidence when UI changed.

## Known limitations
List explicitly. Do not hide incomplete behavior.

## Completion state
- [ ] Implemented
- [ ] Tested
- [ ] Staging verified
- [ ] Production-ready under current release policy


## Work / Workforce
- [ ] Not applicable.
- [ ] Work/Capability model remains primary; no title-only shortcut introduced.
- [ ] Matching change considers hard constraints before ranking.
- [ ] Cold-start/fair-exposure impact considered.
- [ ] No public race-to-the-bottom bidding introduced.
- [ ] No opaque universal worker score introduced.
- [ ] Purpose limitation for worker/candidate data considered.

## Trust & Safety
- [ ] Not applicable.
- [ ] Fraud/abuse/dispute impact considered.
- [ ] High-impact restriction has review/appeal path where applicable.
- [ ] Engagement mode/legal counterparty remains explicit.

## Analytics / Learning
- [ ] Not applicable.
- [ ] Metric definitions are governed.
- [ ] No unrestricted production SQL from AI.
- [ ] Predictive change includes baseline/uncertainty.
- [ ] Cross-tenant learning/privacy policy respected.
- [ ] No silent self-modifying production policy.

## Critical test protection
- [ ] This PR does not weaken protected invariant/tenant/security/release tests.
- [ ] If a protected test changed, independent approval/rationale is attached.


## Extensions / Developer Platform
- [ ] Not applicable.
- [ ] No protected Core patch used for customer-specific behavior.
- [ ] Public API/event compatibility checked.
- [ ] App permission/data/egress impact reviewed.
- [ ] Extension remains isolated from protected Core/tenant data.
- [ ] Manifest/version/update/uninstall behavior considered.
- [ ] Public contract change has migration/deprecation plan.

## AI Cost / Necessity
- [ ] Not applicable.
- [ ] A metered AI call is justified over deterministic/search/solver alternatives.
- [ ] Cost attribution/budget behavior exists.
- [ ] AI-off/provider-failure fallback considered.
- [ ] Model choice has evaluation/cost rationale.

## Pricing / Commercial Logic
- [ ] Not applicable.
- [ ] Margin vocabulary is correct.
- [ ] Hard price/margin floors cannot be bypassed.
- [ ] Pricing experiment has defined cohort/hypothesis/guardrails if applicable.
- [ ] No sensitive-attribute hidden individualized pricing introduced.

