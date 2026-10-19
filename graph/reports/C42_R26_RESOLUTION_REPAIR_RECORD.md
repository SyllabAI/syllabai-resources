# T-C42 R26 — R1-SHAPED REPAIR ROUND over the R25 4-row defect inventory
## (the loop's SEVENTH R1-shaped repair round — and the FIRST over the promoted surface)

- Course: igcse-maths-a (4MA1 Higher)
- Round: R26 (lane numbering per the loop's iteration precedent R6-R9 / R10-R13 / R14-R17 / R18-R21 / R22-R25)
- Fired by: operator directive **"(a) an R26-shaped repair over the 4-row inventory"** (2026-10-04, zai-web, gateway trace `1a10641c64283c99`) — option (a) of the R25 re-gate record's next-decision menu, named verbatim
- Over: the R25 re-gate's fresh defect inventory (4 REJECT rows in `scripts/c42_r25_fresh_verdicts.yaml`; the R25 gate PASSED at Part A 458/464 = 98.7%, per-class exact 88/94 = 93.62% / partial 100% / none 100% — the loop's first gate pass under the promoted surface, zero movement)
- Round-start pin: `00abec1` (the R25 post-commit audit commit)
- **ZERO STORE BYTES MOVE from this round** (the anti-forgery rule): every adjudication lands as a next-re-build-facing record, consumed fail-closed at the R28-shaped lane

---

## 1. The R26 novelty — the promoted surface

All 4 inventory rows sit on the R5-promoted 832-row HUMAN_VALIDATED surface, each pinned in `scripts/c42_r5_promotions.yaml` (sha16 `9bad739bd79e5899`) **with its then-code**. This is the loop's first repair round over promoted rows. The round's store-facing state carrier is therefore TWofold:

1. **The override map** `scripts/c42_section_overrides_r26.yaml` (schema `c42-r28-section-overrides/1.0`) — the section-level re-homing, consumed by the c40 tool at the R28-shaped rebuild together with the R1/R6/R10/R14/R18/R22 maps (the R12/R16/R20/R24 wiring convention).
2. **The promotions amendment** `scripts/c42_r26_promotions_amendment.yaml` (schema `c42-r28-promotions-amendment/1.0`) — 3 code supersedes + 1 exclusion, consumed by the rebuild's promotions re-application AFTER the R5 file. **The R5 file itself stays BYTE-UNTOUCHED** (the P5 convention: landed records never edited; corrections land as dated records of their own). Wiring the amendment into the rebuild tool is the rebuild lane's job (the R24 tool-bump precedent).

