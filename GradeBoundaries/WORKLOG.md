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

---
## T-GRADE-2 run-002 — CIE session-listing crawl + aggregation wave (trace 1a19222d36f71611)

- CIE UNLOCK (corrects run-001): the `/grade-threshold-tables/<session>/` hub listing pages ARE server-rendered — the run-001 "JS-rendered, not crawlable" conclusion only held for the syllabus pages. fetch_cie.py rewritten as a session-listing crawler (8 listing pages → per-syllabus `/Images/<id>-…-grade-threshold-table.pdf` links), WANTED_CODES = the 31 course-map syllabi, sessions June 2026/June 2025/November 2025/November 2024, parallel downloads, CIE_IDS kept as verified fallback seed.
- FETCHED: 118 CIE docs present (30/31 codes × up to 4 sessions). Honest absences recorded in raw/fetch-missing.json: 0490 Religious Studies (no June 2025/June 2026 award in CIE listings — Nov 2024/Nov 2025 only) and 0264 Business (code changed for FIRST ASSESSMENT MARCH 2027 per official CIE syllabus page — no award exists yet; the cie-igcse-business-25 course honestly stays on roadmap).
- PARSE_CIE v2: award-section tagging ("Cambridge International A Level (linear assessment)" / "(staged assessment)" / "Cambridge International AS Level" exact standalone headers; 2025-and-earlier docs infer per-route award from the A* column, never applied to IGCSE docs); ladder-tail guard (a DATA row whose values end in single digits — e.g. 0470 "…11 9 8 7 6" — can no longer be mistaken for a grade ladder); 9-9…1-1 pair-ladder tokens for 0973 Co-ordinated Sciences (Double Award). Regression: 259 wave-1 CIE route rows byte-identical.
- PARSE_PEARSON fix: the 4XSD1 Science (Double Award) modular cash-in prints a 17-grade pair ladder as TWO segments (99…54 values line + 44…11+U labels on the code row + values line); June 2025's text layer lacks the second-segment labels entirely — stitched positionally / in-order (verified equal to June 2026 where labels are present). Both sessions now parse the full ladder {99:432 … 11:48, U:0}; 653 wave-1 Pearson rows re-verified (only intra-session ordering swaps of same-code variant rows).
- AGGREGATION STRUCTURE (curated/aggregation.json, cited): IAL cash-in compositions from the Pearson Qualifications Information Manual 2025/26 (YMA01 = WMA11-14 + one of the FIVE official applied pairs; YBI11/YCH11/YPH11 = units 1-6) and the A* rule from Pearson "IAL results explained" (A overall + 90% of A2 UMS; Maths 480 overall + 180/200 from P3+P4; six-unit IAL 480 + 270/300). Modular compositions from the 2024 specs (4XMAF/4XMAH = 1F/1H+2F/2H; 4XSD1 = Biology 1-2 + Chemistry 3-4 + Physics 5-6, unit codes verified against the spec). Structure metadata ONLY — every boundary value still document-sourced.
- course-map.yaml: explicit gbCashIn/gbUnits overrides for the 10 modular unit slugs (the legacy suite join could never split 4XMAF/4XMAH and would have mis-joined the shared-code 4XSD1 sciences).
- build_hub_import v2: aggregate-ums calculator blocks (cashIn + required + optionalPairs + aStar), per-series calculatorUnits (standard variant per composition unit — Pearson prints standard before variants), CIE routes level-filtered by parsed award (AS pages get AS routes, A-Level pages get A-Level-linear+staged), cash-ins carry their own gradeLadder (the 4XSD1 pair ladder).
- GATES: G1 0 errors (24 Pearson + 119 CIE docs); G2 MathsGenie parity 6/6 EXACT; G3(b) CIE coverage 30/31 (0264 honestly absent); G3(c) 28 aggregate-ums courses structurally sound (UMS maxima sum to cash-in maxima; per-session absences like WMA13/14 pre-June-2019 are info, not errors).
- BUNDLE: **105 served / 1 roadmap / 106 total** (was 50/56). Remaining roadmap: cie-igcse-business-25 (0264, no award exists yet).
- OPEN: YFM01 Further Maths aggregation (multi-route cash-in with unit locking — needs a verified official worked example); Pearson Jan 2023 / Nov 2021 golden sessions still unfound.

---
## NOTE — unlabelled R-variant rows: the 2019/2020-era `Papers X & Y` wording defeats parse_pearson's `Paper(s)`-only matcher (follow-up to T-GRADE-1/T-GRADE-2; fix-run candidate T-GRADE-3; base 009e8bf4, trace 1a194934c518f8e1)

