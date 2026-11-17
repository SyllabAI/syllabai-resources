# W-F6 — CIE graph YAMLs: design of record

Order: operator message "CIE graph YAMLs" (trace `1a1e9d9c217c8e75`) — opens the backlog
lane named in the Wave-43 push-confirm report. Wave of record: **W-F6**. This document is
the T1 design of record; T2 (build + gates + local land) fires under the same order,
W-F5 precedent (T1+T2 same order, push by separate order).

## 1. Inputs of record (pinned)

- Base: pushed GitHub tip `062a4c3463af9a45a9f086dd42d7637ed24b35bc` (Wave-43 rebuild,
  parent `16bbd4e8`). All inputs read via `git cat-file blob <HEAD>:<path>` — zero
  worktree dependency, zero network, zero LLM.
- Per qual (34 × `Official-Specifications/parsed/cie-*/`): `spec_points.json`
  (schema `syllabai.spec-points/1.0`, issue **2**, 14-field contract of record W-F3-T1 §2)
  + `topics.json` (schema `syllabai.topics/1.0`).
- Schema precedents of record (landed graph layer, read at the same HEAD):
  `emit_graph.py` law (scripts__emit_graph.py, W-F2 era) + landed
  `_derived/graph/{ial-chemistry, ial-biology, igcse-biology, igcse-ict}/` byte shapes
  (row shapes, meta block, honest-empty practicals, SF fallback codes, SUB{n} codes).
- Input census of record: `cache/w-f6/census-inputs.json` (script
  `scripts/wf6_census_inputs.py`). Headline: **6,920 spec_points / 467 topics /
  1,646 subsections — exactly the Wave-39 counts of record**; ordering strictly
  increasing + unique 34/34; topic ordering == index and subsection ordering == index
  34/34; topic codes: 408 `-T{n}` canonical (325 index-contiguous, 83 with gaps —
  verbatim, never re-derived; the gaps carry the Wave-39 dedupe history), 59 null,
  and duplicated codes in 6 quals (distinct topics sharing a printed number — see
  §4 law); sub code collisions in 17 quals (tier_columns AS/A2 lists); topic-ref
  null on exactly 5 rows (cie-a-level-maths-2023-2025 :1.1.1–:1.1.5); subsection-ref
  failures 0; `practical=true` rows 0; rows with subsection ref 5,901 / null 1,019;
  `text_render != text` on 73 rows (W-F5 presentation delta — bundle-layer only);
  flags vocab 9 classes (incl. reparse-2.0 ×40).

## 2. File plan (write surface)

136 NEW files — nothing else in the parsed tree is touched:

```
Official-Specifications/parsed/_derived/graph/cie-<qual>/{specification_points,topics,relationships,practicals}.yaml   × 34 quals
```

One revertible build commit (revert = delete the 34 directories). Census 0.6 stays
agent-side (covers spec_points.json only; the graph adds derived files, census
additivity unaffected).

## 3. Transform law (zero-LLM, deterministic; pure function of the pinned blobs)

Meta block (identical in all 4 files of a qual, Edexcel law):
`curriculum_code` = canonical id namespace (spec-point id prefix before `:`,
e.g. `CIE_IGCSE_BIOLOGY_2023_2025`); `qualification` = `"<bundle id> (Issue <issue>)"`;
`phase: 1`; `node_families: [TOPIC, SUBTOPIC, SPEC_POINT]`; `graph_format_version: 1`;
`source_documents: [{file, role: official-pdf-direct-parse, sha1: pdf_sha1}]`;
`edge_vocabulary` = the landed V2 enum string, verbatim; `provenance_default: RULE_DERIVED`;
`generator: scripts/wf6_emit_cie_graph.py (from parsed/cie-*/spec_points.json)`;
`generated: '2026-11-17'` (BUILD_DATE, pinned per build — determinism law);
`counts` = honest per-qual {spec_points, topics, subsections, practicals: 0}.
No `qualification_units` / excluded-points / parse-gap blocks (no structure.json for
CIE — honest absence, igcse precedent).

1. **specification_points.yaml** — one row per canonical row (all 6,920; no exclusions):
   `code` = canonical id; `official_code`, `ordering`, `scope`, `applicability`
   (verbatim dict), `leading_verb`, `damage_flags` = canonical `flags`; `official_wording`
   = canonical **`text`** (frozen verbatim — the audit anchor; `text_render` is the W-F5
   bundle presentation layer and does NOT enter the graph); `section` = resolved topic
   code (T-code verbatim, SF fallback §4; `null` for the 5 honest topic-null rows);
   `subsection` = resolved SUBTOPIC code (`null` for the 1,019 rows without a subsection
   ref); `unit_code`/`unit` = null (no structure.json); `global_order` = `ordering`;
   `practical` = canonical practical; `validation_status: RULE_DERIVED`,
   `confidence: 1.0`, `version: 1`; `provenance` = {tier: RULE_DERIVED, source_file,
   spec_issue: '2', extraction_method: canonical provenance.extraction_method,
   generated_by, generated_date, pdf_page, pdf_oy, pdf_sha1} (canonical page/oy/sha1).
