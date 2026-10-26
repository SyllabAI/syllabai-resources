# LANE-STATUS — igcse-physics-19 (Official-ExamQuestion)

> Landed 2026-10-26 (Task 16) under **ADR-039** ("the pipeline improves; provenance
> discloses") on the operator's explicit order to land the REVIEW-heavy corpus now
> rather than after the MS-parser wave (trace 1a174b2c6305cbfd). Re-generated
> 2026-10-26 (Task 17) after the MS-table parser wave (converter v0.19.0, LEDGER
> F72). **Re-generated 2026-10-26 (Task 18)** after the QP-side wave (converter
> v0.21.0, LEDGER F85) closed the last disclosed delta — the 4 QP-side structural
> G3 fails. This file is the lane's disclosure of record: what is served, what is
> honestly withheld, and which waves are open. Chemistry precedent:
> `AUDIT-2026-10-25-igcse-chemistry-19.md` and `AGENTS.md`.

## Verdict

**LANDED (Task 18 supersedes the Task 17 state); all gates green corpus-wide.**
53 of the 58 census paper dirs of the Edexcel IGCSE Physics (4PH1) corpus convert end-to-end
on converter v0.21.0 and are committed here as serving content: 520 questions, 2,171 parts,
4,790 marks, 531 figure assets. **Every slice passes every gate** — G0 identity (sha256 vs
archive manifests, staged fresh per slice), G1 structure (the physics footer law: 1P = 110,
2P = 70, every part-sum exact), G2-D disclosure, G3 MCQ integrity, G4 figure resolution,
G5 answer linkage, G6 registry (codes validated against the SME `igcse-physics-19`
registry), G7 solution emission — and every run's negative controls are DETECTED 3/3.
The corpus is now **53/53 fully PASS**: G5 answer linkage is corpus-complete
(2,171/2,171 parts carry their verbatim MS block) and G3 MCQ keying is corpus-complete
(135/135 keyed). The Task 17 open delta — the 4 QP-side structural fails — is closed by
the F85 wave, with two serving corrections recorded honestly:

- **2020-01 1PR 1(b) — the QP print-defect class**: the QP's own typo prints the 4th
  option row as `A S` where the run is A/B/C/D-S (the MS of record keys `B – arrow Q`
  and its rebuttal row names `D is incorrect as arrow S`, corroborating the intended
  label). v0.21.0's repeat-first-label law completes the run in exactly one way: the
  slice serves A P / B Q / C R / **D S** keyed B, the leaked `A S` row is gone from
  `problem_md`, and the normalization is disclosed on the part
  (`value_trace.choices: "normalized:qp-print-defect-repeat-label …"`), in LEDGER F85,
  and in canaries C89/C90. Corpus census: exactly 1 instance across 53 slices.
- **The marks-law class (3 parts re-typed)**: the F85 census proved the corpus law —
  every true 4PH1 single-select MCQ prints exactly 1 mark (129 of 138 option-run
  parts); the marks≥2 exceptions are exactly the structural shapes the QP parser
  mis-typed as `multiple_choice`: **2023-06 2PR 7(a)** (place-ticks-in-the-table,
  2 marks — v0.20.0 had served a **FALSE key**, `C 500 Hz is_correct`, derived from
  the compound tick rule `C and D ticked…`, plus a false mark_point "Answer C: 500"),
  **2022-06 2PR 1(a)** (draw-matching-lines, 4 marks), **2026-06 1PR 1(a)**
  (name-the-object labelling, 4 marks — v0.20.0 served the raw dot-run answer lines
  as choice texts). All three now type `structured`, carry their printed rows
  verbatim in `problem_md`, and link their MS blocks through the ordinary G5 lane
  (the tick rule, the matching scheme, and the naming scheme serve as solutions).
  Pinned by canaries C91/C92/C93. Review queue 67 → 65 (the two "MCQ key
  unresolved" entries cleared with the false population).

## Coverage (58 census dirs → 53 landed, 5 dispositioned)

All 17 series (2019-06 … 2026-06) are represented. The 5 non-landed dirs, each with a
standing receipt:

| dir | disposition | evidence |
|---|---|---|
| 2020-11 1PR / 2P / 2PR | **NO-QP** — the archive holds manifest + ms.pdf but no qp.pdf; `na:pmt-not-listed` (COVID print-reuse session; PMT never listed them) | Task 13 census + `docs/ledger/file-gap-sweep.csv` (pastpapers) |
| 2019-06 1P | **CRASH-RECEIPT** — image-only 144-dpi QP scan (32-char text layer); converter fails closed on the empty footer census (ValueError, receipted) | Task 15 run receipt; the physics twin of chemistry's F41 case; OCR-source-layer wave open |
| 2023-06 2P | **ARCHIVE-DEFECT** — the archived qp.pdf bytes are a 2PR Examiners' Report (sha faithfully matches its own manifest, so G0 cannot catch it; content-vs-paper identity is enforced only for the series field) | Task 14 receipt; pastpapers repair wave + ledger row owed |

## What is served vs withheld (the learner surface)

- **Served**: verbatim stems and problems, choices as printed, page-anchored provenance per
  part, marks corroborating the printed QP totals, verbatim MS answer blocks for all 2,171
  linked parts (corpus-complete; the 2026-06 2P 4(c)(i) equation-image answer serves via
  `MS-LINK-OVERRIDES.json` under the F42 doctrine — eyeballed from the rendered MS page,
  never model guessed), keyed answers on **135 of 135** MCQ parts, spec codes where the
  registry resolved them (G6), figure crops for resolved mentions.
- **Withheld (disclosed): nothing.** The Task 17 withheld surface (the 4 structural
  MCQ failures) is closed by F85; that was the entire withheld surface.
- **Provenance fields**: schema `syllabai.official-paper-questions/0.2`; every part
  carries `edit_status: "extracted"` and `value_trace` (no serving edits were made in
  any wave — the PUA symbol-glyph normalizations are converter-level, per the F48/F52
  precedent; the F85 print-defect relabel is a converter-level normalization disclosed
  on `value_trace.choices` with the MS-of-record corroboration named).

## Figures

531 assets: 501 `kind:"crop"` + 30 `kind:"crop-required"` stubs. 65 crops carry
`review: true` — the CROP-REVIEW ledger has **no 4ph1 homes yet** (chemistry verdicts
are the only entries); the physics crop-eyeball wave is open. Per the AGENTS review
taxonomy, `figure crop emitted — human verify` (35) and `figure crop required` (30)
stay human queues.

## Spec tagging

0 of 2,171 parts tagged — every part is an honest `pending-llm`. The SME
`igcse-physics-19` registry (8 topics, 184 codes) is wired and G6-validates every code;
the physics spec-labels wave (`spec-labels/4ph1-<series>[-<paper>].json`) is open.

## Converter provenance (v0.21.0 = v0.19.0 + run-004 union + F85)

This lane's outputs were produced by **v0.21.0** = the v0.19.0 MS-table wave + the
run-004 maths-B union (lane-scoped, physics-inert) **+ the F85 QP-side wave**: (1) the
repeat-first-label completion in `parse_mcq_block` (4PH1-gated; relabels the final row
of a 4-option run when it repeats the first label — the canonical printed run is A–D,
so the completion is unique; disclosed on `value_trace.choices`); (2) the marks-law
structural disqualification in `finalize_part` (4PH1-gated; an option-run on a part
carrying ≥2 marks is not a single-select MCQ — the rows stay verbatim in the problem
text); (3) the chemistry `\uf033` tick-repair lane override (the battery assembly
caught run-004's global digit-range clobber of chemistry's F48 tick mapping — repaired
as a `4ch1` `pua_override`, the union's own lane-split pattern; exactly 1 `\uf03x`
occurrence across 54 chemistry staging layers). Every F85 change is 4PH1/4ch1-lane-gated:
**chemistry 2023-06 1C parity receipt: 10/10 files byte-identical** (7 assets
byte-identical, topic.json/validation-report.json/questions.md identical modulo
`generated_utc` + generator version string), gate stdout identical modulo the version
string and the sandbox path line; the 4MB1 lane is untouched by construction and the
C87 registry drift-guard holds.

## Canaries

Battery of record: **91 canaries; 90 hold on the freshly re-emitted chemistry (54) +
physics (53) + maths (fetched, lane untouched) corpus; the 1 exception is disclosed
below.** Task 18 additions: **C89** (2020-01 1PR G3 PASS — the print-defect
completion), **C90** (2020-01 1PR 1(b) keyed B), **C91/C92/C93** (the three
marks-law re-typed parts stay structured, choice-free, and linked — a new
`part_structured` check), plus the `part_structured` checker arm. Standing pins:
C74 (`no_pua_served`, spec 4ph1), C75 (2P footer law), C76 (2023-06 1P 12 questions),
C83 (2024-06 2P G3 triple-glue), C84 (2023-01 2P G5), C85 (2026-06 2P G5 + the F42
override), C86–C88 (the maths union tranche).

The one non-holding canary is **C61** (2019-06 1CR 5(a)(ii) keyed B) — a **pre-existing
staging-era boundary, exonerated for this wave**: the v0.20.0 baseline converter
re-emitted from this workspace's staging leaves the part unkeyed identically (A/B
identical), v0.19.0 behaves the same, and the served corpus keyed it from an earlier
staging era whose MS text-layer layout differs (the row-lane rebuttal regex's dormant
`\b\b` concatenation quirk — hoisted byte-exact per F72 — plus the re-extracted
line shapes defeat the positional key). The same class explains the two remaining
C56 pin misses on fresh chemistry re-emission (2019-06 2C 7(a) ⇌ block linkage and
2021-01 2C 3(a)(i) bullet row — both A/B-identical baseline vs fixed). Recorded as
LEDGER F86; the repair belongs to a chemistry re-staging wave (pdftotext -layout of
record + the C61 row-rebuttal lexeme), not to the physics lane.

## Open waves (prioritized)

1. **Crop eyeball wave**: 65 review-flagged crops + 30 crop-required stubs →
   CROP-REVIEW 4ph1 homes (`4ph1-<series>:<paper>` convention).
2. **Spec-labels wave**: 2,171 `pending-llm` parts → registry-validated labels.
3. **2019-06 1P OCR source layer** (F41 machinery exists from chemistry) + the
   converter's empty-footer-census crash → fail-closed attribution instead.
4. **pastpapers repair waves**: 2023-06 2P mislabel bytes (Examiners' Report); the 3
   2020-11 missing QPs stay `na:pmt-not-listed` unless a source surfaces.
5. **Chemistry re-staging wave** (F86, from this wave's battery findings): regenerate
   the chemistry staging txt layers with the method of record so fresh re-emissions
   reproduce the served corpus (C56 pin misses + C61), and give the row-lane rebuttal
   regex its missing alternation with the corpus-wide re-receipt that change deserves.
6. **Hub export + handover**: NOT started — the hub plane still serves the SME sets
   for physics; `official-papers.json` does not exist for igcse-physics-19 and the
   two-file exporter needs a bootstrap decision (no prior bundle of record). The
   H1→H2→H3 handover protocol applies only when conversion completes (all gates
   green), per AGENTS.md.
7. **run_all.sh / report aggregator generalization**: both remain chemistry-scoped
   (`igcse-chemistry-19`, 4CH1 globs, PAPER_TOTALS 1C/2C); the physics lane runs via
   the converter's `--spec 4ph1` interface with its own report generator for now.

## Receipts (local, cited not committed — F63)

`physics-intake/qpwave/` (the wave workspace: the F85 census `census-qpwave.json` +
`qpcensus.py`, the served-corpus A/B copies `served/` + `served-all/`, the doc
sources), `scripts/qpwave_run.py` / `qpwave_gates.py` / `qpwave_diff2.py` /
`qpwave_report.py` (the 53-slice run + gate + diff + report harness;
`qpwave-sandbox/out-{baseline,fixed}/` = the run receipts), `qpwave-chem-base` /
`qpwave-chem-fixed` / `qpwave-battery` (the parity + battery sandboxes),
`physics-intake/census-4ph1.json` (Task 13), and the workspace worklog Tasks 13–18.
Rollback anchor: the Task 17 state is merge `5246e175`; this wave's delta is the
converter (3 laws + 1 lane override), the checker (`part_structured`), CANARIES.json
(+5), the ledgers/docs, and the four physics slices' corrected serving records —
the diff of record is 49/53 slices byte-clean and 4 slices carrying exactly the
designed corrections.
