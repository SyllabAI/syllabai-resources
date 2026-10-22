# AGENTS.md — operating the Official-ExamQuestion pipeline

> Read this before touching anything in `Official-ExamQuestion/`.
> Doctrine (ADR-037, `syllabai` repo): **the converter extracts; it never authors.**
> Every character of question text is copied from the official source layer; the only
> generated fields are labels and links, and labels are registry-validated or flagged.
> Gates fail closed: a paper ships only when every gate passes, and anything the
> pipeline cannot prove becomes a human review item — never a guess.

## What lives here

```
Official-ExamQuestion/
  README.md                 what this directory is, storage-placement decision
  AGENTS.md                 this file — the operating manual for agents
  LEDGER.md                 append-only improvement ledger (findings F# -> fix -> canary)
  CANARIES.json             machine-checkable regression assertions
  check_canaries.py         canary checker (exit 1 on violation)
  run_all.sh                one-command full-corpus run + canary verification
  CHANGELOG.md              converter version history
  CROP-REVIEW.json          durable human eyeball verdicts for figure crops (F29)
  MCQ-KEYS.json             durable human-adjudicated MCQ keys + corrected MS rows (F37)
  spec-labels/<series>.json LLM spec-tagging wave labels (parts -> 4CH1 codes)
  MULTI-SERIES-REPORT.{md,json}   per-series gate matrix + findings + cross-diff summary
  CROSS-DIFF.json           marks agreement vs the repo's own parsed/ layer
  igcse-chemistry-19/<series>/4CH1-<paper>/   (1C since the prototype; 2C since v0.8/F34)
    topic.json              syllabai.official-paper-questions/0.1 (the product)
    questions.md            human-readable render
    validation-report.json  G0–G7 receipts + negative controls + review queue
    assets/*.png            figure crops rendered from the QP PDF (v0.5)
../scripts/
  official_examq_extract.py the converter (deterministic; no LLM in the extraction loop)
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

1. **Verbatim-first.** No paraphrase, no cleanup beyond whitespace, no "obvious" typo
   fixes. If the source says it, the output says it. G2 enforces this with 5-gram
   overlap against each part's own extracted source lines.
2. **Fail closed.** A gate that cannot prove success is a failure. Ambiguous MCQ keys
   are refused (see 2020-01: the pipeline refused to key 7(a)(iii) where a naive read
   of drifted marker rows would have emitted a wrong answer).
3. **Never fill gaps by invention.** Damaged/rasterized sources produce REVIEW states
   with page attribution (see 2019-06 Q7: lost to rasterization, marks honestly
   reported as 104/110), never synthetic content.
4. **Identity comes from the manifest, not the filename.** The canonical example: a
   paper labelled "June 2020" (a series that never ran — COVID) fingerprinted byte-for-
   byte as November 2020. G0 checks sha256 against `manifest.yaml`.
5. **Registry or review.** Spec-point codes must exist in the SME spec-point resolution
   registry (`spec_point_resolution.json`) or be documented gaps. Unresolved codes go
   to the review queue tagged `pending-llm` / `registry-gap-review`.

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

Negative controls (N1 mark-bump, N2 one-word paraphrase, N3 fake spec code) run every
session and MUST be DETECTED 3/3 — otherwise the run is void.

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
- Known verbatim limitation: PUA glyphs in the source text layer (e.g. `\uf0b4` for
  ×) pass through un-mapped; a PUA→Unicode pass is future work and must not be done
  ad hoc inside the converter.

## Spec tagging (v0.7 spec-point waves)

Parts carry `spec_point_codes` + a `tagging` state: `seed-demo` (v0.5 registry-
validated demo seeds), `llm-spec-wave` (codes from `spec-labels/<series>.json`,
LLM-authored as LABELS ONLY — AGENTS.md review taxonomy), `no-spec-point`
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
both directions. Adjudications are HUMAN decisions (rendered-page evidence in
each entry); agents must not append entries without rendering and viewing the
MS page. Known printed typo: (ii)'s fourth rebuttal reads 'C is incorrect as
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
| `MCQ key unresolved`     | MS layout ambiguous and not ledger-adjudicated | never auto-key; adjudicate via MCQ-KEYS.json with rendered-page evidence |
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

## Known open work (pick up from here)

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
- PUA→Unicode mapping pass for the source text layer (\uf0b4 → × etc.) — must be
  added as a converter-level mapping table with its own parity run, not ad hoc.
- 2019-06 archive damage: DONE (v0.10.0) — the six rasterized content pages were
  re-captured through the F41 OCR source layer and G1 is PASS 110/110. The one
  residual honest item is 2019-06 3(d)(ii): its MS answer cell is a printed image
  (no extractable text), so the part stays unmatched (C52); serving that answer
  would need an MS-figure crop capability. Stem-level figures on the recovered
  pages (Q1 beakers, Q7 structures, Q11/Q13 apparatus, Q12/Q13/Q15 results tables)
  are not asset-backed — no part-level mention triggers the crop machinery on
  text-anchor-less pages; a stem-scan stub pass is future work.
- 2020-06 never ran (COVID); do not "fix" its absence in the archive.
- 2C follow-ups (F34 wave): (a) DONE v0.9.0 — the 22 review-queue figure items
  were eyeballed and 17 verdicts recorded in CROP-REVIEW.json under
  `<series>:2C` keys (F40 documents the 9 defect mechanisms behind them);
  (b) DONE v0.9.0 — the 2C spec-label waves are authored
  (`spec-labels/<series>-2C.json`, labels only, G6 judges; 607/607 resolved,
  C33 pins the terminal state); (c) the repo parsed/ layer is 1C-only — a 2C
  parsed layer would unlock the independent-parse cross-diff for 2C; (d) the
  remaining GO'd variants (1CR ×11, 2CR ×11) run on the same kit via
  `--paper 1CR/2CR` once their totals/counts are footer-verified into
  `PAPER_TOTALS`/`EXPECT_QUESTIONS` and any layout findings go through the loop.
- Serving semantics (v0.6): `assets[]` entries are `kind: "crop"` (real PNG under
  `path`), or `kind: "crop"` with `shared: true` + `ref_part` (a reference to the
  part/stem figure that already owns the PNG — render the referenced `path`, do
  not expect a second file), or `kind: "crop-required"` (honest stub). Asset ids
  ending in `_stem` are question-level figures introduced by a stem sentence.
