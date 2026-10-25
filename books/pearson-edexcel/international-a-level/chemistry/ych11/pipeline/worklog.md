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

---
Task ID: T-PARSE-YCH11-1-R2
Agent: Z.ai (main, zai-web)
Task: Polish R2 restoration window(s) under the operator directive "Restore
polish R2, and if not possible right now, then Open a new SB2 (YCH12) lane"
(trace 1a16eb539f8701c1).

Work Log:
- Quota probe: 429 wall confirmed at session start; one foreground window
  (PROBE_MAX=2) attempted late in the session — the wall briefly lifted:
  22 OK / 2 rejected / 3 error-cum-429, then the script's 2-consecutive-429
  stop fired cleanly (resumable design working as intended).
- Cumulative polish ledger: R1 48 + R2 22 = **70/800 OK** (81 records total:
  70 ok / 6 rejected / 5 error-cum-429).
- MERGE FROM PRISTINE BASELINE (the r1-lesson fix): re-running the R1-style
  merge over an already-polished corpus would clobber text_original with
  repaired text for previously-repaired chunks; instead the out/ corpus was
  reset to .pristine and the FULL repairs file (all 70 ok) applied once —
  text_original = pre-polish truth for every repaired chunk, idempotent.
- merge_llm_ych11.py: 1571 chunks, llm_repaired 70, text changed 70,
  anchor check PASS (0 drift). audit_polish_ych11.py: corpus-wide space_run
  635 → 7 (the 7 residuals are genuine long chemistry words:
  disproportionation, tetrachloromethane, trifluoromethanesulfonate, ...),
  0 Unicode-unit regressions vs text_original. validate_ych11.py: ALL CHECKS
  PASSED (after rebuilding out/parse_report_v1.json from the lane report —
  the merge regenerates the report and had dropped by_design_gaps; the lane
  report remains the base of record).
- Landed: parsed/ corpus + parse_report + full_book_docling.md refreshed;
  evidence/llm_repairs_ych11.jsonl now 81 records. Ledgers updated in the
  same commit.

Stage Summary:
- Polish parked at **70/800** (730 selected ids remain, quota-walled,
  resumable: node llm_repair_ych11.js → cp pristine → merge → audit →
  validate). YCH11 lane otherwise COMPLETE (r0 + r1 + R2).

---
Task ID: T-PARSE-YCH11-1-R3
Agent: Z.ai (main, zai-web)
Task: Polish continuation under the operator directive "Run YCH12 polish R1
(800 ids already staged) + YCH11 with 730 ids remaining" (trace
1a16f2faf1f993f5).

Work Log:
- Two windows attempted (W2 +20 OK, W1/W3 walled); the intermittent 429 wall
  pattern (lift ~5-10 min, then down) held all session.
- Cumulative polish: R1 48 + R2 22 + R3 20 = **90/800 OK** (108 records:
  90 ok / 10 rejected / 8 error-cum-429).
- Merge from pristine baseline again (idempotent law): anchor check PASS
  (0 drift); audit: on changed chunks space_run 765 → 9 (real long chemistry
  words), corpus-wide space_run 3446 → 2690; 0 Unicode-unit regressions.
  validate_ych11.py: ALL CHECKS PASSED.
- Landed: parsed/ corpus + parse_report + full_book_docling.md refreshed;
  evidence/llm_repairs_ych11.jsonl (108 records). Ledgers updated in the
  same commit.

Stage Summary:
- Polish parked at **90/800** (710 ids remain — todo is 710 because 10
  rejected ids are permanently skipped by the resume done-set; the "730"
  figure counted rejected as pending). Recipe unchanged.

---
Task ID: T-PARSE-YCH11-1-R4
Agent: Z.ai (main, zai-web)
Task: Polish continuation under the operator directive "Run polish after the
firewall is lifted" (traces 1a1739e8ff0dc1e1 / 1a17520d1e2deda1). Sandbox
reset between sessions: workspaces rebuilt from the repo recipe first.

Work Log:
- Post-reset bootstrap: fetched (origin had advanced to 11205d6c), pulled
  ff-only, sparse-checkout extended with books/; both workspaces rebuilt
  (pristine + FULL repairs merge) — rebuilt out/ byte-identical to landed
  parsed/ (sha256 98d7f891…, third independent reproduction); validators green.
- Wall pattern this session: LONG closures with brief (~30-120 s) openings.
  Burst-harvest driver (probe 1x -> grind -> stop on 2x429 -> gap -> repeat):
  ~10 windows, 40+ bursts. First opening harvested 4 OK in ~40 s.
- INCIDENT (disclosed): the first protocol invocation ran the workspace
  REBUILD (which re-copies repo evidence) after the harvest — clobbering the
  then-accumulated records (134 ok) back to 90. ~34 ok records' repaired text
  lost (ids recoverable from the log; grind re-attempts them naturally).
  Fixed: post_grind_protocol.sh no longer re-copies evidence (backup +
  reset + merge from the WORKSPACE records); rebuild gained a clobber guard.
- Recovered grind continued after the fix; final protocol: merge from pristine
  baseline — 1571 chunks, llm_repaired 130, text changed 129, anchor check
  PASS (0 drift); audit: 0 Unicode-unit regressions; validate: ALL CHECKS
  PASSED.
- Landed: parsed/ corpus + parse_report + full_book_docling.md refreshed;
  evidence/llm_repairs_ych11.jsonl now 152 records (130 ok / 14 rejected /
  8 error-cum-429). Ledgers updated in the same commit (incl. the stale
  "SB2 = NOT SOURCED" header drift repair — SB2 landed in the sibling lane
  2026-10-25).

Stage Summary:
- Polish parked at **130/800** (done-set 144 -> todo 656 — rejected ids are
  permanently skipped by the resume done-set; 8 error ids re-attempt on the
  next run). Recipe unchanged: node llm_repair_ych11.js (burst-harvest while
  the wall is bursty) -> post-grind protocol -> land.
