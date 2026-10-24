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
