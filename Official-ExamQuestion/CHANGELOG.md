# CHANGELOG — official_examq_extract.py (ADR-037 converter)

Semantics: outputs embed `generator: official_examq_extract.py v<version>`, so any
topic.json traces to exactly this behaviour. Every version bump must follow the
AGENTS.md improvement loop: ledger entry (F#) + canary + full-corpus re-run.

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
