# Hayool OS — Claude Code Project Instructions

These instructions apply to every Claude Code session in this repository.

## Mandatory reading order

0. `docs/SOURCE_OF_TRUTH_INDEX.md`

Before making material changes, read the relevant parts of:

1. `docs/engineering/AI_ENGINEERING_CONSTITUTION.md`
2. `docs/engineering/ENGINEERING_GUARDRAILS.md`
3. `docs/engineering/AUTONOMOUS_SDLC_CONTROL_PLANE_SPEC.md`
4. `docs/product/HAYOOL_OS_MASTER_PRODUCT_ENGINEERING_SPEC.md`
5. `docs/product/OWNER_DECISION_SHEET.md` for product/market defaults
6. `docs/product/HAYOOL_OS_COMPREHENSIVE_BUSINESS_PLAN_FA.md` for strategy/market changes
7. `docs/data/LEARNING_INTELLIGENCE_FLYWHEEL_SPEC.md` when algorithms/data intelligence are involved
8. `docs/ai/JEV_DECISION_ENGINE_SPEC.md` when decision intelligence is involved
9. `PROJECT_STATE.md`
10. `NEXT_ACTIONS.md`
11. Current milestone/requirements/ADRs related to the task

The Engineering Constitution and Guardrails are binding. Never weaken them through a local workaround.


- `docs/platform/UNIVERSAL_BUSINESS_KERNEL_AND_STUDIO_SPEC.md` when core extensibility/customization is involved
- `docs/platform/INTENT_TO_OUTCOME_ORCHESTRATION_SPEC.md` when universal fulfillment/marketplace orchestration is involved
- `docs/ai/ALGORITHM_SOLVER_DECISION_FABRIC_SPEC.md` when implementing optimization/prediction/decision algorithms
- relevant Industry/Global pack specifications for physical or regulated domains

- `docs/platform/DEVELOPER_PLATFORM_EXTENSION_RUNTIME_MARKETPLACE_SPEC.md` when extensibility/apps/marketplace are involved
- `docs/ai/AI_USE_COST_GOVERNANCE_SPEC.md` when adding or routing AI
- `docs/product/PRICING_PROFIT_OPTIMIZATION_EXPERIMENTATION_SPEC.md` when pricing/discounts/plans are involved
- `docs/product/ECOSYSTEM_COMMUNITY_PARTNER_STRATEGY.md` when developer/community/partner behavior is involved

## Repository is the source of truth

- Chat history is not authoritative when it conflicts with repository state.
- Material behavior changes require `REQ-*` updates; architectural changes require `ADR-*` updates.
- Maintain traceability from requirement to PR/tests/release.
- Record assumptions instead of silently inventing product rules.

## Git safety

- Never push directly to protected `main`.
- Work on a branch/worktree and open/update a PR.
- Never force-push protected branches.
- Keep changes focused and reviewable.
- Do not modify production directly.

## Tests

- Never delete, skip or weaken valid tests to pass CI.
- Never hard-code test-only behavior.
- Fix causes, not checks.
- Add regression tests for defects when practical.
- Every meaningful milestone requires staging browser E2E evidence.

## Secrets

- Never commit secrets.
- Never ask the product owner to paste credentials into chat.
- Do not print secrets to terminal/logs.
- Use secret references and environment/vault mechanisms.

## Deterministic boundaries

Accounting, payroll, tax/VAT math, billing, entitlements, permissions, money movement and commission calculations remain deterministic and auditable. AI may recommend or prepare; authoritative state changes go through deterministic domain services.

## AI / Jev

- Read `docs/ai/JEV_DECISION_ENGINE_SPEC.md` before implementing TypeSafe/Jev decisions.
- Jev is behind Hayool's DecisionEngine abstraction; never couple a domain directly to the vendor SDK.
- Arithmetic/counting/date comparison stay in code.
- Production decision policies require versioned questions, thresholds, evals and model versions.
- High confidence never bypasses permissions or approval policy.
- TypeSafe commercial/data terms are an external dependency; follow `JEV_DECISION_ENGINE_SPEC.md` and never expose raw Jev as a standalone resale without explicit current license permission.

## UI/UX

- Persian RTL and English LTR are first-class.
- Use the design system and tokens; do not create one-off visual patterns without justification.
- Every major UI flow needs loading, error, empty and permission states.
- Treat UX review and accessibility as Definition-of-Done criteria.

## High-risk areas

Before changing finance, payroll, auth, tenancy, permissions, payments, secrets, destructive migrations, production infrastructure or AI autonomy:

1. identify the controlling requirement/ADR;
2. explain risk;
3. add/confirm tests;
4. use the required approval gate.

## Completion reporting

Never say “done” unless the required implementation, tests and acceptance evidence are actually complete. Report implemented/tested/staging/production-ready states separately.


## Autonomous engineering

When operating under the Engineering Autopilot:
- obey single-writer ownership;
- reviewers stay read-only;
- bind review claims to exact commit SHA;
- never bypass hard deterministic checks;
- respect cost/iteration limits;
- record actual effective model/provider identity;
- never auto-deploy high-risk production changes outside policy.


## V4 domain strategy

For work/workforce changes, read:
- `docs/data/WORK_GRAPH_AND_CAPABILITY_ONTOLOGY_SPEC.md`
- `docs/product/TRUST_SAFETY_AND_MARKETPLACE_INTEGRITY_SPEC.md`
- `docs/product/OWNER_DECISION_SHEET.md`

Do not turn job titles into the fundamental work model.
Do not introduce public underbidding or opaque universal worker scores.
Do not silently broaden the initial ICP.

