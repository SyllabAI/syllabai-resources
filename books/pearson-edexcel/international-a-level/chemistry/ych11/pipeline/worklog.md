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
---
Task ID: T-PARSE-YCH11-1-R5
Agent: Z.ai (main, zai-web)
Task: "resuming YCH11 polish with the same parameterized tooling" (2026-11-01,
zai-web, trace 1a195fe3279586d9) — resume the R4-parked 130/800 grind on the
YCH12-v2-style env-parameterized toolchain.

Work Log:
- Sandbox reset #14 recovery: mirror rolled back to the base image (refs at
  a8803c5, objects from the prior session's fetch gone), sparse flipped back
  to cone mode by a parallel session — non-cone lane patterns re-applied
  (now covering BOTH chemistry lanes), fetch + ff to tip 5a9d5f46. Opening
  guard: 3cda3af3..5a9d5f46 checked for ych11 activity — none (GradeBoundaries
  / guided-lessons lanes only); no parallel landing to re-point at.
- TOOLING PARAMETERIZED (the round's infrastructure deliverable): the ych11
  lane scripts predate the YCH12 v2 env convention — `llm_repair_ych11.js`
  (4 paths), `merge_llm_ych11.py` (5 paths) and `audit_polish_ych11.py`
  (3 paths) now read YCH11_* env overrides with defaults = the previous
  hardcoded v1 paths, byte-proven unchanged (same diff-only convention as
  T-PARSE-YCH12-2). New repo-resident: `ych11_env_template.sh` (YCH11_*
  surface, CONC=2/PROBE_WAIT=45 cadence), `ych11_reseed.sh` (L-024 law:
  corpus<-pristine, report<-landed, baseline<-landed corpus) and
  `ych11_reconcile.py` (three-way R1-R6 port of ych12_v2_reconcile.py —
  logic is id-generic, zero ych12-specific bits). Template-doc nit found and
  fixed here: the reseed writes the baseline next to the corpus (out/), the
  reconcile doc line now says $YCH11_WS/out/baseline_landed_v1.jsonl (the
  YCH12 template carries the same stale doc line — untouched this round,
  disclosed for its next touch). Chain sanity before grinding: reseed ->
  merge (130 applied, anchor 0 drift) -> reconcile ALL PASS net-new 0 vs the
  landed corpus — the parameterized toolchain reproduces the landed state.
- GRIND (9 windows, 07:39-08:49Z, CONC=2, PROBE_WAIT=45, foreground 580 s):
  6 harvesting — +49/+25/+27/+21/+24/+19 = **+165 ok** (130 -> 295); 3 fully
  walled (08:36Z onward, ~25 min closure) -> parked. rejected 14 -> 28
  (+14), error-cum-429 records 8 -> 20 (all retried to terminal on their
  next run by the self-heal law). todo 477/800 (done-set 323).
- AUDIT: 0 Unicode-unit regressions; 17/293 changed chunks carry residual
  18+ lowercase runs — 15 are genuine chemistry vocabulary (disproportionation,
  tetrachloromethane, trifluoromethanesulfonate, electronegativities,
  bromomethylpropane), benign; 2 chunks (ych1_v1_u6_c21_pdf172_0960,
  ych1_v1_u10_c0_pdf313_1702) retain sentence-length space-glue the pass-1
  model declined to fix. PASS-2 spot retry (repo-resident
  `retry_glue_ych11.js`: re-asks only those ids with the runner's exact
  prompt + sanity check; appends an improved ok record ONLY on a clean
  pass, so a 429/failed retry appends nothing and the pass-1 record stands
  — latest-wins merge can never regress) fired twice, both walled (429) —
  nothing appended, disclosed residual, re-run when the wall cracks.
- LANDING CHAIN: reseed -> merge (1571 chunks, llm_repaired 295, text
  changed 293, anchor PASS 0 drift) -> reconcile ALL PASS (net-new 165,
  overlap 130 re-applied from pristine, R6 no orphans) -> audit 0 Unicode
  regressions -> validate ALL CHECKS PASSED x2 (workspace + repo copy, EP
  10/10). Artifacts copied back to parsed/ + evidence/ (325 records).

Stage Summary:
- **Polish 130/800 -> 295/800 (net-new +165, the lane's largest single
  round), on the fully parameterized YCH12-v2-convention toolchain; every
  gate green.** Open follow-ups: (a) todo 477 + 20 error-cum-429 records —
  grind resumes as R6; (b) the 2-chunk glue residual — retry_glue_ych11.js
  when the wall cracks; (c) YCH11_BASELINE doc line in the YCH12 env
  template (disclosed above).

---
Task ID: T-PARSE-YCH11-1-R6
Agent: Z.ai (main, zai-web)
Task: "Continue" (2026-11-02, zai-web, trace 1a19c372e4e0d355) — resume the
R5-parked 295/800 grind on the established parameterized toolchain.

Work Log:
- Sandbox reset #15 recovery: mirror rolled back to the base image again
  (refs at a8803c5, 12e136296 objects gone) — fetch + ff to tip fb28c174.
  Opening guard: 12e136296..fb28c174 checked for ych11/ledger activity —
  ZERO commits touch the lane or books/README.md + CATALOG.md (the 20
  parallel commits are physics guided waves 1-3, T-GRADE-7/8/9,
  T-OEQ-MATHSB-SERVE-1, T-OEQ-PHYS-FORMAT-1); baseline stands. Sparse
  flipped back to cone mode (parallel-session law) — full non-cone pattern
  set re-applied, lane materialized. Workspace: partial-survival reset
  (data/ kept, node_modules + mirror gone) — env copied from the
  repo-resident template, reseed (corpus<-pristine, report<-landed,
  baseline<-landed corpus), evidence 343 records + 800 ids copied in.
- GRIND (12 windows, 18:15-20:03Z, CONC=2, PROBE_WAIT=45, foreground 580 s):
  9 harvesting — +56/+26/+26/+26/+26/+26/+27/+42/+11 = +266 terminal
  (295 -> 555 applied after one pre-landing drop, below); 3 fully walled
  (W7, W11, W12; the 20:03Z closure ran past the round's stop rule) ->
  parked. rejected 28 -> 33 (+5), error-cum-429 records 20 -> 41 (all
  self-heal candidates for R7; the bursty-crack rhythm continues).
- ENOSPC INCIDENT (W9, 19:40Z): disk hit 100% mid-window (global usage —
  4.1G partial-clone .git + 3.1G legacy workspaces + 1.9G docling venv),
  runner died on a log append. Remediation: freed ~1.28G (scratch/ych11
  probe renders 213M, workspace probe/ 48M, docling HF model cache 1,012M
  — all re-derivable); evidence tail-check found ONE truncated record
  (ych1_v1_u3_c9_pdf090_0535 ok, cut mid-string by the failed append) —
  dropped with backup (llm_repairs_ych11.jsonl.bak_enospc_20261102), the
  id stays out of the done-set so the runner re-attempts it (self-heal
  law); all 617 surviving records parse clean.
- PASS-2 GLUE RETRY (retry_glue_ych11.js): ych1_v1_u10_c0_pdf313_1702
  CLEARED (improved repair appended, 1203 -> 1233 chars — input taken
  from the LANDED corpus, note: the workspace corpus is pristine by
  reseed design, the pass-2 targets are repaired chunks); 1 of R5's two
  residuals closed. Re-run later against the merged corpus + the R6 audit
  added two NEW true-glue targets (ych1_v1_u5_c15_pdf151_0858,
  ych1_v1_u0_c0_pdf003_0009; ych1_v1_u6_c21_pdf172_0960 NOOP'd once) —
  RETRY_IDS updated to the 3-id list; two attempts (20:05Z, 20:08Z) both
  fully walled, nothing appended (invariant held), disclosed residual.
- VALIDATE-GATE DROP (first in lane history): one R6 ok record
  (ych1_v1_u5_c15_pdf146_0835) repaired its chunk 2315 -> 2447 chars,
  over the book's 2400 hard max — the runner's sanity check verifies
  content ratios (0.6x/1.7x + lcsRatio 0.97) but never the book-level
  bound, a blind spot this round closes: `llm_repair_ych11.js` and
  `retry_glue_ych11.js` sanityCheck now reject t.length > 2400 (R6
  lesson comment in-code). The record was dropped with backup
  (.bak_drop_20261102), the id returns to todo for an R7 re-attempt
  under the patched gate; reseed -> re-merge -> reconcile re-run clean.
- LANDING CHAIN: merge (1571 chunks, llm_repaired 555, text changed 552,
  anchor PASS 0 drift) -> reconcile ALL PASS (net-new 260, overlap 295
  re-applied from pristine, 591 latest-wins ids: 555 ok / 33 rejected /
  3 err in flight) -> audit 0 Unicode regressions (25 residual 18+
  lowercase runs: 22 benign chemistry vocabulary + the 3 glue targets
  above) -> validate ALL CHECKS PASSED x2 (workspace + repo copy,
  EP 10/10) -> artifacts copied back, cmp byte-equal x5 (corpus / md /
  report / evidence / ids).

Stage Summary:
- **Polish 295/800 -> 555/800 (net-new +260, todo 212), every gate green;
  tooling hardened on two fronts (book-bound sanity + pass-2 target
  refresh).** Open follow-ups: (a) todo 212 + 41 error-cum-429 records —
  grind resumes as R7; (b) 3-chunk glue residual (u6_c21 / u5_c15_pdf151 /
  u0_c0) — retry_glue_ych11.js when the wall cracks; (c) YCH12 env
  template stale baseline doc line (still disclosed-untouched).
