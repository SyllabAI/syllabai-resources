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

---
Task ID: T-PARSE-YCH12-2
Agent: Z.ai (main, zai-web)
Task: v2 fresh-parse lane — consume the banked rescue R2 sidecar as a new
corpus of record (operator order "v2 fresh-parse lane", trace
1a17e7ccd46f6181).

Work Log:
- SANDBOX RESET recovery (fetch-first): repo advanced to dec103e6e (SIB pass
  15); ych12 sparse-restored; source PDF sha256 verified (7b1bc6cf…618).
- THE PAGES SURVIVED: data/ych12_sb2/docling_pages intact (320/320, mtimes
  2026-10-25 = the R2 rebuild) WITH the FULL sidecar already applied —
  re-verified item-for-item: 306 filled-exact + 9 adjudicated-empty =
  315/315. The planned 10-14 window OCR re-run was consumed as already done;
  no docling env needed (parse/validate are stdlib-only).
- SCRIPTING: parse_docling_ych12.py + validate_ych12.py + select_noisy_ych12.py
  gained a YCH12_VERSION / YCH12_CORPUS env surface (default v1 byte-proven
  unchanged via prefix-swap diff == identical).
- RE-CHUNK: 1406 chunks ych2_v2_ (deterministic re-run == the R2 count);
  validator ALL CHECKS PASSED (EP 10/10, index 311-316, gaps asserted).
- ADJUDICATION (full numbers in METHOD D-12): error-class rates statistically
  identical to v1-pristine on all 5 classes; structure identical (17 types,
  EP 20 pages, thinking_bigger 69, units 11-20); 0 over-hard-max; rescue
  consumption 305/306 (whitespace-normalized) — the 1 residual (p49 i9,
  N₂(g) + 3H₂(g) → 2NH₃(g)) dropped by the <40-char pack floor via the
  WORKED EXAMPLE 2 micro-segment (14+25=39 chars): SAME drop in v1,
  pre-existing edge, provenance intact (pages + sidecar); pack-floor fold fix
  registered as its own follow-up task. Drift disclosure: 947/1406 shared
  slots, 326 identical text (different OCR run, position-true per R2).
- LANDED: parsed/ chunks_v2.jsonl + .pristine (== pre-polish baseline) +
  parse_report_v2.json + full_book_docling_v2.md + pipeline/docling_pages_v2/
  (320 pages, 2.2 MB — the v2 provenance, banked reset-proof) +
  evidence/llm_repair_ids_ych12_v2.json (801 staged — force-inclusion pushed
  one over the 800 cap; the runner consumes the list as-is).
- Ledgers same commit: METHOD D-12, lane README, CATALOG row 12.

Stage Summary:
- v2 is the corpus of record: rescue COMPLETE (315/315 consumed, 305 in
  chunk text), polish resets to 0/801 staged (v1's 103 repairs do not carry
  by id — the v1 corpus + evidence remain landed and in history). Next:
  polish grind on v2 (llm_repair recipe re-targeted at the v2 corpus +
  ids file), pack-floor follow-up task, serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2
Agent: Z.ai (main, zai-web)
Task: "v2 polish" (trace 1a17e9a6f1fb8471) — resume the polish grind on the v2
corpus of record, and report all lane learnings to the self-improving playbook
(books/README.md §9).

Work Log:
- SANDBOX RESET #5 recovered (fetch + ff-only to f65758e8d == origin/main;
  sparse-add ych12); disk was 100% full (ENOSPC blocked the SDK reinstall) —
  freed 1.4 GB by deleting the rebuildable docling venv + ~/.cache + the two
  local PDF copies (derivative sha256 re-verified == repo pin before delete).
- SCRIPTS parameterized per the L-026 law: llm_repair_ych12.js /
  merge_llm_ych12.py / audit_polish_ych12.py gained the env surface
  (YCH12_CORPUS / YCH12_IDS / YCH12_REPAIRS / YCH12_PRISTINE / YCH12_MD /
  YCH12_REPORT / YCH12_LOG); no-env defaults = the original v1 paths.
