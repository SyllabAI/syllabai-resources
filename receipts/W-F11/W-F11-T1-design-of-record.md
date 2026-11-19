# W-F11-T1 — Design of record: the CIE 9702 book-layer join (the first restructured-syllabus join)

Order trace 1a1f524947d586d9 ("Proceed with next", 2026-11-20). Design authority:
W-F4-T1 (schemas `syllabai.book-structure/1.0` + `syllabai.book-spec-join/1.0`,
join-key ladder J1-J6, coverage contract); emitter laws of record: W-F7-T1 M-1..M-7
+ the W-F8 M-8/M-9 exclusions + the W-F10 N-law CIE adaptations. This T1 pins the
9702 adaptations (N-2b/N-2c, M-8' plural fold, the self-reference exclusion, the
N-4 J4 amendment), the probes of record, the gates, and the write surface.

## 1. Order reading

The order executes the next actionable lane in the join program queue as reported
by the W-F10 push-confirm receipt of record: "CIE quartet joins for 9702 / 9701 /
0625 NOT STARTED (each needs its own probe + design under the same laws...) — the
next actionable lanes". The queue order of record names 9702 first; this wave is
therefore the CIE 9702 book-layer join (the 2nd-ed coursebook corpus x the
`cie-a-level-physics-2025-2027` spec of record). No sourcing correction is needed
this time — the lane is a CIE lane with a PARSED corpus (W-F9). The Edexcel
ial-biology-18 (YBI11) join stays honest-blocked on sourcing (CATALOG section 4.2
state em-dash; operator purchases, never agent-fetches, W-F7-T1 section 7 law).
The remaining lanes (9701, 0625) stay NOT STARTED — each needs its own probes.

## 2. Inputs of record (all pinned at HEAD 9605a43a9e7a911da86a350fe85d1008b97e76b7)

- Corpus: books/cambridge-international/ial/physics/9702/parsed/
  cie_a_level_physics_9702_chunks_v1.jsonl (2046 chunks, 13-key v1 grammar;
  blob oid 980210bca91dcd84328ea7c629c2f03767518bc5; file sha256 93552fed4f73a204
  0de566086f0130abf287185569b02cc9e93999005a84806a == the W-F9 T2 build receipt pin)
- Spec of record: Official-Specifications/parsed/cie-a-level-physics-2025-2027/
  {topics.json, spec_points.json} — 25 topics / 76 subsections (t.s codes) /
  303 points (t.s.p official_codes), scope AS Level/A Level per point
  (W-F3/W-F6 parse of record)
- Lane README source pin: sha256 fa3e5ed25da0c3c1217959d50144e8e7291d09851ad8298bda
  5df2839e097ae6 (2nd edition, Sang/Jones/Chadha/Woodside, CIE 9702 2016 syllabus
  line, 744 pp; CATALOG section 4.3: 3rd ed ISBN 9781108859035 = upgrade candidate)
- Probes of record: cache/w-f11/probe.json (P1 spine + contiguity, P1b cx groups,
  P2 spec census, P3 J5 adjudication with the naive-vs-refined collision record,
  P4 M-1 admission with per-chip exclusion evidence, P4b 2-part classification,
  P4c 3-part census, P5 J4 equality, P6 mentions, P7 pins) — single probe of
  record; script scripts/wf11_probe.py (zero-LLM, zero-network, zero repo writes).
  NOTE: the W-F10 first-P4 official_code key bug is known and avoided (the
  subsection namespace reads s["code"] everywhere).

## 3. Probe verdicts of record

- P1 spine: 32 content chapters (u0:c1..c32; unit_no None corpus-wide — a
  single-unit lane u0; honest units []), pdf 13..540 / book 1..528, ZERO overlaps;
  exactly ONE pdf gap 251..269 and ONE book gap 239..257 — both filled exactly by
  the P1 cx group (N-9, the 9700 P1-in-gap law repeating); learning_outcomes x34
  (32 chapter openers + P1 + P2 per the D-3 opener law); chapter_questions x37
  with all 32 chapters anchored (EOC 32/32 — c12 and c21 each carry a second
  set; 3 cx question chunks sit in P1/P2).
