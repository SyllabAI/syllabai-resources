# C42 R40 — Substrate Re-build consuming BOTH R39 carriers — igcse-maths-a

**Generated:** 2026-10-16T17:33:03+00:00  |  **Baseline:** `ad12bc9d92ff`
**Operator directive:** "fire R39/R40" (2026-10-16, zai-web (gateway trace 1a145a7c26a0d4e5)).
The directive fired the R39 record's NEXT lane: this re-build (the store
move the R39 round deferred). The next validation re-gate is NOT named by
the directive — the operator's call, explicit instruction only.

## What this is

The FIFTH substrate re-build consuming a promotions AMENDMENT — and the
SECOND consuming an EXCLUSION-ONLY one, and the third consecutive with NO
tool-version move: the amended c40 tool (scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0)
re-emits the store ALL-SUGGESTED consuming the ELEVEN operator override
maps (R1 + R6 + R10 + R14 + R18 + R22 + R26 + R30 + R33 + R36 + **R39**,
the new one, schema `c42-r28-section-overrides/1.0`), and the R5
promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED FIVE TIMES OVER**:
`scripts/c42_r39_promotions_amendment.yaml` (schema
`c42-r31-promotions-amendment/1.0`, the loop's FIFTH
promotions-affecting repair record and the SECOND exclusion-ONLY): the 2
DEMOTE rows are EXCLUDED from the re-applied set (they land
unresolved-span via the c40 DEMOTE convention, chunk identity intact —
the W3 invariant), ZERO supersedes and ZERO additions (the R30 additions
mechanism present and UNUSED — no sign-offs owed). The re-applied count
**830 -> 828** (825 from the R5 chain [832 - 1 R26 - 3 R30 - 1 R36 - 2
R39 exclusions] + 3 R30-added sign-offs, the 3 R33 movers re-pinned at
1.8D) — the SECOND re-application that NARROWS the promoted surface.

## The DEMOTE landings (from the R39 map, fail-closed — the loop's FIRST 2-row batch)

- `4MA1-6.3A` -> worklist — basic-probability ord 1
  (mapping_id `a5b737e510606829` -> `09f012e4cabef0cc` = the projected
  re-key `sha16("demoted|<note_path>|1")`, verified live;
  the loop's SEVENTH DEMOTE).
- `4MA1-6.2B` -> worklist — calculations-with-the-mean ord 1
  (mapping_id `d545cd5f5aeae9a9` -> `80d783fb13def4e2` = the projected
  re-key, verified live; the loop's EIGHTH DEMOTE).

Both rows land unresolved-span with the round-tagged `worklist_reason` +
`disposition` (the operator-round descriptor `C42 R39 (surface 3: ...`
parsing under the DEMOTE handler's regex, the R16 discipline), RECORDED
never forced, the worklist's demote-landed class deepening 8 -> 10. The
LANDED R36 exclusion re-applies via the still-wired R36 map (the demoted
row re-lands at the same re-key `8254a7fc75ad2946`).

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **133 -> 133** (UNCHANGED: 6.3A keeps 17 anchored rows via the
tree-diagrams quartet + the combined/conditional 8 + basic-probability
ords 0/2/3/4/5; 6.2B keeps 23; gained `[]`, lost `[]`), uncovered-SP
**55 -> 55**; rows **917 -> 917**; anchored **834 -> 832**;
unresolved-span **28 -> 30**. Per-code: 4MA1-6.3A anchored **18 -> 17**;
4MA1-6.2B anchored **24 -> 23**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5, NO
  version move): the R39 map consumed fail-closed (2 verdicted
  DEMOTE_TO_WORKLISTs, override_code null per the R8 rule, current_code ==
  join-derived) + the FOUR R26 STANDING pins verified in-generator
  (unchanged) + coverage recomputed (gained/lost computed, never assumed).
- `scripts/c42_r40_substrate_rebuild.py@1.0.0` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R38 ALL PASS 10/10 with its
  store sha pin == the baseline blob + R39 ALL PASS 9/9 + the promotions
  file sha == the R5 record's pin == the amendment's base pin), G7
  determinism, the delta proofs (chunk-identity multiset identical — the W3
  invariant; every surviving row BYTE-IDENTICAL — no tool churn; no
  DEFER-row vanish; meta delta == stage + the 2 moving census keys +
  promoted_rows + the 4 additive re-dated promotion_reapplied* fields),
  the amendment pre-apply integrity (pinned_code verified against the R5
  file BEFORE the amendment applies — any drift fails the rebuild; ALL
  FIVE amendments), the 828-row re-application (825 chained through
  R39-exclusion+R36-exclusion+R33+R30+R26 + 3 R30-added byte-stable), the
  row-set arithmetic, the meta delta assertion, G4-at-apply over every
  chunk row, the anti-forgery sweep, and CI parity (graph_check census
  identical pre/post; kg golden GREEN).
- `scripts/c42_r40_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R37 state) | Post (R40) |
|---|---|---|
| rows | 917 | 917 (the DEMOTE batch re-keys into the worklist) |
| HUMAN_VALIDATED | 830 | 828 (the R39 exclusions narrow the surface) |
| anchored SUGGESTED | 4 (3 REJECT + 1 re-homed hold) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 28 | 30 (the R39 DEMOTE batch) |
| uncovered-SP worklist | 55 | 55 |
| covered codes | 133/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `8d8474c59ca6341f` |
| store (post) | `14d04dfebb71b849` |
| `c42_section_overrides_r39.yaml` | `a6c9bf11028e6325` |
| `c42_r39_promotions_amendment.yaml` | `2bf4cb7240bffa14` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `9bad739bd79e5899` |

## Open operator decisions (untouched by this lane)

- the next validation re-gate (R41-shaped) — NOT named by the directive;
  the operator's call, explicit instruction only

