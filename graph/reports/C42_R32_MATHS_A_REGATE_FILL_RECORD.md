# C42 R32 — K2-B substrate RE-GATE fill record (operator gate 2 re-run evidence)

**Reviewer:** Super Z (GLM agent), acting as operator-delegate under the operator's 'Fix all of these yourself. Validate by yourself.' directive (2026-10-12, zai-web, gateway trace 1a130272fc8acc11) — the R29 record's next-decision gate (operator gate 2 re-run over the R31-rebuilt substrate, the loop's eighth gate-2 pass and the FIRST under the RE-COMPOSED promotion surface) fired verbatim; the human operator retains final sign-off; per the anti-forgery rule this re-gate VERIFIES the re-composed 831-row HUMAN_VALIDATED surface and never moves it
**Review date:** 2026-10-12
**Baseline:** bd3acc1 (the R31 clean-audit HEAD; the R31 substrate is byte-identical to its 3b34c25 landing, store sha16 4aeb73e1575f9586)

## What this is

The loop's EIGHTH gate-2 pass, fired by the validation clause of the
operator directive. Re-seeded draw over the R31-rebuilt substrate (917 rows;
835 anchored; 831 HUMAN_VALIDATED re-composed 828 + 3; covered 133/188),
under the standing convention: re-gates re-seed, the R13→R17→R21→R25→R29
falsification precedent.

## Census

| Surface | Value |
|---|---|
| rows | 917 |
| anchored | 835 (831 HUMAN_VALIDATED + 4 SUGGESTED) |
| worklist | 82 (7 DEMOTE-landed + 57 residual + 18 cleared + 0 uncovered-SP) |
| covered codes | 133/188 |
| store sha16 | 4aeb73e1575f9586 |

## Part A — the anchored draw

| Stratum | Rows in stratum | Sampled | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|---|
| exact | 465 | 93 | 92 | 1 | 0 | 98.9% |
| partial | 238 | 238 | 238 | 0 | 0 | 100.0% |
| none | 132 | 132 | 132 | 0 | 0 | 100.0% |
| **Total** | 835 | 463 | 462 | 1 | 0 | 99.8% |

**Gate result: PASS — every class at or above the 90% gate.**

## Verdict sources

- `FRESH-pending`: 0
- `H2 (content-row CONFIRM standing)`: 7
- `operator-id-verdict`: 28
- `r1-section-override`: 1
- `r10-id-verdict`: 1
- `r10-section-override`: 1
- `r13-carried`: 3
- `r17-carried`: 3
- `r18-section-override`: 2
- `r21-carried`: 3
- `r22-standing`: 1
- `r25-carried`: 3
- `r26-standing`: 4
- `r29-carried`: 391
- `r30-section-override`: 1
- `r32-fresh`: 7
- `r4-carried`: 3
- `r9-carried`: 4

## Tier signatures

- `LEDGER_FOUNDATION`: 49
- `STORE_HIGHER`: 414
— DIVERGENT 0 (the both-tier standing instruction: DIVERGENT fails the fill
closed).

## Part B — the worklist

- `cleared`: 18
- `demote`: 7
- `residual`: 57
— every worklist row decided; the R30 DEMOTE batch verified landed
unresolved-span with chunk identity intact (the W3 invariant); zero
movement.

## Disposition

Zero silent movement; zero silent repair. The re-composed promoted surface
stays exactly as the R31 rebuild landed it (831 HUMAN_VALIDATED = 828
re-applied from the R5 chain AMENDED + 3 ADDED sign-off promotions) and the
4 anchored SUGGESTED rows stay SUGGESTED — the re-gate VERIFIES, it never
re-confers. The store is byte-identical to the R31 landing (sha16
4aeb73e1575f9586).

## NEXT

- any next re-gate — each the operator's call (explicit instruction only).
