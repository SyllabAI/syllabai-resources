# LANE-STATUS — igcse-physics-19 (Official-ExamQuestion)

> Landed 2026-10-26 (Task 16) under **ADR-039** ("the pipeline improves; provenance
> discloses") on the operator's explicit order to land the REVIEW-heavy corpus now
> rather than after the MS-parser wave (trace 1a174b2c6305cbfd). Re-generated
> 2026-10-26 (Task 17) after the MS-table parser wave (converter v0.19.0, LEDGER
> F72). Re-generated 2026-10-26 (Task 18) after the QP-side wave (converter
> v0.21.0, LEDGER F85). **Re-generated 2026-10-27 (Task 21)** after the crop-eyeball
> wave (converter v0.24.0, LEDGER F99) and the spec-labels wave (LEDGER F100) — the
> two open human-review surfaces this lane disclosed at Task 18 are both closed.
> This file is the lane's disclosure of record: what is served, what is honestly
> withheld, and which waves are open. Chemistry precedent:
> `AUDIT-2026-10-25-igcse-chemistry-19.md` and `AGENTS.md`.

## Verdict

**LANDED (Task 21 supersedes the Task 18 state); all gates green corpus-wide.**
53 of the 58 census paper dirs of the Edexcel IGCSE Physics (4PH1) corpus convert end-to-end
on converter v0.24.0 and are committed here as serving content: 520 questions, 2,171 parts,
4,790 marks, 531 figure assets. **Every slice passes every gate** — G0 identity (sha256 vs
archive manifests, staged fresh per slice), G1 structure (the physics footer law: 1P = 110,
2P = 70, every part-sum exact), G2-D disclosure, G3 MCQ integrity, G4 figure resolution,
G5 answer linkage, G6 registry (codes validated against the SME `igcse-physics-19`
registry), G7 solution emission — and every run's negative controls are DETECTED 3/3.
The corpus is now **53/53 fully PASS**: G5 answer linkage is corpus-complete
(2,171/2,171 parts carry their verbatim MS block), G3 MCQ keying is corpus-complete
(135/135 keyed), **spec tagging is corpus-complete (2,106 llm-spec-wave + 65
no-spec-point + 0 pending-llm, every code G6-validated against the 186-code registry)**,
and **the figure review surface is EMPTY (0 assets carry review:true)** — Task 21's two
waves (F99 the crop-eyeball wave, F100 the spec-labels wave) closed exactly the two open
surfaces Task 18 disclosed, with two serving corrections recorded honestly:

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
  Pinned by canaries C91/C92/C93.
- **The F99 crop verdicts (65 eyeballed, all asset review flags cleared)**: 23 crops
  accepted as printed; 5 wrong-region crops **rejected** to honest crop-required stubs
  (the solar-panel photograph served for a conceptual 'line graph' mention, the
  loudspeaker diagram served cross-question, an energy-store table served for a
  student-drawn Sankey, the tumble-dryer stem figure, the 'National Grid' false
  mention); 7 crops **recropped** at eyeballed boxes (Diagram 1→Diagram 2, the
  next-page plot grid, a restored y-axis label, the p9 force diagram behind a p8
  stem illustration, the full ²²⁶₈₈Ra→Rn+α equation, the variables tick table behind
  the stem apparatus, Table 1 behind the ramp diagram); 12 stubs resolved by **F45
  manual crops** (the ship diagram, 4 next-page plot grids under the new page_move
  consent, the field-pattern diagram, the loudspeaker, two nuclear equations, the
  isotope table, the bottle photograph); 18 stubs **stub-accepted** (false mentions
  — 'table tennis ball', 'The National Grid'; student-draws — circuits, Sankey,
  method-design bullets; duplicates). Every replacement rect was proof-rendered and
  eyeballed before shipping; the 12 new/re-rendered PNGs are byte-identical to their
  proofs. Pinned by C99 (rejected demotion) and C100 (recrop page move); the 23
  remaining review-queue items are the chemistry-convention disclosures for resolved
  stubs (18 stub-accepted + 5 rejected), matching the served 4CH1 1CR/2C convention.

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
  MCQ failures) was closed by F85; Task 21 closed the Task 18 human-review surface
  (the 65 flagged assets) and the spec-tagging surface (2,171 pending-llm) — the
  withheld surface is empty and the asset review flags are zero.
- **Provenance fields**: schema `syllabai.official-paper-questions/0.2`; every part
  carries `edit_status: "extracted"` and `value_trace` (no serving edits were made in
  any wave — the PUA symbol-glyph normalizations are converter-level, per the F48/F52
  precedent; the F85 print-defect relabel is a converter-level normalization disclosed
  on `value_trace.choices` with the MS-of-record corroboration named).

## Figures

531 assets: 508 `kind:"crop"` + 23 `kind:"crop-required"` stubs. **0 assets carry
`review: true`** — all 65 review-flagged items hold CROP-REVIEW 4ph1 verdicts
(34 `4ph1-<series>:<paper>` homes: 23 accepted, 5 rejected, 7 recrop, 12
accepted+manual_crop, 18 stub-accepted). The 23 stubs are the chemistry-convention
disclosure class: 18 eyeballed no-croppable-figure decisions (false mentions,
student-draws, duplicate mentions) + 5 wrong-region crops withdrawn by verdict.

