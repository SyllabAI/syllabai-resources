# Worklog

---
Task ID: 2
Agent: main (Super Z)
Task: Repair the parsed chemistry-book corpus (v1 chunks had OCR corruption that
"did not make sense"); user asked for an LLM rewrite. Delivered a
fidelity-preserving repair instead (no paraphrase-rewrite of the copyrighted text).

Work Log:
- Loaded LLM skill; z-ai-web-dev-sdk installed locally in scripts/ (npm).
- Built audit_quality.py: scored 640 chunks for corruption classes. Dominant:
  state-paren subscript commas (348), junk/punct-debris lines (262),
  semicolon-as-subscript-3 formulas (53), zero-for-O (53).
- repair_v2.py (mechanical): state_comma 53, zero_O 53, semi 74, tenq 3 fixes,
  936 junk lines dropped, 242 prefixes cleaned; added breadcrumb context line
  to every chunk; text_original preserved. -> chunks_v2.jsonl (354/640 changed).
- LLM fidelity pass (llm_repair.js + z-ai SDK): strict OCR-repair system prompt
  (fix transcription errors only, never reword), 3 concurrent -> 2 workers with
  429 backoff, resumable results file, sanity checks (length drift, refusals).
  Round 1: 80 chunks (all ok after retries). Round 2: 33 residual-garble chunks.
  Total 113 chunks llm_repaired.
- merge_llm.py applied repairs (breadcrumb re-attached, text_original kept) and
  re-rendered full_book_clean_v2.md. Final audit: formula garbles 348 -> 0,
  semi 53 -> 0, zero-for-O 53 -> 2, junk fragments 262 -> 12 (remaining metrics
  are false-positive-prone patterns like broken_apostrophe).
- README.md rewritten for v2 (schema, repair provenance, ingestion advice).

Stage Summary:
- Deliverable v2: download/rag_chemistry/edexcel_igcse_chemistry_chunks_v2.jsonl
  (640 chunks, 113 LLM-repaired, originals in text_original) +
  full_book_clean_v2.md + updated README/load_rag.py.
- Decision: declined wholesale LLM paraphrase-rewrite (derivative + hallucination
  risk for chemistry + RAG fidelity loss); used constrained OCR repair instead.

---
Task ID: 1
Agent: main (Super Z)
Task: Parse the Edexcel International GCSE (9-1) Chemistry Student Book PDF
(github.com/SyllabAI/syllabai-resources) into RAG-ready chunks.

Work Log:
- Loaded pdf skill + briefs/process.md; clarified requirements (defaults: JSONL,
  heading-based chunking, chapter+page metadata, text-only, aggressive cleaning,
  generic RAG target, normalized formulas).
- Downloaded 54.3 MB PDF to data/chemistry_book.pdf (383 pages).
- Inspected: image-only scan (Adobe Image Conversion Plug-in), 0 text chars,
  1 full-page image per page, fake per-page outline -> OCR pipeline required.
