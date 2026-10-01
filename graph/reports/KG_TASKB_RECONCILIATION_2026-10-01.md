# KG Task B — resources-side kg_export reconciliation vs the golden sample

- **Task**: T-KG-B (the standing "task B" thread from the T-KG-2 closeout:
  *"exporter lives in demo repo — resources-side kg_export reconciliation vs
  golden sample still pending"*)
- **Date**: 2026-10-01
- **Owner**: superz (main agent, zai session web-98866c45)
- **Base**: syllabai-resources main @ `feb0e1c` (ratified store
  `graph/igcse-chemistry/`), syllabai-demo main @ `648e2ae` (golden sample
  `public/kg/data/canonicalKG.edexcel-chemistry-4ch1.json`)
- **Gate verdict**: **GREEN within the pinned ledger** —
  `python3 scripts/kg_export.py --verify-golden` exit 0

## 1. Executive summary

The resources ratified store can now regenerate the golden canonicalKG for
4CH1 end-to-end. A new corpus-derived exporter (`scripts/kg_export.py`)
projects `graph/igcse-chemistry/{topics,specification_points}.yaml` into the
GRAPH_CONTRACT v1.0 payload and reproduces the v75 golden sample **exactly**
on every corpus-provable dimension: all 215 hierarchy nodes match id-for-id,
label-for-label on 213/215, all 182 spec-point ids match, all 222 hierarchy
and assessment edges match as a set with **zero** resources-only surprises,
and 173/182 point statements are byte-exact. Every remaining difference is
classified, itemised, and pinned in a machine-checked acceptance ledger:
19 text-variant fields with two mechanical root causes (PDF-extraction
formula spacing; en-dash vs hyphen), 2 ExamPaper nodes whose display
metadata is presentation-layer (official assessment-table values, pinned
verbatim), and 35 golden-only curated pedagogy edges (30 `pre` + 5 `rel`)
that have **no resources-side source** and stay golden-side until the
operator decides otherwise. The gate fails closed: any future drift in the
store that is not added to the ledger turns it RED (proven by negative
tests).

This closes the asymmetry the T-KG-2 closeout reported: the demo exporter
regenerates the serving payload from demo content; the resources exporter
now proves the authoritative corpus behind it is golden-equivalent.

## 2. Sources and method

| Input | Role |
|---|---|
| `syllabai-demo/public/kg/data/canonicalKG.edexcel-chemistry-4ch1.json` | **Golden sample** — headless extraction of the v75 OpenHuman build's own `syncCanonicalKG()` (2026-09-21, build sha256 `65cc973e…`), 217 nodes / 257 edges |
| `graph/igcse-chemistry/topics.yaml` | ratified sections + subtopics (4 + 28) |
| `graph/igcse-chemistry/specification_points.yaml` | ratified 182 points (wording, bullets, subsection, applicability) |
| `graph/igcse-chemistry/relationships.yaml` | checked for point-level edges — contains **only** 210 `PART_OF` rows (hierarchy) |
| `Official-Specifications/parsed/_derived/graph/igcse-chemistry/` | PDF-direct lane — cross-checked via the in-repo `DIFF_VS_RATIFIED.json` (codes 182/182 equal, wording 182/182 identical normalized) |
| `syllabai-demo/content/igcse-chemistry-19/curriculum.json` | secondary triangulation lens (what the demo serving lane carries) |

Method: a read-only analysis pass (`kg-analysis`, this session) built the
resources projection in memory and diffed it against the golden sample
node-by-node and edge-by-edge; the exporter then implemented that projection
deterministically, and the acceptance ledger was generated **from the
observed evidence** (never hand-typed) so the gate pins exactly what the
reconciliation saw.

## 3. Node reconciliation — GREEN

Golden 217 nodes = 1 Subject + 4 Section + 28 SubTopic + 182
SpecificationPoint + 2 ExamPaper.

| Class | Result |
|---|---|
| Node id sets | 217/217 identical (exporter emits papers from the pinned constant — see §6) |
| Resources-only nodes | **0** |
| Section labels (4) | exact |
| SubTopic labels (28) | **26 exact, 2 dash-variants** (§5) |
| SpecificationPoint ids | 182/182 (`p:<official_code>` ↔ golden `pointId`) |
| Point statements (182) | **173 byte-exact, 9 formula-spacing variants** (§5) |
| Point `subtopic` fields | 174 exact, 8 cascade from the 2 dash-variant titles (§5) |

No golden node is unexplained and no resources node is unexpected. The
subject label (`Chemistry`) is display truth mirrored from the demo course
registry, documented in the exporter's `QUALS` constant.

## 4. Edge reconciliation — GREEN

Golden 257 edges vs exporter 222 edges.

| Kind | Golden | Exporter | Verdict |
|---|---|---|---|
| `hier` | 214 | 214 | **exact set match** (subject→4 sections, sections→28 subtopics, subtopics→182 points) |
| `assess` | 8 | 8 | **exact set match** (4 sections × paper1/paper2; paper ids derived from the applicability census on all 182 points) |
| `pre` | 30 | 0 | **golden-only curated** — no resources-side source (§7) |
| `rel` | 5 | 0 | **golden-only curated** — no resources-side source (§7) |
| resources-only | — | **0** | nothing invented |

Direction convention: golden `hier` is parent→child; the ratified store's
`PART_OF` is child→parent; the exporter inverts on projection. The exporter
deliberately does **not** synthesize `pre`/`rel` edges — the corpus
discipline forbids inventing edges, and 35 un-ratified pedagogy edges must
not enter the corpus through an exporter.

## 5. The 19 accepted text variants — two mechanical root causes

All 19 are pinned field-by-field (both sides verbatim) in
`graph/reports/KG_TASKB_GOLDEN_GATE.json → accepted_text_variants`. The
gate re-verifies each pinned pair on every run: if resources text changes
under a pinned key, or a pinned variant stops differing (i.e. a fix landed),
the gate goes RED and the ledger must be refreshed in the same change.

**Root cause A — PDF-extraction spacing inside chemical notation (9
statements).** The PDF-direct parse tokenizes sub/superscript runs with
spaces: `R f` (golden `Rf`), `dm 3` / `24 000 cm 3` (golden `dm3` /
`24 000 cm3`), `Ag + , Cu 2+` (golden `Ag+, Cu2+`), `Δ H` (golden `ΔH`),
`Q = m c Δ T` (golden `Q = mcΔT`), `C 60` (golden `C60`). Points affected:
`p:1.12`, `p:1.35C`, `p:1.38`, `p:1.50`, `p:2.46`, `p:2.47`, `p:2.48`,
`p:3.14C`, `p:3.3`. Same content, rendering variant of the same
OCR-vs-PDF family already catalogued in `chemistry-rediff.json` (53 known
rows) and the demo statement-diff review (71 rows). Not a content error.

**Root cause B — en-dash vs hyphen in two subtopic titles (2 labels, 8
cascades).** Golden `Group 1 (alkali metals) - lithium, sodium and
potassium` vs ratified `Group 1 (alkali metals) – lithium, sodium and
potassium` (same for `Group 7 (halogens)…`). The 8 cascading point
`subtopic` fields (`p:2.1`, `p:2.2`, `p:2.3`, `p:2.4C`, `p:2.5`, `p:2.6`,
`p:2.7`, `p:2.8C`) are the same two titles propagated onto their points —
fixing the two titles (operator decision: normalize to ASCII hyphen, or
accept the en-dash as canonical and re-pin) collapses all 10.

Triangulation context: the demo serving lane
(`content/igcse-chemistry-19/curriculum.json`) matches the golden statements
only **119 exact + 6 normalized of 182** — the ratified resources store
(173 exact) is measurably the *closest* textual source to the v75 golden.
The demo lane's remaining 57 variants belong to its own known rediff
lineage and are out of task-B scope.

## 6. Papers display metadata — presentation layer, pinned verbatim

The two golden ExamPaper nodes carry official assessment-table values:

- `paper1` — `Paper 1C · 110 marks`, `2 hour · 61.1%`
- `paper2` — `Paper 2C · 70 marks`, `1h 15m · 38.9%`

The parsed corpus does **not** capture the assessment-information table
rows (the PDF lane registers the `Assessment information` topic but has no
points under it), so these values are pinned verbatim in the exporter's
`PAPER_META` constant with their provenance documented in-file and in the
export's `meta.source.note`. Paper *identity* (which papers exist) is
corpus-derived — it falls out of the applicability census across all 182
points (`{1C, 2C}`) — and the exporter fails closed if the census ever
yields a paper the constant doesn't cover. Follow-up (operator-optional):
capture the assessment table into the parsed corpus, then derive §6 from
data and drop the constant.

## 7. Golden-only curated edges — operator decision required

The 35 point-level edges below exist only in the v75 hand-curated dataset.
The resources store has no equivalent (its `relationships.yaml` is
hierarchy-only, and the T-C11 concept web is concept-level: 0 edges with
both endpoints spec-point-like). They are **pinned as expected-golden-only**
in the ledger so their absence is auditable. The exporter will not adopt
them without a ratification decision.

**pre (30)** — reading `A→B` as "A is a prerequisite for B":
1.18→1.19; 1.19→1.22; 1.25→1.28; 1.27→1.28; 1.28→1.29; 1.37→1.39;
1.41→1.42; 1.41→1.43; 1.44→1.46; 1.45→1.47; 1.57C→1.58C; 1.15→1.17;
1.15→1.20; 1.29→1.31; 1.31→1.32; 1.35→1.36; 1.1→1.5C; 1.13→1.14C;
1.19C→1.20C; 1.6C→1.7C; 1.9→1.11; 1.19→1.20; 1.23→1.25; 1.23→1.27;
1.29C→1.31C; 1.29C→1.32C; 1.34C→1.36C; 1.39C→1.40C; 1.44→1.46; 1.7→1.8

**rel (5)** — relation pairs: 1.59C↔1.60C; 2.34↔2.37; 3.22C↔3.21C;
2.27↔2.28; 2.8↔2.9

Options for the operator:

1. **Ratify as a point-edge store** — commit them as
   `graph/igcse-chemistry/point_edges.yaml` (provenance: v75 hand-curated,
   operator-ratified import; not OCR-derived), teach the exporter to emit
   `pre`/`rel`, and drop the pin. The golden then matches 257/257.
2. **Accept the asymmetry** — keep them golden-side; the ledger documents
   the gap permanently. Serving stays hier+assess (demo exporter v1
   behaviour, already the production shape).
3. **Defer** to the T-C11 next-wave (119 HV edges pending the B2 data wave)
   — same substrate, one combined operator review.

## 8. The regression gate (new CI step)

- Exporter: `scripts/kg_export.py` (`--check-only` validates;
  default mode writes
  `graph/igcse-chemistry/_derived/canonicalKG.edexcel-chemistry-4ch1.json`
  with its own honest lineage meta — it is a corpus projection, not a
  pretend v75 extraction).
- Fixture: `graph/igcse-chemistry/_golden/canonicalKG.edexcel-chemistry-4ch1.json`
  (vendored byte-copy of the demo golden, sha256
  `11eb7aa5…21ba0aaf`, re-hashed by the gate every run; see `_golden/README.md`).
- Ledger: `graph/reports/KG_TASKB_GOLDEN_GATE.json` — pinned counts, the 35
  curated triples, and the 19 verbatim variant pairs.
- CI: `.github/workflows/scripts-tests.yml` gains one step,
  `python3 scripts/kg_export.py --verify-golden` (paths filter already
  covers `scripts/**` + `graph/**`).
- Failure modes (all proven by negative tests in this session): unaccepted
  field diff → RED; pinned-variant pair drift → RED; fixture sha drift →
  RED; resources-only node/edge (invention) → RED; pinned variant that
  stopped differing (stale ledger after a fix) → RED.

## 9. Claims

- **VERIFIED**: node/edge parity figures in §3–§4 (mechanically diffed,
  evidence JSON emitted); gate GREEN in sandbox + negative tests RED as
  designed; the 19 variants and 35 curated edges are pinned verbatim from
  observed values; relationships.yaml + concept_edges.yaml + parsed corpus
  exhaustively checked for a pre/rel source (none exists).
- **REPORTED**: the PDF-lane `DIFF_VS_RATIFIED.json` (in-repo) corroborates
  ratified-vs-PDF-direct wording equality; not re-derived here.
- **UNVERIFIED**: nothing in the gate path; the operator decision on §7 is
  by definition open.

## 10. Next safe actions

1. Operator decision on the 35 curated edges (§7 options 1–3).
2. Optional: normalize the two en-dash titles (§5 root cause B) — collapses
   10 of the 19 pinned variants after a ledger refresh.
3. Optional: capture the assessment-information table into the parsed
   corpus (§6) — removes the last non-corpus input from the exporter.
4. When the golden is re-extracted from a newer visualizer build: re-vendor
   the fixture + refresh the ledger in one change (gate enforces the pair).
