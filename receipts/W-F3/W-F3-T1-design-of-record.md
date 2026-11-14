# W-F3-T1 — Lane C design of record: CIE canonical bundles

```yaml
wave: W-F3
task: W-F3-T1 (design only — no bundle emitted anywhere)
origin_trace: 1a1da5cb34cb05e1
executed_utc: 2026-11-14
operator: SyllabAI operator (zai-web 1a1da5cb34cb05e1)
tree_of_record: syllabai-resources @ HEAD d2902fcc064f62f8c9ae03ec2b012f49a8ff8922
audit_of_record: cache/w-f3/full-34-audit.json (34/34 quals, all reads git cat-file, blob-pinned)
status: DESIGN_OF_RECORD — W-F3-T2 PENDING OPERATOR ORDER
```

## 1. Order and interpretation

Order: **"new wave"** (trace `1a1da5cb34cb05e1`). No wave named. The interpretation of
record is W-F3 (Lane C, CIE canonicalization) — the unique un-fired wave of the repair
map of record ("repairs belong to W-F2 (reparse), W-F3 (CIE), W-F4 (book layer)",
tasks/W-F1-validation-and-status-check.md; "No CIE canonicalization (W-F3, Lane C)",
tasks/W-F2-ial-reparse-probe.md non-goals). W-F2 and W-F4 are complete with receipts of
record; this task file is the correction point if the operator meant a different wave.
Nothing repo-side has been touched.

## 2. Facts of record (full-34 audit, gates G-F3-D2 evidence)

- 34 CIE parse dirs @ HEAD; each exactly `*.parsed.json` + `parse_report.json`; zero
  canonical bundle files; census 0.4 `canonical_bundle: false` ×34, `derived_graph: false`
  ×34; per-row remedy_lanes prescribe exactly this wave.
- Parse gates G1-G4 PASS 34/34; `duplicate_ids: []` 34/34; parsers `cie-spec-parser-1.0`
  (29) and `cie-spec-parser-1.0+spec-reparse-1.0` (5).
- Families: nmk_outcomes 8, int_statements 13, heading_bullets 5, tier_columns 5,
  ce_codes 2, lettered_items 1.
- Totals: 6,920 spec_points / 598 topic rows / 1,646 subsection rows /
  practicals_true 0.
- Flag kinds by qual count: code-assembled 14, synthesized-ordinal 13, bullet-row 8,
  synthesized-id 5, reparse-1.0 4, possible-superscript-loss 3, control-glyph-stripped 1,
  edge-whitespace-stripped 1.
- Tiers: Core (7 quals), Supplement (5), Extended (2). Scopes: `AS Level`/`A Level`
  (A-level quals), `Biology`/`Chemistry`/`Physics` (the 2 combined-science quals), none
  elsewhere. The 5 heading_bullets quals have 0 subsections.

## 3. Output contract (of record, byte-shaped like the staged W-F2-T2 outputs)

**spec_points.json** per qual — top keys mirroring
`download/w-f2-swap/ial-chemistry/.../spec_points.json`: `schema`, `id`, `qualification`,
`family`, `source`, `counts`, `spec_codes`, `issue`, `spec_points`. Row fields — exactly
the 13-field contract of record:

| field | CIE emission rule |
|---|---|
| `id` | SOURCE row `id` VERBATIM (no re-keying; G2 uniqueness already proven 34/34) |
| `official_code` | SOURCE `official_code` verbatim (synthesized forms `S1.001`/`C1.1.1`/`C1.1a` ride as-printed-by-parser, flags already disclose synthesis) |
| `scope` | SOURCE `scope` verbatim (`AS Level`/`A Level`/per-science/null) |
| `text` | SOURCE `text` verbatim (whitespace-normalised only, already applied by the SOURCE parser) |
| `topic` | SOURCE topic reference `{number,title,page,oy}` + `scope` key where the SOURCE carries it (as-parsed, no reshaping) |
| `subsection` | `{code,title}` where SOURCE subsection exists (code = SOURCE `official_code`); `null` for the 5 heading_bullets quals (staged IAL precedent for null) |
| `sub_items` | SOURCE verbatim (control glyphs as parsed — honesty law, never cleaned here) |
| `practical` | SOURCE verbatim (0 everywhere; honest-empty, no practicals.json emitted) |
| `flags` | SOURCE flags verbatim, never cleared (§7) |
| `applicability` | `{tier: <Core/Supplement/Extended>}` + `rule` string where the SOURCE carries `tier` (the 13-field contract has no tier field — tier rides applicability, never dropped); `{rule: null}` rows recorded as no-applicability-context |
| `ordering` | 1..N in SOURCE array order |
| `leading_verb` | first whitespace token of `text` (case-normalised like the staged rows) for the verb-led families int_statements / tier_columns / ce_codes / lettered_items; `null` for nmk_outcomes (content-heading rows) and heading_bullets (question/heading rows) — family-classified, deterministic, zero-LLM |
| `provenance` | `{pdf, pdf_sha1, page, oy, extraction_method: "pdf-span-geometry"}` — pdf/pdf_sha1 from the SOURCE parse_report, page/oy from the SOURCE row |

