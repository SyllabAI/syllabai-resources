# Edexcel International GCSE (9-1) Chemistry Student Book → RAG-Ready Corpus

**Project report: method, findings & decisions**

Date: 2026-10-04 → 2026-10-05
Source book: *Edexcel International GCSE (9-1) Chemistry Student Book*, Jim Clark
(originally from github.com/SyllabAI/syllabai-resources)

---

## 1. Objective

Parse the student-book PDF into a RAG-ingestible corpus: JSONL chunks with
heading-based segmentation, chapter + page metadata, text-only content, and
normalized chemical notation — accurate enough that a retrieval system returns
readable, chemically correct passages.

## 2. Source material — key finding #0: the PDF has NO text layer

`data/chemistry_book.pdf` — 54.3 MB, 383 PDF pages.

- Produced by "Adobe Image Conversion Plug-in": **every page is a single
  full-page raster image. Zero extractable text characters.** (`scripts/inspect_pdf.py`)
- The embedded outline is fake (per-page bookmarks, not a real TOC).
- Consequence: any parser must effectively **OCR the whole book**; "just use
  pdfplumber/PyMuPDF" was never an option.

## 3. Environment constraints — decision driver

| Resource | Available | Implication |
|----------|-----------|-------------|
| GPU | **none** | Chandra OCR (needs 16–24 GB VRAM) — infeasible |
| RAM | 3 GB | MinerU (needs ~16 GB RAM) — infeasible |
| CPU / disk | 2 cores / 9.2 GB free | CPU-only pipelines only |
| Internet | OK | Docling + onnxruntime models downloadable |

User had proposed 4 candidate parsers (Chandra / IBM Docling / MinerU /
PaddleOCR). **Decision: IBM Docling (CPU mode)** — best quality per GB of RAM;
PaddleOCR rejected (would require hand-written layout + ordering glue that
Docling already provides).

## 4. Pipeline evolution — three full passes

The corpus was rebuilt three times. Each version is preserved for diffing.

### v1 — Tesseract OCR pipeline (Task 1)

1. **OCR calibration** (`ocr_calibrate.py`): scale 3.0 (≈216 DPI) ≈ scale 4.0
   quality (word-ratio ~0.93) at ~6.3 s/page, 2 workers. Resumable batch
   (`ocr_batch.py`) → `data/ocr_pages/page_*.txt` (383 files).
2. **Structure reverse-engineering** (`scan_structure.py`, `probe2–6.py` →
   `book_structure.py`): 4 units, **29 chapters**; chapter start = its
   LEARNING OBJECTIVES page; titles/book-pages read from the book's own
   contents pages (PDF 4–6) and cross-checked against the answers section.
   **Book page = PDF page − 9** (PDF 1–11 = unnumbered front matter).
   Fixed a coverage gap: unit-1 questions end at PDF 130, not 129.
3. **Cleaning** (`parse_lib.py`): running header/footer removal, roman-numeral
   junk, ligatures, de-hyphenation across line breaks, rejoining of formulas
   split by OCR using an **element-symbol whitelist**.
4. **Chunking** (`parse_book.py`): split at ALL-CAPS sub-headings; pack blocks
   to 350–1600 chars (hard max 2400); sentence/word fallback splits.
5. **Output**: 640 chunks, validation passed (`validate_output.py`: unique IDs,
   29/29 chapters, 0 page-order breaks, avg word-ratio 0.933).

**Finding #1:** Tesseract quality was structurally inadequate for chemistry —
subscripts became commas/semicolons (`2H,(g)`), O read as 0, multi-column
reading order interleaved body text with sidebars, diagrams lost.

### v2 — Mechanical + LLM repair of v1 (Task 2)

User feedback: text "did not make sense". Decision taken: **NOT a wholesale LLM
paraphrase-rewrite** (derivative-work risk on copyrighted text, hallucination
risk for chemistry, RAG fidelity loss). Instead, a **fidelity-preserving repair**:

1. `audit_quality.py` scored all 640 chunks for corruption classes → dominant:
   state-paren subscript commas (348), junk/punct-debris lines (262),
   semicolon-subscript formulas (53), zero-for-O (53).
2. `repair_v2.py` mechanical fixes (936 junk lines dropped, 242 prefixes
   cleaned) → `chunks_v2.jsonl`.
