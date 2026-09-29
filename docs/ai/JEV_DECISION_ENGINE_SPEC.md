> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — TypeSafe Jev / Decision Intelligence Specification

Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping
Purpose: Define how TypeSafe AI Jev is used inside Hayool OS without vendor lock-in or unsafe automation.

## 1. Conclusion of the technical review

TypeSafe AI's Jev is a strong architectural fit for Hayool OS **as a narrow decision primitive**, not as a replacement for generative LLMs, deterministic business logic, mathematical engines or human governance.

The key design insight is to use Jev where Hayool needs a fast, cheap, typed, probability-bearing judgment inside a workflow. Examples include routing, classification, prioritization, semantic risk checks, gating and verification.

The integration must remain optional and provider-neutral because:

- Jev is currently a hosted API rather than a self-hosted model.
- The model can be semantically wrong even though its output type is guaranteed.
- Current vendor documentation says Jev performs best on narrow System-One tasks and warns against math, numeric precision, date comparison, long irrelevant state, indirection and generation.
- English is currently the strongest language, so Persian use cases need independent evaluation.
- On-Premise customers may require offline or data-residency modes.

Therefore Hayool will implement a **Decision Intelligence Layer (DIL)** and a `DecisionEngineProvider` abstraction. `TypeSafeJevProvider` is the preferred V1 hosted provider for suitable tasks, but no business domain is allowed to depend directly on Jev.

## 2. Decision Intelligence Layer

Conceptual flow:

```text
Domain Event / Workflow State
          |
          v
Deterministic preconditions + ACL + data minimization
          |
          v
Decision Policy Registry
          |
          v
Decision Engine
   |          |          |
   |          |          +--> RuleBasedDecisionProvider
   |          +-------------> StructuredLLMDecisionProvider
   +------------------------> TypeSafeJevProvider
          |
          v
Typed Decision Result
          |
          v
Confidence / probability gate
          |
          v
Deterministic Policy + Autonomy Level
          |
    +-----+-----------+
    |                 |
Auto action     Approval / Human / Fallback
```

## 3. Required provider contract

Domain code consumes a Hayool-owned contract resembling:

```ts
interface DecisionEngineProvider {
  evaluate(request: DecisionRequest): Promise<DecisionResponse>;
  capabilities(): DecisionProviderCapabilities;
  health(): Promise<ProviderHealth>;
}
```

The request must use Hayool concepts, not TypeSafe SDK classes.

Required typed primitives in Hayool:

- `binary_probability` — semantic yes/no probability
- `choice_distribution` — closed-set selection + distribution
- `ordinal_score` — ordered semantic score

Jev maps naturally to Noul, Choice and Score.

Alternative providers can emulate the same Hayool contract using structured LLM output, local classifiers or deterministic rules.

## 4. Decision Policy Registry

Every production decision definition is stored/versioned as a first-class policy.

Recommended fields:

- `decision_key`
- `version`
- `status`: draft / shadow / active / retired
- owner
- domain
- purpose
- input schema
- state builder version
- questions
- criteria
- primitive type
- provider policy
- pinned model version
- confidence/probability thresholds
- autonomy mapping
- fallback policy
- evaluation dataset/version
- approved metrics
- effective_from/effective_to
- created_by/approved_by
- change reason

Questions and thresholds must be easy for humans to review in one place.

## 5. Model version policy

Development may experiment with a moving alias.

Production decision policies must normally pin the model version that passed the policy's evaluation suite.

When a new Jev version arrives:

1. Do not silently switch production thresholds.
2. Run the existing golden/private evaluation set against the new version.
3. Compare calibration, false positives, false negatives, abstention/escalation rate, cost and latency.
4. Re-tune thresholds only through a new policy version.
5. Activate through Shadow Mode or controlled rollout.
6. Preserve the model/version used for historical decisions.

## 6. Confidence and probability policy

Never equate confidence with correctness.

Use:

- returned probabilities when the policy needs mathematically meaningful thresholds per outcome;
- confidence as an uncertainty/clarity signal for Choice/Score;
- explicit thresholds based on measured private evals;
- conservative escalation for high-cost mistakes.

No universal threshold such as `0.8` is allowed across all decisions.

Each action type has its own risk-calibrated threshold.

