# Edexcel IGCSE (9-1) Chemistry — RAG-Ready Dataset

Parsed from the scanned student book PDF (383 pages) with **IBM Docling**
(layout model + TableFormer + RapidOCR + CodeFormula VLM for display equations),
then structure-mapped and packed into RAG chunks, with a **light LLM fidelity
polish** over the noisiest chunks (87 chunks; originals preserved in
`text_original`, `llm_repaired: true`).

**v3 (Docling) is the main deliverable.** It replaces the earlier Tesseract-based
v1/v2 corpora, which suffered from garbled chemical formulas (`2H,(g)`), broken
multi-column reading order, and interleaved sidebar text.

## Why v3 is better

| Aspect | v2 (Tesseract + repairs) | v3 (Docling) |
|--------|--------------------------|--------------|
| Chemical formulas | OCR noise, repaired post-hoc | Native sub/superscripts: `H₂O`, `C₂H₆`, `Cr₂O₃`, `Aᵣ`, `Mᵣ` |
| Display equations | mostly lost/garbled | Decoded by a formula VLM → Unicode: `2K(s) + 2H₂O(l) → 2KOH(aq) + H₂(g)` |
| Reading order | multi-column interleave | Layout-model ordered (sidebars, boxes, two-column pages) |
| Tables | flattened text debris | Structured markdown tables (113 `table_data` chunks) |
| Structure labels | regex markers | Docling item labels + book structure map |
| Equilibrium arrows | lost | `⇌` preserved |

## Files

| File | Purpose |
|------|---------|
| `edexcel_igcse_chemistry_chunks_v3.jsonl` | **Main deliverable.** 1234 chunks |
| `full_book_docling.md` | Human-readable full text with Unit/Chapter/section headings |
| `parse_report_v3.json` | v3 parsing statistics |
| `edexcel_igcse_chemistry_chunks_v2.jsonl`, `full_book_clean_v2.md`, `edexcel_igcse_chemistry_chunks.jsonl`, `full_book_clean.md` | previous Tesseract-based versions, kept for diffing |
| `load_rag.py` | Ingestion helpers: plain JSONL, filter, Chroma, LangChain, LlamaIndex |

## JSONL schema (v3)

```json
{
  "id": "chem_v3_u1_c5_pdf050_0166",
  "book_title": "Edexcel International GCSE (9-1) Chemistry Student Book",
  "author": "Jim Clark",
  "unit_no": 1,
  "unit_name": "Principles of Chemistry",
  "chapter_no": 5,
  "chapter_title": "Chemical formulae, equations and calculations - part 1 (chemistry only)",
  "section": "STATE SYMBOLS",
  "content_type": "body",
  "book_pages": [41, 41],
  "pdf_pages": [50, 50],
  "char_count": 520,
  "text": "STATE SYMBOLS\n\nState symbols are often ...\n\n2K(s) + 2H₂O(l) → 2KOH(aq) + H₂(g)"
}
```

- `book_pages` is `null` for front matter (PDF pages 1–11 have no book-page number).
- Every chunk starts with its section heading (when it has one), so it is
  self-contained for embedding; the fuller context lives in the metadata fields.

## Content types & RAG advice

| type | meaning | RAG advice |
|------|---------|-----------|
| `body` | teaching prose | keep |
| `key_point` | boxed key rules/definitions | keep — high retrieval value |
| `learning_objectives` | spec-linked objectives (incl. CHEMISTRY ONLY boxes) | keep |
| `worked_example`, `exam_hint`, `activity`, `practical`, `did_you_know`, `safety` | feature boxes | keep |
| `table_data` | markdown tables (solubility, electrolysis data, …) | keep |
| `chapter_questions` / `unit_questions` | question banks | keep for Q&A practice, else filter |
| `answers` | answers to all questions | keep (pairs with question chunks) |
| `glossary`, `appendix` | definitions / reference tables | keep |
| `front_matter`, `divider`, `skills` | structural noise | filter out |
| `index` | back-of-book term index | filter out |

Recommended filter: `exclude_types={"index", "divider", "front_matter"}`.

## Known limitations

- Source is a scan; the docling layout model occasionally duplicates or drops a
  decorative element (consecutive-duplicate paragraphs are already collapsed).
- Diagrams/figures are not captured (text-only); their captions are kept.
- Some display equations with handwriting-like or heavily stylised notation were
  dropped rather than risk wrong output (281 clean equations kept, 140 uncertain dropped).
- ~90 of the noisiest chunks (tables, some answers) went through an LLM fidelity
  polish with a strict no-paraphrase prompt + sanity guards (length drift, table
  row-count, refusals); 3 were rejected and keep their original text. Spot-check
  chemistry-critical passages before high-stakes use.

## Regenerating

Pipeline scripts in `/home/z/my-project/scripts/`:

1. `docling_full.py FROM TO` — Docling parse → `data/docling_pages/page_*.json`
   (checkpointed per page; RapidOCR + formula enrichment, CPU).
2. `parse_docling.py` — LaTeX→Unicode chemistry, dedup, structure mapping
   (`book_structure.py`), chunk packing → JSONL + full markdown + report.
3. `select_noisy_v3.py` — noise scoring → `data/llm_repair_ids_v3.json`.
4. `llm_repair_v3.js` — LLM polish (z-ai SDK, resumable, sanity-guarded)
   → `data/llm_repairs_v3.jsonl`.
5. `merge_llm_v3.py` — apply repairs (`text_original` kept, flags set),
   regenerate markdown + report.
6. `validate_v3.py` — schema/coverage/order/quality checks.
