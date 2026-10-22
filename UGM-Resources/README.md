# UGM-Resources — Underground Mathematics resource text corpus

Text bodies of the [Underground Mathematics](https://undergroundmathematics.org/)
resources, imported into the SyllabAI resource corpus. Underground Mathematics was a
University of Cambridge (Cambridge Mathematics / DfE-funded) A-level mathematics
project; the site has been frozen since ~2016 and is no longer updated, so this is a
preservation-grade snapshot of a stable source.

**Status:** first lane — `pure-1-quadratics/` (59 resources). Built 2026-10-23 as task
**`T-UGM-IMPORT-1`**. Sibling domain: `UGM-Enrichment/` (facts-only spec enrichment,
task `T-UGM-MODE1-1`, [syllabai-resources#55](https://github.com/SyllabAI/syllabai-resources/pull/55))
— that domain carries slugs/titles/types/levels/relations; this corpus adds the text
bodies.

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
