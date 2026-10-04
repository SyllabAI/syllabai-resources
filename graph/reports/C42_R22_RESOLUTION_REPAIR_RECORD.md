# C42 R22 — R1-SHAPED REPAIR ROUND over the R21 3-row defect inventory (round record)

**Date:** 2026-10-04 | **Directive:** "R1 shaped repair" (2026-10-04, discord, gateway trace f63adc3fd5ac8155cf81200804acb165)
**Round:** R22 — the sixth R1-shaped repair round of the C42 K2-B rework loop (scope §7)
**Reviewer:** Super Z (GLM agent), operator-delegate under the fired R22 directive; the human
operator retains final sign-off; per the anti-forgery rule nothing here flips the store — the
R5-promoted 832-row HUMAN_VALIDATED surface is OUT OF SCOPE for this round
**Baseline:** `df7a6c1` (the R5-closed HEAD: the §18 apply + its audit re-run)

## What fired

The R21 re-gate (operator gate 2 re-run, the loop's fifth pass) closed **PASS** — exact
87/94 = 92.5% / partial 238/238 = 100% / none 132/132 = 100%, Part B 82/82 decided,
mechanical 464/464, X1–X13 all 13/13 — and the operator fired R5 (the §18 substrate apply,
operator gate 3): **832 anchored rows HUMAN_VALIDATED** (resources `2e90f52` + audit
`df7a6c1`), with the honest residue returned to the operator per scope §7: 3 REJECT rows +
4 H3 HOLD rows. The operator's directive names exactly the repair round over that inventory —
the R21 fill record's own disposition ("the fresh defect inventory returns to the operator").
Lane numbering follows the loop's iteration precedent (R6–R9, R10–R13, R14–R17, R18–R21)
with **R5 now consumed by the §18 apply**: this round is **R22**; the next natural lanes are
the join re-run (R23), the substrate re-build consuming this round's map (R24) and the
re-gate (R25); the deterministic follow-ons fire only on explicit operator instruction —
the directive named the repair round alone. The 4 H3 HOLD rows stay SUGGESTED (the per-row
operator sign-off the R21 disposition requires was NOT given with the directive).

## The 3-row inventory (R21 fresh verdicts, scripts/c42_r21_fresh_verdicts.yaml)

All three are section-level scope differences WITH canonical targets — the cleanest repair
round of the loop: **3 verdicted REATTRIBUTEs, 0 DEMOTEs, 0 RETAINs, 0 id-level rows,
0 extension entries, 0 resolution amendments**, coverage STATIONARY 129/188.

| # | Row | Code | Root class | R22 disposition |
|---|---|---|---|---|
| 1 | `a8d23b11c343a3bd` — 3d-pythagoras-and-trigonometry ord 4 "How do I find the angle between a line and a plane?" | 4MA1-4.8D | adjacent-surface scope difference WITH a canonical target | **REATTRIBUTE 4.8D -> 4.8F** |
| 2 | `eb26022693be3948` — difference-of-two-squares ord 3 "How can the difference of two squares be made harder?" | 4MA1-2.2F | limit-scope difference WITH a canonical target | **REATTRIBUTE 2.2F -> 2.2B** |
| 3 | `5fd48f084383be11` — graphical-solutions ord 1 "How do I find the coordinates of points of intersection?" | 4MA1-2.6B | adjacent-surface scope difference WITH a canonical target | **REATTRIBUTE 2.6B -> 3.3E** |

### Row 1 — REATTRIBUTE 4.8D -> 4.8F

The section teaches finding the ANGLE BETWEEN A LINE AND A PLANE (identify the plane, draw
the line, form a right-angled triangle whose height is perpendicular to the plane, use
SOHCAHTOA) — no Pythagoras anywhere, the method is trigonometric end to end. 4.8F's Higher
demand is 'apply trigonometrical methods to solve problems in three dimensions, **including
finding the angle between a line and a plane**' — the including-clause names this exact task
VERBATIM in the store's operative wording. Not a tier artifact: 4.8D and 4.8F are BOTH
absent from the C30 ledger (verified — Higher-only rows), 4.8F a distinct ratified row. The
note-level join to 4.8D STANDS via the note's Pythagoras sections (ord 0 CONFIRMed at R4,
ord 1 at R13 and R17, ord 2 the 3D Pythagoras formula verbatim, ord 5 CONFIRMed at R13).

### Row 2 — REATTRIBUTE 2.2F -> 2.2B

The section teaches the difference of two squares made HARDER — squared variables 4m² − 9n²,
OTHER POWERS r⁸ − t⁶, repeated DOTS to fully factorise a⁴ − b⁴, common factor first 2x² − 18
— and r⁸ − t⁶ / a⁴ − b⁴ are NOT quadratic expressions, while 2.2F's demand is explicitly
capped '(limited to x² + bx + c)'. The un-limited canonical surface EXISTS: **2.2B**, whose
C30 ledger Higher-operative wording is 'understand the concept of a quadratic expression and
be able to factorise such expressions' WITHOUT the cap (ledger row verified verbatim:
higher_preferred, Foundation text 'collect like terms' — a distinct surface). Not a tier
artifact: 2.2F is absent from the ledger (Higher-only); the section rides 2.2B's HIGHER
surface (it is Higher-corpus content), not its Foundation surface. The note-level join to
2.2F STANDS via the within-limit basic DOTS sections (ord 1 CONFIRMed at R9 and R17; ord 2
the basic a² − b² factorisation rides the same within-limit surface).

