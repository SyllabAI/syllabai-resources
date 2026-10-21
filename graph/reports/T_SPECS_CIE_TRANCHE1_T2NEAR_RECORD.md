# T-SPECS-CIE-TRANCHE1-T2NEAR-1 — tranche-1 operator-verdict record

- Date: 2026-10-21 (Asia/Dhaka; session zai-web `web-df0238cc-…`, gateway trace
  `1a15e4200e6af579`)
- Operator order: **"tranche-1"** — fires `tranche1_t2NearVerdicts` of the
  anchor-gap census receipt of record
  (`syllabai-v2 .syllabai/receipts/CIE-INTEGRATION/cie-anchor-gap-census-r0.json`):
  *"OPERATOR-KEYED, smallest: 155 verdicts on already-computed spine-resolvable
  hints (the queue above, part-id named)"*.
- Base commit: `67a173b` (T-SPEC-ACCT-ADJ-1, on origin/main).
- Lane engine: `scripts/cie_tranche1_t2near_fill.py` (deterministic, fixed stamp,
  fail-closed; one-way re-tier — a re-run after apply aborts with zero byte drift).
- Verdict sheet: `scripts/cie_tranche1_t2near_verdicts.yaml` (161 rows, keyed per
  (lane, item, official_id)).
- Battery: `scripts/cie_tranche1_t2near_check.py` **T1–T10: 10/10 PASS**
  (`graph/reports/T_SPECS_CIE_TRANCHE1_T2NEAR_CHECK.json`).

## What was done

The anchor-gap census receipt's tranche-1 queue — **155 unanchored question_part
items whose sole join state is the GATE-1-accepted near hint** (committed v2
content-maps: `t2HintCodes` non-empty, `codes` empty) — promoted to the V*
authoritative class:

- **161 sidecar code entries re-tiered** in place (codes[] order preserved):
  `tier: T2_near -> V6_near_text_verdict`, `method: cie_*_text_join ->
  operator_verdict`. Prior method recorded verbatim per row
  (131 `cie_definition_text_join` + 30 `cie_text_join`).
- **The V6 class (additive to the VERDICT-1 ladder V1–V5)**:
  `V6_near_text_verdict` — the operator ratifies a GATE-1-audited accepted-near
  text join as authoritative for this item. Grounds of record: the T2 tier was
  audited 584/584 lower-bound with zero defects (T-SPECS-CIE-GATE-1), the r9
  consume proved the t2HintCodes discipline end-to-end with zero leaks, and the
  census receipt computed the queue and named it the operator's review queue.
- **Nothing else moved** (T5/T6/T7): item-id sets, kinds, labels, pending lists,
  totals, registry blocks, all 35 non-verdict CIE sidecars, all 49 Edexcel
  sidecars, and every pre-existing manifest field are byte-identical to base.
  No pending anchor was resolved or removed (this lane operates on item-level
  code entries, not spcpt anchors). No code invented (ADR-030): every promoted
  (official_id, official_code) pair was byte-verified against BOTH the sidecar's
  own T2 entry AND the lane's parsed registry (T3).

## The queue (computed, never transcribed)

Computed by the lane-side inventory (both cross-foots GREEN) and re-proven by
the battery: per-slug part counts equal the census receipt's queue EXACTLY.

| lane | parts | entries |
|------|------:|--------:|
| cie-igcse-business-23 | 41 | 41 |
| cie-a-level-biology-25 | 37 | 37 |
| cie-a-level-chemistry-25 | 25 | 25 |
| cie-a-level-physics-25 | 15 | 15 |
| cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry | 15 | 15 |
| cie-igcse-physics-23 | 7 | 13 |
| cie-igcse-computer-science-23 | 6 | 6 |
| cie-igcse-science-combined-science-23-biology | 6 | 6 |
| cie-igcse-science-combined-science-23-chemistry | 3 | 3 |
| **total** | **155** | **161** |

(Out-of-scope disclosures: 284 further question parts carry T2 hints but are
ALREADY anchored via authoritative codes — promoting those is tranche-2-scope
enrichment that does not move the anchor gap; the notes axis carries ~110 T2
hint entries — same program scope, untouched here.)

