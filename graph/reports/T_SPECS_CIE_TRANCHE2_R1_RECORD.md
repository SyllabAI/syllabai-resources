# T-SPECS-CIE-TRANCHE2-R1 — the residual T2_near census promotion + the head-bank verdict sheet

- Date: 2026-10-22 (Asia/Dhaka; session zai-web `web-df0238cc-…`, gateway trace
  `1a15f8160e677949`)
- Operator order: **"Tranche-2"** — fires `tranche2_verdictProgram` of the
  anchor-gap census receipt of record
  (`syllabai-v2 .syllabai/receipts/CIE-INTEGRATION/cie-anchor-gap-census-r0.json`):
  *"the 16,335-part name-phrase verdict program per bank ... tier laws unchanged
  (operator_verdict authoritative; T2_near non-authoritative; never guessed);
  each bank's tranche lands via the same chain as tranche-1"*.
- Base commit: `cef8d5e` (PR #26 v0.8.1) at lane ignition; **REBASED of record
  onto `fc6bf29`** before landing — the sibling T-SPECS-CIE-COMPLETE-1 lane
  (operator order "Proceed with (1) upstream lattice-join completion", gateway
  trace `1a15f79acff5346d`, 2026-10-22) moved `main` by 4 commits mid-lane with
  a `spec-links/` overlap (cie-igcse-business-23 + manifest.json + README.md).
  The rebased fleet T2 census is byte-identical (423 / split / methods / lanes
  all re-verified EXACT on the `fc6bf29` base — the V7 note joins did not touch
  the T2 pool); this lane's commit carries parent `fc6bf29`.
- **Inherited-totals correction (disclosed)**: the COMPLETE-1 lane left
  cie-igcse-business-23's `totals` stale (stored `coded_by_kind.notes` 34 vs
  recomputed 70 — its own `complete` block discloses `notes_coded_after: 70`).
  This lane's engine corrected the counters, provably attributed: the drift
  delta (36) == EXACTLY the count of items whose ONLY codes are
  V7_agent_note_join entries. Any other drift aborts hard.
- Engines: `scripts/cie_tranche2_t2_enrichment_inventory.py` (queue generator,
  pinned fleet census) + `scripts/cie_tranche2_t2_enrichment_fill.py`
  (deterministic, fixed stamp, fail-closed, one-way re-run) +
  `scripts/cie_tranche2_t2_enrichment_check.py` (battery) +
  `scripts/cie_tranche2_chem25_sheet.py` (the head-bank review sheet).
- Battery: **T1/T2/T3/T5/T6/T7/T8/T9/T10 — 9/9 PASS on the rebased base**
  (`graph/reports/T_SPECS_CIE_TRANCHE2_R1_CHECK.json`; the tranche-1 battery's
  T4 vocabulary check is folded into T2 this edition — disclosed; T9 counts
  the payload footprint — the sandbox's deleted SME-RevisionNotes working-tree
  files are disk-rescue noise, never part of the lane payload).

## What was done (round-1 = two components)

### Component A — the residual T2_near census promoted fleet-wide (423 entries)

The tranche-1 round promoted the census receipt's 155-part/161-entry queue. The
**residual** T2 census — 423 entries in 15 of the 44 CIE sidecars — carried the
SAME GATE-1-accepted near evidence and sat in the census receipt's own tranche-2
scope (the anchored-class enrichment + the notes axis). This round re-tiers all
of them in place (codes[] order preserved; prior method verbatim in the sheet):

| class × kind | entries |
|---|---:|
| anchored · question_part | 151 |
| anchored · note | 45 |
| t2only · question_part | 162 |
| t2only · note | 65 |
| **total** | **423** |

- 423 == the post-tranche-1 t2Hints census of record EXACT (584 − 161); the
  110 note entries == the census receipt's "~110 T2 hint entries" EXACT; the
  15-lane/299+124-method split pinned in the engine and battery-verified.
