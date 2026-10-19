# C23 definitive swap record — 2026-09-19

Operator directive (2026-09-19): make the Official-Specifications PDF-direct-parse the
**definitive** specification-point source; copy all ratified enrichments from the old
store; retire the OCR lineage.

- Definitive wording: `international-gcse-chemistry-2017-specification.pdf` via canonical-builder-2.0 (`spec_points.json`,
  gates ALL_PASS, sha1 `3ad641b7c60b…`), zero-LLM span-geometry provenance per record.
- Retired: `international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md` + `scripts/c09_spec_graph_extract.py` (2026-09-10 OCR lineage).
- Records: 182; wording refreshed from PDF: **71**;
  bullet fields added (PDF sub_items): **22**.
- Subsections: OLD ratified values kept everywhere; **74**
  canonical disagreements, **all proven impossible by span geometry** (statement above header).
- Leading verb: **12** canonical `'practical:'` artifacts
  fell back to the ratified command verb.
- Applicability rule text: **182** updated to the
  per-record PDF rule (papers/shared structurally identical 182/182).
- Damage flags: **64** resolved
  by the verbatim wording; kept: {'4.30C': ['possible-superscript-loss']}.
- Quote re-anchors: **12** (6 node + 6 edge; details in the JSON record);
  originals preserved verbatim in this record. Final emission applied the
  re-anchor map inside `c11_concept_pilot.py` so frozen decision records stay
  untouched while the emitted graph carries definitive anchors.
- Colon exceptions: ['4.49C'].

Full per-record detail: `C23_DEFINITIVE_SWAP_RECORD.json`.
