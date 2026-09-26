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

## Manual blocker

The private repository's current GitHub plan blocks branch-protection and ruleset APIs despite admin access. Do not make it public as a workaround. The owner must enable a plan with private-repository protection (or supply an equivalent enforceable policy) and configure PR required, direct/force push denied, required named CI checks, non-self M0 approval and bypass restrictions. Until observed, these controls remain **not configured** and M0.0 cannot pass its protected-repository criterion. All changes remain on isolated branches and PRs; no direct push to `main`.

The above is a scoped GitHub and checkout audit, not proof that no external infrastructure, credentials or environments exist elsewhere.

## Setting changed during bootstrap

After the initial audit, the repository Actions permission API accepted `sha_pinning_required=true`; a fresh GET returned `true`. This enforces full-SHA references for Actions but does not protect `main`, require PRs or provide non-self approval. The Actions token remains read-only.

## Real PR check result

[Bootstrap PR #1](https://github.com/xbroute/hayool-os/pull/1) and [Shadow PR #2](https://github.com/xbroute/hayool-os/pull/2) each produced a failed `engineering-baseline` check. The job annotation says: "The job was not started because recent account payments have failed or your spending limit needs to be increased." No workflow step or artifact ran. This is a GitHub billing/manual blocker, not a test failure or a passing CI run. Fix account billing and rerun the exact current PR heads before treating CI as verified.

Independent read-only reviewers examined bootstrap `0ba42abaabf8fb010d9f66b4292dd44941cc4690` and Shadow `4cafb7bd23aa421f8440145f7bc0a564d6b59d96`. Their P1/P2 findings led to bounded M0.0 gate repairs. The current PR heads must be reviewed again after those changes. The GitHub plan and billing issues remain external blockers.
