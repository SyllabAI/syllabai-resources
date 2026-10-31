# AUDIT-2026-10-31-f127-notation-4ch1 — the Mode-A notation pass (T-OEQ-NOTATION-1)

**Verdict.** The F127 wave repaired flat print notation (subscripts/superscripts the QP sets in
true position but the PDF text layer linearized flat) across ALL serve-facing fields of the 4CH1
corpus — **967 served parts changed across all 54 sets, new=0/gone=0** — every digit VALUE
untouched, all gates and batteries green, the exporter of record unchanged (zero code paths).

## Classification (ADR-039)
Mode A — presentation/notation repair the source page supports: `C2H4 -> C₂H₄`, `cm3 -> cm³`,
`Mg2+(aq) -> Mg²⁺(aq)`, `SO42- -> SO₄²⁻`. Two occurrences of charge-magnitude restoration
(`SO4- -> SO₄²⁻`, sulfate identity) are disclosed as a Mode-B-grade sub-class. The withhold list
never invents.

## The law (NOTATION-REPAIR.json, 485 tokens)
digits after element symbols -> subscripts; trailing charges -> superscripts; coefficients stay
flat; bracket multipliers after `)` subscript; hydrate coefficients stay flat. **Fail-closed**:
any candidate token absent from the ledger ABORTS the run (proved live twice: the solutionMd
extension surfaced 82 more tokens mid-wave; the rebase onto the moved tip surfaced the rest).
Per-occurrence guards: adjacent charge sign -> ion (known-ion templates chemistry-correct);
`(` -> formula; DETACHED charges (ions-table layout) skip+log.

## Census of record
- token applications: **4678** across 54 topic.json + SOLUTION-ENRICH.json ({'dispatch-multi-formula': 2326, 'dispatch-single-ion': 173, 'dispatch-single-molecule': 548, 'coeff-dispatch-molecule': 53, 'coeff-formula': 371, 'dispatch-single-formula': 102, 'coeff-dispatch-formula': 13, 'unit': 854, 'coeff-charge-sup': 59, 'bracket-mult': 46, 'var_formula': 49, 'dispatch-multi-ion': 61, 'coeff-dispatch-ion': 7, 'ion_token': 4, 'titration': 12})
- bracket-multiplier subscripts (the `)digit` rule): 153
- withhold: 48 tokens — isotopes; MS-quoted wrong-answer formulas (repairing would falsify
  the quote); sign-first ALLOW variants; garbled/typos; spaced-equation fragments; bond dashes; prose
- STEM-RESTORE: 16 tails + 11 cut-span anchors re-derived (dropTail/dropSpan track the repaired
  corpus — the F121 anchor law re-proves them)
- CANARIES: 2 match-strings (C50 equation pin) + 19 part_field_sha pins recomputed

## Rebase disclosure
The wave's original base (8f6a6a80) was orphaned upstream mid-flight (main advanced to e967e75f
via book-lane merges). The wave re-based: the pipeline re-ran deterministically on the tip's
chemistry files and the repaired output verified **byte-identical** to the pre-rebase repair —
the chemistry corpus never moved (the spot-check "drift" was a local-clone pruning artifact,
receipted here for the record).

## Gated run (exporter of record, v6, unchanged)
- G-E1: **967 deltas == the disclosure exactly** (54 sets, new=0/gone=0)
- G-E2 shapes ok · G-E3 54/4860 ok · G-E4 questions.json byte-identical (2,605,409 B) ·
  G-E6 labels 2,607/2,607 ok · G-E7 567 stems + 46 cuts + 1 part cut ok
- counts unchanged: 54 sets / 477 questions / 2,607 parts / 4,860 marks / 4,161 markPoints /
  491 crops / 7 honest stubs · new bundle sha256 135ca487ac9b71dd…

## Batteries
F121 **149/149** (2 corpus-text pins re-derived) · strip-law **29/29** · F116/F117/F118/F119
**PASS** · canaries 165 PASS / 49 FAIL — every failure is missing-infrastructure in the JSON-only
local subset (validation-report.json, asset PNGs, spec-labels, FIGURE-QUEUE, CROSS-DIFF,
physics/maths lanes, G9 harness deps); ZERO byte-regressions; independent PUA scan: 0.

## Disclosed deviations & scope
- solution_md + SOLUTION-ENRICH.json joined the universe (the authored layer carried the same
  flat class — repaired in lockstep so the served authored layer stays consistent).
- Context-verified token adjudication replaced the scope's QP-page contact sheets; page renders
  remain the evidence path for any withhold promoted by human review.
- Not checked here: physics/maths-B lanes (same class — future wave), G9 rendered benchmark and
  the live probe (ride the companion deploy).

## Residuals
None new. The withhold list is filed in NOTATION-REPAIR.json for human review.