- Calibrated Tesseract 5.5.0 OCR: scale 3.0 (216 DPI) ~= scale 4.0 quality
  (word-ratio ~0.93), ~6.3 s/page with 2 workers. Ran resumable batch OCR
  (scripts/ocr_batch.py) in 3 foreground chunks -> data/ocr_pages/*.txt (383 files).
- Reverse-engineered book structure via probes (scripts/probe2-6.py): 4 units,
  29 chapters (chapter start pages = LEARNING OBJECTIVES pages, titles + book
  pages from contents pages PDF 4-6, cross-checked vs answers groupings),
  unit question ranges, chemistry-only skills pages, appendices/glossary/index/
  answers back matter. Offset: book page = pdf page - 9. Fixed coverage gap
  (unit 1 questions end at PDF 130, not 129).
- Built parser: scripts/book_structure.py (structure map) + parse_lib.py
  (cleaning: running header/footer removal, roman-numeral junk, de-hyphenation,
  ligatures, element-symbol-whitelisted formula rejoining) + parse_book.py
  (block segmentation at all-caps sub-headings + markers, sentence/line/word
  fallback splitting, chunk packing 350-1600 chars, hard max 2400).
- Outputs in download/rag_chemistry/: edexcel_igcse_chemistry_chunks.jsonl
  (640 chunks / 1.24 MB), full_book_clean.md (0.93 MB, 4 unit + 46 section
  headings), load_rag.py (plain/filter/Chroma/LangChain/LlamaIndex helpers),
  parse_report.json, README.md.
- Validation (scripts/validate_output.py): 640 unique ids, 0 schema errors,
  29/29 chapters covered, avg word-ratio 0.933, 0 page-order breaks,
  size min 80 / max 2463 / avg 1361 chars, 16 content types.

Stage Summary:
- Deliverable: /home/z/my-project/download/rag_chemistry/ (JSONL + md + loader
  + report + README).
- Key decision: scanned PDF forced OCR route; structure derived from the book's
  own TOC/dividers rather than generic regex, giving chapter-level metadata.
- Known limits: OCR-level chemical-notation artifacts (e.g. subscripted gases),
  diagrams not captured, index/answers tagged for easy filtering.

---
Task ID: 3
Agent: main (Super Z)
Task: User reported v2 corpus still had too many errors and suggested modern
document-AI parsers (Chandra / Docling / MinerU / PaddleOCR). Evaluate and
re-parse the book with the best feasible option.

Work Log:
- Environment check: no GPU, 3 GB RAM, 2 cores, 9.2 GB disk, internet OK.
  -> Chandra (needs 16-24 GB VRAM) and MinerU (needs 16 GB RAM) infeasible.
  -> Chose IBM Docling 2.133 (CPU) with RapidOCR (onnxruntime) as OCR backend.
- Backend shootout on sample pages: RapidOCR 26.8 s/page much cleaner text than
  Tesseract backend (11.3 s/page but garbled boxes/formulas). Quality won.
- Enabled do_formula_enrichment (CodeFormula VLM): display equations decoded to
  LaTeX then converted to Unicode chemistry (42.8 s/page, peak RSS ~2.6-3.4 GB).
- Full-book parse: scripts/docling_full.py, per-page JSON checkpointing,
  5-page fresh processes chained per Bash call to stay under RAM/timeout limits.
  All 383 pages parsed (0 errors, 0 empty; 9 pages are single full-page images).
- Chunker scripts/parse_docling.py: latex_to_chem() (sub/superscripts, arrows,
  fractions, state symbols, math lines), heading/paragraph dedup (sidebar
  double-OCR), heading dedup, (A,)->(Ar) fixes, OCR-brace subscript cleanup,
  structure mapping via book_structure.py, marker-based content typing,
  350-1600 char packing + small-chunk merge + sentence split of oversized blocks.
  Fixed: stale-segment duplicate flush bug (table branch), front-matter
  book_pages=None, LaTeX hallucination drops (>600 chars raw), arrow-word junk.
- Outputs: edexcel_igcse_chemistry_chunks_v3.jsonl (1234 chunks),
  full_book_docling.md, parse_report_v3.json, README rewritten, load_rag.py
  now defaults to v3. Validation (validate_v3.py): unique IDs, 29/29 chapters,
  0 order breaks, 0 LaTeX remnants beyond 5 benign OCR stragglers,
  214 chunks with Unicode subscripts, 184 with reaction arrows, 113 table_data.

Stage Summary:
- Deliverable v3 (Docling-based): download/rag_chemistry/
  edexcel_igcse_chemistry_chunks_v3.jsonl + full_book_docling.md.
- Key decision: Docling+RapidOCR+CodeFormula replaced Tesseract entirely;
  formulas like 2K(s) + 2H2O(l) -> 2KOH(aq) + H2(g) now parse natively
  instead of being repaired post-hoc. v1/v2 kept for diffing.

---
Task ID: 4
Agent: main (Super Z)
Task: Light LLM fidelity polish pass over the remaining ~5-7% noisy v3 chunks
(user-requested follow-up to the Docling v3 rebuild).

Work Log:
- Loaded LLM skill; reinstalled z-ai-web-dev-sdk in scripts/ (npm, from lockfile).
- select_noisy_v3.py: v3-specific noise scoring. Fixed two false-positive sources
  first (markdown table borders and multi-space cell padding counted as junk);
  added ascii_formula pattern for tables (CH4/C2H6 = lost subscripts). Selected
  90 chunks (29 tables, 32 body, 10 chapter_questions, 7 key_points, rest scattered).
- llm_repair_v3.js (z-ai SDK): strict no-paraphrase OCR-repair prompt extended for
  v3 (tables: keep pipe/row counts; formulas may be restored where unambiguous,
  CH8->C3H8; tick marks; CI-CI->Cl-Cl). Sanity guards: length drift 0.6-1.6x,
  refusal patterns, per-line pipe-count match. 2 workers, resumable JSONL.
  Hit persistent 429 quota errors near the end -> longer backoff (20s/attempt),
  single worker, two resume runs -> final: 87 ok, 3 rejected (originals kept).
- merge_llm_v3.py: applied repairs in place (text_original preserved,
  llm_repaired flag, char_count recomputed), regenerated full_book_docling.md
  and parse_report_v3.json. 74 of 87 repairs changed text (13 correct no-ops).
- Post-polish audit: state_paren_garble 8->0, junk table prefixes ->0, latex
  remnants 5->0. Residual classes are benign/false-positive-prone (single-letter
  answer labels, ASCII-digit formulas like H2O). validate_v3.py: ALL CHECKS PASSED.

Stage Summary:
- v3 corpus is final: 1234 chunks, 87 LLM-polished (originals kept), zero
  structural errors. Deliverables unchanged in name:
  download/rag_chemistry/edexcel_igcse_chemistry_chunks_v3.jsonl +
  full_book_docling.md + README (updated) + parse_report_v3.json.

---
Task ID: T-PARSE-AGENT-WORKSPACE-1
Agent: main (Super Z)
Task: Per operator directive (audit = green light): preserve the entire parse
workspace in github.com/SyllabAI/syllabai-resources (workspace unreliable),
and scaffold books/4ph1 for the upcoming Physics book parse.

Work Log:
- Cloned repo (partial, --filter=blob:none; full clone + first push timed out).
- Inspected conventions: AGENT.md rules, RAG_RETRIEVAL_CORPUS_GUIDANCE.md,
  chemistry already at books/pearson-edexcel/international-gcse/chemistry/4ch1/
  (student-book.pdf + docling_pages + ocr_pages only).
- Added chemistry/4ch1/parsed/ (v1/v2/v3 JSONLs, full-book markdowns, parse
  reports, load_rag.py, README) and chemistry/4ch1/pipeline/
  (METHOD_AND_FINDINGS.md, worklog.md, AUDIT_VERDICT_2026-10-18.md,
  scripts/ x29, evidence/ x10: quality audit, LLM repair JSONLs, shootout).
- Canonized books/pearson-edexcel/international-gcse/PARSE_STANDARD.md:
  audit's 8-point standard; learning-objectives newline fix applies to FUTURE
  parses only (chemistry v3 NOT retro-edited - chunk ids already consumed).
- Scaffolded physics/4ph1/{README.md, source/, parsed/, pipeline/} - status
  AWAITING SOURCE BOOK; method plan mirrors 4CH1 stack.
- Commit via temp-index (write-tree needed --missing-ok for partial clone;
  plain git add would have staged phantom deletions from the empty worktree).
- Pushed c9fc6df..816541e main; verified remote via API (PARSE_STANDARD.md,
  4ch1/parsed 7.8 MB incl. chunks_v3.jsonl, 4ph1 scaffold all present).

Stage Summary:
- Workspace now durable in-repo; base c9fc6df, commit 816541e (additive-only,
  57 new files, zero existing paths touched).
- 4PH1 folder ready; next step: operator uploads the physics book PDF to
  source/, then the parse fires against PARSE_STANDARD.md.

---
Task ID: T-PARSE-4PH1-2
Agent: main (Super Z)
Task: Physics 4PH1 parse - source intake + durability + structure probe + full
Docling parse launch.

Work Log:
- Downloaded student-book.pdf from operator tmpfiles link (30,915,167 B, 308 pp,
  sha256 9b0783d9...313a, RICOH MP C4503, image-only scan -> OCR route).
- Pushed to repo: source PDF + README source-of-record table + PARSE_STANDARD.md
  updated with serving-critical directive (chapter/unit question typing drives
  the serving split; both page numberings stay per-chunk). Remote had advanced
  (T-SPECS-CIE-REJOIN-1, disjoint); rebuilt commit on origin/main via temp-index
  hash-object surgery -> 495d736, pushed 2578f6b..495d736.
- Structure probe (tesseract on rendered pages): 8 units / 28 chapters, TOC at
  PDF 5-7; author trio Arnold/Johnson/Woolley; offset book=pdf-10 CONFIRMED
  twice (PDF 144 header prints '134'; ch1 opener PDF 13 = book 3; index 289 ->
  PDF 299 plausible vs 308 pp).
- Env rebuilt after workspace reset (packages wiped): venv python3.12; torch
  CPU + torchvision==0.29.1+cpu (PyPI CUDA tv broke nms), transformers<5
  (v5 broke AutoImageProcessor), docling 2.140, rapidocr-onnxruntime; models
  via download_models() -> data/models (1.4 GB, artifacts_path wired).
- scripts/docling_full_physics.py (chemistry script + OFFSET 10 + physics paths)
  tested on page 13: 36 items, Unicode equations v^2=u^2+(2xa*s), m/s^2 correct,
  opener structure (LEARNING OBJECTIVES/KEY POINT/PHYSICS ONLY) detected,
  25.6 s/page, peak RSS 2.0 GB.
- Launched background grinder scripts/run_parse_physics.sh: 10-page windows,
  resume-safe (skips existing JSONs), logs to data/physics/parse.log.

Stage Summary:
- Book durable in repo at books/.../physics/4ph1/source/ (commit 495d736).
- Parse grinding in background; ETA ~2 h for 308 pages.
- TOC anchors recorded (uncertain: ch8 75, ch16 150|151, ch22 221|222) -
  to be refined post-parse via LEARNING OBJECTIVES detection in parsed text.

---
Task ID: T-PARSE-4PH1-3
Agent: main (Super Z)
Task: Physics 4PH1 v1 parse execution (recap; full record = commit 6242e01
message, which is the of-record for this task).

Work Log:
- Docling 2.33 base (heron layout + RapidOCR + TableFormer, ~9-13 s/page) with
  page-level hybrid: 2.133 formula-decode on PDF 16-17, tesseract fallback on
  PDF 14/20/21, 33 pages formula-OFF retry (CodeFormula crash bug), PDF 307
  pixel-verified blank. 308/308 checkpointed.
- parse_docling_physics.py -> 736 chunks (15-key grammar, phys_v1_* ids),
  offset book_page = pdf_page - 10 (triple-confirmed), 8 units / 28 chapters,
  TOC OCR digit garbles resolved by corpus scan (ch8=75, ch16=150, ch17=158,
  ch22=221). NO answers section (verified corpus-wide).
- Serving-critical compliance: chapter_questions (21) / unit_questions (26)
  typed + page-anchored (47 chunks on marker-verified pages); book_pages +
  pdf_pages per chunk on all 736; non-body typed separately.
- validate_physics.py: ALL CHECKS PASSED. Deliverables in parsed/ (v1).

Stage Summary:
- v1 parse complete, pushed as 6242e01 (deliverables + 308 checkpoints +
  scripts + METHOD_AND_FINDINGS + this worklog).

---
Task ID: T-PARSE-4PH1-4
Agent: main (Super Z)
Task: Chemistry-style LLM fidelity polish round 1 (operator directive
2026-10-19: "run the chemistry-style LLM fidelity polish (RapidOCR drops
some spaces on this scan"). Serving-critical constraint: chapter_questions /
unit_questions anchors and both page numberings must stay per-chunk and
untouched.

Work Log:
- Workspace reset since 4PH1-3 (no physics files locally): re-fetched parsed/
  deliverables + pipeline scripts from repo HEAD (raw.githubusercontent), env
  rebuilt (z-ai-web-dev-sdk npm install in scripts/).
- Noise census: 62% of chunks carry 18+ lowercase glue runs; caps-glue 272,
  camel-glue 181 hits corpus-wide; equations already Unicode (0 caret tokens).
- select_noisy_physics.py: physics-adapted scoring (space_run 18+ chars
  weighted 3x, caps-glue whitelisted against legit book labels like
  INTERPRETATION/RADIOACTIVITY, camel-glue 2x, chemistry residual classes
  kept, table/glossary/index/front-matter damped, question types boosted).
  Selected 300/736 incl. ALL 47 chapter/unit question chunks (force-include).
- llm_repair_physics.js (z-ai SDK): no-paraphrase prompt whose PRIMARY class
  is dropped-space restoration; units/equations must survive verbatim;
  guards: length drift 0.6-1.7x, refusals, Unicode-unit non-decrease, tables
  keep per-line pipe counts, prose wording fidelity via whitespace-normalized
  LCS token ratio >= 0.97 (added after first-pass rejects showed +-1-4 line
  reflows with identical wording); rejected raws saved as evidence. CONC=1,
  429 backoff, quota-stop after 3 consecutive 429s, resumable JSONL.
  Persistent 429 quota walls (chemistry precedent) -> 8 foreground batches.
- merge_llm_physics.py: 232/300 applied (231 changed, 1 no-op), text_original
  preserved, char_count recomputed, full_book_docling.md + parse_report_v1
  regenerated. SERVING-CRITICAL ANCHOR CHECK vs pristine v1 snapshot:
  0 drift across id/unit_no/chapter_no/content_type/pdf_pages/book_pages/
  section/unit_name/chapter_title on all 736 chunks; chunk id set unchanged.
- audit_polish_physics.py: polished-chunk glue runs 1008 -> 3 (residuals are
  legit words: thermoluminescence, telecommunications, one front-matter URL);
  camel glue 121 -> 0; caps glue 127 -> 15; Unicode-unit regressions 0.
- validate_physics.py re-run: ALL CHECKS PASSED (736 unique ids, 28/28
  chapters, 8/8 units, 0 order breaks, 47 question chunks page-anchored,
  0 latex remnants).
- Round 2 pending: 68 chunks (49 unresolved + 19 rejects re-queued under the
  improved guard) blocked by LLM quota; resume protocol documented in
  parsed/README.md. No schema/id changes in round 1; round 2 is pure text.

Stage Summary:
- Corpus state of record: parsed/edexcel_igcse_physics_chunks_v1.jsonl
  (736 chunks, 232 llm_repaired with text_original preserved), validation
  green, serving-critical anchors byte-identical to pristine v1.
- Round 2 is a text-only re-run of the same resumable scripts; split
  derivation unaffected (anchors untouched by design and verified).
