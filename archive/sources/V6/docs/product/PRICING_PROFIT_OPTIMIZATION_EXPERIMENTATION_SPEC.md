# Hayool OS — Pricing, Profit Optimization & Experimentation Specification
Version: 6.0
Status: Commercial core architecture

---

## 1. Objective

Pricing must protect the long-term economics of Hayool and tenant businesses while supporting evidence-driven price discovery.

The system must:

- know full cost;
- enforce manager-defined margin floors;
- optimize packaging/pricing;
- run controlled experiments;
- learn from conversion/retention/profit;
- never silently price below required economics.

---

# 2. Margin vocabulary

Never mix these concepts.

## Gross Margin

(Revenue - Direct COGS) / Revenue

## Contribution Margin

(Revenue - Direct COGS - Variable Selling/Delivery Costs) / Revenue

## Operating / Net Margin Target

Includes allocated overhead and broader business costs according to management model.

True accounting net profit is period-level.

For pricing decisions, Hayool may compute an **Estimated Fully Loaded Margin** using allocated overhead.

UI must label estimated vs accounting actual.

---

# 3. Cost waterfall

A product/service price may account for:

- provider/model AI cost
- infrastructure
- storage
- bandwidth/egress
- payment fees
- third-party SaaS
- support
- onboarding
- implementation
- worker/provider payout
- refunds
- dispute reserve
- bad-debt reserve
- transaction tax pass-through
- marketplace payout
- commission
- customer success
- allocated overhead
- risk reserve.

Costs can be fixed, variable, tiered or probabilistic.

---

# 4. Manager profit policies

Manager/platform admin can configure:

- minimum gross margin
- minimum contribution margin
- target fully loaded operating margin
- minimum AI margin
- minimum marketplace take rate
- maximum discount
- price floor
- price ceiling
- allowed experiment range.

Policies can vary by:
- product
- plan
- region
- currency
- channel
- customer segment
- deployment model
- contract.

Hard floor cannot be bypassed by AI without configured high-level approval.

---

# 5. Price floor formula

For a target fully loaded margin `m`:

```text
minimum_price = estimated_fully_loaded_cost / (1 - m)
```

where `0 <= m < 1`.

The engine must clearly state what cost basis is used.

---

# 6. Pricing modes

Support:
- fixed
- per user
- per branch
- per legal entity
- usage based
- AI credits
- transaction
- GMV/take rate
- tiered volume
- metered
- hybrid base + usage
- module/add-on
- enterprise custom
- outcome/managed service.

---

# 7. Hayool OS packaging

Potential dimensions:
- users
- branches
- legal entities
- enabled modules
- storage
- automation volume
- AI credits
- API usage
- marketplace/network
- deployment
- support/SLA.

Avoid plans so complex that buyers cannot predict cost.

---

# 8. Pricing Lab

Pricing experiments are first-class entities.

Fields:
- hypothesis
- target product/plan
- control
- variant
- audience
- randomization
- metric
- guardrail metrics
- start/end
- minimum sample
- statistical method
- result
- decision.

---

# 9. Experiment rules

A good experiment:
- tests a defined hypothesis;
- changes the minimum number of variables;
- has control;
- predefines success metrics;
- observes retention/LTV, not only initial conversion;
- documents outcome.

Do not let AI declare success only because short-term conversion rises.

---

# 10. Primary optimization objective

Manager chooses objective.

Examples:
- maximize contribution profit
- maximize LTV
- maximize ARR subject to margin floor
- maximize adoption while retaining minimum net margin
- maximize marketplace liquidity subject to take-rate floor.

AI does not invent the company's objective.

---

# 11. Guardrail metrics

Examples:
- contribution margin
- refund
- churn
- support load
- bad debt
- network fill rate
- worker payout fairness
- customer satisfaction
- infrastructure cost.

An experiment can be stopped automatically if a guardrail is breached.

---

# 12. Price discovery stages

## Low data
Use:
- design partner interviews
- value research
- competitive reference
- cost floor
- proposal tests.

## Medium data
Controlled cohort experiments.

## High data
More advanced adaptive experimentation may be considered.

Never deploy adaptive personalized pricing solely because sufficient data exists; legal/fairness/customer-trust review is required.

---

# 13. Segmentation

Allowed pricing segments may include:
- plan
- geography
- currency
- company size
- volume
- deployment
- feature package
- contract duration.

Sensitive/protected individual characteristics are not legitimate hidden price optimization inputs.

---

# 14. Geographic/localized pricing

Price Book supports local currency/regional pricing.

Localization can account for:
- currency
- taxes
- purchasing conditions
- payment methods
- market strategy.

Do not pretend FX conversion equals optimal local price.

---

# 15. Price consistency and trust

For recurring subscriptions:
- define renewal-price policy;
- grandfathering;
- notice;
- currency behavior;
- term commitment.

Avoid surprising customers with constant algorithmic price changes.

---

# 16. Discounts

Discount Guardrail evaluates:
- price floor
- minimum margins
- current costs
- commission
- contract lifetime
- expected support.

AI may recommend discount but cannot cross hard floor without approval.

---

# 17. AI Credits pricing

AI Credit pricing engine continuously monitors:
- provider cost
- model mix
- gateway cost
- average retries
- storage/search
- product usage.

It can propose:
- credit conversion schedule
- bundle changes
- included credit amounts
- overage price.

Any material customer price change follows notice/contract rules.

---

# 18. Marketplace pricing

Third-party developers set prices within marketplace policy.

Hayool may take:
- percentage
- fixed platform fee
- runtime/usage fee.

The marketplace take rate should be tested against:
- developer supply
- app quality
- buyer conversion
- support burden
- payment cost.

---

# 19. Managed workforce pricing

Client price protects:
- worker payout
- statutory/partner cost
- ops/account management
- replacement reserve
- bad debt
- payment fees
- target margin.

Do not increase platform margin by silently underpaying talent below compensation floor.

---

# 20. Price recommendation explainability

Authorized manager sees:

- estimated cost
- direct margin
- fully loaded margin
- expected conversion effect
- confidence/data
- experiment history
- assumptions.

---

# 21. Automatic pricing autonomy

Modes:
- manual
- recommendation
- approval
- guarded auto.

Guarded Auto can change price only inside:
- approved product
- approved audience
- configured min/max
- margin floor
- experiment rules.

Never allow unconstrained AI price changes.

---

# 22. Business-level profit optimizer

Hayool can simulate:

- plan price
- AI included credits
- support staffing
- infrastructure
- marketplace take
- churn
- acquisition cost.

Goal:
meet minimum target net operating margin set by management.

The system should distinguish:
- transaction-level profitability
- product-level profitability
- company-level accounting net profit.

---

# 23. Pricing decision ledger

Record:
- price/policy version
- cost model version
- experiment
- recommendation
- approval
- actual performance.

This lets pricing improve from real data.

---

# 24. Ethical/legal constraints

Country/consumer law may restrict:
- misleading price presentation
- discrimination
- reference-price/discount claims
- automatic renewal
- notice
- personalized pricing disclosure.

Country Pack applies local controls.

---

# 25. V1 requirements

V1 must include:
- cost model
- price book
- margin floors
- discount guardrails
- AI-credit economics
- plan/entitlement pricing
- pricing simulator
- manual/recommended price optimization
- experiment framework.

Advanced automated adaptive pricing can follow after data and legal readiness.

