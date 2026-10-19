# T-SPECS-CIE-REJOIN-GATE-1 — the re-join chain's promotion gate (lane record)

- Date: 2026-10-20 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace
  `1a155ee451def291`)
- Operator directive: *"re-join against the index, further re-gates"* — fires
  REJOIN-1 record NEXT #1 (the R41-shaped re-gate of the re-join chain) plus
  the re-join chain's standing verification (below).
- Base commit: `0fe5f772` (T-C42 R41 pair, third landing, on origin/main).

## The re-join chain's verification of record (the no-op ruling)

The re-join input universe is **byte-identical since REJOIN-1** (`2578f6b →
0fe5f772`): zero delta across `spec-links/` (95 files), `SME-ExamQuestion/`
(all lanes incl. the 93 `spec_point_index.json`), and the CIE engine set. The
4PH1/MIG lanes never touched it. With REJOIN-1's own RJ7 byte-idempotence
pin, a REJOIN-2 re-fire at HEAD is a **provable no-op**; it was therefore
recorded rather than re-executed (the partial-clone materialization it would
require — ~60k corpus blobs — is the documented Task-22 trap, unjustifiable
for a provably empty result). The actionable item in the chain was NEXT #1:
this gate.

## What was built

**The 634 SUGGESTED identity-grade re-join resolutions (2,771
`cie_index_rejoin` code entries: J1 253 + J2 36 + J3 16 + J4 329) promoted to
ACCEPTED** across the 22 touched sidecars, per the GATE-1 pattern:

- **Verify-first** (`scripts/cie_rejoin_gate_verify.py`): every one of the
  634 sheet verdicts independently re-fired — rule re-evaluation from the
  sheet's verbatim evidence against the canonical pools (17 quals'
  registries + `vf.lane_pool` scoping), uniqueness re-checked over the FULL
  lane pool, official_id/code/text identity vs the pool, the J3/J4
  verdict-evaluated scoping recomputed from ZERO_LANES + the lane's index
  universe, cure landing verified (pair out of pendings, code entry present
  with tier/method), and the 166 quarantines confirmed reason-carrying and
  untouched. **634/634 PASS, 0 failed** before any write (the applier
  refuses on any FAIL — the GATE-1 law).
- **Apply** (`scripts/cie_rejoin_gate_apply.py`): per sidecar,
  `review_state.rejoin.state` SUGGESTED → ACCEPTED + the additive acceptance
  payload inside the rejoin block (gate / accepted_utc / accepted_by /
  verification); `manifest.json` `cie_rejoin.state` → ACCEPTED + the same
  additive keys + the NEW top-level `cie_rejoin_gate` block appended LAST
  (append-only key order). Items/codes/pending/totals/anchors untouched.
- **Battery** (`scripts/cie_rejoin_gate_check.py`) **RJG1–RJG10: ALL PASS
  exit 0 pre-commit**: footprint exactly 22 sidecars + manifest; the K2
  deep-equal discipline (items/codes/pending/totals/anchors byte-equal to
  HEAD — pendings untouched, the 268 record-less pairs intact); the rejoin
  payload keys byte-preserved; 2,771 entries recounted == STATS; manifest
  rows/legacy blocks deep-equal + append-only key order; verifier re-run
  byte-identical (fixed stamp); applier re-run byte-identical (idempotence);
  166/268 honesty pins; serialization round-trip stable; cross-foot
  634/2,771/166 coherent across sheet, VERIFY, STATS and the gate payload.

## Results

- 22 sidecars promoted; manifest `cie_rejoin` ACCEPTED + `cie_rejoin_gate`
  block of record; verification payload {pairs: 634, code_entries: 2771,
  verified: 634, failed: 0, ambiguous_stay_quarantined: 166}.
- The 166 multi-text quarantines stay quarantined; the stays (4,385
  no-new-evidence + 2,152 no-identity-evidence) and the 268 record-less
  pairs stay pending honestly (AGENT.md rule 3).
- The learner-UI consumption surface is now unblocked (NEXT #2): the rejoin
  J*-tier entries are ACCEPTED (identity-grade), the verdict lane's
  operator-authoritative entries unchanged, T2_near still a non-authoritative
  hint.

## NEXT (operator-gated)

1. Learner-UI consumption of the ACCEPTED rejoin entries (NEXT #2).
2. The C42 chain's next re-gate (R42 — the R41 record reserves it as
   explicit-instruction-only).
3. PAT rotation — CRITICAL overdue (fingerprint `a8ccee736aa8c75b`, 20
   recorded plaintext transits + this lane's push cycle).
