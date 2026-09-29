# Engineering Bootstrap live status — 2026-09-29 UTC

**M0.0 = PENDING; M0.2 = PENDING.** The protected default `main` is still the README-only SHA `138bdb78530403bac8407738c05fe033514a7838`; the V7.2 import and bootstrap code remain on PR #1. PR #1 author is `xbroute`, also the Owner account, so it cannot provide the non-author approval. No human reviewer or merge is recorded. No V1.0 product code, deployment or production credential is in scope.

The new ADR-034 supersedes ADR-033 after the read-only security review of PR #1 SHA `8b46f653f7f2b3f51e268571d67a8066668ba01a` found three code/assurance P1s: mutable PR-body traceability at a fixed SHA, candidate-added test/import poisoning, and writer-created AI review reports accepted by ENG-RUN. Disposable regressions reproduced all three before repair: the first two produced four expected failures in the restricted container; the forged-review CLI returned a false PASS. The current branch changes the hard trace to the head commit, freezes executable/test paths for post-seed M0 PRs, and requires byte-for-byte review output from distinct local Codex sessions before ENG-RUN CLI can pass. The new regressions passed locally after repair. Local session logs are unsigned and host-writable, so this is consistency evidence, not a cryptographic reviewer signature. The exact reviewed SHA and live GitHub CI after this repair are maintained in the [PR #1 evidence ledger](https://github.com/xbroute/hayool-os/pull/1#issuecomment-5849944631); earlier results do not prove the repaired head.

GitHub Actions policy `5892` is configured **disabled** for all workflow paths and only `pull_request_target`. Current branch protection requires one non-author approval and strict `engineering-baseline` from GitHub Actions App ID 15368; that check is PR-controlled for the seed. The protected-main gate, its exact-head required status and the real workflow-spoof attack remain unverified until an independent human approves and merges PR #1, after which the policy and required status must be activated and read back. The original V7.2 ZIP, 194 REQs, 31 original ADRs and owner decisions are preserved; ADR-034 is an additive engineering decision, not a product requirement change. Slack is not an M0 dependency.