3. LLM pass with a **strict "fix transcription errors only, never reword"**
   prompt (`llm_repair.js`, z-ai SDK): 113 chunks repaired in 2 rounds with
   sanity guards (length drift, refusals). `merge_llm.py` applied repairs,
   keeping `text_original`.
4. Result: formula garbles 348 → 0, junk fragments 262 → 12 (residual class
   false-positive-prone).

**Finding #2:** post-hoc repair can fix *some* OCR damage but cannot recover
what Tesseract never captured (reading order, display equations). The only
real fix was a better parser → v3.

### v3 — Docling rebuild, final version (Tasks 3–4)

1. **Backend shootout** (`docling_test*.py`) on sample pages with formulas:
   - RapidOCR (onnxruntime): **26.8 s/page**, much cleaner text.
   - Tesseract backend: 11.3 s/page, garbled boxes/formulas.
   - **Decision: quality over speed → RapidOCR.**
2. **Formula enrichment ON** (CodeFormula VLM): display equations decoded to
   LaTeX, then converted to Unicode chemistry (42.8 s/page, peak RSS ~3.4 GB).
3. **Full-book parse** (`docling_full.py`): per-page JSON checkpoints
   (`data/docling_pages/`); 5-page fresh processes chained per run to stay
   under the 3 GB RAM / shell-timeout limits. **383/383 pages, 0 errors.**
4. **Chunker** (`parse_docling.py`): `latex_to_chem()` (sub/superscripts,
   arrows `→`/`⇌`, fractions, state symbols), sidebar double-OCR dedup,
   heading dedup, `(A,)`→`(Ar)` fixes, structure mapping via
   `book_structure.py`, marker-based content typing, 350–1600 char packing,
   small-chunk merge, oversized-block sentence splitting. Bugs fixed during
   dev: stale-segment duplicate flush, front-matter `book_pages=None`,
   LaTeX hallucination drops (>600 raw chars), arrow-word junk.
5. **LLM polish of residual noise** (Task 4): `select_noisy_v3.py` scored v3
   chunks (fixed 2 false-positive sources first: table borders, cell padding).
   90 chunks selected → `llm_repair_v3.js` with extended no-paraphrase prompt
   (tables keep pipe/row counts; formulas restorable only when unambiguous:
   `CH8→C3H8`, `CI-CI→Cl-Cl`). Quota-429 backoff handling. **87 repaired,
   3 rejected (originals kept)**; `merge_llm_v3.py` applied in place with
   `text_original` preserved.
6. **Validation** (`validate_v3.py`): **ALL CHECKS PASSED** — unique IDs,
   29/29 chapters, 0 order breaks, 0 LaTeX remnants, 214 chunks with Unicode
   subscripts, 184 with reaction arrows, 113 table_data chunks.

## 5. Quality comparison (findings)

| Aspect | v1 Tesseract | v2 repaired | v3 Docling (final) |
|---|---|---|---|
| Chunks | 640 | 640 | **1234** |
| Formulas | `2H,(g)` garble (348×) | repaired to 0 | **native `H₂O`, `C₂H₆`, `Aᵣ`** |
| Display equations | lost/garbled | unchanged | **`2K(s) + 2H₂O(l) → 2KOH(aq) + H₂(g)`** |
| Reading order | multi-column interleave | unchanged | layout-model ordered |
| Tables | text debris | cleaned debris | **113 structured markdown tables** |
| Equilibrium arrows | lost | lost | **`⇌` preserved** |
| LLM-touched chunks | — | 113 | 87 (all with `text_original`) |
| Validation | pass | pass | **pass** |

