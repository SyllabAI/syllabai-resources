# books/cambridge-international/ial/physics/9702 — parsed

## Corpus

- `cie_a_level_physics_9702_chunks_v1.jsonl` — **2046 chunks** (`cie_v1_` prefix grammar
  `c9702_v1_u{unit|0}_c{chapter|0}_pdf{pdfpage:03d}_{n:04d}`), 13-key v1 grammar
  (same schema as 4BI1/YPH11/9701 v1).
- `cie_a_level_physics_9702_chunks_v1.pristine` — byte-identical snapshot
  (merge-diff + anchor law reference for the future polish lane).
- `full_book_textlayer.md` — rendered book.
- `parse_report_v1.json` — provenance, decisions D-1…, census, damage census.

## Book facts

- Cambridge International AS and A Level Physics Coursebook (2nd edition) — David Sang, Graham Jones, Gurinder Chadha, Richard Woodside (CIE 9702 (2016 syllabus line)).
- Source: born-digital print replica (Adobe InDesign CS6 -> 3-Heights PDF Producer 4.4.14.0); two-column body (main + sidebar QUESTION boxes, sides swap per page); openers/EOC/answers single-column.
- Page law: book = pdf - 12 (verified 4 ways: ch1 opener pdf13=book1; ch2 pdf26=book14; ch5 pdf81=book69; running-header digit 285 on pdf 297).
- Column law: per-page gutter vote (gap>=14pt, both sides>=25pt, >=4 votes, both bands >=6 spans); 340/744 pages two-column; the 404 single-band pages are openers, end-of-chapter question pages, answers and back matter (justified inline)

## Content types

| type | chunks |
|---|---|
| body | 1100 |
| questions | 253 |
| answers_eoc | 168 |
| answers_saqs | 151 |
| worked_example | 112 |
| recommended_resources | 44 |
| chapter_questions | 37 |
| learning_outcomes | 34 |
| summary | 33 |
| exam_advice | 33 |
| glossary | 30 |
| index | 17 |
| front_matter | 15 |
| appendix | 11 |
| extension_work | 4 |
| acknowledgements | 4 |

## Quality notes

- **Text-layer lane, no OCR** (the 4BI1/9701 precedent). Sub/superscripts
  rebuilt from span geometry (371 chunks carry Unicode subscripts,
  811 superscripts).
- Damage census: fi-glue 101 / fl-glue 33 / double-space 596 / ligature-char 2 (span-join class, v1 unrepaired; LLM polish NOT STARTED - quota-walled regime)
- Serving-critical anchors: question banks anchored per the validator
  (chapter_questions / exam_bank / banks ranges).
- **LLM fidelity polish: NOT STARTED** (quota-walled regime; protocol
  identical to the 4PH1/4BI1/YPH11/9701 lanes; pristine snapshot is the
  anchor-diff target).
