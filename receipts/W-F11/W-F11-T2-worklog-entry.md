# W-F11-T2 worklog entry (staged; lands with the W-F11 records commit)

- Wave: W-F11 (the CIE 9702 book-layer join — the first restructured-syllabus join)
- Trace of record: 1a1f524947d586d9 ("Proceed with next")
- Date: 2026-11-20

## What happened

T2 built the join artifacts from the pinned blobs at 9605a43a via
scripts/wf11_emit.py (zero LLM, zero network, deterministic, BUILD_TS pinned) and
staged them under download/w-f11-swap/:

- book-structure--9702-coursebook.json — 32 corpus-registered chapters
  (u0:c1..c32, pdf 13..540 / book 1..528, zero overlaps) + the 14 non-lesson cx
  groups (the P1-in-gap law: the single chapter-tile gap 251-269 IS the P1
  Practical skills at AS level range; chapters + cx tile pdf 1..743 completely) +
  honest units [] (single-unit lane u0).
- book-join.json — 32 rows: 15 JOIN_TOPIC (10 J5_EQUAL + 5 J5_CONTAINS under the
  N-2b longest-contained refinement) + 17 NO_TOPIC_MAPPING (the N-2c/N-7
  honest-row grain — no silent drops); the single N-4 J4 key ("state Ohm's law" ==
  9.3.5) rides the c11 row with its LO chunk pinned; coverage 14/25 topics,
  51 listed / 46 distinct subsections, 1/303 points, the partial-spine edition
  disclosure on the header and every row.

The independent gate runner (scripts/wf11t2_gates.py) re-derived everything from
the pinned blobs: B1 four-way source-pin match + corpus sha == the W-F9 receipt
pin; B2 tiles (zero overlaps, the N-9 gap law, 14 disjoint cx, envelope 1..743
minus the textless page {12}, book axis 1..528 zero holes, EOC 32/32); B3 join
rows (independent J5 re-derivation == rows exactly 10/5/0/17; 14 topics; 51/46
subsections; the J4 key resolves against the spec of record); B4
codes-void law (M-1 raw 17; the full stack admits ZERO — 7 M-8 window exclusions
including the N-3a plural-fold case, 1 N-3b self-reference exclusion, 9 row-scope
c0 exclusions; zero 3-part tokens; LO route void; J4 re-run exactly 1/255; P4b 517
classified); B5 surface (exactly the 2 NEW book_layer files + task + 5 receipts);
B6 determinism (byte-identical re-run). G-F11-B1..B6 ALL PASS (6/6) — evidence
cache/w-f11/gate-verdicts.json.

Landing: the build commit (2A) + the records commit (this task file, T1/T2
receipts, the W-F10 push-confirm ride-alongs, the W-F10 task push clause, LEDGER
Waves 57-58) follow as the two commits of the same order, via the zero-index
plumbing lander scripts/wf11_land.py; push of both commits PENDING OPERATOR ORDER
(PAT rotation overdue — 12th+ transit of the same token).
