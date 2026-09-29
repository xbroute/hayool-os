# Hayool OS — Agent Instructions

This file is the repository map and persistent instruction layer for coding agents that support `AGENTS.md`.

## Read first

- `docs/engineering/AI_ENGINEERING_CONSTITUTION.md`
- `docs/engineering/ENGINEERING_GUARDRAILS.md`
- `docs/engineering/AUTONOMOUS_SDLC_CONTROL_PLANE_SPEC.md`
- `docs/product/HAYOOL_OS_MASTER_PRODUCT_ENGINEERING_SPEC.md`
- `docs/product/OWNER_DECISION_SHEET.md` for product defaults
- relevant data/AI/compliance specs
- `PROJECT_STATE.md`
- `NEXT_ACTIONS.md`
- relevant `REQ-*` and `ADR-*`

Keep this file short. Deeper knowledge lives in `docs/`.

## Non-negotiables

- Repository state beats remembered chat context.
- Material feature change => update requirement; architecture change => update ADR.
- No direct push to protected `main`.
- No direct production mutation.
- Never weaken/delete valid tests to make CI pass.
- Never commit/expose secrets.
- Accounting/payroll/tax/billing/permission/money logic is deterministic.
- AI decisions are permission/policy/autonomy gated and auditable.
- Cross-tenant data leakage is release-blocking.
- Significant UI changes require RTL/LTR, accessibility and staging browser review.
- Be honest about partial/incomplete work.

## TypeSafe/Jev

Read `docs/ai/JEV_DECISION_ENGINE_SPEC.md` before changing decision-intelligence code.

Jev is a replaceable decision provider, not a math engine or authoritative business-rule engine. Questions/thresholds/models are versioned and evaluated before production. TypeSafe commercial/data terms are an external dependency; never expose raw Jev as a standalone resale without explicit current license permission.

## Review expectations

When reviewing code, explicitly flag:

- missing REQ/ADR traceability
- weakened tests
- tenant/permission leaks
- financial nondeterminism
- secrets exposure
- unversioned AI policy/thresholds
- AI side effects that bypass approval
- missing failure/idempotency handling
- inaccessible/broken RTL UX
- undocumented dependency/license risk


## Autonomous SDLC

- Single writer per branch/repair iteration.
- Review agents are read-only.
- Review PASS applies only to exact SHA.
- Hard CI/guardrail failure cannot be overridden by model consensus.
- Effective provider/model identity must be recorded even when a compatibility alias is used.


## V4 product invariants

- Work/Capability is modeled before static job title.
- Talent matching is constraint-first, multi-objective and includes fair cold-start exposure.
- Trust & Safety is required before network scale.
- Engagement modes have distinct legal/payment semantics.
- Cross-tenant raw learning is off by default.
- Initial commercial ICP remains focused unless Owner Decision updates it.


## V5 platform architecture

When changing universal entities, customization, physical operations, global packs or industry behavior, read the corresponding files under:
- `docs/platform/`
- `docs/domains/`
- `docs/data/`
- `docs/ai/`

Do not solve cross-industry extensibility by weakening core invariants.


## Developer Platform / extension work

Read:
- `docs/platform/DEVELOPER_PLATFORM_EXTENSION_RUNTIME_MARKETPLACE_SPEC.md`
- `docs/engineering/ENGINEERING_GUARDRAILS.md`

Do not solve a tenant-specific requirement by patching Core when a supported extension path is appropriate.

## AI usage economics

Before adding a new metered AI call, read:
`docs/ai/AI_USE_COST_GOVERNANCE_SPEC.md`

## Pricing changes

Before changing plan/price/discount/AI-credit behavior, read:
`docs/product/PRICING_PROFIT_OPTIMIZATION_EXPERIMENTATION_SPEC.md`

