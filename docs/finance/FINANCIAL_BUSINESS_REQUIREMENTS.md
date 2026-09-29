# Deterministic finance and business model

ADR-014/015. No live rates, tax rules, payroll obligations, prices or owner spending commitments are invented here.

## Authoritative ledger

Fixed-asset accounting/depreciation is a separate V1.9 Finance contract (REQ-FIN-030, `FIXED_ASSET_ACCOUNTING_CONTRACT.md`): Asset metadata links an acquisition but does not post, depreciate or replace the journal; schedules and disposal reconcile to ledger under reviewed book/country policy.

Books owned by legal entity, functional currency and reporting basis. Journal header: tenant/entity/book/source_event/idempotency/rule_version/accounting_date/posted_at/period/correlation/reversal reference. Lines: account, debit or credit exact decimal, transaction currency/amount, functional amount, FX source/date/version, project/cost/profit center, tax dimensions. Sum debit=credit in functional currency; original transaction amounts remain available. Journals and outbox commit atomically. Posted journal update/delete denied at service and DB grants; corrections use linked reversal/adjustment. Period close locks posting; reopening is approved and audited. Opening balances must balance and reconcile import totals before posting.

Money is exact decimal/integer by explicit policy, never binary float. Round at declared line/document/currency boundary using versioned method; allocate residual deterministically with stable line ordering and record it. Variable minor units; overflow/range/negative value checks. FX not inferred from display conversion. Iranian product convention IRR authoritative, Toman explicit display conversion only; all APIs/export/documents label currency/unit. Tax rates are effective-dated pack data, never hard-coded worldwide or inferred from company location alone.

AR/AP supports quotes/proforma/commercial/tax document distinction, credit/debit note, receipt, partial allocation, overpayment, refund, chargeback, settlement fees, write-off approval, aging and reconciliation. Official tax identifiers and internal numbering are separate; number allocation is transactional with void history, not reuse. Revenue recognition and principal/agent policies require accounting review by stream/country before statutory reporting.

Payment attempt records deterministic key, approved amount/currency, provider/corridor, external reference and state. Timeout => OUTCOME_UNKNOWN, no new charge key; poll/reconcile/manual investigation. Authenticated webhook alone does not override amount/payee mismatch. Deduplicate scoped provider events; out-of-order events validate transition not arrival order. Partial refund cannot exceed refundable amount; concurrent refund serialized. Reconciliation difference creates case, never hidden balance correction. Non-custodial default; ledger 'hold' is not escrow or a bank wallet.

Payroll/compensation is separate from client price. Payroll calculation snapshot includes employment, approved time, benefits/leave/deductions and rule pack. Authorized reviewer approves before posting/payment; changing input invalidates approval. Tracked time alone cannot create entitlement. Compensation floors enforced independently of platform margin; no public underbidding. Commission links attributable collected cash and policy; refunds create reproducible clawback rather than historical mutation.

## Pricing and business controls

### Budget and accounting dimensions — V1.0

`BUDGET_COST_CENTER_CONTRACT.md` is the independent normative Budget/Cost Center/Profit Center specification. Finance owns versioned original/approved/revised plans by entity, branch, department, team, project, center, period and currency; commitments, ledger-backed actual, forecast, consumption, variance, thresholds and audited approvals. Organization owns hierarchy, not financial truth. Actual is derived from posted balanced journals and reconciles by accounting dimensions; unposted spend/commitment never masquerades as actual. Budget is a control and forecast, not a Ledger replacement. Project profitability joins the same documented financial basis. REQ-FIN-018–021 and BUD test evidence block V1.0.

Versioned service packages include base/add-ons/limits/SLA/recurrence, full cost waterfall and exclusions. Client scenario and talent compensation views have different ACLs. Gross margin=(revenue-direct COGS)/revenue; contribution additionally deducts variable selling/delivery costs. Estimated fully-loaded margin includes allocated overhead; it is not accounting net profit. Zero/negative revenue produces defined not-applicable/error, not divide-by-zero.

Floor P=C/(1-m), 0<=m<1, where C is the explicitly stated cost basis excluding price-dependent fees. If fee f is proportional to price, P=(fixed basis)/(1-m-f); denominator <=0 => infeasible. Round upward to currency increment then recheck floor. Example only: C=100, m=25%, no fees => unrounded 133.333..., 2-decimal floor 133.34. Price-dependent fee 3% gives 100/0.72 => 138.89. These are synthetic math examples, not actual offers or owner policy.

Business-floor override requires an explicit authorized exception, scope/value/expiry/reason and audit. Legal/fair-rate restrictions remain non-overridable. AI only proposes. Contract renewal/grandfathering/notice preserved; no silent price changes from model/provider cost changes. Pricing Lab has hypothesis/cohort/control/randomization/predefined metrics/sample logic/min duration/guardrail stop/owner decision. No hidden sensitive-trait pricing, no automatic success from conversion alone.

## AI credits

Non-transferable service usage units by default, not redeemable money or custodial balance. reserve -> execute -> reconcile actual usage -> charge/release reservation. Budget reservation is atomic across concurrent jobs and platform/tenant/project/user/agent caps. Failed/unknown provider usage remains pending until reconciled; never silently exceed cap or double-charge retry. Record pricing schedule version, provider effective model, raw units, retries/tools/search/compute/observability allocation, customer charge and margin. BYOK raw provider cost kept separate from platform charge; approved fallback cannot quietly switch billing responsibility.

## Separate business accounts

Tenant operating ledger != Hayool product unit-economics read model != Hayool corporate statutory books. Streams: annual SaaS, Cloud premium, Dedicated, On-Prem support, modules/packs, implementation, premium SLA, AI credits, network/success fee, managed contractor/team/outcome, marketplace share, runtime, partner/certification, assessments/benchmarks, transaction orchestration. Each has billings, recognized revenue, cash, direct COGS, variable delivery cost, contribution, overhead and working capital. GMV is not Hayool revenue; principal-agent review decides gross/net.

## Operating model contract

Monthly conservative/base/upside scenario for 36 months, actuals replacing assumptions. Inputs each have owner/date/unit/currency/source/confidence/range: tenants/users/prices/discounts/renewals/churn/expansion/sales cycle, CAC/payback, onboarding/support time, infra/storage/egress, AI workload and model mix, payment fees/refunds, marketplace GMV/take, managed volume/payout/statutory/partner/reserve/bad debt/DSO, staffing/R&D/G&A/tax/capital. Outputs: MRR-equivalent/ARR, GRR/NRR, stream contribution, cash timing, runway, break-even, sensitivity and downside liquidity. No financial forecast presented as proven without actual input evidence.

Working capital: dated inflow/outflow schedule, delayed collection scenarios, payout obligations and reserve limits. No promised instant payout, employment/EOR or custody activation until legal model, responsible entity, funding and payment partners approved. Forecast insufficiency => block commitment or require funded approval, not lower worker pay silently.

GA evidence: measured COGS and AI usage, support/onboarding baseline, reconciled transactions, approved pricing/margin/renewal policies, credible scenarios from design partners and owner-approved capital/SLA exposure. Financial model requirements are complete now; commercial values remain explicit owner decisions at the relevant gate.
