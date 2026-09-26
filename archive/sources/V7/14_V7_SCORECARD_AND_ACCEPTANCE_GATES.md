# Hayool OS V7 — Multi-Dimensional Scorecard & Acceptance Gates

## 1. Scoring rule

A score above 9.5 is a **target design threshold**, not a claim about an unbuilt product.

No dimension receives an Evidence Readiness score above 9.5 until objective evidence exists.

## 2. Target Design Readiness

| Dimension | Target | What V7 requires |
|---|---:|---|
| Product/Domain Architecture | 9.8 | typed kernel, golden loop, clean-core classification |
| Technical Architecture | 9.8 | modular boundaries, migrations, provider abstractions, failure handling |
| Extensibility | 9.9 | Studio + packages + APIs/events + Remote Apps + compatibility |
| AI/Decision Architecture | 9.8 | correct engine selection, evals, cost, fallback |
| Autonomous Engineering | 9.8 | exact-SHA, bounded repair, deterministic gates, evidence |
| Security | 9.8 | tenant isolation, least privilege, supply chain, incident path |
| Privacy/Data Governance | 9.7 | purpose, retention, residency, cross-border, subprocessors |
| Global Adaptability | 9.8 | Jurisdiction Context + Country Packs + providers + mobility |
| Accessibility | 9.7 | WCAG 2.2 target, RTL/LTR, assistive-tech gate |
| Finance/Economics | 9.7 | deterministic finance + unit economics + working capital |
| Legal/Compliance Architecture | 9.7 | effective-dated policies, evidence, legal review gates |
| Market/GTM Strategy | 9.7 | focused wedge, claims register, design-partner evidence |
| Branding | 9.6 | one masterbrand, audience promises, trademark/claim gate |
| Psychology/Trust | 9.8 | buyer/developer/worker anxiety addressed in product controls |
| Innovation/Creativity | 9.8 | intent-to-outcome, capability bounties, outcome graph |
| Future Readiness | 9.8 | packs, adapters, portability, controlled technology adoption |
| Business/Commercial | 9.7 | multi-stream P&L, partner economics, phased market expansion |

## 3. Evidence Readiness

Before code, expected Evidence Readiness is intentionally low.

Evidence Readiness increases only through:
- real tests
- staging
- restore/upgrade rehearsals
- security evidence
- legal validation
- design partners
- unit economics
- production operations.

This prevents “documentation theater.”

## 4. Gate rules

### Architecture Gate
No unresolved structural blocker.

### Security Gate
No tenant/permission/secrets blocker.

### Financial Gate
No broken ledger invariant or unmodeled critical money state.

### Global Gate
No unsupported jurisdiction/provider claim.

### AI Gate
No high-impact un-evaluated autonomous decision.

### Accessibility Gate
No known blocker in golden journeys.

### Ecosystem Gate
No extension path requiring Core patch for ordinary customization.

### Market Gate
No claim of PMF/readiness without real customer evidence.

## 5. Final 9.5+ meaning

For a dimension to be rated >9.5 in a release review:

1. Design requirements are explicit.
2. Implementation exists.
3. Deterministic tests pass where applicable.
4. Independent review passed at exact SHA.
5. Relevant staging evidence exists.
6. Applicable legal/jurisdiction evidence exists.
7. Material residual risks are accepted.
8. Real-market evidence exists when the dimension concerns market readiness/value/retention.

No AI reviewer may assign >9.5 by impression alone.

