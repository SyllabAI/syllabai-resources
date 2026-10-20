# 4BI1 Biology — Parse Method & Findings (text-layer lane)

**Task:** T-PARSE-4BI1-1 · **Book:** Pearson Edexcel International GCSE (9-1)
Biology Student Book (Bradfield & Potter, Pearson 2017, ISBN 978-0435185084)
· **Source sha256:** `974ad65d913108b9caa98df9eda1584e546177854bcd5efa6d8642797d093006`
· **Date:** 2026-10-21 · **Playbook:** `books/README.md` §5 phases 0–10

## 1. What made this lane different (text-layer route)

This is the **first text-layer lane** in the corpus. Playbook §5 phase 1 says
a book with a text layer must "stop and re-plan" — the intake
(T-INTAKE-4BI1-1) had already re-planned: the source is a **native text
layer** (Adobe Acrobat Pro DC 15 / Microsoft Word 2016 print-replica
conversion), NOT a scan. Consequences:

- **IBM Docling + RapidOCR + CodeFormula are NOT used.** No OCR at all.
  PyMuPDF 1.26.7 extracts the native text with coordinates in ~40 seconds
  for the whole book (vs ~27 s/PAGE for RapidOCR on the physics scans).
- No formula-enrichment retry ladder, no Tesseract fallback, no version
  mines (PM-1 does not apply), no sidebar double-OCR dedup.
- New failure modes replace the OCR ones: broken font→Unicode maps on the
  stylized display/italic font (see §3), and 2-up spread geometry (§2).

## 2. Book geometry — the 2-up law (three-way confirmed)

179 landscape spreads (841.9 × 525.7 pt); **every spread carries two book
pages**: left half = even page `2s−10`, right half = odd page `2s−9`.
Book page 1 = spread 5 R; spreads 1–5 L = cover + roman i–viii; book 349
(spread 179 R) = blank back cover (0 text lines, 11 images).

Three-way confirmation (probe_4bi1_structure.py, evidence in
`data/biology/probe_out/`):
1. **Running-header digits:** 93 right-half top-band hits follow `2s−9`
   across spreads 72–178; left-half hits (spreads 7–11) follow `2s−10`.
2. **Course-structure digits:** ch1 p3 → spread 6 R, ch2 25 → 17 R,
   ch3 39 → 24 R, ch4 52 → 31 L … ch22 289 → 149 R — all verified.
3. **LEARNING OBJECTIVES opener hits:** 15/22 land exactly on the computed
   opener half-pages; the other 7 have CMap-garbled headings, verified by
   direct dump (see §3).

Both page numberings are carried per chunk (PARSE_STANDARD point 1):
`pdf_pages` = [first_spread, last_spread] (viewer numbering of the PDF),
`book_pages` = [first, last] numbered book page covered (null for front/back
matter). The validator re-derives the 2-up law and rejects any chunk whose
book_pages fall outside the spread-derived range.

## 3. Findings — how this text layer actually behaves

- **Broken-CMap display/italic font (the dominant noise class).** The
  stylized display font's ToUnicode map is broken, so italic chapter intros,
  figure captions, box headings and running headers extract garbled:
  "hvmg organisms" (=living), "1s" (=is), "1n" (=in), "chapler" (=chapter),
  "KEV POINT"/"kEY POIHl" (=KEY POINT), "ANO" (=AND), "FOOO" (=FOOD),
  "U1e" (=The), "!his" (=This), "worl<" (=work), "charactenstics", word
  arrows " -+ " (=→), running-header "PLANTS AND FOOO 135". Regular body
  text is CLEAN — the damage is concentrated in italic/display spans.
- **Skill-tag icon junk.** The pedagogy icons (critical thinking, analysis,
  reasoning…) extract as glyph junk: "mD", "11>", "Ell>", "BD", "DD",
  "IEl:!l!l>", sometimes merged with the skill word ("mDANAlYSIS").
- **NO intra-word space splitting.** The intake warned about "differen t
  organs" style artifacts; the real extraction shows PyMuPDF's natural span
  concatenation already re-joins kerning splits ("Th"+"is" → "This"). An
  earlier probe that displayed spans space-joined produced the illusion of
  splits. Lesson L-013.
- **Small-font bullets garble to digits.** LO list bullets render as "11",
  "1", "e", "_" ("11 Investigate diffusion…"). This kills naive
  span-size-based sub/superscript recovery (a subscript heuristic would
  convert bullets to subscripts) — chemical formulas therefore stay as plain
  digits (CO2, C6H12O6) in v1; see §5 D-7.
- **5 of 22 chapter openers carry no extractable LEARNING OBJECTIVES text**
  (ch9, 10, 14, 15, 19 — outline/graphic boxes, 0 text). 17/22 have LO
  chunks (15 via headings incl. garbled "W ANING OBJECTIVES", +2 via the
  opener verb-bullet fallback added to the chunker).
- **22/22 chapters have end-of-chapter question sections**, each announced
  by a "More questions on X can be found at the end of Unit N on page M"
  cross-reference line — exactly 22 such lines, used as the authoritative
  anchor for QUESTION_RANGES (headers alone are unreliable: only 6 strict
  "CHAPTER QUESTIONS" matches, some mid-page at y=409).
- **6 units (not 4):** the intake README guessed "Units 1–4"; the course
  structure shows 6 (Organisms and Life Processes, Animal Physiology, Plant
  Physiology, Ecology and the Environment, Variation and Selection,
  Microorganisms and Genetic Modification), 22 chapters.
