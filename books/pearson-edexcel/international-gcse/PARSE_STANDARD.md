# Parse Quality Standard — Student Books (Pearson Edexcel International GCSE)

**Status:** Canonical intake standard for all student-book parses in `books/`.
**Derived from:** external audit verdict on the chemistry 4CH1 parse (2026-10-18,
"green light" gate — see `chemistry/4ch1/pipeline/AUDIT_VERDICT_2026-10-18.md`).
**Applies to:** every new book parse, starting with Physics 4PH1.

## The 8-point standard

A parse is up to standard when **all eight** hold:

1. **Dual page numbering per chunk** — every chunk carries both `book_pages`
   (citation numbering) and `pdf_pages` (viewer numbering); front matter has
   `book_pages: null`.
2. **Contiguous body ranges / zero overlaps** — chapter `pdf_pages` ranges must
   tile the book without gaps inside chapter bodies and without overlaps.
   Unit-boundary end matter is NOT a gap: it must be typed separately (point 3).
3. **Non-body sections typed separately** — dividers, unit questions,
   chapter questions, answers, glossary, appendices, index, front matter get
   their own `content_type` values instead of being absorbed into chapter
   bodies (this is what produces the by-design "gaps" at unit boundaries).
4. **Spec joins ≥90% verbatim-or-normalized** — joins of chunk content to
   SpecificationPoint codes must be at least 90% `verbatim` + `normalized`,
   with every `fuzzy` join flagged with `method`/`lineage` provenance.
5. **Every code resolves against the spine** — all spec codes referenced must
   resolve against the api concept-graph YAMLs (the spine of record).
6. **15-key v3 grammar** — chunk schema is the v3 JSONL 15-key grammar:
   `id, book_title, author, unit_no, unit_name, chapter_no, chapter_title,
   section, content_type, book_pages, pdf_pages, char_count, text`
   (plus `unit_no`/`unit_name` variants per subject; any deviation must be
   additive, never a rename).
7. **Originals preserved on any LLM polish** — if chunks receive LLM
   fidelity polish, the pre-polish text must be preserved in `text_original`
   with `llm_repaired: true`; repairs are transcription-only (no paraphrase),
   guarded by length-drift/refusal checks.
8. **Per-book source sha256** — the exact source PDF is pinned by sha256 in
   the parse report and the book's README.

## Reference implementation

Chemistry 4CH1 (`books/pearson-edexcel/international-gcse/chemistry/4ch1/`):

- `parsed/` — v1/v2/v3 chunk JSONLs, full-book markdowns, parse reports,
  `load_rag.py` loader, README with schema + RAG advice.
- `pipeline/` — `METHOD_AND_FINDINGS.md` (method, findings, decision log),
  `worklog.md`, `scripts/` (Docling pipeline), `evidence/` (audits, LLM repair
  records, backend-shootout samples).
- `docling_pages/`, `ocr_pages/` — raw per-page intermediates (checkpointing).

Stack used: IBM Docling (layout model + TableFormer) + RapidOCR backend +
CodeFormula VLM for display equations → LaTeX→Unicode chemistry normalization
→ structure mapping → 350–1600 char chunk packing.

## Known action item (from the chemistry audit, non-blocking)

Learning-objectives chunks carry raw newlines (the UI clamps them). Trim
whitespace normalization for `learning_objectives` chunks in the next parse
(apply to Physics 4PH1; do NOT retro-edit chemistry v3 — its chunk IDs are
already consumed by intake receipts and spec joins).
