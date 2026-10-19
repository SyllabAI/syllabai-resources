# Physics 4PH1 — Student Book Parse (scaffold)

**Subject:** Pearson Edexcel International GCSE Physics (spec 4PH1)
**Status:** AWAITING SOURCE BOOK — the book PDF will be uploaded to
`source/` by the operator. Parse has NOT started.

## Folder layout

```
4ph1/
├── source/      ← book PDF lands here (operator upload)
├── parsed/      ← RAG deliverables will land here (chunk JSONL, markdown,
│                  parse report with source sha256, loader, README)
└── pipeline/    ← parse scripts, method/findings/decisions, worklog,
                   evidence (audits, repair records) — written during the parse
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

- [ ] Book PDF uploaded to `source/` + sha256 recorded
- [ ] Page-level structure probed (units/chapters/offset)
- [ ] Docling full-book parse (checkpointed per page)
- [ ] Chunking + normalization + validation (8-point standard)
- [ ] Deliverables in `parsed/`, works/decisions in `pipeline/`
