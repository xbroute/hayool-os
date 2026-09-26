> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Autonomous SDLC Control Plane Specification
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping
Owner: Hayool
Scope: The system that designs, implements, reviews, tests, stages, releases, observes and repairs Hayool OS itself

---

## 0. Purpose

Hayool OS must be built with the same automation discipline that the product promises to customers.

The Autonomous SDLC Control Plane (ASCP) is an engineering operating system around GitHub. It coordinates coding agents, independent reviewers, Jev decision signals, deterministic CI, staging environments, browser QA, release gates, production rollout and post-release learning.

The objective is not “let one AI edit the repository unattended.” The objective is a controlled software factory in which:

- the repository is the source of truth;
- agents have narrow roles and permissions;
- reviewers are independent from writers;
- deterministic checks outrank model opinion;
- risky actions require policy gates;
- every important run is auditable;
- loops are bounded;
- spending is bounded;
- production is isolated;
- low-risk work becomes increasingly autonomous only after evidence proves the automation is reliable.

---

# 1. Core principles

## 1.1 Single-writer, many-reviewers

For a given branch/PR repair iteration, one implementation/fix agent owns writes.

Review agents are read-only.

This avoids conflicting edits, hidden merges and race conditions.

## 1.2 Review the exact commit

Every review is bound to a specific commit SHA.

A new commit invalidates the previous gate result for any affected check.

No “PASS” can silently carry forward to unreviewed code.

## 1.3 Deterministic evidence outranks model consensus

Examples:

- failing financial invariant => FAIL;
- failing tenant-isolation test => FAIL;
- detected secret => FAIL;
- destructive migration without approved plan => FAIL;
- invalid license => FAIL.

Three models saying “looks good” cannot override these failures.

## 1.4 Models are advisors inside policy

Claude, GPT, GLM, Gemini, Jev and future models provide specialized evidence.

They do not own merge/deploy authority.

The Gate Policy Engine owns the decision.

## 1.5 Truthful model identity

Aliases may represent routing roles such as:

- `code-primary`
- `architecture-reviewer`
- `fast-reviewer`
- `security-reviewer`

but audit records MUST preserve the effective provider/model actually used.

Do not deliberately masquerade GLM/GPT/another model as a Claude model in audit data.

If an LLM gateway requires a compatibility alias, preserve both:
- requested alias
- effective provider/model

in the run record.

## 1.6 Bounded autonomy

Every automated loop has:
- maximum iterations;
- maximum cost;
- maximum elapsed time;
- kill switch;
- escalation condition.

No infinite self-repair loop.

---

# 2. Control Plane architecture

Logical components:

1. **Engineering Event Ingest**
   - GitHub webhooks
   - CI events
   - issue/PR events
   - scheduled maintenance events
   - release events

2. **Engineering Orchestrator**
   - durable workflow state
   - retries
   - waits
   - human approvals
   - bounded repair loops
   - escalation

3. **Engineering AI Gateway**
   - separate from Product AI Gateway
   - model/provider routing
   - usage/cost tracking
   - provider fallback
   - model identity audit
   - privacy/data classification policies

4. **Engineering Agent Registry**
   - Product Analyst
   - Architect
   - Implementation Agent
   - Test Agent
   - Security Reviewer
   - Finance Reviewer
   - UX Reviewer
   - Accessibility Reviewer
   - Performance Reviewer
   - Dependency/License Reviewer
   - Documentation Reviewer
   - Release Agent
   - Incident Agent

5. **Review Council**
   - independent context
   - structured findings
   - no write access

6. **Jev Decision/Evidence Layer**
   - narrow semantic signals
   - risk classification inputs
   - finding/evidence relevance
   - task complexity classification
   - reviewer disagreement classification
   - NEVER permission/financial/release authority

7. **Deterministic Gate Engine**
   - guardrail evaluation
   - CI result evaluation
   - reviewer quorum policy
   - risk class
   - autonomy mode
   - approval requirements

