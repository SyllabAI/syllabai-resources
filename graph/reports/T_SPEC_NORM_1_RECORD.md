# T-SPEC-NORM-1 — Parsed Specifications Normalization + PDF-Fidelity Audit

Date: 2026-09-20 · Scope: `Official-Specifications/parsed/` (23 quals, canonical
7-file bundles + derived Layer-A graph YAMLs) · Trigger: operator request —
"Check the parsed specifications against their PDF versions and confirm one
definitive normalized format for the knowledge-graph visualizer."

## Audit method (independent, zero-LLM)

1. **Normalization matrix** (`scripts/t_spec_norm_audit.py`): per-qual checks —
   bundle completeness, spec_point field sets, id prefixes/uniqueness,
   provenance completeness, counts consistency, parse gates, v1↔canonical
   parity, derived YAML presence.
2. **PDF fidelity sweep** (`scripts/t_spec_norm_fidelity.py`): every spec point
   and every sub_item checked against its provenance page's PDF text layer
   (PyMuPDF, independent of the pdfplumber span-geometry parser) — strict
   contiguous match + ≥85% token-coverage fallback.
3. **Targeted forensic probes** (item truncation classifier, ial-maths
   column reconstruction self-validated against clean rows, layout-based
   cut-item detector, sha1 re-verification of all 23 parse products).

## Findings

| # | Finding | Quals | Disposition |
|---|---------|-------|-------------|
| F1 | 3 new quals missing `_derived/graph/` YAMLs (KG loader invisible) | ELA, maths-b, SDA-mod | **fixed** — emitted (T-SME-11 had registered them in FAMILY but never ran the emitter) |
| F2 | 3 new quals' parse_report.json lacked gates + sme_crossref (finalize_reports never run; canonical builder had overwritten the report with only `canonical_bundle`) | ELA, maths-b, SDA-mod | **fixed** — finalize_reports patched to preserve canonical_bundle + dynamic date; all 23 reports regenerated, gates ALL_PASS × 23 |
| F3 | `_summary.json` truncated to 1 row since T-PARSE-FIX-2 (single-qual re-parse overwrote the run log) | corpus | **fixed** — regenerated, 23 rows |
| F4 | SCHEMA.md stale ("20 quals", missing id shapes) | corpus | **fixed** — 23 quals + real id-shape table + normalization invariants section |
| F5 | `validate_parsed.py qual_of()` routed SDA-modular courses to the linear qual | corpus | **fixed** — routing + `_sme_crossref.json` regenerated (23 quals; SDA-mod 418 SME points, 78.8% verbatim) |
| F6 | SDA linear: 120 foreign assessment-bullet sub_items glued to `Physics-8.10` (runaway harvest from the p66 experimental-skills block; truncated mid-phrase) | igcse-science-double-award | **fixed** — cleared; item totals now 101 = modular sibling exactly |
| F7 | ial-maths: at-a-glance duplicate point `IAL_MATHS:6.5` (interleaved garbage text + 41 front-matter items; unit-content row is `IAL_MATHS:P4-6.5`) | ial-maths | **fixed** — deleted (v1 + canonical, orderings renumbered) |
| F8 | ial-maths: 191 rows had Content/Guidance columns line-interleaved (parser's full-width visual-line assembly); 13 rows carried runaway assessment-info bullets | ial-maths | **fixed**: 45 prose rows rebuilt column-sequentially (token-multiset verified); all band-verified `sub_items` set; **146 formula-dense rows carry the new `two-column-line-interleave` flag** (wording approximate — never silently guessed) |
| F9 | econ: runaway foreign items on `2.2.3d` (42) and `1.2.6d` (12); contaminated texts; cut bullet items across rows | igcse-economics | **fixed**: 2.2.3d + 1.2.6d surgical; 17 rows cell-rebuilt under a verbatim acceptance filter (19 applied incl. 1.1.1d/1.1.2b/1.2.3b/1.2.5e/1.2.5f/2.1.1a…) |
| F10 | business: cell-structure damage (4.3.4 flattened bullets, cut items) | igcse-business | **fixed** — 19 rows rebuilt under the same verbatim filter |
| F11 | ict `6.7.3` text tail contaminated by SAMs assessment table | igcse-ict | **fixed** — text = "Create and manage files and folder structures." |
| F12 | SDA modular flame-test/cation items missing satellite spaces (`Li+is red` vs linear convention `Li + is red`) | SDA-mod | **fixed** — 7 items renormalized to the linear sibling convention |
| F13 | false alarms, verified fine: chemistry superscript items (`Ag + , Cu 2+ …` = satellite convention), IAL science strict-misses (formula satellites), geography/accounting `SX.` assessment rows (by-design capture), equations.json two shapes (content-driven, documented) | — | documented in SCHEMA.md |

## Post-repair state (re-audited 2026-09-20)

- Normalization: all 4,278 spec points share one 13-field schema; schema
  string uniform; id prefixes valid; provenance complete; gates ALL_PASS ×23;
  derived graph YAMLs 23/23 (loader contract).
- PDF fidelity (token-coverage ≥85%): 100% on 14/23 quals; ≥95.9% on all;
  hard item misses eliminated everywhere except documented residuals
  (econ 13, business 2, further-maths 2, maths-a 7, maths-a-mod 10, maths-b 4
  — formula glyph-order artifacts of the PDF text layer + the Tier-2 rows below).
- sha1 integrity: 23/23 parse products match committed PDFs.

## Tier-2 backlog (recorded, not silently guessed)

- econ 17 + business 14 rows: rebuilds failed the strict verbatim acceptance
  filter (cut-item continuations / wrapped-code cells); left untouched —
  detector output in `scripts/t_spec_cutitem_scan_results.json`, row lists in
  `scripts/t_spec_rejected_foreign.json`.
- ial-maths 146 `two-column-line-interleave` rows: full column-sequential
  rebuild needs a parser-level fix in `parse_code_column_bands` line assembly
  (per-column grouping changes satellite-token spacing); requires operator
  review of wording changes — flagged in data meanwhile.
- accounting/geography `SX.` assessment rows: consider excluding from the
  spec-point node family in the KG visualizer (they are assessment-metadata
  rows, by-design captured).

## Files changed

- Repairs: v1 parsed.json + canonical spec_points.json for ial-maths,
  igcse-economics, igcse-business, igcse-ict, igcse-science-double-award,
  igcse-science-double-award-modular.
- Infra: `scripts/validate_parsed.py`, `scripts/finalize_reports.py`,
  `_sme_crossref.json`, `_summary.json`, `SCHEMA.md`.
- Derived: `_derived/graph/` — 3 new quals added, 4 quals re-emitted.
- Tooling + evidence committed: `scripts/t_spec_norm_audit.py`,
  `t_spec_norm_fidelity.py` + `t_spec_norm_fidelity_sweep.json`,
  `t_spec_ialmaths_rebuild3.py`, `t_spec_cell_rebuild.py`,
  `t_spec_apply_repairs.py`, `t_spec_cutitem_scan.py`,
  `t_spec_cutitem_scan_results.json`, `t_spec_rejected_foreign.json`.
- Verify: `sme_spcpt_verify` ALL GATES PASSED (49 courses, 27,865 parts).
