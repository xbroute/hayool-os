# M0.0 Engineering Bootstrap (Shadow Mode)

Scope: a small, replaceable gate for repository changes. It builds no Hayool product capability. `engrun.py` never writes to GitHub, calls a model, merges, deploys, or reads production credentials. The only workflow has read-only repository permission and runs on a PR head with no secrets. Its artifact records eight deterministic check results for the PR head SHA. The ENG-RUN CLI separately authenticates the CI run and downloads that artifact.

## Run contract

`engrun.schema.json` describes one `ENG-RUN-*` record. One writer is scoped to a `codex/*` branch and a maximum one-hour lease. At least two other identities produce read-only reports for the same target SHA. The evaluator rejects a stale target or policy SHA, lower-than-computed risk, a missing or failed hard check including real GitHub CI, a dirty-checkout report, a changed evidence hash, an expired lease, more than three repair iterations, more than 60 minutes elapsed, any paid external cost, an engaged kill switch, or any shadow merge/deployment authority. AI review votes cannot override a deterministic failure.

The checked-in `kill_switch.json` disables autonomous writes, merge, deployment and external calls. M0 has no autonomous dispatcher to re-enable them. The operator can additionally set `engaged=true` to make the gate fail. These checks are a bounded local control, not a production orchestration or identity service.

Risk is the maximum risk of all changed paths. Governance, workflow, security, finance, requirements, ADR and archive changes are R3; production infrastructure changes are R4; unknown paths are R3. `samples/` harmless text is R0. R3/R4 cannot gain automatic merge or deployment through this runner.

## Deterministic checks

`baseline.py` verifies the preserved V7.2 ZIP, package/source manifests, design digest and predecessor archive. It runs the gate unit suite, checks workflow privilege and immutable action references, fails on unreviewed installed dependency manifests, validates the planned version/license inventory, scans all tracked files for selected secret formats, blocks modification/removal of pre-existing tests, and checks PR traceability fields. A clean checkout and matching PR head SHA are required for admissible evidence. The action uploads the JSON result even on failure.

The secret patterns are a baseline, not comprehensive detection. Archived provenance is hash-verified and excluded from model input; all tracked archive bytes are included in the pattern scan. The owner changed the repository to public and `main` now requires the named check and an independent approval. These settings and a green workflow result still require exact-SHA evidence and an independent M0 merge operator. `docs/engineering/REPOSITORY_REALITY_2026-09-26.md` records the observed settings.

## Evidence use

For a real shadow PR: record the base/head SHA and changed paths; run CI; retrieve its JSON artifact; have two read-only reviewers inspect that exact SHA and artifact; save their signed or attributable reports; evaluate the ENG-RUN record against those files; retain the run JSON, report hashes, CI URL, review identity/model disclosure and failure-injection output. New commits invalidate affected checks and reviews. The gateway, requested and effective provider/model, and whether the effective identity was verified are recorded. Hidden identity is recorded as unavailable and blocks a PASS rather than being guessed.

`python3 bootstrap/engrun.py RUN.json --root EVIDENCE_DIR --sha EXACT_HEAD_SHA` returns a nonzero exit code on any failure. The JSON schema is descriptive; the stdlib evaluator is the executed gate. The CLI also requires a clean Git checkout whose branch and HEAD equal the record. It compares changed paths to the exact Git diff, checks the actual PR base and head through GitHub, verifies the executed CI steps, and compares the downloaded baseline artifact with local check evidence. All evidence is scoped to the exact SHA rather than to a mutable branch name.

Current GitHub Actions runs on PR #1 and PR #2 did not start due an account payment/spending-limit annotation. ENG-RUN requires a successful real CI proof; local PASS cannot replace it.
