# AUDIT-2026-10-29-f116-f111-remaining-classes — the remaining F111 census classes

**Wave:** F116 (operator order: "the remaining F111 census classes (7(c)(i) curated
form, F97/F92 metadata, F94 curation, drawing-strip/exponent guards)") ·
converter **v0.31.0** · branch `f111/remaining-census-classes-r0`

The F86 corpus-wide re-receipt (F111) classified a 7-class fresh-vs-record delta
universe and left the of-record bytes untouched per the F110 standing decision.
F112 closed class 3 (the F90 80-denominator), F115 closed class 4 (the F88
furniture residue). This wave closes the remaining named classes — 5, 6, 7 — at
source, and guards classes 1 and 2 with per-field fail-visible pins.

## The four classes, their closures

### Class 5 — 7(c)(i)'s longer curated F107 transcription (CLOSED at source)
2023-06 2CR 7(c)(i): the of-record solution_md/mark_points carry the F107
eyeballed 2D transcription (389 B, hand-annotated photograph of the QP displayed
formula, pen circle around the ester group); every fresh emission collapsed the
ASCII-art spacing to 135 B (the standard prose whitespace law destroys the
drawing). Root cause: the F47 ledger application fed `ms_lines` into
`build_solution`, whose whitespace law is prose-shaped.
- **Ledger**: `MS-LINK-OVERRIDES.json` entry gains `transcription_of_record` —
  the exact rendering of record (389 B) with the F116 law note appended to
  `evidence`. Ledger == corpus == fresh, byte-for-byte.
- **Converter (v0.31.0)**: the F47 application emits `transcription_of_record`
  VERBATIM (whitespace-immune; exactly-one-mark-point fail-closed), stamps
  `edit_status=corrected`, a native `edits[]` replay entry (tool = the
  converter itself, evidence_ref cites the F47 ledger entry as the adjudication
  of record — the eyeball chain stays in the ledger), and
  `value_trace.solution = "ms-image-eyeball-transcription (F47 ledger …)"`.
- **Corpus re-point (disclosed)**: 7(c)(i) `edits[]` := the native entry (the
  retired `g9_f107_repair.py` record lives in the F107 ledger row + this
  receipt); `edit_status` stays `corrected`; `value_trace.solution` was already
  the ledger-citing form. Learner-facing bytes: ZERO change.

### Class 6 — the F97/F92(/F112) stale surgical metadata (CLOSED via re-point)
The learner-facing bytes of 2021-11 2C 1(d) (F97 bare-answer), 2025-06 2C
5(c)(i) (F92 tick-glyph) and 2022-06 2C 6(a) (F90/F112 denominator) already
reproduce — the v0.31.0 pipeline serves each natively (row parse / the F92
mirror law / the F108 leg-0 keep law). The of-record `edits[]` + `edit_status=
corrected` records described repairs the current pipeline no longer performs —
stale provenance. Per the F114 doctrine (corpus := what the converter of record
emits) the stale metadata is dropped: `edits[]` removed, `edit_status →
extracted`, 6(a)'s `value_trace.text` removed. The history lives in the F97/
F92/F90/F112 ledger rows and the corpus re-point is disclosed here.

### Class 7 — the F94 shared-asset curation (CLOSED at source + 2-field sync)
- **Sibling shared refs**: the of-record carries the F94 curation's sibling
  refs (2021-11 1C 1(a)(ii)/(iii) → `1(a)(i)`; 2020-11 2CR 1(b) →
  `asset_1_stem_apparatus`) but fresh emissions lost them entirely — dropping
  the figure from the siblings' learner surface and the questions.md
  shared-with captions. `STEM-RESTORE.json` stemFigure entries gain
  `share_with` (the exact of-record asset dicts); the v0.31.0 converter
  replays them after the verdict pass, fail-closed (owner resolved,
  ref_part resolution, target existence, id collisions, slice-scoped
  consumption — the F113 unconsumed-key law) and idempotent.
- **1(a)(i) mention**: the F94 follow-up updated the STEM-RESTORE mention but
  never the corpus; sync := the curated text (topic.json + the questions.md
  caption — the ONE served delta of this wave, disclosure
  `2026-10-29-f116-f111-remaining-classes.json`).
- **2020-01 2C 6(d)(ii)**: `text_coverage` 0.3 → 0.305 (the converter-of-record
  recomputation; corpus := converter form).
- **wave20 stub +1 (2019-06 1CR)**: report-prose only (the of-record report
  predates the wave20 stamp law; gates PASS both sides) — classified, reports
  not regenerated (the C57/F66 clobber lesson; the F110 report-freeze).

