# UGM-Resources — Underground Mathematics resource text corpus

Text bodies of the [Underground Mathematics](https://undergroundmathematics.org/)
resources, imported into the SyllabAI resource corpus. Underground Mathematics was a
University of Cambridge (Cambridge Mathematics / DfE-funded) A-level mathematics
project; the site has been frozen since ~2016 and is no longer updated, so this is a
preservation-grade snapshot of a stable source.

**Status:** eight lanes of record.

- **Lane 1 — `pure-1-quadratics/`** (59 resources, task **`T-UGM-IMPORT-1`**,
  landed via [syllabai-resources#58](https://github.com/SyllabAI/syllabai-resources/pull/58)).
  Sibling facts file: `UGM-Enrichment/cie-a-level-maths-20-pure-1-quadratics.json`
  (task `T-UGM-MODE1-1`, [syllabai-resources#55](https://github.com/SyllabAI/syllabai-resources/pull/55)).
- **Lane 2 — `pure-1-functions/`** (38 resources of the UGM *Combining Functions*
  station, task **`T-UGM-IMPORT-2`**). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-functions.json` (task
  **`T-UGM-MODE1-2`**). Cross-map of record: `cross-map-functions.json` in
  `SyllabAI/syllabai-experimental` (27/38 aligned to CIE 9709 P1 1.2.1–1.2.5;
  11 honest non-overlaps incl. 2 interactive-only pages whose bodies of record
  are honest empty states).
- **Lane 3 — `pure-1-coordinate-geometry/`** (85 resources of the UGM *Geometry of Equations* +
  *Circles* stations — the first two-station lane, task **`T-UGM-IMPORT-3`**). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-coordinate-geometry.json` (task **`T-UGM-MODE1-3`**).
  Cross-map of record: `cross-map-coordinate-geometry.json` in `SyllabAI/syllabai-experimental`
  (61/85 aligned to CIE 9709 P1 1.3.1–1.3.2 with spine fragments 1.3.1a/1.3.2a folded of record;
  24 honest non-overlaps — the circles station's radian-mensuration/theorem strands serve other lanes).
- **Lane 4 — `pure-1-circular-measure/`** (5 resources — the **first strand lane**, task
  **`T-UGM-IMPORT-4`**). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-circular-measure.json` (task **`T-UGM-MODE1-4`**).
  Cross-map of record: `cross-map-circular-measure.json` in `SyllabAI/syllabai-experimental`
  (CIE 9709 P1 1.4 Circular measure — hub parse fragment 1.4.1a folded into 1.4.1 of record; 62
  corpus-sweep candidates resolved as 17 aligned (3 new-text here + 14 cross-lane circles-strand
  facts) + 4 non-overlaps + 41 routed to recorded homes. The corpus importer's cross-lane `ugmId`
  uniqueness law keeps one text body per resource, so the circles strand's 14 alignments + 2
  non-overlaps are recorded as facts pointing at `pure-1-coordinate-geometry/` rather than
  duplicating bodies).
- **Lane 5 — `pure-1-trigonometry/`** (77 resources — the **two-station lane**, task
  **`T-UGM-IMPORT-5`**: the WHOLE substrate ships as text of record — 41 mapped (36
  Triangles-to-Functions + 3 Compound-Angles + 2 cross-station strays r7912/r7184) + 36 recorded
  non-overlaps imported unmapped). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-trigonometry.json` (task **`T-UGM-MODE1-5`**).
  Cross-map of record: `cross-map-trigonometry.json` in `SyllabAI/syllabai-experimental`
  (CIE 9709 P1 1.5 Trigonometry — five spine rows 1.5.1–1.5.5, no fold fragments; 299
  corpus-sweep candidates resolved as 41 aligned (55 alignment rows) + 36 non-overlaps + 2
  cross-lane fact joins (r9924/r8411 → 1.5.4 against lane-2 bodies, recorded with
  `textOfRecordUnder` pointers) + 220 routed to recorded homes. Finding of record: UGM's
  Trigonometry: Compound Angles station maps almost entirely to P3 2.3 (24 recorded
  non-overlaps) — the 2019 CIE revision moved compound/double-angle work out of Pure 1).
- **Lane 6 — `pure-1-series/`** (99 resources — the **second two-station lane**, task
  **`T-UGM-IMPORT-6`**: the WHOLE substrate ships as text of record — 49 mapped (43
  Sequences/Counting-and-Binomials substrate + 6 cross-station strays r5640/r9404/r9916/r8260/r6592/r9312)
  + 50 recorded non-overlaps imported unmapped). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-series.json` (task **`T-UGM-MODE1-6`**).
  Cross-map of record: `cross-map-series.json` in `SyllabAI/syllabai-experimental`
  (CIE 9709 P1 1.6 Series — four spine rows 1.6.1–1.6.4, no fold fragments; 137
  corpus-sweep candidates resolved as 49 aligned (56 alignment rows) + 50 non-overlaps + 2
  cross-lane fact joins (r7553/r9527 → 1.6.3 against lane-2 bodies, recorded with
  `textOfRecordUnder` pointers) + 36 routed to recorded homes. Findings of record: the
  Sequences station maps 31/42 onto 1.6.2–1.6.4 while Counting and Binomials is dominated
  by combinatorics/logic (39 recorded non-overlaps) around a tight binomial-expansion core
  (12/51); the general-index binomial questions carry P3 Series bearings — the natural
  substrate preview for a future P3 lane, mirroring lane 5's P3 2.3 finding).
- **Lane 7 — `pure-1-differentiation/`** (106 resources — the **third two-station lane**, task
  **`T-UGM-IMPORT-7`**: the WHOLE substrate ships as text of record — 72 new-text resources
  (24 Introducing-Calculus + 48 Calculus-of-Powers; 3 already of record via lanes 5–6 excluded) —
  40 mapped + 32 recorded non-overlaps imported unmapped, plus 34 mapped cross-station strays whose
  tested skill is 1.7.x). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-differentiation.json` (task **`T-UGM-MODE1-7`**).
  Cross-map of record: `cross-map-differentiation.json` in `SyllabAI/syllabai-experimental`
  (CIE 9709 P1 1.7 Differentiation — four spine rows 1.7.1–1.7.4, no fold fragments; 195
  corpus-sweep candidates resolved as 74 aligned (107 alignment rows) + 32 non-overlaps + 3
  cross-lane fact joins (r5640 vs lane 6; r7115, r8936 vs lane 4 — recorded with
  `textOfRecordUnder` pointers, the lane-4 non-overlap row for r7115 explicitly names 1.7 as the
  tested skill) + 86 routed to recorded homes. Findings of record: Calculus of Powers is the P1
  workhorse (31/48 aligned — power rule, tangents/normals, stationary points, canonical
  optimisations) while Introducing Calculus splits between gradient-concept building blocks and
  the honest trapezium-rule/kinematics non-overlap cluster (15); the chain-rule, product-rule and
  calculus-trig-log stations are P3-bearing (general chain rule, product/quotient rule, trig/exp/log
  derivatives, parametric and implicit differentiation) and are routed with bearings named — the
  natural substrate preview for future P3 lanes, mirroring lanes 5–6's P3 findings).
- **Lane 8 — `pure-1-integration/`** (10 resources — the **first strand lane on a spec section**, task
  **`T-UGM-IMPORT-8`**). Sibling facts file:
  `UGM-Enrichment/cie-a-level-maths-20-pure-1-integration.json` (task **`T-UGM-MODE1-8`**).
  Cross-map of record: `cross-map-integration.json` in `SyllabAI/syllabai-experimental`
  (CIE 9709 P1 1.8 Integration — the lane that closes the Pure 1 spine; 91 corpus-sweep candidates
  resolved as 28 aligned (10 new-text here + 18 cross-lane joins — 13 of them flipping the lane-7
  Calculus-of-Powers non-overlaps of record, the integration-dressed honesty deferred from lane 7)
  + 32 routed + 31 rejected with reasons. UGM has no dedicated integration station: the two dedicated
  calculus stations were already fully of record via lanes 5–7, so this lane imports new text only and
  records its cross-lane 1.8 mappings as facts pointing at `pure-1-differentiation/`).

`UGM-Enrichment/` carries slugs/titles/types/levels/relations; this corpus adds
the text bodies. `MANIFEST.json` is **v7 (multi-lane)** — one block per lane;
lane-1/2/3/4/5/6 rows carried forward untouched from v6.

## Rights and licensing authority

- **Rights holder:** © University of Cambridge (Underground Mathematics); sourced
  exam questions © UCLES. Every file repeats this in front-matter (`rights:`).
- **Licensing authority of record:** **operator attestation of 2026-10-23** —
  [`LICENSE-DATA.md`](../LICENSE-DATA.md) (Amendment 2026-10-23) records the
  attestation verbatim, its scope (the downloaded UGM text), and the
  takedown / correction procedure. This landing follows exactly the path the
  `UGM-Enrichment/` README anticipated: a text of record arrives as its own
  LICENSE-DATA.md amendment first.
- **Capture:** P2 full-site crawl captured 2026-10-22, held of record in
  `SyllabAI/syllabai-experimental` → `undergroundmathematics/` (crawl + `ugm-clean`
  extraction + relation graph). Import is **text-only**: images, PDFs and GeoGebra
  components are *not* fetched. Where a body references a non-text component, the
  body carries a bracketed reference line and front-matter records the full path
  (`assets:` / `interactive:`) — nothing is lost of record and a later image phase
  can resolve them without re-crawling.
- **Identity:** `MANIFEST.json` carries a SHA-256 per file plus source URL and
  capture date (machine-checkable provenance, per the repo's provenance law).

## Layout and hierarchy

The repo's retrieval hierarchy (Board → Qualification → Subject → CurriculumVersion →
Section → Topic → SpecificationPoint → Resource) is expressed as: directory = the UGM
station (the provider's own topic structure, tier `PROVIDER`); spec-point mapping =
front-matter (`spec_map`); resource = one file each.

```text
UGM-Resources/
  README.md                  — this charter
  MANIFEST.json              — sha256 identity + per-file metadata
  pure-1-quadratics/         — UGM station "quadratics" ↔ CIE 9709 Pure Mathematics 1
    r6638-can-we-find-both-roots-if-one-is-double-the-other.md
    name-that-graph-name-that-graph.md
    ...
  pure-1-functions/          — UGM station "combining-functions" ↔ CIE 9709 Pure Mathematics 1, subtopic 1.2
    r9527-can-we-compose-two-simple-functions.md
    invertibles-invertibles.md
    ...
```

One file per UGM resource, named `<ugm_id>-<slugified-title>.md`. The UGM native
section structure (Question / Suggestion / Solution / Problem / Warm-up / Taking it
further / teacher-support panels…) is preserved as `##` sections in source order,
including the provider's own spelling (e.g. "Opportunites for learning" is kept as
captured — provider fidelity, not a typo to fix).

## Front-matter law

Follows the corpus reference family (`Chemistry IGCSE Revision Notes/`):

- `source` — canonical UGM resource URL.
- `author`, `rights` — attribution + licensing authority of record.
- `resource_identity` — `ugm_id` (e.g. `r6638`), station, resource type (+ id),
  level, `ref`, `old_site_id` (pre-2012 site id, when present).
- `spec_map` — target lane `CIE-9709-P1-2023` (`cie-a-level-maths-20-pure-1`), the
  UGM subsection with provider provenance, and per-spec-point entries. **All mappings
  are `tier: AI_SUGGESTED` / `validation_status: SUGGESTED`** — they carry the P3c
  cross-map evidence and per-row confidence but are NOT human-validated until the
  review/promotion gate accepts them (AGENT.md rule 2). Spec points whose row the
  cross-map judged the best entry carry `primaryPick: true`, cross-referenced from
  the `UGM-Enrichment/` facts of record. Resources the cross-map did not align carry
  an empty `spec_points` list plus a `coverage_note` (coverage is never manufactured
  — AGENT.md rule 3). Cross-map of record:
  `syllabai-experimental → undergroundmathematics/resources/derived/cross-map-quadratics.json`
  (P3c pilot: 56/59 aligned, threshold 70% met).
- `provenance` — capture date/tool and, where the cross-map recovered it, the
  original **exam reference** (e.g. `UCLES 1985 Q1`) carried by the UGM resource.
- `assets` / `interactive` — non-text component paths recorded of record.
- `task` — the landing task id (`T-UGM-IMPORT-1`).

## Body conventions

- **Mathematics is preserved byte-true** in UGM's native delimiters: `\( ... \)`
  inline and `\[ ... \]` display (KaTeX/MathJax-compatible). A build-time audit
  verified delimiter parity: 6,434 in the extraction, 6,434 in this corpus, with
  zero files differing.
- Collapsible-panel titles (UGM's toggle buttons, e.g. "Alternative Solution",
  "Form (1)", "Common issues and misconceptions") are rendered as bold label lines;
  their panel bodies follow as ordinary text.
- Tables render as markdown tables (UGM multiplication grids and Venn-layout tables
  survive as readable grids).
- Figures/GeoGebra: bracketed reference lines with the source path — see Rights
  above.
- Where a resource's question stem was extracted into the question well and was not
  among the crawled sections, it is prepended as the `## Question` section
  (2 files; noted in front-matter `import_note`).

## Counts (this lane)

- 59 resources: 41 review questions, 8 packages of problems, 3 fluency exercises,
  2 food-for-thought, and one each of resource-in-action, bigger-picture,
  scaffolded-task, rich-example, building-blocks.
- Levels: Developing ×17, Introducing ×1, unlevelled ×41.
- 57 asset references and 24 interactive embeds recorded (not fetched).
- Spec-point coverage (SUGGESTED): 1.1.1 ×8, 1.1.2 ×12, 1.1.3 ×20, 1.1.4 ×10,
  1.1.5 ×11; 3 resources honestly unmapped (`parabella`, `parabolic-mirrors`,
  `r6864`).
- 5 primary picks of record: 1.1.1 `name-that-graph`, 1.1.2 `discriminating`,
  1.1.3 `quad-solving-sorter`, 1.1.4 `r7328`, 1.1.5 `r6215`.

## Extension lanes

Later lanes (other UGM stations ↔ other spine exports) follow the same layout: one
directory per station, one file per resource, `spec_map` pointing at the lane's
cross-map of record. The station → lane binding used here is recorded in
`MANIFEST.json → cross_map_of_record`.
A **strand lane** (lane 4, CIE 1.4 Circular measure) relaxes the station↔directory binding: its
directory carries only resources whose text is not already of record in another lane, while the
strand's cross-lane mappings live as facts in the sibling `UGM-Enrichment/` file with
`textOfRecordUnder` pointers. Station provenance stays first-class: every file's front-matter
records its UGM station regardless of which lane directory holds it.

A **two-station lane** (lane 5, CIE 1.5 Trigonometry) binds one lane to TWO UGM stations
(Trigonometry: Triangles to Functions + Trigonometry: Compound Angles, lanes 1–3 shape), plus
cross-station strays whose tested skill is the lane's spec points (r7912 from Introducing
Calculus, r7184 from Exponentials & Logarithms — station provenance stays first-class in
front-matter). A station may also map mostly OUTSIDE its lane's spine subtopic: the
compound-angles station's 24 non-overlaps are recorded with their P3 2.3 homes rather than
forced into 1.5.x.


A **strand lane on a spec section** (lane 8, CIE 1.8 Integration) applies the lane-4 relaxion to a
subtopic with no dedicated UGM station: the seven-station calculus family was already fully of record
via lanes 5–7, so the directory carries only the 10 new-text resources whose tested skill is 1.8.x,
while the 18 cross-lane alignments live as facts in the sibling enrichment with `textOfRecordUnder`
pointers at `pure-1-differentiation/`. Station provenance stays first-class in front-matter.
