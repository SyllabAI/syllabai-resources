# W-F10-T1 — Design of record: the CIE 9700 book-layer join (first CIE join lane)

Order trace 1a1f4cf26af71de1 ("proceed", 2026-11-20). Design authority: W-F4-T1
(schemas `syllabai.book-structure/1.0` + `syllabai.book-spec-join/1.0`, join-key
ladder J1-J6, coverage contract); emitter laws of record: W-F7-T1 M-1..M-7
(norm, RUN/SUFFIXED/TAIL admission, unit-consistency, M-6 J5 three-tier, CP
routing) + the W-F8 M-8/M-9 figure-token exclusions. This T1 pins the CIE
adaptations (N-laws), the probes of record, the gates, and the write surface.

## 1. Order reading + correction of record

The order executes the lane named in the W-F9 push-confirm report: "ial-biology
joins now UNBLOCKED (9700 PARSED landed)". T1 correction of record: the Edexcel
ial-biology-18 (YBI11) join stays honest-blocked on SOURCING (CATALOG §4.2 state
—, operator purchases — never agent-fetches, W-F7-T1 §7 law); the archive-path
segment `ial/biology` (books/cambridge-international/ial/biology/9700) is the CIE
9700 lane, which IS now actionable — the quartet is PARSED (W-F9) and the join
machinery of record applies. The executable reading is therefore the CIE 9700
book-layer join; this correction rides the records landing.

## 2. Inputs of record (all pinned at HEAD d9fdee974dfa7dc0694f26e1c7965a0e05350ee4)

- Corpus: books/cambridge-international/ial/biology/9700/parsed/
  cie_a_level_biology_9700_chunks_v1.jsonl (1971 chunks, 13-key v1 grammar;
  blob oid pinned in the probe inputs block)
- Spec of record: Official-Specifications/parsed/cie-a-level-biology-2025-2027/
  {topics.json, spec_points.json} — 19 topics / 44 subsections / 257 points,
  official_code t.s.p, scope AS Level/A Level per point (W-F3/W-F6 parse of record)
- Lane README source pin: sha256 fa4954c88855a587a63deeb2725f6abb22aed8b3551ed02462dfbf53c036bfe7
  (4th ed, 2014 printing, ISBN 9781107636828; 5th ed ISBN 9781108859028 = upgrade
  candidate note present)
- Probes of record: cache/w-f10/probe.json (P1 spine, P1b cx title groups,
  P2 spec census, P3 J5 adjudication, P4 printed-code census, P5 J4 equality,
  P6 mention census, P7 source pin)

## 3. Probe verdicts of record

- P1 spine: 19 content chapters (u0:c1..c19, chapter_no 1..19; pdf 11..499,
  book 1..489, contiguous + non-overlapping; per-chapter learning_outcomes x19,
  chapter_questions x19 = EOC anchored 21/21 with P1/P2) + the u0:cx bucket
  (chapter_no=None, 624 chunks).
- P1b cx title groups (13, disjoint pdf ranges): Front matter (1-10, 19),
  P1 Practical skills for AS (256-276, 58: body 49 + chapter_questions 1 + LO 1 +
  questions 5 + summary 2), P2 Planning, analysis and evaluation (500-521, 58),
  Appendix 1 (522), Appendix 2 (523), Glossary (524-535, 44), Index (536-543, 17),
  Acknowledgements (544-545, 7), exam advice x2 (547-561, 38 + 562-566, 12),
  Answers to SAQs (567-609, 151), Answers to EOCQs (610-673, 170),
  Recommended resources (674-696, 48). P1 sits exactly in the AS->A2 gap
  (c11 ends pdf 255, c12 starts pdf 277).