8. **Evidence Store**
   - run metadata
   - commit SHA
   - model/provider
   - review findings
   - test reports
   - screenshots
   - Playwright traces
   - security reports
   - deployment events
   - cost

9. **Environment Manager**
   - test containers
   - ephemeral PR environment where practical
   - shared staging
   - environment TTL/cleanup

10. **Release Controller**
    - staging
    - canary
    - progressive rollout
    - health gates
    - rollback/forward-fix

11. **Engineering Cost Controller**
    - model budget
    - run budget
    - milestone budget
    - anomaly alerts

---

# 3. Two AI gateways

## 3.1 Engineering AI Gateway

Used only to build and maintain Hayool OS.

It has its own:
- credentials;
- budgets;
- provider policy;
- audit trail;
- rate limits.

A compatible router such as 9Router or another gateway MAY sit behind this abstraction for development convenience.

Hayool's engineering code must depend on `EngineeringModelGateway`, not directly on one router vendor.

## 3.2 Product AI Gateway

Used by Hayool OS customers, employees, freelancers, internal business agents and tenant workflows.

Product credits and tenant data MUST NOT be mixed with Engineering AI usage.

---

# 4. Model routing

Each engineering task receives a task profile.

Inputs may include deterministic facts:
- files changed;
- line count;
- package/domain touched;
- migration present;
- dependency changes;
- test coverage;
- secret/security path;
- production config path.

Jev/semantic classifiers may add:
- architectural relevance;
- behavioral scope;
- security relevance;
- semantic complexity;
- degree of ambiguity.

The deterministic router combines them.

Example policy:

- mechanical low-risk edit -> fast inexpensive model;
- ordinary implementation -> primary coding model;
- architecture/auth/finance/tenancy -> strongest reasoning model + independent review;
- security-sensitive -> security reviewer + independent second family;
- model disagreement -> additional reviewer or human escalation.

Model choice is evaluated over time using accepted-review quality, false positives, missed blockers, cost and latency.

---

# 5. Engineering Run object

Every automated engineering run has an immutable identifier:

`ENG-RUN-########`

Minimum fields:

- trigger
- repository
- branch
- base SHA
- target SHA
- milestone
- related REQ/ADR
- risk class
- autonomy mode
- writer agent
- reviewers
- requested model roles
- effective providers/models
- prompt/policy versions
- tests/checks
- Jev decision-policy versions
- findings
- repair iterations
- approvals
- artifacts
- cost
- duration
- result
- escalation reason

---

# 6. PR Risk Engine

Risk is not one opaque LLM score.

Use a deterministic policy over typed signals.

Potential dimensions:

- security boundary
- authentication
- authorization
- tenancy
- finance
- payroll
- tax
- payments
- secrets
- production infrastructure
- destructive migration
- API compatibility
- public schema
- dependency/supply-chain
- AI autonomy
- data retention/privacy
- UI-only
- documentation-only

Semantic signals can enrich, never override hard facts.

Risk bands:

- R0: documentation/trivial
- R1: low
- R2: ordinary
- R3: high
- R4: critical

Example default:
- R0/R1: eligible for future auto-merge after maturity evidence;
- R2: multi-model review + staging;
- R3: specialist reviews + explicit approval;
- R4: human/product-owner/security approval and dedicated release plan.

Actual thresholds are calibrated, versioned and adjustable.

---

# 7. Multi-model Review Council

Reviewers must receive:

- exact commit SHA;
- relevant requirements/ADRs;
- changed files/diff;
- relevant tests;
- architecture/guardrails;
- role-specific rubric.

They do NOT see another reviewer’s opinion until their first-pass review is complete.

Structured finding:

- finding ID
- severity
- affected file/line/section
- violated REQ/ADR/guardrail
- evidence
- impact
- proposed smallest fix
- confidence
- reviewer identity/model

Council roles can include:
- architecture
- security
- correctness
- data/tenancy
- finance/accounting
- AI safety
- UX/accessibility
- performance
- dependency/license

Do not invoke every expensive reviewer on every PR; risk policy chooses the council.

