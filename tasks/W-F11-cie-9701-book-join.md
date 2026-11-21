# tasks/W-F11-cie-9701-book-join.md

```yaml
task: W-F11
title: the CIE 9701 book-layer join — design of record (book-structure + book-join
      for the 3rd-ed coursebook x cie-a-level-chemistry-2025-2027; T2 build NOT
      STARTED)
order_trace: 1a1fbb71dc98ef81
order: "Proceed" (operator, 2026-11-21) — executing the standing queue's next
      write face of record: the 9701 T1 design (probe manifest + design of record
      + task file) stages with the Wave-62 records landing; the 9702 lane is the
      structural precedent; YBI11 stays honest-blocked on sourcing (operator
      purchases, never agent-fetches, W-F7-T1 section 7 law).
lane: books rollout queue — join program (design authority: W-F4-T1 schemas +
      join-key regimes J1-J6; emitter laws of record: W-F7-T1 M-1..M-7 + the W-F8
      M-8/M-9 exclusions + the W-F10 N-law CIE adaptations + the W-F11 amendments
      N-2b/N-2c/N-3a/N-3b/N-4/N-7/N-9; the 0625 lane follows under the N-1 folding
      law)
status: W-F11-T1 (9701) COMPLETE 2026-11-21 — probe manifest + design of record
  filed at receipts/W-F11/W-F11-T1-9701-probe-manifest.json +
  receipts/W-F11/W-F11-T1-9701-design-of-record.md (+ the T1 worklog entry); the
  probe ran REMOTE-ONLY during the sandbox outage (traces 1a1f93bb6424e909 +
  1a1fa58df8d73e4d) and was RE-VERIFIED against the tip-of-record blobs
  (1202aaf3) this round by direct blob reads (scripts/wf62_stage_build.py,
  probe gates P1..P8 ALL PASS) — zero repo writes at probe time.
  W-F11-T2 (9701 build) NOT STARTED — the join
  (book-structure--9701-coursebook.json + book-join.json under
  Official-Specifications/parsed/_derived/book_layer/cie-a-level-chemistry-2025-2027/)
  follows as its own ordered wave on the v1 corpus (fidelity polish lane
  separate, quota-walled). This task file + the T1 receipt set land with the
  Wave-62 records landing (trace 1a1fbb71dc98ef81, append-only convention); the
  push executes on any operator-delegated credential per the standing waiver
  (trace 1a1f7e7bd7a43f81).
```

## 1. Scope of record

The third CIE join lane and the second CROSS-LINE design: the 9701 3rd-ed
coursebook corpus (1083 chunks, W-F9 PARSED with the 18/18 reconcile ALL
CHECKS PASSED at trace 1a1f4951330253b5, pristine byte-identical; source
sha256 1fa8afa3…c3e4928, 889 pdf pages, native text layer, no OCR) is a
2017-LINE book (qual_code "CIE 9701 (2017 line, exams from 2022)" per the
parse report of record) joined to the restructured `cie-a-level-chemistry-2025-2027`
spec of record (35 topics / 91 subsections / 356 points, W-F3/W-F6-family
parse of record; syllabus sha1 acc8c02b…, 98 pages; sme_courses
cie-a-level-chemistry-25 + cie-as-chemistry-25). The join is therefore a
CROSS-LINE partial topic-level spine consumed as such: the edition+line
disclosure rides the join header AND every row (the N-8 analog), and the
J5 title-evidence route is the only expected mapper (the 30-chapter book
axis vs the 35-topic spec axis diverge structurally; Tier 3 number identity
is expected to fire rarely and is gated by the title-variant requirement).
The probe decisions D-1..D-6 pin the honest constraints of the source side:
D-1 no printed page numbers (book_pages None on all chunks — the 9702 page
law book = pdf − 12 is NOT portable); D-2 margin features absent from the
render (types tip/cross_link/extension_work not emitted); D-3 WeChat
watermark stripped with the zero-CJK validator gate; D-4 sub/superscripts
rebuilt from span geometry (553 subscript / 533 superscript chunks); D-5
chapter map = 30 LEARNING-INTENTIONS openers + P1 (pdf 522-536) + P2 (pdf
870-882) + appendices/acks, TOC used for titles only; D-6 22 residual
<80-char fragments (2%) accepted for v1 and routed to the polish lane.

