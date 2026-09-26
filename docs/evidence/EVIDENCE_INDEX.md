# Evidence and claims registry

Current state: V7.2 design-only, 2026-09-26. **M0.1 DOCUMENTATION GATE = PASS**, solely for pre-code Source of Truth consistency; **M0.0 = PENDING; M0.2 = PENDING**. `EVID-DOC-001` verifies original source bytes, not product validation. The V7.1 `EVID-DOC-002` review is historical and invalidated for V7.2 by material edits; its record is retained in `archive/V7.1/`. `EVID-DOC-003` records two independent read-only reviews on a shared digest and final package integrity in `DOCUMENT_REVIEW.md`. It cannot pass implementation, security assessment, legal applicability, market readiness or M0.2. No Git SHA, executable build, test output, qualified country opinion, live provider agreement, real design-partner outcome or commercial validation exists.

| ID | Claim / required proof | Present evidence | Status / next trigger |
|---|---|---|---|
| EVID-DOC-001 | Original V6/V7 completeness | `SOURCE_MANIFEST.json` 61 paths and preserved `archive/sources/`; source coverage and byte hashes | PASS documentation source-byte integrity |
| EVID-DOC-002 | V7.1 M0.1 internal consistency | Historical scoped digest and reviews in predecessor archive | Superseded for current V7.2 design |
| EVID-DOC-003 | V7.2 M0.1 closure | 194 REQs, 31 ADR records, 138-ID audit, 25-dimension audit, two read-only reviews, `DOCUMENT_REVIEW.md`, final digest and ZIP manifest | **M0.1 DOCUMENTATION GATE = PASS**; pre-code document only |
| EVID-ENG-001 | M0.0 shadow Autopilot and protection | Exact repo SHA, ENG-RUN and seeded blocker traces | Planned; no repo |
| EVID-ENG-002 | M0.2 independent architecture | Exact SHA, signatures/findings/closure | Planned; no repo |
| EVID-PROD-001 | Internal golden journey | Real approved business trace, ledger, multi-tenant/security, UX/AI-off and recovery | Planned V1.0 |
| EVID-PROD-002 | Design partner independence | Consent/agreement, measurements, support, upgrade/export | Planned V1.1 |
| EVID-POL-001 | IR live sourcing | Qualified applicable policy, approved pack, tests, provider/worker facts | Planned V1.2 |
| EVID-POL-002 | Other country live capability | Per capability/corridor packet, reviewer, effective law/provider | Planned, no blanket global claim |
| EVID-FIN-001 | Money and reconciliation | Independent fixtures, exact journals, sandbox settlement and real review | Planned V1.0+/activation |
| EVID-UX-001 | Accessibility/RTL | Human assistive technology, automated and task completion on declared matrix | Planned V1.0+ |
| EVID-EXT-001 | Studio/private app/re-consent/upgrade | Three independent app dossiers and logs | Planned V1.7–1.10 |
| EVID-MKT-001 | Commercial viability/claims | Paid cohort, real costs, conversion/retention, owner-approved terms | Planned V1.6 |

## Claim status

Claim records contain claim_id, exact wording, scope/country/product version, class (hypothesis/research/specification/measured/qualified/approved/published), owner, source, methodology/sample, limitations, expiry, signoff and public placement. Draft statements about market size, competitor position, ROI, law, provider availability, certification, security or readiness are `hypothesis/research` until reviewed. No publication from a draft. Legal source quotation is never itself an applicability determination.

## Evidence envelope and invalidation

EVID ID, REQ/test/gate, exact Git SHA/build digest, environment and synthetic/real cohort, policy/pack/provider/model versions, clock, tool and procedure, expected/actual result, artifacts and hashes, reviewer, limitations, expiry, disclosure class. Product results are append-only and access-controlled. Code, schema, policy, model, provider terms, infrastructure, jurisdiction or test oracle changes invalidate affected evidence. Restore and live proof cannot be inferred from a planned scenario. Current quality score is unassigned, not 9.5/10. `TESTING_STRATEGY.md` owns methods; `RELEASE_ROADMAP.md` owns pass criteria.
