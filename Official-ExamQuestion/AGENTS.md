# AGENTS.md — operating the Official-ExamQuestion pipeline

> Read this before touching anything in `Official-ExamQuestion/`.
> Doctrine (ADR-039, `syllabai` repo, 2026-10-24 — supersedes ADR-037's verbatim/no-LLM
> clauses): **the pipeline improves; provenance discloses.** The deterministic extraction
> pass remains the baseline every document is measured against; on top of it, any tool —
> script or LLM — may correct, clarify or enrich any serving field, provided every
> departure is disclosed (`edit_status`, `edits[]`, `value_trace`), graded values
> (marks, mark_points, MCQ keys) corroborate the MS of record or carry explicit
> correction evidence, and labels remain registry-validated (G6). Gates fail disclosed:
> an edit that cannot be disclosed is not an edit — it is a defect.

## What lives here

```
Official-ExamQuestion/
  README.md                 what this directory is, storage-placement decision
  AGENTS.md                 this file — the operating manual for agents
  LEDGER.md                 append-only improvement ledger (findings F# -> fix -> canary)
  CANARIES.json             machine-checkable regression assertions
  check_canaries.py         canary checker (exit 1 on violation)
  run_all.sh                one-command full-corpus battery + canary verification;
                            emits a leg-structured receipt per run (F63)
  RECEIPTS-AND-BATTERIES.md the operating-culture import: receipts, batteries,
                            honest verdicts, and what we deliberately did NOT import (F63)
  receipts/                 LOCAL battery receipts from run_all.sh — gitignored; cite
                            them from PRs/LEDGER entries, never commit routine runs (F63)
  CHANGELOG.md              converter version history
  CROP-REVIEW.json          durable human eyeball verdicts for figure crops (F29)
  MCQ-KEYS.json             durable human-adjudicated MCQ keys + corrected MS rows (F37)
  STEM-RESTORE.json         wave-19 stem-restore ledger + stemFigure crop specs (F53/F57)
  SOLUTION-ENRICH.json      authored SME-style worked answers keyed to parts (F60,
                            schema syllabai.official-solution-enrichment/0.1)
  MS-LINK-OVERRIDES.json    transcription overrides for degraded MS rows (F50)
  spec-labels/<series>.json LLM spec-tagging wave labels (parts -> 4CH1 codes)
  MULTI-SERIES-REPORT.{md,json}   per-series gate matrix + findings + cross-diff summary
  CROSS-DIFF.json           marks agreement vs the repo's own parsed/ layer
  igcse-chemistry-19/<series>/4CH1-<paper>/   (1C since the prototype; 2C since v0.8/F34;
                                                1CR since v0.12 — R-VARIANT tranche 1)
  igcse-physics-19/<series>/4PH1-<paper>/   SECOND LANE (landed Task 16; MS-table parser
                                                wave Task 17 F72; QP-side wave Task 18
                                                F85; crop-eyeball + spec-labels waves
                                                Task 21 F99/F100; OCR layer +
                                                repair-reconversion Task 22 F101/F102):
                                                55 slices LANDED
                                                under ADR-039, 55/55 fully PASS (G3
                                                142/142, G5 2,254/2,254, spec tags
                                                2,254/2,254 terminal, asset review
                                                flags 0) — its LANE-STATUS.md is the
                                                disclosure of record; converter lane
                                                key `--spec 4ph1` (v0.16.0)
    topic.json              syllabai.official-paper-questions/0.1 (the product)
    questions.md            human-readable render
    validation-report.json  G0–G7 receipts + negative controls + review queue
    assets/*.png            figure crops rendered from the QP PDF (v0.5)
../scripts/
  official_examq_extract.py the extraction baseline (deterministic); improving passes run
                             on top under the disclosure contract (ADR-039 §4)
  make_multiseries_report.py report aggregator (auto-discovers series dirs)
  cross_diff_parsed.py      independent-parse marks agreement checker
```

Sibling corpus (NOT this pipeline): `../SME-ExamQuestion/` is the scraped Save My Exams
corpus. It is a **cross-check reference and spec registry source** for this pipeline,
never an input to verbatim extraction.

## Quickstart (per-series)

The kit runs from any clean checkout. Outputs are ALWAYS written inside the checkout
(`Official-ExamQuestion/igcse-chemistry-19/<series>/4CH1-1C/`, F15). Inputs are
staged under `$EXAMQ_UPLOAD_DIR` (default `/home/z/my-project/upload`) with fixed
names (see `official_examq_extract.py:paths_for`):

    official-4CH1-<paper>-<series>-qp.pdf / -ms.pdf  raw PDFs from syllabai-pastpapers
    official-<series>-<paper>-qp.txt / -ms.txt       pdftotext -layout extractions
    manifest-<series>-<paper>.yaml                   manifest from the archive repo
  (pre-0.8 bare 1C txt names are still honored for old staging areas)
    ocr/<series>-<paper>/qp-pNN.txt + ocr-pages.json  OCR source layer (F41, optional):
                                  prepared text for image-only archive pages; sha256-
                                  pinned manifest, fail-closed on any mismatch

Cold start needs no manual prep: `run_all.sh` bootstraps the series index itself
(one contents-API call; set `GHTOKEN` for a private archive repo, F16).

Run one series (writes topic.json + questions.md + validation-report.json):

    python3 scripts/official_examq_extract.py --series 2020-11             (paper 1C)
    python3 scripts/official_examq_extract.py --series 2022-06 --paper 2C  (2C tranche, F34)

Run the whole corpus and verify nothing regressed:

    bash Official-ExamQuestion/run_all.sh

## The iron rules

1. **Correct-first, disclose-always.** Any serving field may be corrected, clarified or
   enriched by any tool; every departure from the extracted source layer carries a
   complete `edits[]` entry with a non-empty `evidence_ref`. An undisclosed edit fails
   G2-D exactly as an undisclosed mutation always has.
2. **Fail disclosed.** A gate that cannot prove disclosure is a failure. Ambiguous MCQ
   keys are still refused (see 2020-01 7(a)(iii)); the difference is what happens next —
   a provable defect is now *fixed with disclosure* (any tool, evidence recorded), not
   frozen behind a ledger ceremony.
3. **Values are never invented.** Every number, key and mark traces to the printed QP/MS
   evidence or verifies as correct arithmetic on printed values (the corpus-wide
   verifier, exit 1 on any problem). Graded-value corrections require printed-MS or
   rendered-page evidence in `evidence_ref` — LLM may propose, evidence applies.
   Damaged/rasterized sources produce disclosed REVIEW states with page attribution
   (2019-06 Q7 precedent), never silent synthetic content.
4. **Identity comes from the manifest, not the filename.** The canonical example: a
   paper labelled "June 2020" (a series that never ran — COVID) fingerprinted byte-for-
   byte as November 2020. G0 checks sha256 against `manifest.yaml`.
