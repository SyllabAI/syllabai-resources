# tasks/W-F11-cie-9702-book-join.md

```yaml
task: W-F11
title: the CIE 9702 book-layer join — the first restructured-syllabus join (book-structure
      + book-join for the 2nd-ed coursebook x cie-a-level-physics-2025-2027)
order_trace: 1a1f524947d586d9
order: "Proceed with next" (operator, 2026-11-20) — executing the first lane in the
      join program queue named by the W-F10 push-confirm receipt ("CIE quartet joins
      for 9702 / 9701 / 0625 NOT STARTED … the next actionable lanes", queue order of
      record: 9702 first). YBI11 stays honest-blocked on sourcing (CATALOG §4.2 state
      —, operator purchases, never agent-fetches, W-F7-T1 §7 law).
lane: books rollout queue — join program (design authority: W-F4-T1 schemas + join-key
      regimes J1-J6; emitter laws of record: W-F7-T1 M-1..M-7 + the W-F8 M-8/M-9
      exclusions + the W-F10 N-law CIE adaptations; the W-F11 amendments N-2b/N-2c/
      N-3a/N-3b/N-4/N-7/N-9 pinned in the design of record)
status: W-F11-T1 COMPLETE 2026-11-20 — design of record filed at
  receipts/W-F11/W-F11-T1-design-of-record.md (probes of record cache/w-f11/probe.json,
  zero repo writes). W-F11-T2 COMPLETE 2026-11-20 — build staged (2 NEW artifacts under
  Official-Specifications/parsed/_derived/book_layer/cie-a-level-physics-2025-2027/);
  gates G-F11-B1..B6 ALL PASS (6/6, evidence cache/w-f11/); the records landing (this
  task file, T1/T2 receipts, the W-F10 push-confirm ride-alongs, the W-F10 task push
  clause, LEDGER Waves 57-58) follows as the next commit of the same order;
  PUSH PENDING OPERATOR ORDER (PAT rotation overdue — 12th+ transit of the same token).
```

## 1. Scope of record

The second CIE join lane and the first RESTRUCTURED-SYLLABUS join: the 9702 2nd-ed
coursebook corpus (2046 chunks, W-F9 PARSED, source sha256 fa3e5ed2…, 2016 syllabus
line) joined to the `cie-a-level-physics-2025-2027` spec of record (25 topics / 76
subsections / 303 points, W-F3/W-F6 parse of record). UNLIKE the 9700 case (whose
19-topic structure carried through the revision intact), the 2025-2027 revision
RESTRUCTURED the topic map: the 2016-line book's 32 chapters do not coincide with
the 25 spec topics. The probes of record (cache/w-f11/probe.json) pin the honest
partial mapping: 15/32 chapters title-evidenced (10 J5_EQUAL + 5 J5_CONTAINS under
the N-2b longest-contained refinement) onto 14 distinct topics; 17 chapters carry
honest NO_TOPIC_MAPPING rows (N-2c) — dropped subject areas ("Communications
systems", "Electronics"), consolidated splits (the electricity chapters, thermal
physics), and renames without a title-evidenced mapping. Tier 3 (number identity)
fires zero times — the 32-vs-25 number axes diverge and the title-variant
requirement correctly rejects the false pairings. The edition disclosure (2nd ed vs
the 2025-2027 lane; 3rd ed ISBN 9781108859035 = the CATALOG §4.3 upgrade candidate)
rides the join header AND every row (N-8): the join is a PARTIAL topic-level spine
consumed as such.

## 2. Build of record (receipts/W-F11/W-F11-T2-build-receipt.json)

- Emitter `scripts/wf11_emit.py`: pure function of the pinned blobs at
  9605a43a9e7a911da86a350fe85d1008b97e76b7 (corpus 2046 chunks + topics.json +
  spec_points.json + lane README sha pin); zero LLM, zero network, deterministic.
- book-structure--9702-coursebook.json (NEW, schema syllabai.book-structure/1.0):
  32 chapters (u0:c1..c32, corpus-registered page ranges pdf 13..540 / book 1..528,
  zero overlaps) + 14 non-lesson sections of record (the probe P1b cx title groups;
  the envelope of chapters + cx tiles pdf 1..743 except the single textless page
  12 of record (pre-chapter blank — no text, no chunk, outside every envelope; pdf
  2 is textless inside the front-matter envelope 1-11); the N-9 law: exactly one
  chapter-tile
  gap 251-269 == the P1 Practical skills at AS level range, the W-F10 P1-in-gap law
  repeating) + honest units [] (single-unit corpus u0; AS/A2 scope carried from the
  spec side per point) + notes (page law book = pdf - 12, EOC 32/32 with 37
  chapter_questions chunks, edition law, damage-census fold, P1/P2 routing).
