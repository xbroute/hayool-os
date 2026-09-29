# Developer, Studio and Marketplace architecture

ADR-017–020. The platform must support customer-specific depth without Core forks. The four extension levels plus protected Core are configuration -> Studio -> bounded low-code -> Remote App -> first-party Core only when justified by correctness/security/cross-industry need.

## Package and schema

Manifest fields: app_id/publisher/name/version/compatibility range/maximum tested version/type/dependencies/scopes/field and entity grants/protected classes/egress/processor regions/AI providers/events/UI slots/actions/settings schema/migrations/install hooks/uninstall-retention-license-billing-support-security/privacy contact/signature. Immutable package digest and publisher key reference. Dependency resolver rejects cycles, conflicting schema ownership and incompatible versions. Installation is tenant-specific; consent_version independent of package/API version.

Custom fields/objects use validated versioned schemas with tenant/app namespace, typed relations, field ACLs, audit and index quotas. Never redefine ledger/identity/payment truth as a custom blob. Form/report/query builders compile to bounded capability/query plans. Formula AST permits pure arithmetic/date/reference expressions with precision rules, deterministic function allowlist and CPU/row/depth quotas; no network/filesystem/eval/JS/shell. A low-code connector is a typed adapter configuration with egress policy and vault references, not an SSRF tunnel.

Studio lifecycle: describe/manual design -> draft -> schema validation -> preview -> test tenant/simulation -> permission/impact review -> approved publish -> observe -> rollback metadata or forward-repair. AI-generated output has no extra privilege. Protected operations remain domain commands. Permission expansion never silently inherits admin rights. Destructive custom schema change requires export/snapshot/migration plan and approval. Existing valid financial/business facts survive config rollback.

Independent Studio acceptance boundaries are REQ-EXT-002 (schema/records), REQ-EXT-018 (accessible form/view authoring) and REQ-EXT-019 (pure-rule/workflow execution). `STUDIO_BUILDERS_EXECUTION_CONTRACT.md` specifies each owner/test; an expression sandbox test alone cannot establish a usable builder or safe approval workflow.

## API and event contracts

Initial selected description line OpenAPI 3.1.1 (ADR-019); exact tooling pin tested in M0.0. Public API stages experimental/preview/stable/deprecated. Internal methods are not automatically public. Scoped OAuth/OIDC app identity, tenant context, cursor pagination, idempotent writes, expected version, structured errors, correlation and rate-limit headers. Public data shaped by field-level permission and purpose. Consumer replay cursor references a supported retention boundary; expired replay requires snapshot/resync.

Event delivery is at-least-once with schema version, tenant/entity/aggregate sequence/correlation/classification. Signed delivery with key rotation/replay window; subscriber inbox dedup and bounded retry. Public event payload minimizes personal data; reference retrieval checks current scope. Subscription and replay cannot outlive revoked consent. Contract tests compare schema compatibility, real sample apps, generated SDK and migrations.

Engineering default stable deprecation window: at least 180 days and two supported minor releases, whichever longer; an emergency security removal needs risk approval, advisory and migration route. This is a design/support budget assumption, not a published customer/developer contract until ODR-007/ODR-010 approval. App consent changes require reapproval regardless of semver. During pending expansion existing version may run only under existing scopes; no broadened egress or billing.

## Runtime and UI

Declarative package first; Remote App hosted by developer/customer second. Third-party code never enters main API process. Remote apps own processor obligations and external storage declarations. Use approved component schema or isolated-origin sandboxed iframe: strict CSP, explicit frame sandbox, typed postMessage with origin/source checks, no main session cookie/token, short-lived audience-bound capability token, minimal record context. Untrusted hosted runtime remains future until isolated compute/egress/resource/secret controls independently proven.

## Developer experience

Developer portal: API/events/manifest/scopes/tutorials/security/localization/SDK/CLI/simulator/recipes/migration/deprecation/status/support. CLI contract: login, create, dev, lint, test, package, sign, publish, installations, logs. Test tenants synthetic, isolated, resettable, quota-bound, incapable of live payment/email to arbitrary recipients. Local test kit provides contract/permission/tenant fixtures, event replay, UI accessibility harness and example apps. Target time to first working extension <=30 minutes for a competent external developer; measured task evidence, not a promise inferred from docs.

Minimum independent sample scenarios: repair-service Studio package (device/ticket/approval); remote supplier quote app (scoped discovery/offers/webhook); project quality dashboard (read-only events/report). At least one survives platform upgrade, one permission/egress expansion blocked until re-consent, one uninstall exports app-owned data and revokes tokens/subscriptions. Developer GA additionally proves an external developer completes the whole journey without persistent Hayool engineering intervention.

## Lifecycle, economics and trust

Publication: draft -> private test -> submitted -> reviewed -> published -> updated -> deprecated -> retired. Installation: installing -> configured -> active -> upgrade-pending-consent -> suspended -> uninstalling -> removed. Failure leaves explicit resumable state. Uninstall first revokes capabilities/webhooks/jobs, then offers export and defined retention/delete action; never deletes unrelated tenant data. Remote deletion requires processor acknowledgment, otherwise pending/overdue case visible to admin.

Marketplace scans signed package/manifests/dependencies/licenses/secrets/malware, verifies publisher, evaluates minimal scopes/data/egress, contracts/accessibility/performance/install-upgrade-uninstall. High-risk protected-data/country packs require specialist review. Badge has scope/reviewer/date/expiry. Kill/suspend/revoke is independent of uninstall. Abandoned apps get notice/support state/export/migration; transfer/fork only when license permits.

Developer billing (free/one-time/subscription/usage/quote) and Hayool share are configurable; final take rate/payout/merchant role requires owner/legal approval. Reconciliation includes refunds/fees/taxes/payout liability. No privileged marketplace data used to clone successful apps; Core overlap needs rationale, partner transition and IP review. Capability Request Board retains private/public need, budget, acceptance and IP/distribution choice. No public talent underbidding introduced through bounty feature.

Country, industry, themes, workflows, reports, assessment packs, AI agents and connectors share package controls, but regulated publication requires actual jurisdiction evidence. Offline On-Prem signed import includes license, dependencies and revocation/update metadata; stale security state cannot silently grant new privileges.
