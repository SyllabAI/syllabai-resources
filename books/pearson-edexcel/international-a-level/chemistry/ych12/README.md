# Pearson Edexcel International A-Level Chemistry (2018), YCH12 — Student Book 2

**Status:** SB2 **PARSED** (T-PARSE-YCH12-1, 2026-10-25: corpus v1 1400 chunks,
validator ALL CHECKS PASSED; 315 blank display-equation regions exported, 133
transcribed verbatim by the agent rescue pass (127 fills + 6 adjudicated);
rescue R2 (T-PARSE-YCH12-1-R2, 2026-10-25): the remaining 182 orphans ALL
transcribed verbatim and banked at
`pipeline/evidence/rescue_r2_2026-10-25/` (315/315 sidecar coverage,
bbox-verified position-true against an independent second OCR run), but the
landing is BLOCKED — the sandbox reset destroyed `docling_pages/`, the rebuilt
320-page re-OCR failed the pre-declared re-chunk diff gate (33% chunk-id
renumber, 68% shared-id text drift; suspected unpinned onnxruntime backend),
so the landed v1 corpus stands byte-untouched; consumption needs a fresh-parse
(v2) lane — see the rescue R2 README. LLM polish R1 at 103/800 (POLISH-CONT-2, 2026-10-26), quota-walled,
resumable). **v2 fresh-parse lane COMPLETE (T-PARSE-YCH12-2, 2026-10-27): the R2 pages survived the
recycle with the FULL 315-record sidecar applied (re-verified 306+9=315/315) — consumed as the v2
corpus of record (1406 chunks, `ych2_v2_`, validator ALL CHECKS PASSED; adjudication: error-class
rates identical to r0, structure identical, 305/306 fills in chunk text — METHOD D-12).** v2 polish R1
grind **COMPLETE** (POLISH-CONT-V2, 2026-10-27; CONT-V2-2/3, 2026-10-28; CONT-V2-4/5/6, 2026-10-30;
CONT-V2-7/8, 2026-10-31): runner/merge/audit parameterized
via env (defaults = v1 byte-proven unchanged, L-026), **801/801 staged ids terminal — 748/801 applied
(53 rejected by guard, raws in evidence; 64 error-cum-429 records all retried to terminal)** across
~50 quota windows (merge anchor 0 drift from the v2 pristine, three-way reconciliation ALL PASS,
audit 0 Unicode-unit regressions, validator ALL CHECKS PASSED; CONT-V2-8 closed the grind: the last
78 harvested behind a ~56-minute full closure then a 3-window crack, final id `ych2_v2_u17_c0_pdf231_1131`
OK 2026-10-31). Pack-floor fold fix (T-PARSE-YCH12-2-FOLD-1, 2026-10-31): the
last unconsumed rescue fill (p49 i9, dropped by the <40-char pack floor) folded
into the next reading-order chunk `ych2_v2_u12_c2_pdf049_0220` with its own
gate (pristine of record edited, corpus regenerated, one-chunk diff proof,
reconcile/audit/validator all green ×2) — **306/306 sidecar fills consumed**.
SB1 = parsed in the sibling `ych11` lane. Scaffold per
`books/README.md` §5 (copy of the `chemistry/ych11` IAL lane).

## Books of this lane

### Pearson Edexcel International A Level Chemistry Student Book 2

