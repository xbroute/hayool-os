# Engineering Bootstrap live next actions — 2026-09-29 UTC

**M0.0 and M0.2 remain PENDING.** Finish the ADR-034 repair on PR #1: freeze the head with SHA-bound traceability, post-seed M0 change allowlist and external-session review consistency check; verify local pre/post exploit regressions, actual GitHub CI/artifact and two new independent read-only reviews on that exact head. Rebase and rerun harmless Shadow PR #2 and failing injection PR #3, update both evidence ledgers and prepare a non-PASS ENG-RUN candidate. No V1.0 feature or Slack work is authorized.

Then a genuine GitHub collaborator other than PR author `xbroute` must inspect the final SHA, approve and merge PR #1 under current protection. After that human action, read back `main`, activate/read back Actions policy 5892, switch/read back the required strict exact-head trusted status, and run the protected-main Shadow and workflow-spoof attack. Only live passing evidence with no open P0/P1 permits final ENG-RUN and M0.0 PASS. Only after that may M0.2 start. The older queue below is retained as dated history where its ADR/check details differ.

---

# Historical Engineering Bootstrap next actions — 2026-09-28 UTC

Current gate: **M0.0 PENDING; M0.2 PENDING.** The only permitted implementation scope remains Engineering Bootstrap, with no V1.0 product feature. Slack is not an M0.0 dependency.

| Order | Action | Exit condition |
|---|---|---|
| 1 engineering | Freeze PR #1 after ADR-033 repair; run real GitHub candidate CI and restricted-container exploit regressions, rebase Shadow PR #2 and failure-injection PR #3 onto the frozen SHA, verify their actual runs/artifact digests, and obtain two independent read-only reviews on that exact SHA. | P0/P1 findings from new code resolved; exact SHA and evidence in PR ledgers. Candidate CI is advisory until protected main is seeded. |
| 2 manual seed | An actual GitHub collaborator other than `xbroute` reviews and approves PR #1's frozen SHA, then merges under the existing required-review and CI protection. Do not use self-approval, a dummy account or a protection bypass. | GitHub records independent approval and merge of the reviewed SHA. |
| 3 dependent on 2 | Verify main SHA. Activate staged repository Actions policy 5892 (`~ALL` paths; only `pull_request_target`) and read it back. Require `engineering-trusted-gate-status` from GitHub Actions App ID 15368 with strict freshness; read back branch protection. | PR-controlled workflow events are server-blocked and trusted exact-head status is required. The current policy is disabled and does not satisfy this step. |
| 4 dependent on 3 | Retarget/re-run Shadow PR #2 against main. Run a real workflow-spoof attack PR and the kill-switch failure injection under the active policy. Verify the protected-main job, both artifacts, exact SHA status and merge block for the attacks. | Hard failure cannot be overridden by AI votes or a PR-created workflow/check; evidence includes run/attempt/artifact IDs and SHA-256. |
| 5 dependent on 4 | Produce final ENG-RUN only from live exact-SHA API/artifact/status/policy readbacks plus two independent read-only reviewer reports with no open P0/P1. | Strict evaluator returns PASS, then M0.0 may be marked PASS and state/evidence updated. |
| 6 gated | Execute M0.2 independent architecture gate on the exact M0.0 final SHA; close P0/P1, then stop before V1.0. | Real read-only domain reviews and evidence; no product code. |

ADR-033 is the traceable CI architecture update. No original REQ or owner decision changed. A human review/merge is still required for PR #1; activating the server-side policy and proving it on live PRs remain dependent verification work after that merge.

---

# Engineering Bootstrap next actions — 2026-09-26 UTC

The queue below applies to the current repository. The older V7.2 pre-code queue after the divider is historical. The owner authorized only M0.0, followed by M0.2 **after** genuine M0.0 PASS; V1.0 product features remain prohibited.

| Order | Action | Exit condition |
|---|---|---|
| 1 in progress | Freeze the bootstrap repair on a final SHA, run real candidate CI and artifact checks, rerun the failure injection, and obtain two independent read-only AI reviews on that exact SHA. | No open code P0/P1; full run IDs, hashes, actual provider/model identity and severity findings in [PR #1 ledger](https://github.com/xbroute/hayool-os/pull/1#issuecomment-5849944631). A candidate check does not itself attest trusted main policy. |
| 2 in progress | Rebase harmless Shadow PR #2 on the final bootstrap commit and rerun candidate CI, isolation and hard-failure injection. | One-line Shadow diff, exact SHA, real Actions run and artifact, evidence in [Shadow ledger](https://github.com/xbroute/hayool-os/pull/2#issuecomment-5849945980). No merge/deploy. |
| 3 manual seed | An actual independent collaborator with write access reviews and approves final PR #1 SHA, then performs the merge under the existing protected-main rule. `xbroute` authored PR #1 and cannot supply its required approval or satisfy M0 no-self-merge by merging it. | GitHub records non-author approval and merge with no protection bypass. No dummy account or AI review replaces this step. |
| 4 dependent on 3 | After the seed merge, read back `main` SHA; activate and verify server-side protection against changes to `.github/workflows/**` and trusted gate/evaluator files, and require `engineering-trusted-gate-status` only with proof that same-App spoofing is blocked. Retarget Shadow PR #2 to `main`, rerun the default-branch trusted workflow and real spoof attack. | Live trusted run/artifact on exact head and policy SHA; protected-path or independent-App source enforcement read back; attempted spoof cannot merge. A status from the GitHub Actions app alone is insufficient. |
| 5 dependent on 4 | Produce final strict ENG-RUN only after exact-SHA CI, independent reviews, and failure proof. | Evaluator authenticates candidate and trusted GitHub runs, all hard checks, reviewer reports, writer lease, limits and kill switch; P0/P1=0; actual result PASS. Then M0.0 may be accepted. |
| 6 gated | Run M0.2 Independent Architecture Gate only after M0.0 PASS on the final exact SHA, close P0/P1, and stop before V1.0. | Required domains reviewed read-only and evidence indexed; no product feature implementation. |

The earlier billing stop has been resolved in practice for two older candidate runs, but final SHA runs must be observed again. The P1 regressions are implemented locally; the default-branch trust anchor and native anti-spoof enforcement are not yet configured. ADR-032 records this engineering decision. No REQ or owner-decision change is made. Slack is not part of the M0.0 gate and its connection state has no bearing on this queue.

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