5. **Registry or review.** Spec-point codes must exist in the SME spec-point resolution
   registry (`spec_point_resolution.json`) or be documented gaps. Unresolved codes go
   to the review queue tagged `pending-llm` / `registry-gap-review`.
6. **Binary assets cross the boundary only through the byte guard (F104/F105).** Any
   asset published or committed goes through `scripts/official_examq_asset_bytes.py`:
   format-truth validation (by actual bytes, never extension or URL status; UTF-8-
   mojibake binaries — the `C2 89 50 4E 47` class — rejected) BEFORE the push, base64
   binary encoding only, and a read-back that demands sha256 byte-identity with the
   source. An HTTP 200 from an API or CDN is never evidence of a healthy asset; byte
   identity is. Wave scripts that push assets MUST import the guard — a bare git-data
   POST is an iron-rule violation even when the bytes happen to be right.

## Operating culture — receipts & batteries (F63)

Imported from the maths-B lane cross-review (the full statement of the laws, their
failure-class evidence, and the two deliberate non-imports live in
`RECEIPTS-AND-BATTERIES.md`; the one-line forms):

1. **Receipts** — every run leaves a machine-readable artifact (`run_all.sh` →
   `receipts/battery-*.json`); evidence or it didn't happen. Local + gitignored;
   cite, don't commit.
2. **Batteries** — one command, numbered legs, honest `N/M PASS` summary; a run
   that dies at leg 3 does not claim legs 4-5.
3. **Re-execution, not receipt-trust** — reviews and landings re-run gates fresh.
4. **Pre-registration & honest verdicts** — BLOCKED is a verdict; human queues
   stay human; incidents are disclosed verbatim.
5. **Census before ship** — defect classes are measured corpus-wide (disclosure
   census + G-E1 exact match), never fixed from eyeball lists.
6. **Claims exist once pushed** — PR-first; ephemeral staging is assumed to die
   with the session (wave-21's withheld drafts did).
7. **Rollback anchors** — every serving change names the state it replaces (G-E5
   source-cut pins; the battery receipt records `git_head`).
8. **Gates measure the learner surface** — parse correctness is not UX
   correctness; new surfaces get their gate class on day one.

## The handover rule — SME EQ → Official EQ on Past Papers (per course)

The hub serves a course's Past Papers "Interactive" buttons from exactly one
source at a time. Before this pipeline starts for a course, the parsed
SME-ExamQuestion sets (their per-part `sourcePaper` provenance) reconstruct
past papers and light the buttons. When this pipeline finishes for that
course, its Official output **replaces** the SME sets as the past-paper
source. The handover is a mandatory pipeline stage with three receipts —
chemistry (igcse-chemistry-19, 2026-10) is the executed precedent:

1. **H1 — baseline census (at pipeline start).** Before converting the first
   series, census what SME EQ currently connects to Past Papers for the
   course: which corpus paper rows carry an active Interactive button via SME
   provenance, questions/parts per reconstruction, coverage chips shown.
   Receipt: `receipts/handover-<course>-h1-baseline.json` (local, gitignored,
   cited from the PR like any battery receipt). This is the state the cutover
   must not silently degrade.
2. **H2 — comparison (when the course's conversion is complete, all gates
   green).** Diff the Official output against H1 per paper: papers/sessions
   each source covers, questions, parts, mark_points, assets, keyed MCQs.
   Any paper SME served that the Official output would serve **worse** (fewer
   parts, lost figures, unkeyed MCQs, missing solutions) is a cutover
   BLOCKER — fix the official set, or disclose the regression and obtain a
   human verdict first. Receipt: `receipts/handover-<course>-h2-comparison.json`.
3. **H3 — cutover (record in LEDGER.md).** Ship the course's official sets on
   the dedicated hub plane
   (`apps/hub/content/<course>/official-papers.json` → `officialPaperTopics`;
   they NEVER render in the Exam Questions topic tree — IA decision, user
   directive) and disconnect the SME sets from past-paper matching for that
   course. On the hub, the Official sets enter the Past Papers pairing FIRST
   (first-match-wins), so the complete official paper shadows any partial SME
   reconstruction of the same session; the invariant is that a course's
   past-paper interactive source is either SME or Official — never a blend.
   The LEDGER entry names the replaced state (rollback-anchor discipline).

The invariant the rule protects: "connect the new" may never silently drop
coverage "disconnect the old" was serving — the learner surface only improves
or discloses.

## Gate catalog

| Gate    | Proves                                   | Fails when                                          |
|---------|------------------------------------------|-----------------------------------------------------|
| G0 identity | the PDFs ARE the manifest's paper     | sha256 mismatch, manifest schema surprises (F13)     |
| G1 structure | Σ parts = printed Q total = paper total (110 for 1C, 70 for 2C — `PAPER_TOTALS`) | mark-sum drift, missing footers, count-registry miss |
| G2 verbatim | emitted text == extracted source text | any post-hoc edit (≥1 5-gram below overlap)          |
| G3 MCQ     | options as printed, exactly one key   | option count drift, ambiguous/unresolved keys        |
| G4 figures | every table/diagram mention → asset; crops rendered | mentions without page-anchored asset records |
| G5 answers | positional linkage into the MS        | unmatched parts below threshold                      |
| G6 registry| spec codes exist or are documented    | unknown code without a documented gap                |
| G7 solutions| verbatim MS block + awardable points | linked part without solution_md; point marks ≠ part marks |
| G8 post-completion audit | the PRODUCT is good, not just the process | any confirmed defect class without a fix-or-disclose entry (see G8 section) |
| G9 learner-surface | the question WORKS in the real syllabai-v2 renderer | any rendered/interaction/solution check FAIL; NOT_RUN never counts as a pass (see G9 section) |

Negative controls (N1 mark-bump, N2 one-word paraphrase, N3 fake spec code) run every
session and MUST be DETECTED 3/3 — otherwise the run is void.

## G8 — POST-COMPLETION AUDIT (mandatory; no course is "done" without it)

When the pipeline finishes for a course, run a full audit of the output BEFORE
declaring the wave complete — not "gates green, ship it". The G0–G7 gates prove
the process was followed; G8 proves the PRODUCT is good. Re-run G8 whenever a
course re-exports (new series, key fixes, crop additions).

### G8 checklist (every item must be run and reported; failures are fix-or-disclose)

1. **Inventory** — set counts match the course spec (e.g. 16/16/11/11); every
   `topic.json` parses; `paper_info.session`/`code` match the directory; zero
   duplicate question ids.
2. **Marks arithmetic** — Σ(part marks) = question total_marks for every
   question; Σ(questions) = printed paper total (read it from the QP footer,
   not memory); zero parts with marks ≤ 0; Σ(mark_points) = part marks where
   mark_points exist.
3. **MCQ integrity** — exactly one `is_correct` per MCQ part; labels A–D in
   order; no duplicate choice texts; every adjudication in MCQ-KEYS.json still
   matches the corpus choices.
4. **Text hygiene** — scan problem/solution/choices/mark_points/stems/groups
   for: control chars (note BEL U+0007 from numbered method steps), PUA chars,
   mojibake (Ã, â€, U+FFFD), Pearson footer lines ("(Total for Question N = M)",
   "Pearson Edexcel", "DO NOT WRITE") in mark_points, empty fields. Report
   counts and say which classes are cleaned downstream (exporter) vs user-facing.
5. **Artwork (the one that always bites)** —
   a. every referenced asset path exists in the repo tree (0 missing);
   b. no shipped asset has `review:true` unless its CROP-REVIEW verdict is
      recorded;
   c. census CROP-REVIEW verdicts (accepted / stub-accepted / rejected) and
      list every `stub-accepted` crop that ships to the hub as `crop-required`;
   d. figure-language sweep: parts containing "diagram|graph|chart|chromatogram|
      apparatus|displayed formula|dot-and-cross|shown in the" where NO part of
      the question embeds an image and the text is not a draw/sketch task —
      EVERY hit goes on a review queue and is checked against the actual QP
      page (yes/no crop needed). The queue is finished when it is empty, not
      when it is documented. Ground truth = the QP PDF from syllabai-pastpapers
      (`past-papers/<spec>/past-papers/<session>/<dir>/qp.pdf`), never memory;
   e. figure-as-text check: flag problem text containing atom-letter soup
      ("H H H H C C C…" runs) — a figure was extracted as text instead of
      cropped.
6. **Hub propagation** — exported bundle vs corpus: set-for-set counts, marks,
   asset counts equal; every SOLUTION-ENRICH key's `solutionMd` byte-equal to
   the hub part's `solutionMd` (the export must serve the authored layer, not
   the verbatim layer); sample embedded image URLs → HTTP 200.