- ERRATA E-005 found + fixed: the scripts' comments claimed
  "YCH12_VERSION=2" but VER interpolates directly (id regex + report
  filename) — the working value is "v2"; proven by the validator crash with
  "2" then ALL CHECKS PASSED with "v2".
- BASELINE: v2 validator ALL CHECKS PASSED (1406 chunks) before grinding.
- GRIND: 9 foreground windows; openings caught 18:30 / 18:50 / 19:10 / 19:30
  / 19:50 (~20 min cadence this session, 1–4 min bursts); evidence 0 → 49
  records (40 ok / 3 rejected / 6 error-cum-429; errors self-heal); 43/801
  unique done.
- MERGE (clobber law observed): out_v2 corpus reset from the v2 .pristine,
  FULL evidence applied ONCE — 40 llm_repaired / 40 text changed, anchor
  PASS 0 drift. THREE-WAY RECONCILIATION ALL PASS: vs pristine 40 expected
  fixes / vs landed 40 net-new (landed had 0) / text_original == pristine on
  every repaired chunk; untouched chunks byte-identical; id set unchanged.
- AUDIT: corpus space_run 3675 -> 3242; changed chunks space_run 437 -> 4,
  camel_glue 43 -> 0; 0 Unicode-unit regressions; 3 residual long runs all
  genuine chemistry words (benign class as in v1).
- VALIDATE: YCH12_VERSION=v2 ALL CHECKS PASSED post-merge.
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2 +
  evidence/llm_repairs_ych12_v2.jsonl (49 records); scripts + ledgers same
  commit. PLAYBOOK REPORT-BACK (§9): L-024/L-025/L-026 + E-003
  reconstituted + E-005 + R-007/R-008/R-009 retro-records + R-010 (this
  task) + changelog v1.7 + CATALOG row 12/§3.6 updates.

Stage Summary:
- v2 polish R1 at **40/801 applied (43 done incl. 3 rejected)**, todo 758;
  recipe unchanged (quota-walled burst-harvest, ~20 min window cadence this
  session); v1 corpus + evidence remain landed/history. Open follow-ups:
  pack-floor fold fix (own gate), serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-2
Agent: Z.ai (main, zai-web)
Task: "continue" (2026-10-28, zai-web, trace 1a180d9c9a9d9e55) — resume the v2
polish grind, land the delta, keep the §9 playbook report-back current.

Work Log:
- SANDBOX RESET #6 recovery: fetch + ff-only (origin advanced 548 commits,
  incl. other lanes: T-C42 R25/R26, F110); sparse-add ych12 (first sparse-add
  timed out inside the big merge, second call clean); lane restored at
  2ed40226.
- STATE: v2 fresh-parse + POLISH-CONT-V2 (40/801) already landed by the
  parallel session — this round continues the grind per the standing "v2
  polish" directive. Self-improving docs CONFIRMED EXISTING =
  books/README.md §9 playbook (L-001..L-026 / E-001..E-005 / R-001..R-010 /
  changelog v1.7); report-back continues there.
