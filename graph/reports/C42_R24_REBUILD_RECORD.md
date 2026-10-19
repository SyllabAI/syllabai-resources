# C42 R24 — Substrate Re-build + Promotions Re-application — igcse-maths-a

**Generated:** 2026-10-04T08:30:44+00:00  |  **Baseline:** `61334637b894`
**Operator directive:** "R24" (2026-10-04, discord (gateway trace 44ed8bf6a3f36790164951e2f79c451b)). The directive
names exactly the R22 record's next-decision gate; **the R25 re-gate is NOT
fired**.

## What this is

The first substrate re-build UNDER a promoted surface (the R24 novelty): the
amended c40 tool (scripts/c40_maths_a_chunk_sp_substrate.py@2.5.0 — the R16→R20 rebuild-lane version
convention) re-emits the store ALL-SUGGESTED consuming the SIX operator
override maps (R1 + R6 + R10 + R14 + R18 + **R22**, the new one), and the R5
promotions file (832 exact row identities) is re-applied byte-stably. The 3
R22 override rows stayed SUGGESTED at R5, so the promotion set is identity-
and code-stable under the re-attributions (verified, not assumed). Every
surviving row differs from the baseline ONLY in `provenance.tool`
(@2.4.0 → @2.5.0) — the store records its builder honestly.

## The three re-attributions (from the R22 map, fail-closed)

- `4MA1-2.2F` -> `4MA1-2.2B` — difference-of-two-squares ord 3 (mapping_id eb26022693be3948 -> 9af27c9ae0133ad8)
- `4MA1-2.6B` -> `4MA1-3.3E` — graphical-solutions ord 1 (mapping_id 5fd48f084383be11 -> 83e7238929d00f56)
- `4MA1-4.8D` -> `4MA1-4.8F` — 3d-pythagoras-and-trigonometry ord 4 (mapping_id a8d23b11c343a3bd -> 430c0f1c124a4732)

## DC-R24-01 — the R22 coverage projection, corrected

The R22 map asserted "coverage STATIONARY 129/188 (all three targets already
covered)" **without computing it**. True for 3.3E (2 rows) and 2.2B (10
rows); FALSE for **4.8F — it carried ZERO anchored rows**. The actual
landing is a coverage GAIN (the R12/R16/R20 precedent shape): covered
**129 → 130**, gained `['4MA1-4.8F']`, lost `[]`; the 4MA1-4.8F uncovered-SP
DEFER row resolves into an anchored row; rows **921 → 920**; anchored 839 /
unresolved-span 23 unchanged (zero row-census movement among chunk rows —
no DEMOTEs). Recorded per P5; the R22 records stay byte-untouched; the
re-attribution substance is unaffected.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.5.0 (amended per P5): the
  R22 map consumed fail-closed (3 verdicted REATTRIBUTEs, targets ratified,
  current_code == join-derived) + the THREE R22 STANDING pins verified
  in-generator (list-shaped adjudications, the R23 precedent) + coverage
  recomputed (gained/lost computed, never assumed).
- `scripts/c42_r24_substrate_rebuild.py@1.0.0` (this lane): pre-state pins, map contract, promotions
  authority chain (R21 regate all_pass + the promotions file sha == the R5
  record's pin), G7 determinism, the delta proofs (chunk-identity multiset
  identical; tool-string-only churn elsewhere; the DEFER-row vanish shape;
  meta delta == stage+tool), the 832-row byte-stable re-application, the
  row-set arithmetic, G4-at-apply over every chunk row, the anti-forgery
  sweep, and CI parity (graph_check census identical pre/post; kg golden
  GREEN).
- `scripts/c42_r24_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R5 state) | Post (R24) |
|---|---|---|
| rows | 921 | 920 |
| HUMAN_VALIDATED | 832 | 832 (re-applied byte-stably) |
| anchored SUGGESTED | 7 (3 REJECT + 4 HOLD) | 7 (3 re-attributed + 4 HOLD) |
| unresolved-span worklist | 23 | 23 |
| uncovered-SP worklist | 59 | 58 (4.8F resolved) |
| covered codes | 129/188 | 130/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `1cbb9c87fc1be7bf` |
| store (post) | `ac37a91b9b657ef6` |
| `c42_section_overrides_r22.yaml` | `b969627a811f7986` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `9bad739bd79e5899` |

## Open operator decisions (untouched by this lane)

- the R25 re-gate (explicit instruction only)
- the 4 H3 HOLD rows (per-row sign-off owed: 1.7B / 6.3J / 3.3F / 2.2C)
- the ord-3 promoted-surface extension candidate (3d-pythagoras SOHCAHTOA-3D)

