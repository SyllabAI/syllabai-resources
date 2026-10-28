# T-SPECS-CIE-REJOIN-2 — index re-join lane record (wave-2 AS lanes)

- Date: 2026-10-28 (Asia/Dhaka; session zai-web `web-df0238cc-…`, gateway
  trace `1a181f6adcfa4c55`)
- Operator directive: *"fire the re-join lane"* — fires the T-SPECS-CIE-JOIN-2
  record's follow-on #1, the index re-join class (the T-SPECS-CIE-REJOIN-1
  precedent) applied to the 8 wave-2 AS sidecar lanes.
- Base commit: `8460a5f3a03fd7d43ed31e39c27d846f8a747208` (maths-b content
  join r0, on origin/main; engine asserts HEAD == pin before any write —
  fetch-first discipline).
- Lane script: `scripts/cie_index_rejoin_wave2as.py` (deterministic engine,
  fixed stamp `2026-10-28T12:30:00Z`, HEAD-pinned reads — TOCTOU-free,
  byte-idempotent pre-commit re-runs), battery
  `scripts/cie_rejoin_check_wave2as.py` (RJ1-RJ10), resolution sheet
  `scripts/cie_rejoin_wave2as_resolutions.yaml`.

## What was built

**The pending spec-point references of the 8 wave-2 AS lanes re-fired against
the canonical per-course spec-point indexes**, corpus-wide definition context
over all 52 CIE lanes (own + sibling definition holders + cross_lane_join
cures), pools bounded by the JOIN-2 AS scope law (the parsed registries' own
printed markers, the SME-WAVE2 spine scope_eq basis):

| lane | law | lane points / registry |
|---|---|---|
| cie-as-chemistry-25 / cie-as-physics-25 / cie-as-business-23 | `AS Level` only | 204/356, 145/303, 62/116 |
| cie-as-computer-science-19 | `A Level`-marked EXCLUDED, scope-less retained | 161 / 227 |
| cie-as-maths-20-{pure-1,pure-2,mechanics,probability-and-statistics-1} | unscoped 9709 registry — no filter (JOIN-1 semantics) | 146 / 146 |

None of the 8 lanes was evaluated by any operator verdict lane (no
`anchors.verdict` block — battery RJ8 pins 0 verdict-evaluated pairs), so
the name rules fired on every pending pair. The substrate is name-only
(definitions null corpus-wide, harvest H4-verified; business-23 carries one
definition), so the yield class is J3/J4 name identity — the honest
REJOIN-1 baseline class, exactly as the JOIN-2 record projected.

Rules: J1 definition-text identity, J2 definition-phrase identity,
J3 name-text identity, J4 name-phrase identity (tier == rule name, method
`cie_index_rejoin_wave2as`, priority chain J1→J4, quarantine-on-multi, no
fall-through — the T-SPEC-2c doctrine).

## Results (honest)

- **Reconciliation EXACT**: 10,867 pending refs → 924 unique (lane, sid)
  pairs = **124 resolved (J3 4 + J4 120) + 34 quarantined
  (name_phrase_multi_text, matched codes recorded) + 766 stays
  (no_identity_evidence 762 + recordless 4)**.
- **1,541 code entries cascaded** (deduped per item by official_id),
  **1,541 pending refs cured** (10,867 → 9,326), **7 lanes touched**;
  per lane: physics-25 41 pairs/636 refs, chemistry-25 25/354,
  computer-science-19 29/129, mechanics 7/191, business-23 12/60,
  probstat-1 5/106, pure-1 5/65. **cie-as-maths-20-pure-2 resolved 0 —
  honest zero, untouched.**
- The 34 multi-text quarantines stay pending with matched codes recorded;
  the 4 recordless pairs stay pending honestly (AGENT.md rule 3).
- Resolutions land **SUGGESTED** (anchors.rejoin + review_state.rejoin
  additive blocks, state SUGGESTED): engine-derived identity-grade joins
  are suggestions until the next review/promotion gate (AGENT.md rule 2).
  This lane does NOT promote, does NOT consume, does NOT touch v2 — the
  follow-on chain of record (verdict fills -> review gate -> v2 consume +
  census re-pin) stays operator-keyed, exactly as the 44 evolved.

## Battery

`scripts/cie_rejoin_check_wave2as.py` **RJ1-RJ10: 10/10 PASS**
(`graph/reports/T_SPECS_CIE_REJOIN_2_CHECK.json`):

| id | check |
|----|-------|
| RJ1 | 7 touched sidecars well-formed (additive rejoin blocks, SUGGESTED state, method/tier vocab, scope-law note, trailing newline) |
| RJ2 | mutation discipline vs HEAD: only codes-append (prefix property) / pending-shrink (order preserved) / additive rejoin blocks / recounted counters (pending_refs; universe_resolved join semantics preserved — no verdict block); every other field deep-equal |
| RJ3 | INDEPENDENT re-derivation (fresh pools from the raw parsed registries, fresh normalization, fresh rule chain, fresh scope law) + sheet bijection: 124 resolves + 34 quarantines equal |
| RJ4 | cascade integrity (codes dedup-correct, pendings shrunk exactly, anchors recounts, stats coherent); 1,541 code entries |
| RJ5 | manifest discipline (touched rows value-consistent, pre-existing rows preserved, `cie_rejoin_wave2as` block additive + appended last) |
| RJ6 | footprint 13 paths ⊆ declared; spec-links delta == 7 sidecars + manifest; SME trees / Official-Specifications / SME-Flashcards guards intact; 49 Edexcel sidecars untouched |
| RJ7 | engine fixed-stamp re-run byte-identical (7 sidecars + manifest + sheet + stats, sha256; the stats artifact carries NO wall-clock fields) |
| RJ8 | honesty + scope pins: 4 record-less pairs still pending; 0 verdict-evaluated pairs (AS lane class); all 124 resolves inside their lane's AS-scoped pool, raw scope predicate re-checked independently |
| RJ9 | 2-lane full-document rebuild from HEAD + independent resolutions == staged bytes (cie-as-business-23, cie-as-chemistry-25) |
| RJ10 | cross-foots: manifest rows 27,465 → 35,692 (+8,227 gained-key recount on rows that never carried pending_refs, −1,541 resolved inside those values); 8-lane sidecar anchors 10,867 → 9,326; reconciliation 924 pairs exact |

## NEXT (operator-gated, the JOIN-2 chain of record, stages #2-#4)

1. Operator-verdict fills (V-class) where identity is single-target.
2. Review/promotion gate (the T-SPECS-CIE-GATE-1 precedent) — promotes the
   124 J* resolutions SUGGESTED → ACCEPTED.
3. v2 consume (`cie_consume_spec_links.py`) + bundle linkage re-emit
   (linkage-fields-only law) + census re-pin (computed, never transcribed)
   + the operator-gated prod-apply posture per the phase-4 plane law.
4. PAT rotation — standing order REITERATED (the credential transited
   plaintext in-chat in a prior session; rotation remains CRITICAL-OVERDUE
   of record).
