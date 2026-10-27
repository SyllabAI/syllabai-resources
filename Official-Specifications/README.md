# Official Specifications (Pearson Edexcel + Cambridge International)

Official exam-board specification PDFs for the qualifications behind the SME
courses in `../SME-ExamQuestion/` and `../SME-RevisionNotes/`.
58 qualifications covering every course in the corpus registry.

## How these were found

- **Edexcel + most CIE courses**: SME course landing pages expose
  `props.pageProps.courseExamSpecificationPdfLink` (rendered as the
  "Exam specification" card) pointing at the official PDF on
  `qualifications.pearson.com` / `cambridgeinternational.org`.
- **AS lanes without a landing card** (business-23, computer-science-19,
  accounting-21 AS views): the CIE syllabus PDF is a combined
  "AS & A Level" document, so the AS course joins the qualification its
  sibling A-level course already maps to (recorded per qualification in
  `manifest.json`; probe receipt 2026-10-28).
- **3 Science Double Award courses**: SME leaves the link `null` (no card);
  the 4SD0 PDF came from Pearson's own qualification page
  (`edexcel-international-gcses/international-gcse-science-double-award-2017.html`).
- **1 stale link**: SME's Business URL now serves the Pearson CDN's HTTP-200
  HTML 404 page; replaced with the current URL from Pearson's
  `business-2017.html` qualification page (recorded in `spec.json` as
  `sme_source_url`).

## Layout

```
Official-Specifications/
  manifest.json                      # schema 1.0: provenance + per-qualification records
  <qualification-slug>/              # one dir per official qualification
    <original-filename>.pdf          # unmodified download
    spec.json                        # source URL, sha1, bytes, pages, cover_code,
                                     # spec_codes, issue (Edexcel) / edition_window
                                     # (CIE), sme_courses, fetched_utc
```

Qualification slugs group SME courses that share one official spec (e.g.
`ial-maths` covers all ten `ial-maths-20-*` units plus
`ial-further-maths-18-further-pure-1`; `cie-a-level-maths-2023-2025` covers
the A-level maths units AND the four AS maths units — one 9709 syllabus).

## Qualification inventory — Cambridge International (34)

