# W-F11-T1 (9701) design of record — the CIE 9701 book-layer join (staged; rides the Wave-62 records landing, trace 1a1fbb71dc98ef81)

- Task: W-F11 (the 9701 lane); stage: T1 design
- Trace of record: 1a1fbb71dc98ef81 (operator order "Proceed", 2026-11-21)
- Probe traces of record: 1a1f93bb6424e909 + 1a1fa58df8d73e4d (remote-only,
  sandbox outage) — RE-VERIFIED against the tip-of-record blobs (1202aaf3)
  this round (probe gates P1..P8 ALL PASS, receipts/W-F11/
  W-F11-T1-9701-probe-manifest.json)
- Precedents of record: the 9702 join (tasks/W-F11-cie-9702-book-join.md,
  the first restructured-syllabus join) + the 9700 join (W-F10, the
  P1-in-gap precedent)
- Status: DESIGN COMPLETE — the T2 build is NOT STARTED and executes as its
  own ordered wave

## 1. Scope of record

A CROSS-LINE join: the 9701 3rd-ed coursebook (Ryan & Norris; qual_code
"CIE 9701 (2017 line, exams from 2022)"; 889 pdf pages, source sha256
1fa8afa3…c3e4928, native text layer, no OCR; corpus v1 = 1083 chunks,
W-F9 PARSED, reconcile 18/18 ALL CHECKS PASSED at trace 1a1f4951330253b5,
pristine byte-identical) joined to the restructured spec of record
cie-a-level-chemistry-2025-2027 (35 topics / 91 subsections / 356 points;
syllabus 2025-2027, 98 pages, sha1 acc8c02b…; sme_courses
cie-a-level-chemistry-25 + cie-as-chemistry-25). The book's 30-chapter
axis and the spec's 35-topic axis diverge structurally; the join is a
PARTIAL topic-level spine consumed as such, with the edition+line
disclosure riding the header AND every row (the N-8 analog — MANDATORY for
a cross-line join). The probe decisions D-1..D-6 (verbatim in
books/cambridge-international/ial/chemistry/9701/parsed/parse_report_v1.json)
pin the source-side constraints.

## 2. Inputs of record (dual pins, re-verified at tip 1202aaf3 this round)

| input | git blob | sha256 | bytes |
|---|---|---|---|
| parsed/cie_a_level_chemistry_9701_chunks_v1.jsonl | 1cf9a9895b9573366763b5b09e2056e55d12e30e | 774d616c1db882fbfd870482aae67f23651a6ee1cfbc0a728933ff5086ec1de2 | 1867874 |
| parsed/cie_a_level_chemistry_9701_chunks_v1.pristine | 1cf9a9895b9573366763b5b09e2056e55d12e30e | 774d616c1db882fbfd870482aae67f23651a6ee1cfbc0a728933ff5086ec1de2 | 1867874 |
| parsed/full_book_textlayer.md | bf86dbe0073d2d4e80e226933a3628ce7942870b | f1d51e9bda1a813bfae3f68de17683ab083b464e2b92a82a550810af62b1e76f | 1432100 |
| parsed/parse_report_v1.json | fb0f5c42d371f0e5050e92980903fe2e4b149c8d | faed7eb1d9c826ae804e68a6cc902bfe63b3245b761ab6e3c4f51e367f4dbfa0 | 1823 |
| source/student-book.pdf | 08176a0e0cb452ce7cf949eb22e4e59341970ca0 | 1fa8afa3b3a3dc7dd4b981041e7bd9e2019c19095a0f59d75858e5c12c3e4928 | 38227604 |
| Official-Specifications/…/664563-2025-2027-syllabus.pdf | a81b8ac70389b0895056191c31b30a75ad80d8fe | bc40af1d0789b3217524f380337d3a36e49264f5f28ab991e3e85c9102d53ad2 | 4091637 |
| Official-Specifications/…/spec.json | 3d5196da1de42521a585b40073058c0f3bfd8d75 | 3b69a3d4b450a9a6e2bbc6ec87e91d4b1b3cd7f26c1da8b3f78f9c3b4fa126e7 | 777 |
| Official-Specifications/parsed/…/topics.json | 4af7fc82f7c4de54d84411883f72692ee01a61b9 | 3db018cee733c7d58acc6951e3614f0a6ecd648306e49af12e8069ac0fe70f4e | 28947 |
| Official-Specifications/parsed/…/spec_points.json | cfd8beb53b4e53bae070e06bd6b7005e8a99d94a | 012c8c2bb787eada97826f078250975b4572e7a801e73a890c49de37d1304233 | 372302 |