**topics.json** per qual — top keys as staged (`schema`, `id`, `counts`, `source`,
`topics`, `subsections`): topic rows `{code, number, title, ordering, provenance}`;
`code = "<SOURCE_ID_PREFIX>-T<number>"` with duplicate `(number,title)` pairs (observed:
ce_codes maths `1/Number` ×3, lettered_items RS `1/Worship` ×2) DEDUPLICATED to one node
whose `provenance` carries every SOURCE span (dedup law — deterministic, audit trail kept
via counts: emitted topics + `source_topic_rows` both reported). Subsection rows in the
`subsections` array with `{code,title,ordering,provenance}`.

**Honest-absent block** (in the bundle's parse_report update + receipt): the SOURCE
parses carry no AO, command-word, equation or practicals arrays — therefore
`assessment_objectives.json` / `command_words.json` / `equations.json` /
`practicals.json` are NOT emitted for any CIE qual (igcse-history 2-file bundle
precedent). Practical-endorsement content lives in separate CIE documents not in the
tree — honest-empty, named as such.

## 4. Per-family emitter rules (grounded in audited shapes)

| family | quals | id/code shape (real samples) | emitter notes |
|---|---|---|---|
| nmk_outcomes | 8 | `CIE_A_LEVEL_ACCOUNTING_2023_2025:1.1.1` | codes printed verbatim; text = content-heading rows; sub_items carry the outcome bullets; leading_verb null |
| int_statements | 13 | `CIE_A_LEVEL_BIOLOGY_2025_2027:1.1.1` | `number` = printed statement ordinal; codes parser-assembled (`code-assembled` flag rides); verb-led leading_verb |
| heading_bullets | 5 | `CIE_IGCSE_HISTORY_2024_2026:S1.001` | synthesized section ids (`synthesized-id` rides); subsection null; leading_verb null |
| tier_columns | 5 | `CIE_IGCSE_BIOLOGY_2023_2025:1.1.1` + `tier: Core/Supplement` | tier → applicability; per-science scopes on combined-science quals; sub_items may carry stripped control glyphs (flags ride) |
| ce_codes | 2 | `CIE_IGCSE_MATHS_2025_2027:C1.1.1` | C/E prefix codes; tier Core/Extended → applicability; subsections `C1.1`-style |
| lettered_items | 1 | `CIE_IGCSE_RELIGIOUS_STUDIES_2025_2027:C1.1a` | letter suffix items; `number` carries the letter; subsection reference `C1.1` |

## 5. Census 0.5 rider (PROPOSED here, applied in T2 exactly as written)

- 34 row amendments: `canonical_bundle: false -> true`; NEW per-row field
  `canonical_bundle_files: ["spec_points.json","topics.json"]`; NEW per-row field
  `canonical_parser: "canonical-builder-2.0-cie-1.0"`; `remedy_lanes`: the
  "C: canonical bundle" entry annotated `(DONE W-F3-T2, trace <t2-trace>)` —
  blanket-flag adjudication and V: book alignment entries stay open.
- One changelog entry, seq 7: task_id W-F3-T2, change text with before/after summary
  (mirrors seq 6 format), origin_trace 1a1da5cb34cb05e1 + T2 firing trace.
- Additivity law: zero other fields touched on any row; `fine_class`, `v1_counts`,
  `lane_b` blocks byte-untouched (deep-compare before/after).

## 6. SCHEMA.md rider (filed in T2 as a staged proposal alongside the bundles)

SCHEMA.md's ID-scheme and family-strategy tables carry no CIE rows. T2 stages a rider
block adding: the 6 CIE families to the family-strategy table; the ID shapes
`<QUAL>:N.M.K` (nmk/int/tier), `<QUAL>:C|E N.M.K` (ce_codes), `<QUAL>:C N.M.<letter>`
(lettered), `<QUAL>:S<sec>.<nnn>` (heading_bullets) to the ID-scheme table; the
`<QUAL>` prefix law `CIE_<QUAL_SLUG>_<WINDOWS>` (as already emitted by
cie-spec-parser-1.0, G4-validated 34/34). The rider documents the parser of record
(`canonical-builder-2.0-cie-1.0`, agent-side emitter honoring build_canonical row
shapes); the repo-side `scripts/build_canonical.py` CIE config block is an OPTIONAL
operator commit (staged as a proposal file, not required for the swap).

## 7. Blanket-flag adjudication classes (record-only, per the census remedy)

| flag | quals | adjudication class |
|---|---|---|
| code-assembled | 14 | parser-assembled N.M.K from topic/subsection/ordinal numbering (CIE prints no statement codes on these rows) — carried, codes are of record only as parser outputs |
| synthesized-ordinal | 13 | ordinal ids synthesized where CIE prints bare lists — carried |
| bullet-row | 8 | sub_items are printed bullets — carried |
| synthesized-id | 5 | heading_bullets quals: S<sec>.<nnn> ids synthesized (no official codes exist) — carried |
| reparse-1.0 | 4 | rows reprocessed by spec-reparse-1.0 (5 quals carry the parser marker) — carried |
| possible-superscript-loss | 3 | text-layer superscript risk (chem/bio/science rows) — carried; per-qual superscript/subscript classes recorded in the bundle manifest, never auto-repaired |
| control-glyph-stripped, edge-whitespace-stripped | 1 | text-layer cleanup disclosed — carried |

Law: flags describe the parse; the canonical layer never drops, upgrades or "fixes"
them (same law as Lane B never reclassifying fine_class).

## 8. Gates

Design gates (this wave): **G-F3-D1 PASS** — every rule above cites a real artifact
(pinned blobs, staged files, audit JSON); no invented shapes (the dedup, tier→applicability
and leading_verb-by-family rules are derivations from the audited shapes, each stated
with its evidence). **G-F3-D2 PASS** — 34/34 quals audited from pinned blobs, evidence at
cache/w-f3/full-34-audit.json; honest-empty rows (AO/command_words/equations/practicals)
name their evidence. **G-F3-D3 PASS** — writes this wave: tasks/W-F3-*.md (NEW) +
receipts/W-F3/ (3 files) + cache/w-f3/ recon caches + worklog append; zero repo writes;
census stays 0.4 (rider PROPOSED).

Build gates for T2: G-F3-C1..C6 as fixed in tasks/W-F3-cie-lane-c-canonicalization.md §5.

## 9. W-F3-T2 execution plan (PENDING OPERATOR ORDER)

1. Emit 68 canonical files (34 × spec_points.json + topics.json) agent-side under
   `download/w-f3-swap/Official-Specifications/parsed/<cie-qual>/`, plus the staged
   SCHEMA.md rider proposal file and (optional) build_canonical.py CIE config proposal.
2. Verify per G-F3-C1..C4 (verify script: id-set equality, counts equality, 13-field
   presence, 0 unresolved refs).
3. Apply the census 0.5 rider per §5 (deep-compare additivity check).
4. SWAP.md with sha256 pins; operator swaps + commits as ONE revertible commit
   (68 new files + rider + optional proposal); `git diff --stat` must show ONLY those
   additions.
5. Backlog after T2: CIE graph YAMLs (derived_graph follow-on), V: book alignment
   (books-lane blocked), practicals lane (separate documents, rollout queue).

## 10. Operator actions

1. Commit the W-F3 task file + receipts alongside the pending W-F2/W-F4 swaps.
2. Optional: order **"W-F3-T2"** to fire the build exactly as designed.
