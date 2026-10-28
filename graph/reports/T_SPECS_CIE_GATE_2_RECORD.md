# T-SPECS-CIE-GATE-2 — wave-2 AS chain review/promotion gate record

- Date: 2026-10-29 (Asia/Dhaka; session zai-web `web-df0238cc-…`, gateway
  trace `1a183e66619bd6dd`)
- Operator directive: *"verdict fills → review gate → v2 consume"* — the
  gate is stage #2 of the JOIN-2 chain of record (T-SPECS-CIE-REJOIN-2
  record NEXT #2 / T-SPECS-CIE-VERDICT-2 record NEXT #2), operator-keyed
  per AGENT.md rule 2 (no self-promotion anywhere in the chain).
- Base commit: `b97a80c72bcba64546b376746efac76fd7847737` (the VERDICT-2
  landing; verifier asserts HEAD == base before any evaluation).
- Scripts: `scripts/cie_gate2_verify.py` (independent verifier),
  `scripts/cie_gate2_apply.py` (disposition applier — refuses on any FAIL),
  `scripts/cie_gate2_check.py` (battery GT1-GT7).

## Verification (independent, before promotion)

`cie_gate2_verify.py` re-fired every resolution of the wave-2 chain from
its sheet's verbatim evidence against the canonical AS-scoped pools:

| class | total | verified | method |
|---|---|---|---|
| V (VERDICT-2 operator-verdict fills) | 18 | 18 | V3 head-identity re-fire from the recorded head evidence, uniqueness re-checked over the FULL scoped pool, official_text verbatim vs pool, pair out of every item's pendings, code entry present (method operator_verdict), scope-law raw predicate re-checked, V4 pinned 0 |
| J (REJOIN-2 index re-join) | 124 | 124 | J1-J4 rule re-fire from the sheet evidence with the same re-fire + uniqueness + payload checks; verdict_evaluated scoping recomputed (AS lanes ∉ ZERO_LANES → pinned False for every pair) |
| T2 (JOIN-2 anchors) | 49 | 49 | the GATE-1 V3 lower-bound audit adapted to the 8 lanes: per-anchor definition-line Jaccard ≥ 0.55 against either pool, OR name == point-text tokens with a line ≥ 0.35, OR name == the official subsection title; anchors read fresh from HEAD blobs; pools bounded by the AS scope law |
| **total** | **191** | **191** | **zero defects** (`T_SPECS_CIE_GATE_2_VERIFY.json` verdict PASS) |

State-of-record pins: all 8 lanes' top-level review_state exactly the
JOIN-2 SUGGESTED/pending state; rejoin blocks SUGGESTED on the 7 touched
lanes (pure-2 honest zero — none); verdict blocks SUGGESTED on the 2
touched lanes (none elsewhere). The 11 inherited REJOIN-2 in-item
duplicates are pinned at their disclosed census (known-defect disclosure —
the consume lane dedups per official_id at attach time; a sidecar-side
repair remains the rejoin owners' one-line fix-forward). Both quarantine
populations (34 J + 575 V) verified still pending — nothing cured outside
its lane.

## Promotion

`cie_gate2_apply.py` (run ONLY on the verifier's PASS):
- 8 sidecars' `review_state.state` SUGGESTED → **ACCEPTED**, gate
  "pending" → `T-SPECS-CIE-GATE-2`, additive acceptance payload
  (accepted_utc / accepted_by / verification) inside the top-level block;
- `review_state.rejoin.state` → ACCEPTED (7 lanes),
  `review_state.verdict.state` → ACCEPTED (2 lanes) — same additive shape;
- manifest: `cie_join_wave2as.review_state` → ACCEPTED,
  `cie_rejoin_wave2as.state` → ACCEPTED, `cie_verdict_wave2as.state` →
  ACCEPTED (each + the acceptance payload); NEW top-level
  `cie_gate_wave2as` block appended LAST (append-only order);
- items / codes / pending / totals / anchors BYTE-PRESERVED (battery
  deep-equal); accepted_by = the operator directive verbatim + gateway
  trace (operator-keyed promotion, rule 2).

## Battery

`scripts/cie_gate2_check.py` **GT1-GT7: 7/7 PASS**
(`graph/reports/T_SPECS_CIE_GATE_2_CHECK.json`):

| id | check |
|----|-------|
| GT1 | verifier PASS precondition (191/191, V 18 + J 124 + T2 49, base pinned) |
| GT2 | mutation discipline vs the base commit: items/codes/pending/totals/anchors deep-equal; ONLY review_state (+ its rejoin/verdict blocks) promoted, with additive acceptance keys and the recorded pre-existing payload preserved |
| GT3 | 8/8 sidecars promoted (rejoin ×7, verdict ×2); acceptance payload consistent with the verifier |
| GT4 | manifest discipline: three chain blocks → ACCEPTED, all pre-existing blocks/rows deep-equal, `cie_gate_wave2as` appended last |
| GT5 | footprint 14 paths subset-of declared; spec-links delta == 8 sidecars + manifest; SME trees / Official-Specifications / SME-Flashcards guards intact |
| GT6 | apply idempotence: re-run byte-identical (8 sidecars + manifest, sha256) |
| GT7 | cross-foots: codes census unchanged through the gate (1,759 entries; the 11 inherited duplicates still pinned — the disclosed REJOIN-2 known defect) |

## What this gate does NOT do (fail-closed)

- No quarantine promotion: the 609 quarantined pairs (575 V + 34 J) stay
  out of the codes with their reasons of record.
- No v2 contact: the consume / linkage re-emit / census re-pin chain is
  stage #3 — its own lane.
- No repair of the inherited REJOIN-2 duplicates (that lane's plane).

## NEXT (the chain of record)

1. ~~Operator-verdict fills~~ — VERDICT-2 (landed b97a80c72, gate-accepted).
2. ~~Review/promotion gate~~ — THIS GATE (191/191, promoted ACCEPTED).
3. v2 consume (`apps/hub/scripts/cie/cie_consume_spec_links.py`) + bundle
   linkage re-emit (linkage-fields-only law) + census re-pin (computed,
   never transcribed) + the operator-gated prod-apply posture per the
   phase-4 plane law.
4. PAT rotation — standing order REITERATED (CRITICAL-OVERDUE of record).