(chunks == pristine byte-identical by sha256 — the W-F9 pristine law holds;
the syllabus sha1 of record is acc8c02b6c6e185aeb31fbf9423637eed507f3bb; the source pdf sha256 equals the
parse report's source_sha256 pin.)

## 3. The join design (what T2 will build)

- book-structure--9701-coursebook.json (schema syllabai.book-structure/1.0):
  30 chapter tiles u0:c1..c30 (the D-5 LEARNING-INTENTIONS opener map,
  corpus-registered pdf ranges, zero overlaps) + the non-lesson sections of
  record (front matter, P1 pdf 522-536, P2 pdf 870-882, appendices,
  acknowledgements — the c0-registered chunks) + honest units [] (single-unit
  corpus u0) + notes carrying the D-laws (D-1: book_pages None — NO book
  axis, the 9702 book=pdf−12 law NOT portable; D-3: the watermark law +
  zero-CJK gate; D-4: the span-geometry sub/superscript law; the
  damage-census fold; P1/P2 routing per the W-F10 P1-in-gap law — the
  chapter-tile gaps must equal the P1/P2 pdf ranges exactly, the N-9
  analog).
- book-join.json (schema syllabai.book-spec-join/1.0): 31 rows
  (chapter_key u0:c0..c30; the c0 row covers the non-chapter matter and
  expects an honest NO_TOPIC_MAPPING or a front-matter disposition recorded
  at T2) — verdicts JOIN_TOPIC | NO_TOPIC_MAPPING only; J5 three-tier title
  evidence (EQUAL > CONTAINS under the N-2b longest-contained refinement >
  Tier 3 number identity, title-variant gated) with basis recorded per row;
  spec_refs.subsections = the mapped topic's subsections of record; the J4
  verbatim-TEXT point-key route per the W-F11 family law (zero printed
  codes in this render; J4 fires only on exact TEXT equality, expected
  near-zero, full-stack evidence mandatory); NO_TOPIC_MAPPING rows carry
  flags ["no_title_match"], spec_refs.topic null, NEVER repaired (N-7);
  coverage block (chapters 31, mapped/unmatched, topics_covered n/35,
  subsections listed/distinct/total 91, points_keyed k/356);
  edition_disclosure (3rd ed, 2017 line, exams from 2022 vs the 2025-2027
  lane) on the header AND every row.
- Emitter law: pure function of the §2 pinned blobs; zero LLM, zero
  network, deterministic; the join is built on the v1 corpus — the LLM
  fidelity polish lane is SEPARATE (quota-walled; the pristine snapshot is
  the anchor-diff target).

## 4. Gates at T2 (G-F11-B1..B6, the 9702 definitions adapted)

- B1 input pins: the §2 dual-pin table must hold at the T2 base commit.
- B2 structure tiling: 30 chapter tiles zero-overlap; the P1/P2 gap law
  exact; non-lesson sections disjoint from the chapter tiles; the c0
  partition fully accounted (62 chunks).
- B3 join rows: independent J5 re-derivation == rows; NO_TOPIC_MAPPING
  honest; the J4 re-run; coverage arithmetic exact.
- B4 codes-void law: the LO/points routes carry zero printed codes (the
  family law) with full-stack evidence; row-scope exceptions enumerated
  honestly.
- B5 surface: exactly 2 NEW files under the book_layer course directory;
  zero spec-side/census/graph writes.
- B6 determinism: byte-identical re-run (sha256).

## 5. Honest leftovers (routed, not repaired)

- W-F11-T2 NOT STARTED (this design builds nothing until its own wave is
  ordered).
- book_pages None (D-1): no printed-page axis exists — serving anchors on
  pdf pages + chunk ids; no repair possible or attempted.
- Margin features absent (D-2): a source-state fact of this accessibility
  re-layout render; the disclosure carries it.
- 22 residual fragments (D-6): the LLM polish lane (quota-walled).
- The cross-line join is PARTIAL by construction; serving consumes it as
  such.
- The 0625 lane follows under the N-1 folding law (its spec basis pinnable
  at the tip of record: Official-Specifications/cie-igcse-physics-2023-2025/,
  cover_code 0625, 61 pages, sha1 794defb5…).
