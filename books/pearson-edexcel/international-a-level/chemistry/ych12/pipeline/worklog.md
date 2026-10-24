# YCH12 lane — pipeline worklog

---
Task ID: T-PARSE-YCH12-1
Agent: Z.ai (main, zai-web)
Task: Parse IAL Chemistry SB2 (YCH12, Curtis/Murgatroyd/Scott) per
books/README.md §5 phases 0-10; operator directive "Restore polish R2, and if
not possible right now, then Open a new SB2 (YCH12) lane" (trace
1a16eb539f8701c1) — R2 was quota-walled (429, probe-verified), so the SB2
follow-on lane (pre-declared by T-PARSE-YCH11-1 under the ych2_v1_ law) was
opened; continuation "Continue, why did you stop?" (trace 1a16ec98548ab75d)
carried it to parse completion.

Work Log:
- Fetch-first: origin/main live tree inspected BEFORE anything (the 6dc1f0a2
  lesson) — books/pearson-edexcel/international-a-level/chemistry/ contained
  ONLY ych11; CATALOG row 11 declared "SB2 (IAL Units 4-5) not yet sourced —
  follow-on lane under the ych2_v1_ ID law". Genuine delta; lane scaffolded
  fresh.
- Phase 0: source landed via taleem360 direct link (f=a4c5a983, Googlebot UA,
  162,939,218 B, sha256 44af34a5…748 pinned; page title not walled). Cover
  render verified authors (Curtis/Murgatroyd/Scott, E-001) and the third-party
  "PDF COMPILED BY SAAD" mark (disclosed). 100 MiB limit → 145 dpi ghostscript
  archive derivative (72,675,329 B, sha256 7b1bc6cf…618, L-022 flag),
  320/320 pages, 9.7 s.
- Phase 1: 320 pp, 5/5 sampled pages 0 text chars (Acrobat 19.12 Image
  Conversion) → OCR route mandatory. L-021: TOC's INDEX 299 promise present
  (printed chip "299" on PDF 311) → copy COMPLETE.
- Phase 2: page law book = pdf − 12 confirmed 4 ways (TOC openers; printed
  "299"/"305"/"306"/"308" chips; roman = pdf − 0 with i absent — a DIFFERENT
  roman law from SB1's pdf−1, caught by probe instead of assumed). Book 1
  absent (print blank omitted). Structure probed from the book's own COURSE
  STRUCTURE pages (PDF 4-7) + content-page banner mining.
- Phase 3: book_structure_ych12.py; boundary_coherence() tiles book 2..308
  exactly. KEY layout law: every topic's opener spread carries the
  chapter-LIST chip, not the chapter banner (SB1's 11A-on-divider reading was
  corrected by the T12 divider probe); chapters start at topic page + 2.
- Environment rebuilt after workspace recycle (L-018): CPU torch 2.14.1 +
  torchvision 0.29.1+cpu force-match (the venv had a CUDA-era torchvision
  breaking RTDetrImageProcessor import), transformers pinned 4.52.4,
  docling 2.33.0, rapidocr-onnxruntime 1.4.4. artifacts_path pitfall: a
  set-but-invalid path makes 2.33 fail ALL pages with empty error records —
  removed, models auto-downloaded, 27 error pages re-OCR'd.
- Phase 4: docling_full_ych12.py, 320/329 pages checkpointed in 7 foreground
  windows + front matter + cover (9.2 s/page avg, index tail slower, 0 page
  errors, peak RSS 2.2 GB). Background processes do NOT survive tool-call
  teardown in this environment — foreground-window discipline enforced
  (the r0 pattern, now with the cause identified).
- Rescue pass: 315 empty formula regions on 101 pages exported; 101 pages
  rendered at 150 dpi; 12 batch windows transcribed 133 regions VERBATIM
  (127 fills + 6 adjudicated slivers/duplicates, incl. 2 overlap cases);
  manual_formula_ws_ych12.py applied with 0 bbox mismatches. 182 orphans on
  71 pages REMAIN — partial rescue shipped honestly, resumable (r0 polish
  precedent).
- Phase 5: parse_docling_ych12.py → 1400 chunks (ych2_v1_), 17 content types,
  sizes 41-2367 (0 over hard max); formulas converted 150, 1 sub-4-char
  symbol skipped (benign, documented).
- Phase 6: validate_ych12.py — ALL CHECKS PASSED (unique ids, 19/19 chapters,
  10/10 topics, offset law on every chunk, 84 chapter_questions anchored
  10/10 EP banks, index coverage pdf 311-316, by-design gaps asserted:
  periodic table book 298 + FOUR graph-paper leaves books 305-308). Chunker
  byte-identity double-run verified (sha256 06864a80… twice).
- Phase 7: select_noisy (800 selected; 80 question chunks force-included);
  polish R1 NOT started — the 2026-10-24/25 account-level 429 wall persists
  (probe-verified); staged resumable per PM-3.

Stage Summary:
- Corpus v1 LIVE in parsed/ (1400 chunks, ych2_v1_ ids) + pristine snapshot +
  parse_report_v1.json (page law + formula_rescue + polish staging provenance)
  + full_book_docling.md. Formula rescue parked at 133/315 — resume:
  transcribe remaining orphans → manual_formula_ws_ych12.py → parse →
  validate. LLM polish R1 staged at 800/1400, quota-walled. CATALOG row 12 +
  books/README.md records land in the same commit.

---
Task ID: T-PARSE-YCH12-1-R1
Agent: Z.ai (main, zai-web)
Task: Polish R1 execution under the operator directive "Run YCH12 polish R1
(800 ids already staged) + YCH11 with 730 ids remaining" (trace
1a16f2faf1f993f5).

Work Log:
- The 2026-10-24/25 account-level 429 wall finally lifted in intermittent
  ~5-10 min windows; four windows attempted, two caught openings:
  W1 +40 OK (9 min run), W2 +22 OK, W3 +12 OK, W4-5 walled.
- Cumulative R1: **74/800 OK** (87 records: 74 ok / 6 rejected / 7 error).
- MERGE FROM PRISTINE BASELINE (the YCH11 r1-lesson law): out/ corpus reset
  to .pristine, the FULL repairs file applied once — text_original =
  pre-polish truth for every repaired chunk.
- merge_llm_ych12.py: 1400 chunks, llm_repaired 74, text changed 74,
  anchor check PASS (0 drift). audit_polish_ych12.py: on changed chunks
  space_run 702 → 8, caps_glue 32 → 7; corpus-wide space_run 3675 → 2981
  (726 remaining selected ids will grind it further); 0 Unicode-unit
  regressions vs text_original. validate_ych12.py: ALL CHECKS PASSED.
- Landed: parsed/ corpus + parse_report + full_book_docling.md refreshed;
  evidence/llm_repairs_ych12.jsonl (87 records). Ledgers updated in the
  same commit.

Stage Summary:
- Polish R1 parked at **74/800** (726 ids remain — the wall is intermittent;
  resume recipe unchanged: node llm_repair_ych12.js → cp pristine → merge →
  audit → validate). YCH12 lane otherwise COMPLETE (r0 + R1-partial).
