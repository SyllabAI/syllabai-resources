# W-F11-T1 (9701) worklog entry (staged; rides the Wave-62 records landing)

- Wave: W-F11-T1 (the 9701 design stage — append-only records of record)
- Trace of record: 1a1fbb71dc98ef81 (operator order "Proceed", 2026-11-21);
  probe traces of record: 1a1f93bb6424e909 + 1a1fa58df8d73e4d (remote-only,
  sandbox outage)
- Date: 2026-11-21

## What happened

The 9701 probe ran REMOTE-ONLY across the sandbox outage (traces
1a1f93bb6424e909 + 1a1fa58df8d73e4d — anonymous GitHub API reads at the then
tips): the lane was found PARSED (corpus v1 1083 chunks + .pristine +
full_book_textlayer.md + parse_report_v1.json at
books/cambridge-international/ial/chemistry/9701/parsed/), the W-F9
reconcile ALL CHECKS PASSED (18/18, trace 1a1f4951330253b5), and the
D-1..D-6 decisions + spec-side pins were extracted. This round (sandbox
recovered) RE-VERIFIED every pin by direct blob reads at the tip of record
1202aaf3 (scripts/wf62_stage_build.py — the probe gate battery P1..P8,
ALL PASS, computed results embedded in receipts/W-F11/
W-F11-T1-9701-probe-manifest.json) and staged the T1 set: the probe
manifest + the design of record (receipts/W-F11/W-F11-T1-9701-design-of-record.md)
+ this worklog + the task file (tasks/W-F11-cie-9701-book-join.md). Zero
repo writes at probe time; the only repo writes this round are the Wave-62
records landing itself (this T1 set + the W-F11d push-confirm ride-alongs +
the LEDGER Wave-62 section + the deea76f2 task clause), composed on the
advanced tip per the Wave-46 re-base law.

## The probe facts of record (re-verified this round)

- corpus census: 1083 chunks; content types == the parse report exactly
  (body 668 / learning_objectives 36 / before_you_start 64 /
  science_in_context 1 / reflection 70 / chapter_questions 86 /
  self_evaluation 38 / activity 27 / worked_example 58 / summary 35);
  chunk ids c9701_v1_u0_c{n}_pdf{p}_{i} over c0..c30 (31 keys, 62/21/36/79/50/36/38/34/63/26/35/20/23/15/32/31/18/23/26/35/58/48/46/48/36/25/21/23/26/18/31
  = 1083); unit None on all chunks (single-unit corpus u0).
- pristine byte-identity: the .pristine snapshot's sha256 == the chunks
  jsonl's sha256 (774d616c…, re-computed from the tip blobs).
- spec side: topics.json counts {topics 35, subsections 91};
  spec_points.json counts {spec_points 356, practicals 0, flagged 356};
  AS Level 21 / A Level 14 topic scope split; family int_statements,
  issue 2; sme_courses cie-a-level-chemistry-25 + cie-as-chemistry-25.
- the item-(a) verification also executed this round
  (scripts/wf11g_verify_orphan_pins.sh, 8 sections A..H): the core proofs
  ALL PASS (pin resolution per the race-rebuild receipt V7/V10, orphan
  non-ancestry exit 1, 5-path blob identity, staged-set sha256 pins); two
  honest notes — the remote tip had advanced deea76f2..1202aaf3 (96 paths,
  all under Videos/, zero surface overlap — the Wave-46 recomposition
  applies to THIS landing), and the staged wf11e commit-msg draft predates
  the landed message (the landed message carries the BASE-ADVANCE NOTE +
  the f-string flaw).

## Honest state

W-F11-T2 (the 9701 join build) NOT STARTED — it follows as its own ordered
wave on the v1 corpus. The push of the Wave-62 landing executes on any
operator-delegated credential per the standing waiver (trace
1a1f7e7bd7a43f81); no credential was delegated this round, so the commit of
record is pinned locally (refs/local/wf11f-ridealong-1a1fbb71dc98ef81) and the push is NOT attempted
anonymously.
