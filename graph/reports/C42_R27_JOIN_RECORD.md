# T-C42 R27 — Join Re-Run over the Unchanged C42-R14-Amended Resolution (the four R26 STANDING pins land in-generator)

| | |
|---|---|
| **Task ID** | T-C42 R27 (the join re-run lane) — the operator directive "R27 join re-run + R28 rebuild consuming both carriers" (2026-10-04, zai-web, gateway trace 1a106d1aa121ab59), naming exactly the R26 record's next-decision menu option (a) verbatim |
| **Date** | 2026-10-04 |
| **Baseline** | `a8803c5` (the R26 post-commit audit commit; local == remote at round start) |
| **Kind** | agent-deterministic join re-run under a dated generator amendment (P5: the generator is re-pinned, landed records never edited); every gate fail-closed; zero store bytes move — the R27 lane writes the derived notes-join artifact ONLY |
| **Verification** | `scripts/c42_r27_join_check.py` → `graph/reports/C42_R27_JOIN_CHECK.json` (J1–J9 ALL PASS, exit 0; deterministic re-run content-identical modulo `generated_utc`) |
| **Not fired** | R29 (the re-gate) is NOT fired by this directive; the 4 H3 HOLD rows (1.7B / 6.3J / 3.3F / 2.2C) and the ord-3 promoted-surface extension candidate remain open operator decisions — nothing self-fires. R28 IS fired by the same directive and runs after this round closes |

## What the round did

`scripts/c32_notes_maths_a_join.py` re-run under a dated **T-C42 R27 amendment**:
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
refreshed with the census **UNCHANGED** — **198 joined / 5 unresolved / 203
anchors / 0 foreign codes**; **120/188 distinct codes** (61 Foundation / 59
Higher); anchors by tier **81 Foundation / 117 Higher**; wording census **EXACT
173 / LEDGER_EXPLAINABLE 25**. The R26 repair round (the loop's SEVENTH
R1-shaped round and the FIRST over the promoted surface) re-pointed **0
note-level joins** — ALL FOUR of its note-level adjudications ruled the joins
STANDING — and cleared **0 anchors**, so the census is unchanged from
R7/R11/R15/R19/R23: the C31 §3 residual KEPT UNRESOLVED at R1 + the 2 anchors
the R1 round cleared + the 2 anchors the R6 round cleared. The resolution file
is **BYTE-UNTOUCHED** (HEAD blob `93419a291b9b87ff…` == the R14-era pin, counts
recomputed **222 / 214 / 8**; last writer remains R14).

**NEW at R27: the four R26 STANDING joins are pinned in-generator** — ruling,
anchor id and the landed join code verified together against the R26 map's own
`note_level_adjudications` (**list-shaped**, the R23 precedent), fail-closed
(the R12/R16/R19/R23 in-generator pin convention):

| note | STANDING join | anchor |
|---|---|---|
| `types-of-number` | `4MA1-1.1G` | `spcpt_J55PhZ2cbPsYvpt8` |
| `factorising-by-grouping` | `4MA1-2.2F` | `spcpt_vMSNnYkKPf62MRH9` |
| `drawing-straight-line-graphs` | `4MA1-3.3F` | `spcpt_h8QyRmzX5mCJb3X9` |
| `introduction-to-vectors` | `4MA1-5.1D` | `spcpt_v6tP4DSVShVJMJhk` |