- P1b cx title groups: 14, pairwise disjoint on pdf — Front matter (1-11, 15),
  P1 Practical skills at AS level (251-269, 61), P2 Planning, analysis and
  evaluation (541-553, 39), Appendix 1/2/3 (554/555-556/557), Glossary (558-566,
  30), Index (567-575, 17), Acknowledgements (576, 4), Advice on how to revise
  (577-584, 22), Introduction to the examination (585-587, 11), Answers to SAQs
  (588-645, 151), Answers to EOC questions (646-711, 168), Recommended resources
  (712-743, 44). The min-max envelope of chapters + cx tiles pdf 1..743 except the
  single TEXTLESS page 12 of record (pre-chapter blank — no text, no chunk,
  outside every envelope; pdf 2 is textless INSIDE the front-matter envelope 1-11);
  the book axis tiles 1..528 with zero holes.
- P2 spec side: 25 topics T1-T25 / 76 subsections / 303 points.
- P3 J5 three-tier (M-6) with the longest-contained refinement (N-2b): **10 EQUAL +
  5 CONTAINS + 0 NUMBER_IDENTITY + 17 UNMATCHED** across the 32 chapters; 14
  distinct topics covered. The refinement resolves exactly one collision the naive
  first-match law would mis-map (c14 "Superposition of waves": naive -> T7 "Waves",
  refined -> T8 "Superposition" — the longest contained spec title); the full
  naive-vs-refined diff is pinned in the probe. Tier 3 fires ZERO times: the 32 vs
  25 number axes diverge (e.g. book c17 "Circular motion" sits at spec T17
  "Oscillations" — a false pairing the title-variant requirement correctly
  rejects); every unmatched title is honest (e.g. c20 "Communications systems" and
  c25 "Electronics" — dropped from the 2025-2027 syllabus; c2 "Accelerated motion",
  c6 "Momentum", c7 "Matter and materials", c9-c12 electricity split, c16
  "Radioactivity", c21 "Thermal physics", c23 "Coulomb's law", c27 "Charged
  particles", c28 "Electromagnetic induction", c32 "Medical imaging" — 2016-line
  chapter structure the 2025-2027 restructure consolidated or renamed without a
  title-evidenced mapping).
- P4 printed-code census (J2/J3 viability): M-1 conservative admission (RUN /
  SUFFIXED / TAIL) yields **17 raw chips (TAIL 6 + RUN 11 + SUFFIXED 0)**; the
  full law stack of record admits **ZERO spec chips** — per-chip exclusion
  evidence pinned in the probe: 7 excluded by the M-8 figure-window (Figure 2.1 /
  Figure 4.1 / Table 11.2 / Box 14.1 / Box 15.1 / Table 24.3 / "as shown in
  Figures 9.1, 9.2 and 9.3" — the last requiring the M-8' plural-fold amendment
  N-3a), 1 excluded by the self-reference law N-3b ("9.2" inside chapter c9's
  figure-credit context — the token's topic number equals the host chapter number,
  the book's own internal chapter.t.s numbering), 9 excluded by row scope (c0:
  the P1/P2 practical-worksheet measurement values "20.5, 20.5" / "12.1 12.1 s"
  and the Acknowledgements photo-credit lists). M-9 zero-integer excludes none
  additionally. **Zero 3-part tokens corpus-wide** (P4c empty census). The J2 LO
  route is void at the source: zero admitted chips in all 34 LO chunks and zero
  coded LO line starts. P4b: 517 corpus-wide 2-part namespace survivors classified
  (the measurement-value + internal box/figure/table/question + photo-credit
  classes; leading-word census pinned — a PHYSICS corpus structurally collides
  with the t.s namespace far more than the biology one: answers_eoc 133,
  answers_saqs 115, body 151, acknowledgements 42).
- P5 J4 LO equality: 34 LO chunks / 255 bullet lines — **exactly 1 exact match**
  (space-free diagnostic 0): the c11 LO line "state Ohm's law" ==
  spec point CIE_A_LEVEL_PHYSICS_2025_2027:9.3.5 (official_code 9.3.5, topic 9
  Electricity, subsection 9.3, scope AS Level). This is the W-F11 family
  amendment: the CIE no-printed-codes family law holds for the CODE routes
  (J1/J2/J3), and the J4 TEXT route carries exactly one verbatim equality —
  keyed under the c11 row (N-4).
- P6 mentions: syllabus x19, learning outcomes x37, practical x40
  (routing evidence only).
- P7 source pins: probe-extracted sha256 == lane README pin == parse report pin ==
  W-F9 T2 build receipt pin (fa3e5ed2...); corpus file sha256 == the W-F9 receipt's
  corpus pin (93552fed...); CATALOG section 2 #5 (cie-a-level-physics-25) +
  section 4.3 row pinned.

