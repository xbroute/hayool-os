# Engineering Bootstrap next actions — 2026-09-26 UTC

The earlier queue below is historical V7.2 pre-code guidance. The owner has now authorized only M0.0, then M0.2 after a real M0.0 PASS. No V1.0 feature work is authorized.

| Order | Action | Exit condition |
|---|---|---|
| 1 | Finish M0.0 bootstrap branch and open PR from the verified V7.2 import. | Exact head SHA, green deterministic CI artifact, independent read-only re-review on the final exact SHA, and traceable source/runtime records. |
| 2 | Run a separate harmless Shadow PR and a seeded hard failure. | ENG-RUN bound to exact SHA, two independent read-only reviews, bounded repair if needed, observed PASS/FAIL; no merge/deploy. |
| 3 | Resolve the GitHub private-repository protection blocker. | GitHub plan or equivalent enforceable policy supports PR requirement, direct/force push denial, required named CI, non-self M0 approval and bypass control; verify through API and a real PR. Do not publicize the repository as a workaround. |
| 4 | After M0.0 is genuinely PASS and its bootstrap is merged by an independent authorized reviewer, run M0.2 on the final exact SHA. | All required architecture domains independently reviewed; P0/P1 closed; hard checks green; immutable evidence indexed. |
| 5 | Stop before V1.0 implementation and deliver the Engineering Bootstrap report. | M0.0 and M0.2 evidence-backed results with explicit remaining manual controls and V1.0 entry plan. |

Current manual blockers: GitHub Actions jobs on PR #1 and #2 were not started because GitHub reported account payment/spending-limit trouble; no CI evidence can pass until billing is fixed. `main` is unprotected because branch-protection and rulesets endpoints return HTTP 403 for this private repository on its current plan. M0.0 and M0.2 stay PENDING until actual proof meets their gates. The independent reviewers found that CI policy provenance, live CI authentication, Git-diff risk binding, and secret scanning needed repair; code for those checks was added, but the current exact head still needs new review and executed CI. Reviewer/provider identity attestations and non-self merge remain manual. Candidate versions and licenses are listed in `docs/engineering/DEPENDENCY_VALIDATION.md`; no product dependency is installed. No REQ or ADR change is made here.

---

# NEXT_ACTIONS — priority queue

Updated 2026-09-26. **M0.1 DOCUMENTATION GATE = PASS** for pre-code Source of Truth only, supported by EVID-DOC-003 and final package integrity; it grants no implementation, security, legal or market readiness. **M0.0 = PENDING; M0.2 = PENDING**. Actions 1–2 close the current documentation phase; no product action is authorized by this request.

| Order | Action / owner role | Done when / dependency |
|---|---|
| 1 completed | Documentation reviewers: audit V7.2 194 REQs/31 ADR records, source/138-ID coverage, market, country policy, budget/incident/asset/vault/meeting, release dependencies and all 25 dimensions. | Two independent read-only PASS results on shared design digest, no unresolved blocker; EVID-DOC-003. |
| 2 completed | Package owner: verify 61 raw originals and V7.1 predecessor, regenerate JSON and package hashes, validate ZIP and deliver. | Source/path/link/hash/mirror/ZIP integrity checks and final manifest. |
| 3 later | Owner: decide whether/where to start the separately authorized phase two. | Only after this no-code request; identify/authorize target repo and access. No need to settle later commercial/legal activations now. |
| 4 later | Engineering (later coding phase): inspect supplied repo/default SHA/code/migrations/CI/rules/staging and existing decisions read-only; reconcile imports on branch. | Reality matrix and drift/owner-decision diff linked to SHA. Depends 3. |
| 5 | Engineering/Security: construct minimal M0.0 protected CI/ENG-RUN shadow Autopilot, no paid external provider by default. | Benign PR and seeded blocker traces; exact checks. Depends 4. |
| 6 | Independent reviewers: revalidate M0.1 against imported repo and run M0.2. | Review same exact SHA and close blockers, signed evidence. Depends 5. |
| 7 | Product/Engineering: implement thin V1.0 golden loop with tenant/finance/privacy/AI-off/accessibility and recovery invariants. | Real approved Hayool operation + independent ledger/tenant/restore proof; depends 6. |
| 8 | Product/Owner: recruit design partner and complete V1.1; choose live pack/provider/financial decisions only at the gates in OWNER_DECISIONS. | Independent journey evidence and signed activation policy; depends 7. |

At each action update PROJECT_STATE, REQ/ADR delta, evidence and risk. A failed hard test or unresolved qualified legal review blocks only dependent activation, and must not be declared passed because unrelated work continues. Never write to protected main directly, invent prices/law/provider availability or activate AI/system privileges from draft documents.
