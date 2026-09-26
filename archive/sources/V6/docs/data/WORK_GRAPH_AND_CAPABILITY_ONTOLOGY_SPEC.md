# Hayool OS — Work Graph & Capability Ontology Specification
Version: 6.0
Status: Core domain architecture

## 1. Purpose
Hayool OS must reason about work independently from job titles and employment forms.

The Work Graph provides a shared semantic model connecting business goals to capabilities, processes, work, skills, resources, economics and outcomes.

## 2. Core concepts

### Goal
A desired business outcome.

### Capability
What an organization must be able to do.

### Process
A recurring or structured sequence that realizes a capability.

### Work Unit
The smallest meaningful planning unit independent of who performs it.

Subtypes may include recurring operation, project work package, task, service activity, support activity and control/review activity.

### Skill
A competence needed to perform work.

### Role
A reusable bundle of responsibilities/capabilities.

### Position
A tenant-specific organizational slot.

### Execution Resource
A planning abstraction.

Concrete resource types:
- Human Resource
- Internal Team
- External Talent
- Vendor/Company
- Managed Team
- Digital Worker / AI Agent
- Automation

Human and digital resources MUST retain separate legal/security/performance semantics.

### Assignment
A bounded commitment of a resource to work.

### Evidence
Observed proof related to skill, work, quality or outcome.

### Outcome
A measurable result of work.

## 3. Relationships
Goal -> requires Capability
Capability -> realized by Process/Work
Work -> requires Skill/Constraint
Resource -> demonstrates Skill/Evidence
Assignment -> binds Resource to Work
Work -> produces Deliverable/Outcome
Outcome -> updates Evidence
Work -> incurs Cost
Project/Service -> produces Revenue

## 4. Work taxonomy
Each work unit may include:
- domain
- category
- type
- recurrence
- complexity dimensions
- criticality
- confidentiality
- collaboration need
- onsite/remote constraint
- tool/system requirement
- expected effort range
- quality/acceptance definition
- review requirement
- legal/compliance requirement
- automation suitability
- AI suitability
- knowledge-retention importance

## 5. Capability architecture
Tenant may define capabilities hierarchically.

Example:
Software Delivery -> Backend / Frontend / QA / DevOps / Architecture.
Marketing -> Positioning / Performance / SEO / Content / Creative.

The hierarchy is tenant-extensible.

## 6. External taxonomies
M0 may evaluate public/standard taxonomies such as ESCO, O*NET or domain taxonomies as seed/reference data.

Core identity MUST NOT depend on an external taxonomy ID. Use mapping tables.

## 7. Skill evidence
Evidence types:
- self claim
- assessment
- project outcome
- task outcome
- code/review
- credential
- manager review
- peer review
- client feedback
- portfolio artifact

Each evidence item records source, time, context, confidence, verifier, visibility and expiry/recency policy.

## 8. Resource matching

Matching is two-stage.

### Stage A: Constraint satisfaction
Eliminate resources violating:
- eligibility
- required skills
- capacity
- location
- security
- engagement type
- minimum compensation
- language
- legal constraint.

### Stage B: Multi-objective optimization
Consider:
- skill/evidence fit
- availability
- total delivery cost
- quality
- reliability
- risk
- collaboration fit
- continuity
- development/growth value
- diversity/fair-opportunity policy
- exploration for new talent.

Do not collapse all information into one opaque universal score.

## 9. Exploration and cold start
New talent has little historical evidence.

Avoid rich-get-richer ranking loops.

Strategies may include:
- assessment-backed confidence
- low-risk starter assignments
- exploration quota
- controlled randomization among similarly qualified candidates
- manager override
- probationary capacity.

Exploration policy is versioned and fairness-tested.

## 10. Digital workers
AI Agents are modeled as Digital Workers with:
- owner
- capabilities
- allowed tools
- permission scope
- autonomy
- model/provider policy
- cost
- budget
- SLO
- quality metrics
- audit
- evaluation suite
- version.

Do not treat an AI Agent as an employee legal entity.

## 11. Human-AI work design
A work package may be decomposed into:
- human-only
- AI-first + human review
- human-first + AI assist
- deterministic automation
- hybrid
- vendor/external.

Workforce Architect compares strategies.

## 12. Work lifecycle
Proposed -> Scoped -> Estimated -> Planned -> Assigned -> In Progress -> Review -> Accepted -> Learned/Closed.

## 13. Knowledge retention
For strategically important work, assignment planning should consider:
- key-person risk
- documentation
- handover
- bus factor
- internal learning
- continuity.

Lowest cost is not always best.

## 14. Versioning
Taxonomy, skill definitions, complexity model and matching policies are versioned.

Historical assignment reasoning remains reproducible.

## 15. Architecture principle
Start relational.

Build read models for graph-like queries.

Introduce a graph database only after demonstrated query/performance need.


## 16. Resource & Supply Graph

V6 retains and expands the Work Graph into a broader Operations Graph.

Resource nodes may represent:
- human
- team
- supplier
- vendor
- physical asset
- equipment
- vehicle
- location
- stock
- provider
- AI agent
- automation.

Supply relationships include:
- owns
- provides
- stocks
- can-deliver
- located-at
- available-in
- certified-for
- compatible-with.

## 17. Transaction & Fulfillment Graph

Connect:
Intent
→ Offer
→ Commitment
→ Order/Assignment
→ Fulfillment
→ Evidence
→ Settlement
→ Outcome.

This enables the same planning architecture to reason over:
- hiring
- projects
- procurement
- physical delivery
- service work
- manufacturing.

## 18. Graph implementation

The word Graph describes the domain relationships.

V1 still starts with PostgreSQL and relational/read-model strategies.

A graph database is introduced only after demonstrated query/performance value.

