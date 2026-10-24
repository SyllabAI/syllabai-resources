# YCH11 lane — pipeline worklog

---
Task ID: T-PARSE-YCH11-1
Agent: Z.ai (main, zai-web)
Task: Parse IAL Chemistry SB1 (YCH11, Curtis/Murgatroyd/Scott) per
books/README.md §5 phases 0-10; operator directive "Parse YCH11 IAL chem
according to the instructions" (trace 1a16ac2fe536fbe5).

Work Log:
- Fetch-first: origin/main re-fetched and the live books/ tree inspected
  BEFORE anything else (the 6dc1f0a2 revert lesson) — no YCH11 lane, no
  YCH11 source existed on the remote; CATALOG rows 1-10 have no IAL
  chemistry book. Lane scaffolded fresh.
- Phase 0: source landed via taleem360 direct link (f=062fc8b2, Googlebot
  UA, 148,791,436 B, sha256 3d534889…72eb pinned); NOT walled for this
  title. Cover render verified authors (Curtis/Murgatroyd/Scott, E-001
  discipline). Environment rebuilt (L-018 order: CPU torch, docling 2.33.0,
  rapidocr-onnxruntime 1.4.4); artifacts 506 MB (layout+TableFormer; no
  CodeFormula per D-7).
- Phase 1: 329 pp, 20/20 sampled pages 0 text chars, Skia/PDF m75, fake
  OPS outline, uniform single pages → OCR route mandatory. L-021 check:
  TOC's INDEX 309 promise present at book 309 (PDF 322) → copy COMPLETE.
- Phase 2: page law book = pdf − 13 confirmed 3 ways (roman = pdf−1; TOC
  openers; printed digits "27"/"309"/"311"). Book 1 absent (print blank
  omitted). Structure probed from renders + OCR: 2 units / 10 topics /
  35 chapters; 10 TB + 10 EP banks; back matter 290-316; no answers
  section (Lab Book/Pearson own them).
- Phase 3: book_structure_ych11.py; boundary_coherence() tiles 2..316
  exactly (ran clean pre-chunk and in every census).
- Phase 4: docling_full_ych11.py, 329/329 pages checkpointed in 14
  foreground windows (~10 s/page avg; index tail 70-305 s/page; peak RSS
  2.55 GB; 0 page errors). Formula enrichment OFF (D-7 deviation, documented).
- Rescue pass: 291 empty formula regions on 100 pages exported; 100 pages
  rendered at 150 dpi; 295-record sidecar transcribed verbatim from renders
  (287 fills + 4 mangled-formula replacements + 8 adjudicated slivers);
  manual_formula_ws_ych11.py applied with 0 mismatches. Post-rescue: 309
  nonempty / 8 adjudicated-empty.
- Phase 5: parse_docling_ych11.py → 1571 chunks (ych1_v1_), 16 content
  types, sizes 40-2315 (0 over hard max), formulas converted 309/0 failed.
- Phase 6: validate_ych11.py — ALL CHECKS PASSED (one unit bug in the EP
  anchor check fixed in the validator; two image-only end-matter pages
  registered as by-design gaps per the honesty rules, not silently
  dropped). Byte-identity double-run of the chunker verified
  (sha256 0bdb1c5e… both runs).
- Source derivative: ghostscript 145 dpi archive copy (73,538,565 B,
  sha256 b17ea91f…7927; -dPassThroughJPEGImages=false per L-022); 329/329
  pages, geometry parity, contents-page pixel MAE 1.17/255.
- Phase 7: select_noisy (800 selected; 59 question chunks force-included);
  llm_repair_ych11.js staged; two quota windows harvested 48 OK / 4
  rejected / 2 errors; merge applied 48/800 (text_original preserved,
  anchor diff 0 drift); audit clean (glue 459→5 on changed chunks — the 5
  are real long chemistry words; 0 Unicode regressions); re-validated ALL
  CHECKS PASSED. Shipped partial per PM-3 (R-002/R-004/R-005 disposition).

Stage Summary:
- Corpus v1 LIVE in parsed/ (1571 chunks, ych1_v1_ ids) + pristine snapshot
  + parse_report_v1.json (by_design_gaps + formula_rescue provenance) +
  full_book_docling.md. Polish R1 parked at 48/800 — resume: `node
  llm_repair_ych11.js` → `merge_llm_ych11.py` → `audit_polish_ych11.py` →
  `validate_ych11.py`. CATALOG row 11 + books/README.md records land in the
  same commit. SB2 (YCH12 book) is the follow-on lane (ych2_v1_ law).
