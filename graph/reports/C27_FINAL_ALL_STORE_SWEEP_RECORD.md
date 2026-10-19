# C27 — Final All-Store Integrity Sweep + Residual Repairs (Closing Record)

- **Head at sweep**: `7ca311a` (T-SPEC-NORM-1 fast-forwarded over the C26 landing `b4e4d91` before sweeping — the normalisation lane did not touch `graph/` igcse-chemistry stores; verified via `git diff --name-only b4e4d91 7ca311a -- graph/` = its own record file only)
- **Trigger**: operator directive — "do a final all-store integrity sweep"
- **Battery**: `scripts/c27_final_all_store_sweep.py` (S0–S7, 85 gates + 7 informational lines), repairs `scripts/c27_repair_ao_weighting_matrix.py`, `scripts/c27_repair_chunkmap_sp_titles.py`
- **Verdict**: **ALL STORES CLEAN** after the two residual repairs below; every store in `graph/` now derives wording from the definitive PDF-direct lineage

## 1. Sweep scope and result

| Section | Coverage | Result |
|---|---|---|
| S0 | HEAD == origin/main, tree clean | PASS (post-landing; pre-landing dirty = the repairs themselves) |
| S1 | 10 `graph/` stores: parse, damage-class scan (CJK / kana / CJK-punct / fullwidth / U+FFFD / `\uXXXX` / control / inline-math / mojibake), meta & lineage audit | PASS — 0 damage hits; 0 "md OCR" residue; no store names retired `c09` as generator; spec_points policy line + PDF sha1 + `retired_lineage` intact |
| S2 | Counts + canonical equality vs `parsed/igcse-chemistry/` | PASS — spec_points 182/182 wording-equal (whitespace-normalised), 52 c-points; topics 4 + 28 subtopics 1:1; practicals 12 (label-prefix rule + ledger exceptions); AO 3 + papers 2 (ratified overlay); command words 25 punctuation-insensitive, diff ⊆ C26 ledger |
| S3 | Reference integrity | PASS — relationships 210 edges / 214 distinct endpoints 0 unresolved; subtopic→spec 182 refs; chunk-maps 211 codes + 210 mapped quotes; command kinds 82 verbs known; concepts 117 refs / 113 nodes; concept_edges 275 edges 0 unresolved |
| S4 | sha256 pins (C25 + C26 + C27) | PASS — 15/15 |
| S5 | `_derived/graph` 23 quals × 4 files | PASS — KG-loader contract 92/92, parse clean, 0 damage, 0 "md OCR", 4,274 point rows |
| S6 | `parsed/` canonical battery | PASS — 23 bundles, parse_reports 23/23 all-gates-pass, canonical JSON parse clean, official PDF sha1 `3ad641b7…` unchanged |
| S7 | Knowledge-graph HTML freshness | PASS — **v77 is the latest** (tracked on FileUpload origin/main `b975298`, local clone == remote, download copy byte-identical) |

Informational (documented, no action): 210/210 relationship edges carry per-edge provenance citing the retired md (accurate history; C26 refresh was meta/lineage-scoped); 1 chunk-map WORKLIST row (`4CH1-4.15`, registered corpus gap, empty quote by design); chunk-map note_paths and concept-edge evidence files reference the notes corpus that lives outside this repo (107/471 evidence files resolvable here — same situation as at C11/C13 landing).

## 2. Finding F1 — AO `weighting_by_paper` matrix (repaired)

The shared anchored matrix (`paper_1: &id001` / `paper_2: &id002`, aliased into all three AO records) carried **AO3's column values in the ao1/ao2 cells of both papers** (`11.6–12.8%` / `7.4–8.2%` replicated), contradicting (a) the PDF p35 table, (b) the canonical `unit_weightings`, (c) the C26 field map's own `adopted_fields` contract, and (d) the records' own `weighting_overall` (38–42% vs 19.0–21.0 component sum). Pre-state pin `36f361ec8afa3dcc…` equals the C26 record's post-pin — the mis-assignment was inherited from the c09-era table extraction and C26's en-dash adoption preserved it in place.

