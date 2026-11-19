# W-F8 — Book-alignment lane: the igcse trio V-lane completion (correction + deepening)

```yaml
wave: W-F8
tasks:
  - W-F8-T1   # Design of record (EXECUTED 2026-11-19, trace 1a1f3f29f14afce5) — scope of
              # the wave off the operator order "Proceed with the three W-F4-T2": the trio
              # igcse-chemistry/igcse-biology/igcse-physics (their W-F4-T2 joins are landed
              # and pushed; the open program is the unapplied W-F7 law set + the corrections
              # the probes prove); probes of record cache/w-f8/probe.json + probe2.json;
              # build-time laws M-8..M-11; gates G-F8-B1..B6 fixed; design filed receipts/W-F8/
  - W-F8-T2   # Build + land (EXECUTED 2026-11-19, same order) — zero-LLM emitter (pure
              # function of the pinned blobs at cf1c8378), swap staging download/w-f8-swap/,
              # gates G-F8-B1..B6 ALL PASS (6/6; determinism sha256 re-run), landed as one
              # revertible commit via zero-index plumbing
origin_trace: 1a1f3f29f14afce5
order_note: >-
  fired by the operator order "Proceed with the three W-F4-T2" (trace 1a1f3f29f14afce5) —
  the three igcse quals named in the Wave-50 push report's backlog. T1 + T2 same order
  (W-F6/W-F7 precedent); push by separate operator order.
design_authority: W-F4-T1 book-join design (schemas/ladder/verdict classes) + W-F7-T1
  design of record (laws M-1..M-7) — adopted unchanged; W-F8-T1 adds the IGCSE-family
  laws M-8..M-11 the probes force, and one correction the probes prove
inputs_of_record:
  - Official-Specifications/parsed/{igcse-chemistry,igcse-biology,igcse-physics}/
    {spec_points.json,topics.json} @ cf1c8378 (182/176/195 points, zero null/dupe codes)
  - books/.../chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl (1,234 chunks,
    parse_report_v3 of record) + biology/4bi1/..._v1.jsonl (863) + physics/4ph1/..._v1.jsonl
    (736) — corpus pins in the corrected joins' inputs and cache/w-f8/probe.json
  - the landed W-F4-T2 trio joins (records of record being corrected) @ cf1c8378
  - cache/w-f8/probe.json + probe2.json (probes of record) + gate-verdicts.json (G-F8 verdict)
status: W-F8-T1 COMPLETE 2026-11-19 — design of record filed at
  receipts/W-F8/W-F8-T1-design-of-record.md + JSON receipt + worklog entry.
  W-F8-T2 EXECUTED 2026-11-19 — the three book-join.json files corrected/deepened:
  igcse-chemistry (M): all 62 landed point entries removed (figure-caption numbers and
  numeric constants — the W-F4-T2 keys were false per L-2; errata block enumerates each
  removal with its re-derived context evidence; 'points_keyed' 7 -> 0 honest figure-void);
  J5 deepening +9 CONTAINS mappings with unit/topic vetting (SUB5 -> u1:c5 + u1:c6
  multi-chapter) -> subsections covered 18 -> 26/28; SUB10/SUB11 honest stays
  (reverse-direction only). igcse-physics (M): the 7 landed point entries removed (5
  figure_adjacent + 2 not_in_cited_evidence); 'points_keyed' 7 -> 0; J5 unchanged 22/30
  (the 8 'Units' SUBs have 0 title hits). igcse-biology (M): additive enrichment only —
  rows byte-preserved (the 172 J1 COURSE-STRUCTURE keys stand; the 4 uncovered codes stay
  honest no_printed_key with the 0-hit corpus search as evidence of record); J2/J3 route
  verdicts re-stated figure-void. Family law of record: the IGCSE student books print NO
  spec-reference codes (0 coded LO line starts across 2,833 chunks) — the point-level chip
  route is figure-void in this family (M-8 figure-token exclusion + M-9 zero-integer
  constants); gates G-F8-B1..B6 ALL PASS (6/6); the 3 files landed as build commit
  b6c09f8250740251fdc9b2329beaa8ec7155e458 (parent cf1c8378); the records landing (this task file, T1/T2 receipts, the
  W-F7 push-confirm ride-alongs, the W-F7 push clause, LEDGER Waves 50-52) follows as the
  next commit of the same order; PUSHED 2026-11-20 (trace 1a1f48dd27c13881): both commits
  on GitHub main via clean fast-forward cf1c8378..02325c5b, no force; pre-push anonymous
  ls-remote race gate tip-match PASS; post-push verification 7/7 PASS (tip/tree/ancestor/
  stability/url-clean/token-zero-hit/no-credential-files); push-confirm receipt
  EXEC-1a1f48dd27c13881-push-confirm.json rides the next landing per the append-only
  convention. Zero spec-side changes, zero
  books-lane changes, zero structure-file changes, zero census changes, no index files
  (single-book quals — the multi-book registration law does not fire).
write_surface: Official-Specifications/parsed/_derived/book_layer/{igcse-chemistry,
  igcse-physics,igcse-biology}/book-join.json (M x3, edited regions only) +
  tasks/W-F8-igcse-trio-join-completion.md (NEW, this file) + tasks/W-F7-book-alignment.md
  (M, push clause ride) + receipts/W-F8/ (design doc + JSON receipts + worklog entries) +
  receipts ride-along (EXEC-1a1f27218b046a15-push-confirm.json + the W-F7 push-confirm
  worklog, append-only convention) + LEDGER.md append + cache/w-f8/ (probes/gates) +
  download/w-f8-swap/ (staging, agent-side). Zero bundle mutations, zero census writes,
  zero books-lane writes.
```

## 1. Design of record (receipts/W-F8/W-F8-T1-design-of-record.md)

- Baseline errata of record: the Wave-50 backlog phrasing "staged/BUILT_NOT_JOINED"
  mischaracterized the trio — their W-F4-T2 joins were landed and pushed; the open
  program was the unapplied law set + corrections, which is what this wave ran.
- Findings F1-F6: the IGCSE books print no spec codes (figure-void); the landed 4CH1/4PH1
  point keys were figure-caption false positives (correction per M-11); 4BI1's J1 stands
  (ToC transcription of record); J5 deepening admits 8 of 10 uncovered 4CH1 SUBs; J1
  anchored probed-empty; no index files (single-book quals).
- Laws M-8 (figure-token exclusion, space-preserved + OCR-glue branches),
  M-9 (zero-integer constants), M-10 (trio J5 deepening with unit/topic vetting),
  M-11 (correction law — proven-false keys removed with per-entry evidence, old state in
  git history).

## 2. Build of record (receipts/W-F8/W-F8-T2-build-receipt.json)

- Emitter `scripts/wf8_emit_join.py`: reads ONLY pinned blobs; deterministic.
- Gates `scripts/wf8t2_gates.py`: G-F8-B1..B6 ALL PASS (6/6) — independent removal-set
  identity + window re-scan (own implementation), deepening re-derivation, resolution,
  surface exactly 3M, confinement (17 neighbor blobs pinned), determinism sha256 re-run.
- Landing: zero-index plumbing commit, surface exactly 3M; commit `b6c09f8250740251fdc9b2329beaa8ec7155e458`
  (parent cf1c8378). PUSHED 2026-11-20 (trace 1a1f48dd27c13881): clean fast-forward
  cf1c8378..02325c5b — build b6c09f82 + records 02325c5b both on GitHub main, no force;
  race gate tip-match + post-push 7/7 PASS; push-confirm receipt of record
  receipts/EXEC-1a1f48dd27c13881-push-confirm.json rides the next landing.
