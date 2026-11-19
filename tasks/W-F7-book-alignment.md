# W-F7 — Book-alignment lane: the ial-chemistry V-lane corroboration book-join

```yaml
wave: W-F7
tasks:
  - W-F7-T1   # Design of record (EXECUTED 2026-11-18, trace 1a1ef43dcfda2a59) — scope of
              # the lane off the W-F4-T1 eligibility ledger (exactly one actionable item:
              # the ial-chemistry join; everything else honest-blocked), probes of record
              # J1-J5 (cache/w-f7/probe.json + probe2.json), build-time laws M-1..M-7,
              # gates G-F7-B1..B6 fixed; design filed receipts/W-F7/
  - W-F7-T2   # Build + land (EXECUTED 2026-11-18, same order) — zero-LLM emitter (pure
              # function of the pinned blobs), swap staging download/w-f7-swap/, gates
              # G-F7-B1..B6 ALL PASS (23/23; determinism sha256 re-run), landed as one
              # revertible commit via zero-index plumbing
origin_trace: 1a1ef43dcfda2a59
order_note: >-
  fired by the operator order "book-alignment lane" (trace 1a1ef43dcfda2a59) — the backlog
  lane named in the Wave-43/46 push-confirm reports. T1 + T2 same order (W-F6 precedent);
  push by separate operator order.
design_authority: W-F4-T1 book-join design of record (schemas/ladder/verdict classes
  adopted unchanged); W-F7-T1 adds the ial-chemistry build-time laws only
inputs_of_record:
  - Official-Specifications/parsed/ial-chemistry/{spec_points.json,topics.json} @ 5608e2e1
    (319 points, official_code 1.1-20.5 all present+unique; 20 content topics)
  - books/.../ych11/...sb1_chunks_v1.jsonl (blob 5924f3d9) + ych12/...sb2_chunks_v2.jsonl
    (blob 7a22b6b9) — the Wave-37 corpus pins of record, object-store verified
  - the landed Wave-37 book_layer/ial-chemistry/ structures + index (join deferral of record)
  - cache/w-f7/probe.json + probe2.json (probes of record) + gate-verdicts.json (G-F7 verdict)
status: W-F7-T1 COMPLETE 2026-11-18 — design of record filed at
  receipts/W-F7/W-F7-T1-design-of-record.md + JSON receipt + worklog entry.
  W-F7-T2 EXECUTED 2026-11-18 — book-join.json emitted (54 rows: 35 SB1 + 19 SB2; every row
  topic-mapped via M-6: 42 J5_EQUAL + 11 J5_CONTAINS + 1 J5_NUMBER_IDENTITY variant,
  as-printed pairs; point-level corroboration 48/319 codes keyed via J2 7 chips + J3 69
  margin chips with the conservative RUN/SUFFIXED/TAIL admission law, honest
  no_printed_key for the rest; J4 0/714 honest zero; J1 anchored list recorded topic-level
  verbatim; CP chips routed practicals_lane x8 chapters; 31 printed sub-item resolutions);
  book-layer-index.json rewritten (join_status JOINED + the Wave-37 no_book_units errata
  corrected with the exam_unit_note of record; books/schema/qual byte-preserved); gates
  G-F7-B1..B6 PASS (23/23); the 2 files landed as commit 3bfbe69f179a06c560fc0c489b2cf4d9eb92fbf7 (parent 5608e2e1);
  the records landing (this task file, T1/T2 receipts, the Wave-46/47 ride-alongs, the W-F6
  push clause, LEDGER Waves 47-49) follows as the next commit of the same order;
  BOTH COMMITS PUSHED 2026-11-19 (trace 1a1f27218b046a15): fast-forward
  5608e2e1..cf1c8378, exit 0, no race, no force; post-push verified (remote tree ==
  local tree f7982423, ancestry, URL clean, token zero-persist); push-confirm receipt
  of record receipts/EXEC-1a1f27218b046a15-push-confirm.json. Zero spec-side changes,
  zero books-lane changes, zero structure-file changes, zero census changes.
write_surface: Official-Specifications/parsed/_derived/book_layer/ial-chemistry/
  book-join.json (NEW) + book-layer-index.json (M, edited regions only) +
  tasks/W-F7-book-alignment.md (NEW, this file) + tasks/W-F6-cie-graph-yamls.md (M, push
  clause ride) + receipts/W-F7/ (design doc + JSON receipts + worklog entries) + receipts
  ride-along (Wave-46/47 push + landing receipts + worklogs, append-only convention) +
  LEDGER.md append + cache/w-f7/ (probes/gates) + download/w-f7-swap/ (staging, agent-side).
  Zero bundle mutations, zero census writes, zero books-lane writes.
```

## 1. Design of record (receipts/W-F7/W-F7-T1-design-of-record.md)

- Scope: the lane completes the W-F4-T1 Lane B join program — exactly ONE actionable item
  (the ial-chemistry join, deferred BUILT_NOT_JOINED at Wave 37 with both deferral
  conditions now resolved); everything else honest-blocked (10 NO_BOOK quals, ial-biology,
  CIE SOURCE_ONLY = Lane C follow-on).
- Laws M-1..M-7 pinned from the probes: the conservative margin-chip admission
  (RUN/SUFFIXED/TAIL + ratio/letter-glue exclusions + unit-consistency), sub-item ordinal
  resolution (as-printed kept), CP routing, the J1 anchor law (topic-level, L-2), the M-6
  three-tier J5 topic law, the row grain (54 manifest chapters).
- Errata of record: the Wave-37 no_book_units namespace conflation (corrected by the index
  rewrite); the T19 spec-title truncation + W-F4-T2 J2 probe count (routed, not repaired).

## 2. Build of record (receipts/W-F7/W-F7-T2-build-receipt.json)

- Emitter `scripts/wf7_emit_join.py`: reads ONLY pinned blobs; deterministic.
- Gates `scripts/wf7t2_gates.py`: G-F7-B1..B6 ALL PASS (23/23) — independent chip
  re-derivation == rows exactly, M-law verification, coverage accounting, index edited-region
  confinement, structure files byte-untouched, determinism sha256 re-run.
- Landing: zero-index plumbing commit, surface exactly 1A + 1M; commit `3bfbe69f179a06c560fc0c489b2cf4d9eb92fbf7`
  (parent 5608e2e1). Pushed to GitHub main 2026-11-19 (trace 1a1f27218b046a15),
  fast-forward 5608e2e1..cf1c8378 with the records landing commit cf1c8378
  (parent 3bfbe69f); no race, no force; post-push verification ALL PASS
  (receipts/EXEC-1a1f27218b046a15-push-confirm.json, riding the next records
  landing with this clause and the LEDGER Wave-50 section).