## 2. Design of record (receipts/W-F11/W-F11-T1-9701-design-of-record.md)

- Surface (at T2): Official-Specifications/parsed/_derived/book_layer/
  cie-a-level-chemistry-2025-2027/book-structure--9701-coursebook.json (NEW)
  + book-join.json (NEW) — the 9702 artifact shape, zero spec-side/census/
  graph writes.
- Row keys: u0:c0..c30 (c0 = the 62 non-chapter chunks — front matter,
  P1/P2, appendices, acknowledgements; c1..c30 = the 30 chapters; census
  re-verified this round: 31 keys summing 1083).
- Verdicts: JOIN_TOPIC | NO_TOPIC_MAPPING only; NO_TOPIC_MAPPING rows are
  honest, flagged ["no_title_match"], and NEVER repaired (the N-7 law).
- Join-key regime: J5 three-tier title evidence (EQUAL > CONTAINS under the
  N-2b longest-contained refinement > Tier 3 number identity, title-variant
  gated) with basis recorded per row; spec_refs.subsections = the mapped
  topic's subsections of record; the J4 verbatim-TEXT point-key route per
  the W-F11 family law (zero printed codes in this render; J4 fires only on
  exact TEXT equality, expected near-zero, full-stack evidence mandatory).
- P1/P2 enter as gap rows per the W-F10 P1-in-gap precedent (the N-9 analog:
  the chapter-tile gaps must equal the P1/P2 pdf ranges exactly).
- Gates at T2: G-F11-B1..B6 (the 9702 definitions adapted — see the design
  of record); landing verification V0..V10; manifests + dual pins (sha256 +
  git blob); determinism byte-identical re-run.

## 3. Write surface

- Official-Specifications/parsed/_derived/book_layer/
  cie-a-level-chemistry-2025-2027/ book-structure--9701-coursebook.json +
  book-join.json (both NEW, at T2) +
- tasks/W-F11-cie-9701-book-join.md (NEW, this file — T1) +
- receipts/W-F11/ (the T1 receipt set: probe manifest + design of record +
  worklog) + LEDGER.md append (Wave 62) + the ride-alongs of the Wave-62
  records landing + cache/w-f11/ (staging, agent-side). Zero bundle
  mutations, zero census writes, zero graph writes, zero spec-side writes.

## 4. Honest leftovers (routed, not repaired)

- W-F11-T2 (the 9701 join build): NOT STARTED — it executes as its own
  ordered wave on the v1 corpus; nothing in this design builds anything
  until that wave is ordered.
- book_pages None (D-1): no printed-page axis exists — serving anchors on
  pdf pages + chunk ids; no repair possible or attempted.
- Margin features absent (D-2): a source-state fact of this accessibility
  re-layout render; the disclosure carries it.
- 22 residual fragments (D-6): the LLM fidelity polish lane (quota-walled;
  the pristine snapshot is the anchor-diff target).
- The cross-line join is PARTIAL by construction; serving consumes it as
  such (the edition+line disclosure is mandatory on header + rows).
- The 0625 join: NOT STARTED (the D-2 ligature-loss class, 488 occurrences,
  the N-1 folding law applies); its spec basis is PINNABLE at the tip of
  record (Official-Specifications/cie-igcse-physics-2023-2025/, cover_code
  0625, 61 pages, sha1 794defb5… — the prior round's provisional "no
  cie-igcse-physics-* directory" note is corrected by this census).
- YBI11 stays honest-blocked on sourcing (operator purchases, never
  agent-fetches, W-F7-T1 section 7 law). INTEGRATED/LIVE remains the
  v2-repo/DB lever (not this repo's write face, CATALOG section 1 state
  law).