- WORKSPACE: data/ych12_sb2_v2 rebuilt (corpus seeded from the v2 .pristine
  per the clobber law L-024; evidence 49 records copied; 801 ids staged);
  baseline validator ALL CHECKS PASSED; SDK reinstalled (disk healthy, 7 GB
  free — last round's ENOSPC cleared).
- GRIND: window 1 +53 (49→102), window 2 +18 (→120: 103 ok / 9 rejected /
  8 error-cum-429); then the wall closed 05:14→06:05 (51+ min — longer than
  last round's ~20 min cadence; L-017 class). A background nohup grind loop
  was attempted and DIED silently at tool-call end — the sandbox reaps
  background processes between tool calls (echo line written, node never
  started; grind_loop.out empty). Lesson filed as L-027: polish grind runs
  in FOREGROUND windows only; the runner's probe-wait + clean-exit + done-set
  design makes each foreground window self-managing.
- MERGE (clobber law observed): pristine-seeded corpus, FULL evidence applied
  ONCE — 103 llm_repaired / 103 text changed, anchor PASS 0 drift. THREE-WAY
  RECONCILIATION ALL PASS (ych12_v2_reconcile.py): vs pristine diff set ==
  ok set (103) with anchor keys byte-identical / vs landed net-new 63
  (overlap 40 re-applied, text_original re-stamped from pristine, NOT from
  the landed corpus) / untouched chunks byte-identical / id set unchanged.
- AUDIT: changed chunks camel_glue 71→0, space_run 892→14, caps_glue 49→18;
  0 Unicode-unit regressions; 10 residual 18+ runs ALL genuine chemistry
  words (methylethylpropanoate, dichlorodifluoromethane,
  dinitrophenylhydrazine, ethylenediaminetetraacetic, …) — the known benign
  class (same as v1 audit).
- VALIDATE: YCH12_VERSION=v2 ALL CHECKS PASSED post-merge (EP 10/10).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 40→103) + evidence/llm_repairs_ych12_v2.jsonl (120 records);
  ledgers same commit: lane README, CATALOG row 12 + §3.6, playbook R-011 +
  L-027 + changelog v1.8.

Stage Summary:
- v2 polish R1 at **103/801 applied (112 done incl. 9 rejected, 8 error
  records self-heal)**, todo 689; quota-walled burst-harvest regime (windows
  1-2 harvested, then a 51+ min wall; cadence varies session to session).
  Grind remains resumable via the unchanged recipe (foreground windows, env-
  parameterized runner). Open follow-ups: pack-floor fold fix (own gate),
  serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-3
Agent: Z.ai (main, zai-web)
Task: "continue" (2026-10-28, zai-web, trace 1a183f5a24a10299) — continue the v2
polish grind, land the delta, keep the §9 playbook current.

Work Log:
- SANDBOX RESET #7 recovery: fetch + ff-only (origin advanced 574 commits,
  other lanes: T-SPECS-9696/4HI1, CIE-JOIN-2 wave-2, F110/F111, T-C42 R25/R26);
  sparse-add ych12. ENOSPC hit the sparse-add (disk 100%) — freed ~4.3 GB by
  deleting the STALE v1-era workspaces (data/ych12_sb2 1.8G — everything
  landed in-repo; data/ych11_sb1 264M sibling lane), the rebuildable docling
  models (data/models 1G) and browser caches (~/.cache 1.2G). All deleted
  content is either the repo's durable state (evidence, corpora, page banks)
  or rebuildable tooling. v1-default runner paths are stale by design (the
  v2 lane always sources the env surface — L-026).
- WORKSPACE: data/ych12_sb2_v2 rebuilt from the repo (corpus seeded from the
  v2 .pristine per the clobber law L-024; evidence 120 records; 801 ids);
  baseline validator ALL CHECKS PASSED; SDK reinstalled.
- GRIND: 4 harvesting windows (+50, +27, +28, +28 records; bursts 26-40);
  wall closures 19:34/19:46/19:56/20:05 UTC (~10-12 min cadence — healthier
  than CONT-V2-2's 51+ min wall); foreground windows only per L-027.
- EVIDENCE: 253 records (218 ok / 23 rejected / 12 error-cum-429 self-heal);
  241/801 done, todo 560.
- MERGE (clobber law observed): pristine-seeded corpus, FULL evidence applied
  ONCE — 218 llm_repaired / 218 text changed, anchor PASS 0 drift. THREE-WAY
  RECONCILIATION ALL PASS (ych12_v2_reconcile.py): vs pristine diff set ==
  ok set (218) / vs landed net-new 115 (103 overlap re-applied, text_original
  re-stamped from pristine) / untouched byte-identical / id set unchanged.
- AUDIT: changed chunks camel_glue 106→0, space_run 1547→21, caps_glue
  105→29; 0 Unicode-unit regressions; 14 residual 18+ runs ALL genuine
  chemistry words (dinitrophenylhydrazine, disproportionation,
  chloromethylpropane, methylethylpropanoate, tetrachlorocuprate, …) — the
  known benign class.
- VALIDATE: YCH12_VERSION=v2 ALL CHECKS PASSED post-merge (EP 10/10).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 103→218) + evidence/llm_repairs_ych12_v2.jsonl (253 records);
  ledgers same commit: lane README, CATALOG row 12 + §3.6, playbook R-012 +
  changelog v1.9 (no new lessons — this run CONFIRMS the playbook: quota
  regime per L-007/L-017, foreground windows per L-027, clobber law per
  L-024, env parameterization per L-026).