### Classes 1+2 — drawing-strip remains (19 parts) and exponent-restore
(23 parts / 51 fields) (GUARDED, not closed)
Closing them would require 19 new Task-20-eyeball text-repair registrations and
a Finding-8b exponent law beyond `restore_flat_exponents`' validity rule — both
eyeball-gated, neither prescribed. The wave instead pins every guarded field
with `part_field_sha` canaries (the C121–C146 pattern): **70 new pins,
C147–C216** — 19 strip pins (problem_md; incl. 2020-01 2C 6(d)(ii), whose
problem_md delta is the polyester-equation strip) + 51 exponent pins over the
23 parts (solution_md/mark_points/problem_md as flagged). Any re-extraction or
re-baseline that loses the curation of record trips fail-closed.

## Proof

**Census** (`official_examq_reemission_census.py`, all 54 slices re-emitted at
v0.31.0 from the staging of record, 54/54 exit 0, diffed under the F111
normalization law):

| | v0.30.1 (before) | v0.31.0 (after) |
| --- | --- | --- |
| delta fields | problem_md 32, assets 5, mark_points 20, solution_md 20, edit_status 4, edits 4, value_trace 2 | problem_md 32, mark_points 19, solution_md 19 |
| classes 5/6/7 fields | 13 | **0** |
| guarded fields (classes 1+2) | 70 | 70 (1:1 with the pins — zero unpinned deltas, zero stale pins) |

Census deltas ↔ guard pins: **exactly 70 ↔ 70, verified set-equal both ways.**

**Battery columns** (check_canaries.py):

| Tree | check_canaries |
| --- | --- |
| of-record (HEAD, restored) | **214/214 PASS** (144 prior + 70 new pins) |
| fresh emissions (v0.31.0, all 54 slices) | 143/214 — the 71 exceptions are C95 (the designed Finding-8b guard) + the 70 new F111 class-1/class-2 guards, each pinning a curation of record the fresh tree does not reproduce — the guards' own designed, fail-visible refusals |

Report-prose drift (8 slices, all gates PASS both sides): the wave20 stamp
(4 slices) + review-queue drift (4 slices) — the known classified classes;
reports not regenerated.

**Exporter + verifier** (the two-file law, v2 IA 662654ade0): exporter G-E1 =
1 delta matching the disclosure exactly (`official-4ch1-1c-2021-11 /
offp_2021-11_1c_1-a-i`, the caption leaf); G-E1b 54/54 identity byte-equal;
G-E4 questions.json byte-identical passthrough (2,605,409 B, 28 SME sets
untouched); verifier census matches the disclosure exactly (1 part, 1 field);
self-test 4/4 seeds refused. The v2 companion sync ships the caption leaf per
the F110 convention; the r2-consumed twin follows the F109 rhythm.

**Unit battery** (`scripts/official_examq_f116_tests.py`, zero network, CI
step added): the F47 ledger==corpus law (tor == corpus solution_md ==
mark_points[0].text_md, 389 B), the F94 share_with replay data (== corpus of
record, ref_parts resolve), all 70 pins recompute live, the sync-of-record
fields hold, the converter law blocks + version present, the disclosure
census-shaped. All green.

## Corpus sync of record (exactly-once guarded)

7 files, key-universe asserted per file (the F112 pattern): 2021-11 1C
topic.json (mention) + questions.md (caption); 2020-01 2C topic.json
(text_coverage); 2021-11 2C / 2025-06 2C / 2022-06 2C topic.json (stale
metadata drops); 2023-06 2CR topic.json (the 7(c)(i) edits[] re-point).
Hygiene: PUA/FFFD 0, mark_points sums exact across the 262 parts of the
touched files, `validation-report.json` NOT regenerated (the C57/F66 lesson).
Assets 414/414 byte-identical throughout.

## Standing decisions honored

- The F110 decision is updated, not broken: the corpus bytes changed ONLY by
  the disclosed class-5/6/7 re-point (the wave's own prescription, the F112
  shape); classes 1+2 bytes remain untouched and are now pinned.
- The of-record `validation-report.json` files: untouched.
- The exporter's G-E1 strict-equality law: unchanged (1 delta == 1 disclosed).

## Verdict

**REPRODUCTION-CLOSED where the pipeline is the author, GUARDED where the
eyeball is.** Classes 5/6/7: zero fresh-vs-record deltas remain, and the
converter of record reproduces every learner-facing byte and every provenance
stamp. Classes 1+2: every guarded field is pinned fail-closed under a named
canary. The F111 delta universe is now fully accounted for: closed, synced, or
guarded — zero unexplained deltas.