The R26 section-level rulings (1.1G→1.1A, 5.1D→5.1C, 3.3F→3.3H, and the
loop's fourth DEMOTE — factorising-by-grouping ord 2, the FIRST of a PROMOTED
row) ride the **TWofold R26 carriers** — the override map
`scripts/c42_section_overrides_r26.yaml` (schema
`c42-r28-section-overrides/1.0`) AND the promotions amendment
`scripts/c42_r26_promotions_amendment.yaml` (schema
`c42-r28-promotions-amendment/1.0`) — into the **R28-shaped substrate
re-build** (the maps' own consuming-lane contract); they do NOT touch the
join layer.

**THE R26 NOVELTY verified at the join layer (J5, verified not assumed):** the
R5 promotions file (**832 rows**) intersects the R26 map's 4 rows in **EXACTLY
those 4 rows** BY `mapping_id` AND by note+ordinal — the R22/R23-era
intersection was NOTHING, because R26 is the loop's first promoted-surface
inventory. The R5-pinned codes equal the map's `current_codes` on all four
rows, and the amendment agrees end-to-end: base-file sha `9bad739bd79e5899`
== the live R5 sha (the R5 file byte-untouched per the P5 convention), 3
supersedes with `amended_code` == the map's `override_code`, 1 excluded with
disposition `DEMOTE_TO_WORKLIST`, `pinned_code` == the R5 code on every entry,
the 4 ids distinct and covering exactly the map's rows.

Every carried pin stays and re-verifies: the R14 re-point
(composite-functions → 3.2D), the R10 CORRECT pair (2.2A / 2.2C), the R10
STANDING pin (related-calculations → 1.8D), the two R18 STANDING pins
(1.2G / 4.1B) and the three R22 STANDING pins (4.8D / 2.2F / 2.6B) — **13
verbatim note-level pins in all** (J2). All four input pins equal the recorded
R19-era constants (manifest `cc470d40873f51a4`, resolution
`b4539ab904c9a319`, SP store `33d3e5313d37464a`, ledger `7f9322a8a05d3767`),
and the resolution pin equals the live git blob (J1).

## What the round does not do

Zero store bytes move: the round's write surface is the derived notes-join
artifact, the amended generator, this battery and the round records — nothing
else (J8: the working-tree delta stays inside the declared footprint; **76
protected paths** byte-untouched baseline→HEAD→working tree, incl. the chunk
store `spec_chunk_mappings.yaml` — sha16 `ac37a91b9b657ef6` re-verified, the
R25/R26-era pin, 920 rows = 832 HUMAN_VALIDATED / 7 anchored SUGGESTED / 81
worklist —, the C30 ledger, the Lane C stores, every standing loop record, the
R26 map + amendment, and the R5 apply artifacts). The substrate re-build that
consumes the R26 map AND amendment is **R28** — fired by the same directive
and running after this round closes; the R29 re-gate is NOT fired; the
R5-promoted 832-row HUMAN_VALIDATED surface is out of scope for the join lane
by the anti-forgery rule.

## Environment finding (recorded, not repaired — the R0/R22/R23 pattern)

This workspace materializes the repo under a sparse checkout (`graph/` +
`scripts/` + the maths-a notes corpus + the notes-join artifact) — the
`SME-ExamQuestion/` tree is NOT materialized, so the resolution substrate is
read through the generator's git-fallback (`cat-file --batch`) and pinned by
blob sha (J6) instead of a disk read; the standing `sme_spcpt_verify.py` sweep
is NOT re-run this round (the R18-recorded accounting failures remain a
separate operator census item, byte-unrelated to this round's footprint). A
local `core.fileMode false` remains set from R23 to silence environmental
mode-only churn — a sandbox setting only; no repo config changes.

## Footprint

`scripts/c32_notes_maths_a_join.py` (the dated R27 amendment) +
`scripts/c42_r27_join_check.py` + the refreshed
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
(delta: `task`, `validation_tier`, `generated_utc` — joins/unresolved/counts/
inputs content-identical) + `graph/reports/C42_{R27_JOIN_RECORD.md,
R27_JOIN_RECORD.json, R27_JOIN_CHECK.json}` — nothing else.

## Next operator gates

**R28** (substrate re-build consuming the R26 override map AND the R26
promotions amendment — the c40 tool emits all-SUGGESTED, so the 832-row
promotion set is re-applied over the rebuilt store AMENDED by the
`c42-r28-promotions-amendment/1.0` record: 3 code supersedes re-key
old→new, 1 exclusion lands the DEMOTE row unresolved-span, the re-applied
promotion count becoming **831**) — fired by the SAME directive, next. Then
the R29 re-gate (operator gate 2 re-run, re-seeded) — explicit operator
instruction only. The 4 H3 HOLD rows and the ord-3 promoted-surface extension
candidate await explicit operator decisions.
