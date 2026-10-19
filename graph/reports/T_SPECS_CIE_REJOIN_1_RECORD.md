# T-SPECS-CIE-REJOIN-1 — index re-join lane record

- Date: 2026-10-19 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace
  `1a15370131f93699`)
- Operator directive: *"Re-join against the index"* — fires NEXT lane #1 of the
  T-SPECS-CIE-XJOIN-1 record (INDEX-1's NEXT (2)): the structured pendings fire
  against the canonical per-course indexes instead of blob-restricted evidence.
- Base commit: `c9fc6dfb` (T-SPECS-CIE-XJOIN-1, on origin/main).
- Lane script: `scripts/cie_index_rejoin.py` (deterministic engine, fixed stamp
  `2026-10-19T11:00:00Z`, byte-idempotent pre-commit re-runs; every base read
  from HEAD), battery `scripts/cie_rejoin_check.py`, resolution sheet
  `scripts/cie_rejoin_resolutions.yaml`.

## What was built

**The pending spec-point references of all 44 CIE lanes re-fired against the
canonical per-course spec-point indexes** (cross-lane-aware post-XJOIN). The
original join's T1 text confirmation was gated on path-numbering candidates and
the verdict lane's V1–V5 rules were NAME-only — so full-pool DEFINITION-text
identities had never fired anywhere, and NAME identities had never fired on the
coded lanes. The indexes close both gaps (H4: index entries deep-equal the
blobs; cross_lane_join blocks carry the 54 dangling cures).

Rules (tier == rule name, the verdict-lane pattern; method `cie_index_rejoin`;
priority chain J1→J2→J3→J4 with quarantine-on-multi and NO fall-through — the
T-SPEC-2c doctrine):

| rule | evidence | resolves |
|------|----------|----------|
| J1_definition_text_identity | norm(definition) == norm(official point text), unique in lane pool | 253 |
| J2_definition_phrase_identity | token-bounded norm(definition) phrase in exactly one official text | 36 |
| J3_name_text_identity | norm(name) == norm(official text), unique — ONLY where the verdict lane's name rules did not already evaluate the pair | 16 |
| J4_name_phrase_identity | token-bounded norm(name) phrase in exactly one official text (same scoping) | 329 |

Definition evidence is assembled corpus-wide (own lane + sibling lanes holding
the same spcpt id + cross_lane_join definition-grade cures) and must agree under
the lineage normalization SPEC or the pair quarantines
(definition_conflict_across_lanes — 0 on this corpus). Pools mirror the
join/verdict scoping (0654 scope, 0580/0607 tier, 9709 component topics).

## Results

- **Reconciliation EXACT**: 33,900 pending refs → 7,605 unique (lane, sid) pairs
  (7,283 universe + 322 non-universe == the XJOIN 322) = **634 resolved (J1 253
  + J2 36 + J3 16 + J4 329) + 166 quarantined (name_phrase_multi_text, matched
  codes recorded) + 6,805 stays (no_new_evidence_verdict_evaluated 4,385 +
  no_identity_evidence 2,152 + recordless 268)**.
- **2,771 code entries cascaded** (tier J*, method cie_index_rejoin),
  **2,794 pending refs cured** (33,900 → 31,106), **22 lanes touched**; top:
  physics-23 134 pairs/430 refs, physics-25 81/660, chemistry-25 46/373,
  biology-23 92/290, chemistry-23 68/256.
- **Exactly 1 verdict-pending cure** (4,386 → 4,385) — via definition rules
  only, respecting the verdict lane's name-rule exhaustion.
- **The 268 record-less (lane, id) pairs stay pending honestly** (rule 3) —
  byte-verified still in their pendings.
- Resolutions land **SUGGESTED** (review_state.rejoin block, state SUGGESTED):
  engine-derived identity-grade joins are suggestions until the next
  review/promotion gate (AGENT.md rule 2); the gate's ACCEPTED payload and the
  verdict lane's authoritative operator entries are preserved. The next gate
  (NEXT #3) promotes them.
- Sheet: `scripts/cie_rejoin_resolutions.yaml` — per-(lane, id) verdicts with
  verbatim evidence (sme_name/sme_definition/official_text/evidence_source
  own|sibling:<lane>|cross_lane_join + corroborating sources) + ambiguous
  entries.

## Checks

Battery `scripts/cie_rejoin_check.py` **RJ1–RJ10: 10/10 PASS**
(`graph/reports/T_SPECS_CIE_REJOIN_1_CHECK.json`):

| id | check |
|----|-------|
| RJ1 | 22 touched sidecars well-formed (additive rejoin blocks, SUGGESTED state, method/tier vocab, no-trailing-NL) |
| RJ2 | mutation discipline vs HEAD: only codes-append (prefix property) / pending-shrink (order preserved) / additive rejoin blocks / recounted counters (pending_refs, verdict-semantics universe_resolved); every other field deep-equal |
| RJ3 | INDEPENDENT re-derivation (fresh pool builders, fresh normalization, fresh rule chain) + sheet bijection: 634 resolves + 166 quarantines equal |
| RJ4 | cascade integrity (codes dedup-correct, pendings shrunk exactly, anchors recounts, stats coherent) |
| RJ5 | manifest discipline (touched rows value-consistent, pre-existing rows preserved, cie_rejoin additive) |
| RJ6 | footprint 28 paths ⊆ declared; spec-links delta == 22 sidecars + manifest; guards intact; 49 Edexcel sidecars untouched |
| RJ7 | engine fixed-stamp re-run byte-identical (sidecars + manifest + sheet + stats, sha256) |
| RJ8 | honesty pins: 268 record-less pairs still pending; name rules scoped to non-verdict pairs; exactly 1 verdict-pending cure via definition rules |
| RJ9 | 2-lane full-document rebuild from HEAD + independent resolutions == staged bytes |
| RJ10 | global cross-foot: pending refs 31,106 == 33,900 − 2,794; pins (7,605 / 4,385 / 634-by-rule) reproduced |

## Defects on the record (all caught en route, all fixed, none shipped)

Engine (2 chain/logic defects, both caught by cross-checks before commit):
1. **J3/J4 chain overwrite**: the J4 block was not in J3's else-branch — a J3
   hit was overwritten by a J4 phrase hit (13 pairs mis-tiered) or discarded by
   a J4 multi-quarantine (3 pairs lost). Caught by the survey probe's
   independent J3/J4 counts (J3 16 / J4 329 + 166 multi) vs the engine's (J3 0
   / J4 342 + 169). Fixed to the else-branch chain; 634/166 exact thereafter.
2. **anchors.pending_refs main counter not updated** (only the rejoin block's)
   + **universe_resolved recompute applied to ALL touched lanes** — the latter
   corrupted the coded lanes' JOIN-semantics value (biology-25's
   text-resolved count 260) with the verdict-fill formula. Discovery: the
   corpus carries TWO universe_resolved lineages (verdict-fill's
   universe-minus-pending on the 25 zero lanes; the join's text-resolved count
   on the 19 coded lanes). Fixed: recompute ONLY where anchors.verdict lives;
   coded lanes preserve the join value; a["pending_refs"] always recounted.
3. Census double-count (multi-hits in both ambiguous and stays) — caught by
   the engine's internal reconciliation assert before any sheet write.

Battery (verifier defects, engine output correct throughout):
4. pend_u counted pending REFS (1,644) instead of DISTINCT universe sids (133)
   — nonsense negative expectation on maths-25-core; initially also nested
   inside the per-key loop (double count). Fixed to a distinct-sid set.
5. rj3 unpacked the ambiguous value dict as a reason string → always-false
   compare reported on the first pair. Fixed.
6. rj7 before_s/before_j missing `.hexdigest()` → always-false drift. Fixed.
7. rj8 iterated recordless pairs over non-touched lanes → KeyError. Guarded.
8. rj9's final require compared **str to bytes** (`rb == staged_bytes(...)`) →
   always-false; survived several content fixes; diagnosed via temporary
   first-byte-diff instrumentation; fixed with `.encode()`. The rj9 rebuild
   itself was also initially missing the anchors.pending_refs update.
9. rj9's rebuild initially recomputed universe_resolved unconditionally.
   Fixed to the same conditional as the engine.

## Footprint

- Modified: 22 spec-links sidecars (codes/pending/totals/anchors + additive
  rejoin blocks), spec-links/manifest.json (22 rows + cie_rejoin block),
  plus the lane's own scripts/sheet/reports.
- Byte-untouched: the other 22 CIE sidecars, all 49 Edexcel spec-links files,
  SME-RevisionNotes/**, SME-ExamQuestion/** (incl. the 44+49 indexes),
  SME-Flashcards/**, Official-Specifications/**.

## NEXT (operator-gated, NOT fired by this directive)

1. **Review/promotion gate on the SUGGESTED re-join resolutions** — the
   R41-shaped re-gate (explicit instruction only) promotes the 2,771
   cie_index_rejoin code entries to ACCEPTED.
2. Learner-UI consumption — verdict semantics (operator-verdict
   authoritative) + T2_near non-authoritative hint + the rejoin's J*-tier
   entries post-gate.
3. PAT rotation still CRITICAL-OVERDUE (fingerprint `a8ccee736aa8c75b`, now
   20 recorded plaintext transits).