## 6. Decision log

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | OCR route mandatory | PDF is image-only (finding #0) |
| 2 | Docling over Chandra/MinerU/Paddle | no GPU / 3 GB RAM; Docling = production quality at CPU |
| 3 | RapidOCR over Tesseract backend | 26.8 vs 11.3 s/page — chose quality |
| 4 | Formula-enrichment VLM ON | equations are core chemistry content |
| 5 | Declined wholesale LLM rewrite | copyright derivative + hallucination + fidelity risks; used constrained OCR-repair instead |
| 6 | Structure from the book's own TOC/dividers | more reliable than generic regex; gives real chapter metadata |
| 7 | Keep v1/v2 alongside v3 | enables diffing and rollback |
| 8 | `text_original` always preserved | auditability of every LLM touch |
| 9 | Uncertain equations dropped (140) rather than guessed | wrong chemistry is worse than missing text (281 clean kept) |
| 10 | Chained 5-page fresh processes | stay under 3 GB RAM and shell timeout; checkpointed per page |

## 7. Package inventory

```
edexcel_igcse_chemistry_rag_package/
├── METHOD_AND_FINDINGS.md        ← this report
├── worklog.md                    ← raw chronological agent worklog
├── chemistry_book.pdf            ← original source (54.3 MB, 383 pp, image-only)
├── download/rag_chemistry/       ← DELIVERABLES
│   ├── edexcel_igcse_chemistry_chunks_v3.jsonl   ← MAIN: 1234 chunks
│   ├── full_book_docling.md                      ← full book, readable
│   ├── parse_report_v3.json                      ← v3 stats
│   ├── edexcel_igcse_chemistry_chunks_v2.jsonl   ← v2 (diffing)
│   ├── full_book_clean_v2.md
│   ├── edexcel_igcse_chemistry_chunks.jsonl      ← v1 (diffing)
│   ├── full_book_clean.md
│   ├── parse_report.json
│   ├── load_rag.py               ← ingestion helpers (plain/Chroma/LangChain/LlamaIndex)
│   └── README.md                 ← schema, RAG advice, limitations
├── scripts/                      ← full pipeline (v1+LLM+v3)
│   ├── inspect_pdf.py            ← PDF inspection
│   ├── ocr_calibrate.py          ← Tesseract DPI calibration
│   ├── ocr_batch.py              ← resumable Tesseract OCR
│   ├── scan_structure.py, probe2–6.py, book_structure.py
│   ├── parse_lib.py, parse_book.py, validate_output.py   ← v1 parser
│   ├── audit_quality.py, repair_v2.py                    ← v2 mechanical
│   ├── select_llm_chunks.py, llm_repair.js, merge_llm.py ← v2 LLM (Node, z-ai SDK)
│   ├── docling_test*.py, docling_full.py                 ← v3 Docling parse
│   ├── parse_docling.py, validate_v3.py                  ← v3 chunker/validator
│   └── select_noisy_v3.py, llm_repair_v3.js, merge_llm_v3.py ← v3 LLM polish
└── data/
    ├── ocr_pages/                ← v1: 383 Tesseract page texts
    ├── docling_pages/            ← v3: 383 Docling per-page JSON checkpoints
    ├── docling_test_*.md         ← backend-shootout sample outputs
    ├── llm_repairs*.jsonl        ← all LLM repair records (auditable)
    ├── llm_repair_ids*.json      ← selected chunk IDs
    └── quality_audit.json        ← v1 corruption-class audit
```

## 8. JSONL schema (v3)

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
  "text": "..."
}
```

`content_type` values: `body`, `key_point`, `learning_objectives`,
`worked_example`, `exam_hint`, `activity`, `practical`, `did_you_know`,
`safety`, `table_data`, `chapter_questions`, `unit_questions`, `answers`,
`glossary`, `appendix`, `divider`, `skills`, `front_matter`, `index`.

Recommended RAG filter: exclude `{"index", "divider", "front_matter"}`.

## 9. Reproduction guide

```bash
pip install docling docling-core onnxruntime   # CPU
# 1. Docling parse (checkpointed; ranges e.g. 1 5, 6 10, ... due to RAM caps)
python scripts/docling_full.py 1 383
# 2. Chunk + structure-map + LaTeX→Unicode chemistry
python scripts/parse_docling.py
# 3. Optional LLM polish (needs z-ai SDK): select → repair → merge
python scripts/select_noisy_v3.py
node scripts/llm_repair_v3.js
python scripts/merge_llm_v3.py
# 4. Validate
python scripts/validate_v3.py
```

## 10. Known limitations

- Diagrams/figures are not captured (text-only deliverable); captions kept.
- 140 uncertain display equations were dropped rather than risk wrong output.
- 87 of 1234 chunks carry LLM polish — originals in `text_original`;
  spot-check chemistry-critical passages before high-stakes use.
- Docling occasionally duplicates/drops a decorative element; consecutive
  duplicates are collapsed already.
- `book_pages` is `null` for front matter (PDF 1–11).
