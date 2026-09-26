# M0.0 Engineering Bootstrap (Shadow Mode)

Scope: a small, replaceable gate for repository changes. It builds no Hayool product capability. `engrun.py` never writes to GitHub, calls a model, merges, deploys, or reads production credentials. The only workflow has read-only repository permission and runs on a PR head with no secrets. Its artifact binds eight deterministic check results to the PR head SHA.

## Run contract

`engrun.schema.json` describes one `ENG-RUN-*` record. One writer is scoped to a `codex/*` branch and a maximum one-hour lease. At least two other identities produce read-only reports for the same target SHA. The evaluator rejects a stale target or policy SHA, lower-than-computed risk, a missing or failed hard check, a dirty-checkout report, a changed evidence hash, an expired lease, more than three repair iterations, more than 60 minutes elapsed, any paid external cost, an engaged kill switch, or any shadow merge/deployment authority. AI review votes cannot override a deterministic failure.

The checked-in `kill_switch.json` disables autonomous writes, merge, deployment and external calls. M0 has no autonomous dispatcher to re-enable them. The operator can additionally set `engaged=true` to make the gate fail. These checks are a bounded local control, not a production orchestration or identity service.

Risk is the maximum risk of all changed paths. Governance, workflow, security, finance, requirements, ADR and archive changes are R3; production infrastructure changes are R4; unknown paths are R3. `samples/` harmless text is R0. R3/R4 cannot gain automatic merge or deployment through this runner.

## Deterministic checks

`baseline.py` verifies the preserved V7.2 ZIP, package/source manifests, design digest and predecessor archive. It runs the gate unit suite, checks workflow privilege and immutable action references, fails on unreviewed installed dependency manifests, validates the planned version/license inventory, scans tracked non-archive files for selected secret formats, blocks modification/removal of pre-existing tests, and checks PR traceability fields. A clean checkout and matching PR head SHA are required for admissible evidence. The action uploads the JSON result even on failure.

The secret patterns are a baseline, not comprehensive detection. Archived provenance is hash-verified and excluded from model input and the pattern scan. GitHub plan restrictions currently prevent enforcing required checks or independent approval on `main`; the workflow result therefore cannot by itself authorize merge. `docs/engineering/REPOSITORY_REALITY_2026-09-26.md` records that blocker.

## Evidence use

For a real shadow PR: record the base/head SHA and changed paths; run CI; retrieve its JSON artifact; have two read-only reviewers inspect that exact SHA and artifact; save their signed or attributable reports; evaluate the ENG-RUN record against those files; retain the run JSON, report hashes, CI URL, review identity/model disclosure and failure-injection output. New commits invalidate affected checks and reviews. Model/provider identity hidden by the host is recorded as unavailable, never guessed.

`python3 bootstrap/engrun.py RUN.json --root EVIDENCE_DIR --sha EXACT_HEAD_SHA` returns a nonzero exit code on any failure. The JSON schema is descriptive; the stdlib evaluator is the executed gate. All evidence is scoped to the exact SHA rather than to a mutable branch name.
