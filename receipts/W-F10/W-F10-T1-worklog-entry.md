# W-F10-T1 worklog entry (staged; lands with the W-F10 records commit)

- Wave: W-F10 (the CIE 9700 book-layer join — first CIE join lane)
- Trace of record: 1a1f4cf26af71de1 ("proceed"); follows the W-F9 push-confirm
  report's named next lane
- Date: 2026-11-20

## What happened

The operator ordered "proceed" on the lane named in the W-F9 push-confirm report
("ial-biology joins now UNBLOCKED (9700 PARSED landed)"). The survey first pinned
the lane law: the Edexcel ial-biology-18 (YBI11) join — the literal backlog item —
stays honest-blocked on sourcing (CATALOG section 4.2 state em-dash; operator
purchases, never agent-fetches, W-F7-T1 section 7 law). The archive-path segment
`ial/biology` in the books tree is the CIE 9700 lane, and THAT is what the W-F9
parse actually unblocked. The correction of record is pinned in the task file and
the design of record; the wave proceeds on the executable reading — the CIE 9700
book-layer join (Lane C follow-on, first CIE join lane).

The T1 probes ran zero-LLM over the pinned blobs at d9fdee97 (scripts/wf10_probe.py
+ wf10_probe2_subns.py + wf10_probe3_admission.py, cache/w-f10/): the 19-chapter
4th-ed spine maps 19/19 onto the 2025-2027 spec's 19 topics under the M-6 three-tier
law (15 EQUAL / 2 CONTAINS / 2 NUMBER_IDENTITY / 0 UNMATCHED); the printed-code
analysis was AMENDED POST-GATE — the first census's subsection-namespace check used
a wrong key and silently passed; probe2 (198 post-exclusion candidates classified:
internal box/figure/table/question/credit numbering + prose constants) and probe3
(the M-1 admission law: 22 raw chips, zero admitted under the full stack — the 6
M-2-consistent TAIL survivors are internal Table/Box/Figure refs excluded by the
M-8 window; the 16 RUN survivors are M-2-inconsistent or out of row scope) supersede
it; the J2 LO route is void at the source (zero namespace tokens in all 21 LO
chunks); J4 LO equality 0/119 (the book paraphrases); the source sha256 pin matches
the lane README and the W-F9 build receipt. The edition law is pinned (book 4th ed
2014 vs spec 2025-2027; the 5th ed ISBN 9781108859028 remains the upgrade candidate
of record) — the join is a TOPIC-LEVEL spine with the disclosure carried on the
header and every row.

Design of record filed at receipts/W-F10/W-F10-T1-design-of-record.md (laws
N-1..N-8, artifacts per the W-F4-T1 schema authority, gates G-F10-B1..B6). Zero
repo writes this task; probes live in cache/w-f10/; staging in download/w-f10-swap/.
