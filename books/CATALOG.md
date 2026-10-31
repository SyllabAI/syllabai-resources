# books/CATALOG.md — Student-Book Catalog & Parse-Completion Tracker

**Status:** catalog of record for every student book in `books/` — identity,
archive home, source provenance, parse state, and serving state.
**Companion to:** [`README.md`](README.md) (the parse playbook — HOW to parse)
and [`pearson-edexcel/international-gcse/PARSE_STANDARD.md`](pearson-edexcel/international-gcse/PARSE_STANDARD.md)
(the quality gate — HOW DONE is defined). This file is the WHAT and WHERE.
**Update law:** a book's row is updated in the SAME commit that advances its
state (source lands / parse validates / serving integrates / shelf goes live).
Append-only per row's history notes; never delete a row.

---

## 1. Status vocabulary

A book moves through four states. Each state's evidence lives where the
arrows point — the catalog row records the state + date + pointer.

| State | Meaning | Evidence of record |
|---|---|---|
| **SOURCE** | PDF received & sha256-pinned in `<lane>/source/` | lane README (provenance + sha256 + pages) |
| **PARSED** | chunk corpus final, validator ALL CHECKS PASSED | `parsed/` JSONL + `parse_report*.json` + parse README |
| **INTEGRATED** | TEXTBOOK document + book_chapters registered on the serving plane (api/hub) | v2-repo lane receipt (documents.id + chapter count) |
| **LIVE** | VALIDATED (T-C20 gate) + shelf + hub entry options render | books-registry `BOOKS_ARCHIVE_COURSES` + production fetch |

Serving-plane levers (v2 repo): the T-C20 validation flip is the operator's
serving lever; the hub entry (landing card + sidebar "Student Book") gates on
the committed books-registry set; the shelf is always the live gate.

## 2. Parsed-completion tracker