7. **Report** — write the audit as a document with: verdict paragraph, PASS
   table, confirmed defects with paper/question/page evidence, minor defects,
   honest "not checked" list, prioritized fixes. Save next to the course
   corpus and reference it from the wave's CHANGELOG/LEDGER entry.

### First G8 (igcse-chemistry-19, 2026-10-25) — baseline results

PASS: inventory (54/54, 0 dups), marks (0 violations), MCQ keys (4/4),
gates (432/432), hub propagation (2,607/2,607 byte-equal), 424 image URLs 200.
CONFIRMED defects — ALL CLOSED by wave-24 the same day (F64/F65): 3 missing
figures cropped (2019-06 1C Q11(b) apparatus, Q12 calorimeter, 2025-06 1C 9(a)
displayed formula); the 36-part figure queue fully dispositioned
(FIGURE-QUEUE.json: 25 cropped + 10 served_via + 12 dismissed with QP-page
evidence); the ambiguous MCQ 2026-06 1C 1(a) A=D="NH4+" closed at source by the
F64 choice-script restoration (C72 pins the scripts). The REMAINING OPEN minor
classes closed by wave-25 (F69/F70/F71, 2026-10-26, converter v0.18.0): the MS
page-bottom furniture class was measured at 362 lines in 245 corpus text blocks
(the audit's 57-line single-shape estimate undercounted it — census before
ship), dropped at source in parse_ms with the three footer-only masquerade
blocks re-linked through the F47 ledger (50 served mark points cleaned; C77/
C78/C79/C80/C81/C82); the 15 BEL control-char strings normalized at source (C78); the 57
orphan crop PNGs pruned (C79). Full report:
`AUDIT-2026-10-25-igcse-chemistry-19.md` (beside this corpus).

## G9 — LEARNER-SURFACE QUALITY (rendered gate; benchmark-driven; benchmark/README.md)

G0–G7 prove the conversion, G8 proves the course product. **G9 proves the
question works where the learner meets it**: through the REAL `syllabai-v2`
hub (`apps/hub` — the production Next.js app of record; a local `next dev` of
the same app shares its component tree, the deployed Vercel hub is the same
code). JSON validity, extraction success and Markdown-shaped output are
explicitly NOT evidence of a working learner surface.

- **The two legs.** Static (`scripts/official_examq_g9_static_check.py`): the
  frozen benchmark contract against the corpus of record and the serving
  bundles — marks/count/MCQ-key laws + asset presence. Rendered
  (`scripts/official_examq_g9_render_check.py`): a headless browser drives the
  hub — question blocks, marks meta, images actually decoded, frozen semantic
  facts in the rendered text, zero `.katex-error`/raw-TeX/markdown artifacts,
  MCQ select→submit→deterministic feedback (correct AND distractor), solution
  reveal, screenshot evidence. Renderer class is recorded per receipt
  (`syllabai-v2-local-runtime` | `syllabai-v2-vercel`); a static or mock run can
  never masquerade as a rendered one.
- **Dispositions.** `PASS` / `REVIEW` / `FAIL` / `NOT_RUN` / `NOT_APPLICABLE` — and
  **`NOT_RUN` is never a pass**: a required check that did not run can never yield a
  `PASS`ing case; mixed cases rise to `REVIEW`; a case fails on any `FAIL`. A check that
  is genuinely not applicable at one layer is recorded `NOT_APPLICABLE` and NAMES the
  responsible validation layer(s) ("delegated") — lawful only because those layers are
  themselves mandatory legs of the overall gate; it never silently counts as a pass.
  The aggregation law is code (`scripts/official_examq_g9_semantics.py`, F105) shared by
  both legs, and the OVERALL learner-surface gate (`official_examq_g9_aggregate.py`) is
  `PASS` only when all three mandatory legs (static-corpus, static-bundles, rendered)
  and every required check completed successfully, with every delegation covered. The
  law's seven required scenarios are pinned by `scripts/official_examq_g9_tests.py` in
  CI (corpus-gates).
- **Receipts.** `syllabai.g9-{static,render}-receipt/0.1`: content ids +
  hashes, renderer identity + class, validator + benchmark versions, per-check
  outcomes with detail, disposition, artifact paths. Committed under
  `benchmark/receipts/<run>/`.
- **Anti-gaming.** Expected facts are FROZEN in `benchmark/cases.json`
  (versioned; casegen committed for provenance). Expectations change only with
  a `benchmark_version` BUMP + a LEDGER entry. The negative controls are
  permanent fixtures: a mutated fact MUST FAIL; an unreachable renderer MUST
  NOT_RUN.