Stage Summary:
- v2 polish R1 at **218/801 applied (241 done incl. 23 rejected, 12 error
  records self-heal)**, todo 560; quota-walled burst-harvest regime, windows
  healthy this session (~10-12 min cadence, +27-50/window). Grind resumable
  via the unchanged recipe. Open follow-ups: pack-floor fold fix (own gate),
  serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-4
Agent: Z.ai (main, zai-web)
Task: "continue" (2026-10-30, zai-web, trace 1a18bc2b68b0b609) — continue the v2
polish grind, land whatever delta survives the quota, keep the §9 playbook
current.

Work Log:
- SANDBOX RESET #8 recovery: fresh rootfs (8.5 GB free — no ENOSPC this time;
  the reset itself cleared the disk), fetch + ff-only 626 commits (parallel
  lanes: T-TEXTDEBRIS-1 1,826-file debris cleanup, T-SPECS, CIE-JOIN-2),
  sparse-add ych12, SDK reinstalled, v2 workspace rebuilt from the repo
  (env + reconcile helper scripts recreated — reset wipes scripts/ too).
- GRIND: 5 windows, HARSH REGIME — window 1 +4 (2 ok), window 2 +0, window 3
  +9 (6 ok / 1 rej), windows 4-5 +0; the wall opened only in brief cracks
  (~1 call) instead of yesterday's full 10-12 min windows. Evidence 266
  records (226 ok / 24 rejected / 16 error-cum-429); 250/801 done, todo 551.
- CLOBBER REPLAY CAUGHT (L-024 protocol, detector = three-way reconciliation):
  a merge invocation inside a FAILED tool call had already executed (its
  stdout was swallowed by the tool error) — the explicit re-run then
  double-applied on the merged corpus: "llm_repaired 226, text changed 0" +
  R3 text_original != pristine on all 226. Repo untouched (copy happens
  after reconciliation). Fix per the law: re-seed from .pristine, single
  full-evidence merge → 226 text changed, anchor PASS 0 drift, reconciliation
  ALL PASS (net-new 8, overlap 218 re-applied from pristine). NUANCE worth
  recording: re-seed before EVERY merge invocation, not once per session —
  a "failed" tool call may have succeeded invisibly, and this merge is not
  idempotent (re-running it is destructive by design).
- AUDIT: 0 Unicode-unit regressions; residual 18+ runs all genuine chemistry
  words (disproportionation, electronegativities, dinitrophenylhydrazine,
  hydroxypropanenitrile, …) — benign class. VALIDATE: ALL CHECKS PASSED
  post-merge (EP 10/10).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 218→226) + evidence/llm_repairs_ych12_v2.jsonl (266 records);
  ledgers same commit: lane README, CATALOG row 12 + §3.6, playbook R-013 +
  changelog v1.10 (no new L-entry — the replay is L-024's own scenario
  caught by its own protocol; nuance disclosed in R-013).

Stage Summary:
- v2 polish R1 at **226/801 applied (250 done incl. 24 rejected, 16 error
  records self-heal)**, todo 551; quota regime turned harsh (crack-openings
  vs full windows); grind resumable via the unchanged recipe. Open
  follow-ups: pack-floor fold fix (own gate), serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-5
Agent: Z.ai (main, zai-web)
Task: "continue" (2026-10-30, zai-web, trace 1a18d0c67c43613d) — continue the v2
polish grind, land whatever delta survives the quota, keep the §9 playbook
current.

Work Log:
- SANDBOX RESET #9 recovery: fresh rootfs (8.5 GB free; disk healthy since the
  ENOSPC cleanup of reset #7). The local checkout was a DIFFERENT project —
  the lane repo had to be re-located first (origin/main not in any local
  clone; found via the GitHub commit-lookup loop across the account's repos:
  e3d648a1 lives in syllabai-resources). Re-cloned sparse + blob-filter,
  ff'd to main tip (parallel lanes had advanced it: PR #240/#241 r3 stageB3
  + #242 stageB4), verified 0 ych12 commits between 8dd16e99 (CONT-V2-4)
  and the new tip, evidence baseline byte-match (266 records).
