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

## Rights

UGM content © University of Cambridge; sourced exam questions © UCLES.
No licence for content reuse exists or is claimed. Takedown/correction:
open an issue on this repository; affected rows will be removed promptly.