**Repair** (triple-verified against PDF p35 `pdftotext`, canonical JSON, and component arithmetic 23.2–25.7 + 14.8–16.3 = 38.0–42.0; 11.6–12.8 + 7.4–8.2 = 19.0–21.0):

| Cell | Pre | Post |
|---|---|---|
| paper_1.ao1 | 11.6–12.8% | **23.2–25.7%** |
| paper_1.ao2 | 11.6–12.8% | **23.2–25.7%** |
| paper_2.ao1 | 7.4–8.2% | **14.8–16.3%** |
| paper_2.ao2 | 7.4–8.2% | **14.8–16.3%** |

plus a `definitive_lineage.note` extension documenting the repair. Anchor/alias structure preserved (1 anchor + 2 aliases each, asserted). Pin: `graph/assessment_objectives.yaml` `36f361ec8afa3dcc…` → `3dc670176f2f5529…`. This is recorded here as a C26 errata per record-immutability convention (C26 records unedited).

## 3. Finding F2 — chunk-map `sp_title` stale labels (repaired)

`spec_chunk_mappings.yaml` sp_title display labels were copied from the spec store at c13 build time (pre-C24): **84/211 drifted** from the definitive `official_wording`, and **4 carried retired-lineage notation damage** — inline-math `$R_f$`/`$A_r$` forms (rows `3e6b6d8628103928`, `c3d3cb1a632c338b`) and a CJK ideograph in the 1.10 technique list (rows `cabb0bb60b6450dd`, `743c5006b4685a93`) — the exact damage classes C24 eliminated. `graph/` therefore still contained one store deriving wording from the retired OCR lineage, contradicting the C26 "zero stores" unification.

**Repair**: all 84 labels re-sourced from the definitive store wording (211/211 aligned); mapping decisions, spec codes, note anchors, evidence quotes, HUMAN_VALIDATED promotion state — all untouched (deep-verified field-by-field). Meta gained `sp_title_wording_source` + `sp_title_refresh` lineage keys. Pin: `graph/spec_chunk_mappings.yaml` `3d4877dd0cc5f75f…` → `f36910450bd50726…`. Both repair scripts are idempotent (verify-only on re-run).

## 4. Knowledge-graph HTML (latest)

| Artifact | Location | sha256 (16) |
|---|---|---|
| **v77 (latest)** — regression-fix release | `FileUpload` repo `syllabai-openhuman-edexcel-chemistry-kg/syllabai-openhuman-edexcel-chemistry-v77-regression-fixes.html` @ origin/main `b975298`; local mirror `/home/z/my-project/download/syllabai-openhuman-edexcel-chemistry-v77-regression-fixes.html` | `d485753bcf213206` |
| v76 (prior) — audit-fix release | same repo @ `7975028`; local mirror in `download/` | `2636ddc05921f6ed` |

## 5. Pins (sha256, 16-hex)

| File | Pre | Post |
|---|---|---|
| `graph/assessment_objectives.yaml` | `36f361ec8afa3dcc` (C26 post) | `3dc670176f2f5529` |
| `graph/spec_chunk_mappings.yaml` | `3d4877dd0cc5f75f` | `f36910450bd50726` |

All other C25/C26 pins re-verified unchanged (15/15 in sweep S4).

## 6. Scope guards honored

Node states byte-untouched; 2012-Jan escalations and the data bridge not approached; C25/C26 records unedited (both findings closed here as errata); no surface changes beyond the two repaired stores and this record; derived stores `_derived/**` untouched.

## 7. Open items (documented, untouched)

- 1 chunk-map WORKLIST row (`4CH1-4.15`) — registered corpus gap, owner-held decision.
- Chunk-map/concept-edge evidence files pointing into the notes corpus living outside this repo (join-time contract per c13 forward_contract).
- Operator-held: snap-002 re-freeze; T-C11 batch 5 commissioning; PAT rotation advised.
