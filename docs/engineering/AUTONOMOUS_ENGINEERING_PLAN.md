# Autonomous development, debugging and updates

ADR-002/023/024. Current maturity AE0, documentation only. No autonomous run/CI/merge/deployment is claimed. Minimum bootstrap uses repository workflows and bounded jobs, not a new distributed platform.

## Policy and authority

Trusted policy is read from approved base revision outside untrusted PR changes. A PR cannot grant itself privileges by editing AGENTS, CODEOWNERS, tests or workflow. Risk=max(deterministic path/data/behavior signals); governance docs are high-risk, not R0 merely because Markdown. R0 ordinary docs; R1 isolated low-impact; R2 ordinary behavior; R3 auth/tenancy/money/payroll/tax/secrets/privacy/public API/governance; R4 production destructive changes/money movement/authority expansion. Unknown risk escalates, never defaults low.

| Role | Rights | Explicit denial |
|---|---|---|
| Planner | read approved SOT, propose scoped task | production/code write |
| Writer | leased branch/worktree only | protected main, own high-risk approval |
| Reviewer | immutable diff/tests/evidence read | branch write, credential access |
| Test runner | isolated fixtures, bounded egress | live customer data, prod tokens |
| Evidence uploader | append run namespace | artifact replacement outside namespace |
| Gate engine | inspect required checks and approvals | waive blocker by model vote |
| Release identity | approved immutable artifact deployment | interactive arbitrary DB writes |

Writer lease includes branch/run/fencing token/expiry; stale writer cannot commit through orchestrator. Reviews isolated first pass; model-family diversity preferred, unavailable diversity disclosed. Requested alias/provider/effective model logged exactly; never invent identity hidden by gateway. A review is bound to target SHA, artifact digest, base policy, test-oracle version and context. New SHA invalidates affected approvals; no review reuse by prose similarity.

## Run schema and bounded execution

ENG-RUN identifier, trigger/event dedup key, repository/base/target SHA, branch, milestone, REQ/ADR/task, risk, approved policy, writer lease, reviewer identities, requested/effective models, prompt/data classification, checks/results, findings, repair count, approvals, artifact hashes, spend reservations/actuals, elapsed time, kill switch state, result/escalation.

Working engineering defaults: max 3 repair iterations, 60min wall clock per scoped run, max 10min provider request plus cancellation/polling by policy, one writer. Paid external API cap = 0 until owner supplies budget; this restricts future external API spending, not current authorized document work. Owner sets per-run/day/milestone absolute caps; reserving expected maximum cost occurs before concurrent calls. Missing reliable price/usage or unverified provider => pause that route. No retry can exceed parent budget. An incident does not grant unlimited spending.

## Delivery machine

PLANNED -> READY (REQ/test/oracle/dependencies) -> LEASED -> IMPLEMENTING -> PR_READY -> SHA_FROZEN -> DETERMINISTIC_CHECKS -> INDEPENDENT_REVIEW -> REPAIR or STAGING -> QA -> GATE_PASSED -> APPROVED_MERGE -> MILESTONE_ACCEPTANCE. Escalated/cancelled/failed are explicit terminal or resumable states. Merge uses normal repository protection. M0 cannot self-merge. Initial production always human-approved. Policy-denied action remains denied even with unanimous model agreement.

Checks: trace/format/lint/type/unit/integration, finance and tenancy invariants, negative permissions, schema/migrations, secrets/dependencies/licenses/SBOM, public API/event compatibility, build/provenance, AI eval/policy, browser RTL/LTR/accessibility, staging smoke, restore/upgrade when affected. Required actual check names registered after first real run; never mark a missing job 'not applicable' silently. Protected oracle edits require independent rationale against approved requirements.

Untrusted fork/PR runs without secrets, deploy tokens or write credentials; do not execute untrusted checkout in a privileged event context. Pin external actions/dependencies, verify artifact origin/digest, sanitize logs and uploaded reports. Runner cleanup and egress policy part of proof. Models get minimal source, no production records/keys; provider processing must be approved.

## Debug protocol

Collect redacted deterministic evidence -> reproduce at recorded environment/SHA/input -> minimize case -> classify risk -> independent requirement-derived regression oracle -> root-cause hypothesis -> smallest repair -> affected hard suite -> exact-SHA independent review -> staging replay -> normal release gate. If environment/flaky oracle is suspected, demonstrate with independent reproduction; never delete/skip/assert less solely to pass. Stop after bounded attempts with precise hypothesis/evidence/remaining ambiguity. Production incident recovery and code repair are separate tracks; preserve evidence and use approved rollback/forward-fix.

## Update candidates

Watchers (future implementation, not scheduled in this phase): daily dependency/CVE/base image advisories; weekly provider/model/API/price/terms changes; country sources by qualified owner's risk schedule plus urgent notices; per-release extension compatibility. Polling frequency itself is configuration. Each observation has source/date/hash/diff/affected REQ/provider/policy and creates candidate issue/PR. It never activates legal/finance/security/AI-autonomy changes. License/data terms change can disable affected routing under approved safety policy pending review.

Candidate -> impact -> REQ/ADR delta -> compatibility/eval/regression -> specialist/qualified review -> isolated staging -> approval -> rollout -> monitor. Dependency updates are not blindly all-at-once. Legal rollback cannot revive invalid law; freeze/forward-fix if no legally valid previous version. Model version change invalidates calibration evidence. Provider fallback must pass jurisdiction/privacy/budget rules anew.

## Autonomy maturity

AE0 advisory; AE1 branch/PR writer with human merge; AE2 automated independent review/repair with human merge; AE3 guarded R0/R1 merge; AE4 low-risk release; AE5 controlled routing-policy optimization. No level inferred from documentation.

Promotion test plan: M0.0 exercises full benign PR plus seeded tenant leak, test weakening, secret exposure, spoofed model, cap exhaustion, stale SHA, stale writer, injection and kill-switch cases. Every injected blocker must stop. For candidate AE3 require at least 30 consecutive low-risk shadow PR decisions over >=14 days, zero observed blocker false-pass, reviewed disagreements, successful rollback and explicit owner/security authorization. Sample size is a minimum engineering screen, not statistical proof of safety. R3/R4 remain approval-gated. AE4 additionally requires measured staging/canary/recovery drills and agreed SLOs; AE5 policy changes follow same offline/shadow/limited review cycle.

Kill switch separately stops writes/merge/staging/prod/external calls/provider/workflow; revokes leases and cancels pending dispatch; safe in-flight financial work reconciles rather than being assumed cancelled. Manual safe repository/recovery access remains. Re-enable requires authorized acknowledgment and stale approval revalidation.