- P3 J5 three-tier (M-6, CIE adaptation: no unit-prefix strip — the corpus is a
  single-unit lane u0): **19/19 mapped, 0 UNMATCHED** — 15 J5_EQUAL, 2
  J5_CONTAINS (c9 "Gas exchange and smoking" vs T9 "Gas exchange"; c15
  "Coordination" vs T15 "Control and coordination"), 2 J5_NUMBER_IDENTITY_
  TITLE_VARIANT (c16 "Inherited change" = T16 "Inheritance"; c18 "Biodiversity,
  classification and conservation" = T18 "Classification, biodiversity and
  conservation"). The 4th-ed chapter structure = the 2025-2027 topic structure.
- P4 printed-code census (J2/J3 viability), AS AMENDED POST-GATE — the first
  probe's subsection-namespace check used a wrong key and silently passed; probe2
  (cache/w-f10/probe2-subns.json, classification) + probe3 (cache/w-f10/
  probe3-admission.json, the M-1/M-2 admission law) supersede it. Honest verdict:
  **zero admitted spec chips under the full law stack of record** — M-1 admission
  (RUN/SUFFIXED/TAIL) yields 22 raw chips; the 6 M-2-consistent TAIL survivors are
  the book's internal Table 1.2 / Box 7.1 / Figure 7.2 / Figure 8.3 / Figure 12.2 /
  Table 15.2 references (M-8 figure-window excludes all six); the 16 RUN survivors
  are M-2-inconsistent (topic number != chapter number) or out of row scope (the
  answers-section runs, c0); 198 post-exclusion 2-part candidates classified by
  probe2 as the book's internal box/figure/table/question/credit numbering or prose
  constants; zero 3-part tokens corpus-wide; the J2 LO route is void at the source
  (zero namespace tokens in all 21 LO chunks, zero coded LO line starts). The CIE
  coursebook family prints no spec-reference codes (the CIE analog of the W-F8
  M-11 IGCSE-family law), with the structural-collision disclosure: the book's
  internal chapter.t.s numbering occupies the same form.
- P5 J4 LO equality: 21 LO chunks / 119 bullet lines — **0 exact, 0 space-free**
  (the book paraphrases the learning outcomes; honest zero, W-F7 law verbatim).
- P6 mentions: syllabus x23, learning outcomes x28, practical x44, cross-link x7
  (routing evidence only).
- P7 source pin: probe-extracted sha256 == lane README pin == W-F9 build receipt pin.

## 4. Build-time laws (N-1..N-8, the CIE adaptations)

- **N-1 norm law**: wf7 norm() verbatim + ligature folding (ufb01->fi, ufb02->fl)
  — the 9700 damage census carries fi-glue 53 / fl-glue 13; both sides fold.
- **N-2 J5 law**: M-6 three-tier verbatim (EQUAL / CONTAINS / NUMBER_IDENTITY_
  TITLE_VARIANT / UNMATCHED), TOPIC_PREFIX strip applied defensively; basis
  recorded per row; zero-UNMATCHED is a gate (B3), not a repair target.
- **N-3 no-printed-codes law (CIE family)**: rows carry spec_refs.points = []
  with the honest no_printed_key note; J2/J3 recorded as honest zeros with the
  FULL-LAW-STACK evidence (probe2 classification + probe3 admission — see the
  amended P4 verdict; the M-1 x M-8 x M-9 x M-2 + row-scope stack admits zero
  spec chips); no chip rows are emitted.
- **N-4 J4 law**: recorded honest zero (P5); no LO-text rows.
- **N-5 J1 law**: not-applicable (no "SPECIFICATION REFERENCE" anchor family in
  CIE coursebooks); the P6 mention census is routing evidence, not keys.
- **N-6 J6 law**: not-applicable (cross-document page adjacency meaningless).
- **N-7 row grain + routing**: rows = the 19 topic chapters only; front matter,
  P1/P2 and all back-matter groups are honest no_spec_target (excluded from
  rows, carried as structure non_lesson_sections); P1/P2 carry the practicals-
  lane routing note (the W-F7 CP-routing analog; spec-side practicals of record
  = the graph practicals.yaml lane).
- **N-8 edition disclosure law**: book 4th ed (2014) vs spec 2025-2027 — the
  edition disclosure rides the join header AND every row (basis field already
  carries the J5 evidence); the 5th ed remains the upgrade candidate of record;
  the join is a TOPIC-LEVEL spine, and serving consumes it as such.

## 5. Artifacts (W-F4-T1 schema authority)

1. `book-structure--9700-coursebook.json` (NEW, syllabai.book-structure/1.0):
   qual `cie-a-level-biology-2025-2027`; book.key `9700-coursebook`; corpus pins
   (chunks_jsonl path + blob oid + 1971 + prefix law `c9700_v1_u{u}_c{c}_pdf{p}_{i}`);
   chapters x19 (key u0:c{n}, title, page_range_pdf, page_range_book, tier
   CORPUS_REGISTERED, evidence {chunk_ids, opener_page}, flags []);
   non_lesson_sections x13 (the P1b groups, each with pdf range + chunk counts);
   units [] (honest — single-unit corpus; AS/A2 scope carried from the spec side
   per point); notes (edition law, EOC 21/21, P1/P2 routing).
2. `book-join.json` (NEW, syllabai.book-spec-join/1.0): qual; lane
   `books/cambridge-international/ial/biology/9700`; spec_side {id, topics 19,
   subsections 44, points 257, source blobs}; join_keys status map (J5 ACTIVE
   three-tier; J2/J3 honest zero figure-void with P4 evidence; J4 honest zero;
   J1/J6 not-applicable); rows x19 {chapter_key, book_key, chapter_title,
   spec_refs {topic {code, number, title, basis}, subsections [{code, title}],
   points []}, join_key "J5_TITLE_ADJUDICATED", verdict "JOIN_TOPIC",
   evidence {chunk_ids, n_chunks, page_range_pdf}}; coverage {topics_covered
   19/19, subsections_listed 44/44, points_keyed 0/257 honest figure-void};
   edition_disclosure; generated_utc pinned; generator; inputs.

## 6. Gates (G-F10-B1..B6)

| gate | pass condition |
|---|---|
| B1 | input pins verified: probe sha256 == lane README pin == build receipt pin; corpus/spec blobs resolve at HEAD |
| B2 | structure tiles: 19 chapters contiguous + non-overlapping (pdf + book axes); 13 cx groups disjoint; EOC 21/21 carried |
| B3 | join rows: independent J5 re-derivation == rows exactly (19/19, 0 UNMATCHED); every topic/subsection/point id resolves against the spec of record; subsections total 44 |
| B4 | figure-void law: full-stack admission (M-1 x M-8 x M-9 x M-2 + row scope) == ZERO admitted spec chips; M-1 raw admission == 22; LO route void at source (0 namespace tokens, 0 coded line starts); J4 re-run == 0/119; zero 3-part tokens; probe2 (198 classified) + probe3 pinned |
| B5 | surface: build commit touches exactly the 2 NEW book_layer files; zero spec-side/census/graph/book-lane writes |
| B6 | determinism: byte-identical re-run (sha256 of both artifacts) |

## 7. Write surface

Build commit: the 2 NEW book_layer files only. Records commit: this task file +
receipts/W-F10/ + the W-F9 push-confirm ride-alongs (staged cache/w-f9/) +
tasks/W-F9-cie-books-parse.md (M, push clause) + LEDGER.md (M, Waves 55-56).
Zero bundle/census/graph/book-lane writes.

## 8. Honest leftovers

See tasks/W-F10-cie-9700-book-join.md §4 (YBI11 correction of record; the
9702/9701/0625 joins NOT STARTED; point-level keys honest zeros; LLM polish
quota-walled; INTEGRATED/LIVE = the v2 lever).
