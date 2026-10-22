# YPH11 SB1 — Method & Findings (T-PARSE-YPH11-1, 2026-10-22)

First IAL (two-book course) lane; first full playbook-driven parse after the
playbook bootstrap. Route: OCR (image-only print replica) via the proven 4PH1
stack, with three lane-specific problems solved: (1) a rewritten PyPI package
mine, (2) a blank-formula-region bug at 4× the physics scale, (3) the first
multi-book-course chunk-ID law.

## Decision log

- **D-1 — queue order.** CATALOG tracker row 3 (YPH11 SB1+SB2, both SOURCE) is
  the first unparsed row and heads §4.2; the operator directive "start the next
  book from CATALOG queue" resolves to it. SB1 parsed first; SB2 is a separate
  follow-on task (two per-book corpora per the multi-book law note).
- **D-2 — workspace reset #3 (PM-5).** Packages + caches wiped again;
  data/yph11 + scripts survived. Environment rebuild order of record:
  CPU-index torch FIRST (`torch==2.14.1+cpu` + `torchvision==0.29.1+cpu`
  forced from download.pytorch.org/whl/cpu), then docling, then
  rapidocr-onnxruntime + onnxruntime. PyPI torchvision is CUDA-linked and
  breaks docling-ibm-models' layout import (RTDetrImageProcessor via
  torchvision::nms) — see L-016.
- **D-3 — PyPI docling version mine (new).** Today's PyPI `docling==2.133.0`
  is a SLIM-REBUILD architecture (meta package + docling-slim, no
  `DocumentConverter`, broken CLI entry point) — NOT the chemistry lane's
  formula-decoding 2.133.0. `docling==2.33.0` still serves the old
  architecture and remains the base-corpus pin. The old-arch formula-decoder
  pinned in the playbook (§4.3) is no longer installable from PyPI — see
  L-017 and the slim-2.133 dead-end record below.
- **D-4 — page law.** `book = pdf − 11`, front matter roman `= pdf − 1`,
  confirmed 5 ways: roman headers (iii=PDF4…xi=PDF12), TOC cross-checks
  (STANDARD UNITS b4=PDF15, ESTIMATION b6=PDF17, 1 MOMENTUM b48=PDF59),
  PREPARING b200=PDF211, INDEX header digit "211" printed on PDF 222.
  Book page 1 does not exist in the PDF (print blank omitted); arabic starts
  at book 2 = PDF 13. Front matter chunks carry `book_pages: null`.
- **D-5 — structure map.** Top level = 4 TOPICS (the IAL unit mapping per the
  book's own assessment tables: Unit 1 exams Topics 1-2, Unit 2 Topics 3-4).
  The book's own word for 1A-4B is CHAPTER. Chunk grammar: u = topic (1-4),
  c = chapter (1-11 sequential). No standalone unit dividers — the topic
  divider shares the first-chapter opener page (e.g. TOPIC 3 + 3A on one page).
- **D-6 — marker census (production stack, per L-013).** 223/225 pages carry
  glue runs (5,476 long runs) — the RICOH-class space-drop damage is
  scan-wide here too, so an LLM polish round is mandatory in the plan.
  Hudson marker families: LEARNING OBJECTIVES, WORKED EXAMPLE, EXAM HINT,
  LEARNING TIP, THINKING BIGGER (+TIP), MATHS SKILLS FOR THIS CHAPTER,
  SUBJECT VOCABULARY, CHECKPOINT, PRACTICAL SKILLS, DID YOU KNOW?, CORE
  PRACTICAL, SPEC REFERENCE chips, and WaaP skill tags (INTERPRETATION/
  PROBLEM SOLVING/CRITICAL THINKING/…). Additive types: `checkpoint`,
  `subject_vocabulary`, `thinking_bigger`, `maths_skills→skills`.
- **D-7 — formula-region rescue (the big one).** docling 2.33.0 detects
  formula regions but emits EMPTY text (§4.3 bug): 267/272 formula items
  blank across 76 pages; unlike 4PH1 (equations survived as plain text),
  display equations here were truly lost. Attempted remedies, in order:
  (a) rapidocr 3.9.2 stack — wrong package for docling 2.33 (needs
  rapidocr-onnxruntime 1.4.4); (b) formula-OFF re-parse — regions still
  blanked (layout model classifies before OCR text is emitted); (c) today's
  slim docling 2.133.0 — no local converter, dead end (D-3); (d) direct
  CodeFormulaV2 crops via transformers — technically alive but ~40 s/crop on
  2 CPU cores (≈3 h) AND hallucinated plausible-looking physics
  ("a₁+b₁+c₁+d₁=111" for a clean refraction crop) that a math-symbol guard
  cannot catch. **Adopted: verbatim manual transcription from rendered
  pages** (the agent reads the page images and transcribes the missing
  equations — transcription-only, zero hallucination). 253 orphans + 7
  late-found = 260 equations across 75 pages, sidecar-logged in
  `pipeline/evidence/manual_formulas.jsonl`, applied by
  `manual_formula_ws_yph11.py` with idempotent, position-verified patching
  (bbox + prev/next text alignment). 5 remaining empty regions were
  adjudicated against the renders as decorative (SKILLS badge) or
  region-split slivers (content present in the sibling item).
- **D-8 — ID grammar for a two-book course.** `yph1_v1_u<unit|0>_c<chapter|0>
  _pdf<pdfpage:03d>_<block:04d>`; SB2 will use `yph2_v1_` so the two corpora
  stay globally disjoint. Book-level prefix chosen over course-level because
  chunk ids are immutable and the hub's per-book file law (T-MIG-140) is
  still pending.
- **D-9 — front-matter typing guard.** The About-this-book pages describe the
  book's features and carry an "EXAM PRACTICE" heading; naive marker typing
  produced two phantom `chapter_questions` chunks on PDF 8. Chunker now keeps
  `front_matter` base type on front-matter pages regardless of marker hits.
- **D-10 — index/glossary behavior.** The 4-column index (book 211-213) parses
  as TableFormer tables → `table_data` chunks (same as 4PH1's index pages);
  validator checks page coverage (pdf 222-224) rather than an `index` type.

## Findings

- Scan class: space-drop glue scan-wide (63% of chunks) + dense-table index
  pages needing 300+ s/page under the no-formula retry. Peak RSS 3.4-3.6 GB
  (tight on the ~3 GB workspace; batch windows stayed ≤ 30 pages).
- Ground truth for later lanes: a print-replica PDF can OMIT blank printed
  pages (here book page 1) — offset laws must be confirmed on BOTH ends
  (front matter AND a late printed header digit), not just the TOC.
- The slim-2.133 mine invalidates the playbook's literal version pins; the
  repair ladder in D-7 is the transferable asset.

## Environment of record (2026-10-22)

python 3.12.15 venv; torch 2.14.1+cpu; torchvision 0.29.1+cpu (forced);
docling 2.33.0 (docling-core 2.103.1, docling-ibm-models 3.15.0,
docling-parse 4.7.3); rapidocr-onnxruntime 1.4.4; onnxruntime 1.31.0;
transformers 4.57.6; artifacts `data/models` (1.0 GB; CodeFormulaV2 611 MB
downloaded for the rejected crop experiment, kept for SB2 reconsideration).