## 4. Build-time laws (the 9702 adaptations)

- **N-1 norm law**: wf7/wf10 norm() verbatim + ligature folding (ufb01->fi,
  ufb02->fl) — the 9702 damage census (fi-glue 101 / fl-glue 33 / double-space
  596 / ligature-char 2, W-F9 parse report) folds on both sides.
- **N-2 J5 law**: M-6 three-tier verbatim (EQUAL / CONTAINS /
  NUMBER_IDENTITY_TITLE_VARIANT / UNMATCHED), TOPIC_PREFIX strip defensive, basis
  recorded per row. **N-2b (new, longest-contained)**: within the CONTAINS tier,
  the mapped topic is the LONGEST contained spec title (tie -> lowest topic
  number) — the naive first-match law is preserved in the probe as the comparison
  record (exactly one divergence: c14 -> T8 not T7). **N-2c (new, honest
  UNMATCHED rows)**: chapters with no title-evidenced topic carry verdict
  NO_TOPIC_MAPPING with spec_refs.topic = null — no number-identity fabrication,
  no semantic repair (tier 3 fires 0 times here).
- **N-3 no-printed-codes law (CIE family, code routes)**: J1/J2/J3 recorded as
  honest zeros with the full-law-stack evidence (P4 + P4b + P4c); rows carry
  spec_refs.points = [] EXCEPT where the N-4 J4 route keys a point; no chip rows.
  **N-3a (M-8' plural fold)**: the figure-window exclusion folds plural forms
  (leading word "figures" -> "figure") — pinned on the "Figures 9.1, 9.2 and 9.3"
  case. **N-3b (self-reference exclusion)**: a t.s token whose topic number equals
  the host chunk's chapter_no is the book's internal chapter.t.s numbering, not a
  spec chip — the structural-collision disclosure of W-F10 turned into a
  deterministic exclusion (evidence: all 8 self-consistent tokens in this corpus
  are Figure/Table/Box/credit references).
- **N-4 J4 law (ACTIVE with one)**: J4_LO_TEXT_EQUALITY is no longer a pure zero
  for 9702 — exactly 1/255 verbatim; the keyed point rides the host chapter's row
  (c11) as spec_refs.points = [{id, official_code, text, route, evidence}] with
  the LO chunk id pinned; coverage.points_keyed = 1/303. This amends the family
  law honestly: zero PRINTED CODES, one verbatim TEXT equality.
- **N-5 J1 law**: not applicable (no "SPECIFICATION REFERENCE" anchor family;
  P6 mentions are routing evidence).
- **N-6 J6 law**: not applicable (cross-document page adjacency meaningless).
- **N-7 row grain (revised for the restructured case)**: rows = ALL 32 content
  chapters (15 verdict JOIN_TOPIC + 17 verdict NO_TOPIC_MAPPING, flags
  ["no_title_match"] plus ["j4_point_keyed"] on c11) — the W-F10 rows-only-mapped
  grain would silently drop 17 chapters, and the W-F8 no-silent-drops law (D-6
  analog) forbids that; front matter, P1/P2 and all back-matter cx groups stay
  structure-only (non_lesson_sections), with the P1/P2 practicals-lane routing
  note carried (the W-F7 CP-routing analog).
- **N-8 edition disclosure law**: book 2nd ed (2016 syllabus line) vs spec
  2025-2027 — UNLIKE the 9700 case, the syllabus revision RESTRUCTURED the topic
  map (25 topics vs 32 chapters); the join is a PARTIAL topic-level spine
  (15/32 rows title-evidenced, 14/25 topics covered at title level, 1/303 points
  keyed via J4) consumed as such, with the disclosure on the header AND every row
  (basis field / flags); the 3rd ed (ISBN 9781108859035, CATALOG section 4.3)
  remains the upgrade candidate of record.
- **N-9 P1-in-gap tile law**: the 32-chapter pdf tile carries exactly one gap
  (251..269) and the book tile exactly one gap (239..257), each filled exactly by
  the P1 Practical skills at AS level cx group (the W-F10 P1-in-gap law
  repeating); P2 sits after c32's end (541 > 540).

## 5. Artifacts (W-F4-T1 schema authority)

1. `book-structure--9702-coursebook.json` (NEW, syllabai.book-structure/1.0):
   qual `cie-a-level-physics-2025-2027`; book.key `9702-coursebook`; corpus pins
   (chunks_jsonl path + blob oid + 2046 + prefix law
   `c9702_v1_u{unit|0}_c{chapter|0}_pdf{pdfpage:03d}_{n:04d}`); chapters x32
   (key u0:c{n}, title, page_range_pdf, page_range_book, tier CORPUS_REGISTERED,
   evidence {chunk_ids, opener_page}, flags []); non_lesson_sections x14 (the P1b
   groups, each with pdf range + chunk counts + content types); units [] (honest —
   single-unit corpus; AS/A2 scope carried from the spec side per point); notes
   (page law book = pdf - 12, EOC 32/32, the N-9 P1-in-gap law, the edition law,
   the damage census fold, P1/P2 routing).
2. `book-join.json` (NEW, syllabai.book-spec-join/1.0): qual; lane
   `books/cambridge-international/ial/physics/9702`; spec_side {id, topics 25,
   subsections 76, points 303, source blobs}; join_keys status map (J5 ACTIVE
   three-tier + N-2b refinement; J2/J3 honest zero codes-void with the P4
   full-stack evidence; J4 ACTIVE with exactly 1/255 (the N-4 amendment); J1/J6
   not-applicable); rows x32 {chapter_key, book_key, chapter_title, spec_refs
   {topic {code, number, title, basis} | null, subsections [{code, title}],
   points [] | [the J4 key]}, join_key "J5_TITLE_ADJUDICATED", verdict
   "JOIN_TOPIC" | "NO_TOPIC_MAPPING", evidence {chunk_ids, n_chunks,
   page_range_pdf, page_range_book, lo_chunk}, flags}; coverage {chapters_total 32,
   chapters_mapped 15, unmatched_chapters 17, unmatched_chapter_titles [17],
   topics_covered 14, topics_total 25, subsections_listed 51,
   subsections_distinct_covered 46, subsections_total 76, points_keyed 1,
   points_total 303, points_keyed_note (the N-4 amendment + evidence),
   topics_covered_note (the N-2c/N-8 partial-spine law)}; edition_disclosure;
   generated_utc pinned; generator; inputs.

## 6. Gates (G-F11-B1..B6)

| gate | pass condition |
|---|---|
| B1 | input pins verified: probe sha256 == lane README pin == parse report pin == W-F9 T2 receipt pin; corpus file sha256 == receipt corpus pin; corpus/spec blobs resolve at HEAD |
| B2 | structure tiles: 32 chapters, ZERO overlaps on both axes, exactly one pdf gap (251-269) and one book gap (239-257) each == the P1 cx range; 14 cx groups disjoint; envelope tile 1..743 minus the textless page {12}; book axis 1..528 zero holes; EOC 32/32 (37 chapter_questions chunks — c12/c21 double sets, 3 cx) |
| B3 | join rows: independent J5 re-derivation (with the N-2b refinement) == rows exactly (10 EQUAL / 5 CONTAINS / 0 NUMBER_IDENTITY / 17 UNMATCHED; 14 distinct topics); every topic/subsection/point id resolves against the spec of record; subsections_listed 51, distinct 46; the J4 key on c11 resolves (9.3.5 in NS3; LO chunk in c11) |
| B4 | codes-void law: M-1 raw == 17 (TAIL 6 + RUN 11 + SUFFIXED 0); full stack (M-8 with box/boxes + plural fold, M-9, self-reference, row scope) admits ZERO; zero 3-part tokens; LO route void of codes (0 admitted, 0 coded starts); J4 re-run == exactly 1/255 == 9.3.5; P4b 517 classified |
| B5 | surface: build commit touches exactly the 2 NEW book_layer files; zero spec-side/census/graph/book-lane writes |
| B6 | determinism: byte-identical re-run (sha256 of both artifacts) |

## 7. Write surface

Build commit: the 2 NEW book_layer files only. Records commit: this task file +
receipts/W-F11/ + the W-F10 push-confirm ride-alongs (staged cache/w-f10/) +
tasks/W-F10-cie-9700-book-join.md (M, push clause for 17916a3c/9605a43a) +
LEDGER.md (M, Waves 57-58). Zero bundle/census/graph/book-lane writes.

## 8. Honest leftovers

See tasks/W-F11-cie-9702-book-join.md section 4 (9701/0625 joins NOT STARTED —
0625 carries the D-2 ligature-loss class, N-1 folding law applies; YBI11
honest-blocked on sourcing; LLM polish quota-walled; INTEGRATED/LIVE = the v2
lever; the 17 unmatched chapters need either the 3rd-ed upgrade corpus or an
operator-ordered semantic mapping lane — both out of this wave's write face).
