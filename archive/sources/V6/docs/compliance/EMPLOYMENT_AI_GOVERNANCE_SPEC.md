# Hayool OS — Employment AI & Workforce Decision Governance
Version: 6.0
Status: Mandatory architecture for workforce AI
Purpose: Support explainable, contestable and jurisdiction-aware AI in recruitment, allocation and performance workflows

---

# 1. Principle

Employment and worker-management decisions can significantly affect people.

Hayool must treat workforce AI as a governed high-impact domain, not as ordinary recommendation UI.

This specification does not replace legal advice or country packs.

---

# 2. AI Decision Inventory

Maintain a registry of workforce AI use cases:

- sourcing
- job ad targeting
- candidate matching
- screening
- interview analysis
- assessments
- shortlist
- compensation recommendation
- task allocation
- scheduling
- performance evaluation
- promotion/mobility
- replacement recommendation
- termination-supporting analysis

For each:
- jurisdiction
- purpose
- controller/processor roles
- data used
- legal basis/consent if required
- significant-decision classification
- human involvement
- model/policy
- bias evaluation
- notice requirement
- appeal/review
- retention.

---

# 3. Human review

For high-impact employment outcomes, the default is meaningful human review.

Human reviewer must have:
- authority to change outcome;
- relevant evidence;
- time to review;
- explanation;
- ability to request additional information.

“Click approve automatically” is not meaningful review.

---

# 4. Candidate notice

Where required or product policy chooses transparency:
- disclose AI/automation use;
- explain the general purpose;
- identify relevant data categories;
- explain review/appeal;
- provide accessibility/accommodation channel;
- retention/privacy link.

---

# 5. Contestability

Candidate/worker can:
- request correction of factual data;
- challenge a significant automated outcome where applicable;
- request human review where required/available;
- provide missing context.

The audit trail records challenge and resolution.

---

# 6. Bias/fairness

Workforce decision policies require:
- documented evaluation;
- monitored drift;
- job/role-specific analysis where relevant;
- language/locality checks;
- accessible alternative process.

Do not infer sensitive/protected traits solely to drive selection.

If sensitive traits are legitimately collected for fairness audit, isolate purpose/access.

---

# 7. Performance monitoring

Do not use invasive surveillance as default.

Avoid unsupported inference of:
- mental state;
- personality;
- health;
- political/religious views;
- sensitive personal traits.

Use evidence related to job/work outcomes.

---

# 8. Automatic replacement/termination

Automatic replacement recommendation can exist.

Automatic termination of employees is a protected action by default.

For bounded freelance assignments, automated reassignment may be permitted only when:
- contract/policy allows;
- objective acceptance condition exists;
- dispute/review path exists;
- jurisdiction permits.

---

# 9. Explainability

For a significant recommendation, authorized users should see:
- main factors;
- evidence;
- uncertainty;
- missing data;
- policy/model version.

Candidate-facing explanation is designed separately to be understandable and protect confidential/security information.

---

# 10. Jurisdiction packs

Employment AI policy must be jurisdiction-aware.

The platform must be able to turn on:
- bias-audit workflow;
- notice;
- human review;
- DPIA/risk assessment;
- retention;
- additional logging;
- restricted automation;
- prohibited feature use.

---

# 11. EU readiness

Recruitment, selection, worker-management, task allocation based on behavior/traits, performance monitoring and related employment AI may fall into high-risk categories under the EU AI Act.

Architecture therefore must support:
- risk management;
- data governance;
- technical documentation;
- logs/records;
- transparency;
- human oversight;
- accuracy/robustness/cybersecurity;
- post-market monitoring as applicable.

Exact obligations/timing must be checked against current law at deployment time.

---

# 12. NYC AEDT readiness

Where applicable, support:
- bias audit artifacts;
- publication/export of required summaries;
- candidate/employee notice;
- data-use/retention information;
- audit versioning.

Exact applicability is jurisdiction/use-case dependent.

---

# 13. UK data protection readiness

Support:
- DPIA;
- lawful-basis documentation;
- controller/processor roles;
- data minimization;
- transparency;
- fairness/bias monitoring;
- safeguards for solely automated significant decisions;
- human review/challenge.

---

# 14. Provider governance

If external models/Jev receive candidate/worker data:
- provider approval;
- DPA/terms review;
- minimization;
- purpose limitation;
- retention setting;
- residency requirement where relevant;
- secret removal;
- audit.

---

# 15. Product advantage

These controls should not feel like compliance paperwork bolted on later.

Turn them into features:
- AI Decision Center
- Fairness Dashboard
- Candidate Notice Templates
- Human Review Queue
- Decision Explanation
- Audit Export
- Policy Versioning
- Country Compliance Pack

This increases enterprise trust.


# 16. Worker data boundaries
Separate:
- employment HR records
- candidate records
- marketplace profile
- project performance evidence
- fairness-audit data.

Access/retention purposes differ.

Do not make a sensitive HR record automatically visible to marketplace ranking.

# 17. Data minimization in performance intelligence
Collect what improves legitimate work outcomes.

Default product must not require:
- continuous screen capture
- keystroke logging
- webcam analysis
- emotion inference
- off-hours surveillance.

Any later enterprise request for invasive monitoring requires a separate legal/product/security review and must not silently enter the shared worker reputation model.

# 18. Decision explanation quality
High-impact recommendations should provide:
- criteria
- evidence
- material factors
- uncertainty
- missing information
- policy/model version
- human override path.

Do not expose protected fraud/security internals if disclosure would enable abuse; provide an appropriate user-facing explanation instead.

# 19. Cross-context use restriction
Evidence gathered for one purpose cannot automatically be reused for another.

Example:
support-ticket tone should not silently become an employee promotion signal.

Any cross-purpose feature use requires documented purpose/justification.

