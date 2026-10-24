# YCH11 SB1 — Method & Findings (T-PARSE-YCH11-1, 2026-10-24)

Second IAL lane, first chemistry IAL book; executed end-to-end against the
playbook (`books/README.md` §5 phases 0–10) with the YPH11 SB1 lane as the IAL
exemplar. Route: OCR (image-only Skia/ActiveLearn print replica) via the proven
docling 2.33.0 + rapidocr-onnxruntime 1.4.4 stack, with the L-020 manual
transcription remedy carrying the display equations.

## Decision log

- **D-1 — directive of record.** Operator order "Parse YCH11 IAL chem according
  to the instructions" (zai-web, gateway trace 1a16ac2fe536fbe5; continuation
  "Continue, why did you stop", trace 1a16cce8bdfb15e5). CATALOG had no IAL
  chemistry row; the fresh-fetch discipline (the 6dc1f0a2 revert lesson) was
  applied FIRST: origin/main re-fetched, live `books/` tree inspected, no YCH11
  lane and no YCH11 source existed anywhere on the remote before this task.
- **D-2 — source of record.** taleem360.com listing page served a direct link
  (`?f=062fc8b2`, 148,791,436 bytes) to a Googlebot UA without a reCAPTCHA wall
  (the YPH11 method of record; this title was NOT walled). sha256
  `3d534889…72eb` pinned as original of record. Authors verified from the cover
  render (Cliff Curtis, Jason Murgatroyd, with David Scott) per E-001
  discipline — the dokumen.pub listing agreed (ISBN 9781292244860).
- **D-3 — archive copy (L-022 law).** Original exceeds GitHub's 100 MiB limit;
  ghostscript pdfwrite derivative at 145 dpi Bicubic with
  `-dPassThroughJPEGImages=false` landed as `source/student-book-1.pdf`
  (73,538,565 B, sha256 `b17ea91f…7927`). Verification: 329/329 pages,
  geometry parity, contents-page pixel MAE 1.17/255.
- **D-4 — page law.** `book = pdf − 13` confirmed 3 ways: roman headers
  (`roman = pdf − 1`, i–xiii = PDF 2–14); TOC cross-checks (TOPIC 1 = book 2 →
  PDF 15, 1A = book 4 → PDF 17); printed header digits (PDF 40 prints "27";
  INDEX prints "309" on PDF 322 and "311" on PDF 324). Book page 1 does not
  exist (print blank omitted; arabic starts book 2 = PDF 15) — same law class
  as both YPH11 books. L-021 completeness check: the file's TOC promises
  (INDEX 309) are present, so the copy is COMPLETE (dokumen's "328 pages"
  listing was off by one; the file has 329).
