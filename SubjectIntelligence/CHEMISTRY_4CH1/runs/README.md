# runs/ — run records of record (SIB-GEN receipts)

Each `SIB-CHEMISTRY_4CH1-RUN-*` directory is the committed receipt of record for one
SIB-GEN generation or remediation pass (`../pipeline/`, docs/PIPELINE.md §3):

- `run_manifest.json` — the run receipt: provider triple, source-revision pins
  (syllabai-resources / syllabai-pastpapers / syllabai), per-artifact records
  (evidence-pack id + sha256, artifact sha256, outcome, layered gates), and the
  run-level disclosures.
- `preflight/` — the source-resolution report and the per-family primary-coverage
  gate state.
- `evidence/<ARTIFACT>/` — the curated evidence pack grounding that artifact:
  `pack_spec.json` (the agent-authored extraction plan, committed), `evidence_pack.json`
  (the materialized bounded excerpts), `evidence_pack.sha256` (the pack digest).
- `bodies/` + `staged/` — the authored bodies and the stamped pre-deploy copies.
- `census.json` — the per-artifact pack/artifact census annex.
- `evidence_claim_qa_report.json` — the citation-binding QA result (r4 grammar).

Publication status: run records, packs and digests have been IN-REPO by design since
RUN-001 (verified of record at BL-011 / RUN-011, closing remediation item 7 of the
external-review queue). The per-artifact validator receipts live at the library root
(`../qa-reports/<ARTIFACT>.qa.json`). Nothing here constitutes artifact publication:
`staged/` and `published/` moves remain operator-ordered under the validator
publication law.