- **ANSWERS section (book 329–348)** is present but NOT listed in the book's
  own contents pages — found via marker census ("UNIT 1 ANSWERS" header,
  spread 169 R). Organized by UNIT N ANSWERS → CHAPTER N.
- **Unit question banks** (with sz≈17 "UNIT QUESTIONS" headers): book
  32–37, 130–133, 182–185, 221–225, 277–279, 301–302. On continuation pages
  the running header itself reads "UNIT QUESTIONS" (y=14) — a naive
  header-strip band (y<30) is safe only because page CONTEXT types those
  pages, never the stripped header (serving-critical discipline).
- **Front matter** carries real content (copyright, course structure with
  spec codes, about-this-book, assessment overview with weightings) plus a
  few stylized-art junk lines ('11wBli\MiM!…') from the cover/assessment
  graphics — kept as-is in 2 front-matter chunks, documented.
- **Unit dividers are near-empty graphic pages** (u4 divider = 0 text lines)
  — divider chunks exist where text exists (6/6 after the min-size drop to
  <20); u4's divider content is graphics-only and is recorded here.

## 4. Decision log

- **D-1 (text-layer route).** PyMuPDF native extraction replaces the Docling
  OCR stack for this lane. Approved by intake; playbook §5 phase 1 re-plan
  clause. Extraction (extract_text_4bi1.py) writes per-half-page JSON
  checkpoints (skip-if-exists, resumable; golden rule 7).
- **D-2 (half-page context).** Page context is keyed per (spread, side)
  half, not per PDF page — chapters change mid-spread. Chunker inherits
  physics segment/packing logic unchanged otherwise.
- **D-3 (natural stream order, NOT y-sort).** Word print-replicas export
  blocks in authored reading order. Y-sorting was tested and INTERLEAVES
  sidebar boxes (DID YOU KNOW sidebars come as coherent blocks first in
  stream order). All probes that pre-sorted by y were re-run before any
  structural conclusion was baked in.
- **D-4 (surgical cleaning only).** The first cleaner draft dropped tokens
  without 3+ consecutive letters — silently eating two-letter words
  ("composed of" → "composed"; caught in self-review, PM-4 discipline).
  Surviving cleaner: skill-word salvage from icon-merged tokens, dash-rule
  line drops, whitespace normalize; everything else verbatim. Residual icon
  junk (~150 tokens) is the LLM polish phase's job.
- **D-5 (question anchors from cross-reference lines).** QUESTION_RANGES
  (22 chapters) anchored on the per-chapter "More questions …" lines,
  cross-checked against "Total N marks" census and skill-tag density.
  Serving-critical typing derives from page CONTEXT (structure module),
  so stripped running headers can never break it.
- **D-6 (additive content types).** Added `did_you_know` (59 chunks) and
  `biology_only` (the Double-Award label boxes) on top of the physics set —
  additive per golden rule 3. `back_cover` exists as a type for the blank
  final half (produces 0 chunks; recorded).
- **D-7 (no sub/superscript conversion in v1).** Span-size heuristics are
  unsafe here (garbled bullets mimic small spans). Formulas stay CO2/C6H12O6;
  validator reports 0 Unicode sub/sup chunks as EXPECTED for this lane.
  Candidate for an additive v2 using vertical-offset analysis.
- **D-8 (LO opener fallback).** Opener half-pages get a verb-bullet
  detection (Understand/Know/Describe/…) that starts a learning_objectives
  segment when the LO heading is garbled — recovers 2 otherwise-body openers.
- **D-9 (garble-map-normalized fidelity guard).** The LLM polish guard
  normalizes KNOWN garble classes in both strings before the char-level
  whitespace-stripped LCS ≥ 0.97 check, so transcription repairs that fix
  character substitutions pass while wording changes still bite (extends
  the PM-2 guard to substitution-class damage).
- **D-10 (LLM polish scope).** 363/871 chunks selected: all 171
  question-typed chunks (serving-critical, force rule) + 192 garble-scored
  chunks (0 obvious garbles missed outside selection). Selection heuristics
  were tightened twice after false-positive storms (living/lumen words).

## 5. Results

- **871 chunks** (`bio_v1_` prefix), 0.83 MB chars, size min/median/max =
  20/943/2095, 0 over HARD_MAX 2400.
- Content types: body 344, chapter_questions 126, answers 65, did_you_know
  59, key_point 58, unit_questions 45, extension_work 34, glossary 29,
  learning_objectives 21, appendix 21, index 20, front_matter 15, exam_hint
  11, safety 9, divider 6, practical 5, biology_only 2, skills 1.
- Validation: **ALL CHECKS PASSED** (validate_biology.py): unique IDs,
  15-key grammar, 22/22 chapters, 6/6 units, 0 order breaks, dual numbering
  + 2-up law coherence, question anchoring to all probed ranges, answers
  coverage 329–348, size bounds, char_count recomputation.
- LLM polish round 1: 363 selected; N applied / rejected / quota-pending —
  see parse_report_v1.json `llm_polish` for the final numbers (updated by
  merge_llm_biology.py, which also runs the 0-drift anchor diff).

## 6. Reusable lessons (see also books/README.md §9 ledgers)

- Print-replica text layers fail via FONT ENCODING, not OCR: damage is
  deterministic per font/style, concentrated in display/italic spans.
- The book's own cross-reference apparatus ("More questions … on page M")
  is a stronger structural anchor than decorative section headers.
- Probe-display code can CREATE the noise it reports (space-joined span
  dumps simulated intra-word splits). Always re-derive noise classes from
  the production extraction before writing cleaning rules.
