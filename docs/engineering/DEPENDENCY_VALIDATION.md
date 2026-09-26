# Planned dependency and runtime validation — 2026-09-26 UTC

ADR-005 calls for a TypeScript modular monolith with Next.js, NestJS, PostgreSQL, Valkey, Temporal behind `WorkflowPort`, S3-compatible storage behind a port, and OpenTelemetry. The exact candidate versions and upstream license references are in [`bootstrap/dependency_baseline.json`](../../bootstrap/dependency_baseline.json). Every row is `planned` and `installed=false`. This is a pin for the first implementation review, not a lockfile, compatibility test, deployment, or license clearance of transitive packages.

| Surface | Candidate pin | Current-source observation and selection reason |
|---|---:|---|
| Node.js | 24.21.0 LTS | [Official v24.21.0 release](https://nodejs.org/en/blog/release/v24.21.0); Node also has a newer Current line, so the LTS line is the candidate. Its distribution includes separately licensed bundled components. |
| TypeScript | 6.0.3 | [Official 6.0.3 release](https://github.com/microsoft/TypeScript/releases/tag/v6.0.3); [7.0.2 is current latest](https://github.com/microsoft/TypeScript/releases/tag/v7.0.2), but compiler/framework compatibility has not been tested. Hold 7.x adoption for an isolated build and ADR review if needed. |
| pnpm | 12.6.0 | [Official release](https://github.com/pnpm/pnpm/releases/tag/v12.6.0); no package has been installed. |
| Next.js | 16.3.6 | [Official release](https://github.com/vercel/next.js/releases/tag/v16.3.6), including the [September security fix](https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j). |
| NestJS | 12.1.0 | [Official release](https://github.com/nestjs/nest/releases/tag/v12.1.0). |
| PostgreSQL | 18.6 | [Official release notes](https://www.postgresql.org/docs/release/18.6/); PostgreSQL 19 was beta at this audit, so it is not selected. |
| Valkey | 9.1.2 | [Official release](https://github.com/valkey-io/valkey/releases/tag/9.1.2). |
| Temporal Server | 1.32.0 | [Official release](https://github.com/temporalio/temporal/releases/tag/v1.32.0); `WorkflowPort` remains the ADR boundary. |
| Object storage | ObjectStorePort 1.0.0 | Internal planned interface; no S3 vendor, SDK, service or provider terms selected. This is a contract version, not a claim of external compatibility. |
| OpenTelemetry Collector | 0.161.0 | [Official release](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.161.0). |
| Docker Engine | 29.8.1 | [Official engine release notes](https://docs.docker.com/engine/release-notes/29/); Docker Desktop terms are outside this pin. |
| Ubuntu Server | 26.04.1 LTS | [Official point release notes](https://documentation.ubuntu.com/release-notes/26.04/1/). Ubuntu is an aggregate with per-package licenses and [Canonical IP terms](https://ubuntu.com/legal/intellectual-property-policy). |
| Future tooling | Ruff 0.16.9, ESLint 10.11.0, Vitest 5.0.2, Playwright 1.63.0, OSV-Scanner 2.6.0, Gitleaks 8.30.1 | Official release/license links and exact candidate pins are in the JSON inventory. None is installed or executed in M0. |

## M0 reality and follow-up

M0 executes only Python standard-library tests and checks on GitHub's `ubuntu-24.04` runner, with `actions/checkout` and `actions/upload-artifact` pinned to full upstream commit SHAs. The hosted runner image and Python patch version are not immutable. The CI report is tied to a commit SHA but must record the observed environment before a reproducibility claim. There is no application dependency lock, SBOM or vulnerability scan of installed product packages because none exists. The baseline fails if an unreviewed package manifest appears. Dependabot is configured to propose GitHub Actions updates only; it does not authorize merge.

Before V1 implementation: install the chosen versions in an isolated branch, capture exact package/image digests and transitive SBOM/licenses, run a current vulnerability scan and integration compatibility tests, and update ADR-005 if a component or boundary changes. Mixed Node/Ubuntu license sets and any object-storage provider contract need review at selection time. The M0 license check validates the planned inventory format and known top-level identifiers; it is not a legal opinion.

No REQ or architecture ADR is changed by recording these candidate pins.