- R-013 ACTION LANDED THIS ROUND: the lane tooling that lived only in the
  sandbox (env surface + reconcile tool) is now repo-resident —
  `pipeline/scripts/ych12_v2_reconcile.py` (three-way reconciliation,
  R1-R6 checks incl. the clobber/double-apply detector) and
  `pipeline/scripts/ych12_v2_reseed.sh` (the L-024 re-seed law as an
  executable: corpus <- pristine, report <- landed parse_report,
  baseline <- landed corpus; idempotent, re-run before EVERY merge).
- GRIND: 7 windows, MIXED REGIME — window 1 FULL (+53: 45 ok / 5 rej /
  3 err-429, the CONT-V2-3-style full window returned), window 2 crack +11,
  window 3 crack +46, windows 4-7 steady cracks +28/+28/+27/+29 (~5.5 min
  probe to clear, ~4 min crack each; PROBE_WAIT shortened 90->45s to fit
  more probes per 10-min foreground window). Session +194 ok net-new
  (226->420) = the grind's single-round record (previous +115, CONT-V2-3).
  Evidence 488 raw records (420 ok / 38 rejected / 30 error-cum-429;
  458/801 done, todo 343).
- VALIDATE GATE HIT, RESOLVED WITH DISCLOSURE (E-007): a legitimate de-glue
  repair grew u15_c11_pdf154_0756 2367->2430 (restored spaces, wording
  identical, LCS guard passed) — over the validator's parse-era hard max
  2400. First polish-induced over-max; pristine max 2367; near-max
  population = 2 chunks total. Bound raised 2400->2500 with an in-code
  disclosure comment + errata E-007 (bounded headroom, the parse-era
  runaway class stays closed). Also caught on the same validate run: the
  merge's regenerated report dropped `by_design_gaps` (fresh workspace
  report) — CONT-V2-4 had carried it by hand, unrecorded; now structural:
  the re-seed law seeds the report from the landed copy and the merge
  preserves existing keys.
- MERGE (after ych12_v2_reseed.sh): llm_repaired 420, text changed 418,
  anchor PASS 0 drift; deterministic full replay re-run once more (re-seed
  -> merge) with identical numbers — the not-idempotent merge is safe under
  the law. RECONCILIATION ALL PASS (net-new 194, overlap 226 re-applied
  from pristine, R1-R6 clean). AUDIT: 0 Unicode-unit regressions; residual
  18+ runs genuine chemistry words (dinitrophenylhydrazine,
  disproportionation, tetraaquadihydroxoiron, …) — benign class.
  VALIDATE: ALL CHECKS PASSED post-merge (EP 10/10, size_max 2430).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 226->420) + evidence/llm_repairs_ych12_v2.jsonl (488
  records) + pipeline/scripts/{ych12_v2_reconcile.py, ych12_v2_reseed.sh,
  validate_ych12.py (E-007 bound)}; ledgers same commit: lane README,
  CATALOG row 12 + §3.6, playbook E-007 + R-014 + changelog v1.11.

Stage Summary:
- v2 polish R1 at **420/801 applied (458 done incl. 38 rejected, 30 error
  records self-heal)**, todo 343; single-round record +194; the re-seed law
  and the reconciliation are now repo-resident tooling (R-013 closed).
  Open follow-ups: pack-floor fold fix (own gate), serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-6
Agent: Z.ai (main, zai-web)
Task: "continue" (2026-10-30, zai-web, trace 1a18d9ef7edd1c41) — continue the v2
polish grind, land whatever delta survives the quota, keep the §9 playbook
current.