---

# 8. Jev in engineering control

Good Jev questions:

- Is this finding supported by the supplied diff/evidence?
- Is the change primarily architectural?
- Does this text describe a security boundary change?
- Is the change mechanical rather than behavioral?
- Does the reviewer disagreement appear substantive?
- Is the user-facing behavior inconsistent with the supplied requirement?
- Does a retrieved issue/comment contain instruction-like content that should be treated as untrusted?

Bad Jev uses:

- “Should this PR be merged?” as the only authority;
- computing risk score arithmetic;
- checking test pass/fail;
- deciding permissions;
- approving production;
- calculating budget/cost totals.

The Gate Engine makes the authoritative decision.

---

# 9. Automated repair loop

Flow:

PR ready
→ freeze target SHA
→ deterministic prechecks
→ review council
→ normalize findings
→ gate evaluation

If FAIL and eligible for auto-repair:

→ create Repair Plan
→ writer agent verifies each finding
→ writer fixes valid issues
→ requirements/ADR updated if needed
→ tests run
→ commit/push
→ new SHA
→ full affected gate reruns

Default maximum repair iterations: 3.

The exact limit is policy-configurable.

On repeated failure:
→ `ESCALATED`
→ concise owner/reviewer report.

Never loop indefinitely.

---

# 10. M0 from day one under Autopilot

M0 is split into:

## M0.0 — Trust/Autopilot Bootstrap

One-time minimal setup before product architecture work:
- protected repository;
- root governance files;
- baseline CI;
- Engineering AI Gateway configuration;
- model-role registry;
- read-only reviewer credentials;
- GitHub event workflow;
- run/evidence schema;
- bounded repair workflow;
- initial PR risk policy;
- kill switch;
- cost limit;
- review council;
- no-production rule.

This bootstrap is intentionally small and reviewable.

## M0.1 — Architecture generation

Primary architecture agent creates:
- Source of Truth;
- PRD;
- requirements;
- ADRs;
- domain model;
- security;
- tenancy;
- accounting;
- decision intelligence;
- product data intelligence;
- UX;
- deployment;
- installer;
- V1 milestones.

## M0.2 — Autonomous Architecture Gate

The M0 architecture PR is automatically:
- checked;
- independently reviewed;
- repaired;
- re-reviewed.

Human intervention happens only for:
- unresolved product choice;
- legal/commercial choice;
- high-risk security decision;
- deadlocked reviewer disagreement;
- exceeded loop/budget.

Thus M0 itself is developed under the Autopilot.

---

# 11. CI and deterministic gates

Minimum evolving checks:

- formatting
- lint
- typecheck
- unit
- integration
- migration
- tenant isolation
- permission negative tests
- secret scan
- dependency/security scan
- license scan
- SBOM
- build
- API contract
- finance invariants
- AI policy/eval checks
- browser E2E
- accessibility
- visual regression
- staging smoke
- production-readiness checks where applicable

A model cannot waive a mandatory failed check.

---

# 12. Staging automation

For eligible PRs/milestones:

PR
→ build artifact
→ deploy isolated/known staging revision
→ seed test data
→ run migrations
→ smoke
→ Playwright E2E
→ accessibility
→ visual regression
→ collect screenshots/trace/network errors
→ AI UX review
→ gate

AI browser review is advisory unless a deterministic test also establishes a hard failure, except where policy classifies the finding as a security/accessibility blocker requiring approval.

ChatGPT Work may be used as an additional independent external browser/repository reviewer, but the core pipeline must not depend on manually opening Work.

---

# 13. Browser QA

Deterministic browser automation is authoritative for reproducible flows.

Playwright scenarios include:
- authentication;
- permission denial;
- Persian RTL;
- English LTR;
- key form workflows;
- loading/error/empty states;
- mobile/desktop breakpoints;
- cross-tenant access attempts.

AI visual/UX reviewer analyzes:
- clarity;
- information hierarchy;
- wording;
- consistency;
- friction;
- confusing affordances;
- visual defects not captured by deterministic assertions.