The [Shadow PR #2 ledger](https://github.com/xbroute/hayool-os/pull/2#issuecomment-5849945980) and draft injection PR #3 record candidate CI and hard-failure evidence on their exact heads. After the new bootstrap SHA is frozen, both must be rebased and rerun. A final ENG-RUN cannot pass without a successful protected-main run, active server policy, exact status, independent reviews and non-author merge. M0.2 and V1.0 remain unstarted.

---

# Historical Engineering Bootstrap status — 2026-09-28 UTC

**M0.0 = PENDING; M0.2 = PENDING.** The current protected `main` remains the README-only SHA `138bdb78530403bac8407738c05fe033514a7838`. PR #1 is authored by GitHub identity `xbroute`; that same account cannot supply the required non-author approval. No human reviewer has been identified, and no M0 merge has occurred. No V1.0 product feature is authorized or implemented.

The bootstrap branch now proposes ADR-033, which supersedes ADR-032 before activation: a default-main `pull_request_target` gate with separate read-only candidate and status-writing jobs. Candidate Python tests run only in the pinned, restricted Docker container. The status job checks out only main and requires exact run/artifact/PR evidence. GitHub repository Actions policy **5892** was created and read back with `~ALL` workflow paths and only `pull_request_target` allowed; its enforcement is **disabled** until the independently approved PR #1 seed merge. The current `main` protection still requires only `engineering-baseline` from GitHub Actions App ID 15368. Therefore the anti-spoof trust boundary is **specified/implemented on an unmerged branch, not configured or live verified**. Activation, required-status readback and a real workflow-spoof PR must follow the seed merge before M0.0 can PASS.

The earlier final-at-the-time PR #1 candidate run `36451227946` on `98241deca25660a500692d06b5106669102f3528` and Shadow PR #2 run `36451342576` on `b7fb307a00421405037f0f276e2483b0000a1100` succeeded with artifacts `10983417148` and `10983013579`, respectively. Those SHAs predate the ADR-033 repair now being prepared; they are real historical evidence, not final-SHA proof. A draft failure-injection PR #3 failed run `36450680179` on `610891268ec918715eec14348ff4b73f463ccbf7`, also before the new architecture. The ENG-RUN evaluator's open-P1 acceptance flaw was reproduced in a restricted container (12 tests, one expected failure) and repaired (15 tests PASS); the final branch CI and fresh exact-SHA independent reviews are still pending. Current ENG-RUN cannot PASS without a live trusted-main run, active event policy, exact-head required status and evidence artifacts. Slack is not part of M0.0.

The V7.2 ZIP/provenance is preserved without REQ or owner-decision edits. The 31 original ADRs remain in the source package; ADR-032 is superseded by new ADR-033. Planned runtime pins remain an inventory, not installed product dependencies. No production credentials, deployment, backup/restore proof or production readiness is claimed.

---

# Engineering Bootstrap repository reality — 2026-09-26 UTC

This addendum supersedes the historical pre-code status below. The original V7.2 ZIP remains byte-for-byte at `archive/V7.2/Hayool-OS-V7.2-Final-Source-of-Truth.zip` (SHA-256 `35054ad417242eda797d81816d81ae10a2bcc44b4a10fcc8784005c7d1d5d700`). Before and after import checks covered 153 safe ZIP entries, 152 package-manifest file hashes, 61 raw sources, the V7.1 predecessor and design review digest. The original requirements, 31 ADRs and owner decisions remain in the preserved package. ADR-032 is a new traceable M0 engineering decision on this branch; no REQ or owner-decision change was made.

| Dimension | Observed status and limit |
|---|---|
| Repository | Public `xbroute/hayool-os`; default `main` remains README-only SHA `138bdb78530403bac8407738c05fe033514a7838`. The verified V7.2 import commit `7f8ecbd986ccb399d736bbb0f55a1345067de911` is on `codex/m0-bootstrap`, not in `main`. |
| Specified | V7.2 has 194 REQs and 31 original ADR records. ADR-032 adds the M0 trusted CI decision, linked to ADR-023/025 and REQ-GOV-004–009. No V1.0 feature is authorized. |
| Implemented | Bootstrap branch contains deterministic checks, ENG-RUN evaluator, a candidate PR workflow, a default-branch `workflow_run` verifier and a container boundary for candidate tests. The trusted workflow is **not installed on `main`**. No Hayool product feature exists. |
| Tested | Earlier candidate CI for PR #1 (`36267802714`) and PR #2 (`36267822272`) succeeded on their earlier SHAs and produced real artifacts. Those runs predate the two-P1 repair and cannot prove the final gate. Disposable regressions reproduced an in-process test poisoning bypass and a PR-controlled workflow/artifact self-attestation bypass; the new isolated runner and trusted verifier reject those fixtures locally. Exact final-SHA CI and independent reviews are recorded separately in the [PR #1 evidence ledger](https://github.com/xbroute/hayool-os/pull/1#issuecomment-5849944631) and [PR #2 Shadow ledger](https://github.com/xbroute/hayool-os/pull/2#issuecomment-5849945980). |
| Configured | GitHub Actions enabled; default token read-only; full SHA pinning enforced. `main` requires PR, one non-author approval, stale dismissal, last-push approval, strict `engineering-baseline` check from GitHub Actions app ID 15368, admin enforcement, no force push/deletion. The required check is still candidate-controlled for the bootstrap PR. A trusted status requirement and server-side gate-path restriction are not active. No repository secret or environment was observed at the initial audit. |
| Verified | Original package integrity and prior candidate run/artifact identity. Local new-boundary regressions. The live default-main trusted workflow, nonforgeable merge enforcement, final ENG-RUN PASS and Shadow PASS remain unverified. |
| Production-ready | No; there is no product build, deployment, staging, production credential, restoration or upgrade proof. |

**M0.1 documentation gate = PASS for its original documentary scope. M0.0 = PENDING; M0.2 = PENDING.** The two P1 code paths have repairs and regressions, but the CI trust boundary is not operational while `main` lacks the trusted workflow and a server-side anti-spoof control. PR #1 author is `xbroute`, the same GitHub identity as Owner; GitHub cannot count self-approval. A genuine different person with write access must review the final SHA and merge without weakening protection. After that seed, revalidate the trusted gate and Shadow PR against `main` before any M0.0 PASS. The current ENG-RUN schema fails closed when a real trusted run is absent. AI votes never override that failure. Shadow Mode keeps autonomous writes, merge, deployment and external calls disabled. Planned product dependency pins are not installed or compatibility-tested. No M0.2 or V1.0 work has begun.

---

# PROJECT_STATE — Hayool OS

Updated 2026-09-26 UTC. Current phase: V7.2 pre-code Source of Truth final; **M0.1 DOCUMENTATION GATE = PASS**. This PASS establishes only documentation/source-trace consistency, not implementation, security assessment, legal applicability or market readiness. No product code written; owner explicitly forbids phase two. V6 and V7 original sources: 61 files inventoried/read with raw originals under `archive/sources/`; complete V7.1 predecessor ZIP retained. Current design authority is V7.2 with explicit conflict ledger. The Master Prompt remains the implementation mission for later authorized phases, not permission to code now.

| Dimension | Observed state | Evidence / limitation |
|---|---|---|
| Source inventory | 61/61 original read/preserved; V7.1 predecessor retained | SOURCE_MANIFEST and PACKAGE_MANIFEST hash verification; final ZIP inventory bound to manifest |
| Specified/designed | V7.2 design baseline, 194 REQs and 31 ADR records (30 active, 1 superseded) | EVID-DOC-003: two independent read-only documentation PASS results on shared design digest; no product assessment |
| Implemented | Not observed in provided materials | Current scratch workspace has no Hayool project Git repo; cannot assert none exists elsewhere |
| Unit/integration/E2E tested | Not observed | Tests are planned contracts, no executed product result |
| Security/accessibility reviewed | Design contracts reviewed for consistency only; product assessment not observed | EVID-DOC-003 is documentation-only; specialist product review later |
| Staging/restore/upgrade verified | Not observed | No connected staging/infrastructure |
| Jurisdiction/provider verified | None in this package | Synthetic matrix only; IR sourcing default is product policy, not legal opinion |
| Market validated | Not observed | No design-partner or paid-cohort evidence supplied |
| Production ready/deployed | Not observed | No release, SLA or launch approval |
| Autonomy | AE0 advisory/document design | No ENG-RUN, shadow PR or merge/deploy authority |

Milestones: **M0.1 DOCUMENTATION GATE = PASS** (pre-code Source of Truth only); **M0.0 = PENDING; M0.2 = PENDING** exact repository SHA review; V1.0–V1.10 pending. The design-first order is explicit C-002, not a false M0.0 pass. No 9.5 score is assigned. No documentation blocker remains for beginning M0.0 after the owner lifts the no-code instruction and identifies/authorizes the target repository and access. Later regulated/payment/provider/commercial decisions are activation holds, not blockers to policy-disabled technical foundation. Risks R-01–20 remain open. Owners are roles until people assigned. Branch/default SHA, dependency lock, migrations, CI, rules, environment, costs and product feature state are unknown.

Next operational steps: `NEXT_ACTIONS.md`. Changes to this state require evidence pointers, reviewer and timestamp. When imported to a real repo, replace these observations with read-only repository audit before any implementation claims.
