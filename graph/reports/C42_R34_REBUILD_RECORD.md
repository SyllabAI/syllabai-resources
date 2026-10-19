# C42 R34 — Substrate Re-build consuming BOTH R33 carriers — igcse-maths-a

**Generated:** 2026-10-16T08:07:22+00:00  |  **Baseline:** `9cd386c12aac`
**Operator directive:** "fire R34 -> R35" (2026-10-16, zai-web (gateway trace 1a1439559c9023f1)).
The directive fired the R33 record's NEXT lanes in order: this re-build, then
the R35 validation re-gate (fired separately).

## What this is

The THIRD substrate re-build consuming a promotions AMENDMENT — and the
FIRST consuming a SUPERSEDES-ONLY one, and the first with NO tool-version
move: the amended c40 tool (scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0 — the R33
carriers' own contract) re-emits the store ALL-SUGGESTED consuming the NINE
operator override maps (R1 + R6 + R10 + R14 + R18 + R22 + R26 + R30 +
**R33**, the new one, schema `c42-r28-section-overrides/1.0`), and the R5
promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED THRICE OVER**: `scripts/c42_r33_promotions_amendment.yaml`
(schema `c42-r31-promotions-amendment/1.0`, the loop's THIRD
promotions-affecting repair record and the FIRST supersedes-ONLY): the 3
REATTRIBUTE rows REMAIN in the promoted set at their amended codes
(re-keyed old->new per the R24 id_pairs convention), ZERO exclusions and
ZERO additions (the R30 additions mechanism present and UNUSED — no
sign-offs owed). The re-applied count stays **831** (828 from the R5 chain
+ 3 R30-added sign-offs, the 3 R33 movers re-pinned within the set).

## The three re-attributions (from the R33 map, fail-closed)

- `4MA1-1.8B` -> `4MA1-1.8D` — rounding-and-estimation ord 6 (mapping_id a7c0585948a3e06e -> 8f22e1623c025e18; promotion re-pinned to `4MA1-1.8D`)
- `4MA1-1.8B` -> `4MA1-1.8D` — rounding-and-estimation ord 7 (mapping_id b5c13a3e2908b8d1 -> bb44385407a47188; promotion re-pinned to `4MA1-1.8D`)
- `4MA1-1.8B` -> `4MA1-1.8D` — rounding-and-estimation ord 8 (mapping_id 7169cc1735d43642 -> 68c165d51b56047a; promotion re-pinned to `4MA1-1.8D`)

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **133 → 133** (UNCHANGED: 1.8B keeps its coverage via the rounding
half — ords 0-5 — and 1.8D is already covered via the R10
related-calculations STANDING join; gained `[]`, lost `[]`), uncovered-SP
**55 → 55**; rows **917 → 917**; anchored **835 → 835**; unresolved-span
**27 → 27**. Per-code: 1.8B anchored **9 → 6**, 1.8D anchored **3 → 6**
(the loop's FIRST SPLIT-note scoping landed row-level).

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5, NO
  version move): the R33 map consumed fail-closed (3 verdicted
  REATTRIBUTEs, targets ratified, current_code == join-derived) + the FOUR
  R26 STANDING pins verified in-generator (unchanged) + coverage recomputed
  (gained/lost computed, never assumed).
- `scripts/c42_r34_substrate_rebuild.py@1.0.0` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R32 ALL PASS 10/10 with its
  store sha pin == the baseline blob + R33 ALL PASS 9/9 + the promotions
  file sha == the R5 record's pin == the amendment's base pin), G7
  determinism, the delta proofs (chunk-identity multiset identical; every
  surviving row BYTE-IDENTICAL — no tool churn; no DEFER-row vanish; meta
  delta == stage + the 4 additive re-dated promotion_reapplied* fields),
  the amendment pre-apply integrity (pinned_code verified against the R5
  file BEFORE the amendment applies — any drift fails the rebuild; ALL
  THREE amendments), the 831-row re-application (828 chained through
  R33+R30+R26 + 3 R30-added byte-stable), the row-set arithmetic, the meta
  delta assertion, G4-at-apply over every chunk row, the anti-forgery
  sweep, and CI parity (graph_check census identical pre/post; kg golden
  GREEN).
- `scripts/c42_r34_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R31 state) | Post (R34) |
|---|---|---|
| rows | 917 | 917 |
| HUMAN_VALIDATED | 831 | 831 (re-pinned: ords 6/7/8 now at 1.8D) |
| anchored SUGGESTED | 4 (3 REJECT + 1 re-homed hold) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 27 | 27 |
| uncovered-SP worklist | 55 | 55 |
| covered codes | 133/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `4aeb73e1575f9586` |
| store (post) | `9174915650d49f4a` |
| `c42_section_overrides_r33.yaml` | `c4bdea37bb331ef1` |
| `c42_r33_promotions_amendment.yaml` | `d50bf35a180e495f` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `9bad739bd79e5899` |

## Open operator decisions (untouched by this lane)

- the R35 validation re-gate — sanctioned by the directive's "→ R35" clause,
  fired as its own round

