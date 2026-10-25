# LANE-STATUS — igcse-physics-19 (Official-ExamQuestion)

> Landed 2026-10-26 (Task 16) under **ADR-039** ("the pipeline improves; provenance
> discloses") on the operator's explicit order to land the REVIEW-heavy corpus now
> rather than after the MS-parser wave (trace 1a174b2c6305cbfd). This file is the
> lane's disclosure of record: what is served, what is honestly withheld, and which
> waves are open. Chemistry precedent: `AUDIT-2026-10-25-igcse-chemistry-19.md` and
> `AGENTS.md`.

## Verdict

**LANDED-REVIEW-HEAVY, fail-closed honest.** 53 of the 58 census paper dirs of the
Edexcel IGCSE Physics (4PH1) corpus convert end-to-end on converter v0.17.4 and are
committed here as serving content: 520 questions, 2,171 parts, 4,790 marks, 531 figure
assets. Every slice passes the structural gates — G0 identity (sha256 vs archive
manifests, staged fresh per slice), G1 structure (the physics footer law: 1P = 110,
2P = 70, every part-sum exact), G2-D disclosure, G4 figure resolution, G6 registry
(codes validated against the SME `igcse-physics-19` registry), G7 solution emission —
and every run's negative controls are DETECTED 3/3. What does NOT pass is exactly the
known physics MS-table parser wave, disclosed here and in every slice's
`validation-report.json`: **G3 MCQ keying** (39 FAIL / 14 PASS — 79 of 138 MCQ parts
carry choices as printed but no `is_correct`) and **G5 answer linkage** (11 FAIL /
42 REVIEW — 936 of 2,171 parts unmatched). Nothing is invented to fill those gaps:
unmatched parts serve question, marks and provenance with `answer_status: "unmatched"`
and no solution; keyed-vs-unkeyed is exactly the converter's honest refusal, never a
guess. Zero linked parts carry an empty `solution_md` (1,235/1,235 linked carry their
verbatim MS block). The corpus-wide review queue is 1,080 items: 936 linkage + 79 MCQ
keys + 35 crop-verify + 30 crop-required.

## Coverage (58 census dirs → 53 landed, 5 dispositioned)

All 17 series (2019-06 … 2026-06) are represented. The 5 non-landed dirs, each with a
standing receipt:

| dir | disposition | evidence |
|---|---|---|
| 2020-11 1PR / 2P / 2PR | **NO-QP** — the archive holds manifest + ms.pdf but no qp.pdf; `na:pmt-not-listed` (COVID print-reuse session; PMT never listed them) | Task 13 census + `docs/ledger/file-gap-sweep.csv` (pastpapers) |
| 2019-06 1P | **CRASH-RECEIPT** — image-only 144-dpi QP scan (32-char text layer); converter fails closed on the empty footer census (ValueError, receipted) | Task 15 run receipt; the physics twin of chemistry's F41 case; OCR-source-layer wave open |
| 2023-06 2P | **ARCHIVE-DEFECT** — the archived qp.pdf bytes are a 2PR Examiners' Report (sha faithfully matches its own manifest, so G0 cannot catch it; content-vs-paper identity is enforced only for the series field) | Task 14 receipt; pastpapers repair wave + ledger row owed |

## What is served vs withheld (the learner surface)

- **Served**: verbatim stems and problems, choices as printed (even when unkeyed),
  page-anchored provenance per part, marks corroborating the printed QP totals, verbatim
  MS answer blocks for all 1,235 linked parts, spec codes where the registry resolved
  them (G6), figure crops for resolved mentions.
- **Withheld (disclosed)**: `is_correct` on the 79 unresolved MCQ parts (the physics MS
  prints its key in a cell-per-line table layout the parser wave has not yet mastered);
  `solution_md`/`mark_points` on the 936 unmatched parts. G5-REVIEW slices serve their
  linked parts normally — the REVIEW state is about the unlinked remainder.
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

This lane's outputs were produced by **v0.17.4** = the byte-exact restore of the
v0.17.3 physics PUA tranche (merge `2254347353`) **plus F67** (the vertical-MS-lane
F48 PUA gate). The tranche had been clobbered on main by the #136 tree-snapshot merge
(third occurrence of the concurrent-merge clobber class — F66 below); the landing
re-ships it with its outputs, per the "commit outputs and pipeline changes together"
convention. Chemistry bit-identity: `parse_ms_vertical` is 4ph1-only
(`ms_layout: "vertical"`), chemistry never calls it — by construction, the same
argument v0.17.0 itself was landed under; the restored v0.17.3 delta carried the
Task-15 chemistry no-op receipt (byte-identical outputs modulo `generated_utc` +
generator string).

## Canaries

`check_canaries.py` gained the spec-lane registry (each canary may carry
`spec: "4ch1" | "4ph1"`; chemistry defaults unchanged — bit-identical behavior). New
pins: **C74** (`no_pua_served`, spec 4ph1, corpus-wide absence law + two π-mapping
pins — written to catch the clobber class and it promptly caught the F67 leak
pre-ship), **C75** (4PH1 2P footer law: G1 PASS, marks_total 70), **C76** (2023-06 1P
prints 12 questions). Battery of record: **74/74 hold** on these outputs.

## Open waves (prioritized)

1. **Physics MS-table parser** (the one big wave): cell-per-line MS layout — G3 keying
   (79 parts) + G5 linkage (936 parts). The vertical-lane state machine (v0.17.0) and
   its successor fixes are the foundation; the remaining work is the option-column /
   tick-glyph semantics that chemistry's row parser never needed.
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

`physics-intake/runs-landing/*.json` (53 fresh v0.17.4 run receipts + 5 dispositions),
`physics-intake/run-matrix.json` (Task 15 wave), `physics-intake/census-4ph1.json`
(Task 13), `physics-intake/pua-evidence/` (font traces + page renders), and the
workspace worklog Tasks 13–16. Rollback anchor: this lane replaces **nothing** (it did
not exist); the converter restore replaces main's clobbered v0.17.2 blob at `6a0779e0`.