### Row 3 — REATTRIBUTE 2.6B -> 3.3E

The section's worked instance is a LINEAR + NON-LINEAR pair (plot y = x² + 3x + 1 and
y = 2x + 1; they meet twice at (−1, −1) and (0, 1)) — **3.3E's Higher demand VERBATIM**
('find the intersection points of two graphs, one linear (y) and one non-linear (y), and
recognise that the solutions correspond'), while 2.6B's demand is 'interpret the equations
AS LINES and the common solution as the point of intersection' and the section's only
example is not a pair of lines. Tier facts PRECISELY stated (see DC-R22-01 below): 2.6B is
absent from the ledger (Higher-only); **3.3E is PRESENT as a shared-tier row** whose Higher
wording is the target demand verbatim and whose Foundation wording (midpoint coordinates)
is a different surface — the section rides 3.3E's Higher-operative surface and is not a
tier-variant artifact; the ledger presence STRENGTHENS the citation. The note-level join to
2.6B STANDS via the lines-based sections (ord 0 CONFIRMed at R13, ord 2 sampled fresh at
R21 — the two-lines surface verbatim, ord 3 CONFIRMed at R9).

## Convergence note (corroboration, not authority)

The deterministic proposals scorer (scripts/c42_r22_repair_proposals.py, PROPOSAL-ONLY)
ranks **exactly the three verdict targets as top-1s**: 3.3E @ 0.3125, 4.8F @ 0.2707,
2.2B @ 0.2355 — with the runner-ups all ≤ 0.197 noise rankings. Unlike the R14/R18
scorer-artifact cases, the scorer converged with the semantic adjudication this round;
recorded as corroboration only — the verdicts stand on the store wordings + ledger facts +
section content, not on the scorer.

## Census remarks (recorded, NOT adjudicated — the R6/R18 observation discipline)

- **3d-pythagoras ord 3 "How do I use SOHCAHTOA in 3D?"** (`75244f93401689fe`,
  HUMAN_VALIDATED on 4.8D via the R5 apply's gate-passed unsampled class): the section's
  verbatim content (cone base/slant-height ANGLE via SOHCAHTOA — a 3D angle task with no
  Pythagoras step) rides 4.8F's general clause at least as well as 4.8D's. This is the
  R6/R18 extension-row class EXCEPT the row sits on the R5-PROMOTED surface: an extension
  REATTRIBUTE would move a promoted row's code — an operator-level decision (the promotions
  file pins the row at 4.8D; no agent-side movement of promoted rows). **Not adjudicated
  this round** — the operator decides: (a) verdict a future round's extension with a
  promotions-file amendment, or (b) leave as-is (arguably dual-surface; the next re-gate's
  re-seeded draw will test it).
- **3d-pythagoras ord 5** (`14f9913db35b9db1`, HUMAN_VALIDATED; CONFIRMed at R13):
  genuinely mixed-surface (Pythagoras AND SOHCAHTOA; prism-angle example is 4.8F class,
  cuboid/pencil example is 4.8D class). The R13 CONFIRM STANDS — no re-adjudication
  without fresh sampled evidence; the dual-surface reading is on the record.
- **difference-of-two-squares ord 4** (`e7d416112d95b437`, HUMAN_VALIDATED, never sampled):
  expansion-strand content on a factorising note; no sampled evidence against the join and
  no inventory entry — left for the re-gate's draw; listed because the round censused the
  implicated notes in full.

## Dated correction DC-R22-01 (landed records never edited; corrections land as dated records)

The R21 fresh verdict note for `5fd48f084383be11` cites "2.6B and 3.3E are both absent from
the C30 ledger — Higher-only". The ledger fact: **2.6B IS absent** (as cited); **3.3E is
PRESENT** — ledger row official_code '3.3E', higher_preferred true, Higher text 'find the
intersection points of two graphs, one linear ( y ) and one non-linear ( y ), and and
recognise that the solutions correspond', Foundation text 'determine the coordinates of the
midpoint of a line segment, given the coordinates of the two end points'. The R21 ruling's
SUBSTANCE holds unchanged — not a tier artifact; 3.3E is a distinct ratified row whose
HIGHER wording is the target demand verbatim and the section is Higher-corpus content — and
the ledger presence strengthens rather than weakens the citation. The R21 records stay
byte-untouched; this dated record is the correction.

## Projections (computed here, land at the R24-shaped rebuild — never assumed at a gate)

- The 3 rows RE-ATTRIBUTE in place; **coverage STATIONARY 129/188** (all three targets are
  already covered — none is in the store's 59-code uncovered list; all three current codes
  keep coverage via their standing ords); anchored 839 and unresolved-span 23 unchanged
  (no DEMOTEs); the uncovered-SP worklist recomputes to the same 59 rows.
- The loop's first zero-census-movement repair round: only code attribution moves, and
  only on the 3 non-promoted rows. **The R5-promoted 832-row set is identity- and
  code-stable** under the three re-attributions (A6 asserts the empty intersection).
- Gate outcome is NOT projected or claimed: every re-gate re-seeds (the R13 → R17
  falsification precedent). What the R25-shaped re-gate computes is what it computes.

## The state carrier

`scripts/c42_section_overrides_r22.yaml` (schema **c42-r24-section-overrides/1.0**, the
consuming-lane convention: R1 map -> r3, R6 -> r8, R10 -> r12, R14 -> r16, R18 -> r20) —
3 verdicted REATTRIBUTE entries + the 3 note-level STANDING adjudications + the 4-H3
continuity block + the census remarks + DC-R22-01. Consumed fail-closed by the c40
substrate tool at the NEXT substrate re-build TOGETHER WITH the R1/R6/R10/R14/R18 maps —
wiring the map into the tool is the re-build lane's job (the R12/R16/R20 precedent).
**Promotions interaction (pinned in the map's contract):** the R24-shaped rebuild must
re-apply `scripts/c42_r5_promotions.yaml` to the rebuilt store (the c40 tool emits
all-SUGGESTED); the 3 R22 override rows are NOT in the promotions file, so the 832-entry
set carries over unchanged; the re-applied apply's round contract needs its census
re-pinned to the R24-era shape. Zero store bytes move from this round.

## Audit

`scripts/c42_r22_repair_check.py` -> `graph/reports/C42_R22_REPAIR_CHECK.json`, A1–A10:

- **A1** inventory agreement (3 REJECT rows, 0 id-level — verified not assumed; R21 record pins)
- **A2** projection agreement (3 verdicted REATTRIBUTEs, 0 extensions/DEMOTEs, 3 STANDING
  rulings, the 4 H3 rows listed, DC-R22-01, census remarks, no subsumed entries)
- **A3** code domain (188 members, distinct targets, currents match the live substrate,
  rows SUGGESTED)
- **A4** wordings verbatim (4.8F including-clause / 2.2B un-capped vs 2.2F cap / 3.3E
  linear+non-linear) + the ledger facts asserted (4 absent, 2 present with cited texts)
- **A5** joins STAND + resolution byte-untouched vs `df7a6c1` (git-read — see the
  environment finding)
- **A6** substrate pins (3 targets SUGGESTED; the promoted 832-row surface intersects the
  targets in NOTHING, promotions file included; the 4 H3 rows HOLD on the R21 record)
- **A7** idempotency (projection + proposals byte-identical re-runs)
- **A8/A10** footprint + commit state (delta vs `df7a6c1` within the declared footprint;
  post-commit the delta is empty and the check re-runs)
- **A9** round artifacts (proposals surfaces 0/3/4; the standing convention record pinned)

ALL PASS exit 0 (pre-commit run; re-run post-commit for the committed-clean form).

## Environment finding (recorded, not repaired — the R0 pattern)

This workspace materializes the repo under a sparse checkout (graph/ + scripts/ + the
maths-a notes corpus + the notes-join artifact) — the SME-ExamQuestion tree is NOT
materialized, so the standing `sme_spcpt_verify.py` sweep is NOT re-run this round (the
R18 check ran it with an EQ materialization and recorded the accounting G1/G2 failures as
a census item). The resolution file is asserted byte-identical via git blobs instead. The
R18-recorded accounting failures remain a separate operator census item, byte-unrelated to
this round's footprint.

## Scope guards

Chemistry, parsed canonical bundles, the Lane C stores, spec-links/**, the C25–C41 + R0–R21
records, the C30 ledger, the resolution file, the R5 apply artifacts (promotions file,
apply/check records) and the R5-promoted store surface byte-untouched (A8/A10: the delta vs
`df7a6c1` is within the declared footprint).

## Footprint

`scripts/c42_r22_{repair_proposals.py, repair_verdicts.yaml, override_projection.py,
repair_check.py}` + `scripts/c42_section_overrides_r22.yaml` +
`graph/reports/C42_{R22_REPAIR_PROPOSALS.json, R22_RESOLUTION_REPAIR_RECORD.md,
R22_REPAIR_CHECK.json}` — nothing else.

## Next operator gates

R23 (join re-run) + R24 (substrate re-build consuming the R22 map + re-applying the R5
promotions file), then the R25 re-gate (operator gate 2 re-run) — each fired only by
explicit operator instruction. The 4 H3 HOLD rows (1.7B / 6.3J / 3.3F / 2.2C) and the
ord-3 promoted-surface extension candidate await explicit operator decisions; nothing
self-fires.