2. **topics.yaml** — `topics` rows {code (§4), title, ordering = canonical ordering,
   unit_code: null, unit: null, validation_status, confidence, version,
   provenance (below), damage_flags: []};
   `subsections` rows {code = `<curriculum_code>-SUB<n>` (n = 1-based array index;
   Edexcel igcse-biology law — unique by construction, source collisions irrelevant),
   letter: null (CIE subs are numbered, not lettered), title,
   parent_topic (§5), provenance {tier, source_code: canonical printed code,
   pdf_page, pdf_oy, pdf_sha1}}.
   Topic provenance mirrors the canonical shape honestly: single-span topics
   (420) carry {tier, source_number, pdf_page, pdf_oy, pdf_sha1}; the 47
   multi-span topics of record (canonical provenance is a span list — Wave-39
   "47 multi-span") carry {tier, source_number, multi_span: true, spans:
   [{pdf_page, pdf_oy, pdf_sha1} × N]}; SF/# deviations add source_code per §4.
3. **relationships.yaml** — PART_OF only, two edge classes (landed-layer law; the
   landed layer carries zero SUB edges after the Stage-R vacates — no new edge types):
   (a) sub → parent_topic (1,646); (b) point → resolved topic (6,915). The 5
   topic-null rows get **no edge** (honest: no fabricated association).
   Expected total: **8,561 edges**.
4. **Topic code law**: canonical `code` verbatim where unique within the qual
   (gaps included — the T-numbering carries the Wave-39 dedupe history and is of
   record). Two honest deviations, both markered in provenance:
   (a) `null` code (59 rows) → fallback `<curriculum_code>-SF<i>` (i = array index;
   `4BI1-SF2` precedent), `provenance.source_code: null`;
   (b) duplicated canonical codes (6 quals of record: a-level-economics T8 ×2,
   english-language ×2 quals T1/T2/T4/T5, igcse-history T1–T6 ×2, the two science
   quals T1–T12 per subject column — distinct topics sharing a printed number)
   → first occurrence verbatim, subsequent occurrences `<code>#<k>` (k = occurrence
   number; unique by construction), `provenance.source_code` = the canonical code.
   SF/# codes never collide with each other or with T-codes (gate-checked).
   Resolution key (number,title) is duplicate-free across all 34 quals (validated).
5. **Parent derivation law** (sub → topic): (a) dotted-prefix — strip leading
   non-digit chars from the sub source code, first dotted segment == topic number
   (covers "1.1", "C1.1"); (b) fallback: last topic whose (page, oy) <= sub's
   (page, oy) (Edexcel law), multi-span topics anchored at their FIRST span;
   (c) last resort: first topic. Breakdown recorded in
   the build receipt; gate requires 1,646/1,646 resolved.
6. **practicals.yaml** — `practicals: []` honest-empty in all 34 quals (no
   practicals.json exists for CIE — Wave-39 honest-empty of record; census:
   `practical=true` rows 0; `igcse-ict` precedent for the empty file shape).

YAML style: `yaml.safe_dump(..., sort_keys=False, allow_unicode=True, width=100)` —
byte-style parity with the landed layer.

## 4. Gates (G-F6-C1..C8, fail-closed battery over swap files + pinned inputs)

- **C1** shape: 34×4 files; meta block identical across a qual's 4 files; required
  row keys present; node_families/graph_format_version/edge_vocabulary exact.
- **C2** node integrity: point/topic/sub codes unique per qual (topic uniqueness by
  the §4 verbatim/SF/# law — deviations markered in provenance.source_code); SF/#
  codes disjoint from bare T-codes; every row.section resolves to a topics.yaml code
  (except exactly 5 null); every row.subsection resolves to a topics.yaml sub code
  (exactly 1,019 null).
- **C3** edge integrity: 8,561 edges total (1,646 + 6,915); endpoints resolve;
  from/to classes correct; relation == PART_OF only.
- **C4** field fidelity: official_wording == canonical `text` byte-exact (6,920);
  ordering/global_order/practical/scope/applicability/leading_verb/official_code/
  damage_flags == canonical (serialized comparison); provenance page/oy/sha1 == canonical.
- **C5** counts honesty: meta counts == actual rows/edges everywhere; per-qual sums ==
  6,920 / 467 / 1,646 (Wave-39 totals of record).
- **C6** parent derivation coverage: 1,646/1,646 resolved; prefix/page breakdown recorded.
- **C7** determinism: emitter re-run → 136/136 files byte-identical (sha256).
- **C8** provenance pins: source_documents sha1 == canonical bundle sha1 for every
  qual; generator/generated stamps uniform.

## 5. Out of scope (honest boundaries)

- `text_render` does not enter the graph (bundle presentation layer, W-F5);
  the 73 render≠text rows stay byte-frozen at `text` here.
- `sub_items` (997 rows / 3,748 items) do not enter the graph — the landed layer has
  no sub-item nodes or SUB edges (Stage-R of record); the row-level `subsection`
  link is carried instead.
- No REQUIRES_PREREQUISITE/RELATED_TO/... edges (the enum is carried in
  edge_vocabulary; no derivation law exists — honest-empty).
- No units (no structure.json for CIE), no excluded points, no parse-gap notes.
