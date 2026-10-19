# External Audit Verdict — Chemistry 4CH1 Parse

**Received:** 2026-10-18, relayed by the operator (audited by a second,
independent agent lane). Recorded here verbatim-in-substance as the gate of
record for the 4CH1 parse.

## Verdict

> **Yes — up to standard. Green light for the remaining books.**

Verified first-hand by the auditor against three layers:

1. the **live registry** (structural QA),
2. the **parse receipts of record** (intake receipts + validation standard,
   contracts band 133a/133b),
3. **spec-join spot-checks against the spine**.

## Evidence table (as delivered by the auditor)

| Check | Result |
|---|---|
| Structure | 29 chapters, unit layout matches the real book (U1:10 / U2:8 / U3:3 / U4:8), **zero overlaps, zero malformed ranges** |
| Coordinates | 100% dual-numbered — `book_pages` (citation) + `pdf_pages` (viewer) on all 29 |
| Spec joins | 145 refs / 143 distinct codes — **143/143 resolve against the api concept-graph spine** (0 unresolved) |
| Join quality | 85 verbatim (59%) + 51 normalized (35%) + 9 fuzzy (6%), each flagged with `method`/`lineage` provenance |
| Parse stack | IBM Docling v3 (layout model + TableFormer + RapidOCR + formula VLM) on the sha-pinned 383pp scanned source; 1,234 chunks, 17 content types |
| Independent verify | Second lane's Neon census: chunks 823 exact, chapters 29 exact, spec refs 145 exact |
| Human gate | Operator's own validation flip (T-C20 law) |

## The 8 page-range "gaps" — by design, not misses

> They're the unit end-matter/dividers (10/8/7pp at unit boundaries, 1pp
> dividers mid-book), which the parse types separately (`divider`,
> `unit_questions`, `chapter_questions`…). Those pages are parsed, just not
> bound to chapter bodies.

## Cosmetic note (non-blocking)

> Learning objectives carry raw newlines — the UI clamps them; worth a trim in
> the next parse but non-blocking.

Actioned as a standard item for future parses — see
`../../PARSE_STANDARD.md` ("Known action item"). Chemistry v3 is NOT
retro-edited (chunk IDs already consumed by intake receipts and spec joins).

## The 8-point standard handed to the parse agent

Reproduced from the audit and now canonical at
`books/pearson-edexcel/international-gcse/PARSE_STANDARD.md`:

1. both page numberings per chunk;
2. contiguous body ranges / zero overlaps;
3. non-body sections typed separately;
4. ≥90% verbatim-or-normalized joins with fuzzy flagged;
5. every code must resolve against the spine;
6. the 15-key v3 grammar;
7. originals preserved on any LLM polish;
8. per-book source sha256.

## Parse provenance (of record)

- Source: 383-page image-only scan, sha256 pinned in `parsed/parse_report_v3.json`.
- Zip package of record: release asset on tag `books-intake-2026-10-18`,
  manifest `edexcel_igcse_chemistry_rag_package.manifest.json` (repo root).
- Full method/decisions: `METHOD_AND_FINDINGS.md` in this folder.
