# Engineering evidence addendum — 2026-09-26 UTC

The original V7.2 package is preserved at `archive/V7.2/Hayool-OS-V7.2-Final-Source-of-Truth.zip` (SHA-256 `35054ad417242eda797d81816d81ae10a2bcc44b4a10fcc8784005c7d1d5d700`). The pre-code wording below is historical where it conflicts with this live repository addendum. Exact final-head observations are maintained without changing the reviewed commit in the linked GitHub PR evidence ledgers.

| ID | Status | Observed evidence and limit |
|---|---|---|
| EVID-IMP-001 | PASS, import only | Verified import commit `7f8ecbd986ccb399d736bbb0f55a1345067de911`, 153 safe ZIP entries, 152 package-manifest files, 61 source files, predecessor hash and design digest before/after import. No product claim. |
| EVID-REPO-001 | OBSERVED | [Repository audit](../engineering/REPOSITORY_REALITY_2026-09-26.md): public `xbroute/hayool-os`; original private-plan 403 later resolved by public visibility; `main` SHA `138bdb78530403bac8407738c05fe033514a7838` and current PR/review/status protection verified. Initial secret/environment metadata empty. |
| EVID-ENG-001 | **M0.0 PENDING** | [Bootstrap PR #1 evidence ledger](https://github.com/xbroute/hayool-os/pull/1#issuecomment-5849944631). Earlier real candidate Actions run `36267802714` on `e5cf65c0e7e85e7383a6b5b3e5075078801649d4` succeeded with artifact `10914339627`, digest `sha256:ea015d6e57f1192ad2afbd078d08a40f6d6912e59983d9d0211e9fb8e492fcfb`; it predates the two-P1 repair. New regression tests reproduce the prior workflow self-attestation and in-process test poisoning, and reject them after the code fix. Final-head CI/reviews are recorded in the ledger. Default `main` does not yet run the trusted verifier; a same-App status alone is forgeable. Strict ENG-RUN cannot PASS before live trusted proof and independent approval/merge. |
| EVID-ENG-SHADOW-001 | **PENDING** | [Shadow PR #2 ledger](https://github.com/xbroute/hayool-os/pull/2#issuecomment-5849945980). Earlier real candidate run `36267822272` on `eda3c9158904d368cbd5dfb44f303d671fb59fe0` succeeded with artifact `10913803842`, digest `sha256:b6396b31791c880fa9aab51bce302f66fe52152313e88ea3a91a037cbba1c1d6`. Earlier [failure injection](https://github.com/xbroute/hayool-os/pull/2#issuecomment-5849273815) rejected two explicitly synthetic AI PASS votes over hard FAIL. Final architecture/final SHA still require rerun; no Shadow PASS is claimed. |
| EVID-ENG-P1-001 | LOCAL REGRESSION PASS; LIVE PENDING | `bootstrap/regression_tests/test_unit_boundary.py` demonstrates old candidate test poisoning and proves the pinned, read-only, no-network container cannot change trusted evaluator state. `bootstrap/regression_tests/test_trusted_gate.py` demonstrates forged workflow/artifact acceptance risk and deterministic rejection by the new verifier. These are local tests until a final-head GitHub run executes. |
| EVID-ENG-002 | **M0.2 PENDING** | M0.2 is not started until M0.0 has real PASS, P0/P1=0, exact-SHA CI/reviews/ENG-RUN and independent merge. |

ADR-032 adds the CI trust-boundary decision with traceability to ADR-023/025 and REQ-GOV-004–009. No original V7.2 requirement, owner decision or product capability has been changed. The prepared strict ENG-RUN schema requires a live default-main trusted run; a preparation record with no such run is not a PASS. No production secret, deployment or V1.0 implementation is claimed.

---

# Evidence and claims registry

Current state: V7.2 design-only, 2026-09-26. **M0.1 DOCUMENTATION GATE = PASS**, solely for pre-code Source of Truth consistency; **M0.0 = PENDING; M0.2 = PENDING**. `EVID-DOC-001` verifies original source bytes, not product validation. The V7.1 `EVID-DOC-002` review is historical and invalidated for V7.2 by material edits; its record is retained in `archive/V7.1/`. `EVID-DOC-003` records two independent read-only reviews on a shared digest and final package integrity in `DOCUMENT_REVIEW.md`. It cannot pass implementation, security assessment, legal applicability, market readiness or M0.2. No Git SHA, executable build, test output, qualified country opinion, live provider agreement, real design-partner outcome or commercial validation exists.

| ID | Claim / required proof | Present evidence | Status / next trigger |
|---|---|---|---|
| EVID-DOC-001 | Original V6/V7 completeness | `SOURCE_MANIFEST.json` 61 paths and preserved `archive/sources/`; source coverage and byte hashes | PASS documentation source-byte integrity |
| EVID-DOC-002 | V7.1 M0.1 internal consistency | Historical scoped digest and reviews in predecessor archive | Superseded for current V7.2 design |
| EVID-DOC-003 | V7.2 M0.1 closure | 194 REQs, 31 ADR records, 138-ID audit, 25-dimension audit, two read-only reviews, `DOCUMENT_REVIEW.md`, final digest and ZIP manifest | **M0.1 DOCUMENTATION GATE = PASS**; pre-code document only |
| EVID-ENG-001 | M0.0 shadow Autopilot and protection | Bootstrap code and two independent earlier-SHA reviews exist; real CI and final-SHA reviewer proof are pending; main protection configured after public visibility; CI and final-head review pending | PENDING; no milestone PASS |
| EVID-ENG-002 | M0.2 independent architecture | Required only after real M0.0 PASS on exact repository SHA | PENDING; not run |
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
