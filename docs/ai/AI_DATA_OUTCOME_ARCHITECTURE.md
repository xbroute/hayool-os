# AI, algorithms, analytics and outcome learning

ADR-016/021/030. Engine choice is deterministic rules -> retrieval -> solver -> prediction -> semantic decision -> generative model, chosen by problem rather than marketing. Money, eligibility, authority, dates and exact counting stay deterministic. AI Off keeps essential CRM/work/finance/HR/commerce/meeting decisions intact through structured/manual paths. Meeting's consent, local/private/external transcription, source-linked drafts, retention and approval are specified independently in `MEETING_INTELLIGENCE_CONTRACT.md`; no model may supply legal consent or authoritative action by itself.

## Registry and gateway

Algorithm record: id/version/owner/problem/input-output schema/engine class/hard constraints/objective/prohibited inputs/privacy/purpose/jurisdiction/autonomy/fallback/eval/effective interval. Gateways are separate for Engineering and Product. Provider/model registry records actual identity, supported capabilities, effective price version, region, contractual eligibility, eval state, latency/health and secret ref. Admin can register compatible/native/custom HTTP/local adapters after sandbox/egress/schema verification; registration does not grant production activation.

Before invocation: tenant ACL and purpose -> eligibility -> AI necessity/value vs non-AI baseline -> engine/model eligible set -> atomic budget reserve -> minimized context -> versioned execution -> typed validation -> deterministic action gate -> usage reconciliation/audit. Cache keys include tenant/ACL/purpose/model/prompt/input versions; retention and revocation propagate. Unknown model identity or usage cost disables automatic paid escalation. Fallback repeats all policies and may become manual; never secretly sends data to an unapproved vendor.

Jev is optional semantic provider behind DecisionEngineProvider, returning binary probability, closed choice distribution or ordinal score. No universal 0.8 threshold; calibration by decision/language/cost of error. Provider marketing claims and inherited model names remain unverified. A schema-valid answer may be wrong. Production requires private labeled eval, Persian/local-language slice, abstention/out-of-distribution handling, reviewed terms and rollback. Initial safe pilot support routing or relevance; no final hiring/payroll/permission authority.

## Work and intelligence

Workforce Architect turns goals/processes/constraints into editable capability/work/capacity gaps and build/buy/train/hire/automate scenarios. Solver produces feasible/infeasible/time-limited result, constraints, objective and alternative tradeoffs; never silently softens hard legal/availability/compensation rules. Cold-start exposure applies only among eligible qualified talent, bounded by work risk, versioned and fairness-reviewed. Human/digital resources share planning concepts, not labor rights or sensitive profiles.

Personal copilot/AI PM can summarize authorized facts and draft scope, tasks, updates and risks. Meeting extraction points to transcript/time-span and consent; draft requirements need approval. RAG retrieval is ACL-filtered before context, including counts/snippets; source references and uncertainty in answers. Tool proposals require schemas, resource scope, cost/side effects, preview/approval as applicable; hostile document instructions cannot authorize them.

Operational PostgreSQL -> outbox -> governed read models -> semantic metrics/query plans. Metric registry names formula/grain/dimensions/currency/owner/version/freshness/access; cash != revenue, markup != margin. Natural language resolves approved plans, never unrestricted SQL. Decision ledger links context snapshot/candidate set/policy/evidence/recommendation/override/action/outcome; privacy payload separated from durable minimal envelope.

Forecast model includes target/horizon/training window/features available at decision time/lineage/error/uncertainty/baseline/champion/challenger. No future-label leakage. Synthetic data proves mechanics, not predictive efficacy. Promote only if preregistered held-out evidence improves the declared outcome or value over baseline with acceptable cost; otherwise baseline/manual remains. Drift may lower autonomy or suspend, never silently retrain and promote.

Digital Twin copies versioned assumptions and immutable snapshot into isolated scenario workspace. Cost/time/capacity/cash/risk scenarios are simulations, not causal certainty. Applying a plan creates a fresh validated proposal and approvals; simulation cannot mutate live state. Outcome feedback preserves source quality and context; no universal human score or surveillance. Cross-purpose and cross-tenant learning default denied.

## Evaluation and promotion

Draft -> offline eval -> shadow -> limited cohort -> active -> monitored -> retired. Each promotion binds policy/model/prompt/feature/dataset/price versions, privacy/fairness/language results, baseline comparison, cost/latency, approval and rollback. High-impact decisions retain meaningful human review and appeal. Golden evals cover schema errors, hallucinated citations, prompt injection, provider outage, unknown model, budget concurrency, stale ACL, biased proxies, low-evidence predictions and regressions. Offline score alone is not a production-readiness claim.
