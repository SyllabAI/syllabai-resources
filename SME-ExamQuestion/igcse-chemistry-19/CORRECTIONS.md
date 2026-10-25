# Corrections Record — SME-ExamQuestion/igcse-chemistry-19

**Wave:** T-SME-13 (corrective wave against the SME corpus)
**Date:** 2026-10-25
**Source of findings:** 1:1 comparison of `SME-ExamQuestion` vs
`Official-ExamQuestion/igcse-chemistry-19` (4CH1), SME-bank-scoped — 1,404 SME
parts audited, 441 mapped to official counterparts, 12 hard discrepancies
adjudicated (comparison order trace `1a16ebc4279576d5`; corrective-wave
operator go-ahead trace `1a16f2b1cc9689d5`).

## Doctrine

Fix-and-disclose (ADR-039 principle, applied by analogy to the licensed SME
corpus): graded/serving values are corrected to the mark scheme of record and
every change is disclosed here. The official corpus itself required **zero**
edits — 434/438 marks, 11/11 MCQ keys and stems at verbatim level already
agreed before this wave; every discrepancy adjudicated was SME-side.

## Method (evidence chain)

1. Findings originate from a deterministic 1:1 comparison (stem similarity,
   marks equality, MCQ-key equality at mapped coordinates) with manual
   adjudication of all 12 hard flags by reading both sides.
2. Every correction below was re-verified against the official corpus
   (`Official-ExamQuestion/igcse-chemistry-19`, schema `/0.2`, converter
   v0.15.0, gated PASS) immediately before this wave:
   - **overstatements**: official part marks confirmed at the same question
     (incl. sub-part sums, e.g. 2(c)(i)=3 + 2(c)(ii)=1);
   - **label drifts**: marks confirmed equal at the TRUE home and different at
     the labeled home in all 9 cases (drift independently confirmed).
3. Edits applied surgically with exactly-once assertions across all three
   surfaces per topic (`topic.json`, `questions.md`, `mark-schemes.md`) plus
   `manifest.json`; totals invariant `question.total_marks == sum(part marks)`
   holds after the wave.

## A. Marks overstatements (3) — graded values corrected to MS of record

| # | Part (SME id) | Topic | Label | SME marks | Official | Evidence |
|---|---|---|---|---|---|---|
| 1 | `qstnprt_gwPsCgCxxhdbxTWW` | 1-1-states-of-matter | 2021 · Ja1C 3(b) | 3 | **2** | 2021-01 4CH1-1C Q3(b) = 2, "links any two of" 3 candidate points |
| 2 | `qstnprt_G5QRwZ2VcmQcvrJT` | 1-7-covalent-bonding | 2020 · Nov1C 5(a) | 3 | **2** | 2020-11 4CH1-1C Q5(a) = 2, "Any two from" M1–M3 |
| 3 | `qstnprt_SrgvJncYpDKY4zGg` | 1-2-elements-compounds-and-mixtures | 2020 · Nov2C 2(c) | 5 | **4** | 2020-11 4CH1-2C Q2(c) = 4 = (c)(i) 3 + (c)(ii) 1; SME's second (ii) point is the ORA alternative of a single mark point |

Each fix also lowered the parent `question.total_marks` by the same delta
(8→7, 13→12, 8→7), the `[Total: N marks]` display line in the model answer,
the part/question headings in `questions.md` / `mark-schemes.md`, the
per-topic header total in `questions.md`, and `manifest.json` totals.

## B. Label drifts (9) — provenance repointed to the verified true home

Content and marks were already correct in all 9 cases; only the
`source_paper` coordinates were wrong. Drift independently confirmed: at
every labeled home the official marks differ from the part.

