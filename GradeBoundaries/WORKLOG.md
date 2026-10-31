# WORKLOG — GradeBoundaries lane (append-only)

---
## T-GRADE-1 run-001 — lane opened: Pearson/CIE fetch+parse+gates+bundle v1 (trace 1a191d55e2154601)

- SOURCES: Pearson slug matrix decoded (2024+ `grade-boundaries-<m>-<y>-<fam>.pdf` vs legacy `{yymm}-*` patterns — `1906-ig-9-1-subject-grade-boundaries.pdf`, `2201_intGCSE_(9-1)_Subject_Grade_Boundaries_V1.pdf`, `2001-ial-grade-boundaries.pdf`); CIE known-ID registry (listing pages are JS-rendered, not crawlable).
- Fetched 33 official PDFs (12 linear IGCSE incl. 6/8 golden sessions, 4 modular, 8 IAL, 9 CIE), each with url+final_url+sha256 in `raw/MANIFEST.jsonl`; 83 absent session probes recorded in `raw/fetch-missing.json` (covid-era + unpublished).
- PARSER LESSON OF RECORD: pdftotext renders blank/greyed cells as whitespace, so token-order parsing SHIFTS columns on tiered rows (Maths A Foundation = grades 5-1 only) — first parser produced 4CH1 Jun 2026 9=141 (true: 150). Parser rebuilt on pdfplumber x-coordinate joins; also glue-aware (pdfplumber fuses `…ChemistryRaw 80`), heading-lookahead-verified subject grouping (wrapped unit-title fragments can no longer create subjects), cash-in codes include the Y prefix. Final: 24 docs / 922 subjects / 0 warnings.
- GATES: G1 schema+monotonic GREEN (0 errors across 24 docs); G2 MathsGenie golden-master parity 6/6 EXACT (June 2019, Jan 2020, Jan 2022, Jun 2022, Nov 2023, Jun 2026 — the R-variant row equals MG's published data on every overlap); G3 coverage 6 >= 6 GREEN.
- CIE: two layout generations parsed (2026 titled tables + 2024/25 `Minimum raw mark required for grade` / `The overall thresholds` markers; option-coded rows `BX 200 21, 41, 51 …`); 9 docs → components + per-route thresholds, 0 warnings.
- BUNDLE: `hub-import/grade-boundaries-1.0/bundle.json` — **50 served / 56 roadmap / 106 total**; tier-split for 4MA1 F/H, unit-filtered modular suites (`-unit-N` slugs), IAL whole-subject blocks (units raw+UMS + X/Y cash-ins), linear-total calculator mode for linear IGCSE, display-only for modular/IAL/CIE (honest limitation, aggregation wave later).
- OPEN: 56 roadmap courses (CIE syllabi awaiting CIE_IDS extension; 2 missing golden sessions Jan 2023 / Nov 2021 not found under any probed Pearson slug — recorded, not invented).
