# T-SPECS-CIE-VERDICT-2 — operator-verdict fill lane record (wave-2 AS lanes)

- Date: 2026-10-29 (Asia/Dhaka; session zai-web `web-df0238cc-…`, gateway
  trace `1a183e66619bd6dd`)
- Operator directive: *"verdict fills → review gate → v2 consume"* — fires
  the T-SPECS-CIE-REJOIN-2 record NEXT #1 (the operator-verdict fill class,
  the T-SPECS-CIE-VERDICT-1 precedent) on the 8 wave-2 AS sidecar lanes.
  The same directive orders this chain's stage #2 (review/promotion gate)
  and stage #3 (v2 consume) — each remains its own gated lane.
- Base commit: `251b46ba0bd9a08d66d57eca44fc8c80cd283289` (origin/main;
  engine asserts HEAD == pin before any write plus a foreign-dirty TOCTOU
  guard — fetch-first discipline; the only spec-links deltas since the
  REJOIN-2 landing 8a9e224 are the maths-b lanes', zero contact with the
  8 AS sidecars — verified first-hand).
- Lane script: `scripts/cie_verdict_fill_wave2as.py` (deterministic engine,
  fixed stamp `2026-10-29T12:00:00Z`, HEAD-pinned reads, byte-idempotent),
  battery `scripts/cie_verdict_check_wave2as.py` (VD1-VD10), verdict sheet
  `scripts/cie_verdict_wave2as_verdicts.yaml`.

## What was built

The still-pending anchors of the 8 wave-2 AS lanes re-evaluated under the
**V-class operator-verdict rules** (the VERDICT-1 lineage, imported — not
forked normalization), pools bounded by the JOIN-2 AS scope law imported
from the REJOIN-2 engine (AS Level-only chem-25/phys-25/business-23,
A-Level-marked excluded cs-19, unscoped 9709 maths x4):

- Substrate: the lane's SME note `spec_point` blocks, read verbatim from
  HEAD blobs (the VERDICT-1 substrate). Pairs whose sid carries no note
  block in the lane (EQ/flashcard-referenced, recordless) are not
  V-evaluable and stay pending honestly (`dangling_eq_reference` — the
  planned SME-native index harvest remains the named cure).
- Rules V1→V2(+V5 topic-scoped disambiguation)→V3→V4, quarantine-on-multi,
  no fall-through (the T-SPEC-2c doctrine). V4 is pinned 0 for this lane
  class (no literature registry in the 8).

## Results (honest)

- **Reconciliation EXACT**: 9,326 pending refs → 800 unique (lane, sid)
  pairs = **18 resolved (all V3_subsection_head_identity) + 575 quarantined
  (finer_than_official_subsection 541 + name_phrase_multi_text 34) + 207
  stays (no_unique_identity 205 + dangling_eq_reference 2)**.
- **169 code entries cascaded** (deduped per item by official_id), **184
  pending refs cured** (9,326 → 9,142), **2 lanes touched**:
  - `cie-as-business-23` 14 ids / 33 refs / 18 codes — the topic-head
    identities: 11 note topics "Management" → the single-point AS
    subsection "Management" (2.3.1 *Management and managers*) and 3 note
    topics "Forecasting & Managing Cash Flows" → 5.3.1 *Cash flow
    forecasts*;
  - `cie-as-chemistry-25` 4 ids / 151 refs / 151 codes — "Metallic
    Bonding" → 3.3.1, "Homogeneous & Heterogeneous Catalysts" → 8.3.1,
    "Reacting Masses & Volumes (of Solutions & Gases)" → 2.4.1, "Infrared
    Spectroscopy" → 22.1.1 (the JOIN-2 precedent class: 2.2.1/3.7.1 were
    the same identity family at the name level).
- The 541 `finer_than_official_subsection` quarantines are the T-SPEC-2c
  doctrine working: a note topic title equals an official subsection title
  that holds MORE THAN ONE AS point — never collapsed (this is the
  REJOIN-2 "no_identity_evidence" stay class re-labelled by the deeper V3
  predicate; the pairs stay pending either way). The 34
  `name_phrase_multi_text` are exactly the REJOIN-2 J4 quarantines (V5
  found no topic-scoped single hit).
- V1/V2 yield 0 on the remaining pairs — expected: the REJOIN-2 J3/J4 pass
  already exhausted the name-identity class on every pending pair.
- Resolutions land **SUGGESTED** (anchors.verdict + review_state.verdict
  additive blocks, state SUGGESTED): identity-grade single-target verdicts
  are authoritative by construction (AGENT.md rule 1), but the lane-level
  promotion happens at the stage-#2 review/promotion gate (rule 2). This
  lane does NOT promote, does NOT consume, does NOT touch v2.

## Battery

`scripts/cie_verdict_check_wave2as.py` **VD1-VD10: 10/10 PASS**
(`graph/reports/T_SPECS_CIE_VERDICT_2_CHECK.json`):

