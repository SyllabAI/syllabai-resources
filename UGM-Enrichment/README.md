# UGM-Enrichment — Underground Mathematics metadata enrichment (facts only)

Additive, agent-generated lane enrichment derived from the Underground
Mathematics (UGM) reverse-engineering corpus. This directory follows the
repo's provenance law: every fact is machine-checkable back to its source
commit, every candidate is a **suggestion** until the review/promotion gate
accepts it, and **no third-party content text ships** — see licensing below.

## Files

- `cie-a-level-maths-20-pure-1-quadratics.json` — schema
  `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-MODE1-1`: the CIE 9709
  Pure 1 Quadratics spec points (1.1.1–1.1.5) enriched with UGM candidate
  resources from the quadratics station (56 aligned of 59 considered;
  3 explicit non-overlaps recorded, never collapsed — AGENT.md rule 3).
- `cie-a-level-maths-20-pure-1-circular-measure.json` — schema
  `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-MODE1-4`: the CIE 9709 Pure 1 Circular measure
  spec point (1.4.1, hub parse fragment 1.4.1a folded of record) enriched with UGM candidates —
  the **first strand lane**: 3 new-text aligned resources (text of record under
  `UGM-Resources/pure-1-circular-measure/`), 2 boundary non-overlaps, plus 14 cross-lane
  circles-strand alignments and 2 cross-lane non-overlaps recorded as facts with
  `textOfRecordUnder` pointers (62 corpus-sweep candidates: 41 routed to recorded homes —
  never forced, AGENT.md rule 3).
- `cie-a-level-maths-20-pure-1-trigonometry.json` — schema
  `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-MODE1-5`: the CIE 9709 Pure 1 Trigonometry
  spec points (1.5.1–1.5.5, no fold fragments) enriched with UGM candidates — the **two-station
  lane**: 41 aligned resources (36 Triangles-to-Functions + 3 Compound-Angles + 2 cross-station
  strays; 55 alignment rows), 36 non-overlaps (the compound-angles station's honest P3 2.3
  mapping — text of record imported UNMAPPED in the same lane directory, per the station-lane
  corpus law), plus 2 cross-lane fact joins to lane-2 bodies (r9924, r8411 → 1.5.4,
  `textOfRecordUnder` pointers) — 299 corpus-sweep candidates: 220 routed to recorded homes,
  never forced (AGENT.md rule 3).

- `cie-a-level-maths-20-pure-2-algebra.json` — schema `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-P2-1`: the CIE 9709 Pure 2 spec points (2.1.1–2.1.2) enriched entirely by cross-course twin joins of record — 31 cross-lane rows riding of-record pure-1/pure-3 bodies via `textOfRecordUnder` (the circular-slice precedent), 0 fresh bodies, 0 fresh psp rows (the lane-16 law).
- `cie-a-level-maths-20-pure-2-logarithmic-and-exponential-functions.json` — schema `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-P2-1`: the CIE 9709 Pure 2 spec points (2.2.1–2.2.4) enriched entirely by cross-course twin joins of record — 39 cross-lane rows riding of-record pure-1/pure-3 bodies via `textOfRecordUnder` (the circular-slice precedent), 0 fresh bodies, 0 fresh psp rows (the lane-16 law).
- `cie-a-level-maths-20-pure-2-trigonometry.json` — schema `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-P2-1`: the CIE 9709 Pure 2 spec points (2.3.1–2.3.2) enriched entirely by cross-course twin joins of record — 28 cross-lane rows riding of-record pure-1/pure-3 bodies via `textOfRecordUnder` (the circular-slice precedent), 0 fresh bodies, 0 fresh psp rows (the lane-16 law).
- `cie-a-level-maths-20-pure-2-differentiation.json` — schema `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-P2-1`: the CIE 9709 Pure 2 spec points (2.4.1–2.4.3) enriched entirely by cross-course twin joins of record — 41 cross-lane rows riding of-record pure-1/pure-3 bodies via `textOfRecordUnder` (the circular-slice precedent), 0 fresh bodies, 0 fresh psp rows (the lane-16 law).
- `cie-a-level-maths-20-pure-2-integration.json` — schema `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-P2-1`: the CIE 9709 Pure 2 spec points (2.5.1–2.5.3) enriched entirely by cross-course twin joins of record — 20 cross-lane rows riding of-record pure-1/pure-3 bodies via `textOfRecordUnder` (the circular-slice precedent), 0 fresh bodies, 0 fresh psp rows (the lane-16 law).
- `cie-a-level-maths-20-pure-2-numerical-solution-of-equations.json` — schema `syllabai.ugm-spec-enrichment/1.0`, task `T-UGM-P2-1`: the CIE 9709 Pure 2 spec points (2.6.1–2.6.3) enriched entirely by cross-course twin joins of record — 7 cross-lane rows riding of-record pure-1/pure-3 bodies via `textOfRecordUnder` (the circular-slice precedent), 0 fresh bodies, 0 fresh psp rows (the lane-16 law).

