# C42 R37 — Substrate Re-build consuming BOTH R36 carriers — igcse-maths-a

**Generated:** 2026-10-16T13:53:44+00:00  |  **Baseline:** `936e6c11adff`
**Operator directive:** "fire R37 -> R38" (2026-10-16, zai-web (gateway trace 1a144e6357d603d9)).
The directive fired the R36 record's NEXT lanes in order: this re-build, then
the R38 validation re-gate (fired separately).

## What this is

The FOURTH substrate re-build consuming a promotions AMENDMENT — and the
FIRST consuming an EXCLUSION-ONLY one, and the second consecutive with NO
tool-version move: the amended c40 tool (scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0 —
the R36 carriers' own contract) re-emits the store ALL-SUGGESTED consuming
the TEN operator override maps (R1 + R6 + R10 + R14 + R18 + R22 + R26 + R30
+ R33 + **R36**, the new one, schema `c42-r28-section-overrides/1.0`), and
the R5 promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED FOUR TIMES OVER**:
`scripts/c42_r36_promotions_amendment.yaml` (schema
`c42-r31-promotions-amendment/1.0`, the loop's FOURTH
promotions-affecting repair record and the FIRST exclusion-ONLY): the
DEMOTE row is EXCLUDED from the re-applied set (it lands unresolved-span via
the c40 DEMOTE convention, chunk identity intact — the W3 invariant), ZERO
supersedes and ZERO additions (the R30 additions mechanism present and
UNUSED — no sign-offs owed). The re-applied count **831 -> 830** (827 from
the R5 chain [832 - 1 R26 - 3 R30 - 1 R36 exclusions] + 3 R30-added
sign-offs, the 3 R33 movers re-pinned at 1.8D) — the FIRST re-application
that NARROWS the promoted surface.

## The DEMOTE landing (from the R36 map, fail-closed)

- `4MA1-1.6F` -> worklist — basic-percentages ord 4
  (mapping_id `a107f5041769fdd9` -> `8254a7fc75ad2946` = the projected re-key
  `sha16("demoted|<note_path>|4")`, verified live; the loop's
  SIXTH DEMOTE, single-row batch over a promoted row). The row lands
  unresolved-span with the round-tagged `worklist_reason` + `disposition`
  (the operator-round descriptor `C42 R36 (surface 3: ...` parsing under
  the DEMOTE handler's regex, the R16 discipline), RECORDED never forced,
  the worklist's demote-landed class deepening 7 -> 8.

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **133 -> 133** (UNCHANGED: 1.6F keeps its coverage via the
reverse-percentages trio + basic-percentages ords 0/3 — the demoted row's
code keeps its dedicated note's trio; gained `[]`, lost `[]`), uncovered-SP
**55 -> 55**; rows **917 -> 917**; anchored **835 -> 834**; unresolved-span
**27 -> 28**. Per-code: 4MA1-1.6F anchored **6 -> 5**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5, NO
  version move): the R36 map consumed fail-closed (1 verdicted
  DEMOTE_TO_WORKLIST, override_code null per the R8 rule, current_code ==
  join-derived) + the FOUR R26 STANDING pins verified in-generator
  (unchanged) + coverage recomputed (gained/lost computed, never assumed).
- `scripts/c42_r37_substrate_rebuild.py@1.0.0` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R35 ALL PASS 10/10 with its
  store sha pin == the baseline blob + R36 ALL PASS 9/9 + the promotions
  file sha == the R5 record's pin == the amendment's base pin), G7
  determinism, the delta proofs (chunk-identity multiset identical — the W3
  invariant; every surviving row BYTE-IDENTICAL — no tool churn; no
  DEFER-row vanish; meta delta == stage + the 2 moving census keys +
  promoted_rows + the 4 additive re-dated promotion_reapplied* fields),
  the amendment pre-apply integrity (pinned_code verified against the R5
  file BEFORE the amendment applies — any drift fails the rebuild; ALL
  FOUR amendments), the 830-row re-application (827 chained through
  R36-exclusion+R33+R30+R26 + 3 R30-added byte-stable), the row-set
  arithmetic, the meta delta assertion, G4-at-apply over every chunk row,
  the anti-forgery sweep, and CI parity (graph_check census identical
  pre/post; kg golden GREEN).
- `scripts/c42_r37_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R34 state) | Post (R37) |
|---|---|---|
| rows | 917 | 917 (the DEMOTE re-keys into the worklist) |
| HUMAN_VALIDATED | 831 | 830 (the R36 exclusion narrows the surface) |
| anchored SUGGESTED | 4 (3 REJECT + 1 re-homed hold) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 27 | 28 (the R36 DEMOTE) |
| uncovered-SP worklist | 55 | 55 |
| covered codes | 133/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `9174915650d49f4a` |
| store (post) | `8d8474c59ca6341f` |
| `c42_section_overrides_r36.yaml` | `b35b2403c43ebfc2` |
| `c42_r36_promotions_amendment.yaml` | `4d871d3089290b60` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `9bad739bd79e5899` |

## Open operator decisions (untouched by this lane)

- the R38 validation re-gate — sanctioned by the directive's "→ R38" clause,
  fired as its own round

