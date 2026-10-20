# Edexcel IGCSE (9-1) Biology — RAG-Ready Dataset (4BI1)

Parsed from the **native text layer** of the student book PDF (357 book pages
rendered as 179 landscape 2-up spreads) with **PyMuPDF 1.26.7** — the first
**text-layer lane** in `books/`: the source is a Word-2016 → Acrobat
print-replica, NOT a scan, so the IBM Docling OCR stack was not used (see
`../pipeline/METHOD_AND_FINDINGS.md` for the full method and findings).

**v1 is the deliverable: 869 chunks, 6 units / 22 chapters, validation ALL
CHECKS PASSED** (`validate_biology.py`: unique IDs, 15-key grammar, 22/22
chapters, 6/6 units, 0 body order breaks, dual page numbering + 2-up law
coherence, question typing anchored to all 22 probed chapter ranges + 6 unit
banks, answers coverage 329–348, size bounds).

**LLM fidelity polish round 1 — PARTIAL (quota-walled):** 363 chunks selected
(all 171 question-typed chunks + 192 garble-scored); **91 applied** before an
account-level gateway 429 wall stopped the run (books/README.md PM-3). The
runner (`../pipeline/scripts/llm_repair_biology.js`) is resumable — re-running
it continues from the append-only JSONL. Polished chunks carry
`text_original` + `llm_repaired: true`; the anchor diff vs the pristine
corpus reports **0 drift** on every serving-critical field.

Source of record: `../source/student-book.pdf`,
sha256 `974ad65d913108b9caa98df9eda1584e546177854bcd5efa6d8642797d093006`.

## Files

| File | Purpose |
|------|---------|
| `edexcel_igcse_biology_chunks_v1.jsonl` | **Main deliverable.** 869 chunks |
| `full_book_textlayer.md` | Human-readable full text with Unit/Chapter/section headings |
| `parse_report_v1.json` | Parse statistics + provenance (sha256, parser stack, polish state) |
| `load_rag.py` | Ingestion helpers: plain JSONL, filter, Chroma, LangChain, LlamaIndex |

## JSONL schema (v1 — 15-key grammar, flat keys)

```json
{
  "id": "bio_v1_u1_c1_pdf006_0059",
  "book_title": "Edexcel International GCSE (9-1) Biology Student Book",
  "author": "Philip Bradfield, Steve Potter",
  "unit_no": 1,
  "unit_name": "Organisms and Life Processes",
  "chapter_no": 1,
  "chapter_title": "Life processes",
  "section": "LEARNING OBJECTIVES",
  "content_type": "learning_objectives",
  "book_pages": [3, 3],
  "pdf_pages": [6, 6],
  "char_count": 912,
  "text": "...",
  "text_original": "...(only on llm_repaired chunks)",
  "llm_repaired": true
}
```

- **2-up law:** one PDF page (spread) carries TWO book pages — left half =
  even page `2s−10`, right half = odd page `2s−9`. `pdf_pages` is the spread
  range, `book_pages` the covered book-page range (null for front/back
  matter). **Both numberings stay per-chunk** (serving-critical per
  PARSE_STANDARD.md).
- Every chunk starts with its section heading when it has one.

## Content types & RAG advice

| type | meaning | RAG advice |
|------|---------|-----------|
| `body` | teaching prose | keep |
| `key_point` | boxed rules/definitions (incl. garbled "KEV POINT" forms) | keep — high retrieval value |
| `learning_objectives` | spec-linked objectives (17/22 chapters; 5 openers carry outline-graphic LO boxes with no text) | keep |
| `did_you_know` | DID YOU KNOW? enrichment boxes (new type this lane) | keep, mark enrichment |
| `exam_hint` | HINT boxes | keep |
| `extension_work` | EXTENSION WORK / LOOKING AHEAD boxes (not examinable) | keep, mark non-examinable |
| `practical` | Practical boxes / required practicals | keep |
| `safety` | Safety Note boxes | keep |
| `biology_only` | BIOLOGY ONLY label boxes (content beyond Science Double Award; new type this lane) | keep; filter IN for 4BI1, filter OUT for Double Award serving |
| `chapter_questions` / `unit_questions` | question banks — **serving-critical: the serving split derives from these anchors** | keep for Q&A practice, else filter |
| `answers` | ANSWERS section (book 329–348, by unit then chapter — present here, unlike 4PH1) | keep for self-assessment, else filter |
| `glossary`, `appendix` | definitions / Appendices A-B (experimental skills, command words) | keep |
| `front_matter`, `divider`, `skills` | structural noise (cover, contents, course structure, about-this-book, assessment overview, unit dividers) | filter out |
| `index` | back-of-book term index (book 320–328) | filter out |

Recommended filter: `exclude_types={"index", "divider", "front_matter", "skills"}`.

## Known limitations (v1)

- Chemical formulas keep plain digits (`CO2`, `C6H12O6`) — span-size-based
  sub/superscript recovery is unsafe on this source (garbled bullets mimic
  small spans); additive v2 candidate (vertical-offset analysis).
- Residual broken-CMap garbles/icon junk remain in the 272 polish-pending
  chunks (quota wall) and inside 2 front-matter chunks (stylized cover art).
- 5 chapter openers (ch9/10/14/15/19) have no extractable LO text (their
  objectives are outline graphics in the PDF).

## Stats snapshot

- chunks 869 · size min/median/max 20/943/2095 · 0 over HARD_MAX 2400
- types: body 344 · chapter_questions 124 · answers 65 · did_you_know 59 ·
  key_point 58 · unit_questions 45 · extension_work 34 · glossary 29 ·
  learning_objectives 21 · appendix 21 · index 20 · front_matter 15 ·
  exam_hint 11 · safety 9 · divider 6 · practical 5 · biology_only 2 · skills 1
- per unit: u1 81 · u2 240 · u3 121 · u4 91 · u5 132 · u6 53 (rest = non-unit sections)
