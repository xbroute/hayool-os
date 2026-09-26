# Hayool OS V7 — Requirements, ADR, Traceability & Evidence Specification

## 1. Purpose

Autonomous engineering cannot be reliable when product truth lives in prose scattered across chat and large strategy documents.

V7 converts vision into executable traceability.

## 2. Required repository structure

Suggested:

`docs/requirements/`
`docs/adr/`
`docs/evidence/`
`docs/releases/`
`docs/policies/`
`docs/country-packs/`
`docs/industry-packs/`

Root:
- `PROJECT_STATE.md`
- `NEXT_ACTIONS.md`.

## 3. Requirement schema

Every material requirement has:

- `REQ-ID`
- title
- status
- owner
- source document
- product outcome
- user/actor
- behavior
- invariants
- jurisdiction applicability
- security/privacy class
- accessibility implications
- AI/algorithm class
- extension/core classification
- acceptance criteria
- negative criteria
- evidence required
- related ADR
- test references
- release target
- dependencies
- open questions.

## 4. ADR schema

Every architecture decision has:
- ADR ID/title
- status
- context
- decision
- alternatives
- rationale
- tradeoffs
- consequences
- security/privacy
- global/jurisdiction impact
- operability
- cost
- exit/migration path
- implementation constraints
- revisit triggers.

## 5. Evidence schema

Evidence artifact:
- Evidence ID
- claim/requirement
- exact SHA/release
- environment
- test/tool/process
- timestamp
- result
- artifact reference
- reviewer
- limitations
- expiry/revalidation condition.

Examples:
- tenant isolation test
- restore rehearsal
- accessibility review
- legal review
- design-partner workflow completion
- pricing interview
- API compatibility test.

## 6. Claims registry

External product claims map to evidence.

A claim expires when:
- supporting policy changes
- provider changes
- jurisdiction law changes
- major platform version changes
- evidence validity period ends.

## 7. Definition of done

Never use a single “done.”

Track separately:
- specified
- designed
- implemented
- unit-tested
- integration-tested
- security-reviewed
- accessibility-reviewed
- staging-verified
- jurisdiction-verified
- market-validated
- production-ready
- production-deployed.

## 8. Project State

`PROJECT_STATE.md` must answer:
- exact default branch/SHA
- current milestone
- current release target
- implemented capability map
- missing critical artifacts
- current blockers
- risk summary
- open owner decisions
- CI/staging state
- autonomy maturity
- last evidence refresh.

## 9. Next Actions

`NEXT_ACTIONS.md` contains executable prioritized work only.

Each action:
- ID
- priority
- outcome
- owner/agent role
- risk
- prerequisite
- expected evidence
- stop condition.

Avoid a giant unranked backlog.

## 10. Traceability graph

Required path:

Vision/Owner Decision
→ REQ
→ ADR if needed
→ Issue/Task
→ Branch
→ Commit/PR
→ Test
→ Evidence
→ Release
→ Outcome.

Autonomous agents must be able to traverse this path in both directions.

## 11. Source-of-Truth conflict rule

Repository precedence remains authoritative.

When two canonical docs conflict:
- record Conflict ID
- identify exact sections
- apply precedence
- if unresolved/high-impact, owner decision
- update affected REQ/ADR
- never silently choose.

## 12. Historical docs

Mark historical docs explicitly.

Agents should not derive current requirements from V4/V5 material where V7/V6 canonical text supersedes it.

## 13. Gate

No material implementation begins until the relevant REQ exists.

No architecture change begins without an ADR.

Emergency security fixes may proceed through a documented emergency path, but traceability is backfilled immediately and independently reviewed.

