# YCH12 SB2 — Method and Findings (T-PARSE-YCH12-1)

Deviations, laws and one-off findings for the IAL Chemistry SB2 parse. The
YPH11/YCH11 METHOD records (D-1..D-12) carry over unchanged except where
superseded below; this file logs only what is NEW or DIFFERENT on SB2.

## D-1 Source and archive copy (unchanged in kind)
taleem360 direct link `?f=a4c5a983` (Googlebot UA, method of record); original
of record 162,939,218 B sha256 `44af34a5…748`; ghostscript 145 dpi derivative
72,675,329 B sha256 `7b1bc6cf…618` landed under the 100 MiB limit (L-022).
Cover carries the third-party "PDF COMPILED BY SAAD" mark (SB1 was clean).

## D-2 Page law: book = pdf − 12, roman = pdf − 0
4-way confirmed. TWO deltas vs SB1: the offset is 12 (not 13) and the roman
front matter maps as `roman = pdf − 0` (SB1 was pdf − 1) — roman i does not
exist and roman ii is PDF 2. Lesson: NEVER carry a sibling book's roman law
across; probe it (the SB1-derived assumption would have shifted every front
matter chunk by one page).

## D-3 Structure law: chapter-list chip ≠ chapter banner
Each topic's opener spread (divider 2pp) shows a chapter-LIST chip ("A ENTROPY
| B LATTICE ENERGY"); for single-chapter topics (11, 13, 18, 19, 20) the chip
shows a single "A …" line that reads like a chapter banner (it fooled the
first probe on PDF 14). The banner + LEARNING OBJECTIVES actually land on the
topic page + 2. The CHAPTERS map follows the physical book: dividers
(topic, topic+1), chapters from topic+2.

## D-4 End matter: FOUR graph-paper leaves
Books 305–308 (PDF 317–320) are four blank practice graph grids (printed chips
305/306/307/308), one more than SB1's single end leaf. All four are image-only
by-design gaps, each registered individually in parse_report.by_design_gaps
and asserted by the validator.

## D-5 Environment rebuild hazards (workspace recycle)
1. torch/torchvision binary mismatch: the recycled venv had a CUDA-era
   torchvision whose `torchvision::nms` operator was absent from
   torch 2.14.1+cpu → `RTDetrImageProcessor` import failed. Fix:
   `pip install --force-reinstall --no-deps torchvision --index-url
   https://download.pytorch.org/whl/cpu` (0.29.1+cpu). transformers pinned
   4.52.4 (newer versions drop RTDetrImageProcessor).
2. `pip` on PATH belongs to python3.13 while `python3` is a 3.12 venv — use
   `python3 -m pip` exclusively.
3. docling 2.33 with a set-but-invalid `artifacts_path` fails EVERY page with
   an empty-items error record instead of downloading models. 27 pages were
   silently error records before the first content check caught it. Fix:
   leave artifacts_path unset (auto-download), delete the error pages, re-run.

## D-6 Foreground-window discipline (cause identified)
Background processes (nohup AND setsid) are reaped seconds after the tool
call that spawned them ends in this runtime. All long work MUST run as
foreground windows against checkpointed state (the r0 OCR pattern), or be
re-launched per window. This is now a known environment law, not a style
preference.

## D-7 Formula rescue, partial by design
315 empty formula regions on 101 pages (L-020 bug class). 133 transcribed
verbatim across 12 batch windows (127 fills + 6 adjudicated slivers/duplicates
— including two overlap cases where docling emitted a single-line region
nested inside its multi-line parent; the parent carries the full block, the
nested region is adjudicated empty, never double-filled). 182 orphans on 71
pages remain — shipped partial and resumable, exactly like the YCH11 polish
R1 partial. The sidecar application is idempotent and bbox-verified (0
mismatches).

## D-8 ID law
`ych2_v1_u<unit|0>_c<chapter|0>_pdf<pdfpage:03d>_<block:04d>`, unit = topic
number 11–20 (never 1–10), chapter = sequential c1–c19 over the lettered
chapters 11A–20A.