- **The census-queue hole (disclosed of record)**: the 162 t2only part entries
  in 8 lanes (cs-23 48 / geography-20 62 / physics-23 23 / economics-20 10 /
  env-mgmt-20 8 / business-23 5 / chemistry-23 4 / biology-23 2) were NOT in
  the census receipt's tranche-1 queue although they carry the same audited
  evidence and sit in the v2 maps as `t2HintCodes` on codes-empty items (map
  hint arithmetic 313 == 151 + 162 EXACT per lane). The census receipt's queue
  figures stay historical-of-record (append-only); the fleet T2 census of
  record is THIS round's sheet (computed, never transcribed).
- **Gap movement**: the 162 t2only part entries anchor their parts — the expQ
  re-pin after the v2 consume re-run is the of-record number. The anchored
  class and the notes do not move the question census (the notes axis gains
  its accepted-near codes as authoritative).
- **The T2_near class retires fleet-wide** (battery T2: zero residual).

### Component B — the head-bank operator review sheet (cie-a-level-chemistry-25)

The mass order's head bank: **1,336 pending question parts / 256 distinct
pending spcpt entities**. The substrate is NAME-ONLY (255/256 entities carry a
name record, ZERO carry a definition — the rejoin's identity-grade rules J1–J4
are exhausted on this pool; identity residual 0 verified first-hand). The
honest mass instrument is the operator review sheet (the c11 batch pattern):

| evidence class | entities |
|---|---:|
| J4_residue (unique-phrase hit, flagged for the operator's eye) | 1 |
| multi_hit (the rejoin's quarantine class) | 10 |
| declared_link (home note already authoritatively coded) | 20 |
| record_less (no corpus record — upstream coverage gap) | 1 |
| no_match (the operator's semantic ruling is the only honest path) | 224 |

Deliverables: `scripts/cie_tranche2_chem25_review_sheet.yaml` (256 rows:
verbatim SME name + subtopic scope + section + part refs + wide hits + scoped
official candidates with statement texts + `ruling: PENDING`) and
`graph/reports/T_SPECS_CIE_TRANCHE2_CHEM25_SHEET.md` (the reading surface,
grouped by section). **Nothing in the sheet is auto-applied** — the no-match
pool's mappings are semantic judgments and belong to the operator (ADR-030;
AGENT.md rule 3).

## Footprint

- Modified: `spec-links/cie-<15 lanes>.json` (entry re-tiers + additive
  `review_state.tranche2` / `anchors.tranche2` blocks),
  `spec-links/manifest.json` (15 row blocks + top-level `cie_tranche2`).
- Added: the four scripts + `graph/reports/T_SPECS_CIE_TRANCHE2_R1_RECORD.md`
  + `T_SPECS_CIE_TRANCHE2_R1_FILL.json` + `T_SPECS_CIE_TRANCHE2_R1_CHECK.json`
  + the chem-25 sheet pair.
- Byte-untouched: the 29 non-queue CIE sidecars, all 49 Edexcel spec-links
  files, SME trees, Official-Specifications/**, graph/** beyond the new
  records (battery T6/T9).

## NEXT (the census receipt's chain)

1. **v2 consume re-run** at the advanced pin (this lane's merge sha) — the V6
   entries are consume-authoritative by the sidecar_rank law; the 162 t2only
   parts' codes fill; bundle linkage re-emits linkage-fields-only; the maps'
   t2Hints census drops to 0; the census re-pins (the expQ delta is the
   162-entries' distinct unmapped parents — computed, never transcribed;
   any divergence from the v2-side pre-flight prediction is a hard stop).
2. The **operator's ruling batches** on the chem-25 sheet (and the remaining
   37 banks' sheets generated by the same engine on demand) — each batch
   encodes as operator_verdict rows and lands via the same chain.
3. Each tranche's DB landing stays the **operator-gated 134c re-run**.