## What is and is not here

**Is (mode-1 facts):** UGM slugs, titles, resource types, levels,
confidence ratings, station/slug URLs, the cross-map's mode flags of
record, and UGM's own acknowledgement/provenance strings as recorded
metadata. Per-row `primaryPick` marks the one candidate the cross-map
judged the best low-threshold entry per spec point.

**Is not:** any UGM question text, suggestion/solution bodies, teacher-
support content, or images. Those remain in the research corpus
(`SyllabAI/syllabai-experimental` → `undergroundmathematics/`) and stay
there. Nothing in this directory renders or embeds UGM content.

## Governance

- `review_state.state = "SUGGESTED"` (AGENT.md rule 2): these are
  LLM-assisted alignment candidates with per-row confidence — not the
  verbatim-text joins the `spec-links/` tier vocabulary is built on.
  Promotion through the review/promotion gate may upgrade individual rows;
  the honest path for uncertain rows is demotion or removal, never
  similarity-manufactured coverage.
- Mode-2 (deep-link rendering on hub lane pages) was **dropped by operator
  directive 2026-10-22** before implementation (ADR-UGM-0001 amendment,
  syllabai-v2#305 closed not_planned). These rows land as data only.
- If UGM text of record is ever wanted, the only route is the Mode-3
  licensing ask scoped in ADR-UGM-0001 §Decision item 4 (provenance-
  matched, non-exclusive, attribution in UI) — it would land as its own
  LICENSE-DATA.md amendment first.
- **2026-10-23 addendum:** UGM text of record now ships under the operator attestation of
  2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23) via `UGM-Resources/` (per-lane text corpora,
  task ids `T-UGM-IMPORT-*`). This directory remains **facts-only** (mode 1); the "Is not"
  paragraph above describes this directory, not the corpus family.

## Provenance

- Source: `SyllabAI/syllabai-experimental` @ `915bfa8c`,
  `undergroundmathematics/resources/derived/cross-map-quadratics.json`
  (phase-3c pilot: 56/59 aligned = 95%, per-row confidence + notes).
- Decision record: `ADR-UGM-0001` (Accepted 2026-10-22, operator-ratified).
- Refresh chain: re-run the cross-map generalisation per lane in the
  research repo, then re-emit this artifact with a new `generated_utc`
  stamp (files are byte-idempotent per stamp). Do not hand-edit rows.


- **Lane 6 (CIE 9709 P1 1.6 Series)** — `cie-a-level-maths-20-pure-1-series.json`: the **second
  two-station lane**: 49 aligned resources (43 Sequences/Counting-and-Binomials substrate + 6 cross-station
  strays whose tested skill is 1.6.x; 56 alignment rows; primary picks r7078 / sort-it-out / r8907 /
  square-spirals), 50 recorded non-overlaps (combinatorics/logic dominance in Counting and Binomials;
  general-index binomial questions carry P3 Series bearings — recorded, never forced — text of record
  imported UNMAPPED in the same lane directory, per the station-lane corpus law), plus 2 cross-lane fact
  joins to lane-2 bodies (r7553, r9527 → 1.6.3, `textOfRecordUnder` pointers).
