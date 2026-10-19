# Edexcel IGCSE (9-1) Physics — RAG-Ready Dataset (4PH1)

Parsed from the scanned student book PDF (308 pages, image-only scan) with
**IBM Docling** (layout model + TableFormer + RapidOCR + CodeFormula V2 for
display equations), then structure-mapped and packed into RAG chunks.

**v1 is the deliverable: 736 chunks, 8 units / 28 chapters, validation
passed** (`validate_physics.py`: unique IDs, 28/28 chapters, 8/8 units, 0 body
order breaks, dual page numbering on every chunk, question typing page-anchored).

**LLM fidelity polish round 1 applied (2026-10-19):** this scan (RICOH MP
C4503) drops spaces between words scan-wide, so 300 noisiest chunks were
selected and 232 polished with a strict no-paraphrase OCR-repair pass
(originals preserved in `text_original`, `llm_repaired` flag set). See
"LLM polish" below. Validation re-run after polish: ALL CHECKS PASSED, and
the serving-critical anchor check (id / unit_no / chapter_no / content_type /
pdf_pages / book_pages / section vs pristine v1) reports 0 drift.

Source of record: `../source/student-book.pdf`,
sha256 `9b0783d9fe99790a08255eb1f2ebb6eab5833c03ef8e36dd51b7643ac68a313a`.

## Files

| File | Purpose |
|------|---------|
| `edexcel_igcse_physics_chunks_v1.jsonl` | **Main deliverable.** 736 chunks |
| `full_book_docling.md` | Human-readable full text with Unit/Chapter/section headings |
| `parse_report_v1.json` | Parse statistics + provenance (sha256, parser stack, polish counts) |
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
  "text": "...",
  "text_original": "...(only on llm_repaired chunks)",
  "llm_repaired": true
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

## LLM polish (round 1, 2026-10-19)

- **Why:** RapidOCR on this scan drops spaces between words
  ("therelationshipbetween", "PearsonEdexcel") — 62% of chunks carried at
  least one glued run, far above the chemistry scan's noise level.
- **Selection** (`pipeline/scripts/select_noisy_physics.py`): physics-adapted
  noise scoring — space-run / caps-glue / camel-glue classes plus the
  chemistry residual classes; question-typed chunks (chapter_questions /
  unit_questions) force-included. 300 selected of 736.
- **Repair** (`pipeline/scripts/llm_repair_physics.js`): strict no-paraphrase
  OCR-repair prompt whose PRIMARY job is restoring dropped spaces; physics
  units/equations (m/s², kg·m/s, N/kg, Ω, °C, v²) must survive verbatim;
  tables keep per-line pipe counts. Guards: length drift, refusal patterns,
  Unicode-unit non-decrease, and wording fidelity via whitespace-normalized
  token similarity (LCS ≥ 0.97) for prose; strict line/pipe discipline for
  tables. z-ai SDK, resumable JSONL, single worker with 429 backoff.
- **Result:** 232 of 300 polished (68 pending a quota-limited round 2;
  19 first-pass rejects re-queued under the wording-fidelity guard).
  Post-polish audit (`pipeline/scripts/audit_polish_physics.py`): on polished
  chunks, 18+ lowercase glue runs 1008 → 3 (residuals are legit long words:
  "thermoluminescence", "telecommunications", one front-matter URL line);
  camel glue 121 → 0; Unicode-unit regressions 0. Corpus-wide space-glue
  runs 1456 → 451 (unpolished remainder concentrated in the 68 round-2
  pending chunks and damp-typed back matter).
- **Merge** (`pipeline/scripts/merge_llm_physics.py`): applied in place,
  `text_original` preserved, `char_count` recomputed, full markdown +
  parse report regenerated, serving-critical anchor diff vs pristine v1
  snapshot = 0 drift. Repair evidence (per-id records incl. rejects with
  raw outputs) in `pipeline/evidence/`.
- **Round 2 protocol:** rerun `select_noisy_physics.py` (list unchanged),
  then `llm_repair_physics.js` (resume-safe), then
  `merge_llm_physics.py` + `audit_polish_physics.py` +
  `validate_physics.py`. No schema or id changes expected.

## Parser stack & provenance

- docling 2.33.0 pipeline: heron layout + RapidOCR + TableFormer + CodeFormula
  (formula enrichment), CPU, checkpointed per page (`../pipeline/` +
  `../docling_pages/`).
- Page-level hybrid: 305 pages docling 2.33; PDF 16–17 docling 2.133 (formula
  decode verified); PDF 14/20/21/307-region: tesseract fallback where the
  docling pipeline crashed or the page is blank (PDF 307 is genuinely blank).
- 33 pages re-parsed with formula enrichment OFF (CodeFormula crash bug) —
  their display equations appear as plain text, not LaTeX-decoded.

## Known limitations

- Diagrams/figures not captured (text-only); captions kept.
- Display-equation boxes: 63 formula regions detected; most decoded to LaTeX
  then Unicode (e.g. `v² = u² + 2×a×s`); where the region decode produced
  junk, the equation also survives in nearby body text.
- Space-drop repair is round-1 complete: 232/300 selected chunks polished;
  the remaining 68 keep their v1 text (originals unaffected) until round 2.
- 3 of 53 learning-objectives chunks carry intra-item newlines (audit cosmetic
  note from chemistry; mostly addressed here, trim further on next pass).