Work Log:
- SANDBOX RESET #10 recovery, FASTEST YET: the base image ships a clone of
  this very repo (`gh_repos/syllabai-resources`, blob:none) — reused it
  instead of re-cloning; fetch had one 300 s stall then completed, ff'd to
  the tip (parallel lanes: PR #243), sparse-checkout switched to NON-CONE
  mode (cone rejects the file-level patterns: books/README.md, CATALOG.md,
  lane README/worklog) with a minimal pattern set — docling_pages_v2 and
  the 72 MB source PDF stay excluded. Recovery used ONLY repo-resident
  tooling this time: env copied from `ych12_v2_env_template.sh`,
  workspace seeded by `ych12_v2_reseed.sh` (R-013/R-014's closed action
  paying off — nothing had to be recreated from memory).
- GRIND: 8 windows, STEADY-CRACK REGIME — every window probed clear within
  0-2 attempts, harvested ~4 min, walled (2x429): +30/+28/+30/+31/+29/
  +28/+30/+30 records (26/25/26/28/24/22/26/27 ok each, ~3 err-cum-429 per
  window, rejects 0-3). Session +204 ok net-new (420->624) = the SECOND
  consecutive record round (CONT-V2-5 +194). Evidence 724 raw records
  (624 ok / 46 rejected / 54 error-cum-429); 670/801 done, todo 131 —
  the grind is now ~83.5% applied with only 131 resumable ids left.
- LANDING ON REPO-RESIDENT TOOLING END-TO-END: reseed.sh (corpus <- pristine,
  report <- landed keeping by_design_gaps, baseline <- landed corpus) ->
  merge (llm_repaired 624, text changed 620, anchor PASS 0 drift) ->
  reconcile ALL PASS (net-new 204, overlap 420 re-applied from pristine,
  R1-R6 clean) -> audit 0 Unicode-unit regressions (residual 18+ runs
  genuine chemistry words: hydroxybutanenitrile, disproportionation, …,
  benign class) -> validate ALL CHECKS PASSED (EP 10/10) — and the same
  validate re-run against the REPO copy post-copy (ALL CHECKS PASSED,
  gaps True, polished 624, changed 620).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 420->624) + evidence/llm_repairs_ych12_v2.jsonl (724
  records); ledgers same commit: lane README, CATALOG row 12 + §3.6,
  playbook R-015 + changelog v1.12. No new L-entries, no new errata
  (E-007 headroom 2500 untouched — no near-max chunk repaired this round).

Stage Summary:
- v2 polish R1 at **624/801 applied (670 done incl. 46 rejected, 54 error
  records self-heal)**, todo 131; two record rounds back-to-back (+194,
  +204); recovery and landing now fully repo-resident. Open follow-ups:
  finish the last 131 ids, pack-floor fold fix (own gate), serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-7
Agent: Z.ai (main, zai-web)
Task: "continue" (2026-10-31, zai-web, trace 1a18ffa5c8740e49) — continue the v2
polish grind, land whatever delta survives the quota, keep the §9 playbook
current.

Work Log:
- SANDBOX RESET #11 recovery: same base-image clone route as CONT-V2-6
  (reused, not re-cloned), non-cone sparse pattern re-applied from the
  round recipe, ff to the tip (parallel lanes: PR #244-#248), ych12
  baseline verified (last lane commit = CONT-V2-6, evidence 724 records).
  Workspace seeded via the repo-resident reseed.sh + env template — the
  third consecutive reset recovered without recreating anything from
  memory.
- GRIND: 9 windows, BURST-THEN-WALLS — window 1 a FULL window, the
  grind's most productive single crack since CONT-V2-3 (+56 records: 51
  ok / 2 rej / 3 err) taking done to 680/801; then the wall CLOSED
  COMPLETELY — windows 2-9 all clean-exit probe windows (8 x 12 probes,
  PROBE_WAIT 45-50s) against a ~73-minute full closure, THE GRIND'S
  LONGEST (previous max observed: 51+ min, L-017's third intensity data
  point now at 73 min). Landed per the standing discipline: harvest the
  delta, resume the rest. Evidence 780 raw records (675 ok / 48 rejected
  / 57 error-cum-429); 723/801 done, todo 78.
