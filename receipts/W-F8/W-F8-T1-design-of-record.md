# W-F8-T1 — Book-alignment lane design of record
# the igcse trio V-lane completion: figure-void correction + J5 deepening

```yaml
schema: syllabai.book-alignment-design/1.0
task: W-F8-T1 (the igcse trio V-lane completion design of record)
wave: W-F8
origin_trace: 1a1f3f29f14afce5
trace_id: 1a1f3f29f14afce5
executed_utc: 2026-11-19
operator: SyllabAI operator (zai-web 1a1f3f29f14afce5)
order: "Proceed with the three W-F4-T2"
tree_of_record: syllabai-resources @ HEAD cf1c8378b7ffdb581360c1e6b79bac157443c08c
design_authority: W-F4-T1 book-join design (schemas/ladder/verdict classes) + W-F7-T1
  design of record (laws M-1..M-7) — adopted UNCHANGED; this document adds only the
  IGCSE-family laws M-8..M-11 the probes force, and one correction the probes prove
status: DESIGN_OF_RECORD — artifacts emitted by W-F8-T2 in the same order (the W-F6/W-F7
  T1+T2 precedent); push by separate operator order
```

## 1. Scope: what "the three W-F4-T2" means at the cf1c8378 tree

The operator order fires the three W-F4-T2 quals named in the Wave-50 push report's
backlog: **igcse-chemistry (4CH1), igcse-biology (4BI1), igcse-physics (4PH1)**.

**Errata of record (baseline correction, made first).** The Wave-50 push report phrased
these as "staged joins (BUILT_NOT_JOINED from W-F4-T2) ready as a future V-lane wave".
That phrasing is wrong and is corrected here: the trio's W-F4-T2 `book-join.json` files
were **landed and pushed** (Wave 37/38, 13 artifacts; the W-F7-T1 design §1 says so
verbatim: "ial-physics/4BI1/4PH1/4CH1 joins are landed and pushed"). What is actually
open on them — recorded in their own `join_keys` blocks — is the unapplied part of the
program: J3 "not applied" on all three, J1 "not harvested" for 4CH1, and the honest
uncovered sets (4CH1: 10/28 subsections, 175/182 points unkeyed; 4PH1: 8/30 subsections,
188/195 unkeyed; 4BI1: 4/176 unkeyed). W-F8 therefore runs the **W-F7 law set against the
trio corpora and applies whatever the probes prove** — which turns out to be one
correction (§2 F1/F2), one deepening (§2 F4), and three honest stays (§2 F3/F5/F6).

Everything else stays honest-blocked, unchanged: the 10 NO_BOOK quals (books rollout
queue), ial-biology (YBI11 row `—`), CIE SOURCE_ONLY books (Lane C follow-on).

## 2. Probes of record (cache/w-f8/probe.json + probe2.json; zero repo writes, zero LLM)

Ran the W-F7 law set (M-1 harvest generalized to the C/P/B suffix-code family, strict
and punct-stripped variants) against the trio corpora at the pinned blobs, plus a
per-entry context classification of every LANDED point entry, plus corpus-wide searches.
Inputs pinned: spec_points/topics/landed-join/structure/corpus/manifest per qual (blob
shas in probe.json `pins`); corpora of record = 4CH1 v3 chunks (parse_report_v3 of
record), 4BI1 v1 chunks, 4PH1 v1 chunks (1,234 + 863 + 736 = 2,833 chunks).

