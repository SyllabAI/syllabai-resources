# W-F9-T1 worklog entry (design + probes)

- Trace of record: 1a1f4951330253b5 · 2026-11-20 · zero repo writes this round.

## What happened

The operator ordered "Proceed with books rollout queue" (trace
1a1f4951330253b5). T1 triaged the queue of record (books/CATALOG.md §4) and
probed the four SOURCE-state text-layer books before any write:

1. Queue triage: the only lanes whose next state (PARSED) is reachable without
   external dependencies are the CIE text-layer quartet. 9701 turned out to
   already carry a complete parse (1083 chunks, pristine, validator of record)
   with the CATALOG row + lane README never synced — a catalog-lag errata of
   record, reconciled this wave. 0610/0620 are image-only (OCR route,
   quota-walled — honest-blocked). All never-sourced lanes are operator
   purchases (never agent-fetches, W-F7-T1 §7 law).
2. Structure probes: text-layer coverage (99.6/99.7/98.8%), TOC parsing with
   column-awareness, full display-heading scans (the section maps), marker and
   damage censuses, raw-span gutter probes.
3. The column laws were pinned from raw span geometry after the merged-block
   census proved unreliable: 9702/9700 true two-column bodies (the 9702
   QUESTION sidebars swap sides page-by-page — pdf 22 shows the box left, main
   text right; pdf 17 the reverse), 0625 irregular two-band grid → fixed
   gutter x=307.
4. The offset laws were verified 4/4/5 ways before any chunk numbering
   (TOC digits vs openers vs running-header digits vs bank anchors).
5. The 0625 opener anatomy (head → at-a-glance box → body) and its bullet
   glyph variants ('l' symbol font vs single '●') were probed across all 50
   openers before the chunker was written.

Design of record filed at receipts/W-F9/W-F9-T1-design-of-record.md. W-F9-T2
(build + gates + landing) follows in the same order.
