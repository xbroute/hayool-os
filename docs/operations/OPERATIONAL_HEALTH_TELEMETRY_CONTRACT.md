# Operational health and telemetry — V1.0 domain contract

Status: specified design only. Owner: Operations/Recovery module. ADR-005/009; REQ-PLAT-018 and independent TEST-REQ-PLAT-018. The operational signal is diagnostic evidence, never a replacement for financial journal, approval or immutable audit records.

## Signals and lifecycle

Service and dependency health distinguish liveness from readiness and partial degradation. Structured events, metrics and traces carry correlation ID, service/workflow/provider operation, deployment/tenant scope where authorized, timestamp, build/config/policy version and redacted cause. Cover API, queue/workflow lag, dead letters, storage, backup age and restore status, payment reconciliation uncertainty, provider eligibility/health and incident links. Define signal owner, thresholds, routing, acknowledgement, resolution and retention per deployment policy; customer-visible incident communication remains governed by the separate Incident contract. A healthy API process with failed financial reconciliation is degraded, not green. Sampling must not erase consequential failures.

At collection, storage, alert and diagnostic export boundaries, remove credentials, secret values, meeting media, raw payment data and unauthorized tenant/personal fields. Tenant-specific traces require scoped access; cross-tenant infrastructure operators may see aggregate diagnostics without identifiable customer data. Debug logs do not authorize secret retrieval or convert an unposted event into ledger actual. Cloud/Dedicated telemetry egress requires provider/purpose/region approval; On-Prem opt-out of external telemetry retains local health, troubleshooting and owner-controlled export. Alert storm and receiver failure must be visible; diagnostics must tolerate dependency outage and bounded storage without compromising the business transaction.

## Independent acceptance

| Test | Given / action | Pass oracle |
|---|---|---|
| TEST-REQ-PLAT-018 | Inject API readiness loss, queue delay/dead letter, stale backup, unhealthy but policy-ineligible provider and unsettled payment across two tenants. | Correct degradation/alert with source timestamps and correlated trace; no false healthy state from one successful component; authorized operator can link an incident without treating diagnostic events as authoritative finance truth. |
| TEST-REQ-PLAT-018 negative/privacy | Inject secret sentinel, meeting notes and another tenant's identifier; enable On-Prem external telemetry opt-out and interrupt collector/export. | No sensitive value leaks into log, metric label, trace, alert or browser; local On-Prem diagnostics work; external egress is denied; failed collector does not block or falsely mark a transaction complete. |
| TEST-REQ-PLAT-018 recovery | Recover dependency, replay queued work and restore backup service with duplicate/out-of-order signals. | Alert timeline and acknowledgement remain auditable, readiness returns only when dependencies and reconciliation are checked, and backup age is recomputed rather than guessed. |

The OPS and SEC suites require deterministic fault injection, negative permission cases and exact version-bound evidence. SLO thresholds and public availability claims remain unapproved until measured in a real deployment and authorized by the owner.