- SYMPTOM (hub `/courses/igcse-chemistry-19/grade-boundaries`): 8 of the 19 bundle series rows for 4CH1 arrive as same-session duplicate pairs (June 2019, January 2020, January 2022, June 2022, June 2023, June 2024, June 2025, June 2026 — the hub rowSpan-groups them). The June 2022+ pairs carry the terse `papersNote` codes (`1C 2C` / `1CR 2CR`), but **June 2019 and January 2020 pairs have `papersNote: null`** — the hub renders `—` in the paper column and `isRegionalVariant` can never badge the R row (grade-boundaries-workspace.tsx:877/882/924); the honest "rows without a combination label appear in source order" footnote covers the display, but the gap is in the data, not the UI.
- ROOT CAUSE (document-level, nothing invented): Pearson changed the wording between layout generations — the 2019/2020-era docs print `Papers 1C & 2C` / `Papers 1CR & 2CR` under each 4CH1 row (pdftotext: June 2019.pdf lines 98/100, January 2020.pdf lines 54/56, sha16 `2623bf1ccdd16fa1` / `3a11dc2f5b7887c2`), the 2022+ docs print `Paper(s) 1C 2C` (June 2022.pdf lines 88/90, parses fine). parse_pearson.py:239 gates on `toks[0].startswith("Paper(s)")`, so the older spelling leaves papersNote None; build_hub_import.py:125 faithfully carries the null into the bundle. The data exists in the source documents — only the label capture is defeated.
- BLAST RADIUS (corpus scan of parsed/): pearson-int-gcse-linear only — 27 codes have multi-row variant sessions; **23 codes / 111 unlabelled rows, every one inside January 2019 (20 rows / 5 codes, sha16 `31634838f2c08237`), June 2019 (57 / 23), January 2020 (34 / 12)**. Multi-variant sets hurt most: 4EA1 and 4ET1 print 6 unlabelled rows per session, 4MA1 4, 4ES1 3. Every document from January 2022 onward captured its labels; modular, IAL and CIE families are unaffected.
- G2 NOTE: the MathsGenie golden rows equal the FIRST (standard-variant) row of each session (June 2019 = 143, January 2020 = 162 — the `1C 2C` row, never the R row), so a label-capture fix adds metadata only: values and row order byte-identical, parity must stay 6/6. Any run that shifts a value is by definition wrong.
- FIX PATH (queued, not executed in this note): parse_pearson.py accepts both wordings and normalizes to the newer shape (`Papers 1C & 2C` → `1C 2C`, `Papers 1CR & 2CR` → `1CR 2CR`); re-run run_all gates (G1/G2/G3) with a labels-only regression assert over the 653 wave-1 Pearson rows; rebuild the bundle and re-import to v2 — the June 2019 / January 2020 pairs then get labels + R badges and the `—` fallback retires for those rows.
- NON-GOALS: this note changes no parsed or bundled values; the exact official definition of the R papers is not asserted beyond the document text itself (labels derived from document text only, per the SOURCES law).

---
## T-GRADE-3 run-001 — variant-label capture: parse_pearson accepts the 2019/2020-era note wordings, zero value movement (base 7854805d, trace 1a194934c518f8e1)