## D-9 EP banks and back matter typing
Unchanged from YCH11 r0: per-TOPIC EXAM PRACTICE typed `chapter_questions`
(chapter_no None), THINKING BIGGER 2pp spreads typed `thinking_bigger`, back
matter attached to unit 20 (not 10 — SB2's back matter starts at book 282).

## D-10 Validator deltas vs YCH11
Coverage checks: index pages pdf 311–316 (not 322–328); by-design gaps
(310, 317, 318, 319, 320); topic coverage 11–20; id grammar ych2_v1_.
ALL CHECKS PASSED post-rescue, post-double-run.

## D-11 Polish R1 staged, not started
select_noisy: 800/1400 selected (80 question chunks force-included), ids at
pipeline/evidence/llm_repair_ids_ych12.json. The account-level 429 wall that
parked YCH11 polish at 48/800 (2026-10-24) was probe-verified still up
2026-10-25 — R1 not attempted beyond staging. Resumable per PM-3.

## D-12 v2 fresh-parse lane (T-PARSE-YCH12-2, 2026-10-27)
1. PAGES RECOVERED, NO OCR RE-RUN: the R2 rebuilt docling_pages (2026-10-25)
   survived a later workspace recycle with the FULL 315-record sidecar already
   applied — re-verified item-for-item at v2 session start (306 filled-exact +
   9 adjudicated-empty = 315/315). The of-record v2 OCR env is therefore the
   R2 rebuild: docling 2.33.0, rapidocr-onnxruntime 1.4.4, transformers
   4.52.4, torch 2.14.1+cpu, onnxruntime 1.31.0 (the position-proven pin).
2. VERSIONING LAW: `YCH12_VERSION` env re-tags ids + filenames
   (`ych2_v2_u…`, chunks_v2.jsonl, parse_report_v2.json); the default v1
   reproduces the r0 recipe — byte-proven (prefix-swap diff == identical).
   Validator gains the same env assertion.
3. RE-CHUNK: 1406 chunks (deterministic re-run of the same pages equals the
   R2 count), validator ALL CHECKS PASSED (19 chapters, 10 topics, EP 10/10,
   index pdf 311-316, by-design gaps asserted).
4. ADJUDICATION (v2-raw vs v1-pristine, both pre-polish): error-class rates
   per 10k chars statistically identical — space_run 41.21/41.55, caps_glue
   7.92/7.98, camel_glue 2.96/2.98, latex_remnant 0/0, repeated_punct
   30.75/30.98. Structure identical (17 content types, EP banks 20 pages /
   10 ranges, thinking_bigger 69, units 11-20). 0 over-hard-max; char_count
   41-2367.
5. RESCUE CONSUMPTION: 305/306 sidecar fills verbatim-or-whitespace-
   normalized in v2 chunk text. The 1 residual (p49 i9, `N₂(g) + 3H₂(g) →
   2NH₃(g)`) is dropped by the <40-char pack floor via the WORKED EXAMPLE 2
   micro-segment (heading 14 + formula 25 = 39 chars) — the SAME drop exists
   in v1 (pre-existing edge, not a v2 regression); pages + sidecar retain it.
   Follow-up EXECUTED (T-PARSE-YCH12-2-FOLD-1, 2026-10-31, own gate): the
   residual folded into the next reading-order chunk
   `ych2_v2_u12_c2_pdf049_0220` (body, UNPOLISHED — folding into the
   polished `_0219` is R1-illegal: a polished chunk's corpus text is frozen
   to its evidence repair text) — prepend `WORKEDEXAMPLE2\n\nN₂(g) + 3H₂(g)
   → 2NH₃(g)` (40 chars, sidecar i8+i9 byte-match), pristine of record
   edited in place (474 -> 516 chars, char_count law preserved), corpus +
   markdown + report regenerated through the resident chain
   (reseed -> merge, 748/743, anchor 0 drift); the fold gate: corpus diff
   vs the landed corpus is EXACTLY that one chunk (+42 chars,
   fold-prefixed, anchors/text_original/llm_repaired byte-identical),
   reconcile ALL PASS x2 (workspace + repo), audit 0 Unicode-unit
   regressions, validator ALL CHECKS PASSED x2 — **306/306 sidecar fills
   now consumed**. Tool: `pipeline/scripts/ych12_v2_fold_p49i9.py`
   (sidecar byte-match + idempotence-guarded; docling_pages_v2 is
   sparse-excluded, so the sidecar reads via git show with a
   YCH12_SIDECAR_P49 fallback). v1 keeps the drop as landed history
   (byte-untouched law); the chunker's drop-semantics floor is left
   as-is — any future-parse behavior change would need its own
   deterministic proof per L-025.
6. DRIFT DISCLOSURE: 947/1406 id slots shared with v1 (67.4%); text
   identical on 326 shared slots (34.4%) — a different OCR run of the same
   scan (position-true per R2), disclosed not defective. The 103 v1 polish
   repairs do NOT carry over by id; polish restarts on the v2 pristine.

## D-13 Polish R1-v2: env-parameterized grind on the v2 corpus of record (T-PARSE-YCH12-2 POLISH-CONT-V2, 2026-10-27)

1. SCRIPTS: `llm_repair_ych12.js` / `merge_llm_ych12.py` /
   `audit_polish_ych12.py` gained the lane env surface (`YCH12_CORPUS`,
   `YCH12_IDS`, `YCH12_REPAIRS`, `YCH12_PRISTINE`, `YCH12_MD`,
   `YCH12_REPORT`, `YCH12_LOG`). No-env defaults are the original v1 paths,
   byte-proven unchanged (the L-026 law); the clobber-law warning lives in
   the merge docstring.
2. STAGING: 801 ids on v2 (`pipeline/evidence/llm_repair_ids_ych12_v2.json`;
   force-inclusion pushed one over the 800 cap — the runner consumes the
   list as-is). Baseline: v2 validator ALL CHECKS PASSED before grinding.
3. GRIND: burst-harvest regime as POLISH-CONT-2 (probe loop 5x60s,
   quota-stop after 2 consecutive 429 chunks, append-only JSONL resume;
   evidence `llm_repairs_ych12_v2.jsonl` SEPARATE from the v1 evidence —
   v1 history stays intact).
4. MERGE LAW (restated, load-bearing — L-024): seed the v2 corpus from the
   v2 `.pristine`, apply the FULL evidence exactly once, three-way reconcile
   (vs pristine expected-fixes / vs landed net-new /
   text_original==pristine), then audit + validate (YCH12_VERSION=v2).
