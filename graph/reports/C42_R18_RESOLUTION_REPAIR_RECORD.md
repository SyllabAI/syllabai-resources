# C42 R18 — R1-SHAPED REPAIR ROUND over the R17 2-row defect inventory (round record)

**Date:** 2026-10-04 | **Directive:** "R18-shaped round over the 2 rows" (2026-10-04, zai-web)
**Round:** R18 — the fifth R1-shaped repair round of the C42 K2-B rework loop (scope §7)
**Reviewer:** Super Z (GLM agent), operator-delegate under the fired R18 directive; the human
operator retains final sign-off; per the anti-forgery rule nothing here flips the store (the
§18 apply is R5, operator gate 3)
**Baseline:** `cf1d8ad` (the R17-closed HEAD)

## What fired

The R17 re-gate (operator gate 2 re-run, the loop's fourth pass) closed **FAIL, honest**:
Part A 454/464 = 97.8% with partial 238/238 and none 132/132 at 100.0%, but the EXACT
stratum at 84/94 = 89.4% < 90% — the R13 projection falsified by the re-seeded draw
mechanics and recorded as the finding. The R17 record's next-decision menu (scope §7)
named this round as option (a): *"an R18-shaped repair round over the 2-row inventory
(1 REATTRIBUTE 1.2G -> 1.3D + 1 DEMOTE/RETAIN decision on the labeling primer), which per
the loop's arithmetic puts the exact stratum at 86/94 = 91.5% on this draw's composition"*.
Menu options (b) (the heading-only convention amendment), (c) (fire R5 on the confirmed
rows) and (d) (accept and re-scope) are **NOT fired** by this directive — each stays the
operator's call. Lane numbering follows the loop's iteration precedent
(R6–R9, R10–R13, R14–R17): this round is R18; the next natural lanes are the join re-run
(R19), the substrate re-build (R20) and the re-gate (R21); R5 stays reserved; the
deterministic follow-ons fire only on explicit operator instruction — the directive named
the repair round alone.

## The 2-row inventory (R17 fresh verdicts, scripts/c42_r17_fresh_verdicts.yaml)

| # | Row | Code | Root | R18 disposition |
|---|---|---|---|---|
| 1 | `73324fa2b6bd3433` — converting-between-fdp ord 3 "How do I convert from a decimal to a fraction?" | 4MA1-1.2G | inverse-direction scope difference WITH a canonical target (the R9/R10 ord-1 precedent in this very note) | **REATTRIBUTE 1.2G -> 1.3D** |
| 2 | `9c1ff91e80080d4b` — basic-angle-properties ord 1 "How do I label lines segments, angles and shapes?" | 4MA1-4.1B | notation-primer scope difference, no canonical 188 row teaches geometric labeling per se | **DEMOTE_TO_WORKLIST** (the loop's third DEMOTE) |

### Row 1 — REATTRIBUTE 1.2G -> 1.3D

The section teaches converting a DECIMAL to a FRACTION (place value over 10/100/10^n:
0.3 = 3/10, 0.07 = 7/100, 30.01 = 3001/100, n decimal places over 10^n). 1.2G's demand is
'convert a fraction to a decimal or a percentage' — the FORWARD direction; the section
teaches the inverse operation. Not a tier artifact (1.2G absent from the C30 ledger — no
foundation wording widens it). The canonical target EXISTS: **1.3D 'convert a decimal to a
fraction or a percentage' is the section's surface verbatim** (a Foundation code — bare
`IGCSE_MATHS_A:1.3D` id per the R10 tier convention). This is exactly the R9/R10 ord-1
repair shape: ord 1 (percentage -> decimal) was REJECTed at R9 in these words and
REATTRIBUTE'd to 1.6C by the R10 operator round; this row is its decimal->fraction
sibling. The note-level join STANDS via its forward-conversion sections (ords 5/6 teach
fraction->decimal and fraction->percentage — the demand verbatim). CONSEQUENCE: 1.3D
gains chunk coverage at the next substrate re-build (the R12/R16 coverage-gain precedent:
1.6A + 1.6C at R12 via the R10 rows, 4.1D at R16 via the R14 rows) — the 1.3D uncovered-SP
DEFER row on the R17 worklist resolves into anchored rows; coverage 128 -> 129 codes
projected (129/188, 59 uncovered). The arithmetic lands at the re-build/re-gate lanes,
not asserted here.

### Row 2 — DEMOTE_TO_WORKLIST (the DEMOTE/RETAIN decision)

The section teaches LABELING conventions (line segment AB, angle ABC at point B, acute vs
obtuse, triangle ABC from its segments) — 4.1B's demand is 'use angle properties of
intersecting lines, parallel lines and angles on a straight line' and the section teaches
no angle property at all. Not a tier artifact (4.1B absent from the C30 ledger). No
canonical 188 row teaches geometric labeling per se — the proposals packet's top-1 for
this row is 4.1B ITSELF (score 0.167), the scorer confirming the absence of any better
surface (a scorer artifact by construction, the R14 mass-conversion-near-miss class).
The note-level join STANDS via its property sections (ords 0/2/3 carry the basic angle
facts — ord 0 CONFIRMed at R4; ord 4 is the R1 4.2B ruling), so a section-level
REATTRIBUTE has no target and a RETAIN would knowingly re-create the scope difference for
the next re-gate to reject again: the honest disposition is the menu's DEMOTE — the chunk
leaves the anchored surface for the unresolved-span worklist, recorded with this reason,
never forced. Third exercise of the scope §4 R1 menu's DEMOTE action (R10
related-calculations ord 2, R14 unit-conversions ord 2, here). CONSEQUENCE: the
unresolved-span class grows 22 -> 23 at the next re-build (three DEMOTEs now incl.
R10 + R14); 4.1B keeps its note-level join and its coverage via ords 0/2/3.

## Extension rows (the R17 census remark, the R6 precedent — transparently labeled, zero silent repair)

| Row | Content | Target | Basis |
|---|---|---|---|
| `2c9be555e064b975` — fdp ord 2 "decimal to a percentage" (multiply by 100) | 4MA1-1.2G -> **1.3D** | 1.3D names the surface verbatim ("the same 1.3D surface" — the R17 census remark's own finding) |
| `734603c6ddf10662` — fdp ord 4 "percentage to a fraction" (write over 100) | 4MA1-1.2G -> **1.6C** | 1.6C 'express a percentage as a fraction and as a decimal' verbatim — the same class R10 already repaired at ord 1 |

Both are `provenance_class: extension` in the override map (the R6 convention: recorded so
the next re-build does not knowingly re-create the same scope difference; not R17-sampled;
each verified against the section's verbatim chunk evidence on the live R16 substrate).

## Note-level adjudications (both STANDING — zero resolution-file amendments this round)

- **converting-between-fdp** (`spcpt_8MpvS5pnYkf9QswF`): THE NOTE-LEVEL JOIN TO 1.2G
  STANDS (ords 5/6 forward-conversion sections; ord 0 heading-only class; the
  inverse-direction sections re-home section-by-section via the override map).
- **basic-angle-properties** (`spcpt_5FMXZMjqSZ3GK53q`): THE NOTE-LEVEL JOIN TO 4.1B
  STANDS (ords 0/2/3 property sections; ord 4 the R1 4.2B ruling; the labeling primer
  DEMOTEs section-level).

Because there are ZERO id-level rows and ZERO note-level re-points, the resolution file is
**byte-untouched** this round (counts stay 222/214/8; last writer remains R14) — the R14
apply surface does not exist here; the round's entire state carrier is the override map
`scripts/c42_section_overrides_r18.yaml` (schema `c42-r20-section-overrides/1.0`, the
consuming-lane convention), derived deterministically from the verdict record by
`scripts/c42_r18_override_projection.py`. Wiring the R18 map into the c40 tool is the
re-build lane's job (the R12/R16 precedent). No prior-round entries are subsumed (the only
entries touching these notes are different-ordinal standing rulings: R1
basic-angle-properties::4 -> 4.2B, R10 converting-between-fdp::1 -> 1.6C).

## Heading-only class (standing convention, no new decision)

The 8 fresh H3 HOLD rows on the R17 sheet ride `c42-heading-only-convention-1` with no R18
action (they are NOT part of the 2-row inventory). The draw variance 4 -> 8 rows between
R13 and R17 is structural (each re-gate re-seeds) — the durable-PASS question it raises is
menu option (b), the operator's call, never assumed. CONTINUITY, mechanically grounded in
the R17 fill's own source-base convention (the H2 index is built from PRIOR re-gate
records only): three of the eight now carry R17-fresh CONTENT-row CONFIRMs of the same
note+code and resolve via H2 at the next re-gate's ladder replay — standard-form ord 0
(1.9A; R17 rows 0211af0e0b8a806d + d7339b416c53ba5e), classifying-stationary-points ord 0
(3.4C; row 59aec49753b23112), working-with-vectors ord 0 (5.1F; row 7b279735e8877e9e);
the other five stay H3 until evidence accumulates. H3 rows still ride R5 only with the
operator's explicit per-row sign-off.

## Residual

The C32 §3 residual (`spcpt_QWXhzVp2S3VYZdZc`) re-affirmed **KEPT UNRESOLVED** — the
PDF-verified reason stands; unchanged from the R1 adjudication (re-affirmed at R6, R10,
R14); the R17 Part B carried it DEFER and nothing in the R17 inventory touches it.

## Gate arithmetic (recorded, not claimed)

The R17 menu's projection (exact stratum 86/94 = 91.5% on this draw's composition) is
recorded but NOT claimed as a gate outcome: every re-gate re-seeds (the R13 -> R17
falsification precedent — a projection was verified against a re-seeded draw and failed on
the H3 variance plus fresh rejects). The gate outcome is whatever the next re-gate
(R21-shaped, fired only by explicit operator instruction) actually computes. R5 (§18
substrate apply, operator gate 3) is NOT armed by anything here.

