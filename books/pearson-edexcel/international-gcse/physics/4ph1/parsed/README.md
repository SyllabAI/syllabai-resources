# Edexcel IGCSE (9-1) Physics — RAG-Ready Dataset (4PH1)

Parsed from the scanned student book PDF (308 pages, image-only scan) with
**IBM Docling** (layout model + TableFormer + RapidOCR + CodeFormula V2 for
display equations), then structure-mapped and packed into RAG chunks.

**v1 is the first deliverable: 736 chunks, 8 units / 28 chapters, validation
passed** (`validate_physics.py`: unique IDs, 28/28 chapters, 8/8 units, 0 body
order breaks, dual page numbering on every chunk, question typing page-anchored).

Source of record: `../source/student-book.pdf`,
sha256 `9b0783d9fe99790a08255eb1f2ebb6eab5833c03ef8e36dd51b7643ac68a313a`.

## Files

| File | Purpose |
|------|---------|
| `edexcel_igcse_physics_chunks_v1.jsonl` | **Main deliverable.** 736 chunks |
| `full_book_docling.md` | Human-readable full text with Unit/Chapter/section headings |
| `parse_report_v1.json` | Parse statistics + provenance (sha256, parser stack) |
| `load_rag.py` | Ingestion helpers: plain JSONL, filter, Chroma, LangChain, LlamaIndex |

## JSONL schema (v1, same 15-key grammar as chemistry 4CH1 v3)

```json
{
  "id": "phys_v1_u1_c5_pdf058_0090",
  "book_title": "Edexcel International GCSE (9-1) Physics Student Book",
  "author": "Brian Arnold, Penny Johnson, Steve Woolley",
  "unit_no": 1,
  "unit_name": "Forces and Motion",
  "chapter_no": 5,
  "chapter_title": "The turning effect of forces (physics only)",
  "section": "MOMENTUM",
  "content_type": "body",
  "book_pages": [48, 49],
  "pdf_pages": [58, 59],
  "char_count": 780,
  "text": "..."
}
```

- `book_pages` is `null` for front matter (PDF 1–10 have no book-page number;
  book page 1 = PDF 11, the Experimental Skills page). **Both numberings stay
  per-chunk** (serving-critical per PARSE_STANDARD.md).
- Every chunk starts with its section heading when it has one.

## Content types & RAG advice

| type | meaning | RAG advice |
|------|---------|-----------|
| `body` | teaching prose | keep |
| `key_point` | boxed rules/definitions | keep — high retrieval value |
| `learning_objectives` | spec-linked objectives (incl. PHYSICS ONLY sections) | keep |
| `worked_example` | EXAMPLE 1/2/3… boxes | keep |
| `exam_hint` | HINT / REMINDER boxes | keep |
| `extension_work` | EXTENSION WORK boxes (not examinable) | keep, mark non-examinable |
| `practical` | Practical boxes / required practicals | keep |
| `activity` | ACTIVITY n boxes | keep |
| `table_data` | markdown tables (data, unit tables) | keep |
| `chapter_questions` / `unit_questions` | question banks — **serving-critical: the serving split derives from these anchors** | keep for Q&A practice, else filter |
| `glossary`, `appendix` | definitions / reference (formulae sheet is Appendix B) | keep |
| `front_matter`, `divider`, `skills` | structural noise | filter out |
| `index` | back-of-book term index | filter out |

Recommended filter: `exclude_types={"index", "divider", "front_matter"}`.
This book has NO answers section (unlike chemistry 4CH1).

## Parser stack & provenance

- docling 2.33.0 pipeline: heron layout + RapidOCR + TableFormer + CodeFormula
  (formula enrichment), CPU, checkpointed per page (`../pipeline/` +
  `../docling_pages/`).
- Page-level hybrid: 305 pages docling 2.33; PDF 16–17 docling 2.133 (formula
  decode verified); PDF 14/20/21/307-region: tesseract fallback where the
  docling pipeline crashed or the page is blank (PDF 307 is genuinely blank).
- 33 pages re-parsed with formula enrichment OFF (CodeFormula crash bug) —
  their display equations appear as plain text, not LaTeX-decoded.
- No LLM polish applied (`n_llm_polished: 0`).

## Known limitations

- Diagrams/figures not captured (text-only); captions kept.
- Display-equation boxes: 63 formula regions detected; most decoded to LaTeX
  then Unicode (e.g. `v² = u² + 2×a×s`); where the region decode produced
  junk, the equation also survives in nearby body text.
- RapidOCR on this scan (RICOH) drops some spaces between words
  ("isnot avectorquantity") — more than on the chemistry scan. A constrained
  LLM fidelity polish (chemistry v2/v3 pattern, originals preserved) is the
  ready remedy if needed.
- 3 of 53 learning-objectives chunks carry intra-item newlines (audit cosmetic
  note from chemistry; mostly addressed here, trim further on next pass).