## Expected landing (the census re-pin is the of-record number)

116 distinct fully-unmapped parent questions of the 155 parts are predicted to
close (computed lane-side from the committed bundles: business-23 41,
chemistry-25 23, sdv-chem 15, biology-25 13, physics-23 7, cs-23 6,
combined-bio 4, physics-25 4, combined-chem 3). The downstream chain (consume
re-run at the advanced pin → linkage-only re-emit → census re-pin) re-derives
the of-record figures; any divergence from the prediction is a hard stop.

## Battery

| id | check |
|----|-------|
| T1 | 9 lanes well-formed (ACCEPTED + additive tranche1 blocks) + receipt-queue cross-foot (155/161) |
| T2 | bijection: promoted set (base-blob T2 entries on sheet items) == sheet, per lane; zero other entry drift |
| T3 | zero dangling verdict targets (official_id AND official_code in the lane registry) |
| T4 | vocabulary conformance (V6+operator_verdict pairing; zero T2_near left on the 155 sheet items) |
| T5 | structural integrity vs base (items/kinds/labels/pending/totals/registry/pre-existing blocks byte-identical) |
| T6 | non-verdict footprint byte-identical to base (35 CIE + 49 Edexcel sidecars) |
| T7 | manifest: pre-existing rows/fields value-identical + additive tranche1 blocks |
| T8 | v2-map cross-foot: every row's (item, official_id, spine_code) matches the committed t2HintCodes |
| T9 | footprint guard (git status within the declared set) |
| T10 | re-run safety: engine re-run fail-closes AND zero byte drift |

Defects caught en route (recorded honestly):

1. **Sheet prior-method hardcode** (caught by the engine's fail-closed gate —
   exactly its job): the sheet generator hardcoded
   `prior.method = cie_definition_text_join` on all rows while 30 entries are
   `cie_text_join` (cs-23 / sdv-chem / combined lanes); the engine refused all
   30. Fixed to verbatim per-row recording; the two text-join families are both
   of record (the law is the TIER — gate-audited T2_near — not one method
   string).
2. **promoted_parts miscount** (caught in the engine's own output review): the
   fill summary counted sheet ROWS (entries) as parts (physics-23: 13 vs 7).
   Fixed to distinct items; reverted and re-applied clean.

## Footprint

- Modified: `spec-links/cie-<9 lanes>.json` (entry re-tiers + additive
  `review_state.tranche1` / `anchors.tranche1` blocks), `spec-links/manifest.json`
  (9 row blocks + top-level `cie_tranche1`), `spec-links/README.md` (lane section).
- Added: `scripts/cie_tranche1_t2near_fill.py`, `scripts/cie_tranche1_t2near_verdicts.yaml`,
  `scripts/cie_tranche1_t2near_check.py`, `graph/reports/T_SPECS_CIE_TRANCHE1_T2NEAR_RECORD.md`,
  `T_SPECS_CIE_TRANCHE1_T2NEAR_FILL.json`, `T_SPECS_CIE_TRANCHE1_T2NEAR_CHECK.json`.
- Byte-untouched: the 35 non-queue CIE sidecars, all 49 Edexcel spec-links files,
  SME trees, Official-Specifications/**, graph/** beyond the three tranche-1 records.

## NEXT (the census receipt's chain; the 134c re-run stays OPERATOR-GATED)

1. **Learner-UI consumption re-run** in syllabai-v2 (`cie_consume_spec_links.py`)
   at the advanced pin — the V6 entries are consume-authoritative by the r9
   semantics (`sidecar_rank`: V* → rank 0); bundle linkage re-emits
   linkage-fields-only; the census re-pins (expect expQ 6,599 → 6,715, the gap
   12,479 → 12,363, per the 116-question prediction).
2. **The 134c cow+prod re-run** to land the new linkage on the DB of record —
   OPERATOR-GATED per the phase-4 plane posture (NOT fired by this order).
3. Tranche-2 (the 16,335-part verdict program) and tranche-3 (the 1,203-part
   SME coverage gap) remain programmed of record in the census receipt.
4. **PAT rotation still CRITICAL-OVERDUE** (fingerprint `a8ccee736aa8c75b`).