| qualification | board | cover code(s) | edition window | pages | SME courses |
|---|---|---|---|---|---|
| cie-a-level-accounting-2023-2025 | Cambridge | 9706 | 2023-2025 | 40 | cie-a-level-accounting-21, cie-as-accounting-21 |
| cie-a-level-biology-2025-2027 | Cambridge | 9700 | 2025-2027 | 73 | cie-a-level-biology-25, cie-as-biology-25 |
| cie-a-level-business-2023-2025 | Cambridge | 9609 | 2023-2025 | 46 | cie-a-level-business-23, cie-as-business-23 |
| cie-a-level-chemistry-2025-2027 | Cambridge | 9701 | 2025-2027 | 98 | cie-a-level-chemistry-25, cie-as-chemistry-25 |
| cie-a-level-computer-science-2024-2025 | Cambridge | 9618 | 2024-2025 | 48 | cie-a-level-computer-science-19, cie-as-computer-science-19 |
| cie-a-level-economics-2023-2025 | Cambridge | 9708 | 2023-2025 | 43 | cie-a-level-economics-23 |
| cie-a-level-geography-2025-2026 | Cambridge | 9696 | - | 40 | cie-a-level-geography-21 |
| cie-a-level-maths-2023-2025 | Cambridge | 9709 | 2023-2025 | 59 | cie-a-level-maths-20-mechanics, cie-a-level-maths-20-probability-and-statistics-1, cie-a-level-maths-20-probability-and-statistics-2, cie-a-level-maths-20-pure-1, cie-a-level-maths-20-pure-3, cie-as-maths-20-mechanics, cie-as-maths-20-probability-and-statistics-1, cie-as-maths-20-pure-1, cie-as-maths-20-pure-2 |
| cie-a-level-physics-2025-2027 | Cambridge | 9702 | 2025-2027 | 68 | cie-a-level-physics-25, cie-as-physics-25 |
| cie-as-english-general-paper-2028-2030 | Cambridge | 8021 | 2028-2030 | 25 | cie-as-english-general-paper-21 |
| cie-as-environmental-management-2025-2027 | Cambridge | 8291 | 2025-2027 | 49 | cie-as-environmental-management-20 |
| cie-igcse-accounting-2023-2025 | Cambridge | 0452 | 2023-2025 | 26 | cie-igcse-accounting-21 |
| cie-igcse-accounting-2027-2029 | Cambridge | 0452 | 2027-2029 | 30 | cie-igcse-accounting-25 |
| cie-igcse-biology-2023-2025 | Cambridge | 0610 | 2023-2025 | 61 | cie-igcse-biology-23 |
| cie-igcse-business-2023-2025 | Cambridge | 0450 | 2023-2025 | 30 | cie-igcse-business-23 |
| cie-igcse-business-2027-2029 | Cambridge | 0264 | 2027-2029 | 33 | cie-igcse-business-25 |
| cie-igcse-chemistry-2023-2025 | Cambridge | 0620 | 2023-2025 | 59 | cie-igcse-chemistry-23 |
| cie-igcse-computer-science-2023-2025 | Cambridge | 0478 | 2023-2025 | 55 | cie-igcse-computer-science-23 |
| cie-igcse-economics-2023-2025 | Cambridge | 0455 | 2023-2025 | 30 | cie-igcse-economics-20 |
| cie-igcse-economics-2027-2029 | Cambridge | 0455 | 2027-2029 | 37 | cie-igcse-economics-25 |
| cie-igcse-english-language-2024-2026 | Cambridge | 0500 | 2024-2026 | 36 | cie-igcse-english-language-20 |
| cie-igcse-english-language-2027-2029 | Cambridge | 0500 | 2027-2029 | 42 | cie-igcse-english-language-25 |
| cie-igcse-english-literature-2023-2025 | Cambridge | 0475 | 2023-2025 | 35 | cie-igcse-english-literature-21 |
| cie-igcse-environmental-management-2027-2029 | Cambridge | 0680 | 2027-2029 | 50 | cie-igcse-environmental-management-25 |
| cie-igcse-further-maths-additional-maths-2025-2027 | Cambridge | 0606 | 2025-2027 | 31 | cie-igcse-further-maths-additional-maths-25 |
| cie-igcse-geography-2025-2026 | Cambridge | 0460 | 2025-2026 | 44 | cie-igcse-geography-20, cie-igcse-geography-25 |
| cie-igcse-history-2024-2026 | Cambridge | 0470 | 2024-2026 | 44 | cie-igcse-history-18 |
| cie-igcse-ict-2023-2025 | Cambridge | 0417 | 2023-2025 | 43 | cie-igcse-ict-21 |
| cie-igcse-maths-2025-2027 | Cambridge | 0580 | 2025-2027 | 71 | cie-igcse-maths-25-core, cie-igcse-maths-25-extended |
| cie-igcse-maths-international-maths-2025-2027 | Cambridge | 0607 | 2025-2027 | 72 | cie-igcse-maths-international-maths-23-core, cie-igcse-maths-international-maths-23-extended |
| cie-igcse-physics-2023-2025 | Cambridge | 0625 | 2023-2025 | 61 | cie-igcse-physics-23 |
| cie-igcse-religious-studies-2025-2027 | Cambridge | 0490 | 2025-2027 | 45 | cie-igcse-religious-studies-23 |
| cie-igcse-science-co-ordinated-sciences-double-award-2025-2027 | Cambridge | 0973 | 2025-2027 | 108 | cie-igcse-science-co-ordinated-sciences-double-award-23-biology, cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry, cie-igcse-science-co-ordinated-sciences-double-award-23-physics |
| cie-igcse-science-combined-science-2023-2024 | Cambridge | 0653 | 2023-2024 | 65 | cie-igcse-science-combined-science-23-biology, cie-igcse-science-combined-science-23-chemistry, cie-igcse-science-combined-science-23-physics |

## Qualification inventory — Pearson Edexcel (24)