- **D-5 — structure map.** 2 units / 10 topics / 35 lettered chapters
  (1A–10D) — nearly 3× the YPH11 chapter count (11). Per-topic THINKING
  BIGGER (2 pp) + EXAM PRACTICE (2 pp; Topic 9's is 4 pp) banks = 10+10
  anchored page pairs. Back matter: MATHS SKILLS 290, PREPARING 296, COMMAND
  WORDS 302, GLOSSARY 304, PERIODIC TABLE 308, INDEX 309–315, graph-paper end
  leaf 316. NO answers section (Pearson publishes answers separately, as with
  the YPH11 books). `book_structure_ych11.boundary_coherence()` asserts the
  arabic map tiles book 2..316 exactly — ran clean before chunking.
- **D-6 — marker census (production-side, L-013 discipline).** All Curtis/
  Murgatroyd/Scott families mapped incl. merged OCR forms
  (LEARNINGOBJECTIVES 95, LEARNINGTIP 90, SUBJECTVOCABULARY 77, CHECKPOINT
  101, DIDYOUKNOW 37, WORKEDEXAMPLE, EXAMPRACTICE, THINKINGBIGGER,
  MATHSSKILLSFORTHISTOPIC, CHEMISTRYINDETAIL, SCIENCECOMMUNICATION,
  ADDITIONALREADING). Glue damage scan-wide: 321/329 pages carry long runs
  (8,566 total) → LLM polish round mandatory in the plan (L-005).
- **D-7 — formula enrichment OFF (documented deviation from the literal
  ladder).** The playbook's formula-ON→OFF ladder is dead code on docling
  2.33.0: the 2.33 CodeFormula integration emits EMPTY formula text either way
  (YPH11 D-7), and 2.133.0 is uninstallable (L-019). Base corpus ran with
  `do_formula_enrichment=False` — the layout model still labels formula
  regions, so the orphan census is complete, and the lane saves the 611 MB
  CodeFormula download plus ~2× runtime. Result identical in kind to YPH11:
  291 empty formula items on 100 pages (vs 267/272 there); 26 nonempty but
  fraction-mangled ("n(CuCO3)= 5.78 0.0468mol 123.5").
- **D-8 — formula rescue (L-020 remedy of record).** 100 affected pages
  rendered at 150 dpi; every orphan transcribed VERBATIM from the renders by
  the agent (zero hallucination, zero auto-decoder), with bbox + prev/next
  context alignment; 4 fraction-mangled nonempty items replaced in the same
  pass; 8 regions adjudicated as region-split slivers/overlapping duplicates
  (content carried by sibling items), left empty and marked
  `rescue_adjudicated`. Sidecar: `pipeline/evidence/manual_formulas_ych11.jsonl`
  (295 records); applier `manual_formula_ws_ych11.py` (idempotent,
  position-verified, 0 mismatches). Post-rescue census: 309 nonempty / 8
  adjudicated-empty formula items; chunker converted 309/309.
- **D-9 — EP-bank typing.** The EXAM PRACTICE banks are PER TOPIC here (10
  banks, not per-chapter as in YPH11). Typed `chapter_questions` with
  `chapter_no: None` per the YPH11 EP precedent — the serving-critical law is
  the exact-page question anchoring (validator: 10/10 banks), not the owner
  granularity. Documented in parsed/README.md.
- **D-10 — image-only end matter.** Periodic table (book 308) and graph-paper
  end leaf (book 316) are single-picture pages with no extractable text —
  recorded in `parse_report.by_design_gaps` and validated there, not chunked.
  Index (309–315) parses as TableFormer tables → `table_data` (the 4PH1/YPH11
  precedent), validator checks page coverage 322–328.
- **D-11 — two-book ID law.** `ych1_v1_u<unit|0>_c<chapter|0>_pdf<pdf:03d>_
  <block:04d>`; SB2 (YCH12 book) will use `ych2_v1_` per the YPH11 D-8 law.
- **D-12 — polish R1 partial, shipped resumable (PM-3 disposition).** Glue
  census → 800 chunks selected (all 59 question chunks force-included);
  runner staged (z-ai SDK, 0.97 whitespace-LCS, line-strict retry, pipe
  discipline, quota-stop). Two quota windows harvested 48 OK / 4 rejected
  (guards kept originals) / 2 error records (self-healing) before the
  account-level wall re-closed; merge applied 48/800 with `text_original`
  preserved, anchor diff vs pristine **0 drift**, post-polish audit clean
  (glue 459→5 on changed chunks; the 5 survivors are real long chemistry
  words — trifluoromethanesulfonate, disproportionation, etc.; 0 Unicode
  regressions). Re-validated ALL CHECKS PASSED. Same shipped-partial
  disposition as R-002/R-004/R-005; resume: `node llm_repair_ych11.js` →
  `merge_llm_ych11.py` → `audit_polish_ych11.py` → `validate_ych11.py`.

## Findings

- Scan class: space-drop glue scan-wide (321/329 pages), same Chromium/Skia
  print-replica class as the YPH11 books; ~10 s/page average on this book
  (329 pp in ~55 min across 14 foreground windows; index tail 322–327 ran
  70–305 s/page — TableFormer on the 3-column index, exactly as forecast).
- Peak RSS 2.55 GB (4 GB workspace, comfortable; ≤30-page windows kept).
- Chemistry-specific equation classes survived via the rescue pass: balanced
  equations with state symbols, ionic half-equations, ⇌ equilibria, ΔH
  notation, dot-and-cross fission notation (transcribed with ✗/● and ⟶),
  fraction-flattened molarity/moles lines restored as `a ÷ b` forms.
- The book's Core Practicals are NOT inline — they live in the companion Lab
  Book; this book carries only SPEC REFERENCE chips (CP1–CP7). No `practical`
  chunks exist, correctly.
- ACTIVITY boxes are the SCIENCE COMMUNICATION activities inside the
  per-topic THINKING BIGGER pages — typed `thinking_bigger` by the page-role
  law, not a separate type (9 heading hits, all on TB pages).

## Environment of record (2026-10-24)

python 3.12.15 venv; torch 2.14.1+cpu; torchvision 0.29.1+cpu (CPU index
first, L-018 order); docling 2.33.0 (docling-core 2.104.0 — drifted from the
YPH11 lane's 2.103.1, import surface verified per L-019;
docling-ibm-models 3.15.0, docling-parse 4.7.3); rapidocr-onnxruntime 1.4.4;
onnxruntime 1.31.0; transformers 4.57.6; artifacts `data/models` (506 MB —
layout + TableFormer only, CodeFormula skipped per D-7); ghostscript pdfwrite
for the archive derivative; node 24 for the polish runner.
