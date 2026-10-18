# T-SPECS-CIE-PARSE-1 — CIE specification parse record (2026-10-19)

**Directive:** operator message (gateway trace 1a1504b1a97e2005, 2026-10-19, zai-web, session web-64d10b73-530a-4f71-9961-85d0436c7fb5) — "CIE parse lane" (fires NEXT lane #1 of the T-SPECS-CIE-1 record).

**Result:** ALL 33 CIE syllabus PDFs parsed deterministically into `parsed/<cie-slug>/` registries (SCHEMA v1.0 shape + the documented CIE extension: per-point `tier`/`number`, `code-assembled`/`synthesized-ordinal`/`bullet-row`/`synthesized-id` flags). **6,758 spec points**, 1,183 topics/subsection families total, zero-LLM (pymupdf text-layer spans, page+oy provenance, same conventions as the Edexcel `spec-parser-1.0`). Check battery C1-C10 ALL PASS (`T_SPECS_CIE_PARSE_1_CHECK.json`).

## Method

1. `scripts/cie_parse_survey.py` + `cie_parse_autodetect.py` + `cie_samples/` — text-layer + numbering-family reconnaissance over all 33 PDFs (families frozen into the parser's FAMILY map).
2. `scripts/cie_spec_parser.py` (`cie-spec-parser-1.0`) — six family extractors over the shared span primitives (running-header kill, gap-aware line joins, y-ordered head switching inside column bands, expect-guarded ordinals, column-geometry sibling rules). Content regions from running-header bands with a one-page backward divider extension.
3. `scripts/cie_parse_check.py` — the C1-C10 battery; Edexcel byte-stability enforced against `parsed/_summary.json` (23 rows deep-equal, serialization sha-pinned).

## Family census

| family | quals | spec points |
|---|---|---|
| `tier_columns` | 5 | 1804 |
| `int_statements` | 12 | 2105 |
| `nmk_outcomes` | 8 | 902 |
| `ce_codes` | 2 | 564 |
| `lettered_items` | 1 | 364 |
| `heading_bullets` | 5 | 1019 |

## Per-qual results (33/33 gates G1-G4 PASS, zero duplicate ids)

| qual | family | points | topics | subsections | pdf |
|---|---|---|---|---|---|
| cie-a-level-accounting-2023-2025 | nmk_outcomes | 34 | 4 | 23 | 595461-2023-2025-syllabus.pdf |
| cie-a-level-biology-2025-2027 | int_statements | 257 | 19 | 44 | 664560-2025-2027-syllabus.pdf |
| cie-a-level-business-2023-2025 | nmk_outcomes | 116 | 10 | 46 | 595459-2023-2025-syllabus.pdf |
| cie-a-level-chemistry-2025-2027 | int_statements | 356 | 35 | 91 | 664563-2025-2027-syllabus.pdf |
| cie-a-level-computer-science-2024-2025 | int_statements | 227 | 20 | 44 | 636089-2024-2025-syllabus.pdf |
| cie-a-level-economics-2023-2025 | nmk_outcomes | 253 | 24 | 57 | 595463-2023-2025-syllabus.pdf |
| cie-a-level-maths-2023-2025 | int_statements | 146 | 6 | 38 | 597421-2023-2025-syllabus.pdf |
| cie-a-level-physics-2025-2027 | int_statements | 303 | 25 | 76 | 664565-2025-2027-syllabus.pdf |
| cie-as-english-general-paper-2028-2030 | heading_bullets | 73 | 2 | 0 | 743333-2028-2030-syllabus.pdf |
| cie-as-environmental-management-2025-2027 | int_statements | 131 | 8 | 28 | 664522-2025-2027-syllabus.pdf |
| cie-igcse-accounting-2023-2025 | int_statements | 144 | 7 | 27 | 596935-2023-2025-syllabus.pdf |
| cie-igcse-accounting-2027-2029 | int_statements | 177 | 7 | 28 | 718141-2027-2029-syllabus.pdf |
| cie-igcse-biology-2023-2025 | tier_columns | 388 | 21 | 69 | 595426-2023-2025-syllabus.pdf |
| cie-igcse-business-2023-2025 | nmk_outcomes | 63 | 6 | 28 | 596930-2023-2025-syllabus.pdf |
| cie-igcse-business-2027-2029 | nmk_outcomes | 52 | 5 | 27 | 718123-2027-2029-syllabus.pdf |
| cie-igcse-chemistry-2023-2025 | tier_columns | 252 | 12 | 53 | 595428-2023-2025-syllabus.pdf |
| cie-igcse-computer-science-2023-2025 | int_statements | 88 | 10 | 22 | 595424-2023-2025-syllabus.pdf |
| cie-igcse-economics-2023-2025 | nmk_outcomes | 129 | 6 | 40 | 596945-2023-2025-syllabus.pdf |
| cie-igcse-economics-2027-2029 | nmk_outcomes | 113 | 6 | 42 | 718148-2027-2029-syllabus.pdf |
| cie-igcse-english-language-2024-2026 | heading_bullets | 163 | 23 | 0 | 635230-2024-2026-syllabus.pdf |
| cie-igcse-english-language-2027-2029 | heading_bullets | 209 | 34 | 0 | 718783-2027-2029-syllabus.pdf |
| cie-igcse-english-literature-2023-2025 | heading_bullets | 203 | 25 | 0 | 596436-2023-2025-syllabus.pdf |
| cie-igcse-environmental-management-2027-2029 | nmk_outcomes | 142 | 7 | 45 | 718156-2027-2029-syllabus.pdf |
| cie-igcse-further-maths-additional-maths-2025-2027 | int_statements | 68 | 14 | 67 | 662470-2025-2027-syllabus.pdf |
| cie-igcse-geography-2025-2026 | int_statements | 113 | 3 | 19 | 664610-2025-2026-syllabus.pdf |
| cie-igcse-history-2024-2026 | heading_bullets | 371 | 37 | 0 | 649636-2024-2026-syllabus.pdf |
| cie-igcse-ict-2023-2025 | int_statements | 95 | 21 | 52 | 595352-2023-2025-syllabus.pdf |
| cie-igcse-maths-2025-2027 | ce_codes | 290 | 45 | 146 | 662466-2025-2027-syllabus.pdf |
| cie-igcse-maths-international-maths-2025-2027 | ce_codes | 274 | 43 | 142 | 662472-2025-2027-syllabus.pdf |
| cie-igcse-physics-2023-2025 | tier_columns | 294 | 6 | 42 | 595430-2023-2025-syllabus.pdf |
| cie-igcse-religious-studies-2025-2027 | lettered_items | 364 | 25 | 85 | 663158-2025-2027-syllabus.pdf |
| cie-igcse-science-co-ordinated-sciences-double-award-2025-2027 | tier_columns | 632 | 38 | 132 | 664570-2025-2027-syllabus.pdf |
| cie-igcse-science-combined-science-2023-2024 | tier_columns | 238 | 30 | 77 | 597065-2023-2024-syllabus.pdf |

Total: **6,758 spec points** across 33 quals; `_summary.json` extended to 56 rows (23 Edexcel rows byte-stable).

## Notes

- Environment rollback recovery (pre-lane): the local clone was restored from a pre-Task-21 snapshot (tip 6af7ee4, manifest 23 quals, sparse-checkout cone dropped the spec dirs); origin was the record of record at cdca9ea (T-SPECS-CIE-1 + push, GitHub API verified). Recovery = fetch + fast-forward + `git sparse-checkout add Official-Specifications` + SHA-1 re-verification 33/33 of the restored CIE PDFs.
- Edition rollovers change numbering families: 0455 economics 2023-2025 prints `N.M.K.`-with-trailing-dot outcome rows (nmk_outcomes) while 2027-2029 prints the same shape without dots; both in nmk_outcomes. 0452 accounting 2023-2025 uses unnumbered sibling bullets; 2027-2029 the same. Family map is per-qual, frozen from evidence.
- Prior-knowledge blocks (9709 divider), topic intro prose (9708/9609), and long component descriptions (0475/0500) are intentionally not captured (documented in SCHEMA.md).
- `parsed/_summary.json` is now the 56-qual run log; the CIE appender replaces prior `cie-*` rows on re-run (idempotent) and never touches the 23 Edexcel rows.

## Next lanes (operator-gated, NOT fired by this directive)

1. **Join lane** — SME spec-point tags → official CIE codes, emitting `spec-links/cie-*.json` sidecars (SUGGESTED state until the review gate accepts them, per AGENT.md). The CIE registries' `tier`/`scope` fields are the join keys for Core/Supplement and AS/A-Level splits.
2. Canonical bundle shape (spec_points.json/topics.json/... v2.0 split) for CIE — deferred until the join lane proves the consumption surface.

