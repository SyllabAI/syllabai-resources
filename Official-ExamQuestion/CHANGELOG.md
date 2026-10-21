# CHANGELOG — official_examq_extract.py (ADR-037 converter)

Semantics: outputs embed `generator: official_examq_extract.py v<version>`, so any
topic.json traces to exactly this behaviour. Every version bump must follow the
AGENTS.md improvement loop: ledger entry (F#) + canary + full-corpus re-run.

## 0.7 — 2026-10 · verdict-ledger + spec-tagging waves (24 still-tagged crops reviewed, 927/930 parts spec-tagged, shared-ref dedup)

All 24 v0.6 `human verify` crops were re-eyeballed against their source pages
(14 had been correct, 10 were wrong: wrong-cluster bindings, clipped callout
labels, twin duplicate files). The verdicts exposed six more defect classes
(F25–F30) plus a seed audit (F31); all fixes generic.

- **Resolution order rebuild (F25)**: numbered figures ('table 1') anchor on
  their OWN page before any cross-page search (2022-06 4(b) was dragged to the
  stem apparatus on the previous page); the adjacent-page pass lost its
  2-word fallback anchor ('The student' matched unrelated lines) and its
  single-unclaimed-cluster rule (it grabbed the printed Periodic Table twice —
  2021-01 1(a) and 2025-06 1(b)); own-page rescue for backward references now
  runs BEFORE the adjacent search; a question-scoped plot fallback claims the
  grid printed beside earlier parts that never name it (2022-06 6(c)(i)).
- **Directional nouns inside forward sentences (F26)**: 'from the table' is a
  backward reference even in 'Plot the data values from the table on the grid'
  (2020-01 9(d)(i) now shares the p24 data table instead of duplicating the
  grid); an intro noun preceded by 'in the diagram' ('the syringe in the
  diagram shows…') is a reference, not an introduction (2022-06 4(b)); numbered
  mentions are per-noun, not per-part.
- **Callout labels + paired figures (F27)**: short unpunctuated text blocks at
  the side of a drawing ('sodium thiosulfate solution', 'Magnesium') are
  absorbed even beyond the ±66pt ring (2020-11 7(b) no longer clips its
  labels); same-row drawing pairs merge into one figure (2024-11 6(b) now
  crops BOTH the Mg and Cl atoms; 2024-11 1(b)(i) gets all three boxes); a
  text block the final rect would slice is absorbed whole (F27c).
- **Wrong-class guards (F30)**: plot-class mentions never bind to text-dense
  regions (coverage > 0.30 is a table, never a grid — every verified plot crop
  is ≤ 0.05); the adjacent pass applies the same guard (2022-06 6(b)(iii)
  claimed the question stem's apparatus, now claims the p14 plotting grid).
- **Shared-ref semantics (F28)**: a same-question re-pick now shares the
  owner's crop (`ref_part` set) instead of writing a byte-identical twin PNG
  with `ref_part: null`; stem crops reuse an already-claimed cluster. Corpus:
  135 crop assets (57 shared refs), 7 honest stubs, no orphan files.
- **Verdict ledger (F29)**: `CROP-REVIEW.json` records durable eyeball
  verdicts; an 'accepted' entry clears `review` on every re-run (applied after
  all confidence overrides); C22 pins ledger↔corpus consistency in both
  directions. The 24 flagged crops are now 18 flags → all 18 re-eyeballed and
  ledger-accepted.
- **Spec-tagging waves (labels only, G6-validated)**: `spec-labels/<series>.json`
  files tag 922 parts across 16 series (1,180 codes, 0 invalid against the
  SME spec registry); 927/930 parts carry `spec_point_codes` — the 3 remaining
  `pending-llm` parts have no clean spec point (airship density, recycle
  stream, safety precaution) and stay honestly queued. Demo seeds audited
  (F31): 2020-11 4(c)(ii) 1.25→1.26, 8(c)(ii) 3.9→3.4, 10(b) 1.31→1.33,
  1(b)(i) 1.20→1.24.
- Parity vs v0.6: **930/930 parts byte-identical** on extraction fields
  (marks, problem_md, solution_md, mark_points, source_page); gate matrix
  unchanged (2019-06 G1/G5 REVIEW, 2020-01 G3 honest FAIL). Canaries C22
  added; floor 0.7.

## 0.6 — 2026-10 · crop-review wave (eyeball of 10 flagged + 32 pending, serving semantics)

The 10 review-flagged v0.5 crops and all 32 pending stubs were eyeballed against
their rendered source pages. The verdicts exposed six defect classes (F18–F24)
in how figures are detected, attributed and shared; all fixes are generic
(pattern-named, corpus-wide), never per-series.

- **Furniture filters (F18)**: full-height margin-stripe images no longer bridge
  whole pages into one discardable mega-cluster (2019-06 table pages had ZERO
  clusters); footer-band clusters (barcode / Turn over) are never cropped — the
  13(b)(i)/(ii) footer-barcode crops are gone.
- **Anchor disambiguation (F18b)**: progressive-length page anchors (shortest
  fragment matching exactly one page) fix collided openings — 2019-06 9(b) now
  finds its Halon 1301 displayed formula on p14; 7 anchors shifted, each
  independently verified against the printed page.
- **Mention semantics (F19)**: 'Periodic Table', 'Draw a dot-and-cross diagram',
  'You may use a diagram', 'piece/set up the apparatus' no longer create
  crop-required stubs (9 spurious queue items removed); printed-scaffold cases
  ('N N', 'H C Cl H H') keep theirs.
- **Anaphora resolution (F20/F21)**: backward references resolve BEFORE any
  own-page anchoring — explicit 'in part (x)' back-refs, stem/group-stem figure
  intros (one lazy stem crop shared by every referencing part), sibling crops of
  the same figure class, then adjacent pages. 2021-01 10(a)(iii) now shares the
  stem graph instead of cropping the 10(b) isomers diagram; 13(b)(i)/(ii) share
  13(a)(i)'s grid; 2024-11 7(c)/2(c) share their stem tables.
- **Foreign-text exclusion (F22)**: crops no longer swallow instruction lines,
  mark tags, '(Total for Question…)' rows, dotted answer rules or whole-page
  text blocks.
- **Adjacent-page continuation figures + question-scoped claims (F23/F24)**:
  grids printed on the page after their referencing parts are cropped
  (2025-11 3(c)(i) p9 grid); a cluster claimed by another question is never
  taken, and same-question reuse emits a shared reference.
- **Corpus effect**: 134 crop assets (52 shared references — anaphoric parts no
  longer duplicate PNGs; 143 unique PNG files), 8 honest stubs (dot-and-cross
  prompts with text-only scaffolds; 2022-06 6(b)(iii) whose plotted grid cannot
  be attributed without guessing), 24 review-flagged crops queued for humans.
  Parity vs v0.5: extraction fields byte-identical in all 16 series (7
  verified source_page disambiguations excepted); gate matrix unchanged.
  Canaries C15–C21 added; floor 0.6.

## 0.5 — 2026-10 · render-reveal + Smart Mark wave (solution layer, figure crop pass)

Two additions requested to unlock frontend rendering and structured marking;
both are strictly additive (v0.4→v0.5 parity: extraction fields byte-identical
in all 16 series, every gate state preserved).

- **`solution_md` + `mark_points[]` per part (G7)**: every MS-linked part now
  carries the verbatim mark-scheme answer block (`solution_md`, whitespace-
  normalized, marks-column digits stripped) and awardable `mark_points[]`
  (`{id, marks, text_md}` — ids like `2024-06-3-c-MP2`). Points split ONLY on
  explicit ascending M1..Mn rows in the answer column, each worth 1, accepted
  only when n == part marks; everything else is one whole-block point; MCQ
  parts emit a label-style point referencing the keyed choice. Fail-closed:
  the splitter can only under-split, never invent. New gate **G7-solution-
  emission** proves coverage (895/895 linked parts) and the sum invariant;
  it also censuses the MS marks-column digit vs the QP marks (agreement
  recorded per series; drift cases are layout facts, not extraction errors).
- **Figure crop pass (G4 upgraded, canary C14)**: the 158 page-anchored
  `crop-required` stubs are now resolved against the QP PDF itself — vector-
  drawing + raster-image clusters (page frames, margin decorations and
  full-page scans removed pre-merge; horizontal ruling lines kept as table
  strokes; axis labels absorbed from a +16pt text ring; full-width ruled
  answer strips filtered) rendered to `assets/<asset_id>.png` at 150 dpi.
  126/158 emitted (4.1 MB), 14 as shared figures reused by sibling mentions,
  10 flagged `review` for human eyes; the 32 pending keep their stubs and
  review entries (blank-to-complete diagrams, rasterized 2019-06 pages).
  Deterministic assignment; clusters claimed per page in document order.
- `questions.md` now embeds the crops and renders the mark-scheme answer.
- New canaries **C13-solution-emission** and **C14-figure-crops**; floor 0.5.
- Tooling finding **F17** (LEDGER): PyMuPDF `Rect` has no `__ior__` — the
  crop pass's `hit |= b` silently dropped every intersecting box until the
  union was rebound into the list; caught by page-3 rendering diff, now
  canaried by C14's file-existence check.
- Known limitation recorded: PUA glyphs (`\uf0b4` for ×) in the source text
  layer pass through verbatim in both problem_md and solution_md (pre-v0.5
  characteristic; a PUA→Unicode mapping pass is future work).

Corpus totals: 169 questions · 930 parts · 895/895 linked parts with
solution_md + mark_points (347 atomic M-splits) · 126 figure crops ·
cross-diff 161/161 unchanged · 14/16 canaried non-PASS states preserved
(2020-01 honest refusal, 2019-06 archive damage).

## 0.4 — 2026-10 · clean-checkout verification wave (portability, F15/F16)

The kit was run from a clean checkout of `main` as shipped:
- **Reproducibility proven**: golden-master parity 56/56 output files byte-identical
  (modulo `generated_utc`) vs the committed corpus; all 11 canaries held.
- **F15 (fixed)**: converter/cross-diff/report had hardcoded output roots into a
  machine-specific mirror — regenerated outputs bypassed the canaries' own reads.
  All roots now derive from `Path(__file__)`; outputs are always written inside the
  checkout. Staging dir overridable via `EXAMQ_UPLOAD_DIR`; spec registry reads the
  repo-tree copy (canonical) with staged-copy fallback.
- **F16 (fixed)**: `run_all.sh` now self-bootstraps the series index via one
  contents-API call when `pp-tree.json` is absent (the recursive `git/trees` API
  truncates on large repos and silently omits subtrees — observed live).
- New canary **C12-no-hardcoded-output-root** guards F15; corpus re-run green with
  an empty staging dir (cold start: bootstrap → fetch 32 PDFs → gates → canaries).
- No extraction behaviour changed: identical question/part/mark/key output.

## 0.3 — 2026-10 · full-corpus batch wave (16/16 series of 4CH1/1C)

New findings fixed (LEDGER.md F11–F14):
- F11: MS continuation-row indent tolerance `{0,10}` → `{0,20}` (2023-06 G5 76% → 100%).
- F12: MCQ positive-statement keying — '<L> is (the) correct answer' is authoritative;
  note filter extended to 2021+ phrasing 'is not the correct answer'.
- F13: manifest schema-v2 tolerance — 2026-06 gap-fill manifests omit
  `series.printed`/`series.source`; G0 annotates instead of crashing.
- F14: elimination keying for rebuttal-style MS ('A is incorrect…' for every wrong
  option, '<L> (answer)' cells, glued 'B4' cells) — key the sole un-rebutted option
  only when corroborated by exactly one answer row.
- Question-count registry extended to all 16 series (9..12 verified against footers
  summing to 110; 2026-06 genuinely prints 9 questions).

Result: 14/16 series all-gates PASS · 169 questions · 930 parts · 1754/1760 marks ·
all MCQs keyed everywhere except the two honest 2020-01 refusals · negative controls
3/3 everywhere · independent-parse cross-diff 161/161 marks agree (2024-06, 2025-06,
2026-06 vs repo parsed/ layer).

## 0.2 — 2026-10 · multi-series generalization wave (6 series)

Findings F1–F10 (LEDGER.md): QSTART indent tolerance, image-only page census with
defect attribution + G1 REVIEW path, footer-gap census, per-series question-count
registry, MS note-phrasing unification, ambiguity-guard answer keying (2020-01 Q7a),
bare-letter MS rows, phrase-level DO-NOT-WRITE handling, damaged-region start
classification, glued marks-digit stripping.
Result: pipeline proven to generalize beyond the baseline; 2019-06 archive damage
honestly attributed; 2024-06 cross-diff 55/55 marks vs repo parsed layer.

## 0.1 — 2026-10 · prototype (2020-11 baseline)

Converter + gates G0–G6 + negative controls N1–N3; verbatim 5-gram gate; positional
MS linkage; MCQ keying from MS answer text; page-anchored asset stubs; spec seeds
validated against the SME spec-point resolution registry.
Result: 10 questions, 64 parts, 110/110 marks, G0–G6 PASS, 6/6 MCQ keyed, NC 3/3.