## Spec tagging

**2,171 of 2,171 parts terminal**: 2,106 carry registry-validated `llm-spec-wave`
codes (per-slice LLM adjudication against the 186-code SME registry over each part's
printed stem, problem, choices and verbatim MS answer block; 9 near-miss codes
adjudicated by hand against the published wordings) and 65 carry terminal
`no_spec_point` decisions (pure graph/table skills, apparatus choice, safety, design
critiques, graph-type justifications, data-relationship tests — the F38 wave
convention, reasoned per part in the labels files). **0 parts pending-llm.** The
53 wave files `spec-labels/4ph1-<series>[-<paper>].json` are the labels of record;
C101 pins the terminal state 4-papers-wide with bidirectional labels↔corpus
agreement.

## Converter provenance (v0.24.0 = v0.19.0 + run-004 union + F85 + F99/F100)

This lane's outputs were produced by **v0.24.0** = the v0.19.0 MS-table wave + the
run-004 maths-B union (lane-scoped, physics-inert) + the F85 QP-side wave **+ the F99/F100
Task 21 waves**. The F99 converter delta is three data-driven verdict mechanisms —
'rejected' (withdraw a wrong-region crop), 'recrop' (re-render at an eyeballed box),
and the F45 `page_move` consent — plus the F100 spec-labels consumption that was already
wired (labels_prefixed lanes read `spec-labels/4ph1-<series>[-<paper>].json`). Every
mechanism is fail-closed and data-driven (chemistry has no such ledger entries): (1) the
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

**Task 21 additions: C99** (the 2020-06 2PR 4(b)(v) rejected demotion stays a
crop-required stub with review_verdict 'rejected'), **C100** (the 2026-06 1P 4(b)
recrop lands on page 10 with manual_crop true), **C101** (spec tagging terminal
4-papers-wide: 0 pending-llm, no_spec_point ↔ labels-file agreement bidirectional).
Battery of record: **99 canaries; the physics battery (14) holds 14/14 on the
re-emitted corpus** (the chemistry C61/C56 staging-era boundary is unchanged — a
chemistry re-staging wave, not a physics one).

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

1. **2019-06 1P OCR source layer** (F41 machinery exists from chemistry) + the
   converter's empty-footer-census crash → fail-closed attribution instead.
2. **pastpapers repair waves**: 2023-06 2P mislabel bytes (Examiners' Report); the 3
   2020-11 missing QPs stay `na:pmt-not-listed` unless a source surfaces.
3. **Chemistry re-staging wave** (F86, from the Task 18 battery findings): regenerate
   the chemistry staging txt layers with the method of record so fresh re-emissions
   reproduce the served corpus (C56 pin misses + C61), and give the row-lane rebuttal
   regex its missing alternation with the corpus-wide re-receipt that change deserves.
   The physics analog closed WITH Task 21: the lane's re-emission of record is now the
   v0.24.0 corpus (the v0.19.0-era staging drift — CONTINUES footers and the F87/F90
   hygiene classes — is superseded by this re-emission).
4. **Hub export + handover**: NOT started — the hub plane still serves the SME sets
   for physics; `official-papers.json` does not exist for igcse-physics-19 and the
   two-file exporter needs a bootstrap decision (no prior bundle of record). The
   H1→H2→H3 handover protocol applies now that conversion + spec tagging are complete
   (all gates green), per AGENTS.md.
5. **run_all.sh / report aggregator generalization**: both remain chemistry-scoped
   (`igcse-chemistry-19`, 4CH1 globs, PAPER_TOTALS 1C/2C); the physics lane runs via
   the converter's `--spec 4ph1` interface with its own report generator for now.

## Receipts (local, cited not committed — F63)

`physics-intake/qpwave/` (Task 18), `physics-intake/qpwave2/` (Task 21: the 65-item
crop inventory + evidence packs `evidence/`, the 19 rect proofs `proofs/`, the verdict
ledger `verdicts.json`, the LLM tag outputs `llmtags/`, the A/B sandboxes
`base/` (v0.22.0) + `noop/` (v0.24.0) and the served A/B copies `served/` +
`served_shas.json`), the Task 21 harness scripts (`eyeball_*.py`, `spec_tag.mjs`,
`spec_tag_*.py`), `physics-intake/census-4ph1.json` (Task 13), and the workspace
worklog Tasks 13–21. Rollback anchor: the Task 18 state is merge `7e2fe8302f96`;
this wave's delta is the converter verdict machinery (rejected/recrop/page_move),
the checker (C22 vocabulary + lane-aware spec_tag_terminal), CANARIES.json (+3),
CROP-REVIEW.json (34 4ph1 homes), the 53 spec-labels wave files, the lane docs, and
the 53 slices' re-emitted serving records — the A/B of record is v0.24.0 vs v0.22.0
on pristine ledgers byte-identical 53/53 (chemistry 1C parity byte-identical) and
the fixed-vs-baseline delta exactly the designed 147 files.
