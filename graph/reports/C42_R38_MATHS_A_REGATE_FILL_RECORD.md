# C42 R38 — K2-B substrate RE-GATE fill record (operator gate 2 re-run evidence)

**Reviewer:** Super Z (GLM agent), acting as operator-delegate under the operator's 'fire R37 → R38' directive (2026-10-16, zai-web, gateway trace 1a144e6357d603d9) — the R37 record's NEXT gate (operator gate 2 re-run over the R37-rebuilt substrate, the loop's tenth gate-2 pass and the FIRST under the NARROWED EXCLUSION-ONLY promotion surface) fired verbatim; the human operator retains final sign-off; per the anti-forgery rule this re-gate VERIFIES the re-composed 830-row HUMAN_VALIDATED surface and never moves it
**Review date:** 2026-10-16
**Baseline:** b07187c (the R37 clean-audit HEAD; the R37 substrate is byte-identical to its dd803dc landing, store sha16 8d8474c59ca6341f)

## What this is

The loop's TENTH gate-2 pass, fired by the second clause of the operator
directive. Re-seeded draw over the R37-rebuilt substrate (917 rows; 834
anchored; 830 HUMAN_VALIDATED re-pinned 827 + 3 with the 3 R33 movers at
1.8D and the R36 DEMOTE row excluded into the worklist; covered 133/188),
under the standing convention: re-gates re-seed, the
R13→R17→R21→R25→R29→R32→R35 falsification precedent.

## Census

| Surface | Value |
|---|---|
| rows | 917 |
| anchored | 834 (830 HUMAN_VALIDATED + 4 SUGGESTED) |
| worklist | 83 (8 DEMOTE-landed + 57 residual + 18 cleared + 0 uncovered-SP) |
| covered codes | 133/188 |
| store sha16 | 8d8474c59ca6341f |

## Part A — the anchored draw

| Stratum | Rows in stratum | Sampled | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|---|
| exact | 464 | 93 | 90 | 2 | 1 | 96.8% |
| partial | 238 | 238 | 238 | 0 | 0 | 100.0% |
| none | 132 | 132 | 132 | 0 | 0 | 100.0% |
| **Total** | 834 | 463 | 460 | 2 | 1 | 99.4% |

**Gate result: PASS — every class at or above the 90% gate.**

## Verdict sources

- `FRESH-pending`: 0
- `H2 (content-row CONFIRM standing)`: 9
- `H3 (fail-closed HOLD)`: 1
- `operator-id-verdict`: 24
- `r1-section-override`: 1
- `r13-carried`: 5
- `r14-section-override`: 1
- `r17-carried`: 1
- `r18-section-override`: 1
- `r21-carried`: 4
- `r25-carried`: 5
- `r26-standing`: 3
- `r29-carried`: 2
- `r30-signoff`: 1
- `r32-carried`: 3
- `r35-carried`: 391
- `r38-fresh`: 9
- `r4-carried`: 1
- `r6-section-override`: 1

## Tier signatures

- `LEDGER_FOUNDATION`: 50
- `STORE_HIGHER`: 413
— DIVERGENT 0 (the both-tier standing instruction: DIVERGENT fails the fill
closed).

## Part B — the worklist

- `cleared`: 18
- `demote`: 8
- `residual`: 57
— every worklist row decided; the R36 DEMOTE verified landed unresolved-span
at the projected re-key with chunk identity intact (the W3 invariant); zero
movement.

## Disposition

Zero silent movement; zero silent repair. The re-composed promoted surface
stays exactly as the R37 rebuild landed it (830 HUMAN_VALIDATED = 827
re-applied from the R5 chain AMENDED by R26+R30+R33 + the R36 exclusion + 3
ADDED sign-off promotions, the 3 R33 movers re-pinned at 1.8D) and the
4 anchored SUGGESTED rows stay SUGGESTED — the re-gate VERIFIES, it never
never re-confers. The store is byte-identical to the R37 landing (sha16
8d8474c59ca6341f").

## NEXT

- any next re-gate or repair round — each the operator's call (explicit
  instruction only).