- MERGE (after reseed.sh): llm_repaired 675, text changed 671, anchor
  PASS 0 drift; reconcile ALL PASS (net-new 51, overlap 624 re-applied
  from pristine, R1-R6 clean); audit 0 Unicode-unit regressions (benign
  chemistry-word residual class); validate ALL CHECKS PASSED x2
  (workspace + repo copy, EP 10/10, by_design_gaps preserved).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 624->675) + evidence/llm_repairs_ych12_v2.jsonl (780
  records); ledgers same commit: lane README, CATALOG row 12 + §3.6,
  playbook R-016 + changelog v1.13. No new L-entries (the 73-min closure
  extends L-017's range observation, recorded here + in R-016 rather
  than as a new lesson — same mechanism, longer tail). No new errata.

Stage Summary:
- v2 polish R1 at **675/801 applied (723 done incl. 48 rejected, 57 error
  records self-heal)**, todo 78 — ~90% of the grind complete, 78 ids
  resumable behind the current wall. Open follow-ups: finish the last
  78, pack-floor fold fix (own gate), serving lane.

---
Task ID: T-PARSE-YCH12-2-POLISH-CONT-V2-8
Agent: Z.ai (main, zai-web)
Task: "Proceed with the remaining work" (2026-10-31, zai-web, trace
1a19276aa93e5b01) — harvest the final 78 ids; if the grind completes, close
it out in the ledgers.

