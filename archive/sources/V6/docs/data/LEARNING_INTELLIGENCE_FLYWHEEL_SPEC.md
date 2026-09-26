# Hayool OS — Learning Intelligence & Decision Flywheel Specification
Version: 6.0
Status: V1 architecture
Purpose: Make Hayool OS improve from outcomes without unsafe self-modifying production logic

---

# 1. Goal

Hayool OS must become better as it observes more work, decisions and outcomes.

“Self-improving” means:
- collect high-quality outcome evidence;
- evaluate predictions/recommendations;
- propose improved policy/model versions;
- test them offline;
- test them in Shadow Mode;
- promote only after gates.

It does NOT mean:
- model rewrites itself directly in production;
- threshold silently changes;
- hiring/pay decisions optimize themselves without oversight.

---

# 2. Data planes

## 2.1 Operational plane

Authoritative transactional data:
- PostgreSQL
- normalized domain models
- strict permissions
- finance/HR/project truth

## 2.2 Event plane

Append-oriented domain events/outbox:
- who/what/when;
- state transition;
- correlation ID;
- policy version.

## 2.3 Analytical plane

Purpose-built analytical read models/warehouse.

M0 must evaluate the simplest scalable approach.

Candidates may include:
- PostgreSQL analytical read models initially;
- columnar warehouse such as ClickHouse when justified;
- object storage/Parquet for durable analytical datasets.

Do not burden OLTP queries with unbounded BI workloads.

## 2.4 Knowledge plane

Documents, embeddings, RAG, semantic search with ACL-aware retrieval.

## 2.5 Decision plane

Decision Registry + Decision Ledger.

---

# 3. Decision Registry

Every algorithmic recommendation/decision type has a registry entry:

- decision key
- purpose
- owner
- business impact
- risk class
- allowed autonomy
- inputs
- prohibited inputs
- provider/model
- algorithm version
- threshold
- evaluation suite
- fairness requirements
- explainability method
- fallback
- effective date
- retirement date

Examples:

- `talent.skill_fit`
- `talent.assignment_recommendation`
- `project.delay_risk`
- `sales.lead_priority`
- `support.ticket_severity`
- `pricing.semantic_complexity`
- `workforce.role_need_recommendation`

---

# 4. Decision Ledger

Every material recommendation stores:

- decision ID
- tenant
- subject/entity
- context snapshot reference
- candidate set
- feature/input references
- policy/model version
- recommendation
- probability/confidence
- explanation factors
- human override
- action taken
- later outcome
- feedback
- timestamps

This is the foundation for evaluation and improvement.

---

# 5. Outcome model

Do not use vague labels like “successful employee.”

Use domain-specific outcomes.

Examples:

Project task:
- accepted?
- quality review?
- rework?
- actual/accepted time?
- deadline?
- incident?

Hiring:
- reached interview?
- hired?
- retained?
- time to productivity?
- role performance dimensions?
- manager/talent satisfaction?

Sales:
- qualified?
- proposal?
- contract?
- collected revenue?
- contribution margin?

A model is evaluated against the outcome it actually claims to predict.

---

# 6. Label quality

Labels may have sources:

- deterministic system outcome;
- manager;
- peer;
- client;
- talent self-feedback;
- audit;
- AI extraction.

Store provenance.

Human feedback is not automatically objective truth.

Weight/review label quality where appropriate.

---

# 7. Controlled policy lifecycle

DRAFT
→ OFFLINE_EVAL
→ SHADOW
→ LIMITED
→ ACTIVE
→ MONITORED
→ RETIRED

Promotion criteria are explicit and versioned.

Never silently replace active production policy because a new model exists.

---

# 8. Offline replay

Use historical states that existed at decision time.

Prevent leakage from future outcomes into the input.

Compare:
- active policy;
- candidate policy;
- human decisions;
- baseline/simple rule.

Metrics depend on decision type.

---

# 9. Shadow Mode

Candidate policy runs on live inputs but cannot change authoritative outcome.

Record:
- what it would recommend;
- confidence;
- disagreement with active policy/human;
- later outcome.

This is the default bridge to safe automation.

---

# 10. Fairness / bias

Employment-related algorithms require explicit fairness evaluation.

Potential analyses:
- selection-rate differences where lawful/appropriate;
- false-positive/false-negative rates;
- calibration;
- subgroup performance;
- intersectional slices where legally appropriate;
- language/location effects;
- grade/task difficulty normalization.

Protected/sensitive attributes should not be inferred casually.

Fairness audit data may require a separate legally governed data store and purpose limitation.

---

# 11. Performance profiles

A talent profile must not collapse into one opaque score.

Dimensions may include:
- technical quality
- delivery reliability
- estimation
- communication
- collaboration
- review quality
- rework
- domain expertise
- learning/growth
- leadership

Each dimension can include:
- estimate
- uncertainty/confidence
- sample size
- recency
- evidence links.

Use task difficulty/context normalization.

---

# 12. Recency and evidence decay

Old evidence may become less representative.

Policy may apply recency weighting.

Never erase history, but distinguish:
- lifetime evidence;
- recent evidence;
- current inferred capability.

---

# 13. Uncertainty

A recommendation based on two tasks should not appear equally certain as one based on fifty.

Expose uncertainty.

Low evidence can trigger:
- assessment;
- probationary assignment;
- human review;
- wider compensation corridor.

---

# 14. Organization graph

Hayool's intelligence model should connect:

Organization
↔ Capability
↔ Process
↔ Role
↔ Skill
↔ Person
↔ Team
↔ Work Unit
↔ Project
↔ Client
↔ Asset
↔ Cost
↔ Revenue
↔ Outcome
↔ Decision.

