# Security, privacy and compliance architecture

Design contract, not an audit certificate. ADR-006/007/012/013/018/028–030. Independent operative detail: `SECRETS_VAULT_CONTRACT.md`, `DATA_CLASSIFICATION_KEY_EGRESS_CONTRACT.md`, `../operations/ASSET_MANAGEMENT_CONTRACT.md`, `../operations/INCIDENT_MANAGEMENT_CONTRACT.md`, and `../ai/MEETING_INTELLIGENCE_CONTRACT.md`.

## Trust boundaries and abuse controls

| Boundary/threat | Prevention | Detection and required proof | Recovery |
|---|---|---|---|
| Internet -> sessions, takeover | privileged MFA mandatory, secure cookie/session rotation, CSRF/CORS, rate limits, OIDC boundary | stolen/revoked session negative tests, auth anomaly metrics | revoke sessions, scoped recovery with audit |
| Tenant A -> tenant B | application authorization, forced RLS, compound FKs, scoped blobs/cache/jobs/search | two-tenant adversarial matrix on every surface | contain, investigate affected records, notify per reviewed obligations |
| Tenant admin -> platform admin | separate roles/admin surface; no implicit support impersonation | elevation denial; explicit time-limited support grant | revoke grant; preserve audit |
| Public upload -> parser | quarantine, type/content/size/decompression limits, malware scan, isolated extraction | zip bomb/polyglot/path traversal fixtures | reject/quarantine and safe user message |
| Webhook -> authoritative state | signature validation, bounded replay window, provider reference and amount check | duplicate, spoof, out-of-order, changed payload | reconciliation, no blind retry |
| Remote app -> core | scoped principal, fresh consent, API only, rate/egress limits | revoked scope, cross-tenant reference, SSRF tests | suspend/revoke without destroying unrelated data |
| Untrusted content -> AI/tool | data/instruction separation, minimized ACL context, typed tools, deterministic gate | prompt injection corpus and exfiltration attempts | cancel tool, safe fallback, incident evidence |
| Untrusted PR -> build credentials | isolated ephemeral runner, no secrets, trusted-base workflow | malicious workflow/artifact tests | quarantine runner/artifact; rotate exposed identity |
| Cloud/AI -> OT | outbound gateway, device identity, protocol allowlist, no control-plane bridge | network segmentation and forbidden command tests | local safe mode, specialist operator |

## Identity and authorization

RBAC supplies baseline roles; contextual policies narrow by tenant/entity/project/object/field/purpose/action. Deny by default. App effective authority = app consent ∩ tenant policy ∩ capability constraints ∩ acting-user scope for delegated operations. Service apps use their own granted scope, never installer identity. OIDC first; SAML/SCIM supported through adapter contracts, provision/deprovision tested before enterprise claim. MFA for tenant owner, finance approval, secrets administration and platform operations. Break-glass is time-limited, reason-bound, independently alerted, post-reviewed, and cannot make cross-tenant access invisible.

## Data classification

PUBLIC_APPROVED: consciously published projection. INTERNAL: routine tenant work. CONFIDENTIAL: contracts, client records, commercially sensitive rates. RESTRICTED: payroll, government IDs, sensitive HR, bank details, security evidence. SECRET: credentials/key material (vault-only; no model processing). Each record/payload links purpose, owner, retention and residency. Derived embeddings, summaries, metrics and traces inherit constraints. Lower classification requires explicit review; a generated summary is not automatically public.

## Privacy lifecycle

Maintain purpose/legal-basis metadata where applicable, controller/processor roles and subprocessor registry. Candidate, employee, network, fairness-audit and support data are separate purposes. No sensitive HR feeding matching; no tone-to-promotion inference. Cross-tenant raw training disabled. Approved aggregated learning needs explicit basis/opt-in, minimum cohort/reidentification analysis and withdrawal handling; no arbitrary claim of anonymity.

Rights requests: authenticate requester -> enumerate source/derived records -> check applicable obligation/hold -> scoped export/correction/restriction/deletion -> verify propagation -> record minimal completion evidence. Inventory includes documents, blobs, indexes, embeddings, caches, read models, model/eval datasets, processor copies and active exports. Expiring export URLs; no open storage link. Legal holds carry authority, scope, reviewer and expiry/review; conflicts go to qualified adjudication, not perpetual retention default.

Deletion tombstones are retained minimally and re-applied before restored service is reopened. Backups have bounded retention and documented deletion handling; restore cannot resurrect withdrawn network profiles or deleted knowledge. Immutable journals preserve required financial facts; avoid embedding unnecessary PII. Audit envelope immutable where required, sensitive payload separate and governed. Crypto-erasure only claimed when key/data architecture proves it, not merely because a delete was attempted.

Meeting recording/import, participant consent and lawful basis, transcript/speaker/source provenance, derivatives and export/retention are capability-specific policy inputs. A local/private transcription route still needs authorized purpose and deletion; an external provider adds processor/region/terms/AI first-use gates. Revoking source access invalidates derivative retrieval and pending draft approvals. Manual notes do not inherit an unauthorized recording grant.

## Secrets and encryption

TLS transport, encrypted persistent volumes/objects/backups and envelope encryption for selected restricted fields. Versioned key IDs, separate key-encryption/data keys, least-privilege decrypt service; key rotation/restore rehearsal. Recovery materials outside primary failure domain, access split where required. Asset record stores only opaque Vault reference; a separately authorized short-lived server capability invokes the secret. No value in general model context/browser/log/export, and dev/test/staging/prod separated. Revocation, expiry and emergency rotation have independent VLT proof. Redaction at ingestion and telemetry sinks; screenshots/traces sanitized. Remote apps normally own their own provider credentials. No promised HSM/customer-managed-key feature without supported implementation evidence; adapter path retained.

## Incident and vulnerability operations

Operational Incident (REQ-WRK-019) and restricted Security Incident (REQ-TRU-014) are separate linked cases. Detect -> triage severity -> contain -> preserve redacted evidence -> assess customer/data impact -> recover -> notify according to current applicable rule -> postmortem/regression. Engineering targets: critical triage within 1h during declared coverage, containment action within 4h; high triage one business day. These are draft operational targets, not contractual or statutory deadlines. Public SLA requires staffing/budget owner approval. Statutory reporting timers derive from approved jurisdiction pack and knowledge timestamp; no universal fixed deadline. Closing a support ticket or operational incident cannot self-close the restricted case.

Vulnerability record: ID/severity/exploitability/affected versions/supply-chain source/owner/remediation/waiver expiry/advisory/customer impact. SBOM and provenance per build; dependency/license/container/IaC scans. No known critical exploitable defect, tenant/permission leak, secret exposure, unreviewed destructive migration or P0/P1 release blocker may pass.

## Compliance controls

Evidence matrix maps requirement/control to source, jurisdiction, owner, test, reviewer, applicability, result and expiry. SOC2/ISO/AI Act/CRA/sector hooks are control architecture, never certification. Regulatory observations are in RESEARCH_REGISTER.md; legal applicability remains unapproved. Employment recommendations require meaningful human review, understandable reasons, accessible alternative, factual correction and appeal. Model confidence cannot remove this floor.

## Security acceptance

Threat tests must include direct API, indirect references, bulk operations, public links, websocket/event delivery, background jobs, exported reports, search counts, RAG snippets, restore and support impersonation. Run with runtime credentials; testing only as a database owner invalidates RLS proof. External specialist review required before initial commercial GA; pending qualified review is a deployment gate, not a claim of security.
