# Rescue R2 (2026-10-25) — the 182-orphan transcription labor, banked

**Status:** transcription COMPLETE + position-verified; landing BLOCKED by the
re-chunk diff gate (see below). This directory is the banked asset for a future
fresh-parse lane.

## What is here

- `manual_batch_r2_w01..w30.jsonl` — 182 verbatim transcriptions, one record per
  unrescued orphan (`pdf_page`, `item_index`, `bbox` = the orphan's own values
  from `formula_orphans.json`, `text` = verbatim transcription; empty `text` =
  adjudicated sliver/duplicate, the r0 protocol).
- `manual_formulas_ych12_FULL_315.jsonl` — the merged sidecar: the 133 landed
  r0 records + the 182 R2 records = full coverage of all 315 orphans
  (315/315 keys, 0 missing, 0 duplicates; 306 filled + 9 adjudicated-empty).
- `rescue_worklist.json` — the 182-item worklist used (grouped by page, with
  prev/next context anchors from the orphan export).

Conventions used (continuity with the r0 133): plain `→`/`⇌` arrows (arrow
labels dropped only where the 133 set did; reagent labels on synthesis schemes
KEPT via `—label→`), `_eq`/`_total`-style underscore word-subscripts
(`ΔS_total`, `[NO₂(g)]²_eq`), modifier-letter superscripts for variable
exponents (`[C]ʸ_eq`, `(pC)ʸ`), `−` U+2212 minus, ` / ` flattened fractions,
`\n` for multi-line items, thousands separators as printed (`+177 900`).

## Why the landing is blocked — the diff gate fired

The resume recipe needs `docling_pages/` (lost in the 2026-10-25 sandbox
reset). The workspace was rebuilt: original-of-record re-downloaded (sha256
`44af34a5…748` re-verified), the docling stack reinstalled to the lane pins
(docling 2.33.0, rapidocr-onnxruntime 1.4.4, transformers 4.52.4, torch
2.14.1+cpu), and all 320 pages re-OCR'd (9 windows, ~10 s/page; index tail
slower). Then:

1. `manual_formula_ws_ych12.py` applied the FULL 315-record sidecar to the
   rebuilt pages: **applied=306, adjudicated=9, mismatch=0** — every one of the
   315 bboxes matched within the 6 pt tolerance, i.e. the re-OCR's item
   POSITIONS are identical to the original run at every checkpoint.
2. `parse_docling_ych12.py` re-chunked → 1406 chunks (landed v1: 1400), with
   **459 new-only vs 453 old-only chunk ids** (~33% renumbered).
3. Text drift on the 947 shared ids: **647 differ (68.3%)**; 541 have
   anchor-field drift (section/book_pages). Far beyond the 182 intended
   insertions → the re-OCR is NOT byte-faithful (prime suspect: unpinned
   onnxruntime backend 1.31.0 vs the original run's version; possibly layout
   model drift). The pre-declared gate verdict: **ABORT the landing**; the
   landed v1 corpus (133 rescues + 74 polish applied) remains the corpus of
   record, byte-untouched.

## How a future lane consumes this

A fresh full parse (v2 law) re-runs docling on the original, applies this
sidecar with `manual_formula_ws_ych12.py` (all 315 in one pass), re-chunks,
and re-runs polish against the fresh pristine. The transcriptions are
position-true (bbox-verified against a second independent OCR run), so they
carry over as-is.
