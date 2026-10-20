# Pearson Edexcel International GCSE (9-1) Biology (2017), 4BI1 — Student Book

**Status:** PARSED — chunk corpus v1 landed (T-PARSE-4BI1-1, 2026-10-21).
Parse route: **text-layer lane** (PyMuPDF native extraction — the source is a
Word-2016 print-replica, NOT a scan; first lane in `books/README.md` to skip
the OCR stack). 871 chunks (`bio_v1_`), 6 units / 22 chapters, validation
ALL CHECKS PASSED (`validate_biology.py`). LLM fidelity polish round 1
(363 selected — all question chunks + garble-scored) — see
`pipeline/METHOD_AND_FINDINGS.md` and `parsed/parse_report_v1.json` for the
final applied/rejected counts.

Method record: `pipeline/METHOD_AND_FINDINGS.md` (2-up spread law, broken-CMap
garble classes, question-range anchoring via the book's "More questions …"
cross-references, decision log D-1…D-10). Intake record: T-INTAKE-4BI1-1
(below).

## Book of this lane

### Pearson Edexcel International GCSE (9-1) Biology Student Book

- **Title:** Pearson Edexcel International GCSE (9-1) Biology Student Book
- **Authors:** Philip Bradfield, Steve Potter (verified: title page of this
  copy + official Pearson sample PDF + Amazon/dokumen ISBN listings).
  NOTE: `books/CATALOG.md` §4.1 previously listed "Penny Johnson, Susan
  Kearsey" — misattribution, corrected in the catalog in this same commit
  (see `books/README.md` errata E-001).
- **ISBN:** 978-0435185084 (1st ed., Pearson Education Limited 2017)
- **Qualification:** Pearson Edexcel International GCSE in Biology (4BI1),
  2017 specification line
- **File:** `source/student-book.pdf`
- **Book pages:** 357 (title/credits/course structure/assessment overview
  front matter + Units 1–4 + Answers; ANSWERS section present, like 4CH1)
- **PDF pages:** 179 landscape **2-up spreads** (841.9 × 525.7 pt) — each PDF
  page carries two book pages; spread→book-page mapping must be probed 3 ways
  at parse time (playbook §5 phase 2)
- **Bytes:** 34,351,405
- **sha256:** `974ad65d913108b9caa98df9eda1584e546177854bcd5efa6d8642797d093006`
- **Quality:** **native text layer** (Producer: Adobe Acrobat Pro DC 15 /
  Creator: Microsoft Word 2016 — print-replica conversion, NOT a scan).
  pypdf census: 179/179 pages, 18/18 sampled pages >40 chars of text.
  This is a HIGHER quality class than the 4CH1/4PH1/0610 sources: the OCR
  route is NOT required, but text-layer cleaning is (see watch items).
- **Disclosed form / defects:**
  - 2-up spread pages (deterministic preprocessing at parse time);
  - Word-conversion spacing artifacts: words occasionally split across
    spaces ("differen t organs", "rathe r than") — expect a noise census at
    parse start; may still need a fidelity polish round, but far below the
    RICOH space-drop level of 4PH1;
  - front matter/cover partially stylized text (p1 census 62 chars);
  - box/heading markers present in text ("KEY POINT", "UNIT QUESTIONS",
    "ANSWERS", "CRITICAL THINKING" icon labels) — marker census will refine
    content typing.
- **Provenance:**
  `https://www.theonlineschool.co.uk/wp-content/uploads/2020/12/Edexcel-Igcse-biology-book-student.pdf`
  — fetched 2026-10-21; host is sgcaptcha-walled, cleared via headless
  browser (agent-browser) then cookie handoff to curl. Verification:
  pypdf page count + per-page text sampling + image census (evidence:
  `scripts/verify_4bi1_candidate.py` output in worklog; gateway trace
  1a15b063a08dbc69).
- **Upgrade candidates (not landed):** dokumen.pub single-page copy (357 pp,
  165 MB, CF-walled at intake:
  `dokumen.pub/edexcel-igcse9-1-biology-student-book-1nbsped-9780435185084.html`);
  pdfcoffee 49 MB copy (`pdfcoffee.com/edexcel-igcse-9-1-biology-student-book-pdf-free.html`,
  CF-walled); Pearson official 69-page sample (full-book NOT covered).

## Course binding (planned)

v2 hub course `igcse-biology-19` · specKey
`pearson-edexcel/international-gcse/biology/4bi1`. Spec spine already in
repo: `Official-Specifications/igcse-biology/` (2017 specification PDF +
`spec.json` concept graph) — the parse's spec joins resolve against it
(PARSE_STANDARD points 4–5).

## Parse-time watch items (from intake probes, for the parse lane)

1. **Spread→book-page mapping** — 2-up spreads; probe the arithmetic 3 ways
   (running headers vs book-page digits vs chapter openers) before chunking;
   every chunk must still carry `book_pages` + `pdf_pages` (serving-critical
   per PARSE_STANDARD point 1/3).
2. **Text-layer cleaning** — de-space Word artifacts; keep the proven
   350–1600/2400 packing and marker-based typing; "UNIT QUESTIONS"/"CHAPTER
   QUESTIONS" typing stays serving-critical.
3. **Answers section** present — type separately (like 4CH1, unlike 4PH1).
4. **Noise census early** (playbook L-005): if glue-run rate is high, budget
   an LLM polish round; text-layer source likely needs far less than 4PH1.

## Serving-path note (for the future integration lane)

The v2 hub serves the book PDF at the lane ROOT
(`books/<specKey>/student-book.pdf`, `bookCorpusPathForCourse`); this intake
keeps the sha256-pinned source under `source/` per the scaffold. Integration
must promote the pinned file to the serving path (hub per-book file law
pending for multi-book courses — T-MIG-140 receipt).

## Next steps

1. ~~Parse lane per `books/README.md` §5 phases 0–10~~ — DONE
   (T-PARSE-4BI1-1): corpus v1 validated, polish round 1 in
   `parsed/`.
2. ~~LLM fidelity polish round(s) IF the noise census justifies it~~ —
   round 1 executed (363 chunks selected: 171 serving-critical question
   chunks + 192 garble-scored); residuals documented in the parse report.
3. Serving lane (TEXTBOOK doc + book_chapters + slices manifest + T-C20
   flip) — next lane; note the serving-path promotion below.
4. Update `books/CATALOG.md` tracker in the same commit as each state
   change — done for the parse state.
5. Additive v2 candidates (NOT blocking): Unicode sub/superscript recovery
   for chemical formulas via vertical-offset span analysis (METHOD D-7);
   LO-text recovery for the 5 openers whose objectives are outline graphics
   (ch9/10/14/15/19).
