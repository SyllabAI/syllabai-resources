# books/cambridge-international/igcse/physics/0625 — parsed

## Corpus

- `cie_igcse_physics_0625_chunks_v1.jsonl` — **896 chunks** (`cie_v1_` prefix grammar
  `c0625_v1_u{unit|0}_c{chapter|0}_pdf{pdfpage:03d}_{n:04d}`), 13-key v1 grammar
  (same schema as 4BI1/YPH11/9701 v1).
- `cie_igcse_physics_0625_chunks_v1.pristine` — byte-identical snapshot
  (merge-diff + anchor law reference for the future polish lane).
- `full_book_textlayer.md` — rendered book.
- `parse_report_v1.json` — provenance, decisions D-1…, census, damage census.

## Book facts

- Cambridge IGCSE Physics (3rd edition, Hodder) — Tom Duncan, Heather Kennett (CIE 0625 (Hodder endorsed 3rd ed)).
- Source: PDFium re-render; irregular two-band grid (text right band x~314-570, figures/margin boxes left); openers carry the 2-column at-a-glance box (bullet glyphs render as 'l' or single U+25CF).
- Page law: book = pdf - 13 (verified 5 ways: Section 1 divider pdf14=book1; ch1 opener pdf15=book2 (TOC); ch2 pdf22=book9 (TOC); Answers pdf312=book299 (TOC); Index pdf321=book308 (TOC)).
- Column law: FIXED gutter x=307 (probed: per-page gap votes irregular across pages); both-bands>=6-spans sanity; crossing spans stay in the left band; 258/328 pages two-column; single-band pages are covers/dividers/figure-dominated pages (justified inline)

## Content types

| type | chunks |
|---|---|
| body | 606 |
| learning_outcomes | 50 |
| checklist | 50 |
| practical | 48 |
| exam_bank | 42 |
| answers | 19 |
| mathematics | 17 |
| index | 15 |
| worked_example | 13 |
| alt_practical_bank | 11 |
| practical_test_bank | 10 |
| revision_bank | 9 |
| investigations | 4 |
| revision_questions | 1 |
| acknowledgements | 1 |

## Quality notes

- **Text-layer lane, no OCR** (the 4BI1/9701 precedent). Sub/superscripts
  rebuilt from span geometry (77 chunks carry Unicode subscripts,
  124 superscripts).
- Damage census: fi-glue 340 / fl-glue 149 / double-space 189 / ligature-char 12; 44 tiny (<30 char) chunks (figure-label debris); LLM polish NOT STARTED
- Serving-critical anchors: question banks anchored per the validator
  (chapter_questions / exam_bank / banks ranges).
- **LLM fidelity polish: NOT STARTED** (quota-walled regime; protocol
  identical to the 4PH1/4BI1/YPH11/9701 lanes; pristine snapshot is the
  anchor-diff target).
