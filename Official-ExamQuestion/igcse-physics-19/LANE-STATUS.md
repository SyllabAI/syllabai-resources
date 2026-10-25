# LANE-STATUS — igcse-physics-19 (Official-ExamQuestion)

> Landed 2026-10-26 (Task 16) under **ADR-039** ("the pipeline improves; provenance
> discloses") on the operator's explicit order to land the REVIEW-heavy corpus now
> rather than after the MS-parser wave (trace 1a174b2c6305cbfd). **Re-generated
> 2026-10-26 (Task 17)** after the MS-table parser wave (converter v0.19.0, LEDGER
> F72) closed the G3/G5 deltas this file originally disclosed. This file is the
> lane's disclosure of record: what is served, what is honestly withheld, and which
> waves are open. Chemistry precedent: `AUDIT-2026-10-25-igcse-chemistry-19.md` and
> `AGENTS.md`.

## Verdict

**LANDED (Task 17 supersedes the Task 16 LANDED-REVIEW-HEAVY state); fail-closed honest.**
53 of the 58 census paper dirs of the Edexcel IGCSE Physics (4PH1) corpus convert end-to-end
on converter v0.19.0 and are committed here as serving content: 520 questions, 2,171 parts,
4,790 marks, 531 figure assets. **Every slice passes every gate** — G0 identity (sha256 vs
archive manifests, staged fresh per slice), G1 structure (the physics footer law: 1P = 110,
2P = 70, every part-sum exact), G2-D disclosure, G3 MCQ integrity, G4 figure resolution,
G5 answer linkage, G6 registry (codes validated against the SME `igcse-physics-19`
registry), G7 solution emission — and every run's negative controls are DETECTED 3/3.
The Task 16 open deltas are closed by the F72 MS-table parser wave: **G5 answer linkage is
corpus-complete (2,171/2,171 parts linked; Task 16 baseline 1,235 — the vertical marker
census found 6 marker-row artifact classes + 3 keying shapes, all fixed vertical-lane-gated)**
and **G3 MCQ keying is 134/138 (PASS 49 / FAIL 4)** — the 4 fails are QP-side structural
classes, disclosed below and in each slice's `validation-report.json`, never guessed: two
choice-label extraction drops (2020-01 1PR 1(b) labels A-C where the MS references arrow S;
2023-06 2PR 7(a) labels A-E where the MS references F) and two non-MCQ questions the QP
parser types as `multiple_choice` (2022-06 2PR 1(a) is a draw-a-matching-line question;
2026-06 1PR 1(a) is a name-the-object labelling question). Zero linked parts carry an empty
`solution_md`. The corpus-wide review queue is 67 items (Task 16: 1,080). One correction
to record honestly: the wave FIXED a Task 16 mis-link the old pin had codified — 2024-11
1P 1(b)(ii) served the 1(c) block ('22/7 for π') because the old parser never opened the
(c) letter entry; it now serves its true MCQ block ('B - gravitational;', keyed B) and 1(c)
serves its own (C74's pin re-anchored to 1(c), receipted in F72).

## Coverage (58 census dirs → 53 landed, 5 dispositioned)

All 17 series (2019-06 … 2026-06) are represented. The 5 non-landed dirs, each with a
standing receipt:

| dir | disposition | evidence |
|---|---|---|
| 2020-11 1PR / 2P / 2PR | **NO-QP** — the archive holds manifest + ms.pdf but no qp.pdf; `na:pmt-not-listed` (COVID print-reuse session; PMT never listed them) | Task 13 census + `docs/ledger/file-gap-sweep.csv` (pastpapers) |
| 2019-06 1P | **CRASH-RECEIPT** — image-only 144-dpi QP scan (32-char text layer); converter fails closed on the empty footer census (ValueError, receipted) | Task 15 run receipt; the physics twin of chemistry's F41 case; OCR-source-layer wave open |
| 2023-06 2P | **ARCHIVE-DEFECT** — the archived qp.pdf bytes are a 2PR Examiners' Report (sha faithfully matches its own manifest, so G0 cannot catch it; content-vs-paper identity is enforced only for the series field) | Task 14 receipt; pastpapers repair wave + ledger row owed |

## What is served vs withheld (the learner surface)

- **Served**: verbatim stems and problems, choices as printed, page-anchored provenance per
  part, marks corroborating the printed QP totals, verbatim MS answer blocks for all 2,171
  linked parts (corpus-complete; the 2026-06 2P 4(c)(i) equation-image answer serves via
  `MS-LINK-OVERRIDES.json` under the F42 doctrine — eyeballed from the rendered MS page,
  never model guessed), keyed answers on 134 of 138 MCQ parts, spec codes where the registry
  resolved them (G6), figure crops for resolved mentions.
- **Withheld (disclosed)**: `is_correct` on the 4 structural MCQ failures listed in the
  verdict (the fix belongs to the QP choice-extraction/question-typing wave, not to the MS
  lane); that is the entire withheld surface.
- **Provenance fields**: schema `syllabai.official-paper-questions/0.2`; every part
  carries `edit_status: "extracted"` and `value_trace` (no serving edits were made in
  this wave — the PUA symbol-glyph normalizations are converter-level, per the F48/F52
  precedent, evidenced by font traces + page renders in the v0.17.3 tranche).

## Figures

531 assets: 501 `kind:"crop"` + 30 `kind:"crop-required"` stubs. 65 crops carry
`review: true` — the CROP-REVIEW ledger has **no 4ph1 homes yet** (chemistry verdicts
are the only entries); the physics crop-eyeball wave is open. Per the AGENTS review
taxonomy, `figure crop emitted — human verify` (35) and `figure crop required` (30)
stay human queues.

## Spec tagging

0 of 2,171 parts tagged — every part is an honest `pending-llm`. The SME
`igcse-physics-19` registry (8 topics, 184 codes) is wired and G6-validates every code;
the physics spec-labels wave (`spec-labels/4ph1-<series>[-<paper>].json`) is open.

## Converter provenance (the restore disclosure)

This lane's outputs were produced by **v0.19.0** = the Task 16 restored tranche (v0.17.3
+ F67) **plus the F72 MS-table parser wave**: six vertical marker-row families (triple
qn+letter+roman rows, letter+content rows, qn+content rows under an ascending+tail+indent
triple gate, an indent gate against notes-wrap paren tokens, a paren-less letter cell, an
orphan-roman re-anchor) + continuation-append semantics, and three vertical-gated keying
refinements (bare-key `B;` rows, paren-span-stripped rebuttal detection, the pure-
elimination F14 arm). `parse_ms_vertical` and every keying refinement are 4ph1-only
(`ms_layout: "vertical"` gates); chemistry never executes any of it — bit-identity by
construction, receipted: 2023-06 1C pre (main 0.18.0, wave-25) vs post (0.19.0) on identical staging
— topic.json / validation-report.json / questions.md byte-identical modulo the version
string, 7/7 assets byte-identical, gate stdout identical. The battery caught one
self-inflicted regression pre-ship (a first-paren rebuttal split broke 2025-11 1P 9(b);
fixed to paren-span stripping) — the battery law worked twice in one wave (F67's C74,
now this).

## Canaries

`check_canaries.py` gained the spec-lane registry (each canary may carry
`spec: "4ch1" | "4ph1"`; chemistry defaults unchanged — bit-identical behavior). Pins:
**C74** (`no_pua_served`, spec 4ph1, corpus-wide absence law + two π-mapping pins —
wrote to catch the clobber class, caught the F67 leak pre-ship, and its π pin exposed
the Task 16 mis-link the wave then corrected), **C75** (4PH1 2P footer law: G1 PASS,
marks_total 70), **C76** (2023-06 1P prints 12 questions), **C83** (2024-06 2P G3 — the
triple-glue MCQ keying), **C84** (2023-01 2P G5 — the qn-content bootstrap + indent
tolerance), **C85** (2026-06 2P G5 — the orphan-roman re-anchor + the F42 override).
C57 (`ms_link_overrides_ledger`) is now lane-aware (the ledger's first physics entry
was invisible to its chemistry-scoped corpus scan). Battery of record: **83/83 hold**
on these outputs.

## Open waves (prioritized)

1. **QP-side structural fixes for the 4 G3 fails** (the wave the MS-table wave could
   not close, disclosed not guessed): choice-label extraction drops (2020-01 1PR 1(b),
   2023-06 2PR 7(a)) and question-typing for non-MCQ choice-bearing questions
   (2022-06 2PR 1(a) matching, 2026-06 1PR 1(a) labelling — these need a
   `question_type` distinction, which is a serving-schema conversation, not a parser
   patch).
2. **Crop eyeball wave**: 65 review-flagged crops + 30 crop-required stubs →
   CROP-REVIEW 4ph1 homes (`4ph1-<series>:<paper>` convention).
3. **Spec-labels wave**: 2,171 `pending-llm` parts → registry-validated labels.
4. **2019-06 1P OCR source layer** (F41 machinery exists from chemistry) + the
   converter's empty-footer-census crash → fail-closed attribution instead.
5. **pastpapers repair waves**: 2023-06 2P mislabel bytes (Examiners' Report); the 3
   2020-11 missing QPs stay `na:pmt-not-listed` unless a source surfaces.
6. **Hub export + handover**: NOT started — the hub plane still serves the SME sets
   for physics; `official-papers.json` does not exist for igcse-physics-19 and the
   two-file exporter needs a bootstrap decision (no prior bundle of record). The
   H1→H2→H3 handover protocol applies only when conversion completes (all gates
   green), per AGENTS.md.
7. **run_all.sh / report aggregator generalization**: both remain chemistry-scoped
   (`igcse-chemistry-19`, 4CH1 globs, PAPER_TOTALS 1C/2C); the physics lane runs via
   the converter's `--spec 4ph1` interface with its own report generator for now.

## Receipts (local, cited not committed — F63)

`physics-intake/runs-mswave/*.json` (53 fresh v0.19.0 run receipts + 5 dispositions,
consolidated.json), `physics-intake/ms-forensics/` (the F72 census: step1-census,
step3-shapes, step4-split + the 2026-06 equation-image render),
`physics-intake/runs-landing/*.json` (Task 16 v0.17.4 receipts, the baseline),
`physics-intake/census-4ph1.json` (Task 13), `physics-intake/pua-evidence/` (font
traces + page renders), and the workspace worklog Tasks 13–17. Rollback anchor: the
v0.17.4 state is merge `2e19a43e`; this wave's delta is the converter + checker +
ledger/docs — no serving file changed shape beyond the linkage corrections the gates
prove.