## 7. What Jev SHOULD do in Hayool OS

### 7.1 AI/model routing

Examples:

- classify task complexity as `simple / normal / complex / frontier`
- classify whether a request needs vision/tool-use/reasoning
- score privacy sensitivity
- score urgency
- choose cheap/balanced/frontier model tier
- decide if a local/private model is required

Code then applies provider availability, budget and entitlement constraints.

### 7.2 Tool-call and autonomy risk gate

Before an AI agent executes a tool, Jev may judge semantic risk dimensions such as:

- destructive intent
- financial impact
- confidentiality
- permission ambiguity
- external side effect
- production impact

The final action is still controlled by deterministic permission/autonomy policy.

Jev must never override a denied permission.

### 7.3 Prompt-injection and LLM guardrail layer

Use Jev as one signal around generative LLMs for:

- jailbreak/injection likelihood
- whether retrieved text is trying to instruct the model
- whether generated output violates a workflow policy
- whether an action needs escalation

Do not present Jev as a perfect security boundary. Combine it with deterministic sanitization, tool permissions, data minimization and testing.

### 7.4 RAG passage classification

After retrieval and before generative answering, classify each passage for:

- relevance
- usable evidence
- contradiction
- instruction/prompt injection
- tenant/project relevance

Code decides keep / conflicting evidence / drop.

This is especially useful for Client Portal support and project knowledge assistants.

### 7.5 Support and SLA triage

Jev can evaluate:

- category
- severity
- urgency
- escalation need
- likely SLA risk
- billing vs technical vs project issue
- sentiment/frustration level

Date/deadline arithmetic remains in code.

### 7.6 CRM / lead routing

Atomic semantic judgments may include:

- service fit
- urgency
- buying intent
- lead quality
- enterprise complexity
- required sales specialist

Final lead score should be a transparent code-level composition of named dimensions rather than an opaque single prompt.

### 7.7 Talent matching

Use Jev for job-relevant semantic dimensions such as:

- evidence strength for a required skill
- domain relevance
- similarity of previous work
- ambiguity in claimed experience
- role fit for a defined work package

Hard constraints (availability, rate floor, contract type, location restrictions, permission, conflict of interest) are deterministic.

Protected/sensitive personal attributes must not become ranking signals.

### 7.8 Recruitment screening

Jev can assist with narrow dimensions and triage, but it does not make unexplained final employment decisions.

Candidate evaluation should decompose dimensions such as:

- skill evidence
- system-design depth
- role-relevant communication evidence
- requirement match

Human-readable rubric + evidence is mandatory.

Final hiring/termination defaults to protected human approval.

### 7.9 Project intake and requirement quality

After an LLM generates/normalizes a project brief, Jev can verify/classify:

- ambiguity
- missing dependency
- requirement testability
- scope-risk category
- whether an item is a requirement/assumption/constraint/question
- whether a requirement likely needs clarification

Jev does not generate long requirement prose.

### 7.10 Project risk

Atomic signals:

- requirement ambiguity risk
- dependency risk
- client-response risk
- skill mismatch risk
- scope-creep likelihood
- quality/rework risk

Timeline/date calculations and financial exposure are deterministic.

### 7.11 Pricing and compensation

Jev MAY produce semantic features such as:

- complexity bucket
- requirement ambiguity
- novelty
- integration difficulty
- coordination difficulty
- risk level
- likely review intensity

Jev MUST NOT calculate money, margin, tax, exact effort totals, hourly pay or date arithmetic.

Deterministic Pricing/Compensation engines consume semantic features plus rate books, historical data and hard rules.

### 7.12 Task grade recommendation

Jev can judge whether a task semantically requires characteristics associated with Junior/Mid/Senior work, such as:

- ambiguity tolerance
- architectural responsibility
- blast radius
- need for independent decision-making
- specialist depth

Resource Optimizer then compares expected total delivery cost and hard constraints.

### 7.13 Meeting intelligence verification

Generative speech/transcription/LLM components produce candidate summaries/tasks/decisions.

Jev can verify/classify whether each candidate item is:

- supported by transcript
- a decision
- an action item
- a requirement
- a risk
- ambiguous and needs human review

### 7.14 Document extraction verification

Use a cascade:

