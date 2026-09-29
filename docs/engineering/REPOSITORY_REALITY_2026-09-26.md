# Repository reality audit — 2026-09-26 UTC

This is an observation of `https://github.com/xbroute/hayool-os` before M0.0 implementation. It does not assert that planned controls are configured.

| Surface | Observed evidence |
|---|---|
| Repository | Private `xbroute/hayool-os`; default branch `main`; admin access for authenticated `xbroute`. GitHub repository API and local clone agree. |
| Initial exact SHA | `138bdb78530403bac8407738c05fe033514a7838` (`Initial commit`). |
| Existing tree | One `README.md` containing `# hayool-os`; no product code, tests, manifests or workflows observed at the initial SHA. |
| Branch protection | `main.protected=false`; required checks empty. Branch-protection GET and rulesets GET each returned HTTP 403: “Upgrade to GitHub Pro or make this repository public to enable this feature.” Neither protection nor ruleset is configured or claimed. |
| Permissions | Authenticated user has admin, maintain, push, pull and triage flags. GitHub Actions is enabled. Default workflow token is read-only; Actions cannot approve PR reviews. Repository `allowed_actions=all` and `sha_pinning_required=false`. |
| Actions | Zero existing workflows. No CI result was available at the initial SHA. |
| Secret metadata | Actions, Dependabot and Codespaces secret listings each reported zero. Values were not requested. Repository secret-scanning service status was not observable from these listings. |
| GitHub environments | Zero configured environments. No staging or production deployment target was observed. |
| Merge settings | Auto-merge disabled. Delete-branch-on-merge disabled. No independent human reviewer identity was observed. |
| Local checkout | Isolated checkout under `hayool-os-workspace`, branch `codex/m0-bootstrap`, created from the exact initial SHA. The ChatGPT project mirror is not the destination repository. |

## Visibility and protection change

At the initial private-repository audit, branch-protection and ruleset APIs returned plan-level HTTP 403. The owner subsequently made this repository public. A fresh API read returned `visibility=public` and `main.protected=true`. The protection API now shows required pull request with one approval, stale review dismissal and last-push approval, strict `engineering-baseline` check tied to GitHub Actions app ID 15368, admin enforcement, no force push and no deletion. These controls are configured; they do not ensure an independent person clicks merge after approval. All changes remain on isolated branches and PRs; no direct push to `main`.

The above is a scoped GitHub and checkout audit, not proof that no external infrastructure, credentials or environments exist elsewhere.

## Setting changed during bootstrap

After the initial audit, the repository Actions permission API accepted `sha_pinning_required=true`; a fresh GET returned `true`. This enforces full-SHA references for Actions but does not protect `main`, require PRs or provide non-self approval. The Actions token remains read-only.

## Real PR check result and bootstrap limit

Initial Actions jobs on [bootstrap PR #1](https://github.com/xbroute/hayool-os/pull/1) and [Shadow PR #2](https://github.com/xbroute/hayool-os/pull/2) did not start because GitHub annotated account payment/spending-limit trouble. Later exact-head reruns succeeded: bootstrap run `36267802714` on `e5cf65c0e7e85e7383a6b5b3e5075078801649d4`, artifact `10914339627`; Shadow run `36267822272` on `eda3c9158904d368cbd5dfb44f303d671fb59fe0`, artifact `10913803842`. These runs precede the new two-P1 repair and cannot attest its final SHA or trusted design.

Independent read-only reviews of those earlier SHAs identified that PR #1 can edit its own `pull_request` workflow and that PR test discovery shares trusted Python process state. ADR-032 and `TRUSTED_CI_ARCHITECTURE.md` document the correction and initial trust-anchor limit: protected `main` still contains only README, so its `workflow_run` verifier has not executed. The existing required `engineering-baseline` context remains a candidate check, and an Actions-app commit status alone is not an unforgeable workflow source. Real final-head CI and two exact-SHA reviews must be observed separately. PR #1 author `xbroute` cannot satisfy the required non-author GitHub approval; an independent collaborator is not yet identified. The original initial-audit table above is retained as dated history, not current configuration.