| id | check |
|----|-------|
| VD1 | 2 touched sidecars well-formed (additive verdict blocks appended last, SUGGESTED state, rejoin blocks byte-preserved, method/tier vocab) |
| VD2 | mutation discipline vs HEAD: only codes-append (deduped) / pending-shrink (order preserved) / additive verdict blocks / recounted counters (universe_resolved join semantics recomputed); every other field deep-equal |
| VD3 | INDEPENDENT re-derivation (fresh pools from the raw parsed registries under a fresh AS scope law, fresh normalization, fresh note-block substrate from HEAD blobs, fresh rule chain) + sheet bijection: 18 resolves + 575 quarantines equal |
| VD4 | cascade integrity (codes dedup-correct, pendings shrunk exactly, anchors recounts, stats coherent); 169 code entries |
| VD5 | manifest discipline (touched rows value-consistent, pre-existing rows preserved, `cie_verdict_wave2as` block additive + appended last) |
| VD6 | footprint 8 paths subset-of declared; spec-links delta == 2 sidecars + manifest; SME trees / Official-Specifications / SME-Flashcards guards intact; 93 out-of-lane sidecars untouched (incl. all 6 untouched AS lanes) |
| VD7 | engine fixed-stamp re-run byte-identical (2 sidecars + manifest + sheet + stats, sha256; the stats artifact carries NO wall-clock fields) |
| VD8 | honesty + scope pins: 2 record-less pairs still pending untouched; V4 == 0; all 18 resolves inside their lane's AS-scoped pool with the raw scope predicate re-checked independently |
| VD9 | 2-lane full-document rebuild from HEAD + independent resolutions == staged bytes (cie-as-business-23, cie-as-chemistry-25) |
| VD10 | cross-foots: manifest rows 35,692 → 35,508 (−184 refs cured); 8-lane sidecar anchors 9,326 → 9,142; reconciliation 800 pairs exact |

## Defects found and fixed pre-landing (the gates working as designed)

- **VD2 dedup catch (real engine defect, fixed before landing)**: an item
  carrying TWO pendings that resolve to the SAME official id received two
  identical code entries — the engine's dedup tested only the pre-existing
  codes, not the in-flight append buffer. Fixed (seen-oid set spans both);
  business-23 codes 33 → 18 (dedup law per the sidecar model: codes are
  the item's official-linkage set, one entry per official_id). The
  RJ-lineage battery never carried an in-slice dedup check — VD2 adds it.

## Inherited defect DISCLOSED (not repaired here — no cross-lane plane contact)

- **REJOIN-2 in-item duplicates**: re-running the VD2 dedup predicate
  against the committed REJOIN-2 delta found **11 items with duplicate
  `cie_index_rejoin_wave2as` code entries** — cie-as-business-23 ×5
  (rn_jz7TdKSJPQXSjCBb 2×2.1.4, rn_P9pQrMHkSmkGyXxX 2×2.2.4,
  qstnprt_dbnrkZv4Trg9wnDz 2×2.1.4, qstnprt_ZMNGwpykHNZvMyBK 2×2.2.4,
  qstnprt_7KHxrR4cy3f9QmQ8 2×2.2.4), cie-as-computer-science-19 ×2
  (rn_g8sjd6PVPvy9XrKJ 3×2.1.5, qstnprt_GD2yB5srCYGmqfgX 2×2.1.5),
  cie-as-maths-20-mechanics ×4 (rn_7vFZ9m4DpPc6jx37 2×4.5.2,
  qstnprt_RFWJQ8HYSgVcNwWC 2×4.5.2, qstnprt_kMFW85MmhBPWfCbW 2×4.5.2+4.5.3,
  qstnprt_VFxRHRYz5kjSwqSH 2×4.5.2). Root cause: the shared append-buffer
  dedup defect this lane fixed in ITS engine (the REJOIN-2 engine carries
  the same one-line flaw); the RJ battery's "codes dedup-correct" leg
  checked official_id validity, not in-slice duplicates. Disposition per
  the lane discipline (the REJOIN-2 addendum's inherited-red precedent):
  DISCLOSED for the rejoin lane owners — NOT repaired by this lane, no
  blind fix, the rejoin codes are that lane's plane. **Stage-#3 consume
  input requirement**: the consume engine must attach codes deduped per
  official_id (verify its law before the run) so the duplicates are inert
  at the bundle linkage plane; a sidecar-side repair remains the rejoin
  owners' one-line fix-forward.

## NEXT (operator-gated, the JOIN-2 chain of record, stages #2-#4)

1. ~~Operator-verdict fills (V-class)~~ — THIS LANE (18 V3 resolves,
   SUGGESTED).
2. Review/promotion gate (the T-SPECS-CIE-GATE-1 / REJOIN-GATE-1
   precedent) — independently re-derives every resolution class, then
   promotes the wave-2 chain SUGGESTED → ACCEPTED: review_state (JOIN-2
   top-level state) + rejoin + verdict blocks.
3. v2 consume (`apps/hub/scripts/cie/cie_consume_spec_links.py`) + bundle
   linkage re-emit (linkage-fields-only law) + census re-pin (computed,
   never transcribed) + the operator-gated prod-apply posture per the
   phase-4 plane law.
4. PAT rotation — standing order REITERATED (CRITICAL-OVERDUE of record).
