# C42 R42 — K2-B substrate RE-GATE fill record (operator gate 2 re-run evidence)

**Reviewer:** Super Z (GLM agent), acting as operator-delegate under the operator's 'fire R42' directive (2026-10-20, zai-web, gateway trace 1a156064469e2f41) — the R41 record's NEXT gate (the Task-25 receipt's open decision 1, recorded READY-TO-FIRE: the seed re-derives identically while the store sha16 14d04dfebb71b849 holds) fired verbatim; the human operator retains final sign-off; per the anti-forgery rule this re-gate VERIFIES the re-composed 828-row HUMAN_VALIDATED surface and never moves it
**Review date:** 2026-10-20
**Baseline:** 50883f51 (the T-SPECS-CIE-REJOIN-GATE-1 tip; the R40 substrate byte-identical through the R41 re-gate and the rejoin-gate lane, store sha16 14d04dfebb71b849)

## What this is

The loop's TWELFTH gate-2 pass — the FIRST STABILITY RE-VERIFICATION —
fired by the operator's explicit "fire R42" instruction. The same
re-seeded draw as R41 (the substrate unchanged since the R40 rebuild:
the seed re-derives identically while the store sha16 14d04dfebb71b849
holds — the Task-25 ready-to-fire condition), re-verified against the
R41 record as the new most-recent-record ladder head (917 rows; 832
anchored; 828 HUMAN_VALIDATED re-pinned 825 + 3 with the 3 R33 movers
at 1.8D and the R36+R39 DEMOTE rows excluded into the worklist; covered
133/188), under the standing convention: re-gates re-seed, the
R13→R17→R21→R25→R29→R32→R35→R38→R41 falsification precedent.

## Census

| Surface | Value |
|---|---|
| rows | 917 |
| anchored | 832 (828 HUMAN_VALIDATED + 4 SUGGESTED) |
| worklist | 85 (10 DEMOTE-landed + 57 residual + 18 cleared + 0 uncovered-SP) |
| covered codes | 133/188 |
| store sha16 | 14d04dfebb71b849 |

## Part A — the anchored draw

| Stratum | Rows in stratum | Sampled | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|---|
| exact | 462 | 93 | 91 | 0 | 2 | 97.8% |
| partial | 238 | 238 | 238 | 0 | 0 | 100.0% |
| none | 132 | 132 | 132 | 0 | 0 | 100.0% |
| **Total** | 832 | 463 | 461 | 0 | 2 | 99.6% |

**Gate result: PASS — every class at or above the 90% gate.**

## Verdict sources

- `r30-section-override`: 2
- `r41-carried`: 459
- `r41-carried-hold`: 2

## Tier signatures

- `LEDGER_FOUNDATION`: 48
- `STORE_HIGHER`: 415
— DIVERGENT 0 (the both-tier standing instruction: DIVERGENT fails the fill
closed).

## Part B — the worklist

- `cleared`: 18
- `demote`: 10
- `residual`: 57
— every worklist row decided; the R36 DEMOTE verified landed unresolved-span
at the projected re-key 8254a7fc75ad2946 and the R39 pair at the projected
re-keys 09f012e4cabef0cc / 80d783fb13def4e2, chunk identity intact (the W3
invariant); zero movement.

## Disposition

Zero silent movement; zero silent repair. The re-composed promoted surface
stays exactly as the R40 rebuild landed it (828 HUMAN_VALIDATED = 825
re-applied from the R5 chain AMENDED FIVE TIMES OVER by R26+R30+R33 + the
R36+R39 exclusions + 3 ADDED sign-off promotions, the 3 R33 movers
re-pinned at 1.8D) and the 4 anchored SUGGESTED rows stay SUGGESTED — the
re-gate VERIFIES, it never re-confers. The store is byte-identical to the
R40 landing (sha16
14d04dfebb71b849).

## NEXT

- any next re-gate or repair round — each the operator's call (explicit
  instruction only).