V1 may represent this with relational tables/read models.

Do not introduce a graph database until query/scale needs justify it.

---

# 15. Semantic layer

Natural-language analytics must resolve to governed semantic definitions.

Metric definition includes:
- name
- formula/query
- source
- dimensions
- grain
- currency/unit
- effective version
- permissions.

Examples:
Revenue != Cash Collected.
Gross Margin != Markup.
Utilization != Billable Utilization.

The AI cannot redefine them ad hoc.

---

# 16. Ask-your-company architecture

Question
→ intent
→ scope/permission
→ semantic metric/entity resolution
→ query planner
→ safe query/read model
→ result verification
→ explanation
→ provenance.

High-risk analytical responses should cite source entities/metrics.

No arbitrary unrestricted SQL from the model against production.

---

# 17. Forecasting

Forecast jobs are versioned analytical artifacts.

Store:
- target;
- horizon;
- training window;
- features;
- model;
- calibration;
- error metrics;
- uncertainty.

Compare forecasts to simple baselines.

If a sophisticated model cannot outperform baseline, do not deploy it.

---

# 18. Online experimentation

A/B tests or bandits require:
- explicit objective;
- guardrail metrics;
- sample requirements;
- stop criteria;
- user/tenant policy.

Safe early domains:
- UI;
- messaging timing;
- content recommendation;
- marketing creative;
- low-impact ranking.

High-impact employment/pay decisions are not the first place for online optimization.

---

# 19. Cross-tenant benchmarking

Default: no raw cross-tenant visibility.

Possible benchmark outputs:
- percentile ranges;
- aggregated rates;
- time-to-fill;
- task effort;
- project margin;
- utilization.

Require:
- minimum cohort size;
- anonymization;
- tenant opt-in/contractual basis;
- no reverse identification;
- access policy.

---

# 20. Privacy-preserving future work

Future options:
- federated learning;
- differential privacy;
- secure aggregation;
- tenant-local embeddings/models;
- local feature extraction.

Do not claim these are implemented until validated.

---

# 21. Data retention

Separate retention policies for:
- finance/legal records;
- HR;
- candidates;
- conversations;
- AI traces;
- recordings;
- analytics;
- model/evaluation datasets.

Deletion/rights handling must propagate to derived data where law/policy requires.

---

# 22. Data quality

Every critical analytical domain needs:
- schema contracts;
- null/range checks;
- freshness;
- lineage;
- duplicate detection;
- reconciliation.

A forecast on stale/broken data should fail closed or show low confidence.

---

# 23. Anti-Goodhart design

Never optimize a performance measure without monitoring side effects.

Examples:

If optimizing “tasks completed”:
- watch quality/rework.

If optimizing utilization:
- watch burnout/bench development.

If optimizing hiring speed:
- watch quality/fairness/retention.

If optimizing project margin:
- watch client satisfaction and talent compensation fairness.

Use balanced metrics.

---

# 24. Causal humility

Correlation is not causal evidence.

AI recommendations such as:
“this marketer causes higher revenue”
must distinguish:
- association;
- experiment;
- causal evidence.

Use controlled experiments where practical.

---

# 25. Human feedback loop

Managers/talent can mark:
- recommendation useful/not useful;
- reason;
- missing context;
- incorrect input;
- unfair/inaccurate assessment.

Feedback improves evaluation datasets but does not directly mutate production policy.

---

# 26. Model/Policy Promotion Gate

Before ACTIVE:

- data quality pass;
- privacy/permission pass;
- offline evaluation pass;
- baseline comparison;
- fairness check if workforce-related;
- Persian/local-language slice where relevant;
- shadow evidence;
- owner/risk approval based on impact;
- rollback path.

---

# 27. Data product opportunities

With proper consent/governance, Hayool may commercialize:

- benchmark reports;
- labor/skill scarcity insights;
- project-effort benchmarks;
- compensation/rate benchmarks;
- staffing forecasts;
- service pricing intelligence.

Do not sell raw identifiable customer/talent data.

---

# 28. Strategic result

The learning flywheel should make Hayool better at:

- deciding what work exists;
- estimating effort;
- selecting resource strategy;
- matching talent;
- pricing;
- predicting risk;
- planning capacity;
- recommending workforce design.

The moat compounds from evaluated outcomes, not simply more AI calls.


# 29. Champion / Challenger
Every important production policy may have:
- Champion: active approved version
- Challenger: candidate version.

Challenger cannot silently replace Champion.

Promotion follows the controlled lifecycle.

# 30. Drift
Monitor:
- input distribution drift
- label/outcome drift
- calibration drift
- subgroup performance drift
- provider/model behavior changes.

Drift may trigger:
- warning
- lower autonomy
- shadow re-evaluation
- policy rollback.

# 31. Feature Registry
For learned/predictive systems maintain governed feature definitions:
- feature name
- source
- meaning
- availability time
- leakage risk
- sensitive classification
- owner
- version.

Do not allow training-only future information to appear in real-time inference.

# 32. Exploration Safety
Recommendation systems may require exploration.

Exploration policy:
- bounded
- explicit
- appropriate to risk
- measured
- fair.

High-risk employment decisions do not use uncontrolled random exploration.

For talent marketplaces, low-risk opportunities may use controlled exposure to reduce incumbent lock-in.

# 33. Counterfactual and causal analysis
When business users ask “what caused this,” distinguish:
- descriptive association
- predictive factor
- causal evidence.

Digital Twin scenarios are simulations and should not be presented as causal certainty without supporting evidence.

# 34. Data access for analysts/AI
Analytics access is permissioned and preferably uses curated semantic/read models.

Sensitive HR/finance raw tables are not broadly exposed to general AI analyst agents.

