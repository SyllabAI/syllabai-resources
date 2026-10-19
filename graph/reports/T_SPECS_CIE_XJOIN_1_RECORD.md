# T-SPECS-CIE-XJOIN-1 — cross-lane join round record

- Date: 2026-10-19 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace
  `1a1535a69f8502d1`)
- Operator directive: *"① cross-lane join round"* — fires NEXT lane #1 of the
  T-SPECS-CIE-INDEX-1 record ("cross-lane join round for the 54 curable dangling
  ids — a join/verdict round consuming the per-lane indexes").
- Base commit: `62b0600f` (T-SPECS-CIE-INDEX-1, on origin/main).
- Lane script: `scripts/cie_xlane_join.py` (deterministic engine, fixed stamp
  `2026-10-19T10:00:00Z`, byte-idempotent), battery
  `scripts/cie_xlane_join_check.py`.

## What was built

**One additive top-level block `cross_lane_join` per CIE index** — appended to all
44 `SME-ExamQuestion/<cie-lane>/spec_point_index.json` files. The pre-existing
bytes are untouched: the battery's X2 proves BYTE-ADDITIVITY per file (the staged
file re-serialized minus the block equals the HEAD blob byte-exactly; top-level
key order is append-only: base 8 keys + `cross_lane_join`). Block shape
(`syllabai.sme-cross-lane-join/1.0`): `{schema, generated_utc, directive,
gateway_trace, fires, dangling_total, resolved{}, ambiguous[], unresolved_ids[],
resolved_count, ambiguous_count, unresolved_count}`.

Per resolved id the block records the cure at its honest grade:

- `grade definition` (9 pairs): >=1 sibling lane holds the id WITH a definition —
  the representative record (lexicographically-first definition-holding sibling)
  is carried VERBATIM (`name`/`definition`/`notes`/`subtopic_slugs`).
- `grade name_only` (45 pairs): siblings hold the id but name-only there —
  representative carried verbatim with `definition: ""` (nothing manufactured,
  AGENT.md rule 3).
- `via_lanes` lists ALL sibling lanes holding the id (corroboration, honest);
  `definition_lanes` (definition grade) the definition-holding subset. A
  `norm_equivalent: true` flag marks cures whose sibling records agree only
  under the lineage normalization SPEC (the V5a-pinned vocabulary) — the flag
  did not fire on this corpus (0 cases).
- `ambiguous[]` is the fail-closed quarantine (definition/name conflicts beyond
  the normalization SPEC, variants recorded per lane) — **empty on this corpus**.
- `unresolved_ids[]` = the record-less remainder — no records manufactured.

## Results

- Reconciliation EXACT with the INDEX-1 record: **322 dangling (lane, id) pairs
  = 54 resolved (9 definition + 45 name_only) + 0 ambiguous + 268 unresolved**;
  54 = the H6 "present-in-sibling" count, 268 = the record-less count, both
  re-derived fresh and re-pinned by the battery.
- Cured lanes: cie-igcse-maths-25-core **26/26 (fully cured)**,
  cie-a-level-maths-20-probability-and-statistics-2 16, cie-igcse-chemistry-23 8,
  cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry 2,
  cie-a-level-maths-20-pure-1 1, cie-igcse-maths-25-extended 1.
- Unresolved 268 stays pending honestly per lane: igcse-business-25 198 (EQ
  references the 2027–2029 redeveloped syllabus ids absent from the entire CIE
  corpus), igcse-economics-25 43, igcse-economics-20 20, igcse-history-18 2,
  a-level-chemistry-25 1, and 4 more across other lanes.
- Multi-sibling corroboration: 27 of the 54 pairs are held by >1 sibling lane;
  every `via_lanes` list re-verified equal to the FRESH sibling holders (X4).

## Mechanism (deterministic, zero-LLM)

1. Enumerate the 44 lanes; read the 44 HEAD index blobs as the canonical
   substrate (the corpus is NOT re-streamed — the index is the designed join
   substrate per the INDEX-1 record).
2. Build the global id→holders map; per lane resolve each
   `coverage.missing_from_index` id via the cure policy (verbatim-first,
   normalization-SPEC fallback, quarantine on conflict, recordless stays).
3. Serialize append-only (byte-additive vs HEAD); stage via the INDEX-1 write
   path (`git add --sparse`; lane dirs outside the sparse cone).
4. Fail-closed sidecar reconciliation per lane (universe == `anchors.universe_ids`).

## Checks

Battery `scripts/cie_xlane_join_check.py` **X1–X10: 10/10 PASS**
(`graph/reports/T_SPECS_CIE_XJOIN_1_CHECK.json`):

| id | check |
|----|-------|
| X1 | 44/44 well-formed additive blocks (shape/stamps/counts/key order/no-trailing-NL) |
| X2 | BYTE-ADDITIVITY: staged file == HEAD bytes + exactly the appended block; coverage/spec_points byte-stable |
| X3 | fresh corpus re-derivation 44/44 (universes + EQ refs from blobs): 32,085 refs / 5,540 = 5,218 + 322; partition per lane; split 54 + 268 |
| X4 | all 54 resolved entries verbatim-equal to FRESH sibling records; grades 9/45; via_lanes == fresh holders |
| X5 | ambiguity quarantine honest (0 entries; variants would deep-equal fresh records) |
| X6 | footprint 48 paths ⊆ declared set; spec-links/SME-RevisionNotes/Official-Specifications/SME-Flashcards untouched; SME-ExamQuestion delta == exactly the 44 CIE files; 93 indexes at HEAD = 49 Edexcel (untouched) + 44 CIE |
| X7 | engine fixed-stamp re-run byte-identical across all 44 files (sha256) |
| X8 | 2-lane independent rebuild from fresh corpus data (maths-25-core 26 cures, chemistry-23 8) == staged bytes |
| X9 | sidecar universe reconciliation 44/44 fail-closed; spec-links byte-identical vs HEAD |
| X10 | stats coherent with staged blocks; record pins (322, 54, 9, 45, 0, 268) ALL reproduced |

Battery defect caught and fixed en route (recorded honestly): **X6 initially
asserted `ls-tree HEAD … spec_point_index.json == 49`** — the INDEX-1-era count.
After Task-31's commit the CIE files live at HEAD too, so the true count is
93 = 49 Edexcel + 44 CIE; the verifier was evolved to the new state (the engine
output was correct throughout; the footprint/delta assertions were green).

## Footprint

- Modified: `SME-ExamQuestion/<cie-lane>/spec_point_index.json` (44, additive
  block only), plus the lane's own scripts/reports.
- Byte-untouched: all 49 Edexcel spec_point_index.json files, all spec-links
  sidecars (X9), SME-RevisionNotes/**, SME-Flashcards/**,
  Official-Specifications/** (X6), and within each index file everything except
  the appended block (X2).

## NEXT (operator-gated, NOT fired by this directive)

1. **Re-join against the index to cure the structured pendings** — the 4,386
   verdict pendings (and the coded lanes' text pendings) can fire against the
   canonical per-course indexes, now cross-lane-aware; the 268 record-less ids
   stay pending honestly (rule 3).
2. Learner-UI consumption — render `cross_lane_join.resolved` alongside
   coverage; verdict entries keep operator-verdict authoritative semantics,
   T2_near stays a non-authoritative hint.
3. R41-shaped re-gate — explicit instruction only; PAT rotation still
   CRITICAL-OVERDUE (fingerprint `a8ccee736aa8c75b`, 17 recorded plaintext
   transits).
