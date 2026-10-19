# Physics 4PH1 — Student Book Parse

**Subject:** Pearson Edexcel International GCSE Physics (spec 4PH1)
**Status:** SOURCE BOOK RECEIVED (2026-10-19) — parse starting.

## Source of record

| Field | Value |
|---|---|
| File | `source/student-book.pdf` |
| sha256 | `9b0783d9fe99790a08255eb1f2ebb6eab5833c03ef8e36dd51b7643ac68a313a` |
| Pages | 308 |
| Size | 30,915,167 bytes (30 MB) |
| Type | **Image-only scan** (producer: RICOH MP C4503; zero text layer on sampled pages) → OCR route required, same as chemistry |
| Provenance | operator-relayed tmpfiles link (gateway trace 1a1539ed1a5c074d) after direct GitHub upload failed |

## Folder layout

```
4ph1/
├── source/      ← student-book.pdf (sha256 above)
├── parsed/      ← RAG deliverables (chunk JSONL, markdown, parse report
│                  with source sha256, loader, README)
└── pipeline/    ← parse scripts, method/findings/decisions, worklog,
                   evidence (audits, repair records)
```

## Plan (method proven in Chemistry 4CH1 — reference implementation)

Parse stack: **IBM Docling** (layout model + TableFormer) + **RapidOCR**
backend + **CodeFormula VLM** for display equations, on CPU; then
LaTeX→Unicode physics normalization, structure mapping (units/chapters from
the book's own contents pages, book_page = pdf_page − offset), 350–1600 char
chunk packing, validation, and (if needed) a strict no-paraphrase LLM polish
with originals preserved.

- Chemistry reference implementation: `../chemistry/4ch1/` (see `parsed/`,
  `pipeline/METHOD_AND_FINDINGS.md`).
- **Canonical quality gate:** `../../PARSE_STANDARD.md` — the 8-point
  standard from the 2026-10-18 chemistry audit (dual page numbering, zero
  overlaps, typed non-body sections, ≥90% verbatim-or-normalized spec joins,
  spine resolution, 15-key v3 grammar, preserved originals, source sha256).
- Physics-specific adaptations expected: equation-heavy content (more
  display equations than chemistry; units like `m/s²`, `kg·m/s`), circuit
  diagrams/figures not captured (text-only, captions kept), different
  page-offset and chapter map (must be reverse-engineered from THIS book's
  contents pages, not assumed from chemistry).

## Checklist

- [x] Book PDF in `source/` + sha256 recorded (2026-10-19)
- [x] Page-level structure probed (8 units / 28 chapters / offset 10;
      see `pipeline/METHOD_AND_FINDINGS.md`)
- [x] Docling full-book parse (308/308 pages checkpointed in `docling_pages/`)
- [x] Chunking + normalization + validation (736 chunks; 8-point standard;
      **serving-critical met: chapter_questions/unit_questions typed and
      page-anchored, book_pages + pdf_pages per-chunk**)
- [x] Deliverables in `parsed/` (v1), works/decisions in `pipeline/`
- [x] LLM fidelity polish round 1 (2026-10-19): scan-wide RapidOCR space-drop
      repaired on 232/300 selected chunks (strict no-paraphrase, originals
      preserved); serving-critical anchor check 0 drift; validation re-run
      ALL CHECKS PASSED. Round 2 (68 chunks) pending LLM quota — protocol in
      `parsed/README.md`.

## Status: v1 PARSE + POLISH ROUND 1 COMPLETE — validation passed (2026-10-19)