| qualification | board | cover code(s) | edition window | pages | SME courses |
|---|---|---|---|---|---|
| ial-biology | Edexcel | XBI11/YBI11 | - | 78 | ial-biology-18 |
| ial-chemistry | Edexcel | XCH11/YCH11 | - | 108 | ial-chemistry-17 |
| ial-maths | Edexcel | XMA01/XFM01/XPM01/YMA01/YFM01/YPM01 | - | 99 | ial-further-maths-18-further-pure-1, ial-maths-20-decision-1, ial-maths-20-mechanics-1, ial-maths-20-mechanics-2, ial-maths-20-pure-1, ial-maths-20-pure-2, ial-maths-20-pure-3, ial-maths-20-pure-4, ial-maths-20-statistics-1, ial-maths-20-statistics-2 |
| ial-physics | Edexcel | XPH11/YPH11 | - | 87 | ial-physics-19 |
| igcse-accounting | Edexcel | 4AC1 | - | 50 | igcse-accounting-17-financial-statements, igcse-accounting-17-introduction-to-bookkeeping-and-accounting |
| igcse-biology | Edexcel | 4BI1 | - | 56 | igcse-biology-19 |
| igcse-biology-modular | Edexcel | 4XBI1 | - | 56 | igcse-biology-modular-24-unit-1, igcse-biology-modular-24-unit-2 |
| igcse-business | Edexcel | 4BS1 | - | 41 | igcse-business-19 |
| igcse-chemistry | Edexcel | 4CH1 | - | 58 | igcse-chemistry-19 |
| igcse-chemistry-modular | Edexcel | 4XCH1 | - | 58 | igcse-chemistry-modular-24-unit-1, igcse-chemistry-modular-24-unit-2 |
| igcse-economics | Edexcel | 4XEC1 | - | 54 | igcse-economics-17 |
| igcse-english-language-a | Edexcel | 4EA1 | - | 46 | igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing, igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing, igcse-english-language-a-16-paper-3-coursework |
| igcse-english-literature | Edexcel | 4ET1 | - | 46 | igcse-english-literature-16 |
| igcse-further-maths | Edexcel | 4PM1 | - | 52 | igcse-further-maths-19 |
| igcse-geography | Edexcel | 4GE1 | - | 57 | igcse-geography-19 |
| igcse-history | Edexcel | 4HI1 | - | 55 | igcse-history-17 |
| igcse-ict | Edexcel | 4IT1 | - | 47 | igcse-ict-17 |
| igcse-maths-a | Edexcel | 4MA1 | - | 70 | igcse-maths-a-18-foundation, igcse-maths-a-18-higher |
| igcse-maths-a-modular | Edexcel | 4XMAF/4XMAH | - | 66 | igcse-maths-a-modular-24-foundation-unit-1, igcse-maths-a-modular-24-foundation-unit-2, igcse-maths-a-modular-24-higher-unit-1, igcse-maths-a-modular-24-higher-unit-2 |
| igcse-maths-b | Edexcel | 4MB1 | - | 50 | igcse-maths-b-16 |
| igcse-physics | Edexcel | 4PH1 | - | 62 | igcse-physics-19 |
| igcse-physics-modular | Edexcel | 4XPH1 | - | 64 | igcse-physics-modular-24-unit-1, igcse-physics-modular-24-unit-2 |
| igcse-science-double-award | Edexcel | 4SD0 | - | 96 | igcse-science-double-award-17-biology, igcse-science-double-award-17-chemistry, igcse-science-double-award-17-physics |
| igcse-science-double-award-modular | Edexcel | 4XSD1 | - | 96 | igcse-science-double-award-modular-24-biology-unit-1, igcse-science-double-award-modular-24-biology-unit-2, igcse-science-double-award-modular-24-chemistry-unit-1, igcse-science-double-award-modular-24-chemistry-unit-2, igcse-science-double-award-modular-24-physics-unit-1, igcse-science-double-award-modular-24-physics-unit-2 |

`cover_code` is read from the PDF cover (authoritative qualification code);
`spec_codes` in `spec.json` additionally lists every unit/qualification code
found in the document text (e.g. the IAL W-unit codes WCH11-16, or the 4SD0
cross-references inside the individual science specs).

## Wave-2 additions (SME-WAVE2 r0, 2026-10-28)

- AS chemistry/biology/physics-25 + the four AS maths-20 units joined their
  shared syllabus qualifications on exact PDF-URL match (probe receipt).
- AS business/computer-science/accounting joined by title-span evidence
  (SME card null; PDF is the combined AS & A Level syllabus; A-level course
  shares the SME mid).
- NEW downloads: cie-a-level-geography-2025-2026 (9696) and igcse-history
  (4HI1), both discovered via the SME landing spec card the same day.
- README rewritten to cover both boards (previous revision listed Edexcel
  only and had gone stale at 20 qualifications / 39 courses).
