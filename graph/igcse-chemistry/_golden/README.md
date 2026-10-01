# _golden/ — vendored golden-sample regression fixture

`canonicalKG.edexcel-chemistry-4ch1.json` is the pinned golden sample for the
resources-side KG export regression (`scripts/kg_export.py --verify-golden`).

## Provenance (verbatim from the artifact's own meta block)

- extracted: 2026-09-21T07:33:38+00:00 by syllabai-demo
  `scripts/extract_canonical_kg.py` — a headless Playwright read of the v75
  OpenHuman build's own `syncCanonicalKG()` output, validated against the
  build's GRAPH_CONTRACT v1.0 rules
- source build: `syllabai-openhuman-edexcel-chemistry-v75-explainer-lasso-minimap.html`,
  sha256 `65cc973e7ea827c1211cd2e76a7f1075a27a45660224c38f72a5efc8d0a1e960`
- counts: 217 nodes (1 Subject / 4 Section / 28 SubTopic / 182
  SpecificationPoint / 2 ExamPaper), 257 edges (hier 214 / pre 30 / rel 5 /
  assess 8)
- fixture sha256 (this vendored copy):
  `11eb7aa571c34aaba600c2f6688c09d1631c67c9f0bad00be6f4bec421ba0aaf`
  (pinned again in `graph/reports/KG_TASKB_GOLDEN_GATE.json`; the gate
  re-hashes the file on every run)

## Why vendored in resources

The task-B integration plan (demo repo
`docs/KNOWLEDGE_GRAPH_VISUALIZER_INTEGRATION.md`, Phase 2) calls for a
golden-sample regression living in the resources lane. The authoritative
copy of the artifact is served by the demo repo at
`public/kg/data/canonicalKG.edexcel-chemistry-4ch1.json`; this fixture is a
byte-identical vendored copy so the gate runs hermetically in resources CI
(no cross-repo fetch). If the demo-side golden is ever re-extracted from a
newer build, re-vendor the file AND refresh the pinned ledger
(`KG_TASKB_GOLDEN_GATE.json`) in the same change — the gate fails closed on
any sha drift between the two.

## Read-only

Never hand-edit the fixture. It is an extraction of an external build, not
corpus data; corrections belong to the corpus and the exporter, and gate
expectations belong to the pinned ledger.