The 3 REATTRIBUTE rows REMAIN in the promoted set at their new codes (the R5 promotion judged the sections' teaching value; the repair corrects their codes); the DEMOTE row leaves the promoted set entirely (832 → 831). Both carriers are reviewable and reversible by the operator before the R28-shaped lane fires.

## 2. Verdicts (operator-delegate; full rationales in `scripts/c42_r26_repair_verdicts.yaml`)

| # | Row | Note :: ord | From | Disposition | To | Root class |
|---|-----|-------------|------|-------------|----|------------|
| 1 | `81c0b59852d5d4b6` | types-of-number :: 1 "What are integers and rational numbers?" | 4MA1-1.1G | **REATTRIBUTE** | **4MA1-1.1A** | adjacent-surface scope difference WITH canonical target — the section's integers definition + the -3..3 example set are 1.1A's "understand and use integers (positive, negative and zero)" VERBATIM; 1.1G's vocabulary (odd/even/prime/factors/multiples) appears nowhere in it |
| 2 | `7fdded0b9245e1c3` | introduction-to-vectors :: 3 "How do I multiply a vector by a scalar?" | 4MA1-5.1D | **REATTRIBUTE** | **4MA1-5.1C** | adjacent-surface scope difference WITH canonical target — scalar multiplication (3 × (2,-1) = (6,-3) componentwise) is 5.1C's "multiply vectors by scalar quantities" VERBATIM; 5.1D demands add/subtract, absent from the section |
| 3 | `e6ed72481e8ffc2e` | drawing-straight-line-graphs :: 4 "What if the equation is not in the form y = mx + c?" | 4MA1-3.3F | **REATTRIBUTE** | **4MA1-3.3H** | adjacent-surface scope difference WITH canonical target — rearranging 3x+5y=30 → y = -3/5 x + 6 and reading off gradient/intercept is 3.3H's y = mx + c recognition VERBATIM; 3.3F demands gradient-from-two-coordinates (absent), and the ledger's Foundation conversion-graphs wording misses too |
| 4 | `70f0b027f3f1528f` | factorising-by-grouping :: 2 "How do I factorise by grouping?" | 4MA1-2.2F | **DEMOTE_TO_WORKLIST** | (worklist) | limit-scope difference with NO canonical 188 target — four-term two-variable grouping (xy + 3x + 5y + 15) is outside 2.2F's "(limited to x^2 + bx + c)" cap and outside even 2.2B's un-limited "quadratic expression"; the R25 menu's DEMOTE option exercised (the directive named no re-anchor) — the loop's fourth DEMOTE, first of a promoted row |

Scorer corroboration (PROPOSAL-ONLY, binds nothing): top-1s excluding-current CONVERGE on 5.1C @ 0.1762 / 3.3H @ 0.2752 (beating the current codes) / 1.1A @ 0.1859; for the DEMOTE row the packet documents the ABSENCE finding in scorer form (current 2.2F @ 0.1944 tops the including-current packet; top-excluding 2.8C @ 0.1937 is noise — nothing in the ratified 188 beats ~0.19, the R18 labeling-primer class).

## 3. Note-level adjudications — all four STANDING (zero resolution-file amendments; the resolution stays byte-untouched since R14, counts 222/214/8)

| Anchor | Note | Joined | Ruling | Basis |
|--------|------|--------|--------|-------|
| `spcpt_J55PhZ2cbPsYvpt8` | types-of-number | 1.1G | STANDING | ords 0/2/3/4/5/6 carry the vocabulary demand verbatim (multiples/factors/primes), ord 10 rides the anchor; the ord-1 reject is section-level |
| `spcpt_vMSNnYkKPf62MRH9` | factorising-by-grouping | 2.2F | STANDING (with the honest scoping note) | the join layer is not amended by repair rounds; the full census finds NO ord of this note teaching the within-cap demand — the ID-LEVEL anchor question (move/unresolve) is an operator decision NOT fired by this directive; 2.2F's coverage does not depend on it (17 rows via the DOTS + factorising-quadratics notes) |
| `spcpt_h8QyRmzX5mCJb3X9` | drawing-straight-line-graphs | 3.3F | STANDING | ord 5 (ax + by = c) rides the anchor unsampled; ord 0 is the H3 HOLD; the conversion-graphs note's 4 promoted rows carry 3.3F's Foundation ledger surface verbatim |
| `spcpt_v6tP4DSVShVJMJhk` | introduction-to-vectors | 5.1D | STANDING | ord 2 "add and subtract column vectors" is the demand verbatim; ords 0/1 the basics; ord 4 unsampled |

## 4. Census remarks (recorded for the operator, NOT adjudicated — promoted rows beyond the fired inventory)

1. **factorising-by-grouping ords 0/1/3** (7f9612c10eaaaa2e / b7602c675bf3a406 / 2ea85d1d97ebae38, all HUMAN_VALIDATED on 2.2F): the SAME out-of-cap grouping class as the DEMOTE'd ord 2 — every section of the note teaches four-term two-variable grouping. Operator menu: a future same-class repair (a 3-row DEMOTE batch or an id-level re-anchor), or leave as-is for the next draw.
2. **types-of-number rational/irrational remainder**: no canonical 188 row classifies rational vs irrational numbers (the R14 mass-conversion absence class) — a CORPUS GAP, not a repair-round action.
3. **drawing-straight-line-graphs ord 5** (d58b7f9f0fa551d3, HV on 3.3F, unsampled): the ax + by = c plotting surface is the rearrangement sibling of the re-homed ord 4 — the same adjacency question applies; the note-level join partly rides it.
4. **introduction-to-vectors ord 4** (5e1e430120ed7e2f, HV on 5.1D, unsampled): combination-of-vectors content adjacent to the add/subtract demand; no sampled evidence against; left for the draw.
5. **The promoted-surface interaction statement** (the R26 novelty, stated once): zero store bytes; two state carriers; R5 file byte-untouched; operator review retained before the R28-shaped lane.

## 5. Coverage & census projections (PROJECTED from verified facts, ASSERTED NOWHERE — the DC-R24-01 discipline)

| Metric | Now (R25 state) | Projected at R28-shaped rebuild | Mechanics |
|--------|-----------------|--------------------------------|-----------|
| Covered codes | 130 / 188 | **132** | GAINED 1.1A + 5.1C (both currently uncovered — the 4.8F-at-R24 class); LOST none (1.1G keeps 7 rows, 5.1D keeps 4, 3.3F keeps 6, 2.2F keeps 17 — verified row-by-row) |
| Uncovered-SP (Part B) | 58 | **56** | the 1.1A DEFER row `da25da48e0be5c64` + the 5.1C DEFER row `2332964a4f1b02ca` resolve into anchored rows |
| Promoted (HUMAN_VALIDATED) | 832 | **831** | the DEMOTE row excluded by the amendment |
| Anchored | 839 (832 HV + 7 SUGGESTED) | **838** (831 HV + 7 SUGGESTED) | the 4 H3 HOLD rows untouched |
| Unresolved-span worklist | 23 | **24** | the DEMOTE row lands via the c40 DEMOTE convention |
| Store rows | 920 | **918** | the 2 resolved DEFER rows vanish; the DEMOTE row re-keys into the worklist |

## 6. Heading-only convention — STANDING, no new decision

The 4 H3 HOLD rows (the R5-apply hold set, unchanged through R25) are LISTED not decided — the per-row operator sign-off the R24/R25 records still owe was NOT given with this directive: 1.7B (multiple-ratios ord 0, `1dfc65df88b35d69`) / 6.3J (relative-and-expected-frequency ord 4, `2d44bcf00f589c18`) / 3.3F (drawing-straight-line-graphs ord 0, `91a5080f8b390de6`) / 2.2C (expanding-single-brackets ord 0, `56905a113334dcd1`). The 3.3F hold shares its note with verdicted row e6ed72481e8ffc2e — the ord-4 REATTRIBUTE is NOT a content-row CONFIRM of note+3.3F and creates NO H2 un-hold evidence.

## 7. Check battery — A1-A9 ALL PASS 9/9 (pre-commit, exit 0)

`scripts/c42_r26_repair_check.py` → `graph/reports/C42_R26_REPAIR_CHECK.json` (schema `c42-r26-repair-check/1.0`): inventory agreement (map + amendment == the R25 4-row set), projection agreement (map == verdicts, 3+1, 4 STANDING, empty dated corrections), code domain (targets canonical, rows HUMAN_VALIDATED), wordings + ledger facts (1.1A/5.1C/3.3H citations; 2.2F cap; 3.3F shared-tier with both cited texts), joins STAND + resolution byte-untouched `00abec1` → HEAD, substrate pins + promoted-surface guards (R5 pins verified; 1.1A/5.1C uncovered; 3.3H = 7 rows), idempotency (proposals + map + amendment byte-identical re-runs), footprint (the declared 9-file R26 footprint), round artifacts (convergences + absence finding pinned).

## 8. Disposition & next lanes

**R26 gate evidence COMPLETE**: 3 verdicted REATTRIBUTEs (1.1G → 1.1A, 5.1D → 5.1C, 3.3F → 3.3H), 1 DEMOTE_TO_WORKLIST (2.2F grouping — the loop's fourth DEMOTE, first of a promoted row), 0 RETAINs, 0 id-level rows, 0 extension entries, 4 note-level STANDING rulings, 4 H3 HOLD rows listed not decided, 5 census remarks, 0 dated corrections. Zero store bytes move; the R5 promotions file stays byte-untouched.

The loop never self-fires. Awaiting explicit operator instruction:
- **(a) R27 (join re-run) + R28 (substrate re-build consuming the R26 map AND the R26 promotions amendment)** — the rebuild tool must wire both (the R24 tool-bump convention) and compute its own delta proofs (promoted re-applied at 831 with the 3 superseded codes, the DEMOTE row landing unresolved-span, the 2 DEFER rows resolving).
- **(b) R29 re-gate** (operator gate 2 re-run) — the re-seeded draw over the rebuilt surface.
- **(c) The 4 H3 HOLD per-row sign-offs** (1.7B / 6.3J / 3.3F / 2.2C) — still owed per the R24/R25 records.
- **(d) The promoted-surface same-class candidates** (grouping ords 0/1/3; drawing-straight-line-graphs ord 5), **the rational/irrational corpus gap**, **the ord-3 promoted-surface extension candidate** (3d-pythagoras SOHCAHTOA-3D) — each an operator-level decision.
- Standing reminder: PAT / RENDER_KEY / Neon rotation.