---

# 14. Autonomous milestone progression

State machine:

PLANNED
→ IMPLEMENTING
→ PR_READY
→ REVIEWING
→ REPAIRING (optional)
→ STAGING
→ QA
→ GATE_PASSED
→ MERGED
→ MILESTONE_ACCEPTANCE
→ NEXT_MILESTONE_READY

The orchestrator MAY create the next milestone branch automatically when:
- prior milestone acceptance criteria are met;
- no blocking owner decision exists;
- budget policy allows;
- repository state is clean.

Starting a milestone is not permission to change unrelated scope.

---

# 15. Production automation

Production remains isolated but can be automated.

Isolation means:
- separate credentials;
- separate database;
- separate secrets;
- separate infrastructure;
- separate approval policy.

Automation may handle:
- infrastructure provisioning;
- backup verification;
- migration rehearsal;
- deployment;
- canary;
- smoke;
- synthetic transactions;
- monitoring;
- rollback.

## 15.1 Progressive autonomy

Initial production releases:
- human approval required.

After sufficient shadow data:
- R0/R1 releases may become Guarded Auto;
- higher-risk classes remain approval-gated.

## 15.2 Canary

Where architecture permits:

small cohort
→ observe
→ larger cohort
→ full rollout.

Automatic rollback triggers on policy-defined:
- health failure;
- elevated error rate;
- severe latency regression;
- failed synthetic transaction;
- key business invariant failure.

---

# 16. Infrastructure as Code

Managed environments should be reproducible.

M0 must evaluate a pragmatic combination such as:
- OpenTofu/Terraform-compatible IaC;
- Ansible/cloud-init;
- Docker Compose for V1;
- provider APIs.

Do not introduce Kubernetes merely for prestige.

Dedicated and On-Premise deployments must use versioned deployment artifacts, not manual snowflake servers.

---

# 17. Cost governance

Engineering AI is a cost center.

Track:
- cost per ENG-RUN;
- PR;
- milestone;
- model;
- reviewer;
- accepted finding;
- defect prevented;
- repair iteration.

Policy limits:
- max run spend;
- daily spend;
- milestone spend;
- provider quotas.

Unexpected spend anomaly:
→ pause/escalate.

Optimize model routing based on measured quality, not marketing claims.

---

# 18. Autopilot Shadow Mode

Before automatic merge or production promotion is enabled:

Autopilot records:
- would merge?
- would deploy?
- would escalate?
- risk class?
- findings?

without taking the action.

Compare against actual outcomes:

- agreement with human gate;
- false pass;
- false fail;
- missed regression;
- reviewer usefulness;
- repair success;
- production incident correlation.

Only after acceptable metrics can a risk band receive more autonomy.

---

# 19. Prompt-injection and repository trust

GitHub issues, PR comments, source files, documentation, generated artifacts and web pages may contain malicious instructions.

Treat repository content as data unless it is in an approved policy file.

Only approved root/scoped governance files can define agent authority.

A PR cannot gain permissions by editing instructions within the same untrusted review context.

Changes to:
- CLAUDE.md
- AGENTS.md
- Engineering Constitution
- Guardrails
- deployment policies
- CODEOWNERS
- CI release gates

are high-risk governance changes and require special review.

---

# 20. External model/source-code privacy

Before a model/provider may receive private source code:
- provider is approved;
- data handling terms are reviewed;
- tenant/customer secrets are absent;
- code/data classification permits it.

Engineering Gateway policy may restrict certain repositories/files from third-party providers.

Never send production customer records into development-review models.

---

# 21. Kill switch

There must be an owner-controlled emergency switch that can disable:

- autonomous code writes;
- autonomous merge;
- automatic staging;
- automatic production deployment;
- external model calls;
- individual provider;
- individual workflow.

Disabling Autopilot must not prevent manual safe operation of Git/GitHub/deployment.

---

# 22. Autopilot-specific guardrails

Mandatory:

