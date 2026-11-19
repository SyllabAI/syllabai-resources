# books/cambridge-international/ial/biology/9700 — parsed

## Corpus

- `cie_a_level_biology_9700_chunks_v1.jsonl` — **1971 chunks** (`cie_v1_` prefix grammar
  `c9700_v1_u{unit|0}_c{chapter|0}_pdf{pdfpage:03d}_{n:04d}`), 13-key v1 grammar
  (same schema as 4BI1/YPH11/9701 v1).
- `cie_a_level_biology_9700_chunks_v1.pristine` — byte-identical snapshot
  (merge-diff + anchor law reference for the future polish lane).
- `full_book_textlayer.md` — rendered book.
- `parse_report_v1.json` — provenance, decisions D-1…, census, damage census.

## Book facts

- Cambridge International AS and A Level Biology Coursebook (4th edition) — Mary Jones, Richard Fosbery, Jennifer Gregory, Dennis Taylor (CIE 9700 (2016 syllabus line)).
- Source: born-digital print replica (Adobe InDesign CC -> 3-Heights PDF Producer 4.4.22.0); two-column body (equal columns); openers/EOC/answers single-column.
- Page law: book = pdf - 10 (verified 4 ways: ch1 pdf11=book1; ch2 pdf37=book27; ch5 pdf103=book93; running-header digit 490 on pdf 500).
- Column law: per-page gutter vote (same law as 9702); 410/696 pages two-column; single-band pages are openers, end-of-chapter pages, answers and back matter (justified inline)

## Content types

| type | chunks |
|---|---|
| body | 1220 |
| answers_eocq | 170 |
| questions | 167 |
| answers_saqs | 151 |
| exam_advice | 50 |
| recommended_resources | 48 |
| glossary | 44 |
| summary | 25 |
| learning_outcomes | 21 |
| chapter_questions | 21 |
| front_matter | 19 |
| index | 17 |
| worked_example | 8 |
| acknowledgements | 7 |
| appendix | 2 |
| cross_link | 1 |

## Quality notes

- **Text-layer lane, no OCR** (the 4BI1/9701 precedent). Sub/superscripts
  rebuilt from span geometry (99 chunks carry Unicode subscripts,
  225 superscripts).
- Damage census: fi-glue 53 / fl-glue 13 / double-space 534 / ligature-char 97 (span-join class, v1 unrepaired; LLM polish NOT STARTED - quota-walled regime)
- Serving-critical anchors: question banks anchored per the validator
  (chapter_questions / exam_bank / banks ranges).
- **LLM fidelity polish: NOT STARTED** (quota-walled regime; protocol
  identical to the 4PH1/4BI1/YPH11/9701 lanes; pristine snapshot is the
  anchor-diff target).
