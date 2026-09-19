# T-C24 — parse-error repair campaign record (2026-09-19)

Operator directive: *"Fix all of them. You also have the official pdf to
cross check."* — following the T-C23 Task B inventory (2,042 findings across
20 subjects and all lineages).

Every fix below is deterministic, zero-LLM, and cross-checked against the
official Pearson PDFs (glyph-geometry or whitespace-free text alignment).
Residual limitations are explicitly adjudicated, never silently patched.

## What was repaired (data changes)

### 1. Attachment geometry — 913 statements across 20 subjects
- Root cause: `parse_code_column_bands` finalized every statement with the
  **page-final** header context; `parse_lettered_table` (economics) and
  `parse_triplet_table` (business/ICT) with the **whole-document-final**
  context (94/108 economics statements claimed the document's last subtopic).
- Repair: geometric re-attachment (last header at-or-above, 6 pt tolerance);
  refs never invented; per-subject modes (`impossible-only` / `recompute-all`).
- Proof: repaired attachments reproduce the ratified store's subsections
  **74/74** for chemistry; re-parsing chemistry with the fixed parser is
  byte-equivalent (`EQUIVALENT`, 182/182).
- Files: `parsed/*/spec_points.json` (+ `.parsed.json` lineage unchanged for
  bands subjects; economics/business/ICT repaired in canonical form).

### 2. Modular topic-header recovery — 13 headers + 2 contaminated records
- Root cause: the big-section guard rejected titles ending in a number, so
  every modular `…: Part 1/2` topic header was dropped (physics 4 & 6,
  biology 2 & 3, chemistry 1–8) → 292 topic-code mismatches.
- Recovery: headers re-extracted from the PDFs (16 pt bold, page + oy pinned),
  inserted into `.parsed.json` + `topics.json`; topic refs re-attached
  geometrically (705 → 0 for the modular trio).
- Parser fix: the guard now accepts multi-word titles ending in a digit.
  Re-parse test (physics-modular): topics 4/6 captured natively, 0 ref diffs.
- Contamination removed (PDF-evidenced, unreferenced by SME/flashcard maps):
  - `IGCSE_CHEMISTRY_MODULAR:3.4` — About-page prose ("3.4 million learners…")
  - `IAL_BIOLOGY:Biology-5.0` — maths-skills appendix fragments

### 3. Space-injection repair — 64 fields + the definitive store
- Discovery: the span join (`' '.join`) fabricated spaces inside tight
  multi-span constructs: `( A r )` where the PDF prints `(Ar)`;
  `( propan-1-ol only )` where it prints `(propan-1-ol only)` —
  glyph proof: chemistry 1.16 p18 spans `(` x1=168.9 / `A` x0=168.8 /
  subscript `r` / `)` — zero gaps. This **disproves the C23 "PDF-verbatim"
  call** for those records.
- Repair: 501 occurrences scanned estate-wide; 64 fields respaced where the
  PDF confirms via whitespace-free alignment; 93 formula fields documented
  (`RESIDUAL_DOCUMENTED` — stacked-formula token order is not text-recoverable).
- Definitive store: **7 records refreshed** (1.16, 1.17, 1.26, 1.28, 1.34C,
  3.4, 4.30C) with `c24_respace` provenance; **2 SPEC evidence quotes
  re-anchored** (originals preserved); concepts.yaml quote updates applied.
- Parser fix: `visual_lines` now uses gap-aware joining (space only when the
  x-gap ≥ 25 % of glyph size).

### 4. Economics subtopic titles — 18 repaired
- Titles had swallowed the first statement ("The economic problem a) The
  problem of scarcity…"); re-derived from the title column (x-band 90–220,
  wrapped lines followed): "The economic problem", "Demand, supply and market
  equilibrium", "Macroeconomic objectives", …

### 5. `_derived` emitter — section mapping fixed, all 20 subjects re-emitted
- Root cause of the "+2 shift": topic codes keyed by **table index**
  (front-matter rows occupy indexes 1–2) instead of the printed topic number.
- Fix: statements/rows take `S{printed number}` for referenced content topics;
  unreferenced rows take unique index/SF codes; PART_OF targets follow.
- Chemistry `_derived` now matches the definitive store **182/182 wordings,
  codes equal, 0 diffs**.

### 6. Four targeted text fixes (PDF-verified)
- ial-biology 4.6 — the three `(i)/(ii)/(iii)` items captured into `sub_items`
- igcse-further-maths 9A — "of x", "ax, cos" spacing restored
- igcse-maths-a H-3.1B — "know and use nth term" restored
- igcse-business 5.4.1 — statement + four bullets restored; mis-attached
  page furniture (assessment footer, access-arrangement fragments) removed

## What was adjudicated without data change (with evidence)

- **Oxidation states / units / polymer names** (110 findings) — copper(I),
  copper(II), lead(II), dichromate(VI), manganate(VII), `[Cu(NH3)4(H2O)2]2+`,
  `(poly)tetrafluoroethene`, `( n − 1)d` — all print-true; the bracket regex
  over-fires.
- **Source-document artifacts** — the Pearson prints themselves contain
  `"and and"` (maths-a H-3.3E p40, single text run), `"Assessment
  Objectives.**"` (accounting p12/p13), the 4.49C/8.21C trailing colon —
  faithfully parsed; wording authority = PDF.
- **412 topic-code mismatches** → legitimate schemes: ial-physics bare-integer
  codes inside `N.M` sections; ICT/business `N.M.K` under `N.M`; further-maths
  alpha-suffixed codes; plus one documented interleave record.
- **345 builder flags** → historical provenance (T-SPEC-8/9 repair stamps,
  statement-letter synthesis markers), not defects.
- **93 formula fields** → `RESIDUAL_DOCUMENTED` (stacked formulas: token order
  not recoverable by text alignment).
- **7 ial-maths/geography records** → `STRUCTURAL_INTERLEAVE`: two-column
  (learn/guidance) chimeras; the honest repair is a column-aware walker
  re-parse, recommended as the follow-up task. Deliberately not text-patched.

## Validation

- `c24_postcheck.py` — ALL PASS (only ledger-recorded fields differ vs HEAD)
- `graph_check.py` — ALL PASS (182 spec points, 275 concept edges)
- `c19_substrate_verify.py` — 117 rows, M-fails 0 (quotes re-anchored cleanly)
- v2 rescan — **0 open findings** out of 1,049 (every record adjudicated)
- Re-parse equivalence — chemistry `EQUIVALENT`; physics-modular topics 4/6
  captured, 0 ref diffs

## Files

- Data: 20 × `parsed/<qual>/spec_points.json`, 3 × `.parsed.json` +
  `topics.json` (modular), store `graph/specification_points.yaml`,
  `graph/concept_edges.yaml`, `graph/concepts.yaml`, 20 × `_derived/graph/<qual>/*.yaml`
- Parser: `scripts/spec_parser.py` (snapshot-at-capture ×3 walkers, bigsec
  guard, gap-aware span join)
- Emitter: `scripts/emit_graph.py` (printed-number section semantics)
- Records: `graph/reports/C24_STORE_RESPACE_RECORD.{json,md}`,
  `kg_audit/c24/*` ledgers (repair, modular recovery, respacing, adjudications)
- Scan: `scripts/c24_scan_errors.py` → `download/SPEC_ERROR_INVENTORY_V2.md`

## Recommended follow-ups

1. **Column-aware re-parse of ial-maths** (learn/guidance two-column table)
   and the geography fieldwork/skills tables — clears the 7 documented
   STRUCTURAL_INTERLEAVE records and the 93 formula-token residuals.
2. Formula/notation layer: consider a structured superscript/subscript
   convention (e.g. `kg/m^3`) for the parsed estate, decided per consumer.
3. `t_spec_9_parse_repair`-style stamps could move to a provenance block so
   flags stay purely uncertainty-bearing.
