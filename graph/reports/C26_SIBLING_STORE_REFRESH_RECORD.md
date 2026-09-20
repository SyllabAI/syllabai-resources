# C26 sibling-store refresh record — 2026-09-20

Operator directive (2026-09-20): execute T-C26 — refresh the five sibling stores from the
canonical PDF-direct parse (same wording authority as the C23 definitive swap), keep all
ratified enrichments, retire the OCR lineage from their meta blocks. Operator-delegate
review authority applied at the Phase-2 adjudication gate (standing delegation).

- Round spec (v1.0 proposal, v1.1 as-run): `C26_SIBLING_STORE_PDF_REFRESH_SPEC.md`
- Full change ledger: `C26_WORDING_DIFF_LEDGER.json` (12 wording changes, 1 identity
  change, 15 field adoptions, 13 flag resolutions — every change evidence-carrying)
- Emitter: `scripts/c26_emit_definitive_sibling_stores.py` (deterministic; idempotent —
  baseline is always `git show HEAD:`; byte-identical re-runs including the ledger)
- Battery: `scripts/c26_postcheck.py` — ALL PASS 8/8
- Field map freeze: `scripts/c26_field_map.yaml`

## Headline results

1. **All five stores now carry the PDF-direct lineage**: `statement_text_policy`,
   `source_documents` (official PDF sha1 `3ad641b7…` + canonical JSONs, builder
   canonical-builder-2.0), `generator`, `definitive_lineage` (with retired OCR lineage).
   No `md OCR` string remains anywhere in `graph/*.yaml`.
2. **12 wording changes**, all verbatim-sourced: 6 practical summaries (4 spacing repairs
   of the `lost-space` class, e.g. `combustion(e.g.magnesium oxide)` → `combustion (e.g.
   magnesium oxide)`; 2 truncation repairs below), 6 command-word definitions (bullets,
   curly apostrophe, en-dash, spacing). 1 identity change: `What,Why,Which` →
   `What, Why, Which`.
3. **Two truncation-damage finds (new damage class — invisible to character sweeps):**
   - `4CH1-PR-09`: old store truncated mid-bullet (`…displacement reacti`); canonical parse
     ALSO truncated (bullet-colon class) → full text restored from PDF p27 verbatim.
   - `4CH1-PR-10`: old store truncated mid-word (`…between marbl`) → canonical
     PDF-direct text adopted (p28 spot-check).
4. **AO2 `ao-range-dash-missing` resolved with proof**: PDF p35 Total row renders `38–42%`
   for AO2 and column arithmetic confirms (23.2–25.7 + 14.8–16.3 = 38.0–42.0); value set to
   `38–42%`. En-dash verbatim adopted across all 15 weighting fields (canonical
   `unit_weightings`).
5. **13 damage flags resolved, 0 added** — all five classes cleared with recorded evidence.
6. **Referential integrity**: 214/214 relationship endpoints resolve; 28/28 subtopic
   `spec_points` refs resolve against the definitive store. Counts preserved everywhere
   (4/28, 12, 3+2, 25, 210).

## Deliberately untouched

- Papers block (marks/duration/weighting): no canonical source → provenance-marked
  `ratified-overlay`.
- `category` (command words), `title_md` (topics), all codes/orderings/confidence/version.
- `concepts.yaml`, `concept_edges.yaml`, `specification_points.yaml`, `_derived/**`.

## sha256 pins

| File | Pre (HEAD before C26) | Post |
|---|---|---|
| `graph/topics.yaml` | `a7b14cbdd34bb9fe…` | `81a4745760bcce2c…` |
| `graph/practicals.yaml` | `e53e5f87606a2b5a…` | `8e0ab9c471937688…` |
| `graph/assessment_objectives.yaml` | `c112fc356445d4e4…` | `36f361ec8afa3dcc…` |
| `graph/command_words.yaml` | `322911acc82a6e68…` | `824c50ee0625672c…` |
| `graph/relationships.yaml` | `b3b7529222d77d80…` | `6bd3f8236ac2120a…` |
| `graph/reports/C26_WORDING_DIFF_LEDGER.json` | — (new) | `b3334f6057ea649a…` |
| `scripts/c26_emit_definitive_sibling_stores.py` | — (new) | `c4ad56a19789cc4d…` |
| `scripts/c26_postcheck.py` | — (new) | `b309c07b087792ac…` |
| `scripts/c26_field_map.yaml` | — (new) | `fbbd8836a75d67dd…` |

Reference (untouched): `specification_points.yaml` = `956d276f…` (C25 post-pin, unchanged);
`concepts.yaml` = `634a743b…`; `concept_edges.yaml` = `ccc674cf…`.

## C25 open-item closure

C25 (`9ea8d113`) §3 documented the five sibling stores as the remaining OCR-lineage item.
This round closes it; per record immutability the closure is recorded here. `graph/` now has
**zero** stores deriving wording from the retired OCR md.

## Scope guards honored

Node states byte-untouched (pins above); no surface changes; 2012-Jan escalations and the
data bridge not approached; R1 chemistry-only; battery check 6 proves the working tree
contains no unintended changes.