- **Lane 7 (CIE 9709 P1 1.7 Differentiation)** — `cie-a-level-maths-20-pure-1-differentiation.json`: the **third
  two-station lane** (Introducing Calculus + Calculus of Powers): 74 aligned resources (40 substrate — 9
  Introducing-Calculus + 31 Calculus-of-Powers — plus 34 cross-station strays whose tested skill is 1.7.x; 107
  alignment rows; primary picks r7692 / r9942 / r8065 / r9260), 32 recorded non-overlaps (the trapezium-rule and
  kinematics cluster in Introducing Calculus — the trapezium rule is not in the 2023–2025 P1 spec — recorded, never
  forced — text of record imported UNMAPPED in the same lane directory, per the station-lane corpus law), plus 3
  cross-lane fact joins to already-of-record bodies (r5640 vs lane 6; r7115 and r8936 vs lane 4,
  `textOfRecordUnder` pointers — the lane-4 non-overlap row for r7115 explicitly names 1.7 as the tested skill).

- **Lane 8 (CIE 9709 P1 1.8 Integration)** — `cie-a-level-maths-20-pure-1-integration.json`: the **first
  strand lane on a spec section** (UGM has no dedicated integration station; the two dedicated calculus
  stations are fully of record via lanes 5–7): 28 aligned resources / 28 alignment rows (10 new-text
  strand resources whose tested skill is 1.8.x — calculus-meets-functions 7, chain-rule 2, product-rule 1 —
  plus 18 cross-lane fact joins to already-of-record bodies under `pure-1-differentiation/`; 13 joins flip
  the lane-7 Calculus-of-Powers non-overlaps of record, the integration-dressed honesty lane 7 deferred to
  this lane, with the lane-7 reasons retained; 5 add one-to-many rows beside standing 1.7 alignments),
  0 new non-overlaps, primary picks r8716 / r7734 / r6067 / r9357, plus 32 routed (P3-technique pools,
  P3/Mechanics, trapezium-rule resources with no spine home) and 31 rejected with reasons — recorded,
  never forced.

- **Lane 9 (CIE 9709 Pure 3 3.1 Algebra)** — `cie-a-level-maths-20-pure-3-algebra.json`: the **first
  lane on the pure-3 course plane** (course `cie-a-level-maths-20-pure-3`; spine rows 3.1.1–3.1.6 verbatim
  from the repaired hub parse — `T-SPECS-CIE-PARSE-REPAIR-1` split official 2.1.1 into the 3.1.1/3.1.2
  limbs and recovered bullets 2–5 as 3.1.3–3.1.6): 47 aligned rows (38 fresh rows over 35 new-text
  resources — inequalities, r5276 and r6577 each carry two codes — plus 9 cross-lane fact joins to
  already-of-record bodies under `pure-1-functions/`, `pure-1-series/`, `pure-1-differentiation/` and
  `pure-1-integration/`; 5 joins flip standing non-overlaps of record — r8427 (lane 2) and
  r5245/r6295/r6340/r7477 (lane 6, whose "P3 Series bearing" reasons predicted exactly this landing) —
  4 add one-to-many rows beside standing alignments), 16 fresh non-overlaps **recorded by reference only**
  (`bodyImported: false` — the lane-8 candidate-model law) with the modulus-vs-surd-squaring and
  vector-norm boundaries argued per row, 30 of-record candidates rejected with reasons (the
  positive-integer binomial pool stays 1.6.1 of record; 3.1.6 is the rational-index `|x| < 1` expansion),
  primary picks absolutely / inequalities / whats-left / r6577 / r7792 / r7436 — recorded, never forced.

- **Lane 10 (CIE 9709 Pure 3 3.2 Logarithmic and exponential functions)** — `cie-a-level-maths-20-pure-3-logarithmic-and-exponential-functions.json`: the
  **second lane on the pure-3 course plane** and the first **dedicated-station lane** there
  (the exp-and-log station held only two of-record resources before this lane): 39 aligned rows
  (34 fresh rows over 34 new-text resources — all single-code — plus 5 cross-course fact joins to
  already-of-record bodies under `pure-1-functions/` (r9824 → 3.2.2, r7607 → 3.2.1),
  `pure-1-series/` (r6137 → 3.2.1, r8260 → 3.2.3) and `pure-1-trigonometry/` (r7184 → 3.2.1);
  all one-to-many beside standing alignments, no flips), 26 fresh non-overlaps **recorded by
  reference only** (`bodyImported: false`) — the no-e/ln exponential-graph family, the lane-7/8
  recorded P3 3.4/3.5 bearings standing, the no-extractable-text trio, the index-law pair and the
  timber-log sweep false positive — 6 of-record candidates rejected with reasons, primary picks
  proving-laws-of-logs / an-irrational-inequality / to-log-or-not-to-log / how-far-did-the-earth-move
  (the lane-9 `to-log-or-not-to-log` nonOverlapByReference row flips to aligned with a fresh body),
  and the 3.2.2 e/ln limb honestly thin (2 fresh + 1 join — UGM's e/ln corpus rides the lane-7/8
  recorded P3 differentiation/integration bearings) — recorded, never forced.

