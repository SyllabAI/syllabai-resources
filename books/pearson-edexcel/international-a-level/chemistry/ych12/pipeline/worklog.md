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

---
Task ID: T-PARSE-YCH12-1-R2
Agent: Z.ai (main, zai-web)
Task: Formula-rescue resume (the lane README's next-step 1) after the operator
session resumed post-sandbox-reset; the 182 unrescued orphans. Quota probe at
session start: 429 wall UP (polish grind parked).

Work Log:
- SANDBOX RESET recovery: data/ workspaces (both lanes) gone, venv stripped to
  the shared base image, docling_full_ych12.py lost from the workspace (repo
  copy intact). Fetched first: origin had advanced massively — T-PARSE-YCH12-1
  (this lane's parse) and YCH11 R3 polish had already landed from parallel
  agents; local main pulled ff-only to cc5f0e8d, ych11+ych12 lanes sparse-checked
  out, both archive PDFs sha256-verified against the README pins.
- Both polish workspaces rebuilt per the lane recipe (pristine reset + FULL
  repairs merge): ych11 1571 chunks / 90 llm_repaired / anchor PASS;
  ych12 1400 / 74 / anchor PASS; rebuilt out/ == landed parsed/ byte-identical
  both lanes (sha256 98d7f891…, bfcb53df…). Validators re-run green on both
  (baseline before any new work).
- RESCUE LABOR COMPLETE: worklist built (182 orphans / 75 pages — note: the
  README's "71 pages" understates; the data says 75); original-of-record
  re-downloaded from the taleem360 provenance URL (162,939,218 B, sha256
  44af34a5…748 re-verified EXACT); 182 full-width 300-dpi crops rendered
  (bbox law probe-verified as PDF-native y-up via the known p16 i13 rescue);
  30 transcription windows produced 182 verbatim records (3 adjudicated
  sliver/duplicates: p80 i8, p187 i38, p297 i7; block-split items resolved
  content-exactly-once: p105 i8/i9, p80 i9/i10, p187 i26/i29, p186 i35);
  merged sidecar = 315/315 orphan keys, 0 missing, 0 dup (306 filled + 9
  adjudicated-empty).
- DOCLING REBUILD: CPU torch 2.14.1+cpu + torchvision 0.29.1+cpu (the CUDA-
  default pip trap hit first — 5.3 GB nvidia wheel set purged, pip cache
  purged, --no-cache-dir + CPU index thereafter), docling 2.33.0 +
  rapidocr-onnxruntime 1.4.4 + transformers 4.52.4 per lane pins. NOTE:
  onnxruntime resolved to 1.31.0 (backend NOT pinned by the lane).
- 320/320 pages re-OCR'd in 10 foreground windows (~10 s/page; index pages
  311-315 up to 310 s each — slower than the r0 run recorded).
- ws apply of the FULL 315-record sidecar onto the rebuilt pages: applied=306,
  adjudicated=9, **mismatch=0** — every orphan bbox matched within 6 pt, i.e.
  the re-OCR's item positions reproduce the original run exactly at all 315
  checkpoints.
- RE-CHUNK DIFF GATE **FIRED** (pre-declared abort condition): out_rescue
  corpus = 1406 chunks vs landed 1400; id sets diverge (459 new-only / 453
  old-only, ~33% renumbered); of 947 shared ids, 647 texts differ (68.3%) and
  541 carry anchor-field drift (section/book_pages) — far beyond the 182
  intended insertions. The re-OCR is NOT byte-faithful (prime suspect: the
  unpinned onnxruntime backend 1.31.0 vs the r0 run's version; layout-model
  drift possible). VERDICT: rescue landing ABORTED; the landed v1 corpus (133
  rescues + 74 polish) stands byte-untouched as the corpus of record.
- LABOR BANKED: evidence/rescue_r2_2026-10-25/ (30 batch files + the merged
  315-record sidecar + worklist + README documenting conventions, the gate
  evidence, and the v2-lane consumption recipe). The transcriptions are
  position-true (bbox-verified against an independent second OCR run) and
  carry over as-is to any fresh parse.

Stage Summary:
- Rescue R2 parked as TRANSCRIBED+BANKED, landing blocked: the lane's "182
  resumable" state is now "182 transcribed & position-verified; consumption
  requires a fresh-parse (v2) lane or a byte-faithful docling env reproduction
  (pin the onnxruntime backend + cache the r0 model artifacts)". Polish R1
  unchanged at 74/800 (quota-walled all session — probes 429 throughout).
- Polish workspaces for BOTH lanes rebuilt and verified; the grind recipe is
  live the moment the wall lifts.

---
Task ID: T-PARSE-YCH12-1-POLISH-CONT-1
Agent: Z.ai (main, zai-web)
Task: LLM polish R1 continuation under the operator directive "Run polish
after the firewall is lifted" (traces 1a1739e8ff0dc1e1 / 1a17520d1e2deda1).
Workspace rebuilt from the repo recipe after the sandbox reset (byte-identity
PASS bfcb53df…, third independent reproduction; validator green).

Work Log:
- Same burst-harvest regime as the YCH11 R4 lane (the wall opened in brief
  ~30-120 s windows; long closures between).
- INCIDENT (disclosed, shared with the YCH11 lane): one protocol invocation
  ran the workspace rebuild after a harvest — repo evidence (87 records)
  re-copied over the workspace file, clobbering the then-accumulated 105 ok
  back to 74. Protocol scripts fixed (no evidence re-copy post-harvest;
  clobber guard on rebuild); grind resumed and recovered past the loss.
- Final protocol: merge from pristine baseline — 1400 chunks, llm_repaired
  79, text changed 79, anchor check PASS (0 drift); audit: 0 Unicode-unit
  regressions; validate: ALL CHECKS PASSED.
- Landed: parsed/ corpus + parse_report + full_book_docling.md refreshed;
  evidence/llm_repairs_ych12.jsonl now 93 records (79 ok / 7 rejected /
  7 error-cum-429). Ledgers updated in the same commit.

Stage Summary:
- Polish R1 parked at **79/800** (done-set 86 -> todo 714). The grind recipe
  is unchanged and the intermittent wall makes every ping turn productive;
  the 182-record rescue sidecar still awaits the fresh-parse (v2) lane.

---
Task ID: T-PARSE-YCH12-1-POLISH-CONT-2
Agent: Z.ai (main, zai-web)
Task: Polish R1 continuation ("continue", trace 1a179d250651d205) after another
sandbox reset — workspace rebuilt from the repo recipe, sdk reinstalled,
baseline validator green pre-grind.

Work Log:
- Grind windows (PROBE_MAX 3-8, CONC 1): W1 walled clean (3x429, 0 harvest);
  W2 opening 20:20-20:24Z +12; W3 opening 20:30-20:34Z +12; W4 slit 20:40Z +3;
  W5 opening 20:50-20:53Z +6. Evidence 93 -> 126 records = 103 ok / 12
  rejected / 11 error-cum-429. llm_repaired 79 -> 103; todo 697.
- INCIDENT (self-caught, disclosed): the first merge ran on an out/ seeded
  from the LANDED corpus instead of the pristine reset — merge re-stamps
  text_original = current text on every ok id, so 103 chunks lost their
  pre-polish truth. Caught by the three-way reconciliation (vs pristine 103
  vs landed 24 + text_original==pristine check, which FAILED). Redone per the
  YCH11 r1-lesson law: pristine reset + FULL evidence applied once -> vs
  pristine 103 / vs landed 24 / text_original = pristine truth True. The
  clobber law fires on BOTH sides (evidence re-copy post-harvest AND
  landed-seed rebuild); the recipe's "reset to .pristine first" wording is
  the load-bearing step, not a style choice.
- Landing: parsed/ corpus + full_book_docling.md + parse_report_v1.json +
  evidence/llm_repairs_ych12.jsonl refreshed. merge anchor check PASS (0
  drift); audit: 0 Unicode-unit regressions, remaining 18+ lowercase runs all
  genuine chemistry words (dinitrophenylhydrazine, disproportionation,
  ethylenediaminetetraacetic class); validate ALL CHECKS PASSED.
- Ledgers updated in the same commit (lane README 3x, CATALOG row 12).

Stage Summary:
- Polish R1 parked at **103/800** (todo 697). The burst-harvest regime
  remains the recipe; openings ran ~10 min apart this session (4 caught of
  5 windows). The 182-record rescue sidecar still awaits the fresh-parse
  (v2) lane.
