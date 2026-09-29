> V7.2 adopted V6 detail. Read `docs/SOURCE_OF_TRUTH_INDEX.md` and `docs/CONFLICT_RESOLUTIONS.md` first. V1 means the complete V1.0–V1.10 family, not V1.0 alone. Vendor/law/version statements inherited below are historical candidates, never production approval. Current contracts, readiness and normative refinements are in the V7.2 architecture and catalogs. Historical setup commands are not execution authority.

# Hayool OS — Unit Economics & Financial Model Specification
Version: 7.2 overlay (V6 detail adopted)
Status: Adopted normative detail; subject to V7.2 resolutions and release mapping

## 1. Purpose
Hayool OS has multiple revenue engines with very different gross-margin and working-capital profiles.

They must not be blended into one misleading revenue number.

## 2. Revenue streams
- Annual SaaS license
- deployment/hosting premium
- On-Prem support
- AI Credits
- implementation/onboarding
- modules/add-ons
- premium SLA
- network/success fees
- managed contractor fees
- managed team/project revenue
- assessments/certification
- analytics/benchmarks
- integrations.
- marketplace app/pack revenue share
- managed extension runtime/hosting
- developer/partner certification services.

## 3. Revenue-stream P&L
For each stream track:
- gross billings
- recognized revenue
- cash collected
- direct COGS
- gross profit
- contribution cost
- contribution margin
- allocated overhead
- working capital.

## 4. AI economics
Track:
- provider/model cost
- metered model cost
- gateway cost
- tool cost
- vector/search cost
- customer credits charged
- gross margin.

Set:
- minimum AI margin policy
- budget alerts
- provider price-change response
- credit schedule versioning.

## 5. Managed workforce economics
Track:
- client billings
- worker pay
- statutory/partner costs
- payment fees
- bad debt
- replacement cost
- account/ops cost
- dispute cost
- contribution margin
- DSO
- payout timing.

High revenue can still be a bad business if working capital and contribution margin are poor.

## 6. SaaS unit economics
Track:
- ARR
- MRR equivalent
- GRR
- NRR
- logo retention
- expansion
- CAC
- CAC payback
- gross margin
- support cost/tenant
- onboarding cost
- infrastructure cost.

## 7. Network metrics
- active demand
- active supply
- liquidity by skill
- fill rate
- time to shortlist
- time to start
- application acceptance
- repeat engagement
- take rate
- dispute rate.

## 8. Pricing constraints
Plans must protect:
- support cost
- AI cost
- storage/infra
- payment fees
- implementation burden.

Avoid unlimited features with unbounded variable cost.

## 9. Cash management
Managed workforce may require paying talent before client cash arrives.

Model:
- payment terms
- reserve
- credit risk
- collection
- payout timing.

Do not promise instant payout if working capital cannot support it.

## 10. Scenario model
Business Digital Twin should model:
- tenant growth
- AI usage
- support load
- managed workforce volume
- take rate
- DSO
- churn
- infrastructure.

## 11. Pricing research gate
Do not lock final public pricing only from internal intuition.

Before GA:
- interview design partners
- competitor packaging study
- willingness-to-pay testing
- proposal experiments
- support/COGS modeling.

## 12. Revenue recognition/legal review
Managed workforce gross-vs-net revenue recognition depends on contractual role/accounting rules.

Accounting/legal experts must determine principal-vs-agent treatment by engagement mode/jurisdiction before financial reporting.


## 13. Pricing and profit optimization

Canonical source:

`docs/product/PRICING_PROFIT_OPTIMIZATION_EXPERIMENTATION_SPEC.md`

Management can configure:
- minimum contribution margin;
- target fully loaded margin;
- minimum AI margin.

The engine may recommend/experiment only within policy bounds.

## 14. Fully loaded AI economics

Canonical source:

`docs/ai/AI_USE_COST_GOVERNANCE_SPEC.md`

AI COGS includes more than model tokens.

Account for:
provider + gateway + retrieval + tools + retries + compute + storage/observability where material.

## 15. Ecosystem economics

Track separately:
- app GMV
- Hayool marketplace share
- developer payout
- payment fees
- refunds
- certification/support cost
- runtime cost
- contribution margin.

A low marketplace take rate may still be strategically valuable if it accelerates platform adoption; decisions require data rather than arbitrary percentages.