## Audit

`scripts/c42_r18_repair_check.py` -> `graph/reports/C42_R18_REPAIR_CHECK.json`, A1–A10:

- **A1** inventory agreement (2 REJECT rows, 0 id-level — verified not assumed; R17 record pins)
- **A2** projection agreement (4 entries: 2 verdicted + 2 census-remark extensions; 2
  STANDING rulings; convention; residual; no subsumed entries)
- **A3** code domain (188 members; Foundation bare-id; DEMOTE null; currents match the
  live substrate)
- **A4** wordings verbatim (1.3D / 1.6C) + ledger absence (1.2G / 4.1B not shared-tier)
- **A5** joins STAND + resolution byte-untouched vs `cf1d8ad` + sme_spcpt_verify green on
  the round's course surface (both maths-a tiers + chemistry; see the environment finding)
- **A6** substrate pins (4 mapping ids SUGGESTED at pinned codes) + the 8 H3 HOLD rows
- **A7** idempotency (projection + proposals byte-identical re-runs)
- **A8/A10** footprint + commit state (delta vs `cf1d8ad` within the declared footprint)
- **A9** round artifacts (proposals surfaces 0/2/8 + standing convention record pinned)

ALL PASS exit 0 (pre-commit run; re-run post-commit for the committed-clean form).