- **Lane 11 (CIE 9709 Pure 3 3.3 Trigonometry)** — `cie-a-level-maths-20-pure-3-trigonometry.json`: the
  **third lane on the pure-3 course plane** and the **first mostly-mapping lane** — the dedicated
  compound-angles station is whole-imported of record under lane 5, so the lane-5 pre-baked pool
  flips by reference: 28 aligned rows = 1 fresh row (r7616 → 3.3.1, the only new text) + 27
  cross-course rows riding `pure-1-trigonometry/` bodies (23 flips of lane-5 non_overlap rows +
  4 one-to-many beside standing alignments: going-round-in-circles, muddled-trig, trig-tables →
  3.3.1, r7021 → 3.3.2; no flips of pure-3 rows, nothing duplicated), 42 fresh non-overlaps
  **recorded by reference only** (`bodyImported: false`; 9 riding prior bodies per the supersede
  law) — 9 P3 3.4 Differentiation bearings, 9 P3 3.5 Integration bearings (incl. the sinx/sin2x
  pair whose 3.3.2∩3.5.2 mix is argued per row), 4 extended-sine-rule bearings, 14 beyond-spine,
  5 sweep false positives — 33 of-record candidates rejected with reasons (their prior alignments
  stand), primary picks r7616 (3.3.1, fresh) / r6018 (3.3.2 — rides a reference row, disclosed of
  record: no fresh 3.3.2 body exists because the dedicated station is whole-imported), the 3.3.2
  spine title's mid-sentence truncation carried verbatim of record — recorded, never forced.

- **Lane 12 (CIE 9709 Pure 3 3.4 Differentiation)** — `cie-a-level-maths-20-pure-3-differentiation.json`: the
  **fourth lane on the pure-3 course plane** and the **largest fresh-text lane since lane 9** — the
  differentiation substrate concentrates on the chain-rule and product-rule stations (neither whole-imported
  of record), so the lane-10/11 pre-baked "P3 3.4 Differentiation" bearing pool converts rather than maps:
  41 aligned rows = 40 fresh rows (13 × 3.4.1 / 12 × 3.4.2 / 15 × 3.4.3; 16 of them promotions of the bearing
  pool, each superseding its stale row of record) + 1 cross-course flip (r8931 → 3.4.2, riding its lane-7 body
  under `pure-1-differentiation/`), 29 fresh non-overlaps **recorded by reference only** (`bodyImported:
  false`; 3 honest re-routings of lane-10 bearings) — 7 further P3 3.5 Integration bearings, the
  inverse-function/arc-length/locus beyond-spec set, the discriminant-method false positives, and the
  P1-1.7-bearing kinematics/power-rule pair — 119 of-record candidates rejected with reasons (104 prior
  alignments — dominated by lane-7's P1-differentiation law — and 15 standing prior non-overlap rows, incl.
  the two declined bearings odd-one-out and r6843), primary picks r6938 (3.4.1, fresh) / r6530 (3.4.2, fresh)
  / r8620 (3.4.3, fresh), the 3.4 spine titles' parse artifacts (dropped math run on e, duplicated "tan x",
  dangling "e.g.") carried verbatim of record — recorded, never forced.

