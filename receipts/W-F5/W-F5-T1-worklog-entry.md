# W-F5-T1 worklog entry (append-ready block)

```yaml
task: W-F5-T1 (design of record — presentation layer for the CIE canonical bundles)
wave: W-F5
origin_trace: 1a1e5bfa1854103d
trace_id: 1a1e5bfa1854103d
executed_utc: 2026-11-15
operator: SyllabAI operator (zai-web 1a1e5bfa1854103d)
order: "W-F5"
verdict: DESIGN COMPLETE — audit of record over the 34 landed bundles (6,920 rows,
  pinned at the manifest oids) found the corpus typographically healthy except six
  deterministic damage classes (subscript-loss 41 rows, hyphen-split 24, math-garble
  22, footer-continued 28, exponent-loss 11, orphan-digit 2); design fixes a three-lane
  architecture — R1 text_render (KaTeX spans, pure transform table, 100% reversal gate),
  R2 geometry-driven source re-recovery from the pinned PDFs (reparse-2.0, per-row
  receipts, no domain-knowledge invention), R3 render-side polish — with T2 gates
  G-F5-C1..C6. Zero repo writes; bundles stay at issue 1; T2 PENDING OPERATOR ORDER.
```

## What was done

- Ran the W-F5-T1 audit of record over all 34 landed `spec_points.json` blobs at the
  pinned oids (commit d926be48 chain): 15-pattern notation inventory + 6 refined damage
  classes, per-qual counts and examples (cache/w-f5/audit-of-record.json).
- Adjudicated the transform inventory from REAL row examples: cosmetic regex is the
  wrong tool for chem-bare/ion-charge classes (F1/W2/A4 false positives) — rejected;
  the real defects are extraction losses (dropped sub/superscripts, interleaved
  two-column spans, leaked footers, line-wrap hyphen splits).
- Key finding of record: flags undercount the loss class (5 rows flagged vs 54 rows
  evidenced); flags stay untouched, repairs derive from pattern evidence and are
  receipted per-row.
- Designed the three-lane architecture and the issue-2 field law (`text_render` added,
  `text` frozen, topics untouched, flags additive-only), the accepted transform tables
  T1-T6 with inverses, and the T2 gate battery G-F5-C1..C6.
- Feasibility: per-row provenance pins (page/oy/pdf_sha1) address every damaged row in
  its pinned PDF; the CIE PDFs are not in the durable cache, so T2 opens with a
  sha1-verified fetch step (fetch-manifest pattern).
- Filed: receipts/W-F5/W-F5-T1-design-of-record.md + W-F5-T1-design-receipt.json +
  this block; task file tasks/W-F5-presentation-layer.md.

## Gates adjudicated

G-F5-D1 PASS / G-F5-D2 PASS / G-F5-D3 PASS (see the JSON receipt for evidence).

## Operator actions

1. Fire W-F5-T2 (build + land) by separate order.
2. Rotate the delegated PAT — still outstanding (4 chat-channel exposures).
