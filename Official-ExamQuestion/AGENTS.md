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
  igcse-physics-19/<series>/4PH1-<paper>/   SECOND LANE (Task 16, 2026-10-26): 53 slices
                                                landed REVIEW-HEAVY under ADR-039 — its
                                                LANE-STATUS.md is the disclosure of record;
                                                converter lane key `--spec 4ph1` (v0.16.0)
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
F64 choice-script restoration (C72 pins the scripts). REMAINING OPEN (honest,
fix-or-disclose next waves): 57 MS footer lines in mark_points (exporter strips
at serve time); 16 BEL control chars in stems (exporter-cleaned, never
user-facing); 58 orphan crops (repo hygiene). Full report:
`AUDIT-2026-10-25-igcse-chemistry-19.md` (beside this corpus).

## The v0.5 serving fields (what the frontend / Smart Mark consume)

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
  re-captured through the F41 OCR source layer and G1 is PASS 110/110. The one
  residual honest item is 2019-06 3(d)(ii): its MS answer cell is a printed image
  (no extractable text), so the part stays unmatched (C52); serving that answer
  would need an MS-figure crop capability. Stem-level figures on the recovered
  pages (Q1 beakers, Q7 structures, Q11/Q13 apparatus, Q12/Q13/Q15 results tables)
  are not asset-backed — no part-level mention triggers the crop machinery on
  text-anchor-less pages; a stem-scan stub pass is future work. UPDATE wave 19:
  the STEM TEXT of all 427 questions now reaches the hub (exporter F53, ledger
  `STEM-RESTORE.json`); the stem FIGURES remain the open crop tranche (see the
  ledger's tranche flags — ~28 figures/tables + 9 formulae letter-runs).
- 2020-06 never ran (COVID); do not "fix" its absence in the archive.
- igcse-physics-19 open waves (F68, Task 16 landing): physics MS-table parser (G3 79 unkeyed /
  G5 936 unmatched), crop eyeball (65 flagged + 30 stubs → CROP-REVIEW 4ph1 homes), spec-labels
  (2,171 pending-llm), 2019-06 1P OCR layer (+ the empty-footer-census crash → attribution fix),
  pastpapers repairs (2023-06 2P mislabel bytes); hub handover NOT started. run_all.sh and
  make_multiseries_report.py remain chemistry-scoped until generalized.
- 2C follow-ups (F34 wave): (a) DONE v0.9.0 — the 22 review-queue figure items
  were eyeballed and 17 verdicts recorded in CROP-REVIEW.json under
  `<series>:2C` keys (F40 documents the 9 defect mechanisms behind them);
  (b) DONE v0.9.0 — the 2C spec-label waves are authored
  (`spec-labels/<series>-2C.json`, labels only, G6 judges; 607/607 resolved,
  C33 pins the terminal state); (c) the repo parsed/ layer is 1C-only — a 2C
  parsed layer would unlock the independent-parse cross-diff for 2C; (d) DONE
  v0.12.0 for 1CR — the 11 1CR sets converted on the same kit via `--paper 1CR`
  (registry entries filed with the outputs per the outputs-and-pipeline law;
  F49/F50 layout repairs through the loop; wave-15 disclosure; spec-label waves
  are the tranche's next step). 2CR remains: runs via `--paper 2CR` when its
  tranche lands (its totals/counts are already footer-verified into the
  registry).
- Serving semantics (v0.6): `assets[]` entries are `kind: "crop"` (real PNG under
  `path`), or `kind: "crop"` with `shared: true` + `ref_part` (a reference to the
  part/stem figure that already owns the PNG — render the referenced `path`, do
  not expect a second file), or `kind: "crop-required"` (honest stub). Asset ids
  ending in `_stem` are question-level figures introduced by a stem sentence.