cheap extraction model/parser
→ deterministic schema validation
→ Jev field-level semantic verification
→ strong reasoning model/human only when a verifier fires.

This is useful for invoices, contracts, resumes and structured intake.

### 7.15 Development pipeline

Jev may help classify:

- PR risk
- likely affected domain
- whether human review is mandatory
- tool-command risk
- whether a test failure resembles product defect / flaky test / environment issue
- issue routing

It cannot replace compilers, linters, tests or security scanners.

### 7.16 Marketing and content operations

Good uses:

- classify campaign intent/audience
- lead/content routing
- brand-risk flag
- content category
- escalation need
- experiment classification

Creative content generation stays with generative models/humans.

## 8. What Jev MUST NOT do

Do not use Jev as authoritative engine for:

- arithmetic
- accounting journal math
- VAT calculation
- payroll calculation
- commission calculation
- exact project cost
- exact time/date differences
- exact counting
- cryptographic/security authorization
- permissions
- balance computation
- invoice totals
- legal conclusion generation
- long-form generation
- final production deploy authorization
- final high-impact employment decision by default

## 9. Numerical/time rule

If the answer can be computed exactly by code, compute it in code.

If the task is semantic, use the decision engine.

If the task requires long deliberative reasoning, use a reasoning LLM/human workflow.

This rule is mandatory.

## 10. State construction and context minimization

Jev state builders must be domain-specific and versioned.

Do not dump entire customer/project/employee records into a decision call.

Only send the minimum fields needed for the specific question.

Benefits:

- better accuracy
- lower cost
- lower privacy exposure
- easier debugging
- clearer explainability

## 11. Persian and multilingual strategy

Jev currently reports English as its strongest language.

Therefore:

1. Build a Persian evaluation set before activating a Persian policy.
2. Compare direct Persian input against any normalization/translation pipeline.
3. Do not assume English thresholds transfer to Persian.
4. Keep policy language and model version in the evaluation record.
5. For high-risk Persian decisions, default to human/strong-model fallback until measured quality is acceptable.

Do not silently translate sensitive text through an external provider unless the tenant's privacy/data policy permits it.

## 12. Privacy and deployment-mode behavior

Jev is an external hosted provider.

For each tenant and data classification:

- allow/deny external AI providers
- choose permitted regions/providers when supported
- redact/minimize PII
- pseudonymize candidate/customer identifiers when the semantic decision does not need identity
- support local provider fallback

On-Premise must remain operational when external AI is disabled.

Core workflows degrade to deterministic/manual mode rather than fail.


### 12.1 Commercial, licensing and data-processing boundary

TypeSafe is a third-party hosted dependency. Before every production rollout that materially changes the integration, the engineering/legal checklist MUST re-check the current TypeSafe agreement, DPA, privacy policy and applicable order terms.

Hayool's integration policy is:

- Use TypeSafe only as an embedded capability inside Hayool applications according to the currently applicable customer-application license.
- Do not expose or resell the raw TypeSafe/Jev service as a standalone API/service unless the applicable agreement explicitly permits it.
- Hayool AI Credits represent Hayool platform usage and orchestration value, not a resale of TypeSafe credits or raw Jev access.
- Do not build product language that guarantees Jev availability, model behavior, pricing or latency indefinitely.
- Treat vendor API updates as potentially incompatible until tested.
- Keep provider cost, Hayool internal credit pricing and customer-facing AI credit pricing separate.
- Maintain a vendor-offboarding path: another decision provider or manual/rule fallback must preserve core workflow correctness.
- External-provider processing must respect tenant policy, data classification, required consents and applicable privacy law.
- Minimize/pseudonymize personal data sent to the provider whenever identity is not semantically necessary.
- Never send raw secrets or credentials.

The current vendor privacy materials state that model training/fine-tuning on customer Input is not performed without the relevant consent/permission, while service operation, telemetry and subprocessors remain governed by the applicable agreement/DPA. Hayool MUST therefore evaluate the complete current contractual/data-processing terms rather than reducing privacy review to a single “not used for training” checkbox.


## 13. Jev availability and resilience

Implement:

- timeout
- bounded retry/backoff
- circuit breaker
- rate-limit handling
- health state
- fallback provider
- manual/approval fallback
- durable workflow retry where appropriate