- book-join.json (NEW, schema syllabai.book-spec-join/1.0): 32 rows
  (chapter_key u0:c{n}) — 15 verdict JOIN_TOPIC (topic-mapped via the M-6 three-tier
  J5 law with the N-2b refinement, basis recorded per row, spec_refs.subsections =
  the mapped topic's subsections of record — 51 listed across rows / 46 distinct of
  76) + 17 verdict NO_TOPIC_MAPPING (spec_refs.topic null, flags ["no_title_match"],
  the N-7 all-chapters row grain — no silent drops); spec_refs.points = [] on 31
  rows and the single N-4 J4 key on c11 ("state Ohm's law" ==
  CIE_A_LEVEL_PHYSICS_2025_2027:9.3.5, LO chunk pinned, flags +["j4_point_keyed"] —
  the family amendment: zero printed CODES, one verbatim TEXT equality);
  coverage {chapters 32, mapped 15, unmatched 17 (titles enumerated), topics_covered
  14/25, subsections_listed 51 / distinct 46 / total 76, points_keyed 1/303};
  edition_disclosure on the header + rows.
- Gates G-F11-B1..B6 ALL PASS (6/6): B1 input pins (four-way source-sha match ==
  fa3e5ed2…, corpus file sha256 == 93552fed… == the W-F9 receipt pin, blobs resolve
  at HEAD); B2 structure tiles (32 chapters zero-overlap, the N-9 gap law, 14 cx
  disjoint, envelope 1..743 minus the textless page {12}, book axis 1..528 zero
  holes, EOC 32/32); B3 join rows (independent J5 re-derivation
  == rows exactly 10/5/0/17, 14 topics, 51/46 subsections, the J4 key resolves);
  B4 codes-void law (M-1 raw 17 = TAIL 6 + RUN 11 + SUFFIXED 0; full stack admits
  ZERO — M-8 window 7 incl. the N-3a plural fold ("Figures 9.1, 9.2 and 9.3") +
  N-3b self-reference 1 ("9.2" in c9's figure-credit context, t == host chapter) +
  row-scope 9 (P1/P2 measurement values, Acknowledgements photo credits); zero
  3-part tokens; LO route void of codes; J4 re-run == exactly 1/255; P4b 517
  classified); B5 surface (exactly 2 NEW book_layer files; zero spec-side/census/
  graph writes); B6 determinism (byte-identical re-run, sha256).

## 3. Write surface

- Official-Specifications/parsed/_derived/book_layer/cie-a-level-physics-2025-2027/
  book-structure--9702-coursebook.json (NEW) + book-join.json (NEW) +
- tasks/W-F11-cie-9702-book-join.md (NEW, this file) + receipts/W-F11/ (design doc
  + JSON receipts + worklogs) + ride-alongs (EXEC-1a1f51885dc00ce5-push-confirm
  receipt + the W-F10 push-confirm worklog, append-only convention) +
  tasks/W-F10-cie-9700-book-join.md (M, push clause ride) + LEDGER.md append
  (Waves 57-58) + cache/w-f11/ (probes/gates, agent-side) + download/w-f11-swap/
  (staging, agent-side). Zero bundle mutations, zero census writes, zero graph
  writes, zero book-lane writes.

## 4. Honest leftovers (routed, not repaired)

- The 17 NO_TOPIC_MAPPING chapters: honest rows, no repair in this lane — the
  levers are the 3rd-ed upgrade corpus (CATALOG §4.3, operator purchase) or an
  operator-ordered semantic mapping lane; neither exists or is ordered.
- The other two CIE quartet joins (9701, 0625): NOT STARTED (each needs its own
  probe + design under the same laws; 0625 carries the D-2 ligature-loss class —
  the N-1 folding law applies).
- Point-level keys beyond 9.3.5: the codes routes (J2/J3) are honest zeros by the
  family law with the full-stack evidence — no repair exists or is needed; serving
  consumes the topic-level spine plus the single keyed point.
- LLM fidelity polish for the 9702 corpus: NOT STARTED (quota-walled; the pristine
  snapshot is the anchor-diff target).
- INTEGRATED/LIVE for the quartet: the v2-repo/DB lever — not this repo's write
  face (CATALOG §1 state law).