| # | Part (SME id) | Topic | Labeled | Corrected to | Evidence (true home = marks match) |
|---|---|---|---|---|---|
| 4 | `qstnprt_YpGnM8cQVDrvMxD9` | 3-1-energetics | 2020 Ja1C 9(c) | **9(b)** | 2020-01 1C Q9(b) = 3 (labeled 9(c) holds 6 marks of other content) |
| 5 | `qstnprt_k8XQpNtgrKMbhfbY` | 4-2-crude-oil | 2022 Ja2CR 2(b) | **2(a)** | 2022-01 2CR Q2(a) = 3 (labeled 2(b) holds 1 mark) |
| 6 | `qstnprt_jxnCVsW9kcPtTz78` | 2-8-chemical-tests | 2020 Nov1CR 5(b) | **6(b)** | 2020-11 1CR Q6(b) = 3 (labeled 5(b) holds 4) |
| 7 | `qstnprt_Hb7HQ6hx9RzTJdKG` | 2-8-chemical-tests | 2020 Nov1CR 5(c) | **6(c)** | 2020-11 1CR Q6(c) = 6 (labeled 5(c) holds 5) |
| 8 | `qstnprt_NnZQGbrDpc9w5pmX` | 1-7-covalent-bonding | 2020 Nov1CR 8(a) | **9(a)** | 2020-11 1CR Q9(a) = 2 (labeled 8(a) holds 3) |
| 9 | `qstnprt_S7rWtWzB4K3cMjsY` | 1-7-covalent-bonding | 2020 Nov1CR 8(b) | **9(b)** | 2020-11 1CR Q9(b) = 2 (labeled 8(b) holds 3) |
| 10 | `qstnprt_n6dC6hYphQhNJNMt` | 1-7-covalent-bonding | 2020 Nov1CR 8(c) | **9(c)** | 2020-11 1CR Q9(c) = 7 (labeled 8(c) holds 4) |
| 11 | `qstnprt_4R9mWn65dN7Sg7zH` | 4-8-synthetic-polymers | 2019 Ju1CR 5(b) | **6(b)** | 2019-06 1CR Q6(b) = 5 (labeled 5(b) holds 2) |
| 12 | `qstnprt_vnds4rhZ4kxXzB4g` | 1-3-atomic-structure | 2020 Ja2C 1(b) | **2021 Ja2C 1(b)** | 2021-01 2C Q1(b) = 2 (sibling 1(a) already 2021; 2020-01 2C Q1(b) holds 1 mark) |

Side benefit: two previously duplicated part labels become unique and correct
(two parts labeled 9(c) → 9(b)+9(c); two labeled 2(b) → 2(a)+2(b)).

## Deliberately NOT changed

- **Per-point `[1 mark]` annotations inside model answers** of the three
  overstatement parts: these are SME's point-listing style (candidate points /
  ORA alternatives), not award totals — e.g. the two corrected "any two from"
  schemes legitimately list three annotated points for a 2-mark award. Graded
  totals (`marks`, `total_marks`, `[Total: …]`, headings) are what this wave
  corroborates.
- **Question/problem text, choices, solutions, spec codes, difficulty** — all
  verified faithful in the comparison.
- **The 963 SME parts without a resolvable official counterpart** (636 without
  source provenance, 324 pointing outside the held 4CH1 universe) — nothing to
  correct against; out of scope by the comparison's SME-bank-scoped mandate.
- **3 unlocatable references** (2021-01 1CR srcQ=None; Nov-2021 1CR R-paper not
  in official holdings; 2021-06 1C srcQ=55) — recorded honestly in the
  comparison workbook, not editable by label correction.

## Regeneration warning

These topic files are scrape artifacts (`schema syllabai.sme-exam-questions/1.1`,
scrapers `scripts/sme_examq_scrape.py` / `sme_examq_setpage_scrape.py`). If a
topic is ever **re-scraped from upstream SME**, upstream will reintroduce the
overstated marks and drifted labels — re-apply this ledger (or re-run the 1:1
comparison) after any re-scrape.

This warning is pinned operationally at: the lane `README.md`, and the scraper
`scripts/sme_examq_scrape.py` (docstring + per-run stderr banner + generated-
README template), so the notice survives regeneration (T-SME-13 pin wave).

## Totals impact

| Surface | Before | After |
|---|---|---|
| Course `manifest.json` totals.marks | 3708 | **3705** |
| 1-1-states-of-matter total_marks | 120 | 119 |
| 1-2-elements-compounds-and-mixtures total_marks | 187 | 186 |
| 1-7-covalent-bonding total_marks | 136 | 135 |

Per-part and per-question detail: `scripts/t_sme_13_receipt.json` in the
session workspace; comparison workbook `sme-vs-official-4ch1-1to1.xlsx`.