| # | finding | evidence | adjudication |
|---|---|---|---|
| F1 | **The IGCSE student books print NO spec-reference codes.** 0 coded LO-line starts across all three corpora (`<code> <verb>` line starts inside LEARNING OBJECTIVES blocks: 0); the 4CH1 v3 corpus's 81 `learning_objectives` chunks carry 0 code tokens in any M-1 chip position; strict harvest 0 tokens corpus-wide | probe2 `lo_coded_line_starts` = [] for all three quals; probe.json `harvest.strict` = 0 chapters/0 tokens everywhere | the IAL margin-chip phenomenon (W-F7 M-1) does NOT exist in the IGCSE family; the point-level chip route is **figure-void** |
| F2 | **The landed 4CH1 and 4PH1 point keys are figure-caption false positives.** 4CH1: 62 landed entries, 73/80 corpus occurrences figure-adjacent (`Figure 1.2`, `Figure 2.1`, …), the 7 non-adjacent are numeric constants (`0.0`, `0.53`, `21.0`, `0.9`, `0.04` — air-composition prose); 4PH1: 7 entries, all 7 figure-adjacent (one behind a mid-word window artifact `InFigure`) | probe2 `entries` per-entry contexts; probe1 m2 sample | **FALSE KEYS per L-2** ("a false chip is invention"): the landed `points_keyed` 7/7 — 4CH1 `1.2, 2.1, 2.2, 2.3, 3.1, 3.3, 4.1` and 4PH1 `1.2 (→1.2P unique_candidate), 2.1, 2.2, 3.1, 5.6, 6.1, 6.2` — all 62 + 7 entries must be **removed by correction**, never silently kept |
| F3 | **4BI1's J1 stands.** The 172/176 keys ride `spec_refs.printed_code_list` from the COURSE STRUCTURE ToC spread — the W-F1-T1-igcse-biology transcription of record, page-cited (book pp. iv-vi). The probe's 3 non-figure occurrences are substring artifacts of the occurrence scan itself (`4.1` ⊂ `14.1 A pond…`). The 4 uncovered codes (`2.10, 2.38, 2.40B, 2.43B`): corpus-wide exact-token search = **0 hits** | probe2 igcse-biology `other_context_examples`; probe1 `uncovered_code_search` all 0 | 4BI1 rows **byte-preserved**; the 4 uncovered stay honest `no_printed_key`, now with the 0-hit search as evidence of record |
| F4 | **J5 deepening: 8 of the 10 uncovered 4CH1 subsections map deterministically** under landed-equality + the W-F4-T1 CONTAINS direction (spec title verbatim substring of the chapter title), each consistent with its book unit: SUB5 → u1:c5 **and** u1:c6 (multi-chapter, the spec title is a prefix of both chapter titles), SUB8 → u1:c9, SUB9 → u1:c10, SUB14 → u2:c15, SUB21 → u4:c22, SUB25 → u4:c26, SUB26 → u4:c27, SUB27 → u4:c28. SUB10 (`Group 1 (alkali metals) – lithium, sodium and…`) and SUB11 (`Group 7 (halogens)…`) match only in the REVERSE direction (book title `The alkali metals`/`The halogens` ⊂ spec title) — **not admitted** (the W-F4-T1 law admits spec-in-book, not book-in-spec; routed as findings). 4PH1's 8 uncovered SUBs are all literally titled `Units` — 0 title hits, honest stay | probe.json `j5_deepening_uncovered` + the chapter-title dump | subsections covered 4CH1 **18 → 26/28**; 4PH1 stays 22/30; 4BI1 stays 22/22 |
| F5 | **J1 anchored lists: 0 anchors** in any trio corpus front matter/table data (the `SPECIFICATION REFERENCE` + code-run pattern does not occur); 4CH1's ToC transcription stays not-of-record in any W receipt | probe.json `j1_anchored` = [] ×3 | route verdicts pinned as probed-empty; nothing harvested |
| F6 | The trio are **single-book quals**: the `book-layer-index.json` artifact is the multi-book registration law (W-F4-T1 §7 design_ref; only ial-physics/ial-chemistry carry one) | landed tree: index files exist only for the ial-* quals | **no index files emitted**; corpus pins ride the corrected joins' `inputs` (the W-F4-T2 staged shape was correct for single-book quals) |

## 3. The IGCSE-family build-time laws (delta over W-F7 M-1..M-7 — nothing else changes)

