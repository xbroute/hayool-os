# Hayool OS — Algorithm, Solver & Decision Fabric
Version: 6.0
Status: Core intelligence architecture

---

## 1. Purpose

Hayool OS must use the correct computational tool for each problem.

"Use AI everywhere" is not an architecture.

The platform recognizes at least five engine classes:

1. Deterministic Rule Engine
2. Mathematical Optimization / Constraint Solver
3. Predictive ML / Forecasting
4. Semantic Decision Engine (e.g. Jev)
5. Generative/Agentic LLM

---

## 2. Deterministic Rule Engine

Use for:
- permissions
- tax formula
- payroll
- invoice math
- accounting
- eligibility
- policy precedence
- hard legal constraints
- unit conversions.

---

## 3. Optimization / Solver Engine

Use for:
- scheduling
- shift planning
- workforce allocation
- vehicle routing
- load planning
- inventory replenishment optimization
- production scheduling
- procurement allocation
- assignment under constraints.

Candidate implementations/providers are evaluated during M0.

Business code uses `OptimizationProvider`.

A solver result includes:
- objective
- constraints
- solution
- feasibility
- optimality/status
- version.

---

## 4. Predictive ML

Use for:
- demand
- cash collection
- churn/renewal
- project delay
- workload
- time/effort
- maintenance failure risk
- inventory demand.

Every predictor has:
- target
- baseline
- training/eval window
- data lineage
- error metrics
- uncertainty
- version.

---

## 5. Semantic Decision Engine

Use for typed semantic judgments:
- relevance
- complexity category
- intent
- evidence strength
- risk signal
- fit dimension.

Jev is one provider.

---

## 6. Generative / Agentic LLM

Use for:
- clarification
- plan drafting
- writing
- code
- summaries
- conversational UX
- decomposition
- explanations.

Generated plans must be validated by deterministic/typed systems before side effects.

---

## 7. Algorithm Contract

Every production algorithm/policy declares:

- ID
- owner
- problem type
- engine class
- inputs
- outputs
- hard constraints
- objective
- prohibited inputs
- fallback
- explainability
- evaluation
- fairness if applicable
- privacy class
- version
- effective dates
- autonomy level.

---

## 8. Multi-objective value function

Optimization can balance:
- quality
- cost
- time
- risk
- fairness
- continuity
- user preference
- sustainability
- growth/learning.

Weights/policies are versioned.

Hard constraints are never converted into weak weights.

---

## 9. Explainability

For solver/ranking:
- constraints satisfied/violated
- key tradeoffs
- alternate options
- sensitivity where practical.

For prediction:
- uncertainty
- key features/factors
- limitations.

For semantic models:
- evidence/context references.

---

## 10. Learning

Algorithm updates follow Learning Intelligence Flywheel.

No silent online self-modification.

---

## 11. Simulation / Replay

Before changing important algorithms:
- replay historical cases
- compare baseline/current/candidate
- measure business outcome
- detect subgroup issues
- estimate cost.

Digital Twin can test strategy changes without committing them.

---

## 12. Failure handling

If an advanced engine is unavailable:
- deterministic safe fallback
- simpler heuristic
- manual queue.

Core business must not become unusable because the "smart" optimizer is down.

---

## 13. AI cost

Routing chooses lowest-cost engine satisfying quality/risk need.

Do not use expensive LLM for deterministic arithmetic or simple lookup.


## 14. AI necessity / economics

Before adopting a metered AI engine, apply the AI Necessity Gate defined in:

`docs/ai/AI_USE_COST_GOVERNANCE_SPEC.md`

Correct engine choice includes economic cost, not only technical feasibility.

## 15. Extension algorithms

Third-party extensions may register algorithms/solvers through approved interfaces.

They declare:
- inputs/outputs
- engine class
- permissions
- cost
- external processing
- evaluation/fallback.

Core policy retains authority over protected side effects.

