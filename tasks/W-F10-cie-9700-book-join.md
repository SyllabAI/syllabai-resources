# tasks/W-F10-cie-9700-book-join.md

```yaml
task: W-F10
title: the CIE 9700 book-layer join — first CIE join lane (book-structure + book-join
      for the 4th-ed coursebook x cie-a-level-biology-2025-2027)
order_trace: 1a1f4cf26af71de1
order: "proceed" (operator, 2026-11-20) — executing the lane named in the W-F9
      push-confirm report ("ial-biology joins now UNBLOCKED (9700 PARSED landed)").
      Correction of record (T1): the Edexcel ial-biology-18 (YBI11) join stays
      honest-blocked on sourcing (CATALOG §4.2 state —, operator purchases, never
      agent-fetches, W-F7-T1 §7 law); the executable reading of the named lane is
      the CIE 9700 book-layer join (Lane C follow-on, now actionable — the quartet
      is PARSED and the join machinery of record applies).
lane: books rollout queue follow-on — join program (design authority: W-F4-T1
      schemas + join-key regimes J1-J6; emitter laws of record: W-F7-T1 M-1..M-7
      + the W-F8 M-8/M-9 figure-token exclusions)
status: W-F10-T1 COMPLETE 2026-11-20 — design of record filed at
  receipts/W-F10/W-F10-T1-design-of-record.md (probes of record cache/w-f10/probe.json,
  zero repo writes). W-F10-T2 COMPLETE 2026-11-20 — build staged (2 NEW artifacts under
  Official-Specifications/parsed/_derived/book_layer/cie-a-level-biology-2025-2027/);
  gates G-F10-B1..B6 ALL PASS (6/6, evidence cache/w-f10/); the records landing (this
  task file, T1/T2 receipts, the W-F9 push-confirm ride-alongs, the W-F9 task push
  clause, LEDGER Waves 55-56) follows as the next commit of the same order;
  PUSH PENDING OPERATOR ORDER (PAT rotation overdue — 11th+ transit of the same token).
```

## 1. Scope of record

The first CIE join lane: the 9700 4th-ed coursebook corpus (1971 chunks, W-F9 PARSED)
joined to the `cie-a-level-biology-2025-2027` spec of record (19 topics / 44
subsections / 257 points, W-F3/W-F6 parse of record). The probes of record
(cache/w-f10/probe.json + probe2-subns.json + probe3-admission.json) pin the
edition law: the book is the 4th ed (2014 printing,
ISBN 9781107636828) while the spec lane is 2025-2027 — the 19-topic structure carried
through the syllabus revision intact (J5 19/19: 15 EQUAL / 2 CONTAINS /
2 NUMBER_IDENTITY / 0 UNMATCHED), so the join is honest as a TOPIC-LEVEL mapping with
the edition disclosure carried on every row (N-8); the 5th ed (ISBN 9781108859028)
remains the upgrade candidate of record (lane README). The CIE coursebook family
prints no spec-reference codes — zero admitted spec chips under the full law stack
of record (probe2 classification + probe3 admission: the M-1 x M-8 x M-9 x M-2 +
row-scope stack admits zero; the book's internal chapter.t.s numbering structurally
occupies the same form; the J2 LO route is void at source) — the point-level routes
J2/J3 are honest zeros and the family law of record (the W-F8 M-11 analog for CIE)
is pinned.

## 2. Build of record (receipts/W-F10/W-F10-T2-build-receipt.json)

- Emitter `scripts/wf10_emit.py`: pure function of the pinned blobs at
  d9fdee974dfa7dc0694f26e1c7965a0e05350ee4 (corpus 1971 chunks + topics.json +
  spec_points.json + lane README sha pin); zero LLM, zero network, deterministic.
- book-structure--9700-coursebook.json (NEW, schema syllabai.book-structure/1.0):
  19 chapters (u0:c1..c19, corpus-registered page ranges pdf 11..499 / book 1..489,
  contiguous + non-overlapping) + 13 non-lesson sections of record (front matter,
  P1 pdf 256-276, P2 pdf 500-521, Appendices 1-2, Glossary, Index,
  Acknowledgements, exam advice x2, Answers SAQs/EOCQs, Recommended resources —
  the probe P1b cx title groups) + honest units [] (single-unit corpus u0; AS/A2
  scope carried from the spec side per point).
- book-join.json (NEW, schema syllabai.book-spec-join/1.0): 19 rows
  (chapter_key u0:c{n}), each row topic-mapped via the M-6 three-tier J5 law
  (basis recorded per row), spec_refs.topic {code, number, title, basis},
  spec_refs.subsections = the topic's subsections of record (44 across 19 rows),
  spec_refs.points = [] honest no_printed_key (N-3); join_key J5_TITLE_ADJUDICATED,
  verdict JOIN_TOPIC; coverage {topics_covered 19/19, subsections_listed 44/44,
  points_keyed 0/257 honest figure-void}; edition_disclosure on the header + rows.
- Gates G-F10-B1..B6 ALL PASS (6/6): B1 input pins (source sha256 ==
  lane README pin fa4954c8…, corpus/spec blobs at HEAD, probe2/probe3 resolve);
  B2 structure tiles (19/19 chapters contiguous, 13 cx groups disjoint, EOC
  21/21 = 19x1 + P1/P2); B3 join rows (independent J5 re-derivation == rows
  exactly, 19/19, zero UNMATCHED; every topic/subsection/point id resolves
  against the spec of record; subsections total 44); B4 figure-void law
  (full-stack admission M-1 x M-8 x M-9 x M-2 + row scope == ZERO admitted spec
  chips; M-1 raw admission 22, all resolved to internal numbering; LO route void
  at source; J4 re-run == 0/119); B5 surface (exactly 2 NEW files under
  book_layer/cie-a-level-biology-2025-2027/; zero spec-side/census/graph
  writes); B6 determinism (byte-identical re-run, sha256).

## 3. Write surface

- Official-Specifications/parsed/_derived/book_layer/cie-a-level-biology-2025-2027/
  book-structure--9700-coursebook.json (NEW) + book-join.json (NEW) +
- tasks/W-F10-cie-9700-book-join.md (NEW, this file) + receipts/W-F10/ (design doc
  + JSON receipts + worklogs) + ride-alongs (EXEC-1a1f4c6c31cd1601-push-confirm
  receipt + the W-F9 push-confirm worklog, append-only convention) +
  tasks/W-F9-cie-books-parse.md (M, push clause ride) + LEDGER.md append
  (Waves 55-56) + cache/w-f10/ (probes/gates, agent-side) + download/w-f10-swap/
  (staging, agent-side). Zero bundle mutations, zero census writes, zero graph
  writes, zero book-lane writes.

## 4. Honest leftovers (routed, not repaired)

- The Edexcel ial-biology-18 (YBI11) join: honest-blocked on sourcing (state —,
  operator purchases) — the correction of record for the W-F9 push-confirm
  report's "ial-biology joins now UNBLOCKED" phrasing.
- The other three CIE quartet joins (9702, 9701, 0625): NOT STARTED (each needs
  its own probe + design under the same laws; 0625 carries the D-2 ligature-loss
  class — the N-1 folding law applies).
- Point-level keys (J2/J3): honest zeros by family law (no printed codes) — no
  repair exists or is needed; serving consumes the topic-level spine.
- LLM fidelity polish for the 9700 corpus: NOT STARTED (quota-walled; pristine
  snapshots are the anchor-diff targets).
- INTEGRATED/LIVE for all four quartet books: the v2-repo/DB lever — not this
  repo's write face (CATALOG §1 state law).