Do not retry high-side-effect domain actions because a decision API timed out. Retry the decision request safely before the side effect.

## 14. Jev observability

Log for each decision (subject to privacy policy):

- decision key/version
- provider
- actual model version
- state-builder version
- state hash/reference, not necessarily raw sensitive state
- question-set version
- returned typed outputs
- probabilities/confidence
- thresholds
- route/action chosen
- autonomy mode
- fallback/escalation
- latency
- token use
- provider cost
- Hayool AI credits charged if relevant
- correlation ID

## 15. Evaluation framework

Every production policy requires a private, versioned evaluation dataset.

Measure as relevant:

- accuracy/agreement
- precision/recall
- false positive rate
- false negative rate
- calibration
- escalation rate
- automation coverage
- human override rate
- cost
- p50/p95 latency
- provider failure rate
- language/domain slices

For high-impact domains, evaluate disparate error patterns across appropriate job-relevant cohorts without introducing protected attributes into production ranking logic.

## 16. Threshold promotion workflow

Draft
→ Offline Eval
→ Shadow
→ Reviewed Thresholds
→ Limited rollout
→ Active
→ Monitor
→ Re-evaluate on model/question change

No threshold is promoted solely because a demo looked good.

## 17. Question design rules

1. One narrow judgment per question.
2. Prefer direct positive wording.
3. Explicitly define boundaries/criteria.
4. Avoid double negatives.
5. Avoid hidden multi-hop reasoning.
6. Avoid irrelevant state.
7. Keep math outside the model.
8. Keep dates normalized/compared in code.
9. Treat adversarial text as data.
10. Review question and threshold changes like code.

## 18. Decision composition

For complex business judgments:

- decompose into atomic dimensions
- call Jev on those dimensions
- combine with explicit code-level weights/rules
- version the weights
- expose them for authorized explanation

Do not ask one huge question such as “Is this candidate good?” or “What price should we charge?”

## 19. Future learning strategy

As Hayool accumulates real outcomes, decision features may feed classical/ML models for tasks such as:

- effort estimation
- project delay prediction
- churn prediction
- conversion prediction
- rework prediction

Jev can provide semantic features, while supervised models learn from Hayool's own outcomes.

This creates a path from AI heuristics to calibrated company-specific prediction without tying core business logic to one generative model.

## 20. Development integration

During development, install the official TypeSafe agent skill for Claude Code or the selected coding agent.

The coding agent may use the skill to propose candidate Jev opportunities and run low-risk experiments with a dedicated development API key.

Rules:

- no production key in prompts
- no unreviewed threshold promotion
- experiments recorded in `docs/ai/experiments/`
- promising use cases become `DEC-*`/`REQ-*` policies
- poor-performing use cases remain deterministic/LLM/manual

## 21. V1 Jev deliverables

M0/M9 must eventually produce:

- `DecisionEngineProvider` contract
- `TypeSafeJevProvider`
- provider health/fallback
- Decision Policy Registry
- versioned Question Registry
- Decision Run audit model
- Evaluation Dataset model
- Shadow Mode integration
- threshold/policy UI for authorized admins
- Jev cost/usage attribution
- Persian evaluation harness
- at least one safe low-risk production pilot before wider activation

Recommended first pilots:

1. support-ticket routing
2. RAG passage relevance/injection classification
3. model-routing complexity classification
4. development PR-risk classification

Do not start with payroll, money movement or final hiring decisions.


## 20. Workforce / marketplace V4 constraints

Jev may contribute narrow semantic signals to:
- work complexity
- skill evidence relevance
- talent/work fit components
- support/risk triage
- retrieved evidence relevance.

It MUST NOT become a universal worker ranking engine.

Matching first applies deterministic eligibility/constraints and then combines multiple objectives.

Fair-exposure/exploration policy is handled by Hayool's deterministic matching policy, not delegated to one Jev confidence score.

## 21. Trust & Safety

Jev may triage:
- report category
- suspicious semantic pattern
- evidence relevance
- content risk.

It does not impose irreversible sanctions.

## 22. Work Graph

Jev questions should reference normalized Work Graph state rather than arbitrary giant profile dumps.

State builders should minimize irrelevant fields and sensitive personal data.

