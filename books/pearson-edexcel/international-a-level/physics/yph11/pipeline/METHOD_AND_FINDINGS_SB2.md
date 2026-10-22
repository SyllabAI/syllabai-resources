# YPH11 SB2 Parse — Method, Findings & Decisions (delta lane)

**Date:** 2026-10-22 · **Parse agent:** Super Z lane (second session) · **Task ID:** T-PARSE-YPH11-1 (SB2 delta)
**SB1 of record:** `../METHOD_AND_FINDINGS.md` (parallel session, same task ID) — this doc covers the SB2 delta only and cross-references the shared findings.
**Standard:** `books/pearson-edexcel/international-gcse/PARSE_STANDARD.md` (8-point)
+ operator serving-critical directive (question typing, per-chunk dual page numbering).

## 1. Sources

- SB1: 225pp image-only Skia/PDF (Chromium-print of the Pearson ActiveLearn
  reader), one ~155dpi full-page image per page, zero text layer → OCR route.
  sha256 `aa1aed60…15d0` (matches lane README). Cover OCR: "PEARSON EDEXCEL
  INTERNATIONAL AS/A LEVEL PHYSICS STUDENT BOOK 1, MILES HUDSON" ✓.
- SB2: see §4 — the intake archive copy was truncated; parse used a fresh
  verified 145dpi derivative (48,278,974 B, sha256 `f8f3fc62…ce82d`) of the
  re-downloaded original of record (120,888,486 B, sha256 `28eabe40…8f`, 237pp).
  Identity proven: cover + imprint (ISBN 978 1 2922 4447 8) + contents.

## 2. Structure reverse-engineering (both books probed independently — L-004)

- **SB1 offset `book = pdf − 11`** (3 ways: running-header digits PDF 60→49,
  120→109, 200→189; TOC TOPIC 1 = 8 ↔ divider PDF 19; roman i–xi = PDF 2–12).
  **No printed page 1**: arabic starts at book 2 = PDF 13 (WaaP opener).
- **SB2 offset `book = pdf − 10`** (running header "SAMPLE EXAM ANSWERS 213" at
  PDF 223; TOC back-matter digits; roman i–xi = PDF 1–11). Same no-page-1 law:
  arabic starts book 2 = PDF 12. **Per-book offsets differ (11 vs 10) — probing
  each book separately was again vindicated.**
- **SB1 topics/chapters** (TOC OCR + divider/opener headers + question-pair
  census): WaaP 2–7 (unnumbered intro); TOPIC 1 MECHANICS 8–57 = 1A Motion 8,
  1B Energy 34, 1C Momentum 46; TOPIC 2 MATERIALS 58–87 = 2A Fluids 58, 2B Solid
  Material Properties 74; TOPIC 3 WAVES AND THE PARTICLE NATURE OF LIGHT 88–147
  = 3A Basic Waves 88, 3B The Behaviour of Waves 100, 3C More Wave Properties of
  Light 118, 3D Quantum Physics 130; TOPIC 4 ELECTRIC CIRCUITS 148–193 = 4A
  Electrical Quantities 148, 4B Complete Electrical Circuits 172; Maths Skills
  194–199; Preparing for Your Exams 200–201; Sample Exam Answers 202–204;
  Command Words 205–206; Glossary 207–210; Index 211–213; Picture Credits 214.
  **TOC digit garble caught:** TOC printed "TOPIC 2 38" but the real Topic 2
  divider/chapter 2A opener is book 46 — page evidence wins (4PH1 precedent).
- **SB2 topics/chapters:** TOPIC 5 FURTHER MECHANICS 2–25 (5A Further Momentum 2,
  5B Circular Motion 14); TOPIC 6 ELECTRIC AND MAGNETIC FIELDS 26–71 (6A Electric
  Fields 26, 6B Capacitors 42, 6C Electromagnetic Effects 56); TOPIC 7 NUCLEAR
  AND PARTICLE PHYSICS 72–115 (7A Probing Matter 72, 7B Particle Accelerators
  and Detectors 84, 7C The Particle Zoo 100); TOPIC 8 THERMODYNAMICS 116–131
  (8A Heat and Temperature); TOPIC 9 NUCLEAR DECAY 132–149 (9A Radioactivity);
  TOPIC 10 OSCILLATIONS 150–167 (10A); TOPIC 11 ASTROPHYSICS AND COSMOLOGY
  168–203 (11A Gravitational Fields 168, 11B Space 178); Maths Skills 204–209;
  Preparing 210–211; Sample Exam Answers 212–217; Command Words 218–219;
  Glossary 220–223; Index 224–227 (no picture-credits page).
- **IAL question architecture differs from IGCSE:** NO "Chapter/Unit Questions"
  banks. Each chapter ends with a 2-page **THINKING BIGGER** article (second
  page often a SCIENCE COMMUNICATION activity) then a 2-page **EXAM PRACTICE**
  set ("(Total for Question N = X marks)" anchors). Census found 11 (SB1) / 13
  (SB2) exact pairs → typed `thinking_bigger` + `chapter_questions`
  (serving-critical) via page ranges in EXTRA_SECTIONS — continuation pages have
  no heading, so marker-based typing alone would miss them.