- THE FIX (parse_pearson.py): the papers-note matcher gated on the 2022+ `Paper(s)` prefix only, so every note line in the three oldest linear docs was dropped (the NOTE above has the pdftotext evidence). Now accepted and normalized to the canonical 2022+ shape: `Papers 1C & 2C` → `1C 2C`; `Papers 1B, 1C & 1P` → `1B 1C 1P` (commas stripped too — verified equal to the January 2022 4SD0 canonical); singular `Paper 01` → `01` (single-paper subjects: English Language B, Bangla, Global Citizenship, Islamic Studies, Sinhala, Tamil — verified equal to the 2022+ 4EB1 canonical `01`/`01R`). Docstring documents all three wording generations.
- RE-PARSE: 24 Pearson docs / 922 subjects / 0 warnings — identical counts to run-001.
- ZERO-VALUE-MOVEMENT ASSERT (parsed layer): every field of every subject identical except `papersNote`; **129 fills, every one None → document-sourced label, zero value rewrites, zero reorders** (January 2019: 20, June 2019: 74, January 2020: 35). This corrects the NOTE's 111-row estimate: the note counted only multi-row variant groups — the single-row subjects (4AA1 Arabic, 4BA0 Bangla, 4BN1 Bangladesh Studies, 4CP0 Computer Science, 4GK1 Greek, 4GL1 Global Citizenship, 4IS1 Islamic Studies, 4PA1 Pakistan Studies, 4RS1 Religious Studies, 4SS0 Science (Single Award), 4SI1 Sinhala, 4SW1 Swahili, 4TA1 Tamil, and the Art/Design suite 4TD1/4FA1/4GC1/4PY1/4TE1) had lost their labels the same way (20 single-row fills).
- HONEST REMAINDERS: the two 4ES1 rows whose document subline reads `Speaking Endorsement` (June 2019, January 2020, max 40) keep no papersNote — the document prints no paper combination for them (the 2022+ era numbers that paper: June 2022 4ES1 note `03`); single-row subjects whose 2019/2020-era doc prints no note line at all (4AC1/4CM1/4HB1 in January 2020) stay None. The hub `—` fallback + footnote remain exactly right for these rows.
- BUNDLE (build_hub_import v1): rebuilt, **105 served / 1 roadmap / 106 total unchanged**, sha256_16 `9c7bc67671dd31e9` → `533671bf1070ff93`; diff contains only `generated` + **133 series fills across 21 served slugs** (chemistry-19 4, biology-19 4, physics-19 4, english-language-a-16 ×3 slugs 18 each, english-literature-16 17, maths-a-18-foundation/higher 6 each, maths-b-16 6, science-double-award-17 ×3 slugs 4 each, accounting-17 ×2 slugs 2 each, economics-17 4, business-19 2, geography-19 2, history-17 2, ict-17 2, further-maths-19 4); all 227 (course, session) joins verified label-list-equal against the parsed layer (bundle fills exceed parsed fills because shared-code rows serve multiple slugs).
- GATES: G1 0 errors (24 Pearson + 119 CIE docs); G2 MathsGenie parity **6/6 EXACT** (values byte-identical, assert-proven); G3(b) CIE 30/31 (0264 honestly absent); G3(c) 28 aggregate-ums courses 0 errors.
- HUB EFFECT: the 4CH1 June 2019 / January 2020 pairs now serve `1C 2C` / `1CR 2CR` → the hub renders the paper labels and the R badge; the `—` fallback retires for every variant group that had it (only the 4ES1 speaking rows keep it, by document).

- T-GRADE-7 HARVEST (operator trace: "Run it" after the why-are-years-missing diagnosis): the missing
  sessions were a fetch-side gap — Pearson names session docs inconsistently and the slug matrix lacked
  the `-v1` suffix family (Jan 2023 serves `2301-intgcse-9-1-subject-grade-boundaries-v1.pdf`; same
  index shows the sibling docs bare-suffixed). fetch_pearson.py matrices extended (`-v1`/`-v2` variants
  per lane; new-era `-v1` names for linear). Re-probe recovered 4 docs: linear January 2023 + November
  2021; IAL January 2021 + November 2020 (modular unchanged — first modular docs are 2024+). TOTAL 26/96;
  70 absences re-recorded in fetch-missing.json (cancelled June 2020/2021 series, October-era guesses,
  and docs Pearson no longer serves under any known slug).
- RE-PARSE: 26 Pearson docs / 991 subjects / 0 warnings. GATES: G1 0 errors; G2 MathsGenie 4CH1 parity
  6/6 EXACT; G3 info-only (honest IAL unit absences). BUNDLE rebuilt 105 served / 1 roadmap / 106 total,
  sha256_16 `7ba6951347f5c37e`; 4CH1 serves 13 sessions (+January 2023, +November 2021).

- T-GRADE-8 WIDGET HARVEST (trace 1a1984c6a317ea2d, operator: "recover these documents, they need to be scraped via their JS-based archive widget. And also what about other courses?"): the widget is AngularJS DocListCtrl backed by ALGOLIA — appId/key/index are public search-only credentials served in hidden inputs on the grade-boundaries page (index qualifications-uk_LIVE_master-content, 146807 records). New scripts/harvest_pearson_index.py paginates type:dam:Asset hits, maps filenames -> (family, session) with the slug grammar, intersects fetch-missing.json, downloads via fetch_pearson's own verified helpers. RECOVERED 14 docs: linear January 2021 + November 2020, ial x11 (June 2019/2022/2023, Jan 2023-26, Oct 2022-25), modular November 2025 — all %PDF-verified, soft-404-guarded.
- PARSE 40 docs / 1209 subjects / 0 warnings. VALIDATOR FIX: the two new linear docs are cancelled-award sessions printing COMPONENT boundaries only (verified in source: 4CH1 carries Paper 1C/1CR/2C/2CR rows, no overall) — G1 "no overall row" demoted to honest absence when NO subject in the doc has an overall row; partial asymmetry stays an error. G1 0 errors, G2 parity 8/8 EXACT (was 6/6 — golden overlap grew), aggregation 0 errors.
- BUNDLE rebuilt 3904274B sha256_16 f6e2a18c4f81636d: 105 served unchanged; +23 courses gain 150 sessions (13 IAL courses +140; 10 modular unit courses +10 November 2025). Linear courses gain ZERO served sessions — Jan 2021/Nov 2020 carry no overall awards (COVID), docs complete the corpus honestly. Remaining fetch-missing: 56 (want 70, recovered 14).

