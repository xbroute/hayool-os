> Historical V7 proposal: retained for provenance; current authority is docs/SOURCE_OF_TRUTH_INDEX.md.

# Hayool OS V7 — Ecosystem, Developer Platform & Trust Compact

## 1. Objective

The ecosystem must make Hayool larger than the Core team without making customers less safe or developers economically disposable.

## 2. Developer promise

Hayool commits to:
- documented stable contracts
- explicit lifecycle/deprecation
- test environment
- meaningful logs/traces
- permission transparency
- migration guidance
- predictable review
- transparent billing
- data portability
- explicit first-party conflict policy.

## 3. First-party conflict policy

A partner app becoming successful does not automatically justify copying it into Core.

A capability may enter Core when:
- required for platform integrity/security;
- broadly cross-industry;
- central deterministic correctness requires ownership;
- performance/transactional integrity requires coupling;
- ecosystem implementation creates unacceptable systemic risk.

If a partner capability overlaps:
- document rationale;
- communicate roadmap;
- provide migration/compatibility path;
- respect IP/license;
- consider partnership/acquisition/transition where appropriate.

Do not weaponize privileged marketplace data to clone partner products.

## 4. Marketplace trust

Listings disclose:
- publisher
- version
- support status
- permissions
- protected data
- egress
- storage region
- retention
- subprocessors
- AI providers
- license
- billing
- security contact
- maintenance state.

## 5. Review tiers

- Community
- Verified Publisher
- Verified App
- Enterprise Ready
- Regulated/Certified Partner
- First-party.

Badges describe review scope, not vague excellence.

## 6. Permission/version model

Material increases in:
- scopes
- protected data
- egress
- privileged actions
- billing behavior

require explicit admin review/re-consent.

Code rollout and permission rollout can be separated so an app cannot use new privilege before consent.

## 7. Supply-chain controls

Marketplace pipeline:
package
→ signature
→ manifest validation
→ dependency/license scan
→ malware/static analysis
→ secret scan
→ permission minimization
→ compatibility tests
→ accessibility checks
→ functional review
→ publication.

High-risk data/regulated apps require specialist review.

## 8. Developer experience KPI

Primary:
**Time to First Working Extension**

Also:
- docs task success
- API error rate
- breaking changes
- sample-app health
- developer retention
- active apps
- support tickets/app
- update success
- uninstall success
- revenue/payout reliability.

## 9. App lifecycle

Draft
→ Development
→ Private Test
→ Submitted
→ Reviewed
→ Published
→ Updated
→ Deprecated
→ Retired.

Installation:
Install
→ Configure
→ Active
→ Upgrade
→ Suspended
→ Uninstall.

## 10. App observability

Developer:
- scoped logs
- traces
- errors
- invocation metrics
- rate-limit metrics
- installation health.

Tenant admin:
- status
- scopes
- protected data
- egress
- recent errors
- usage
- version
- publisher/support.

## 11. Abandonment

Unmaintained app:
- marked visibly
- customers notified
- security status shown
- export/migration path
- possible ownership transfer/fork only when license permits.

## 12. Capability Request / Bounty

Customer need can resolve to:
1. existing Core capability
2. existing Studio template
3. Marketplace app
4. AI-generated draft solution
5. private app
6. bounty/partner build
7. first-party Core proposal.

The Core roadmap is not the only answer.

## 13. Ecosystem economics

Track:
- app GMV
- developer payout
- Hayool share
- refunds
- payment fees
- review/certification cost
- runtime cost
- support
- churn.

Optimize for platform health, not maximum take rate.

## 14. Public/open strategy

Prefer public/permissive where strategically useful:
- SDKs
- CLI where appropriate
- schemas/specs
- sample apps
- extension test kit
- selected connectors.

Commercial Core may remain proprietary.

## 15. Ecosystem GA proof

Do not call the ecosystem ready until an external developer can:

discover docs
→ create app
→ obtain test tenant
→ authenticate
→ call API
→ subscribe event
→ add UI/action
→ request permission
→ test
→ package/sign
→ install
→ observe
→ update
→ receive re-consent if needed
→ bill where supported
→ debug
→ uninstall/export

without persistent Hayool engineering assistance.