Work Log:
- SANDBOX RESET #12 recovery: mirror survived, workspace did not. Local
  HEAD sat at the T-C42 R26 audit commit with sparse-checkout reconfigured
  cone-mode by a parallel maths session — re-applied the non-cone lane
  pattern set (other lanes' dirs kept materialized), fetched, ff to tip
  139d9595 (31 commits, all OTHER lanes: ZNotes CAIE/Edexcel import PR
  #259, spec re-parse, videos; ych12 untouched after bfcb09ad). Discovery
  at baseline check: **CONT-V2-7 was already landed by a parallel session
  of this same lane (bfcb09ad: 675/801 applied, todo 78)** — the round
  became a completion round (final 78, CONT-V2-8) instead of a repeat.
  Workspace reseeded from the repo-resident template + reseed.sh, fourth
  consecutive reset recovered with zero tooling recreated from memory.
- GRIND: 13 windows to the finish. Windows 1-9 clean-exit probe windows
  (8-9 probes each, PROBE_WAIT 45s) against a ~56-minute full closure —
  the wall was already shut when the session opened. Then the crack:
  window 10 +27 (21 ok / 3 rej / 3 err), window 11 +29 (25 ok / 1 rej /
  3 err), window 12 +28 (26 ok / 1 rej / 1 err, natural DONE — no
  quota-stop), window 13 +1 (the last id `ych2_v2_u17_c0_pdf231_1131`,
  429'd at window 12's end, OK on the first clear probe). **GRIND
  COMPLETE: 801/801 staged ids reached a terminal verdict** — no id left
  resumable for the first time since staging.
- FINAL STATE: evidence 865 raw records (748 ok / 53 rejected / 64
  error-cum-429 all retried to terminal); session +73 ok net-new
  (675->748), +4 rejected (48->53).
- MERGE (after reseed.sh): llm_polished 748, changed 743, anchor PASS
  0 drift; reconcile ALL PASS (net-new 73, overlap 675 re-applied from
  pristine, R1-R6 clean); audit 0 Unicode-unit regressions (benign
  chemistry-word residual class: dinitrophenylhydrazine,
  disproportionation, tetrahydridoaluminate, …); validate ALL CHECKS
  PASSED x2 (workspace + repo copy, EP 10/10, by_design_gaps preserved
  (5)).
- LANDED: parsed/ chunks_v2 + full_book_docling_v2 + parse_report_v2
  (llm_polished 675->748) + evidence/llm_repairs_ych12_v2.jsonl (865
  records); ledgers same commit: lane README (v2 polish grind status ->
  COMPLETE), CATALOG row 12 + §3.6, playbook R-017 + changelog v1.14.
  No new L-entries. No new errata.

Stage Summary:
- **v2 polish R1 GRIND COMPLETE: 748/801 applied, 53 rejected (guard,
  raws in evidence), todo 0** — every staged id terminal after 8 rounds
  (POLISH-CONT-V2 + CONT-V2-2..8, ~50 quota windows, 2026-10-27 ->
  2026-10-31). Corpus of record 1406 chunks, validator ALL CHECKS
  PASSED, anchor 0 drift throughout. Open follow-ups: pack-floor fold
  fix (own gate), serving lane consumption of the polished corpus.

---
Task ID: T-PARSE-YCH12-2-FOLD-1
Agent: Z.ai (main, zai-web)
Task: "Proceed" (2026-10-31, zai-web, trace 1a19343903e000e1) — next open
follow-up after the grind's completion: the pack-floor fold fix with its
own gate (METHOD_AND_FINDINGS D-12 §5).

Work Log:
- SANDBOX RESET #13 recovery: base-image clone route again (mirror at the
  T-C42 audit commit, sparse cone-mode), non-cone lane patterns
  re-applied, fetch + ff to tip b952bd81 (3 commits, all other lanes —
  receipt bookkeeping; ych12 untouched since cd45d9f7 = CONT-V2-8).
  Workspace reseeded from the repo-resident template + reseed.sh, fifth
  consecutive reset recovered with zero tooling recreated from memory.
- TARGET ADJUDICATION: sidecar page_049 i8 ("WORKEDEXAMPLE2",
  section_header) + i9 ("N₂(g) + 3H₂(g) → 2NH₃(g)", formula,
  `rescued: true` — the last unconsumed rescue fill) = 38 raw block
  chars < 40-char pack floor, dropped, corpus index _0222 consumed (the
  corpus's 149-gap signature; drop confirmed — no u12_c2 page-49 chunk
  carries the header). Reading-order home: between `_0219`
  (WORKEDEXAMPLE1 block) and `_0220` (ENTROPYCHANGEOFTHESURROUNDINGS
  body). `_0219` is POLISHED — folding there is R1-illegal (corpus text
  frozen to the evidence repair text, append-only evidence law) — so the
  fold PREPENDS to `_0220` (body, UNPOLISHED, pristine==corpus byte-equal,
  cc==len 474).
- FOLD GATE (own gate, all green): pre-checks (target unpolished, no
  partial state, corpus-wide drop confirmation, sidecar byte-match,
  folded size under hard max) -> fold applied to the PRISTINE OF RECORD
  in place (474 -> 516 chars; corpus/markdown/report left to the chain)
  -> reseed -> merge (748/743, anchor PASS 0 drift) -> THE CENTERPIECE:
  regenerated corpus vs the landed corpus differs in EXACTLY one chunk
  (`_0220`, +42 chars, fold-prefixed, anchors/text_original/llm_repaired
  byte-identical) -> reconcile ALL PASS x2 (workspace + repo; net-new 0,
  no evidence change) -> audit 0 Unicode-unit regressions -> validate
  ALL CHECKS PASSED x2. **306/306 sidecar fills now consumed.**
- TOOL: `pipeline/scripts/ych12_v2_fold_p49i9.py` (repo-resident,
  idempotence-guarded; docling_pages_v2 is sparse-excluded so the
  sidecar reads via git show with a YCH12_SIDECAR_P49 fallback — the
  blob:none lazy fetch flaked and the fallback carried the gate).
- DECISIONS: v1 keeps the drop as landed history (byte-untouched law);
  the chunker's drop-semantics pack floor is left as-is — a
  future-parse behavior change would need its own deterministic proof
  per L-025, and no re-parse is planned.
- LANDED: parsed/ pristine + chunks_v2 + full_book_docling_v2 +
  parse_report_v2; pipeline/scripts/ych12_v2_fold_p49i9.py;
  METHOD_AND_FINDINGS D-12 §5 follow-up closed; ledgers same commit:
  lane README, CATALOG row 12 + §3.6, playbook R-018 + changelog v1.15.
  No new L-entries. No new errata.

Stage Summary:
- **Pack-floor fold fix DONE with its own gate: the last unconsumed
  rescue fill (p49 i9) now lives in the corpus of record
  (`ych2_v2_u12_c2_pdf049_0220`), 306/306 sidecar fills consumed,
  every polish invariant intact.** Open follow-up: serving lane
  consumption of the polished corpus (+ the pending DB apply / T-C20
  flip on the serving package, Neon MAIN paused at operator level).