---
## T-GRADE-8 run-003 — the units-absent emission law: build_hub_import v2 (trace 1a19ad282798db31)

- UPSTREAM NOTE OF RECORD (run-014 receipt R0-AUTO-110, v2 PR #622 chain): "build_hub_import.py should not emit a series row whose only content is a cash-in — or should emit units-absent instead of `units: []`". The of-record incident: the October 2022/2023/2024/2025 FP1 sessions (row code YFM01, no aggregation entry → display-only) carry YFM01 cash-in boundaries but the source PDFs contain no WFM01 unit rows at all — v1 emitted those sessions as `units: []` + `cashIns`, and the v2 hub prebuild validator (validate_gradeb_bundle.ts: present-but-empty optional arrays are zero-tolerance) red-flagged main until the run-002 correction (v2 #623) hand-removed the 4 keys (+0/−4) in v2's imported copy. The generator itself stayed able to re-emit the shape on the next harvest.
- THE LAW (generator-wide): a series row's optional arrays (units/cashIns/components/routes/calculatorUnits) are emitted ONLY when they have rows — key-absent, never `[]` (put_rows). Same class fixed at every emission site: the modular path (units/cashIns/calculatorUnits) and the CIE path (components/routes; a session whose award filter empties both is skipped, not stubbed — zero effect on the current corpus, proven by the regen diff). The row-skip law is unchanged: a session with neither unit rows nor cash-in rows still never enters the bundle.
- FAIL-LOUD GUARDS: build_hub_import v2 asserts the law over the built bundle BEFORE writing (exit 1 with the offending rows); validate.py gains the same bundle shape gate (mirrors the hub validator's five-array law). GradeBoundaries/** is outside scripts-tests.yml's trigger paths (scripts/**, graph/**), so these in-lane gates are the merge gate — same posture as run-001/002.
- SELF-CHECK (new GradeBoundaries/scripts/test_units_absent.py — synthetic fixtures, zero corpus/network): 12/12 GREEN — the cash-in-only row keeps cashIns and drops the units key (FP1 shape mirrored from course-map.yaml's YFM01 row); a boundary-less cash-in keeps units and drops the cashIns key; both-present survives; neither skips; CIE AS-filtered routes key absent; guard negative control raises; linear rows carry no optional-array keys.
- REGEN PROOF (zero-invention, two-step): (1) a fresh v1 build over the committed corpus reproduces the committed bundle with zero semantic drift — `generated` stamp only (sha16 dd3c7d3e41c251a2 vs committed f6e2a18c4f81636d); (2) the v2 rebuild differs from v1 by EXACTLY the allowlist: generated, generator v1→v2, and the 4 FP1 October `units: []` keys (removal set assert-verified; no other drift tolerated by the verifier).
- BUNDLE: sha16 f6e2a18c4f81636d → a5912833279e4e61; 3,904,274 B → 3,904,202 B (−72 = the 4 keys); 105 served / 1 roadmap / 106 total UNCHANGED; CIE series key order preserved (source stays last — the reordered intermediate was rejected and rebuilt).
- GATES: G1 0 errors (40 Pearson docs); G2 MathsGenie 4CH1 parity 8/8 EXACT; G3(b) CIE 30/31 (0264 honestly absent); G3(c) 28 aggregate-ums courses 0 errors (info-only honest unit absences unchanged); bundle shape law silent.
- V2 EFFECT: none required now — v2's imported copy already carries the post-#623 units-absent shape on those 4 rows; the next mechanical import is a no-op for every boundary value (only the generated/generator stamps move). The law closes the reopen path: the next T-GRADE harvest re-emitting cash-in-only sessions can no longer re-break the hub prebuild gate.
- T-GRADE-9 ERA-GUARD (approved from the IAL analysis, trace 1a1984c6a317ea2d): Pearson reuses Y-cash-in codes across specs (YMA01 = legacy 2008 AND 2018 Maths). build_hub_import.py now refuses to serve an aggregate-ums row that carries NONE of the course's required-spec units (January 2019 legacy YMA01 was rendering its 480/420/... A-level boundaries on the nine ial-maths-20-* pages); transitional rows with at least one required-spec unit stay, already filtered to the composition allowlist. validate.py gains the enforcement twin: a served aggregate-ums row without a required-spec unit is a HARD error. pure-1 serves 18 sessions (was 19); 15/18 eligible; G1/G2(8/8 EXACT)/G3 all green; bundle 043289a76bf38e85. A* rule verified data-side: 12/12 IAL aggregate-ums courses have aStar config consistent with cash-in data (overallMin == printed A boundary; a2Min == 90% of A2 UMS max: 270/300 six-unit, 180/200 maths P3+P4) — the frontend engine (grade-boundaries-calc.ts gradeFromAggregation) and its honest UI label were already shipped in T-GRADE-2 and apply only when the cash-in row prints no A* boundary, so printed legacy A* rows keep precedence.

- T-GRADE-9 run-001 forensics (trace 1a19d1b53be79cd5, "why did the bundle shrink?"): v2 bundle 00836892->66d83097 measured 3904202->3866528 bytes (-37,674). Deep-diff: ONLY the 9 January 2019 sessions removed, one per ial-maths-20-* course; 0 sessions added, 0 overlapping rows differ, empty-array rows 0->0 (run-003 emission law changed no content; the residual 72B vs my pre-merge rebuild is serialization shape). Unit rows 2127->2091 (-36 = 9 x 4 units): the T-GRADE-8 January 2019 YMA01 row carried WME01/WST01/WME02/WST02 (~2.2KB/row) — those passed the composition allowlist because the applied-unit codes are shared across both specifications — but contained no required Pure unit (WMA11-14 absent), which is exactly the case the approved era-guard suppresses. No legitimate data lost: the removed rows were legacy-spec (2008) boundaries rendering under 2018-spec course pages.

---
## T-GRADE-9 run-002 — sandbox-rebuild verification: the merged chain reproduces itself end-to-end, zero drift (base f6ba6b16, trace f61b2052b1e1cccc)

- CONTEXT: fresh sandbox (no durable processes survive between sessions); the lane state was re-derived from this worklog and the LEDGER alone, then every closed item was re-proven against main + live. PRs confirmed MERGED: resources #257 (T-GRADE-1 lane A, 2026-11-01T05:29:54Z) and v2 #591 (T-GRADE-004 variant-label re-import, 2026-11-01T05:40:46Z). The T-GRADE-3 run-001 parser fix is on main (parse_pearson.py accepts the 2019/2020-era `Papers 1C & 2C` / `Papers 1B, 1C & 1P` / singular `Paper 01` wordings and normalizes to the 2022+ shape — docstring + comment at :16/:245).
- REGEN RECEIPT (the run's of-record proof): fresh build_hub_import v2 over the committed corpus → 105 served / 1 roadmap / 106 total, 3,866,528 B; semantic diff vs the committed bundle = the `generated` stamp ONLY (rest-equal assert TRUE; rebuilt sha16 94228254c09f2411 vs committed 94228254c09f2411). v2's imported copy is BYTE-IDENTICAL to the committed bundle (both 94228254c09f2411; v2 generated 2026-11-02T06:40:40Z) — the resources→v2 sync of record holds at f6ba6b16.
- GATES: validate.py exit 0 (40 Pearson docs 0 errors; 28 aggregate-ums courses 0 errors; honest-absence infos only); test_units_absent.py ALL GREEN.
- NOV 2021 papersNote:null ruled document-honest: in `November 2021.pdf` the sibling row 4CN1 prints `Paper(s) 01 02` under its row while 4CH1 prints NO note line at all (pdftotext lines 55-59) — the parser captured exactly what the document prints; the hub `—` fallback + footnote remain correct for that row.
- LIVE (syllabai-hub-v2.vercel.app, 2026-11-04): /courses/igcse-chemistry-19/grade-boundaries serves 13 sessions newest-first (T-GRADE-006 sort), Average pill + per-session rows, `1C 2C`/`1CR 2CR` labels with the R variant rows (T-GRADE-3 run-001 + T-GRADE-003 run-002 rowSpan grouping), and the 9-1 total-mark calculator; /courses/ial-maths-20-pure-1/grade-boundaries serves 18 sessions (the era-guarded count — was 19) newest-first with the honest "averaged across 15 sessions" label (15/18 eligible) and the UMS aggregate surface (T-GRADE-2 engine + T-GRADE-9 era-guard).
- NO DATA CHANGED: zero bundle bytes, zero parsed rows, zero frontend diffs this run — the run's product is the receipt (T-GRADE-9-VERIFY-RECEIPT.json) + this entry only. Sandbox footprint note: the lane is served by a sparse blobless clone (GradeBoundaries + root files; the other lanes re-materialize on demand via the same filter).

---
## T-GRADE-10 run-001 — YFM01 aggregation UNLOCK: the official multi-route selection cash-in, end-to-end (base f6ba6b16 -> e2c05f9b, trace 5c2f02913c6f798b)

- THE UNLOCK (what the roadmap item waited on): the official worked example exists — "IAL 2018 Mathematics Aggregation Rules & Guidance for Centres" (Rules 1-7: the two-step grade/UMS maximisation, the qualification-group unit locking, three worked Examples; the official AS/A2 unit designation "P1, P2, FP1, M1, S1 and D1 are AS units, P3, P4, FP2, FP3, M2, M3, S2 and S3 are A2 units"), downloaded + sha-pinned `61b32c5016644e74`, cited in curated/aggregation.json alongside the already-cited info-manual p.12 compositions and the results-explained A* rule (re-verified verbatim live this run: "A overall + at least 90% of the A2 UMS marks").
- STRUCTURE OF RECORD (curated/aggregation.json, PR #312): YFM01 = pool of the 10 FM-suite units, pick 6, WFM01 required, at least one of WFM02/WFM03 (the guidance's phrasing of the manual's two routes — provably equivalent); a2 = the six A2-designated units; aStar in RATE form (a2Rate 0.9 — the A2 UMS ceiling depends on which units the candidate's combination uses, so the pair-mode fixed a2Min cannot express it); Rule-1 maximisation flag. Roadmap entry RETIRED.
- BUILDER (PR #312): selection-mode courses join their pool units DOC-WIDE (the FM applied units print in the Mathematics block, the FP units in the Further Mathematics block of the same sha256-recorded documents) and embed calculatorUnits for every pool unit with UMS per session; the T-GRADE-9 era-guard gains the selection-mode posture (unit codes cannot date an FM row — WFM01-03 are shared across specs — so the hard invariant is pool membership; partial pool coverage is an honest absence, and all 18 YFM01 cash-in sessions kept serving).
- VALIDATOR (PR #312): selection-mode twins (pool-membership hard check; honest-absence infos for partial coverage; UMS-max-100 per pool unit; size x 100 == cash-in max; a2Rate 0.9 + a2Units within pool) plus the printed-A == overallMin consistency gate over EVERY aggregate-ums session (18/18 YFM01 sessions print A=480). GATES: run_all ALL GREEN; test_units_absent 12/12 GREEN.
- BUNDLE (PR #312): 105 served / 1 roadmap / 106 total UNCHANGED; only ial-further-maths-18-further-pure-1 changes (display-only -> aggregate-ums; 12/18 sessions calculator-eligible; 6 honest absences: no FP2/FP3 printed Jan 2019/2020, no WFM01 in the four Octobers); all other 105 courses byte-identical ex-stamp (assert-verified). v2 import byte-identical, sha16 2cb0628e9c3e3587.
- V2 (PR #765, merged e2c05f9b, CI green): schema (calculator.selection + the two-form aStar), gradeFromAggregation rate form (threshold = rate x the maxima of the A2 units the aggregation actually uses, zero-ceiling guard), NEW bestAggregationSelection (the board's Rule 1 over every eligible six — best grade first, then best UMS total; ties to first in code order; units without a UMS table can never aggregate; pure), and the workspace: inputs for every pool unit the session published, honest not-offered degradation, the used/banked disclosure, and the official post-rule (IAL Mathematics awarded first or concurrently; units lock to their qualification group; re-entering the Mathematics cash-ins can unlock a better combination). The official Rule 1 Example 1's FM half is a pinned test — it caught and killed a rank-inversion bug (B outranking A) on its first run.
- OPERATOR NOTE: the sandbox recycled twice mid-run and the disk ceiling (10G, 1.3G node_modules) blocked the local Next build — the full verify+build ran green in CI on the complete tree; the flashcard prebuild leg's failure in-sandbox was proven a sparse-checkout artifact (identical on the stock bundle). Local uncommitted work was backed up to work/scratch/tgrade10-backup before the risky legs.

---
## T-GB-STRUCT-1 run-001 — qualification STRUCTURE of record: the paper/weighting/award layer (4MB1 pilot, trace 55e0d4895a68bf0d)

- THE GAP (operator-reported, both examples verified against the official documents this run): the Grade Boundaries pages carry boundaries but not the qualification's structure — Maths B shows a 300-mark total with two 100-mark papers and NO explanation (Paper 2 is weighted 2x: 100x1 + 100x2 = 300), and IAL award rules exist for only 13 of 106 courses. Census: 0/106 courses carry structure/weighting fields; 55 are display-only; the zod schema had no structure fields at all.
- STRUCTURE OF RECORD (curated/structure.json, schema syllabai.grade-boundaries.structure/1): papers (codes, raw maxima, durations, tiers), official weightings as printed rationals (4MB1: Paper 1 100 marks 33 1/3%, Paper 2 100 marks 66 2/3%), the graded-total derivation, award rules, and full-sha256-pinned sources with per-course sourceIds. The 4MB1 spec (Issue 1, Jan 2016) is pinned in full (62d4534ba1c0aee42ce2d3e7fd1da8083fd03216dd106da11ae590525d3187a5, stored raw/specs/) alongside the June 2026 boundaries PDF (9c5627002aeba93e21062705d05da8d39a51364f841617efd335f49d1c3b8abe) as the maxMark-300 cross-check. SOURCES.yaml gains the qualification_structure registry block.
- BUILDER (v3): apply_structure() attaches the resolved block — papers/total/awardRules + the resolved source pins — to matching course entries keyed by code; absent structure stays absent (honest, never a stub). Bundle schema bumps to /1.1, generator string to v3.
- VALIDATOR (G-STRUCT): Σ(rawMax x weightFactor) == total.maxMark, weights sum to the whole, >= 1 sha-pinned source per block, awardRules present (no stubs), calculator.maxMark and EVERY served series maxMark equal the structure total (the cross-document "it shows 300" consistency law, now checked).
- BUNDLE (5d80e1c8f59ffd43): 105 served / 1 roadmap / 106 UNCHANGED; deep-compare vs the committed bundle = the structure block on igcse-maths-b-16 + the two intended string bumps ONLY (assert script scripts/compare_gb_bundle.py in the session workspace); PARITY 8/8, AGGREGATION 29/29, G-STRUCT 1/1 green.
- MANIFEST DISCLOSURE: raw/MANIFEST.jsonl is committed; the committed copy froze a 144-row operator-local state (Oct 31 era incl. the since-narrowed cie-0625 June 2024 window) that is NOT reproducible from the committed corpus. This run rebuilds it honestly as the current 159-row corpus — every row's url/file/sha256/bytes/fetched_at from the parsed docs, CIE byte counts recovered by sha-verified re-download (sha mismatch = fail-loud), new sha16 a71dad2e318a8046; bundle.source.documents/manifest_sha16 drift accordingly (disclosed, serving content unaffected).
- V2: schema + the "How this qualification is graded" block + provenance footer land in the v2 PR (referenced from the receipt).

---
## T-GB-STRUCT-2 run-001 — IGCSE linear family structure audit: 14 qualifications, 20 new blocks (trace c1af7f6f6d837d51)

**What landed.** The qualification-structure layer extends from the 4MB1 pilot
to the whole Pearson International GCSE linear family served by the hub:
14 qualifications → 20 more served courses carry embedded `structure` blocks
(21 of 21 linear courses total, counting run-001's 4MB1). Every value is
transcribed from the official Pearson specification PDF, each now committed
under `raw/specs/` and pinned by full sha256 in SOURCES.yaml +
curated/structure.json (14 new pins).

**Reconciliation with the served boundaries data (the audit's teeth).** Each
block's graded total was cross-checked against the calculator maxMark the hub
actually serves — all match: 4MA1 200 (per tier, F 1F+2F, H 1H+2H, 2h/100
each, 50% each; Issue 2 renamed 3H/4H→1H/2H), 4PM1 200 (01+02, 2h, 100 each),
4BI1/4CH1/4PH1 180 (Paper 1 110/2h + Paper 2 70/1h15, marks not scaled),
4SD0 330 (three Paper 1s 4BI1/1B+4CH1/1C+4PH1/1P, 110 each 33.3%, double
grades 9-9..1-1; papers carry single-science codes per the 4SD1 suite spec
which documents the 4SD0 co-codes), 4AC1 150 (100/2h 66.6% + 50/1h15 33.3%),
4BS1 160 (80+80, 1h30), 4EC1 160 (80+80, 1h30), 4ET1 150 (C1 90/2h + C2 60/1h30),
4EA1 150 (C1 90/2h15 + C2 60/1h30), 4GE1 175 (70/1h10 40% + 105/1h45 60%),
4HI1 120 (60+60, 1h30), 4IT1 200 (written 100/1h30 + practical 100/3h).

**Schema extensions (additive).** `courses[code].tiers` — tier-keyed blocks
for the tiered qualification 4MA1; apply_structure picks by the built entry's
tier and FAILS loud on a missing tier block (config error, never a silent
stub). Single-tier qualifications keep the existing shape untouched.

**Route choices recorded honestly, arithmetic exact.** 4EA1/4ET1 awardRules
notes record the spec's Component 2-or-3 choice (exam vs coursework/NEA, both
60 marks — either route totals 150 with Component 1); the block pins the exam
route; a future lane can render routes explicitly. 4EA1's optional Spoken
Language endorsement is noted (ungraded).

**Gate.** validate.py: STRUCTURE 21 blocks checked, 0 errors (arithmetic law
Σ rawMax×weightFactor == total.maxMark per block, weights sum to 1, full-sha
pinned sources, awardRules present, calculator cross-check per linear-total
course). Bundle rebuilt: 4,023,723 bytes, deterministic except `generated`.

**Honest absences / notes.** Availability windows and AO weightings are in
the specs but not part of the structure schema (not served by the hub page
law this lane covers); 4MA1/4PM1 regional variants (R-papers) are not recorded
— the 4MB1 pattern's regionalVariant field exists but no R-paper structure
differences were extracted this run; roadmap note for a follow-up if the hub
ever serves R-variant boundaries.

---
## T-GB-STRUCT-3 run-001 — modular IGCSE award laws: the 16 aggregate-ums courses get their qualification-grade rules (trace 0b3e2a41c9d75f60)

**Correction to the lane title.** The "16 aggregate-ums courses without an
A* law" are NOT IAL — the 13 IAL unit courses were already covered by the
run-001-era Y-cash-in aStar laws (YBI11/YCH11/YPH11/YMA01/YFM01). The 16 are
the Pearson International GCSE (Modular) 2024 suite unit courses (Biology/
Chemistry/Physics 2 each, Maths A modular F/H 2+2, Science Double Award 6),
aggregating to cash-ins 4XBI1/4XCH1/4XPH1/4XMAF/4XMAH/4XSD1. Honest audit
output, stated plainly.

**What landed.** The award law for all six modular cash-ins, transcribed from
the five official modular specifications (raw/specs/4X?-modular-specification.pdf,
full sha256 pinned in SOURCES.yaml): 9-1 grading on total UMS with FIXED
spec-published thresholds — 4XBI1/4XCH1/4XPH1: units 4WB/CH/PH1+2 at 120 UMS
each, cash-in 240, grade 9 at 216 (90%), 8 at 192 … 1 at 24; 4XMAF (240):
F grades 5–1 at 120/96/72/48/24; 4XMAH (240): H grades 9–3 at
216/192/168/144/120/96/84 (grade 3 allowed at 42 per 120-UMS unit — the spec's
"3 allowed" law); 4XSD1 (480): SEVENTEEN-grade double ladder 9-9..1-1
(9-9 capped at the full 480, 9-8 432 … 1-1 72), six units 4WSD1..6 at 80 UMS
each. Per-unit fixed tables recorded too. Shared rules: best of the two most
recent attempts counts toward aggregation; results held in the unit bank;
first certification August 2025; unclassified below 24 (240-UMS cash-ins) or
48 (480-UMS).

**Embedding.** build_hub_import.py now embeds the law into every modular
course calculator (umsMax, unitUmsMax, gradeThresholds, unitGradeTables,
aStar.overallMin = top-grade threshold with the 9-1 ladder note, resitRule) —
16 courses, additive keys only, IAL calculators untouched.

**Gate.** New check_modular_awards: Σ unitUmsMax == umsMax, thresholds
strictly descending within range, aStar.overallMin == top threshold, and every
served session's unit UMS max must equal the law. The aggregation check now
also enforces the law's thresholds against the boundaries the served cash-in
rows print, session by session — the spec table and the served June 2025 /
November 2025 / June 2026 cash-in rows agree exactly (216/192/.../24),
independent documentary confirmation.

**Audit finds served-data truth, not bugs (adapted sessions).** The structure
cross-check flagged November 2021 (4GE1 160, 4HI1 90) and June 2022
(4GE1 134, 4HI1 90). Re-checked against the official boundaries documents
themselves: those totals ARE what Pearson printed — COVID-era (November 2021)
and advance-information (June 2022) adaptations, with the route rows 4HI1
Papers 1A+2A / 1B+2B at 90. The parsed and served data is faithful; the
assumption "every session totals the spec figure" was the wrong part. The four
sessions are now recorded as adaptedSessions in curated/structure.json
(evidence: the pinned raw boundaries PDFs) and the gate accepts a session
total only when it matches the recorded adaptation. Everything else stays
strict.

**Honest absences.** Modular unit RAW maxima (90 per separate-science unit,
60 per SDA unit, 100 per maths unit) are served per-session already; the spec
documents first assessment June 2025 / first certification August 2025 for the
whole suite. No A* language anywhere: these qualifications top out at grade 9
(9-9 for the double award) — the aStar field carries the top-grade law with
that note spelled out.