- **Lane 13 (CIE 9709 Pure 3 3.5 Integration)** — `cie-a-level-maths-20-pure-3-integration.json`: the **fifth lane
  on the pure-3 course plane** and the **first lane of record with an honest empty spec point** — the integration
  substrate concentrates on the calculus-trig-log, chain-rule and product-rule stations, so the lane-10/11/12
  pre-baked "P3 3.5 Integration" bearing pool converts or declines: 23 aligned rows = 16 fresh rows (15 of them
  promotions of the bearing pool, each superseding its stale row of record) + 1 cross-course flip (circular-slice
  → riding its lane-4 body under `pure-1-circular-measure/`) + 6 one-to-many joins beside standing alignments of
  record (r7616 → the lane-11 3.3.1 pick; r8774 → the lane-12 3.4.2 body, the bearing lane-12's own evidence
  disclosed; r9312 → the lane-6 1.6.4 body — the twice-by-parts envelope integral; r9701, r8694, r5126 → lane-9
  bodies), 11 fresh non-overlaps **recorded by reference only** (`bodyImported: false`; 5 superseding stale
  bearing rows — r6622, r7106, r7461, r7903, r8836 — each declined honestly against its solution of record) — 68
  of-record candidates rejected with reasons, **3.5.4 carries ZERO rows (the honest gap of record: no f′(x)/f(x)
  resource exists corpus-wide — recorded, never forced)**, primary picks r8679 (3.5.1, fresh) / r9297 (3.5.2,
  fresh) / r5126 (3.5.3 — rides its lane-9 body, disclosed of record) / r8134 (3.5.5, fresh) / r8890 (3.5.6,
  fresh), the 3.5 spine titles' parse artifacts (interleaved/dropped math runs, the 3.5.3 glyph debris) carried
  verbatim of record — recorded, never forced.

- **Lane 14 (CIE 9709 Pure 3 3.6 Numerical solution of equations)** —
  `cie-a-level-maths-20-pure-3-iteration.json`: the **sixth lane on the pure-3 course plane** — the iteration
  content is scattered by design (nine stations in scope), so the lane joins heavily: 11 aligned rows = 3 fresh
  rows (r8711 3.6.1, r8013 3.6.1, staircase-sequences 3.6.2+3.6.3) + 1 cross-course flip (r8404 → its lane-6
  body under `pure-1-series/`, `spec_points: []` unmapped-by-design — the circular-slice precedent) + 7
  one-to-many joins beside standing alignments of record (r8231 → 3.6.1/3.6.3; r8679 → 3.6.2/3.6.3 riding the
  lane-13 3.5.1 pick body; r7549, r5948 → 3.6.1; to-log-or-not-to-log, see-the-power, r9082 → 3.6.1 medium), 1
  fresh non-overlap **recorded by reference only** (staircase-sequences-revisited, the companion disclosure —
  convergents as approximations, representation is the aim), 36 of-record candidates rejected with reasons
  (the Newton's-LAWS noise class disposed by name). **No honest gap this lane**: 3.6.1 carries 8 rows, 3.6.2
  three, 3.6.3 four; primary picks r8711 (3.6.1, fresh) / r8404 (3.6.2 — rides its lane-6 body, the r6018
  fresh-pick-impossible convention disclosed) / r8231 (3.6.3 — rides its lane-3 body, disclosed).

- **Lane 15 (CIE 9709 Pure 3 3.7 Vectors)** —
  `cie-a-level-maths-20-pure-3-vectors.json`: the **seventh lane on the pure-3 course plane** and the first
  with zero cross-lane joins — a two-station lane of record (vector-geometry 15 fresh + combining-vectors 5
  fresh; the stations the spec names are the stations the corpus serves from). 20 aligned rows all fresh
  bodies; psp rows 29 = 2/11/5/3/4/4 across 3.7.1–3.7.6; 6 non-overlap companion disclosures (the plane class,
  r5089 vs the 3.7.7 exclusion row, r8828 vs the 3.7.5 common-perpendicular exclusion); 110 of-record
  candidates rejected with reasons. **The DESIGNED honest gap**: 3.7.7 — the spec's own exclusion row
  ('Knowledge of the vector product is not required.') — carries zero rows by rule (the second honest gap of
  record after 3.5.4, this time by design). r8456 PROMOTED (stale lane-3-algebra non-overlap superseded).
  Picks: hit-the-spot (3.7.1) / r8215 (3.7.2) / r9575 (3.7.3) / lots-of-vector-lines (3.7.4) / three-lines
  (3.7.5) / r6493 (3.7.6) — all riding fresh bodies.

- **Lane 16 (CIE 9709 Pure 3 3.8 Differential equations)** —
  `cie-a-level-maths-20-pure-3-differential-equations.json`: the **eighth lane on the pure-3 course plane** and
  the **ZERO-FRESH-BODY lane of record** — 2 aligned rows, both cross-lane joins riding of-record pure-1 bodies
  (r6959 under pure-1-differentiation 1.7.3; r7410 under pure-1-integration 1.8.2; the lane-6 one-to-many law);
  psp rows 0 = 0/0/0/0 (fresh-only counting — coverage rides the joins); 4 non-overlap companion disclosures
  (the modelling-recognition class picture-the-process-i/ii; the beyond-spec separable-DE machinery
  weight-pulling + from-parabolas-to-catenaries); 47 of-record candidates rejected with reasons.
  **THE CORPUS-BOUNDARY DISCLOSURE**: the UGM site's own differential-equations station is EMPTY (0 resources,
  created 2015-11-04, never populated — verified live; the station is one of the four never captured alongside
  the two complex-numbers stations and matrices) — the corpus poverty is the site's, disclosed not repaired.
  Picks: r6959 (3.8.1, 3.8.4) / r7410 (3.8.2, 3.8.3) — both riding joins, the r6018-style disclosure applies
  lane-wide.

