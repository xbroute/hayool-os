> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — AI Use, Cost Governance & Model Economics Specification
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping

---

## 1. Principle

Hayool OS is AI-native, not AI-maximalist.

AI must be used only when it creates enough value to justify:
- cost
- latency
- uncertainty
- privacy exposure
- operational dependency.

If deterministic code, a database query, a search index, a mathematical solver or a simple workflow solves the problem better, use that instead.

---

# 2. AI Necessity Gate

Before a new feature uses an LLM/AI model, document:

1. What decision/output is needed?
2. Can deterministic rules solve it?
3. Can a solver/search/statistical model solve it?
4. Is semantic interpretation or generation genuinely needed?
5. What is the non-AI baseline?
6. Expected quality improvement?
7. Expected monetary/business value?
8. Cost per execution?
9. Latency budget?
10. privacy/data class?
11. failure fallback?

If no clear value exists, do not add the AI call.

---

# 3. Engine selection order

Preferred decision order:

Deterministic
→ Retrieval/Search
→ Mathematical Solver
→ Statistical/Predictive Model
→ Semantic Decision Engine
→ Generative LLM/Agent.

This is not a strict hierarchy for every use case; it is a cost/correctness discipline.

---

# 4. AI Usage Ledger

Every external or metered AI operation records:

- tenant
- user
- feature
- agent
- project
- workflow
- provider
- effective model
- prompt/policy version
- input units/tokens
- output units/tokens
- cached units
- tool costs
- embedding/search cost
- image/audio cost if applicable
- retries
- raw provider cost
- platform allocated cost
- customer credits charged
- latency
- success/failure
- business outcome reference if available.

---

# 5. AI Cost Object

Calculate Fully Loaded AI Cost:

Provider API
+ gateway
+ embeddings
+ vector/search
+ retrieval/storage
+ tool/API fees
+ orchestration compute
+ retries
+ observability/logging
+ estimated support burden where materially attributable.

Do not price AI only from input/output token cost.

---

# 6. AI Credits

AI Credits remain Hayool commercial units.

They are not direct token resale.

Credit pricing can include:
- raw AI cost
- orchestration
- platform value
- support
- margin
- provider-price volatility buffer.

Credits are versioned.

Existing committed plans follow explicit repricing/grandfathering rules.

---

# 7. BYOK

Eligible plans may use Bring Your Own Key.

BYOK policy controls:
- providers
- data scopes
- supported features
- cost reporting
- fallback.

Hayool can still charge platform/orchestration usage even where the customer pays raw model API directly, subject to plan terms.

---

# 8. Model routing

Model routing objective:

Meet required quality/security/latency at lowest sustainable cost.

Inputs:
- task type
- difficulty
- privacy class
- context length
- tool requirement
- historical eval quality
- latency
- provider health
- current price
- tenant plan
- budget.

A premium model should not answer a trivial deterministic question.

---

# 9. Model evaluation

For each routed task category:
- benchmark candidate models
- quality
- latency
- cost
- tool reliability
- structured-output success.

Provider/model changes must pass eval before becoming default for important workflows.

---

# 10. Caching and reuse

Use:
- exact cache
- retrieval cache
- deterministic artifacts
- reusable summaries
- prompt prefix/provider cache where supported.

Never cache across tenant/security boundaries.

Cache invalidation and privacy retention must be defined.

---

# 11. Request deduplication

Avoid duplicate calls caused by:
- repeated browser request
- workflow retry
- concurrent user action.

Use idempotency/deduplication.

---

# 12. Budget Governor

Budgets can exist:
- platform
- tenant
- department
- project
- user
- agent
- workflow.

Controls:
- hard cap
- soft alert
- daily/monthly
- per request
- fallback model
- disable expensive feature.

---

# 13. Graceful degradation

When AI budget/provider unavailable:
- cached result
- smaller model
- deterministic fallback
- manual flow.

Core ERP/business operations must remain functional.

---

# 14. AI ROI

Where measurable, compare:

AI feature cost
vs
- labor saved
- revenue influenced
- error reduced
- response time
- conversion
- retention
- project margin.

An AI feature consistently producing negative value should be optimized, downgraded or removed.

---

# 15. Feature-level AI modes

Tenant/admin can configure:
- Off
- Manual invoke
- Assist
- Automatic.

AI Off mode must remain usable for major core modules.

---

# 16. External provider governance

Track:
- DPA/privacy
- retention
- data residency
- training policy
- subprocessor
- regional endpoint
- availability
- price terms.

Sensitive data routes only to approved providers.

---

# 17. Self-host/local model

On-Prem/Dedicated may use:
- local models
- private inference
- approved external providers
- mixed routing.

Architecture must not assume public Internet AI access.

---

# 18. AI cost shock response

If provider cost changes:
1. detect new price schedule;
2. estimate effect on plan margins;
3. route alternatives;
4. update future credit schedule if needed;
5. notify business owner for material changes.

No silent customer repricing.

---

# 19. AI margin floor

Admin/platform policy can set:
- minimum AI gross margin
- minimum AI contribution margin.

Model router/pricing engine may choose a cheaper acceptable model before violating margin.

---

# 20. AI experimentation

Prompt/model experiments:
- control
- candidate
- quality
- cost
- latency
- business outcome.

Promote only when candidate meets guardrails.

---

# 21. Developer extensions using AI

Extensions declare:
- external AI provider
- data sent
- expected cost
- whether charges use Hayool Credits/BYOK/extension billing.

Tenant admins see AI data/expense implications before installation.

---

# 22. Anti-patterns

Do not:
- add AI because a feature looks modern;
- summarize data the UI already displays clearly;
- use LLM to perform exact arithmetic;
- call multiple premium models for routine tasks without measured benefit;
- hide AI variable costs inside “unlimited” low-priced plan;
- make essential business data inaccessible when AI is disabled.