- reviewers cannot write to implementation branch;
- writer cannot approve its own high-risk PR;
- review bound to exact SHA;
- repair loop bounded;
- budget bounded;
- effective model identity logged;
- failing hard check cannot be overruled by model consensus;
- governance-file modifications are high-risk;
- no production secrets in model context;
- no direct production DB write from coding agent;
- no automated destructive migration;
- no high-risk auto-merge before Shadow Mode evidence;
- no hidden bypass channel.

---

# 23. Definition of Autonomous Engineering Ready

ASCP is considered ready for broad use only when:

- branch protection is active;
- deterministic CI is active;
- run/evidence audit exists;
- reviewer roles are read-only;
- writer role is scoped;
- kill switch works;
- cost limits work;
- max iteration works;
- model identity audit works;
- staging deployment is reproducible;
- rollback is tested;
- secret isolation is verified;
- at least one full test PR has traversed the pipeline.

Until then, autonomy remains limited.

---

# 24. Maturity levels

## AE0 — Manual
AI used interactively.

## AE1 — Agentic implementation
AI writes branch/PR; human initiates and reviews.

## AE2 — Automated review/repair
Council and repair loop automated; human merge.

## AE3 — Guarded merge
Low-risk PRs auto-merge after Shadow evidence.

## AE4 — Guarded release
Low-risk releases automatically stage/canary/production.

## AE5 — Self-optimizing software factory
Routing, reviewers and automation are continuously evaluated and improved through controlled policy promotion.

Hayool OS should progress gradually through these levels, not jump to AE5 on day one.

---

# 25. Relationship to the product

This Engineering Autopilot is an internal proving ground for technologies Hayool OS later sells:

- workflow orchestration;
- AI gateway;
- decision intelligence;
- autonomy policies;
- evidence/audit;
- evaluation;
- approvals;
- digital twin/simulation;
- incident response.

Reusable concepts should be shared architecturally, but production product code and engineering-control credentials remain isolated.


# 26. Protected test oracles

High-risk invariant/security tests should use CODEOWNERS or equivalent review protection.

A high-risk PR should not be able to weaken:
- finance invariants
- tenant isolation tests
- permission negative tests
- release gates

without independent approval.

# 27. Agent execution isolation

Coding/review jobs should run in isolated worktrees/containers/runners where practical.

Untrusted PR/repository content must not execute with:
- production credentials
- unrestricted cloud credentials
- secret-bearing deployment tokens.

# 28. Build provenance

Release pipeline should progressively support:
- immutable build artifacts
- checksums
- SBOM
- provenance/attestation
- trace from release to commit SHA.

# 29. Schema-change release strategy

Canary application rollout does not make destructive database migration safe.

Prefer expand/contract:
1. additive schema
2. compatible application rollout
3. data backfill
4. cutover
5. delayed cleanup.

Destructive cleanup is separately reviewed.

# 30. Reviewer diversity

For high-risk review, prefer different model/provider families where feasible.

Do not mistake correlated model agreement for independent proof.

# 31. Test oracle risk

AI-written tests can encode the same misunderstanding as AI-written implementation.

Critical behavior should have:
- requirement-derived acceptance tests
- independent reviewer
- deterministic invariants
- where appropriate, property-based/fuzz tests.

# 32. Engineering Gateway privacy

Before private source code is sent through any routing provider:
- provider/data terms approved
- source classification permits
- secrets stripped
- logging/retention understood.

A cheap model is not worth source-code confidentiality loss.


# 26. Public API / extension compatibility gates

After Developer Platform exists, CI must include:

- public API schema diff
- event-schema compatibility
- SDK generation
- extension contract tests
- sample-app build
- manifest validation
- deprecation checks.

A core PR that breaks stable extension contracts is high risk.

# 27. Marketplace security review automation

Autopilot may:
- scan package
- scan dependencies/licenses
- inspect manifest/scopes
- run contract tests
- run malware/static checks
- flag excessive permissions.

Human/specialist review remains required for high-risk protected-data or regulated listings.