- **M-8 figure-token exclusion (load-bearing for this family).** A code-form token is
  EXCLUDED when the 60-character window immediately before it ends with a
  figure/table/section reference word (`fig`, `figure`, `figs`, `table`, `eq`,
  `equation`, `chapter`, `section`, `unit`, `step`, `question`, `q` — case-insensitive,
  optional trailing punctuation/abbreviation dot), under two deterministic branches:
  (a) **space-preserved** — a word boundary before the reference word; (b) **OCR
  space-loss glue** — up to 3 letters glued immediately before the reference word (the
  corpus prints `…clearly.InFigure 2.1…` — probe2 F2); branch (b) can over-match rare
  prose (`configure`-class), and over-exclusion is the honest direction per L-2. An
  entry whose printed form does not occur at all in its cited evidence chunks is classed
  `not_in_cited_evidence` (its removal rests on F1 alone). Rationale: in the IGCSE
  family the ONLY code-form tokens in body/LO text are figure/table/section numbers and
  prose constants (F1/F2); M-1's RUN/SUFFIXED/TAIL positions cannot exclude them because a
  caption's number is a single token (single = not RUN, not TAIL) — but the W-F4-T2
  build did not run M-1 at all, which is exactly how the false keys landed. M-2's
  unit-consistency cannot exclude them either (a figure numbered `4.2` sits in a topic-4
  chapter by construction).
- **M-9 zero-integer constant exclusion.** A code-form token whose integer part is 0
  (`0.0`, `0.53`, `0.9`, `0.04`) is excluded: spec codes start at `1.1`; no topic 0
  exists in any of the trio namespaces.
- **M-10 trio J5 deepening.** Extend the landed J5 (normalised equality) with the
  W-F4-T1 CONTAINS direction: the spec subsection title is a verbatim substring of the
  chapter title, normalised. Admissions are gated by book-unit/topic consistency (the
  SUB's spec topic must equal the topic family of the chapter's book-unit siblings'
  mapped SUBs — SUB21 `Introduction` (topic 4) → u4:c22 admitted because every unit-4
  mapping is topic 4; a generic one-word title with inconsistent topic would stay
  unmapped). Multi-chapter mappings are allowed and recorded honestly (SUB5 → u1:c5 +
  u1:c6, the 4BI1 shared-code precedent at mapping grain). Reverse-direction containment
  (book title ⊂ spec title) is NOT admitted (SUB10/SUB11 stay uncovered, recorded as
  findings for a future lane that adopts the W-F1-T1 `superset_title`/`partial_title`
  classes with page-cited evidence — this wave stays conservative).
- **M-11 correction law.** Landed-and-pushed point entries that the probe proves
  figure-derived or constant-derived are **removed** by the corrected join; each removal
  is enumerated in the join's `errata` block with its probe2 evidence (chapter, printed
  form, resolution, chunk contexts). The landed state stays in git history (the W-F7 §4
  precedent: correct in place, preserve history). Everything not proven false is
  **byte-preserved**: 4BI1's rows verbatim; the trio's chapter rows, titles, page ranges,
  evidence citations, subsection mappings and flags verbatim.

## 4. Artifacts of the build (W-F8-T2) — surface EXACTLY 3 modified files