## 3. Parser stack (4PH1 recipe, one new version mine)

- docling **2.33.0** + **rapidocr-onnxruntime** (docling 2.33 wants the OLD
  namespace; the `rapidocr==3.9.2` pin belongs to the 2.133 stack — both
  installed side by side), CodeFormula v1 enrichment with formula-ON → OFF
  retry ladder: **76 pages/book** needed the OFF retry (CodeFormula v1 crash
  "list index out of range"), 0 hard errors, 0 tesseract fallbacks.
- Reinstall mines (fresh workspace): pip pulled torch 2.14.1 + nvidia CUDA
  wheels → disk-full at 8.6GB free; fix = CPU-only torch from the pytorch CPU
  index + `torchvision==0.29.1+cpu` force-realign + **transformers==4.51.3**
  (4.57 removed `RTDetrImageProcessor` used by docling-ibm-models); docling
  2.33.0's `AcceleratorOptions` imports from `pipeline_options` (not a separate
  module as the 4PH1 script had it — import fixed in the SB1 copy).
- Index pages (dense multi-column) take 60–325 s/page vs 9–13 s/page body —
  batch windows sized accordingly; per-page checkpoints made every timeout
  survivable.

## 4. SB2 archive-copy truncation (intake defect, fixed in this task)

The landed archive copy (41,870,983 B, sha256 `449dc3f3…`, per lane README) is
**225pp, truncated**: its own TOC promises INDEX at book 224 but the file ends
at book 215 (mid-SAMPLE-EXAM-ANSWERS); missing ≈ books 216–227 (sample-answers
tail, command words, glossary, index). All Topics 5–11 content was present, so
the defect is silent unless probed. Fix of record: re-downloaded the original
via the documented taleem360 Googlebot-UA route — byte-size AND sha256 match
the README's original-of-record exactly (237pp) — then derived a fresh archive
copy (145dpi bicubic DCTEncode, `-dPassThroughJPEGImages=false` is REQUIRED —
without it pdfwrite passes the source JPEGs through untouched and stays >100MiB)
= 48,278,974 B, sha256 `f8f3fc62…ce82d`, OCR parity 1.0000 (contents page,
284/284 chars). Lane source file replaced in this task's commit; README
derivation note updated.

## 5. Chunking & validation

- `book_structure_ial_physics{,_sb2}.py` + `parse_docling_ial_physics{,_sb2}.py`
  — audited 4PH1 architecture; additive content types for IAL features:
  `thinking_bigger`, `learning_tip`, `subject_vocabulary`, `checkpoint`,
  `physics_in_detail`, `science_communication`, `sample_answers` (7 new,
  PARSE_STANDARD point 6). EXAM PRACTICE → `chapter_questions`.
- New chunker guard: markers only re-type `body` pages — front matter DESCRIBES
  the book's features ("Exam practice" on the about-pages) and was falsely
  question-typed until the base-type-wins fix.
- SB1: 875 chunks, 20 types; SB2: 826 chunks, 18 types. 0 over hard max;
  validators **ALL CHECKS PASSED** (incl. strict offset law on every numbered
  chunk + question anchoring on all 22/26 expected pages, stray-page check).

## 6. LLM polish round 1 (staged, quota-blocked)

Glue-run census: 79% (SB1) / 90% (SB2) of chunks carry 12+ char lowercase runs
(Skia print replica drops spaces worse than the RICOH 4PH1 scan's 62%).
Selected 798/875 + 794/826 (chapter_questions forced + glue-scored). Runner =
4PH1 hardened design (0.97 whitespace-stripped char-LCS guard — the calibration
class matches this damage exactly per L-015, resumable JSONL, 120s timeouts,
429 backoff/quota-stop). Account-level 429 wall (active since 2026-10-20, also
holding 4BI1's pending 272) blocked all processing this session: 0/1592.
Everything staged for resume (see parsed/README.md).

## 7. Decision log

| # | Decision | Rationale |
|---|---|---|
| 1 | OCR route both books | zero text layer (verified per sampled page) |
| 2 | docling 2.33.0 + rapidocr-onnxruntime base | pinned fast stack (9–13 s/page body) |
| 3 | Formula-ON→OFF retry ladder, no 2.133 splices | 4PH1 precedent; equations survive as plain text; 76 crash pages/book recovered by retry |
| 4 | Per-book structure modules + chunker copies | offsets/units/chapters differ (L-004); per-book copies keep diffs meaningful |
| 5 | Question + TB typing via EXTRA page ranges | continuation pages carry no headings; serving-critical anchoring must not depend on markers |
| 6 | Markers never re-type non-body pages | front matter describes features (false EXAM PRACTICE on about-page) |
| 7 | 7 additive IAL content types | truthful typing of IAL feature boxes; RAG filter surface |
| 8 | SB2 re-source + fresh derivative | archive copy truncated; method of record worked; parity verified |
| 9 | unit_no = book topic number (5–11 for SB2) | keeps the book's own numbering; additive key semantics unchanged |
| 10 | Ship v1 with polish R1 pending (4BI1 precedent) | corpus is valid + serving-ready; polish is resumable, quota-gated |
