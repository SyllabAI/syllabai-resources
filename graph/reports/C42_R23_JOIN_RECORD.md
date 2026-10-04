# T-C42 R23 — Join Re-Run over the Unchanged C42-R14-Amended Resolution (the R22 STANDING pins land in-generator)

| | |
|---|---|
| **Task ID** | T-C42 R23 (the join re-run lane) — the operator directive "R23" (2026-10-04, discord, gateway trace 772bb1c553acf115d53f83d9cf6afa81), naming exactly the R22 record's next-decision gate |
| **Date** | 2026-10-04 |
| **Baseline** | `ce7c5c8` (the R22 post-commit audit commit; local == remote at round start) |
| **Kind** | agent-deterministic join re-run under a dated generator amendment (P5: the generator is re-pinned, landed records never edited); every gate fail-closed; zero store bytes move — the R23 lane writes the derived notes-join artifact ONLY |
| **Verification** | `scripts/c42_r23_join_check.py` → `graph/reports/C42_R23_JOIN_CHECK.json` (J1–J8 ALL PASS, exit 0; deterministic re-run content-identical modulo `generated_utc`) |
| **Not fired** | R24 (the substrate re-build consuming the R22 map + the R5 promotions-file re-application) and the R25 re-gate are NOT fired by this directive; the 4 H3 HOLD rows (1.7B / 6.3J / 3.3F / 2.2C) and the ord-3 promoted-surface extension candidate remain open operator decisions — nothing self-fires |

## What the round did

`scripts/c32_notes_maths_a_join.py` re-run under a dated **T-C42 R23 amendment**:
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
refreshed with the census **UNCHANGED** — **198 joined / 5 unresolved / 203
anchors / 0 foreign codes**; **120/188 distinct codes** (61 Foundation / 59
Higher); anchors by tier **81 Foundation / 117 Higher**; wording census **EXACT
173 / LEDGER_EXPLAINABLE 25**. The R22 repair round (the loop's sixth R1-shaped
round) re-pointed **0 note-level joins** — ALL THREE of its note-level
adjudications ruled the joins STANDING — and cleared **0 anchors**, so the
census is unchanged from R7/R11/R15/R19: the C31 §3 residual KEPT UNRESOLVED at
R1 + the 2 anchors the R1 round cleared + the 2 anchors the R6 round cleared.
The resolution file is **BYTE-UNTOUCHED** (HEAD blob `93419a291b9b87ff…` ==
the R14-era pin, counts recomputed **222 / 214 / 8**; last writer remains R14).

**NEW at R23: the three R22 STANDING joins are pinned in-generator** — ruling
STANDING, anchor id and the landed join code verified together against the R22
map's own `note_level_adjudications` (**list-shaped this round**, vs the R18
map's dict shape — the check handles both), fail-closed (the R12/R16/R19
in-generator pin convention):

| note | STANDING join | anchor |
|---|---|---|
| `3d-pythagoras-and-trigonometry` | `4MA1-4.8D` | `spcpt_kX4655D8M3Q3TRzW` |
| `difference-of-two-squares` | `4MA1-2.2F` | `spcpt_RJbgRvXq2VrGpP5g` |
| `graphical-solutions` | `4MA1-2.6B` | `spcpt_sHCB9WZbDMyTFqCP` |

The R22 section-level REATTRIBUTEs (4.8D→4.8F, 2.2F→2.2B, 2.6B→3.3E) ride the
override map `scripts/c42_section_overrides_r22.yaml` into the **R24-shaped
substrate re-build** (the map's own consuming-lane contract) — they do NOT
touch the join layer, and this round verified the other side of the map's
promotions contract too: the R5 promotions file (**832 rows**) intersects the 3
override rows in **NOTHING** by `mapping_id` AND by note+ordinal — the promoted
set is identity- and code-stable at the join layer, **verified not assumed**
(J4). Every carried pin stays and re-verifies: the R14 re-point
(composite-functions → 3.2D), the R10 CORRECT pair (2.2A / 2.2C), the R10
STANDING pin (related-calculations → 1.8D) and the two R18 STANDING pins
(1.2G / 4.1B) — **9 verbatim note-level pins in all** (J2). All four input pins
equal the recorded R19-era constants (manifest `cc470d40873f51a4`, resolution
`b4539ab904c9a319`, SP store `33d3e5313d37464a`, ledger `7f9322a8a05d3767`),
and the resolution pin equals the live git blob (J1).

## What the round does not do

Zero store bytes move: the round's write surface is the derived notes-join
artifact, the amended generator, this battery and the round records — nothing
else (J7: the working-tree delta stays inside the declared footprint; **49
protected paths** byte-untouched baseline→HEAD→working tree, incl. the chunk
store `spec_chunk_mappings.yaml` (921 rows, 832 HUMAN_VALIDATED / 7 anchored
SUGGESTED / 82 worklist), the C30 ledger, the Lane C stores, every standing
loop record and the R5 apply artifacts). The substrate re-build that consumes
the R22 map is **R24** and the re-gate is **R25** — neither is fired by this
directive; the R5-promoted 832-row HUMAN_VALIDATED surface is out of scope by
the anti-forgery rule.

## Environment finding (recorded, not repaired — the R0/R22 pattern)

This workspace materializes the repo under a sparse checkout (`graph/` +
`scripts/` + the maths-a notes corpus + the notes-join artifact) — the
`SME-ExamQuestion/` tree is NOT materialized, so the resolution substrate is
read through the generator's git-fallback (`cat-file --batch`) and pinned by
blob sha (J5) instead of a disk read; the standing `sme_spcpt_verify.py` sweep
is NOT re-run this round (the R18-recorded accounting failures remain a
separate operator census item, byte-unrelated to this round's footprint). A
local `core.fileMode false` was set to silence environmental mode-only churn
(1578 paths, 0 insertions) — a sandbox setting only; no repo config changes.

## Footprint

`scripts/c32_notes_maths_a_join.py` (the dated R23 amendment) +
`scripts/c42_r23_join_check.py` + the refreshed
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
(delta: `task`, `validation_tier`, `generated_utc` — joins/unresolved/counts/
inputs content-identical) + `graph/reports/C42_{R23_JOIN_RECORD.md,
R23_JOIN_RECORD.json, R23_JOIN_CHECK.json}` — nothing else.

## Next operator gates

R24 (substrate re-build consuming the R22 map + re-applying the R5 promotions
file — the c40 tool emits all-SUGGESTED, so the 832-row promotion set is
re-applied over the rebuilt store with its census re-pinned to the R24-era
shape), then the R25 re-gate (operator gate 2 re-run, re-seeded) — each fired
only by explicit operator instruction. The 4 H3 HOLD rows and the ord-3
promoted-surface extension candidate await explicit operator decisions.