## Environment finding (recorded, not repaired — the R0 pattern)

This session's full SME-ExamQuestion materialization (the workspace had lost it under the
sparse checkout) let the standing sme_spcpt_verify.py sweep the accounting pair for the
first time in the C42 loop, exposing **53 G1/G2 failures** (igcse-accounting-17-financial-
statements x6 + igcse-accounting-17-introduction-to-bookkeeping-and-accounting x47:
'foreign code' / 'resolution code not in registry' on S4.069/S4.070/S4.071-class ids) —
the T-KG-13 2026-09-24 accounting dedup rebuilt parsed/igcse-accounting/spec_points.json
while the 2026-09-19 T-SPEC-7 sidecars still reference the pre-dedup id family. The
accounting inputs are byte-identical `a5c5b71 -> HEAD` (verified in the audit), so the
failure predates every C42 round; earlier C7-class greens ran under an incomplete EQ
materialization that never swept the accounting dirs. Census item for a separate operator
decision; the R18 footprint never touches the EQ/parse space.

## Scope guards

Chemistry, parsed canonical bundles, the Lane C stores, spec-links/**, the C25–C41
records, the C42 scope + R0–R17 records and the C30 ledger byte-untouched (A8/A10: the
delta vs `cf1d8ad` is within the declared footprint).

## Footprint

`scripts/c42_r18_{repair_proposals.py, repair_verdicts.yaml, override_projection.py,
repair_check.py}` + `scripts/c42_section_overrides_r18.yaml` +
`graph/reports/C42_{R18_REPAIR_PROPOSALS.json, R18_RESOLUTION_REPAIR_RECORD.md,
R18_REPAIR_CHECK.json}` — nothing else.

## Next operator gates

R19+R20 (join re-run + substrate re-build consuming the R18 map, the DEMOTE and the
extension rows), then the R21 re-gate (operator gate 2 re-run) — each fired only by
explicit operator instruction; R5 (§18 substrate apply, operator gate 3) stays the
operator's choice and is NOT armed by anything here. Menu options (b) (heading-only
convention amendment), (c) (fire R5 on confirmed rows) and (d) (accept and re-scope)
remain open, the operator's call.