- **Lane 17 (CIE 9709 Pure 3 3.9 Complex numbers)** —
  `cie-a-level-maths-20-pure-3-complex-numbers.json`: the **ninth and FINAL spine subtopic on the pure-3 course
  plane** and the **corpus-boundary lane of record** — **ZERO aligned rows (the first zero-aligned lane of
  record)**, zero fresh bodies, zero cross-lane joins; psp blocks 8 = 0/0/0/0/0/0/0/0 (all honest-empty, no
  picks); 1 non-overlap companion disclosure (absurder — the conjugate-pair factorisation `a²+b²=(a+ib)(a−ib)`
  derived from `i²=−1` as a solution aside; the lane-9 row stands) and 42 of-record candidates rejected with
  reasons carrying the six registers of record. **THE CORPUS-BOUNDARY DISCLOSURE, TOTAL**: the site's
  complex-numbers substrate was never published — complex-numbers-faces (id 8) and complex-numbers-plane (id 9)
  are post-freeze AcademicReview stations with ZERO public resources (live-verified with the vector-geometry 27
  control and the differential-equations 0 control; matrices id 17 likewise 0) — the 855/25 corpus of record is
  final. No coverage is manufactured (rule 3): the corpus poverty is the site's, disclosed not repaired.



- **Lane 18 (P2) — the CIE 9709 Pure 2 COURSE PLANE (T-UGM-P2-1)** — the **NEW COURSE PLANE of record** (operator order trace `1a188fcae3769975`, resolving the lane-17 pointer “further UGM lanes need a new course plane, operator's call”): the 2023-2025 Paper 2 spine 2.1.1-2.6.3 adjudicated against the syllabus PDF of record (sha1 `997e5a9f`) — **16/17 spec points are verbatim twins of Paper 3 codes** (9 spine-verbatim, 7 pdf-verbatim with the spine-parse divergence disclosed; `2.1.2` carries the spine's three-bullet merge of 3.1.2+3.1.3+3.1.4), and **`2.5.3` trapezium rule is P2-UNIQUE** (no Paper 3 bullet). Census: **166 cross-lane rows = 161 one-to-many twin joins + 5 trapezium flips (approximating-areas, r5642, r7903, r8140, underneath-the-arches — each routed “beyond spec” of record by the P1/P3 lanes, realized by the P2-unique bullet) + 2 standing-home joins (r6592, r7912)**; ALL 17 spec points carry rows — zero honest gaps; 1 depth-guard hold (integral-chasing-2 @ 2.5.1 — by-parts is Paper-3-only, the lane-8-style beyond-spec law applied in the P2 direction) and 1 capture-gap companion (r5324 — never forced, rule 3). Facts only; zero body text moves; no MANIFEST touch (zero corpus files added, the #55 sibling law). Cross-map `cross-map-p2-full-course.json` + the FIRST pure-2 spine export @ syllabai-experimental `08404b34`.

## Rights

UGM content © University of Cambridge; sourced exam questions © UCLES.
No licence for content reuse exists or is claimed. Takedown/correction:
open an issue on this repository; affected rows will be removed promptly.
