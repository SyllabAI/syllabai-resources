# C42 R28 — Substrate Re-build consuming BOTH R26 carriers — igcse-maths-a

**Generated:** 2026-10-04T12:38:57+00:00  |  **Baseline:** `11c2fc492991`
**Operator directive:** "R27 join re-run + R28 rebuild consuming both carriers" (2026-10-04, zai-web (gateway trace 1a106d1aa121ab59)).
The directive names exactly the R26 record's next-decision menu option (a);
**the R29 re-gate is NOT fired**.

## What this is

The first substrate re-build consuming a promotions AMENDMENT (the R26
novelty): the amended c40 tool (scripts/c40_maths_a_chunk_sp_substrate.py@2.6.0 — the R16→R20→R24
rebuild-lane version convention) re-emits the store ALL-SUGGESTED consuming
the SEVEN operator override maps (R1 + R6 + R10 + R14 + R18 + R22 +
**R26**, the new one, schema `c42-r28-section-overrides/1.0`), and the R5
promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED** by `scripts/c42_r26_promotions_amendment.yaml`
(schema `c42-r28-promotions-amendment/1.0`, the loop's FIRST
promotions-affecting repair record): the 3 REATTRIBUTE rows REMAIN in the
promoted set at their amended codes (re-keyed old→new), the DEMOTE row LEAVES
it (832 → 831) and lands unresolved-span. Every applied block is byte-stable
against both the R5 tool shape and the baseline store's block.

## The three re-attributions + the DEMOTE (from the R26 map, fail-closed)

- `4MA1-1.1G` -> `4MA1-1.1A` — types-of-number ord 1 (mapping_id 81c0b59852d5d4b6 -> 5feaf8109168ae1e; promotion re-pinned to `4MA1-1.1A`)
- `4MA1-3.3F` -> `4MA1-3.3H` — drawing-straight-line-graphs ord 4 (mapping_id e6ed72481e8ffc2e -> 9bd8237d3ec17e43; promotion re-pinned to `4MA1-3.3H`)
- `4MA1-5.1D` -> `4MA1-5.1C` — introduction-to-vectors ord 3 (mapping_id 7fdded0b9245e1c3 -> 19a8724ce211a3b3; promotion re-pinned to `4MA1-5.1C`)
- `4MA1-2.2F` -> unresolved-span — factorising-by-grouping ord
  2 (mapping_id 70f0b027f3f1528f ->
  55bb31c2ad1c8258; the loop's fourth DEMOTE and the FIRST of a PROMOTED row;
  its promotion is EXCLUDED by the amendment — the status change
  HUMAN_VALIDATED → SUGGESTED is enumerated and recorded)

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **130 → 132** (gained `['4MA1-1.1A', '4MA1-5.1C']` — both DEFER rows
`da25da48e0be5c64` / `2332964a4f1b02ca` resolving into anchored rows, the
R12/R16/R20/R24 coverage-gain precedent), lost `[]` (1.1G keeps 7, 5.1D keeps
4, 3.3F keeps 6, 2.2F keeps 17 — verified row-by-row at R26); uncovered-SP
**58 → 56**; rows **920 → 918**; anchored **839 → 838**; unresolved-span
**23 → 24**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.6.0 (amended per P5): the
  R26 map consumed fail-closed (3 verdicted REATTRIBUTEs + 1 DEMOTE, targets
  ratified, current_code == join-derived) + the FOUR R26 STANDING pins
  verified in-generator (list-shaped adjudications, the R24 R22-pins
  precedent) + coverage recomputed (gained/lost computed, never assumed).
- `scripts/c42_r28_substrate_rebuild.py@1.0.0` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R25 all_pass 13/13 + R26 ALL
  PASS 9/9 + the promotions file sha == the R5 record's pin == the
  amendment's base pin), G7 determinism, the delta proofs (chunk-identity
  multiset identical; tool-string-only churn elsewhere; the DEFER-row vanish
  shape; meta delta == stage+tool+census keys), the amendment pre-apply
  integrity (pinned_code verified against the R5 file BEFORE the amendment
  applies — any drift fails the rebuild), the 831-row byte-stable
  re-application with the 3 supersedes re-keyed, the row-set arithmetic,
  G4-at-apply over every chunk row, the anti-forgery sweep, and CI parity
  (graph_check census identical pre/post; kg golden GREEN).
- `scripts/c42_r28_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R26 state) | Post (R28) |
|---|---|---|
| rows | 920 | 918 |
| HUMAN_VALIDATED | 832 | 831 (re-applied AMENDED byte-stably) |
| anchored SUGGESTED | 7 (3 REJECT + 4 HOLD) | 7 (3 REJECT + 4 HOLD) |
| unresolved-span worklist | 23 | 24 (the DEMOTE row lands) |
| uncovered-SP worklist | 58 | 56 (1.1A + 5.1C resolved) |
| covered codes | 130/188 | 132/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `ac37a91b9b657ef6` |
| store (post) | `1b667c0107dfc85c` |
| `c42_section_overrides_r26.yaml` | `80f562ad0a72f7d4` |
| `c42_r26_promotions_amendment.yaml` | `fda9d717d9f58572` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `9bad739bd79e5899` |

## Open operator decisions (untouched by this lane)

- the R29 re-gate (explicit instruction only)
- the 4 H3 HOLD rows (per-row sign-off owed: 1.7B / 6.3J / 3.3F / 2.2C)
- the ord-3 promoted-surface extension candidate (3d-pythagoras SOHCAHTOA-3D)
- the promoted-surface same-class candidates (grouping ords 0/1/3, drawing
  ord 5, vectors ord 4) + the rational/irrational corpus gap — operator
  census remarks per the R26 record

