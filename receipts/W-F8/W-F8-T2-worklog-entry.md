### W-F8-T2 build + local land — the igcse trio joins corrected and deepened (trace 1a1f3f29f14afce5)

- Build per the W-F8-T1 design of record: zero-LLM emitter
  (scripts/wf8_emit_join.py) reading only the pinned blobs at `cf1c8378`
  (spec sides, corpora v3/v1/v1, landed joins, structures); deterministic
  (BUILD_TS pinned, sha256 re-run identical).
- **Correction (M-11):** the landed 4CH1 62 and 4PH1 7 point entries removed —
  every one independently re-verified figure-caption or numeric-constant
  (probe2 classes; 2 entries honest `not_in_cited_evidence`); errata block
  enumerates each removal with its evidence; the false 'points_keyed' 7 + 7
  are gone; the books print no spec codes (F1 figure-void) — J2/J3 route
  verdicts re-stated with the M-8/M-9 laws of record.
- **Deepening (M-10):** 4CH1 subsections covered 18 -> 26/28 — 9 CONTAINS
  mappings added with unit/topic vetting (SUB5 -> u1:c5 + u1:c6
  multi-chapter; SUB8/9/14/21/25/26/27); SUB10/SUB11 stay honestly unmapped
  (reverse-direction only); 4PH1 stays 22/30 (the 8 'Units' SUBs have no
  title hits); 4BI1 rows byte-preserved (172 J1 keys stand; the 4 uncovered
  codes stay with the 0-hit corpus search as evidence).
- Gates G-F8-B1..B6 ALL PASS (6/6; independent re-derivation with the gate's
  own window scan and tree walk; determinism sha256 re-run; evidence
  cache/w-f8/gate-verdicts.json).
- Landing: zero-index plumbing commit, surface exactly 3M (one revertible
  commit: revert = restore the three landed join blobs); build commit
  b6c09f8250740251fdc9b2329beaa8ec7155e458; the records landing (task file + W-F8 receipts + the staged
  W-F7 push-confirm ride-alongs + the W-F7 push clause + LEDGER Waves 50-52)
  follows as the next commit of the same order. PUSH PENDING OPERATOR ORDER.