- **Title:** Pearson Edexcel International AS / A Level Chemistry Student Book 2
- **Authors:** Cliff Curtis, Jason Murgatroyd, with David Scott (verified from the landed copy's cover, per E-001 discipline)
- **ISBN:** 978-1-292-24472-3 (Pearson 2019; printed on the imprint page of the artifact itself + dokumen.pub listing cross-check)
- **Coverage:** IA2 Units 4 & 5 = Topics 11–20 (Unit 4: Rates, Equilibria and Further Organic Chemistry = Topics 11–15; Unit 5: Transition Metals and Organic Nitrogen Chemistry = Topics 16–20). Units 3 and 6 are practical units — no SB.
- **File:** `source/student-book-2.pdf` (ARCHIVE COPY — derivation note below)
- **Pages:** 320 PDF pages (front matter roman ii–xiii = PDF 2–13; arabic book 2–308 = PDF 14–320; book page 1 does not exist in the PDF — print blank omitted, same law class as YCH11/YPH11; roman i also absent)
- **Bytes:** 72,675,329
- **sha256 (archive copy):** `7b1bc6cfaddb79cb067072dbe623be5f87da632f556141ea1c1bd9db60a6be18`
- **Original of record:** 162,939,218 B, sha256 `44af34a590914e81bac53b0fbdca92a742ce7c0b43cd6b85166a39be670ee748`, retained at the provenance URL
- **Quality:** Image-only print replica (Acrobat 19.12 Image Conversion producer; zero text layer — 5/5 sampled pages 0 chars) → OCR route. Cover carries a third-party "PDF COMPILED BY SAAD" mark (same class as the YPH11 siblings; disclosed).
- **Derivation note (disclosed):** the original exceeds GitHub's 100 MiB hard file limit, so the archive copy is a ghostscript `pdfwrite` derivative (/ebook, 145 dpi Bicubic, `-dPassThroughJPEGImages=false` per books/README.md L-022). Pages unchanged (320/320); derived in 9.7 s.
- **Parse of record (T-PARSE-YCH12-1, 2026-10-25):** docling 2.33.0 + rapidocr-onnxruntime 1.4.4 OCR route (formula enrichment OFF — 2.33 emits empty formula text either way, YCH11 D-7/L-020), 320/320 pages checkpointed in 8 foreground windows (~9.2 s/page avg, index tail slower, 0 page errors, peak RSS 2.2 GB); page law `book = pdf − 12` confirmed 4 ways; 2 units / 10 topics / 19 lettered chapters (11A–20A); per-topic THINKING BIGGER (2pp) + EXAM PRACTICE (2pp) banks (10/10 anchored); corpus v1 = **1400 chunks** (`ych2_v1_`), validator ALL CHECKS PASSED; formula rescue partial (127 fills + 6 adjudicated of 315 orphans; 182 resumable); LLM polish R1 partial (103/800 of the staged ids, quota-walled, resumable; CONT-2 2026-10-26)
- **Provenance:** https://www.taleem360.com/edexcel-international-a-level-chemistry-student-book-2-in-pdf-kyc (direct download link `?f=a4c5a983`, served 162,939,218 bytes to a Googlebot UA — the method of record from the YCH11/YPH11 lanes; this title was not reCAPTCHA-walled)

## Structure (probed 2026-10-25, production-confirmed at parse)

- **Page law:** `book = pdf − 12`, confirmed 4 ways: (1) roman headers PDF 3 = iii, PDF 13 = xiii (`roman = pdf − 0`, roman i absent); (2) TOC cross-checks (TOPIC 11 = book 2 → PDF 14; TOPIC 20 = book 258 → PDF 270); (3) printed header digits (PDF 311 prints "299" = INDEX; PDF 317/318 print "305"/"306" on the graph leaves); (4) end leaf PDF 320 prints "308". TOC's INDEX 299 promise present → copy COMPLETE (L-021).
- **Units/topics/chapters:** 2 units, 10 topics, 19 lettered chapters (11A; 12A–B; 13A; 14A–B; 15A–E; 16A–B; 17A–C; 18A; 19A; 20A). Unit 4 = Topics 11–15 (book 2–157), Unit 5 = Topics 16–20 (book 158–281). Every topic's opener spread (divider 2pp) carries the chapter-list chip, NOT the chapter banner; chapters start at the topic page + 2 (= first section / LEARNING OBJECTIVES page).
- **Per-topic THINKING BIGGER** (2pp, first pages book 26/54/74/102/154/178/216/232/254/278) **+ EXAM PRACTICE banks** (2pp, book 28/56/76/104/156/180/218/234/256/280) — 10/10 page-anchored, typed `chapter_questions` per the YPH11 EP precedent.
- **Back matter:** MATHS SKILLS 282, PREPARING FOR YOUR EXAMS 286 (incl. SAMPLE EXAM ANSWERS 288), COMMAND WORDS 293, GLOSSARY 295, PERIODIC TABLE 298, INDEX 299–304, graph-paper end leaves 305–308 (FOUR practice grids — one more than SB1). NO answers section (Pearson publishes answers separately).
- **Front matter:** cover, ii–xiii (imprint, CONTENTS, course structure ×4, about this book ×2, practical skills, assessment overview ×2) — `book_pages: null`.

## Course binding (planned)

v2 hub course ial-chemistry-17 · specKey
`pearson-edexcel/international-a-level/chemistry/ych12` — hub wiring lands at the serving lane.


## SERVING (T-BOOK-SERVE, 2026-10-31 — operator order trace 1a18fe1f9cace659)

- **r0 serving package LANDED**: `manifest.json` (book-slices-manifest-v2; unit =
  TOPIC 11–20) + `chapters/u{t}_c{n}.pdf` (19 lesson slices, 11A–20A) +
  `units/u{t}_practice.pdf` (10 per-topic EXAM PRACTICE banks as `unit_exam`) +
  root `student-book-2.pdf` (blob-reuse of source/). THINKING BIGGER pages
  honestly unsliced. Receipt: `pipeline/slices-gen-receipt.json`.
- documentId `c40f6853-a50c-5743-9a53-611ade397fba` (derived ibm-docling@v3 of the archived bytes,
  sha256 `7b1bc6cf…be18` — suffix abbreviation corrected per E-008 companion
  note).
- Remaining: hub multi-book law (v2 PR) → DB apply + T-C20 flip (operator-gated,
  Neon MAIN paused).

## Next steps

1. ~~Resume the formula rescue (182 orphans on 75 pages)~~ — DONE as labor
   (T-PARSE-YCH12-1-R2): all 182 transcribed + banked
   (`pipeline/evidence/rescue_r2_2026-10-25/`), landing blocked by the re-chunk
   diff gate after the sandbox reset (the rebuilt docling env is not
   byte-faithful; see the rescue R2 README). Consumption = a fresh-parse (v2)
   lane applying the full 315-record sidecar, OR a byte-faithful env
   reproduction (pin the onnxruntime backend, reuse the r0 model artifacts).
2. ~~LLM polish R1 (800 ids staged at `pipeline/evidence/llm_repair_ids_ych12.json`)~~ —
   superseded by the v2 lane: polish re-targeted at the v2 corpus of record,
   **801 ids staged at `pipeline/evidence/llm_repair_ids_ych12_v2.json`**
   (v1's 103 repairs remain v1-history; repairs do not carry by id — L-026).
   Runner/merge/audit parameterized via env (`YCH12_CORPUS`/`YCH12_IDS`/
   `YCH12_REPAIRS`, defaults = v1 byte-proven unchanged). Grind:
   quota-walled burst-harvest, foreground windows only (L-027 —
   background/nohup grind loops are reaped at tool-call end); wall closures
   vary (~20 min cadence 2026-10-27, 51+ min then ~10–12 min 2026-10-28).
3. Serving lane — ARCHIVE-SIDE r0 LANDED 2026-10-31 (T-BOOK-SERVE, trace 1a18fe1f9cace659; see the SERVING section below); remaining: hub multi-book wiring (v2 PR) + DB apply + T-C20 flip.
4. Update `books/CATALOG.md` tracker in the same commit as each state change.
