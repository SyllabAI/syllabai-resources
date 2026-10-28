# F113 — the MS-answer-figure wave (the F95/F97 MS-side crop capability)

Wave receipt of record · 2026-10-28 · converter v0.30.0 · operator order: "the F95/F97
MS-side crop capability wave". Machine receipt: `AUDIT-2026-10-28-f113-ms-answer-figures.json`.

## 1. Reconcile (before executing)

resources AGENTS.md "Known open work" read first, per the standing instruction. Three
anchors claim the wave: the F95 ledger entry ("fix needs MS-side crop support (converter
renders QP-side only today), filed as open wave"), the AGENTS.md 2019-06 3(d)(ii) bullet
("serving that answer would need an MS-figure crop capability"), and F97's leftover
(2021-01 2CR 6(c)(i) `/1000`, "a fragment-tranche item for the same MS-crop wave").
No other queue claims the capability. Two stale entries found and corrected: the 3(d)(ii)
bullet (the part already serves via the F47 transcription — C52's assertion of record)
and F97's leftover (closed en route by the F108 leg-0 denominator keep — verified served).

## 2. The capability

- Converter v0.30.0: `MS-ANSWER-FIGURES.json` (eyeball ledger, flat per-part verdicts)
  emits crop-required stubs with `source: "ms.pdf"`; the F45/F99 verdict branches render
  accepted `manual_crop` boxes FROM the MS PDF — the first MS-side render path. Fail-closed:
  malformed entries, id collisions, and slice-owned unconsumed ledger keys abort the run.
- Exporter (same wave): ms.pdf-sourced crops render in `solutionMd` after the authored
  walkthrough (`![… official mark scheme answer figure (ms.pdf p.N)]`), never in
  `problemMd`; `assets[]` carry `source: "ms"`.

## 3. The seven parts (each eyeballed twice; MS PDFs sha-verified against the corpus pins)

| part | printed MS answer | ms page |
|---|---|---|
| 2026-06 2C 5(a) | M1 ethanol + M2 ethyl ethanoate displayed formulae (embedded rasters) | 9 |
| 2019-06 2C 2(a) | the printed halogen state/colour answer table (embedded raster) | 5 |
| 2019-06 2C 6(d)(ii) | ethanoic acid displayed formula + the 1-mark guidance partial | 16 |
| 2022-01 2C 7(a)(i) | ethyl ethanoate displayed formula, ester group circled | 10 |
| 2023-01 2C 6(a)(i) | partial displayed structure, carbonyl circled | 10 |
| 2024-11 2C 7(a)(ii) | hand-drawn propan-1-ol photograph | 10 |
| 2023-06 2CR 7(c)(ii) | hand-drawn 2-methylpropanoic acid photograph (corroborates F107) | 13 |

Rects derive from document geometry (embedded-image bboxes, word positions, table rules);
the two rotated 2019-06 landscape pages map through `page.rotation_matrix` into the
rendered page space. Evidence renders: `eyeball/*.png` (full pages), `eyeball/final-*.png`
(proof clips) under the wave workbench.

## 4. Proof

- 6/6 slices exit 0, all 8 gates PASS each, at v0.30.0.
- Fresh emissions == surgical corpus edits on every target part (parsed-level); the
  converter-rendered PNGs are byte-identical to the committed PNGs (7/7 sha256).
- Residual fresh-vs-of-record deltas are exactly the F111 disclosed classes
  (2022-01 7(e) drawing-strip remains; 2024-11 1(c) exponent-restore; 2023-06 7(c)(i)
  the F107 curated state). Of-record bytes stay untouched (the F110 standing decision).
- Round-trip fidelity: all 6 of-record topic.json files re-serialize byte-identically.
- Canaries 117/117 on the edited tree (110 existing + C113–C119 new part pins).
- Census subclassification (predicate unchanged): 19 fragment-shape hits = 7 true
  printed-answer parts (served) + 12 MP-copy-with-trailing-guidance shapes (solutions
  already serve; disclosed).

## 5. Serving delta

7 changed parts, disclosed in `scripts/exporter-disclosures/2026-10-28-f113-ms-answer-figures.json`:
solutionMd gains the printed-answer figure (after the authored text); assets gain one
`source: "ms"` crop each. Census constants unchanged (54 / 477 / 2,607 / 4,161); figure
crops 471 -> 478. v2 sync ships in the same wave (the F112 convention).

## 6. Residual open

- The 12 MP-copy-with-trailing-guidance census hits (disclosed, no action).
- The F111 reconciliation classes stand (8a MCQ positional keys, 8b exponent restore,
  Task-20 drawing-strip patches) — untouched here.
- 2023-01 2C 6(a)(ii)'s printed full-ester drawing noted as a possible future MS-figure
  candidate (real MPs -> not an F95 part; NOT landed).
