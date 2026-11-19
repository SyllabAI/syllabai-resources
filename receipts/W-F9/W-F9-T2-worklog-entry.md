# W-F9-T2 worklog entry (build + gates + local landing)

- Trace of record: 1a1f4951330253b5 · 2026-11-20.

## What happened

T2 executed the quartet build per the T1 design of record:

1. **9701 reconcile first** (cheapest, highest-certainty item): fetched the
   landed corpus + pristine blobs, verified byte-identity, ran the landed
   validator of record — ALL CHECKS PASSED (18/18 checks; 1083 chunks; 531
   chunks with Unicode subscripts). The catalog-lag errata (tracker row 4 +
   lane README status) corrected of record.
2. **Extraction**: per-page span-pool JSON checkpoints for 9702/9700/0625
   (1768 pages total, resume-safe). Two extraction-law iterations of record:
   v2 added per-page gutter voting after the merged-block census proved to
   undercount columns; v3 tuned the vote thresholds (gap ≥ 14pt, sides ≥ 25pt,
   ≥ 4 votes) which fixed the 9700 equal-column body; 0625 required the FIXED
   gutter x=307 (its grid is irregular). Post-law spot checks: 9702 pdf 17/22,
   9700 pdf 41, 0625 pdf 16/27/33/120/312/237 all read correctly.
3. **Structure maps**: authored book_structure_{9702,9700,0625}.py from the
   probe evidence with tiling assertions (46/32/65 ranges tile 1..N/1..N/1..M).
4. **Chunkers**: adapted from parse_9701.py (the landed pattern). Three
   fix-iterations of record: markers-over-display-heads precedence + Title-Case
   marker forms (9702 first pass had EOC typed body); whitespace-normalized
   marker matching (9700's AS chapters print 'End-of-chapter  questions' with a
   double space); 0625 opener phase law (head/box/body), '●● Worked example'
   typed worked_example, '●' bullet-glyph variant, symbol-glyph (\x07) strip,
   box→body transition flush.
5. **Validators**: unique ids/grammar/schema/coverage/order/coherence/dual
   page numbering/serving anchors/junk/sizes — ALL CHECKS PASSED ×3 (2046/
   1971/896 chunks). EOC anchors 32/32 (9702), 21/21 (9700), banks anchored
   + checklists 50/50 + openers 50/50 (0625).
6. **Determinism gate**: every corpus regenerated — sha256 byte-identical.
7. **Landing**: deliverables generated (chunks + pristine + textlayer + parse
   report + parsed README + per-book pipeline scripts), CATALOG tracker rows
   4/5/6/7 → PARSED + change-log row, four lane READMEs updated, task file +
   receipts drafted, W-F8 push-confirm ride-alongs staged, LEDGER Waves 53-54
   drafted. Two plumbing commits (books build, then records) on top of the
   pushed tip 02325c5b — push PENDING OPERATOR ORDER.

## Honest leftovers

0610/0620 quota-walled; never-sourced lanes operator-purchase gated; polish
NOT STARTED for all four corpora; 0625 D-2 ligature class + unheaded in-chapter
revision sets routed to the report, not repaired silently.
