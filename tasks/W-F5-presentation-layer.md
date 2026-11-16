# W-F5 — Presentation layer: LaTeX render + source re-recovery for the CIE canonical bundles

```yaml
wave: W-F5
tasks:
  - W-F5-T1   # Design of record (EXECUTED 2026-11-15, trace 1a1e5bfa1854103d) —
              # notation audit of the 34 landed bundles (6,920 rows at the pinned
              # oids), six damage classes quantified, three-lane architecture
              # (R1 render / R2 re-recovery / R3 polish), transform tables with
              # inverses, gates G-F5-D1..D3 PASS, T2 gate law G-F5-C1..C6 fixed
  - W-F5-T2   # Build + land (PENDING OPERATOR ORDER) — sha1-verified PDF fetch step,
              # R2 per-row re-recovery receipts, issue-2 re-issue of the 34
              # spec_points.json (text_render added; topics untouched), swap staging
              # under download/w-f5-swap/ with sha256 pins, single revertible commit
origin_trace: 1a1e5bfa1854103d
order_note: >-
  fired by the bare operator order "W-F5" (trace 1a1e5bfa1854103d), implementing the
  operator's directive traces 1a1e5b85438a9a11 + 1a1e5be7c17de8f1 ("the parsed outputs
  can be better than the original — LaTeX, better formatting; we don't have to be
  verbatim"). T1 fired by the wave order; T2 fires by separate operator order
  (W-F3 precedent).
inputs_of_record:
  - the 68 landed CIE canonical bundles at commit d926be489c016d55b6d5bd3c9210b4d19b5acaf4
    (blob oids via cache/w-exec/manifest-wf3t2-land.json)
  - cache/w-f5/audit-of-record.json (T1 audit of record: P01..P15 + damage_classes_refined)
  - the 13-field contract of record + flag classes of record (W-F3-T1 §2/§5)
  - reparse precedent spec-reparse-1.0 (W-F2); fetch-manifest pattern (W-F1/W-F4)
status: W-F5-T1 COMPLETE 2026-11-15 (trace 1a1e5bfa1854103d) — design of record filed at
  receipts/W-F5/W-F5-T1-design-of-record.md + JSON receipt + worklog entry; audit
  of record cached at cache/w-f5/audit-of-record.json; gates G-F5-D1..D3 PASS.
  W-F5-T2 EXECUTED 2026-11-16 (trace 1a1e5c7c2499bf51) — 15/19 PDFs sha1-verified; 40 rows recovered from the pinned sources (reparse-2.0, per-row receipts; 29 honest unrecovered); 34 spec_points.json re-issued at issue 2 (text_render on all 6,920 rows; topics.json untouched); gates G-F5-C1..C6 PASS; census 0.6 rider (seq 8, additivity CLEAN); the 34 modified files landed as commit 676306b038031e5f299af75f89e6269577f47e5d; the records landing (this task file, T1/T2 receipts, LEDGER Waves 41-42) follows as the next commit of the same order; PUSH PENDING OPERATOR ORDER. Zero repo writes this round.
write_surface: tasks/W-F5-presentation-layer.md (NEW, this file) + receipts/W-F5/
  (design doc + JSON receipt + worklog entry) + worklog append + cache/w-f5/
  (audit caches). Zero repo writes, zero census writes, zero bundle mutations.
```

## 1. What the audit found (facts of record — cache/w-f5/audit-of-record.json)

- 6,920 rows / 34 quals scanned at the pinned blob oids. Corpus typographically healthy
  overall (327 rows already carry correct unicode math; no repair needed).
- Six deterministic damage classes (candidate sets, examples of record):
  subscript-loss 41 rows / 12 quals (`SO , PC l , SF`); hyphen-split 24 / 12
  (`file- based`); math-garble 22 / 5 (`r ^ cos i + i sin i h`); footer-continued
  28 / 7 (trailing ` continued`); exponent-loss 11 / 6 (`6.02 × 10 particles` — the
  ²³ is gone); orphan-digit-prefix 2 / 2.
- Flags of record undercount the loss class (5 flagged rows vs 54 evidenced);
  flags stay untouched — repairs derive from evidence and are receipted per-row.
- Every damaged row is addressable via provenance (page/oy/pdf_sha1); the CIE PDFs
  are not in the durable cache → T2 opens with a sha1-verified fetch step.

## 2. Architecture (design of record §3-§5)

- **R1 render layer** — every row gains `text_render` (KaTeX `$…$` spans + safe
  normalizations) derived by a pure ordered transform table (T1-T6, each with an
  inverse); `text` never modified; rows without applicable transforms get
  `text_render == text`.
- **R2 source re-recovery** — geometry-driven re-extraction of the pinned PDF page
  regions for the sub/super/orphan/math-garble candidates; recovered text re-issues the
  row at issue 2 with `reparse-2.0` appended + per-row receipt; unrecoverable rows stay
  verbatim (no domain-knowledge constant restoration — 10²³ comes from the PDF or not
  at all).
- **R3 polish** — footer strip, degree/prime spacing, geometry-proven hyphen rejoin;
  render-side only, reversible, receipted.

## 3. Gates

| gate | task | pass condition |
|---|---|---|
| G-F5-D1 | T1 | every transform/lane rule cites a real artifact of record (path + pinned oid or audit pointer) | 
| G-F5-D2 | T1 | audit covers 34/34 quals at the pinned oids; every class names its detector regex |
| G-F5-D3 | T1 | zero writes outside tasks/W-F5-*.md + receipts/W-F5/ + worklog + cache/w-f5/; zero repo writes; bundles stay issue 1; census stays 0.5 |
| G-F5-C1 | T2 | de-render(text_render) == text byte-for-byte on 100% of rows, except allow-listed receipted rows |
| G-F5-C2 | T2 | pure-code emitter, zero LLM, byte-reproducible re-run |
| G-F5-C3 | T2 | issue-1 flags preserved (additive only: reparse-2.0) |
| G-F5-C4 | T2 | issue-2 honesty: topics.json byte-identical, counts recomputed, 14-field order intact |
| G-F5-C5 | T2 | swap discipline: ONLY 34 modified spec_points.json; one revertible commit; SWAP.md sha256 pins |
| G-F5-C6 | T2 | R2 per-row recovery receipts (before/after + page/oy + pdf_sha1 match) |

## 4. Receipts of record

`receipts/W-F5/W-F5-T1-design-receipt.json` (schema `syllabai.task-receipt/1`,
`origin_trace: 1a1e5bfa1854103d`), the design of record at
`receipts/W-F5/W-F5-T1-design-of-record.md`, and the append-ready worklog block at
`receipts/W-F5/W-F5-T1-worklog-entry.md`.

## 5. Non-goals

No LLM; no in-place mutation of landed files; no topics.json changes; no flag drops;
no whole-text LaTeXification; no semantic rewriting; no graph YAMLs / notes-join /
book-lane / Pearson-side work.
