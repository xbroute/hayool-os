# Initial risk register — design baseline

Risks have owner **roles** pending named humans; status is open, not a claim that a control has run. Likelihood/impact are qualitative design triage. Owner approves residual risk only after evidence.

| ID | Risk / impact | Planned control and proof | Owner / trigger |
|---|---|---|---|
| R-01 | Cross-tenant read via derived index, worker or restore; critical | Composite FK/FORCE RLS, ACL on every surface, TEN attack suite | Security/Platform; every release |
| R-02 | Duplicate charge or inconsistent ledger; critical | Durable attempt key, unknown reconciliation, exact balance/property tests | Finance; every finance change |
| R-03 | Unverified jurisdiction/provider used as executable rule; critical | Signed scoped pack, applicability/legal review, fail-closed fixtures | Policy; every activation/source change |
| R-04 | Iran sourcing exposes cross-border candidate; high | Verified context and pre-search eligibility, default domestic-only | Policy/Network; V1.2 |
| R-05 | Employment AI unfair decision/appeal failure; high | Human review, bias eval, candidate recourse, scoped rollout | AI/Compliance; V1.2+ |
| R-06 | Agent escalates privilege or weakens test; critical | Separate trust domain, exact SHA, read-only review, hard gates, kill switch | Security/Engineering; M0.0 |
| R-07 | External model leak/cost overrun; high | AI-off, classification, provider eligibility, atomic budget cap | AI/Finance; V1.5 |
| R-08 | Marketplace app scope creep/supply chain; high | Independent app identity, re-consent, Remote runtime and signing | Platform/Security; V1.7+ |
| R-09 | Retained audit vs erasure/restore; high | Split payload/envelope, tombstones and rights reconciliation | Privacy/Ops; V1.0 |
| R-10 | Overly broad delivery delays viable ICP; high | Outcome gates, internal golden loop, constrained initial ICP | Product; every gate |
| R-11 | Unfunded managed payout/SLA exposure; critical | Liquidity model, no custody, owner funding/terms decision | Finance/Owner; V1.4/1.6 |
| R-12 | Public market/legal claim outruns evidence; high | Claims registry, version/expiry and owner publication gate | Product/Legal; publication |
| R-13 | Source docs treated as code readiness; high | Independent maturity fields and exact-SHA gate | Engineering; M0.2 |
| R-14 | Unverified version/license/vulnerability of chosen dependencies; high | M0.0 pin/SBOM/license/CVE inventory before install | Security/Engineering; M0.0 |
| R-15 | Recovery cannot meet data/retention obligations; high | Compatible restore/upgrade/payment reconciliation/deletion proof | Ops/Privacy; V1.0+ |
| R-16 | Budget committed/actual double counts or mismatches Ledger; critical | BUD exact reconciliation, center version, concurrent threshold tests | Finance; V1.0 |
| R-17 | Incident conflated with ticket/issue/risk or communications leak; high | Separate states/ACL, incident timeline/postmortem, INC/SEC proof | Operations/Security; V1.0+ |
| R-18 | Asset register embeds credentials or misses expiry/owner; critical | Separate AST/VLT, opaque reference, sentinel/renewal test | Security/Operations; V1.0 |
| R-19 | Meeting recorded/processed without applicable consent or AI invents authoritative action; high | Policy-gated capture, AI-off path, source/approval/retention tests | Privacy/Knowledge; V1.0+ |
| R-20 | Brand/market claim or Iran domestic definition outruns evidence; high | Canonical claims/trademark gate, pack-defined facts, no live rank without approved pack | Product/Policy; public use/V1.2 |

Escalate any new P0/P1 product finding to gate blocker with reproducible evidence and responsible reviewer. Score/closure requires executed control, not architectural description. The inherited strategic risk register remains additional detail.