| file | change | content |
|---|---|---|
| `_derived/book_layer/igcse-chemistry/book-join.json` | M | all 62 landed point entries removed (M-11, enumerated in `errata`); `join_keys` J2/J3 re-stated **figure-void** (F1) with the M-8 law of record; J5 deepening applied per M-10 (`subsections` covered 18 → 26, SUB5 multi-chapter); rows' `join_key` re-stated `J5_TITLE_ADJUDICATED` and verdicts re-stated `JOIN_SUBSECTION` (the landed trio vocabulary — the coverage grain is the subsection layer; no point keys remain); `coverage` recomputed (`points_keyed` 0, `no_printed_key` 182, SUB10/SUB11 honest stays named); `inputs` gain the corpus/structure blob pins + probe receipts of record; everything else byte-preserved |
| `_derived/book_layer/igcse-physics/book-join.json` | M | the 7 landed point entries removed (M-11, enumerated); J2/J3 re-stated figure-void; the 5 point-rows' `join_key`/`verdict` re-stated to the J5/`JOIN_SUBSECTION` vocabulary their 23 sibling rows already carry; J5 unchanged (22/30 — the 8 `Units` SUBs stay unmapped, F4); `coverage` recomputed (`points_keyed` 0); inputs pinned; everything else byte-preserved |
| `_derived/book_layer/igcse-biology/book-join.json` | M | **additive only**: rows byte-preserved (172 J1 keys stand per F3); `join_keys` J2/J3 re-stated figure-void under M-8 (the landed "4/21 LO chunks carry incidental chips" and the probe's 10 punct-variant BODY tokens are figure captions — no keys stand or are added; J1 remains the sole point-key route of record); `coverage.uncovered_reasons` gains the 0-hit corpus search evidence for `2.10/2.38/2.40B/2.43B`; the J1 evidence-class note of record (W-F1-T1 ToC transcription, corpus-corroborated structure) added to `inputs`/the `w_f8_enrichment` note |

Zero changes to: any spec-side file, any books-lane file, the two structure files per
qual, the ial-* artifacts (including both indexes), the census (stays as landed),
CATALOG. No index files (F6). The 4CH1 evidence blocks' old-corpus chunk ids
(`edex-igcse-chem-NNNN`) stay as-landed (historical citations of the W-F4-T2 build; the
corpus-of-record migration is noted in the errata, not retro-edited).

## 5. Build gates (defined now, for W-F8-T2)

| gate | pass condition |
|---|---|
| G-F8-B1 | **Preservation:** every landed row/field not corrected re-derives byte-identically from the pinned landed blob (4BI1 rows verbatim; trio chapter rows/titles/pages/evidence/subsections/flags verbatim); the removal set is EXACTLY the probe2-proven entries |
| G-F8-B2 | **Correction soundness:** every removed entry independently re-derives figure-derived (M-8 both branches) or constant (M-9) from the pinned corpora, or classes `not_in_cited_evidence` (removal resting on F1); every retained point entry passes its evidence class (4BI1 J1 = the W-F1-T1 ToC receipt of record, not corpus chips) |
| G-F8-B3 | **Deepening soundness:** every new SUB mapping re-derives under M-10 (title containment re-verified normalised, unit/topic vetting re-checked); the uncovered sets match the probe exactly (4CH1 {SUB10, SUB11}, 4PH1 {8 × Units}, 4BI1 {}) |
| G-F8-B4 | **Resolution + surface:** every cited point_id/subsection code resolves against the pinned spec blobs; the landing surface is EXACTLY the 3 join files (3M), nothing else |
| G-F8-B5 | **Confinement:** spec-side, books-lane, structure files, ial-* artifacts, census byte-untouched (blob equality asserted) |
| G-F8-B6 | **Determinism:** `generated_utc` pinned; the emitter re-run reproduces all three files byte-identically (sha256) |

## 6. Non-goals

No index files (F6). No spec-side edits (SUB10/SUB11 adjudication and the 4PH1 `Units`
subsection rows are spec-side matters, routed). No books-lane writes (CATALOG drift
candidates stay routed to the books-lane owners). No census writes. No book acquisition
or fetches. No LLM anywhere. No new lanes fired. The W-F4-T2 `J2` route verdicts are
corrected in place — no retro-edit of any other W-F4-T2 statement outside the three join
files (the task-file note of this wave rides the records landing).

## 7. Definition of done

- Design of record + JSON receipt + worklog filed under `receipts/W-F8/` (with the
  records landing of this order); task file `tasks/W-F8-igcse-trio-join-completion.md`
  drafted.
- Probes of record cached (`cache/w-f8/probe.json`, `probe2.json`).
- W-F8-T2 executes in the same order (W-F6/W-F7 precedent): emitter + gates + swap
  staging + one revertible commit (3M); records landing (task file + receipts + the
  staged W-F7 push-confirm ride-alongs + the W-F7 task push clause + LEDGER Waves 50-52)
  follows as the next commit of the same order; push by separate operator order.