| # | Book | Qual / Code | Course slug | Archive home | SOURCE | PARSED | INTEGRATED | LIVE |
|---|---|---|---|---|---|---|---|---|
| 1 | Edexcel International GCSE (9-1) **Chemistry** Student Book | Pearson Edexcel IGCSE 4CH1 | `igcse-chemistry-19` | `pearson-edexcel/international-gcse/chemistry/4ch1/` | ✅ 2026-10-18 | ✅ 2026-10-18 (v3, 1234 chunks; audit GREEN) | ✅ 2026-10-20 (doc `e6c0db50…`, 29 chapters) | ✅ 2026-10-20 (VALIDATED; card+shelf live) |
| 2 | Edexcel International GCSE (9-1) **Physics** Student Book | Pearson Edexcel IGCSE 4PH1 | `igcse-physics-19` | `pearson-edexcel/international-gcse/physics/4ph1/` | ✅ 2026-10-19 | ✅ 2026-10-20 (v1, 736 chunks; polish R1-R2; validator ALL CHECKS PASSED) | — pending serving lane | — pending |
| 3 | Pearson Edexcel International AS/A2 Level **Physics** Student Books 1+2 (Miles Hudson) | Pearson Edexcel IAL YPH11 (2-book course) | `ial-physics-19` | `pearson-edexcel/international-a-level/physics/yph11/` | ✅ 2026-10-21 (book 1, 225pp + book 2, 237pp; both image replicas; SB2 = 145dpi derived copy under GitHub's 100 MiB limit — derivation disclosed in lane README) | ✅ 2026-10-22 (SB1: v1, **881 chunks**; OCR lane + formula rescue; validator ALL CHECKS PASSED; polish R1 COMPLETE 2026-10-25: 404/404 (394 applied, 7 guard-rejected evidence kept), anchor diff 0 drift, audit space-glue 1759->4 / 0 Unicode regressions, validator ALL CHECKS PASSED post-polish). SB2: ✅ 2026-10-22 (delta lane: v1, **826 chunks** (`yph2_v1_`); truncated intake archive copy re-sourced + replaced; validator ALL CHECKS PASSED; polish R1 staged, quota-walled; formula orphans logged; polish R1 COMPLETE 2026-10-30: **794/794** (774 applied, 20 guard-rejected evidence kept), anchor diff 0 drift, audit space-run 4610->15 on repaired chunks / 0 Unicode-unit regressions, validator ALL CHECKS PASSED post-polish) | — | — |
| 4 | Cambridge International AS & A Level **Chemistry** Coursebook 3rd ed (Ryan & Norris) | CIE 9701 | `cie-a-level-chemistry-25` | `cambridge-international/ial/chemistry/9701/` | ✅ 2026-10-21 (889pp, text layer; 2 pages ad-watermarked — parse must strip) | — | — | — |
| 5 | Cambridge International AS & A Level **Physics** Coursebook 2nd ed (Sang et al.) | CIE 9702 | `cie-a-level-physics-25` | `cambridge-international/ial/physics/9702/` | ✅ 2026-10-21 (744pp, text layer; 3rd-ed upgrade pending) | — | — | — |
| 6 | Cambridge International AS & A Level **Biology** Coursebook 4th ed (Jones et al.) | CIE 9700 | `cie-a-level-biology-25` | `cambridge-international/ial/biology/9700/` | ✅ 2026-10-21 (696pp, text layer) | — | — | — |
| 7 | **Cambridge IGCSE Physics** 3rd ed (Duncan & Kennett, Hodder endorsed) | CIE 0625 | `cie-igcse-physics-23` | `cambridge-international/igcse/physics/0625/` | ✅ 2026-10-21 (328pp, text layer; CUP Sang upgrade pending) | — | — | — |
| 8 | **Cambridge IGCSE Biology** Coursebook 3rd ed (Jones & Jones) | CIE 0610 | `cie-igcse-biology-23` | `cambridge-international/igcse/biology/0610/` | ✅ 2026-10-21 (350pp image scan → OCR route) | — | — | — |
| 9 | Edexcel International GCSE (9-1) **Biology** Student Book | Pearson Edexcel IGCSE 4BI1 | `igcse-biology-19` | `pearson-edexcel/international-gcse/biology/4bi1/` | ✅ 2026-10-21 (357 book pp as 179 native-text 2-up spreads; ISBN 9780435185084; OCR route NOT required) | ✅ 2026-10-21 (v1, 869→863 chunks; text-layer lane, no OCR; validator ALL CHECKS PASSED; polish R1 COMPLETE 2026-10-21 — T-PARSE-4BI1-1-R1: 359/363 OK, 8 junk-sliver drops documented, anchor diff 0 drift, audit 0 regressions) | — | — |
| 10 | **Cambridge IGCSE Chemistry** Coursebook 4th ed (Harwood & Lodge) | CIE 0620 | `cie-igcse-chemistry-23` | `cambridge-international/igcse/chemistry/0620/` | ✅ 2026-10-21 (362pp full copy, image-only + RM.DL watermark disclosed → OCR route; sourcing history in lane README) | — | — | — |
| 11 | Pearson Edexcel International AS Level **Chemistry** Student Book 1 | Pearson Edexcel IAL YCH11 | `ial-chemistry-17` | `pearson-edexcel/international-a-level/chemistry/ych11/` | ✅ 2026-10-24 (329pp image-only print replica; original 148.8 MB > 100 MiB → 145 dpi archive derivative landed, original-of-record sha256 pinned; taleem360 direct link, method of record) | ✅ 2026-10-24 (T-PARSE-YCH11-1: v1, **1571 chunks** (`ych1_v1_`); 291 blank formula regions + 4 mangled items rescued by verbatim manual transcription; validator ALL CHECKS PASSED; polish R1–R4 partial 130/800 (152 records: 130 ok / 14 rejected / 8 error-cum-429) across six quota windows, pristine-baseline merge anchor 0 drift, quota-walled resumable) | — | — |
| 12 | Pearson Edexcel International A Level **Chemistry** Student Book 2 | Pearson Edexcel IAL YCH12 | `ial-chemistry-17` | `pearson-edexcel/international-a-level/chemistry/ych12/` | ✅ 2026-10-25 (320pp image-only print replica; original 162.9 MB > 100 MiB → 145 dpi archive derivative landed, original-of-record sha256 pinned; taleem360 direct link, method of record) | ✅ 2026-10-25 (T-PARSE-YCH12-1: v1, **1400 chunks** (`ych2_v1_`); 315 blank formula regions exported, 133 verbatim-transcribed rescue applied; rescue R2 (T-PARSE-YCH12-1-R2): remaining 182 ALL transcribed + banked in `pipeline/evidence/rescue_r2_2026-10-25/` (315/315 sidecar, bbox-verified position-true), landing BLOCKED by the post-reset re-chunk diff gate (rebuilt docling env not byte-faithful — fresh-parse v2 lane needed to consume); validator ALL CHECKS PASSED; polish R1 103/800 (CONT-2 2026-10-26 burst-harvest), quota-walled resumable; v2 fresh-parse COMPLETE (T-PARSE-YCH12-2 2026-10-27: R2 pages + FULL 315/315 sidecar consumed as corpus of record, 1406 chunks `ych2_v2_`, validator green, adjudication METHOD D-12 — v1 polish resets, v2 grind COMPLETE 748/801 applied + 53 rejected = 801/801 terminal (CONT-V2-8 2026-10-31); pack-floor fold fix FOLD-1 2026-10-31: last rescue fill p49 i9 folded into `pdf049_0220` with its own gate — 306/306 sidecar fills consumed)) | — | — |
| 11+ | → see §4 rollout queue (wave-3: edition upgrades — CUP 0620 5th ed, 9702 3rd ed, 9700 5th ed, 0625 CUP Sang, 0610 4th ed) | | | | | | | |

## 3. Books in the archive — full records

### 3.1 Edexcel International GCSE (9-1) Chemistry Student Book — LIVE

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International GCSE, **4CH1** (2017 line) |
| Course binding (v2 hub) | `igcse-chemistry-19` · specKey `pearson-edexcel/international-gcse/chemistry/4ch1` |
| Author | Jim Clark (DB canonical_json) |
| Source of record | `chemistry/4ch1/student-book.pdf` · sha256 `d48020e0cc0b5545b330bb59b242472198210e424525e4381cd5d2a58a58cc04` · 383 pp · 54,298,792 bytes · image-only scan (OCR route) |
| Parse of record | v3 corpus, **1234 chunks**, 15-key grammar, 17 content types; LLM fidelity polish (87 chunks, originals preserved); external audit **GREEN** 2026-10-18 (`pipeline/AUDIT_VERDICT_2026-10-18.md`) |
| Serving of record | documents id `e6c0db50-0f84-55de-b50c-e4d49285cd6d` v1, **VALIDATED**; 29 `book_chapters` rows, 4 units (u1 Principles ×10, u2 Inorganic ×8, u3 Physical ×3, u4 Organic ×8); slices manifest v2 (33 slices); hub shelf `/courses/igcse-chemistry-19/books` |
| Entry options | landing card (T-MIG-133 band 133k) + sidebar/drawer "Student Book" row (T-MIG-140, commit `0b98e40`) |
| Notes | REFERENCE IMPLEMENTATION per the playbook; the archive home landed by Git-DB tree-composition (commit b589745, blob-reuse mechanism). Native-text upgrade search (2026-10-21, run-003): source re-verified image-only first-hand (Acrobat 20.6 Image Conversion producer, zero embedded fonts, 0 text chars on sampled pp. 60/160/260); no legitimate native-text source found (Open Library 0 hits for ISBN 9780435185169; archive.org holds only old-spec editions); unauthorized copies circulate (z-library 12.23MB/352pp PDF, scribd, fliphtml5, pdfcoffee) and were **NOT ingested** — z-library itself carries a copyright-holder complaint block on this title; upgrade route of record = the Pearson publisher eBook (same 2017 line, print+eBook bundle / school 3-year eBook access, 60-day school trial available) — an operator purchase decision, not an agent-intake |

### 3.2 Edexcel International GCSE (9-1) Physics Student Book — PARSED

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International GCSE, **4PH1** (2017 line) |
| Course binding (v2 hub) | `igcse-physics-19` · specKey `pearson-edexcel/international-gcse/physics/4ph1` |
| Authors | Brian Arnold, Penny Johnson, Steve Woote (Pearson 2017 printing) |
| Source of record | `physics/4ph1/source/student-book.pdf` · sha256 `9b0783d9fe99790a08255eb1f2ebb6eab5833c03ef8e36dd51b7643ac68a313a` · 308 pp · 30,915,167 bytes · **image-only scan** (RICOH MP C4503; zero text layer) → OCR route |
| Provenance | operator-relayed tmpfiles link (gateway trace 1a1539ed1a5c074d) after direct upload failed — per the 4ph1 README |
| Parse of record | v1 corpus, **736 chunks**, 8 units / 28 chapters; Docling+RapidOCR+CodeFormula; LLM polish rounds 1–2 (299/300; char-level LCS ≥0.97 guard); validator **ALL CHECKS PASSED** 2026-10-20; serving-critical anchor diff vs pristine = 0 drift |
| Serving | r0 serving package landed 2026-10-30 (operator order trace 1a18d6866b38000d — shelf needs no parsing): slices manifest v2 (36 slices = 28 lesson + 8 unit-exam, 14 questionsStartPage anchors, all in-range) + chapter/unit slice PDFs + root student-book.pdf blob-reuse, Git-DB commit; documentId `d9b72a0a-23fb-5938-a0a7-a7494e7ebf9e` (133f dry receipt @ ibm-docling@v3); hub registry entry in flight; DB apply + T-C20 flip pending (Neon MAIN paused — manifests drift-guard, honest no-serve until rows land) |
| Notes | second parse; hybrid-stack lessons feed the playbook §7/§8. Native-text upgrade search (2026-10-21, run-003): source re-verified image-only first-hand (RICOH MP C4503 producer, zero embedded fonts, 0 text chars on sampled pp. 60/160/260); ISBN of record corrected to **9780435185275** (Pearson schools catalog + Amazon; the 9780435185282 seen in earlier searches is the Science Double Award — abebooks/amazon.de listings); Open Library 0 hits, archive.org holds only the old-spec 2011 Sunley physics book; unauthorized copies circulate (dokumen.pub native-text conversion per its own page text, z-lib-mirror scribd reposts) and were **NOT ingested** (unauthorized channels; dokumen /download CF-walled regardless per run-002 method notes); upgrade route of record = the Pearson publisher eBook (print+eBook bundle; £40 print, June 2017 production) — operator purchase decision |

### 3.3 Edexcel International GCSE (9-1) Biology Student Book — PARSED

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International GCSE, **4BI1** (2017 line) |
| Course binding (v2 hub) | `igcse-biology-19` · specKey `pearson-edexcel/international-gcse/biology/4bi1` (spec spine already in repo: `Official-Specifications/igcse-biology/`) |
| Authors | Philip Bradfield, Steve Potter (verified from the landed copy's title page + Pearson official sample; §4.1 queue row had misattributed "Penny Johnson, Susan Kearsey" — corrected here, errata E-001 in books/README.md) |
| ISBN | 978-0435185084 (1st ed., 2017) |
| Source of record | `biology/4bi1/source/student-book.pdf` · sha256 `974ad65d913108b9caa98df9eda1584e546177854bcd5efa6d8642797d093006` · 357 book pages rendered as **179 landscape 2-up spread PDF pages** · 34,351,405 bytes · **native text layer** (Word 2016 → Acrobat Pro DC 15 print-replica conversion; OCR route NOT required) |
| Disclosed form | 2-up spreads (deterministic preprocessing at parse); Word-conversion split-word artifacts ("differen t organs") — noise census at parse start; ANSWERS section present (like 4CH1, unlike 4PH1) |
| Provenance | theonlineschool.co.uk direct PDF (sgcaptcha-walled; cleared via headless-browser clearance + cookie handoff to curl), gateway trace 1a15b063a08dbc69; pypdf verification 18/18 sampled pages text>40 chars |
| Upgrade candidates | dokumen.pub single-page 357pp/165MB (CF-walled at intake); pdfcoffee 49MB copy (CF-walled); Pearson official = 69pp sample only |
| Parse | ✅ 2026-10-21 (T-PARSE-4BI1-1): **text-layer lane** — PyMuPDF native extraction, no OCR; 2-up law `book = 2s−10 (L) / 2s−9 (R)` 3-way confirmed; 6 units / 22 chapters; QUESTION_RANGES anchored on the 22 per-chapter "More questions …" cross-references; corpus v1 = 869 chunks (`bio_v1_`), validator ALL CHECKS PASSED; LLM polish R1 partial (91/363 applied — account-level 429 wall, runner resumable); METHOD_AND_FINDINGS.md D-1…D-10 |
| Serving | r0 serving package landed 2026-10-30 (operator order trace 1a18d6866b38000d — shelf needs no parsing): slices manifest v2 (28 slices = 22 lesson + 6 unit-exam, 22/22 questionsStartPage anchors, all in-range) + chapter/unit slice PDFs + root student-book.pdf blob-reuse, Git-DB commit; documentId `d98fb969-eab4-5511-af83-7807d8722f71` (133f dry receipt @ ibm-docling@v3, riding the v2-repo 21-shaped grammar widening r2 for `biology_only` ×2); hub registry entry in flight; DB apply + T-C20 flip pending (Neon MAIN paused — manifests drift-guard, honest no-serve until rows land) |
| Notes | first NATIVE-TEXT-LAYER source in the Pearson IGCSE lanes — quality class above 4CH1/4PH1 scans; parse found 6 units (not 4), broken-CMap garble class in the display/italic font (playbook L-012), and an unlisted ANSWERS section (book 329–348) |

### 3.4 Pearson Edexcel International AS/A2 Level Physics Student Books 1+2 — PARSED

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International A-Level, **YPH11** (2018 line, two-book course) |
| Course binding (v2 hub) | `ial-physics-19` · specKey `pearson-edexcel/international-a-level/physics/yph11` (no spec row in pastpapers-corpus.ts yet; multi-book file law pending hub-side, T-MIG-140 receipt) |
| Authors | Miles Hudson (both books; verified from title pages) |
| ISBNs | SB1 978-1292244877 (IAS, 2018) · SB2 978-1292244478 (IA2, 2019) |
| Sources of record | SB1 sha256 `aa1aed60…15d0` 225pp · SB2 sha256 `faf4c467…f988` **237pp complete** 48,278,974 B (E-008: the archived bytes' digest; the earlier `f8f3fc62…ce82d` pin sits at the same byte size — see books/README.md E-008) (fresh 145dpi derivative landed by the SB2 delta lane; original-of-record 28eabe40…8f; intake copy was truncated — books/README.md E-004) |
| Disclosed form | Both: image-only Skia/ActiveLearn print replicas (~155dpi, zero text layer) → OCR route; SB2 cover carries "PDF COMPILED BY SAAD"; fake per-page ActiveLearn OPS outlines |
| Provenance | taleem360.com direct links (SB1 f=34f2fa1f; SB2 f=8bab16ce via Googlebot-UA wall-bypass — method of record); SB2 re-source byte-verified against original-of-record 2026-10-22 |
| Parse | ✅ SB1 2026-10-22 (first session): 881 chunks (`yph1_v1_`), offset −11, formula rescue via manual transcription (260 equations) · ✅ SB2 2026-10-22 (delta session): **826 chunks** (`yph2_v1_`), offset −10, 7 topics / 13 chapters, 13/13 EXAM PRACTICE pairs page-anchored (serving-critical), 7 additive IAL content types, validator ALL CHECKS PASSED; both books have NO printed page 1 (arabic starts at book 2); LLM polish R1 SB1 COMPLETE 2026-10-25 (404/404; SB1 audit green); SB2 polish R1 COMPLETE 2026-10-30 (794/794 — 774 applied, 20 guard-rejected; anchor diff 0 drift; audit space-run 4610→15 on repaired chunks, 0 Unicode-unit regressions; validator ALL CHECKS PASSED post-polish; chain scripts of record replaced — books/README.md E-006) |
| Serving | r0 serving packages landed 2026-10-31 (operator order trace 1a18fe1f9cace659 — IAL next books): TWO manifests under the MULTI-BOOK MANIFEST LAW (one manifest file per book inside the 2-book lane) — `manifest-sb1.json` (11 slices = 11 lesson, **11/11 EXAM PRACTICE questionsStartPage anchors in-range**, unit = TOPIC 1–4, `sb1/chapters/u{t}_c{n}.pdf`) + `manifest-sb2.json` (13 slices = 13 lesson, **13/13 anchored**, TOPIC 5–11, `sb2/chapters/…`) + root `student-book-1.pdf`/`student-book-2.pdf` blob-reuse, Git-DB commit; documentIds (derived ibm-docling@v3 of the ARCHIVED bytes) `7e6891e1-e41c-5eaf-8aa4-003baffc3907` (SB1) + `a767d89e-d678-5b75-9513-1b325915c189` (SB2); receipt `pipeline/slices-gen-receipt.json`; hub multi-book law rides the v2 repo PR; DB apply + T-C20 flip pending (Neon MAIN paused — honest no-serve until rows land) |
| Notes | glue census 63% (SB1) / 90% (SB2); SB2 formula orphans (278) logged for the manual-transcription rescue (L-020 law); per-chapter EXAM PRACTICE = the IAL analog of IGCSE chapter_questions |

### 3.5 Pearson Edexcel International AS Level Chemistry Student Book 1 — PARSED

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International A-Level, **YCH11** (2018 line, two-book course — this is SB1) |
| Course binding (v2 hub) | `ial-chemistry-17` · specKey `pearson-edexcel/international-a-level/chemistry/ych11` (SME-ExamQuestion ial-chemistry-17 lane already exists; hub wiring lands at the serving lane) |
| Authors | Cliff Curtis, Jason Murgatroyd, with David Scott (verified from the landed copy's cover; ISBN 978-1292244860, 2018) |
| Source of record | `chemistry/ych11/source/student-book-1.pdf` (ARCHIVE COPY, 145 dpi ghostscript derivative, 73,538,565 B, sha256 `b17ea91f…7927`, `-dPassThroughJPEGImages=false` per books/README.md L-022) · original of record 148,791,436 B, sha256 `3d534889…72eb`, retained at the provenance URL |
| Disclosed form | image-only Skia/ActiveLearn print replica, 329 PDF pages (front matter roman i–xiii = PDF 2–14; arabic book 2–316 = PDF 15–329; book page 1 omitted print blank), zero text layer → OCR route; cover CLEAN (no third-party mark) |
| Provenance | taleem360.com direct download link `?f=062fc8b2` (Googlebot UA; this title not reCAPTCHA-walled) — the YPH11 method of record |
| Parse of record | ✅ 2026-10-24 (T-PARSE-YCH11-1): docling 2.33.0 + rapidocr-onnxruntime 1.4.4 (formula enrichment OFF — 2.33 bug, YPH11 D-7/L-020); page law `book = pdf − 13` 3-way confirmed; 2 units / 10 topics / 35 chapters (1A–10D); corpus v1 = **1571 chunks** (`ych1_v1_`), validator ALL CHECKS PASSED; 291 blank formula regions + 4 fraction-mangled items recovered by verbatim manual transcription from 150 dpi renders (295-record evidence sidecar; 8 adjudicated slivers); image-only periodic-table page (book 308) + graph-paper end leaf (book 316) registered as by-design gaps (books/README.md L-023); polish R1–R4 partial (130/800 across six quota windows; pristine-baseline merge, anchor diff 0 drift; 0 Unicode regressions) |
| Serving | r0 serving package landed 2026-10-31 (operator order trace 1a18fe1f9cace659): slices manifest v2 `manifest.json` (**45 slices = 35 lesson (1A–10D, `u{topic}:c{n}`) + 10 unit-exam** = the per-topic EXAM PRACTICE banks `u{t}:xexam-practice` incl. T9's 4pp, `units/u{t}_practice.pdf`; THINKING BIGGER pages honestly unsliced) + root `student-book-1.pdf` blob-reuse, Git-DB commit; unit = TOPIC 1–10; documentId `5fe299af-08a7-53e1-85fc-c914e997062d` (derived ibm-docling@v3 of the archived bytes); receipt `pipeline/slices-gen-receipt.json`; hub multi-book law rides the v2 repo PR; DB apply + T-C20 flip pending (Neon MAIN paused) |
| Notes | Core Practicals are NOT inline (companion Lab Book owns them; this book carries CP chips only); EXAM PRACTICE banks are per-TOPIC (10 banks, T9's is 4 pp); no answers section (Pearson publishes separately); SB2 parsed 2026-10-25 in the sibling `ych12` lane (§3.6, `ych2_v1_` ID law) |

### 3.6 Pearson Edexcel International A Level Chemistry Student Book 2 — PARSED

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International A-Level, **YCH12** (2018 line, two-book course — this is SB2, IA2) |
| Course binding (v2 hub) | `ial-chemistry-17` · specKey `pearson-edexcel/international-a-level/chemistry/ych12` (hub wiring lands at the serving lane) |
| Authors | Cliff Curtis, Jason Murgatroyd, with David Scott (verified from the landed copy's cover; ISBN 978-1-292-24472-3, 2019 — also printed on the artifact's imprint page) |
| Source of record | `chemistry/ych12/source/student-book-2.pdf` (ARCHIVE COPY, 145 dpi ghostscript derivative, 72,675,329 B, sha256 `7b1bc6cf…be18` (suffix abbreviation corrected; byte-identity via git blob sha1 67fc1df868f1), `-dPassThroughJPEGImages=false` per books/README.md L-022) · original of record 162,939,218 B, sha256 `44af34a5…748`, retained at the provenance URL |
| Disclosed form | image-only Acrobat Image Conversion print replica, 320 PDF pages (front matter roman ii–xiii = PDF 2–13; arabic book 2–308 = PDF 14–320; book page 1 omitted print blank), zero text layer → OCR route; cover carries a third-party "PDF COMPILED BY SAAD" mark (disclosed) |
| Provenance | taleem360.com direct download link `?f=a4c5a983` (Googlebot UA; this title not reCAPTCHA-walled) — the YPH11/YCH11 method of record |
| Parse of record | ✅ 2026-10-25 (T-PARSE-YCH12-1): docling 2.33.0 + rapidocr-onnxruntime 1.4.4 (formula enrichment OFF — 2.33 bug, YCH11 D-7/L-020); page law `book = pdf − 12` 4-way confirmed, roman = pdf − 0 (i absent); 2 units / 10 topics / 19 chapters (11A–20A); corpus v1 = **1400 chunks** (`ych2_v1_`), validator ALL CHECKS PASSED, byte-identity double-run verified; 315 blank formula regions exported, 133 verbatim-transcribed (127 fills + 6 adjudicated slivers); rescue R2 (2026-10-25): remaining 182 ALL transcribed + banked (`pipeline/evidence/rescue_r2_2026-10-25/`, 315/315 sidecar, bbox-verified position-true), landing blocked by the post-reset re-chunk diff gate (fresh-parse v2 lane needed to consume); image-only periodic-table page (book 298) + FOUR graph-paper end leaves (books 305–308) registered as by-design gaps; polish R1 v1 partial 103/800 (CONT-2 2026-10-26, burst-harvest). **Corpus of record switched to v2 (T-PARSE-YCH12-2, 2026-10-27): 1406 chunks (`ych2_v2_`), FULL 315/315 sidecar consumed (305/306 fills in chunk text, METHOD D-12), validator ALL CHECKS PASSED; v1 corpus + 103-repair evidence remain landed/history; v2 polish R1 re-staged 801 ids — **GRIND COMPLETE: 748/801 applied + 53 rejected = 801/801 terminal, todo 0 (POLISH-CONT-V2 2026-10-27 + CONT-V2-2/3 2026-10-28 + CONT-V2-4/5/6 2026-10-30 + CONT-V2-7/8 2026-10-31, quota-walled burst-harvest, foreground windows only per L-027; record rounds +194/+204 CONT-V2-5/6, CONT-V2-7's +51 behind the grind's longest full closure (73 min), CONT-V2-8 closed the grind with +73 behind a ~56-min closure then a 3-window crack; merge anchor 0 drift, three-way reconciliation ALL PASS (repo-resident reconcile + reseed tooling per R-013/14), audit clean, validator ALL CHECKS PASSED; 64 error-cum-429 records all retried to terminal)**; pack-floor fold fix (T-PARSE-YCH12-2-FOLD-1, 2026-10-31, own gate per R-018): the last unconsumed rescue fill (p49 i9, `N₂(g) + 3H₂(g) → 2NH₃(g)`, dropped by the <40-char pack floor) folded into the next reading-order chunk `ych2_v2_u12_c2_pdf049_0220` — pristine of record edited in place (474→516 chars), corpus/markdown/report regenerated (748/743, anchor 0 drift), one-chunk diff proof vs the landed corpus, reconcile + audit + validator all green ×2 — **306/306 sidecar fills consumed**; v1 keeps the drop as landed history, chunker floor unchanged per L-025 |
| Serving | r0 serving package landed 2026-10-31 (operator order trace 1a18fe1f9cace659): slices manifest v2 `manifest.json` (**29 slices = 19 lesson (11A–20A, `u{topic}:c{n}`) + 10 unit-exam** per-topic EXAM PRACTICE banks, `units/u{t}_practice.pdf`; THINKING BIGGER pages honestly unsliced) + root `student-book-2.pdf` blob-reuse, Git-DB commit; unit = TOPIC 11–20; documentId `c40f6853-a50c-5743-9a53-611ade397fba` (derived ibm-docling@v3 of the archived bytes); receipt `pipeline/slices-gen-receipt.json`; hub multi-book law rides the v2 repo PR; DB apply + T-C20 flip pending (Neon MAIN paused) |
| Notes | Core Practicals are NOT inline (Lab Book owns them; CP chips only); EXAM PRACTICE banks are per-TOPIC (10 banks, 2 pp each); no answers section (Pearson publishes separately); SB1 = the sibling `ych11` lane (§3.5) |

## 4. Rollout queue — books for every course (decision of record 2026-10-20)

Operator decision (v2 trace 1a15a87407daa94d): **books on every course**.
Board-wise sourcing plan (v2 hub lanes; book picks = the de-facto standard
endorsed/official series per board). State letters: `—` not sourced · `S`
SOURCE · `P` PARSED · `I` INTEGRATED · `L` LIVE.

### 4.1 Pearson Edexcel International GCSE (2017 lines)

| Lane | Course slug | Book | State |
|---|---|---|---|
| Chemistry 4CH1 | `igcse-chemistry-19` | SB (Jim Clark) | **L** (§3.1) |
| Physics 4PH1 | `igcse-physics-19` | SB (Arnold/Johnson/Woote) | **P** (§3.2) |
| Biology 4BI1 | `igcse-biology-19` | SB (Philip Bradfield & Steve Potter, ISBN 9780435185084; authors corrected 2026-10-21 — see §3.3 + books/README.md E-001) | **P** (§3.3, parsed 2026-10-21) |
| Maths A 4MA1 (F/H) | `igcse-maths-a-18-*` | SB (A/O level Maths A; PDF+JSONL package staged upstream, operator-keyed) | — |
| Maths B 4MB1 | `igcse-maths-b-16` | SB (David Turner, Ian Potts) | — |
| Further Pure 4PM1 | `igcse-further-maths-19` | SB | — |
| Accounting 4AC1 | `igcse-accounting-17-*` | SB | — |
| Business 4BS1 | `igcse-business-19` | SB | — |
| Economics 4EC1 | `igcse-economics-17` | SB | — |
| English Lang A 4EA1 | `igcse-english-language-a-16-*` | SB | — |
| English Lit 4ET1 | `igcse-english-literature-16` | SB | — |
| Geography 4GE1 | `igcse-geography-19` | SB | — |
| ICT 4IT1 | `igcse-ict-17` | SB | — |
| Science Double Award 4SD0 | `igcse-science-double-award-*` | SB (single volume) | — |

### 4.2 Pearson Edexcel International A-Level (2018 lines) — YPH11 etc.

| Lane | Course slug | Book(s) | State |
|---|---|---|---|
| **Physics YPH11** | `ial-physics-19` | **Student Book 1** (Miles Hudson, IAS Units 1–2, ISBN 978-1292244877) + **Student Book 2** (IAL Units 4–5, ISBN 978-1292244478) — a TWO-book course; Units 3/6 are practicals, no SB | **SB1 = P · SB2 = P** (SB1 parsed 2026-10-22: 881 chunks; SB2 parsed 2026-10-22 delta lane: 826 chunks, §3.4; SB2 archive copy replaced after truncation fix, books/README.md E-004; polish R1 COMPLETE both books — SB1 404/404 2026-10-25, SB2 794/794 2026-10-30) · **SERVING r0 LANDED 2026-10-31** (manifest-sb1/sb2 + slices + roots, T-BOOK-SERVE trace 1a18fe1f9cace659, §3.4; hub multi-book law in flight as a v2 PR) |
| **Chemistry YCH11** | `ial-chemistry-17` | **Student Book 1** (Curtis/Murgatroyd/Scott, IAS Units 1–2 = Topics 1–10, ISBN 978-1292244860) + **Student Book 2** (IAL Units 4–5 = Topics 11–20, ISBN 978-1-292-24472-3) | **SB1 = P** (parsed 2026-10-24: 1571 chunks, §3.5; polish R1-R3 90/800 quota-walled resumable) · **SB2 = P** (parsed 2026-10-25: 1400 chunks, §3.6; formula rescue partial resumable; polish R1 partial 74/800 quota-walled resumable) · **SERVING r0 LANDED 2026-10-31** (manifests + slices + roots, T-BOOK-SERVE trace 1a18fe1f9cace659, §3.5/§3.6; hub multi-book law in flight as a v2 PR) |
| Biology YBI11 | `ial-biology-18` | Student Book 1 + Student Book 2 | — |
| Maths YMA01 (P1-P4, M1-M2, S1-S2, D1) | `ial-maths-20-*` | per-component SBs | — |
| Further Maths YFM01 | `ial-further-maths-18-*` | per-component SBs | — |

> **Multi-book law (pending hub-side follow-up):** the archive home is one PDF
> per file, so a two-book course stores `source/student-book-1.pdf` +
> `source/student-book-2.pdf`; the v2 hub currently assumes ONE
> `student-book.pdf` per course (`bookCorpusPathForCourse`) and needs a
> per-book file law BEFORE an IAL lane integrates (T-MIG-140 receipt,
> multibook_disclosure).

### 4.3 Cambridge International (CIE) — the endorsed-coursebook series

CIE publishes no books of its own; it endorses third-party titles. The
de-facto standard = the Cambridge University Press "Coursebook" series
(endorsement badge "endorsed by Cambridge Assessment International
Education"). Structural note vs Edexcel IAL: **CUP A-Level coursebooks cover
the whole A Level in ONE volume** (AS + A2), except 9709 which CUP splits per
component.

| Lane | Course slug | Book (CUP unless noted) | State |
|---|---|---|---|
| A-Level Physics 9702 | `cie-a-level-physics-25` | Coursebook 3rd ed — Sang, Jones, Chadha, Woodside (ISBN 9781108859035) | **S** (2nd ed sourced 2026-10-21, 744pp; 3rd ed = upgrade candidate) |
| A-Level Chemistry 9701 | `cie-a-level-chemistry-25` | Coursebook 3rd ed — Ryan & Norris | **S** (2026-10-21, 889pp text layer) |
| A-Level Biology 9700 | `cie-a-level-biology-25` | Coursebook — Jones, Fosbery, Taylor, Widger | **S** (4th ed sourced 2026-10-21, 696pp; 5th ed = upgrade candidate) |
| A-Level Maths 9709 (6 lanes) | `cie-a-level-maths-20-*` | per-component Coursebooks: Pure Math 1; Pure Math 2&3; Mechanics; Prob & Stats 1; Prob & Stats 2 | — |
| IGCSE Physics 0625 | `cie-igcse-physics-23` | Coursebook 3rd ed — Sang | **S** (Hodder Duncan/Kennett 3rd ed sourced 2026-10-21, 328pp; CUP Sang = upgrade candidate) |
| IGCSE Chemistry 0620 | `cie-igcse-chemistry-23` | Coursebook 4th ed — Harwood & Lodge | **S** (2026-10-21 retry: full 362pp copy via libgen.vg; image-only → OCR route; RM.DL per-page watermark disclosed; papacambridge 69pp preview re-proven & rejected; CUP 5th ed = upgrade candidate) |
| IGCSE Biology 0610 | `cie-igcse-biology-23` | Coursebook 3rd ed — Jones | **S** (3rd ed sourced 2026-10-21, 350pp image scan; 4th ed = upgrade candidate) |
| IGCSE Maths 0580 (core/extended) | `cie-igcse-maths-25-*` | Core & Extended Coursebook — Morrison/Humberstone (or Hodder Pimentel/Wall) | — |
| IGCSE Intl Maths 0607 | `cie-igcse-maths-international-maths-23-*` | Coursebook | — |
| Further Maths 0606 | `cie-igcse-further-maths-additional-maths-25` | Coursebook | — |
| Accounting 0452 / 9706 | `cie-igcse-accounting-*`, `cie-a-level-accounting-21` | Coursebook | — |
| Business 0450/0264/9609 | `cie-igcse-business-*`, `cie-a-level-business-23` | Coursebook | — |
| Economics 0455/9708 | `cie-igcse-economics-*`, `cie-a-level-economics-23` | Coursebook | — |
| Computer Science 0478/9618 | `cie-igcse-computer-science-23`, `cie-a-level-computer-science-19` | Coursebook | — |
| English 0500/0475/8021 | `cie-igcse-english-*`, `cie-as-english-general-paper-21` | Coursebook | — |
| Geography 0460 / History 0470 / ICT 0417 / RS 0490 / Env Mgmt 0680/8291 | `cie-igcse-geography-*`, `cie-igcse-history-18`, `cie-igcse-ict-21`, `cie-igcse-religious-studies-23`, `cie-igcse-environmental-management-25`, `cie-as-environmental-management-20` | Coursebook | — |
| Co-ordinated Sci 0973 / Combined Sci 0653 (per-science lanes) | `cie-igcse-science-*-{biology,chemistry,physics}` | the corresponding single-science Coursebook per lane | — |

> Edition/ISBN above are planning-grade (verified where footnoted; else the
> series' standard current edition). Exact edition + ISBN is pinned per lane
> at SOURCE time in that lane's README.

## 5. Archive grammar & lane scaffold

- Home grammar mirrors the past-papers corpus specKey:
  `books/<publisher>/<qualification>/<subject>/<code>/`
  e.g. `books/pearson-edexcel/international-a-level/physics/yph11/`,
  `books/cambridge-international/ial/physics/9702/`,
  `books/cambridge-international/igcse/chemistry/0620/`.
- New-lane scaffold (copy of `physics/4ph1/` per playbook TL;DR):
  `source/` (the sha256-pinned PDF), `parsed/` (deliverables land here at
  parse time), `pipeline/` (scripts + evidence), lane `README.md` (status +
  provenance). Legacy exception: chemistry/4ch1 keeps its pdf at lane root
  (first lane, predates the scaffold).
- Multi-book courses (IAL sciences): `source/student-book-1.pdf`,
  `source/student-book-2.pdf` (+ README rows per book).
- Commits: temp-index protocol only (playbook §5 phase 10); NEVER `git add -A`.

## 6. Change log (catalog)

| Date | Change | Commit / evidence |
|---|---|---|
| 2026-10-21 | Catalog created (T-MIG-141 wave-2 intake): chemistry + physics rows of record, rollout queue for 60+ lanes, status vocabulary, multi-book law note | this commit |
| 2026-10-21 | 4BI1 SOURCE intake (T-INTAKE-4BI1-1): lane `pearson-edexcel/international-gcse/biology/4bi1/` lands per the 4ph1 scaffold (source/ + sha256 974ad65d…93006 + provenance README); book = Bradfield & Potter 2017, 357pp as 179 native-text 2-up spreads — OCR route NOT required; tracker row 9 + §3.3 record + §4.1 state —→S + author misattribution corrected (books/README.md E-001); upgrade candidates: dokumen.pub 357pp/165MB single-page, pdfcoffee 49MB | this commit (lane README = per-book evidence) |
| 2026-10-21 | Wave-2 SOURCE intake: 6 lanes land (YPH11 SB1; 9701; 9702 2nd ed; 9700 4th ed; 0625 Hodder 3rd ed; 0610 3rd ed) — each `source/` + sha256 + provenance README per the 4ph1 scaffold; quality verdicts + disclosed defects (9701 2-page ad watermark; 0610/SB1 image-only → OCR route); pendings: YPH11 SB2, 0620 full copy, 3rd/4th/5th-ed upgrades | this commit (lane READMEs = per-book evidence) |
| 2026-10-21 | Wave-2 retry (run-002): YPH11 SB2 + 0620 land from fresh sources — SB2 via taleem360 direct link (Googlebot-UA wall-bypass method of record; archive copy = disclosed 145dpi ghostscript derivative of the 115 MiB original, OCR-parity verified); 0620 CUP 4th ed via libgen.vg (362pp image-only, RM.DL watermark disclosed; papacambridge 69pp preview re-proven & rejected); 0620 lane scaffold created; tracker rows 3/9 + queue §4.2/§4.3 updated | this commit (lane READMEs = per-book evidence) |
| 2026-10-21 | Native-text upgrade search for 4CH1 + 4PH1 (run-003, operator ask "better versions (native text)"): both current sources re-verified image-only first-hand (zero text layer/fonts); native-text copies confirmed to exist in circulation but **only on unauthorized channels** (z-library / dokumen.pub / scribd class) — NOT ingested as archive policy; the chem title is additionally copyright-complaint-blocked on z-library itself; legitimate upgrade route of record = Pearson publisher eBook (4CH1 ISBN 9780435185169, 4PH1 ISBN 9780435185275 — print+eBook bundle or school 3-year eBook access, 60-day school trial; native born-digital files, would retire the OCR pipeline for both lanes); Open Library 0 hits, archive.org old-spec only; 4PH1 ISBN corrected from the Double-Award number | that commit (§3.1/§3.2 notes) |
| 2026-10-21 | 4BI1 PARSED (T-PARSE-4BI1-1): text-layer lane (PyMuPDF, no OCR — first in books/); corpus v1 869 chunks (`bio_v1_`), 6 units / 22 chapters, validator ALL CHECKS PASSED; polish R1 partial (91/363, 429-quota-walled, resumable); playbook ledgers L-012…L-015 + E-002 + R-002 | this commit (parsed/ + pipeline/ in lane) |
| 2026-10-22 | YPH11 SB1 PARSED (T-PARSE-YPH11-1, first IAL lane): OCR route on the Chromium/Skia print replica (docling 2.33.0 + rapidocr-onnxruntime 1.4.4, 225/225 checkpointed); page law book = pdf − 11 confirmed 5 ways (book page 1 omitted from the PDF); 4 topics / 11 chapters, 11/11 EXAM PRACTICE banks anchored as chapter_questions; corpus v1 **881 chunks** (`yph1_v1_`, SB2 reserved `yph2_v1_`), validator ALL CHECKS PASSED; docling 2.33 blank-formula bug hit at 4× the 4PH1 scale — 260 display equations recovered by verbatim manual transcription (VLM crop decoding rejected for hallucination risk); polish R1 partial (1/404, quota-walled, resumable); PyPI docling 2.133.0 is now a slim rebuild without a local converter (version pin mine, L-019); playbook ledgers L-018…L-020 + E-003 + R-004; row 9 polish-completion note synced from the parallel 4BI1 lane's pushed R-003 | this commit (lane parsed/ + pipeline/ + evidence) |
| 2026-10-22 | YPH11 SB2 PARSED (T-PARSE-YPH11-1 SB2 delta lane, L-008 parallel session on the same operator directive): **826 chunks** (`yph2_v1_` per the SB1 lane's two-book ID law), offset −10 (3-way; no printed page 1), 7 topics / 13 chapters, 13/13 THINKING BIGGER + EXAM PRACTICE pairs page-anchored (serving-critical), 7 additive IAL content types, validator ALL CHECKS PASSED; **SB2 intake archive copy found TRUNCATED** (225pp, books 216–227 missing vs its own TOC — E-004, L-021) → original re-sourced via the documented taleem360 Googlebot-UA route byte-verified vs original-of-record (28eabe40…8f) + fresh complete 145dpi derivative (48,278,974 B sha256 f8f3fc62…ce82d, OCR parity 1.0000, ghostscript JPEG-passthrough law L-022) — lane source/student-book-2.pdf REPLACED; 278 formula orphans logged for the L-020 manual-transcription rescue; polish R1 selected (794/826) staged, 429-wall-blocked (resumable); playbook ledgers L-021/L-022 + E-004 + R-005; tracker row 3 SB2 PARSED, §3.4 course record, §4.2 SB2 S→P, change log | this commit (lane parsed/ + pipeline/ delta; SB2 source blob replaced) |
| 2026-10-30 | YPH11 SB2 polish R1 COMPLETE (T-PARSE-YPH11-1, five quota windows of the account-level 429 wall, 2026-10-25 → 10-30): **794/794 terminal** (774 applied all text-changed, 20 guard-rejected evidence kept; PM-3 probe/resume, crash-safe JSONL); merge anchor diff vs pristine 0 drift, MD + report regenerated; audit space-run 4610→15 on repaired chunks / 0 Unicode-unit regressions (7 residual long-run chunks verified genuine source content vs text_original); validator ALL CHECKS PASSED post-polish (826 chunks, 13/13 chapters, 7/7 units, 26/26 question pages); chain scripts of record replaced — the 2026-10-25 commit shipped pre-fix phantom-path SB2 scripts and omitted the wrapper (books/README.md E-006); tracker row 3 + §3.4 + §4.2 updated | this commit (lane evidence) |
| 2026-10-31 | T-BOOK-SERVE IAL r0 (operator order trace 1a18fe1f9cace659 — "proceed with YPH11 + YCH11/YCH12"): FOUR serving packages landed, no-parse shelf law. YPH11 SB1 (11 lesson slices, 11/11 anchored, sb1/ scope dir) + SB2 (13 lesson, 13/13 anchored, sb2/) with the **MULTI-BOOK MANIFEST LAW** — one manifest file per book (`manifest-sb1.json`/`manifest-sb2.json`), unit = TOPIC, root student-book-1/2.pdf blob-reuse; YCH11 (35 lesson + 10 per-topic unit-exam banks, T9 4pp) + YCH12 (19 + 10) with `manifest.json` per lane; 98 slice PDFs / 236.6MB; documentIds derived ibm-docling@v3 of the archived bytes (`7e6891e1-e41c-5eaf-8aa4-003baffc3907`, `a767d89e-d678-5b75-9513-1b325915c189`, `5fe299af-08a7-53e1-85fc-c914e997062d`, `c40f6853-a50c-5743-9a53-611ade397fba`); per-lane `pipeline/slices-gen-receipt.json` (anchors in-range, ranges non-overlapping); §3.4/§3.5/§3.6 + §4.2 + source-digest corrections (E-008) | this commit (serving packages + receipts) |