- **When G9 runs.** (a) the `g9-static` leg runs in every full-corpus battery
  (`run_all.sh`); (b) the rendered leg runs whenever a lane's serving content
  changes (new slices, exporter changes, hub cutover waves) and at every G8
  post-completion audit; (c) spot checks against the deployed hub of record
  ride the same tool with `--base-url https://syllabai-hub-v2.vercel.app`.
- **First run found a real corpus defect class** (F104): 31 physics crop PNGs
  were git-data-API UTF-8-text-corrupted at push time — broken figures at
  HTTP 200, invisible to exists+200 probes. Repaired in PRs #187/#189; the
  byte census is the regression baseline.

## Generative improvement authority (operational; ADR-039 in practice)

ADR-039 already grants the authority ("the pipeline improves; provenance
discloses"). This section makes it operational for every agent wave:

- **Mode A — autonomous improvement** (no operator sign-off): presentation and
  clarity repairs that do not touch assessed content — paragraph/list/table
  reconstruction, line-wrap repair, notation repair when the source page and
  context support it, renderer-compatibility fixes, enriched worked-solution
  steps, accessible figure descriptions. Still requires tests + disclosure
  appropriate to materiality (edits[] on the touched parts).
- **Mode B — evidence-required correction**: anything that touches a numerical
  value, mathematical expression, scientific claim, answer key, mark
  allocation or question meaning. Requires recorded evidence (source-page
  render, the MS of record, corroborating paper context, or a validated
  correction record), the original interpretation, the proposed value, and the
  validation outcome — per the existing `edits[]`/`value_trace` contract.
- **Mode C — investigate or withhold**: unresolved high-impact ambiguity goes
  through the evidence ladder (source image → alternative extraction → MS →
  safe reconstruction) and then to the review queue or an honest block. NEVER
  invent a plausible value to satisfy a completeness gate.
- **Bounded repair**: a failed rendered/G9 case returns to the responsible
  stage with a bounded attempt budget and explicit stop conditions; the loop
  ends in fix, disclosed-withdrawal, or review — never an endless retry.
- **Model hygiene**: provider/model identifiers live in receipts and pipeline
  config, never in the canonical content model; deterministic checks stay
  runnable with zero model availability.

## The v0.5 serving fields (what the frontend / Smart Mark consume)

- `sourcePaper.questionPart` — F119: the printed part label ("(a)", "(a)(i)") as a FIRST-CLASS
  field on the official plane, derived from the corpus part_number by `printed_part_label()`
  (question number stripped; fail-closed grammar: 1-3 parenthesized [a-z0-9]{1,5} groups;
  bare "7"-style whole-question slices → null) and identity-pinned to the part id slug by
  the G-E6 label gate (fail-closed BOTH directions: label == id-derived, null IFF path-less).
  The hub player consumes it first (lib/part-label data-first branch) with the slug parse as
  fail-closed fallback; it renders INLINE with the part text at a smaller label size
  (T-OEQ-PARTLABEL-2/3). Never derive a printed label from a list index — see LEDGER F119.
- `solution_md` — the verbatim mark-scheme answer block for the part (whitespace-
  normalized; marks-column digits stripped). Render behind a reveal control.
- `mark_points[]` — awardable points `{id, marks, text_md}`; ids are stable
  (`<series>-<part>-MP<n>`); marks ALWAYS sum to the part's marks (G7). Splits exist
  only where the MS prints explicit M1..Mn rows; everything else is one whole-block
  point. MCQ parts carry a label-style point referencing the keyed choice. Smart Mark
  can award per point and reconcile against `marks`.
- `assets[]` — `kind: "crop"` entries carry `path` (relative to topic.json), `page`,
  `render` (vector/raster), `text_coverage`, `shared` (figure reused by a sibling
  mention), `ref_part` (the owning part/stem-asset id for shared refs) and
  `review` (true = human should eyeball the crop; cleared + `review_verdict:
  "accepted"` when CROP-REVIEW.json carries an accepted verdict); `kind:
  "crop-required"` entries stay in the review queue (blank-to-complete diagrams,
  rasterized source pages) until a `review_verdict: "stub-accepted"` records the
  eyeballed no-croppable-figure decision (v0.7.1 verdict vocabulary, F32).
- PUA residue is ordinary disclosed-correction work under ADR-039: an evidenced
  mapping (font-trace + page render) ships as a `notation` edit on the affected parts.
  (F48/F52 already landed the corpus-wide table; residual PUA is a defect, not a
  doctrine violation.)

## Spec tagging (v0.7 spec-point waves)

Parts carry `spec_point_codes` + a `tagging` state: `seed-demo` (v0.5 registry-
validated demo seeds), `llm-spec-wave` (codes from `spec-labels/<series>.json`,
LLM-authored; G6 re-validates every code against the registry on every run — ADR-039 lifts
the labels-only scope for *text* fields, codes stay registry-gated), `no-spec-point`
(v0.8.1 terminal: the official 4CH1 specification gives NO numbered point for
the part — decided against the published spec PDF, documented per part in the
spec-labels file's `no_spec_point` map, verified bidirectionally by C32),
`pending-llm` (no clean spec point found — honestly queued; on the spec-labelled
1C tranche this state must NOT persist: decide or document), `registry-gap-review`
(a code not in the SME registry; G6 routes it to the review queue). G6 re-validates
every code against `spec_point_resolution.json` on every run. 1C coverage after
v0.10.0: 941/941 parts resolved corpus-wide — 1C 927 tagged + 3 terminal no-spec-point + the 11 F41-recovered parts labelled (wave 2); 2C 584 tagged + 23 terminal
parts (2019-06 5(a), 2020-01 10(c)(ii), 2022-01 3(b)(iv)); 0 pending. 2C coverage
after its first wave (v0.9.0): 607/607 parts resolved — 584 tagged (0 invalid
codes) + 23 terminal no-spec-point parts (safety precautions, fuel/ester
property-definitions, investigation-design and graph-skills parts — each decided
against the published spec PDF and documented in the `<series>-2C.json`
`no_spec_point` maps); 0 pending. C33 pins the 2C terminal state.
To extend tagging: append codes to the per-series spec-labels file (part_number
→ [codes]; 1C files are `spec-labels/<series>.json`, other papers use
`spec-labels/<series>-<paper>.json`), re-run, and let G6 judge.

## MCQ-key adjudication ledger (v0.8.1)

`MCQ-KEYS.json` is the durable record for MCQ keys the converter must NEVER
auto-derive: the printed Jan 2020 MS itself misplaces the Q7(a) answer rows
((ii)'s block prints under (iii), a stray (i) rebuttal prints under (ii)), so
no positional linkage can key them (F6's honest refusal). Each entry carries
the eyeballed key (from the rendered MS page + QP stem + chemistry) and the
corrected verbatim MS rows. The converter applies the override BEFORE solution
emission — so `solution_md`, `mark_points[]` and `choices[].is_correct` all
derive from the adjudicated block — and C31 keeps ledger↔corpus consistent in
both directions. Keys are graded values: any proposer (human, agent, LLM) must work from the rendered
MS page + QP stem, and an entry applies only with that evidence recorded. Under
ADR-039 an equivalent in-place `corrected` edit with the same evidence bar is lawful;
the ledger remains the record for printed-MS-defect cases and keeps canary binding
(C28–C31). Known printed typo: (ii)'s fourth rebuttal reads 'C is incorrect as
iodine is dark grey' — corrected to D in the corpus (iodine is option D; C is
the keyed answer), verbatim text preserved in the ledger entry.

## Crop-review verdict ledger (v0.7.1)

`CROP-REVIEW.json` is the durable eyeball record; verdicts are applied AFTER all
confidence overrides on every run and C22 keeps ledger↔corpus consistent in both
directions. Ledger keys: bare `<series>` for 1C, `<series>:<paper>` for other
variants (F34) — verdict homes never collide across papers. Verdict vocabulary:
- `accepted` — the crop matches its source-page figure; clears `review` on
  `kind: "crop"` assets.
- `stub-accepted` — the source page has no croppable figure (text-only scaffold,
  blank answer area); clears `review` on `kind: "crop-required"` stubs. The stub
  record stays (kind never changes) — the text layer is the faithful representation.
- **`manual_crop` arm (v0.10.1, F45)** — an `accepted` entry on a stub may carry
  `manual_crop: {page, rect}` (PDF points): the converter renders that eyeballed box
  at 150 dpi, flips the stub to `kind: "crop"` with `manual_crop: true`, and the
  normal accepted↔crop pairing applies. The box re-renders deterministically on
  every run; malformed boxes abort the run (fail-closed). Use it exactly when the
  printed region IS the scaffold/figure (text-only dot-and-cross skeletons,
  rasterized-page figures) — never for genuinely blank answer areas.
Any other verdict/kind pairing fails closed (C22 flags it). Drawn scaffolds
(overlapping electron shells printed as vector circles) are NOT stubs — the
converter crops them (F32) and the fresh crop is eyeballed like any other.

The ledger holds 25 1C verdicts + 17 2C verdicts under ten `<series>:2C` homes
(v0.9.0); the v0.10.1 crop-pass wave flipped 4 stub-accepted entries to `accepted`
with `manual_crop` boxes (2020-11 5(b)(iv), 2023-11 6(b), 2024-06 7(b), 2019-06
15(a)) and re-verified the 4 genuinely blank ones (2021-06 8(b)(iii), 2025-06
9(a)(i), 2026-06 6(b), 2021-11:2C 5(c)). After the wave: 29 crops + 4 stubs on 1C
homes, 17 verdicts on 2C homes; the corpus review queue has ZERO `figure crop
required` entries.

## Review queue taxonomy (what humans decide; agents must NOT decide)

| reason prefix            | meaning                                    | agent may? |
|--------------------------|--------------------------------------------|------------|
| `MCQ key unresolved`     | MS layout ambiguous and not adjudicated | never silently auto-key; resolve via MCQ-KEYS.json or an in-place `corrected` edit — both require rendered-page evidence (ADR-039 §7.1) |
| `figure crop required`   | no croppable figure region (blank-to-complete diagram, rasterized page) | since v0.10.1 (F45): eyeball the page; if a printed region exists, record a `manual_crop` box in CROP-REVIEW.json (accepted verdict) — otherwise keep the stub with evidence |
| `figure crop emitted — human verify` | crop rendered but low-confidence (no text anchor, text-heavy region) | re-render/adjust; never delete silently |
| `spec code ... not in registry` | registry gap or invalid code        | propose, human accepts |
| `Q<N> ... image-only`    | rasterized source pages, content lost      | build the F41 OCR source layer (`scripts/prep_ocr_layer_2019.py` pattern), re-run gates; 2019-06 is done |
| (tagging states)         | `no-spec-point` = terminal decision; `pending-llm` = undecided, must not persist on the labelled tranche | decide with spec-PDF evidence, or tag |

## The self-improvement loop (MANDATORY protocol when a gate fails)

Every gate failure is either a **source defect** (the paper/manifest really is that
way) or a **parser gap** (our regex/assumption doesn't cover a new layout). The loop:

1. **Diagnose at the raw-text level.** Reproduce with `parse_ms`/`clean_lines` in a
   REPL; find the exact lines that defeat the current rule. Never fix against the
   parsed output alone.
2. **Classify.** Source defect → review-queue attribution (G1's image-only census is
   the model). Parser gap → step 3.
3. **Fix generically, not per-series.** A fix must name the *pattern*, not the paper
   (see LEDGER F11–F14: indent tolerance, positive-statement keying, manifest schema
   drift, elimination keying). Reject your own fix if it would key the 2020-01 canary
   or any other canary differently.
3b. **Disclose the fix.** If the fix changes served text/values, the affected parts
   carry `edit_status: "corrected"` + `edits[]` with the finding id in `evidence_ref`
   (e.g. `LEDGER F62`). The 5-gram baseline is measured against the *pre-fix* extraction,
   so the disclosure is machine-checkable.
4. **Record the finding** in `LEDGER.md` (next `F<max+1>`): series, finding, fix.
   One finding per distinct pattern. This is the ledger that makes the pipeline
   self-improving — new agents inherit every scar.
5. **Add a canary** to `CANARIES.json` that would FAIL if the bug regressed (e.g.
   "2023-06 9(a)(i) keyed B", "2020-01 7(a)(iii) unkeyed"). Canaries are the tests.
6. **Re-run the whole corpus** (`run_all.sh`) — a fix that helps one series and breaks
   another is not a fix (F12 briefly regressed 2020-11 exactly this way; the canary
   caught it). All canaries must pass; per-series gate states must be equal-or-better.
7. **Bump `CONVERTER_VERSION`** in the converter + append `CHANGELOG.md`. Outputs
   embed the generator string, so any topic.json can be traced to converter behaviour.

## Conventions

- Output dirs mirror the archive: `<course>/<series>/<paper>/`. Never write into
  `syllabai-pastpapers` (byte-frozen archive of record; see README).
- Add a new series: stage the 3 input files with the standard names, verify printed
  question count against footers (must sum to the paper total: 110 for 1C, 70 for
  2C — `PAPER_TOTALS`), add the count to `EXPECT_QUESTIONS[<paper>]`, run, then
  follow the improvement loop for whatever the gates surface. G0 also asserts the
  staged manifest's `paper_number_variant` equals `--paper` (a 2C run over 1CR
  bytes fails closed).
- Add a new course (beyond igcse-chemistry-19): parametrize `PAPER_TOTAL`,
  `EXPECT_QUESTIONS`, footer regex, and the spec registry path; the ADR's UNVERIFIED
  list (§6) lists what must be proven for a new course (modular 4XCH1, 4SD0 shared
  papers are known next candidates).
- Commit outputs and pipeline changes together; a converter change without regenerated
  outputs (or vice versa) is an inconsistent state.
- Cite battery receipts: every full `run_all.sh` run writes
  `receipts/battery-<UTCSTAMP>-<pid>.json` (gitignored, local evidence). PR and
  LEDGER entries cite the receipt path + its `N/M PASS` summary; a dirty-tree
  battery pass is advisory and never citable as the state of main (F63).

## Known open work (pick up from here)

- Task 27 (2026-10-30, F120) CLOSED the G9 label-visibility gate gap — the F119 QUEUED
  item (a) — with a benchmark v3 contract: frozen `part_labels` samples + `labelled_parts`
  census per case, enforced at ALL THREE legs (served field + id-slug pin at static-bundles;
  part_number derivation source at static-corpus; ACTUAL VISIBILITY — exact chip text,
  rendered presence, geometric same-line in the flex items-baseline row, whole-page chip
  census == labelled_parts, and the fail-closed null class rendering NO chip — at the
  rendered leg, through the stable `data-part-row`/`data-part-label` hooks, v2 PR of record
  cited in LEDGER F120). A label that exists in data but never renders now FAILS G9 instead
  of shipping. New permanent negative control `--negative-control-label` (mutated label
  refused / original derives). Receipts of record: `benchmark/receipts/2026-10-30-run0/`
  (aggregate PASS; mutated-fact + mutated-label DETECTED; dead renderer NOT_RUN). STANDING
  from the F119 queue: (b) the maths-B corpus back-sync (unchanged; the label contract only
  READS the serve-plane field-write) and the post-deploy vercel spot receipt for the v3
  contract (follows the bake; the local-runtime receipt is the renderer of record). The
  F119 item (c) closed earlier with T-OEQ-PARTLABEL-3 (v2 #477).
- Task 26 (2026-10-30, F119) CLOSED the operator-reported part-label learner-surface gap
  end-to-end and shipped the pipeline's first SERVING-FIELD playbook: the exporter emits
  `sourcePaper.questionPart` (printed_part_label, fail-closed grammar), the new G-E6 gate
  pins it to the part's own identity (label == id-derived, both directions, unit battery
  scripts/official_examq_f119_tests.py + CI step), physics + chemistry re-served at the
  current cut (delta == the label class exactly; G-E4 byte-untouched SME planes;
  manifests re-stamped), maths-B served via a disclose-everything FIELD-WRITE because its
  serving plane is AHEAD of its corpus (the T-OEQ-MATHSB-SERVE-1 run-020..025 hand-repair
  chain, 1,461-pid standing debt — a corpus re-export measured 1,466 regressive deltas,
  corpus-lag census filed). READ the F119 ledger section before any maths-B re-export:
  the next corpus catch-up MUST port printed_part_label + G-E6 into the maths-B port
  first, or the re-serve strips the labels. QUEUED from this wave: (a) a G9
  rendered-benchmark case for part-label VISIBILITY (the gap that let the defect ship —
  data gates could not see a field the exporter never emitted); (b) the maths-B corpus
  back-sync (the standing debt; labels ride the ported exporter); (c) the v2-side
  T-OEQ-PARTLABEL-3 card (data-first part-label consumption + the text-sm label) is the
  serving counterpart of this wave.
- Task 25 (2026-10-29, F117) CLOSED the Finding-8b exponent-restore class at source (the
  F111 census's class 2: 23 parts / 51 fields) and recorded Finding 8a CLOSED BY EVIDENCE.
  8b's mechanism was never a validity-rule refusal: the F89 restore law had been DEAD CODE
  in every real conversion — clean_lines' gate tested lowercase `"4ch1"` while main() sets
  `ACTIVE_SPEC_CODE = cfg["spec_code"]` == `"4CH1"`. One case-robust gate fix
  (`(ACTIVE_SPEC_CODE or "").lower() == "4ch1"`), blast radius zero-mint (of-record: 414
  sup chars, ZERO flat law-fireable instances), 19/19 affected slices re-emitted fresh with
  all gates PASS; 2024-06 1CR 11(d) re-pointed to the converter-of-record emission (the
  printed Notes tail "significant figures from 2" the of-record truncated — eyes-on MS
  p13; C205/C207 re-baselined; disclosure 2026-10-29-f117-exponent-restore-gate.json, 1
  part). 8a (MCQ positional keys, 33 parts at the v0.22.0 deep-audit era) needs NO fix: the
  intervening keying laws dissolved the class — zero choices[] deltas corpus-wide in the
  F86 census, re-confirmed at v0.31.0 and in this wave's fresh census. Unit battery
  scripts/official_examq_f117_tests.py (CI). Remaining reproducibility debt = the F111
  class-1 drawing-strip remains only (19 problem_md parts, C147–C165-guarded).
- Task 24 (2026-10-28, F113) CLOSED the F95/F97 MS-side crop capability wave end-to-end:
  the converter renders crops FROM the MS PDF (MS-ANSWER-FIGURES.json eyeball ledger ->
  crop-required stubs -> CROP-REVIEW manual_crop verdicts rendered from the MS doc, all
  fail-closed), and the exporter serves the printed MS answer in solutionMd (official
  mark scheme answer figure, ms.pdf p.N caption, after the authored walkthrough). The
  F95 census's true printed-answer subclass (7 parts: 2026-06 2C 5(a), 2019-06 2C 2(a),
  2019-06 2C 6(d)(ii), 2022-01 2C 7(a)(i), 2023-01 2C 6(a)(i), 2024-11 2C 7(a)(ii),
  2023-06 2CR 7(c)(ii)) now serves the printed answer — C113-C119 pin them. F97's
  leftover (2021-01 2CR 6(c)(i) /1000) had closed via the F108 leg-0 denominator keep.
  The census's other 12 hits are the MP-copy-with-trailing-guidance shape (solutions
  already serve) — disclosed, predicate unchanged. Proof: 6/6 slices 8/8 gates, fresh ==
  surgical on every target part with PNG byte-identity, residual deltas = F111 classes,
  canaries 117/117.
- Task 23 (2026-10-28, F108) CLOSED the MS-grid parser tranche end-to-end: the
  Finding-5 answer-grid parser (2021-06 1C 1(a), 2023-06 1CR 4(a) serve
  reconstructed two-column tables), the F88-queued converter-side grid strip
  (extraction emits the serve-clean form; re-runs reproduce it), and the F90
  MS-side-aware bare-number rule (printed fraction denominators restore;
  marks digits keep stripping). It also restored the Task-19-r2 converter hunks
  the Task-21 merge had clobbered (F92/F93/F97 — the F66 class, caught by the
  law-5 baseline dry-run). Remaining reconciliation classes (disclosed, open):
  MCQ positional keys (Finding 8a, 33 parts), the exponent restore pass
  (Finding 8b, 8 parts), and the Task-20 drawing-strip surgical patches
  (14 problem_md regions) — a full re-run still diverges on those until their
  own reconciliation waves land.
- Task 20 (2026-10-27) CLOSED the C98 drawing-linearization queue end-to-end: the pinned 15
  plus the 6 the closure re-census discovered (F96 update) are cropped+stripped with durable
  eyeball ledgers (STEM-RESTORE stemFigure specs + CROP-REVIEW manual_crop verdicts), the
  three Task-19 canaries finally have checker arms (F104), and the C98 arm pins the census at
  expected_open = 0 corpus-wide. Residual drawing-linearization classes (4 solution_md-only
  residues; 2023-01 2CR 4(b)(ii)'s bracket residue under its own crop) stay with the
  reconciliation wave, as does re-deriving the known-divergent slices.
- Wave-20 (v0.14.0) CLOSED the wave-19 tranche flags: all 48 stem figures/tables the
  restored stems reference are eyeballed crops rendered through the F45 manual-crop
  branch from STEM-RESTORE.json stemFigures specs (converter v0.14.0 question-stem
  figure pass; exporter v6 inlines them into the stem block; flattened label soup cut
  from the served stems — F-W20-1/F-W20-2). The tranche census reconciled: 2 figures
  were already served (inlined by reference), 1 flag retired with evidence (2023-11 1C
  Q7 has no displayed formulae).
- Wave-22 (F62) COMPLETED the enrichment corpus: 2607/2607 solution-bearing parts
  carry authored worked answers (SOLUTION-ENRICH.json, all authored-r0, the full
  ledger re-verified 0 problems under scripts/official_examq_enrich_verify.py — run
  it against ANY ledger edit BEFORE merging; F-W22-1..5 harden it: mark-point
  furniture/artifact strips, case-corrected symbol/label coverage routes, decimal-
  safe numeric tokeniser, M-label evidence reads, uppercase-only marker jargon).
  C71 pins min_entries=2607 (the floor fails if the ledger ever shrinks). The
  2020-01 2CR 1(b)(i) MCQ key was adjudicated to C (the printed MS contradicts
  itself; MCQ-KEYS.json entries now carry a paper field and the converter lookup
  is paper-scoped). Also open: group-stem restore (the exporter restores QUESTION
  stems only — e.g. 2019-06 2C 5(a)'s "The tables give the bond energies..."
  intro is carried by the crop's context, but group stems remain unrestored
  corpus-wide).

- Human review queues (v0.10.1 state): MCQ keys for 2020-01 Q7(a) are RESOLVED —
  the printed MS itself misplaces the answer rows (a source-document defect), so
  the two refused keys were human-adjudicated against the rendered MS page into
  MCQ-KEYS.json (7(a)(ii)=C chlorine, 7(a)(iii)=A astatine; the 7(a)(i) block
  gained its misplaced third rebuttal) and canaries C28/C29/C30/C31 pin the new
  state (F37). Spec tagging is TERMINAL on 1C: the 3 pending-llm parts are
  decided as `no-spec-point` — the official 4CH1 spec gives no numbered point
  for hydrogen density (airship), NO-recycling in the nitric acid process, or
  safety precautions (verified against the published spec PDF); entries live in
  the series spec-labels files and C32 pins them (F38; 2C's 607 parts were resolved by their first wave (v0.9.0): 584 tagged + 23 terminal no-spec-point; C33 pins it). Crop review is EMPTY and TERMINAL (v0.10.1, F45): all 8 crop-required stubs are dispositioned — 4 manual-cropped from their printed scaffolds/table (2020-11 5(b)(iv), 2023-11 6(b), 2024-06 7(b), 2019-06 15(a) off the rasterized scan) and 4 re-verified genuinely blank with stub-accepted notes (2021-06 8(b)(iii), 2025-06 9(a)(i), 2026-06 6(b), 2021-11:2C 5(c)); zero `figure crop required` entries remain corpus-wide, so new converter flags after any future crop change still need eyeballs before a ledger verdict.
- Residual PUA mapping (post F48/F52): converter-level table + parity run; lands as
  disclosed `notation` edits under ADR-039 — no ledger ceremony required.
- 2019-06 archive damage: DONE (v0.10.0) — the six rasterized content pages were
  re-captured through the F41 OCR source layer and G1 is PASS 110/110. The historical
  residual item 2019-06 3(d)(ii) CLOSED via the F47 manual-linkage ledger (the eyeballed
  verbatim transcription of the printed Property-table answer cell, C52's assertion of
  record) — and the MS-figure crop capability it asked for now exists (F113 below). Stem-level figures on the recovered
  pages (Q1 beakers, Q7 structures, Q11/Q13 apparatus, Q12/Q13/Q15 results tables)
  are not asset-backed — no part-level mention triggers the crop machinery on
  text-anchor-less pages; a stem-scan stub pass is future work. UPDATE wave 19:
  the STEM TEXT of all 427 questions now reaches the hub (exporter F53, ledger
  `STEM-RESTORE.json`); the stem FIGURES remain the open crop tranche (see the
  ledger's tranche flags — ~28 figures/tables + 9 formulae letter-runs).
- 2020-06 never ran (COVID); do not "fix" its absence in the archive.
- igcse-physics-19 open waves (Task 21 after F99/F100 closed the crop-eyeball and
  spec-labels waves: the lane is 53/53 fully PASS — G3 135/135, G5 2,171/2,171, spec tags
  2,171/2,171 terminal, the asset review surface EMPTY): 2019-06 1P OCR layer (+ the
  empty-footer-census crash → attribution fix), pastpapers repairs (2023-06 2P mislabel
  bytes), chemistry re-staging (F86: regenerate the chemistry staging txt layers with the
  method of record so fresh re-emissions reproduce the served corpus — C56 pin misses +
  C61 — and give the row-lane rebuttal regex its missing alternation); hub handover NOT
  started. run_all.sh and make_multiseries_report.py remain chemistry-scoped until
  generalized (the physics lane re-emits via --spec 4ph1 with its own report generator).
- 2C follow-ups (F34 wave): (a) DONE v0.9.0 — the 22 review-queue figure items
  were eyeballed and 17 verdicts recorded in CROP-REVIEW.json under
  `<series>:2C` keys (F40 documents the 9 defect mechanisms behind them);
  (b) DONE v0.9.0 — the 2C spec-label waves are authored
  (`spec-labels/<series>-2C.json`, labels only, G6 judges; 607/607 resolved,
  C33 pins the terminal state); (c) DONE wave-26 — the 2C independent-parse
  cross-diff is live: the repo parsed/ layer now covers all 16 2C sittings
  (pastpapers PR #3: 12 new + 2 regenerated-verified sittings alongside the
  pre-existing 2024-06/2026-06), and `cross_diff_parsed.py --paper 2C` agrees
  with the converter corpus on the FULL 16-sitting 2C part census — 607/607
  part marks (545 leaves + 62 parent labels present in both maps) and 103/103
  question totals, 0 mismatches, 0 converter-only parts; the remaining 134
  pdflane-only letter-parent totals each equal the sum of their children on
  both parsers; every sitting = its printed 70 marks
  with Σparts=Σtotals gated). run_all.sh carries the 2C cross-diff battery step
  (parsed-2C- namespaced inputs); (c-cont) DONE wave-27 — the 2CR variant is
  closed the same way: the repo parsed/ layer covers all 11 2CR sittings
  (pastpapers PR #4: 9 new + 2024-06 regenerated false→true with byte-equal
  part marks, alongside the byte-identical pre-existing 2026-06), and
  `cross_diff_parsed.py --paper 2CR` agrees with the converter corpus on the
  FULL 11-sitting 2CR part census — 423/423 part marks, 79/79 question totals,
  0 mismatches, 0 converter-only parts; the remaining 97 pdflane-only
  letter-parent totals each equal the sum of their children on both parsers;
  every sitting = its printed 70 marks. Disclosed pdflane MS-side classes
  (never the marks axis): 8 G1 FAILs — 2 source-style total-row absences
  (2019-06 Q4, 2020-01 none printed) + 6 grid-scanner gaps (parenthesized /
  'Total = N' row shapes 2021-01, 2023-01, 2025-06, 2026-06; the 'M4 Total 12'
  embedded row 2022-01; a phantom Q8 from an '8 × 100' calc line 2022-06, also
  its G3 FAIL) — and 2025-06 marksVerified=false (Q7 MS point losses; QP marks
  close 15 on both parsers). run_all.sh carries the 2CR cross-diff battery step
  (parsed-2CR- namespaced inputs); (d) DONE
  v0.12.0 for 1CR — the 11 1CR sets converted on the same kit via `--paper 1CR`
  (registry entries filed with the outputs per the outputs-and-pipeline law;
  F49/F50 layout repairs through the loop; wave-15 disclosure; spec-label waves
  are the tranche's next step). 2CR DONE (wave-27): the full 11-sitting 2CR corpus is landed and cross-diffed
  (423/423 part marks, 79/79 question totals, `cross_diff_parsed.py --paper 2CR`);
  run_all.sh carries the 2CR cross-diff battery step.
- Serving semantics (v0.6): `assets[]` entries are `kind: "crop"` (real PNG under
  `path`), or `kind: "crop"` with `shared: true` + `ref_part` (a reference to the
  part/stem figure that already owns the PNG — render the referenced `path`, do
  not expect a second file), or `kind: "crop-required"` (honest stub). Asset ids
  ending in `_stem` are question-level figures introduced by a stem sentence.

## Standing rules — self-improving (operator orders recorded 2026-10-26, hygiene-v2 wave)

1. **Post-completion self-check (standing rule).** Before declaring any wave, task or corpus
   state "done", re-run the battery + canaries fresh against the live main state —
   re-execution, not receipt-trust (F63 law 3) — AND re-read the served layer the way a user
   sees it: fetch at least one live interactive page per affected family and read the rendered
   text end-to-end. A wave that only verifies its own diff is not finished; the Task 17
   render-layer pass passed "0 furniture at serve" precisely because it compared the page to
   the corpus instead of to the source-format furniture universe — the corpus itself was the
   defect carrier. Both layers get a fresh look, every time.
2. **SME→Official cutover protocol (standing rule).** When Official-ExamQuestion coverage
   replaces or augments an SME-sourced surface (topic pages, question banks, practice sets),
   the cutover wave must: (a) pin the Official slice set + head SHA in the task receipt;
   (b) run the SME-vs-Official overlap census and disclose any SME-only content that survives
   the cutover; (c) flip the serve-side source flag in the SAME wave as the data landing,
   never as a follow-up; (d) leave the SME corpus in place as cross-check reference per the
   sibling-corpus law (`SME-ExamQuestion/` is a cross-check reference, never an input to
   verbatim extraction).
3. **Battery completeness (the F87 lesson).** A leak battery is defined against the furniture
   UNIVERSE of the source format — every footer/header/watermark family the printed papers
   actually carry — never against the diff of a previous wave. When a user or reviewer
   surfaces a leak class the battery missed: fix it, extend the converter battery + the
   exporter serve-time defense + the canaries in the SAME wave, then census the class
   corpus-wide (F63 law 5, census before ship). The CONTINUES-footer class
   (`QUESTION 11 CONTINUES ON BACK PAGE`, 9 parts / 9 papers) shipped through three green
   batteries (G-gates, wave-25 corpus battery, canary C77) because no battery ever enumerated
   the QP footer universe — this rule exists so that class of blindness dies here. Corollary:
   "battery green" always means "green against the enumerated universe" — say which universe,
   and grow it from source-format evidence, not from incident diffs alone.
4. **Serve-render shape audit (the F96 lesson).** Text-shape classes are part of the furniture
   universe: a gate that only counts figure MENTION nouns (table/diagram/grid/apparatus) is
   blind to printed drawings whose text layers linearize into atom-run garbage — the same
   structural blind spot as F87 one level deeper, and it shipped through every battery for the
   corpus's whole life. Every serve-facing text field gets a SHAPE census (atom runs, bond
   fragments, margin-note fragments, mojibake slots), not just a keyword census; G3 (MCQ
   candidates), G4 (drawing gaps) and G7 (mp answer gaps) now carry theirs. When a shape class
   is surfaced: converter census + gate arm + canary in the SAME wave, then corpus-wide census
   before ship (F63 law 5). Corollary: a figure queue built from figure-language mentions
   inherits the mention blind spot — queue candidates come from the shape census too.
5. **Reproducibility debt is a tracked hazard (the 0.23.0 lesson).** The corpus of record is a
   MIX of full converter runs and surgical wave patches; a full re-run from HEAD inputs is the
   only proof the corpus is re-derivable, and it MUST be run (dry, diffed against the
   committed state, delta-classified) before any wave that needs one — never assume "the
   converter produces the corpus". Known-divergent slices (at 0.23.0: 14, all default-paper
   1C — MCQ positional keys, exponent restore firing, deferred MS-grid classes) are listed in
   AUDIT-2026-10-27; waves touching them ship surgically with disclosure, and the
   reconciliation wave owns re-deriving them from HEAD converter + staged layers.

