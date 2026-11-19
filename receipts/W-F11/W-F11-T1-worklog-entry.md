# W-F11-T1 worklog entry (staged; lands with the W-F11 records commit)

- Wave: W-F11 (the CIE 9702 book-layer join — the first restructured-syllabus join)
- Trace of record: 1a1f524947d586d9 ("Proceed with next"); executes the next lane in
  the join program queue named by the W-F10 push-confirm receipt (9702 / 9701 / 0625)
- Date: 2026-11-20

## What happened

The operator ordered "Proceed with next" — the queue order of record names the
9702 join first among the remaining CIE quartet lanes, so the wave is the CIE 9702
book-layer join: the 2nd-ed coursebook corpus (2046 chunks, W-F9 PARSED) x the
cie-a-level-physics-2025-2027 spec of record (25 topics / 76 subsections / 303
points). No sourcing correction needed — the lane is a CIE lane with a PARSED
corpus; YBI11 stays honest-blocked on sourcing.

The T1 probes ran zero-LLM over the pinned blobs at 9605a43a (scripts/wf11_probe.py,
cache/w-f11/probe.json). The structural headline: UNLIKE the 9700 case, the
syllabus revision RESTRUCTURED the topic map — the 2016-line book's 32 chapters do
not coincide with the 2025-2027 spec's 25 topics. The J5 three-tier law with the
new longest-contained refinement (N-2b) maps 15/32 chapters (10 EQUAL / 5 CONTAINS)
onto 14 distinct topics; 17 chapters carry honest NO_TOPIC_MAPPING rows (N-2c) —
including whole dropped subject areas ("Communications systems", "Electronics") and
the consolidated electricity/thermal/nuclear splits. Tier 3 (number identity) fires
zero times — the 32 vs 25 number axes diverge, and the title-variant requirement
correctly rejects the false pairings (e.g. book c17 "Circular motion" vs spec T17
"Oscillations").

The code-census probes produced the wave's law amendments: M-1 raw admission 17
chips, zero admitted under the full stack — with two new pinned exclusions, the
M-8' plural fold ("as shown in Figures 9.1, 9.2 and 9.3" — "figures" folds to
"figure") and the self-reference exclusion N-3b (a t.s token whose topic number
equals the host chapter number is the book's own internal chapter.t.s numbering —
all 8 such tokens in this corpus are Figure/Table/Box/credit references); the 9
remaining raw chips are out of row scope (P1/P2 measurement values, the
Acknowledgements photo-credit lists). Zero 3-part tokens corpus-wide; the J2 LO
route void at source. P4b classified 517 corpus-wide 2-part namespace survivors —
a physics corpus structurally collides with the t.s namespace far more than the
biology one (measurement values dominate).

The wave's second finding: J4 is NOT a pure zero here — exactly 1/255 LO bullet
lines equals a spec point verbatim: the c11 line "state Ohm's law" == point 9.3.5
(T9 Electricity, subsection 9.3, AS Level). The family law is amended honestly
(N-4): zero printed CODES (J1/J2/J3 zeros stand), one verbatim TEXT equality,
keyed under the c11 row with the LO chunk pinned — and c11 is one of the 17
unmatched chapters, so the keyed point rides a topic-null row, disclosed as such.

Design of record filed at receipts/W-F11/W-F11-T1-design-of-record.md (laws
N-1..N-9, artifacts per the W-F4-T1 schema authority, gates G-F11-B1..B6). Zero
repo writes this task; probes live in cache/w-f11/; staging in download/w-f11-swap/.
