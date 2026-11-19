# W-F9-T1 design of record — books rollout queue: the CIE text-layer quartet

- Order: operator message "Proceed with books rollout queueu" (trace
  1a1f4951330253b5, 2026-11-20).
- Design authority: W-F4-T1 schema authority + W-F7 M-1..M-11 (join lanes) are
  NOT in scope here; the governing instruments for this lane are
  `books/README.md` (the parse playbook, golden rules 1-11) +
  `books/pearson-edexcel/international-gcse/PARSE_STANDARD.md` (the 8-point
  gate) + `books/CATALOG.md` (the registry of record + its update law) +
  the W-F7-T1 §7 law "operator purchases — never agent-fetches".

## 1. Queue triage (§1 of the task file)

The queue's lanes partition by blockage law. The honest next-actionable set =
the four SOURCE-state books with a native text layer:

| lane | book | pages | source class | action this wave |
|---|---|---|---|---|
| cambridge-international/ial/chemistry/9701 | CUP Chemistry Coursebook 3rd ed | 889 | regenerated single-column re-layout | RECONCILE — corpus landed earlier, catalog/README unsynced; re-validate of record |
| cambridge-international/ial/physics/9702 | CUP Physics Coursebook 2nd ed | 744 | born-digital 2-col print replica | PARSE v1 |
| cambridge-international/ial/biology/9700 | CUP Biology Coursebook 4th ed | 696 | born-digital 2-col print replica | PARSE v1 |
| cambridge-international/igcse/physics/0625 | Hodder IGCSE Physics 3rd ed | 328 | PDFium re-render, irregular 2-band grid | PARSE v1 |

Honest non-actions of record: 0610/0620 (OCR route, quota-walled); all `—`
lanes (operator purchases — never agent-fetches); serving states (v2-repo lever).

## 2. Probes of record (evidence cache/w-f9/, zero repo writes)

- probe-*.json (text-layer coverage 99.6/99.7/98.8%, TOC pages, running
  headers, font-size histograms, marker censuses);
- probe2-structure.txt (TOC dumps, opener candidates, offset censuses, special
  sections by display headings);
- probe3-display.txt (full display-heading scans — the section maps of record);
- probe4 (marker census + damage census);
- raw-span gutter probes (9702 pdf 17/22; 9700 pdf 41; 0625 pdf 16/27/33/120)
  — established the column laws;
- wf9_col_census (post-merge interleave census — undercounts; superseded by
  the raw-span law).

Laws pinned by the probes:

- **Offsets**: 9702 book=pdf−12 (4 ways), 9700 pdf−10 (4 ways), 0625 pdf−13
  (5 ways, incl. the Section-1 divider and two TOC-anchored banks).
- **Columns**: 9702/9700 = true two-column bodies (QUESTION sidebars swap
  sides in 9702); 0625 = irregular two-band grid → fixed gutter x=307.
  Multi-column index pages = justified non-body exceptions (the 9701 precedent).
- **Structure maps**: 32/19/50 chapter openers probed page-by-page (LEARNING
  OUTCOMES pages for CUP; 26pt title + 35pt number for Hodder); tiling
  assertions over 1..N.
- **0625 opener anatomy**: head (≥20pt title+number) → at-a-glance box (9pt
  bullets; glyph variants 'l' and single '●') → body; the box→body transition
  block flushes the box (contamination law).
- **Damage**: 0625 fi/fl ligature loss (488 glue occurrences) — v1-unrepaired
  damage class of record; CUP books carry the milder span-join glue class.

## 3. Schema authority

13-key v1 grammar exactly as landed for 4BI1/YPH11/9701 (id, book_title,
author, unit_no, unit_name, chapter_no, chapter_title, section, content_type,
book_pages, pdf_pages, text, char_count). 0625 adds the unit law (the 5 printed
section dividers = units; ID grammar `u<unit|0>`); 9702/9700 keep unit fields
null (no printed units). New content types are additive only
(answers_saqs/answers_eoc/answers_eocq/exam_advice/recommended_resources/
revision_bank/exam_bank/mathematics/investigations/practical_test_bank/
alt_practical_bank/questions/divider per book).

## 4. Gates of record (G-F9-B1..B6)

B1 source pins match the lane READMEs (sha256); B2 structure maps tile 1..N
(zero gaps/overlaps, asserted in code); B3 corpora pass their validators (the
8-point gate); B4 determinism (corpus regeneration byte-identical, sha256
re-run); B5 surface confinement (books/** + records; zero spec-side/census/
graph writes); B6 CATALOG update law (rows advance in the same commit as the
state change).

## 5. Definition of done

- Three PARSED v1 corpora + textlayers + reports + parsed READMEs + pristine
  snapshots + per-book pipeline scripts landed; CATALOG rows 4/5/6/7 → PARSED
  with the change-log row; four lane READMEs updated; task file + T1/T2
  receipts filed; W-F8 push-confirm ride-alongs land append-only; LEDGER Waves
  53-54 appended. Build commit (books/**) then records commit; push by
  separate operator order.
