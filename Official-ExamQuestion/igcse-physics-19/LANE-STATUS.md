# LANE-STATUS — igcse-physics-19 (Official-ExamQuestion)

> Landed 2026-10-26 (Task 16) under **ADR-039** ("the pipeline improves; provenance
> discloses") on the operator's explicit order to land the REVIEW-heavy corpus now
> rather than after the MS-parser wave (trace 1a174b2c6305cbfd). Re-generated
> 2026-10-26 (Task 17) after the MS-table parser wave (converter v0.19.0, LEDGER
> F72). Re-generated 2026-10-26 (Task 18) after the QP-side wave (converter
> v0.21.0, LEDGER F85). Re-generated 2026-10-27 (Task 21) after the crop-eyeball
> wave (converter v0.24.0, LEDGER F99) and the spec-labels wave (LEDGER F100) —
> the two open human-review surfaces this lane disclosed at Task 18 were both closed.
> **Re-generated 2026-10-27 (Task 22)** after the 2019-06 1P OCR source-layer wave
> and the 2023-06 2P repair-reconversion (converter v0.25.0, LEDGER F101/F102) —
> the two open conversion gaps of record are closed and the lane's convertible
> corpus is complete.
> This file is the lane's disclosure of record: what is served, what is honestly
> withheld, and which waves are open. Chemistry precedent:
> `AUDIT-2026-10-25-igcse-chemistry-19.md` and `AGENTS.md`.

## Verdict

**LANDED (Task 22 supersedes the Task 21 state); all gates green corpus-wide.**
55 of the 58 census paper dirs of the Edexcel IGCSE Physics (4PH1) corpus convert end-to-end
on converter v0.25.0 and are committed here as serving content: 540 questions, 2254 parts,
4970 marks, 545 figure assets. **Every slice passes every gate** — G0 identity (sha256 vs
archive manifests, staged fresh per slice), G1 structure (the physics footer law: 1P = 110,
2P = 70, every part-sum exact), G2-D disclosure, G3 MCQ integrity, G4 figure resolution,
G5 answer linkage, G6 registry (codes validated against the SME `igcse-physics-19`
registry), G7 solution emission — and every run's negative controls are DETECTED 3/3.
The corpus is now **55/55 fully PASS**: G5 answer linkage is corpus-complete
(2254/2254 parts carry their verbatim MS block), G3 MCQ keying is corpus-complete
(142/142 keyed), **spec tagging is corpus-complete (2187 llm-spec-wave + 67
no-spec-point + 0 pending-llm, every code G6-validated against the 186-code registry)**,
and **the figure review surface is EMPTY (0 assets carry review:true)** — the two
Task 18/21 surfaces stay closed and the two Task 22 conversion gaps are closed:

- **2019-06 1P — the OCR source-layer wave (F101)**: the archive QP is an image-only
  Pearson-DAM print-to-PDF scan (zero text layer; the Task 15 CRASH-RECEIPT class).
  The F41 chemistry machinery recovered it: 25 content pages transcribed from the
  600-dpi render (tesseract 5.5.0 --psm 6 drafts cross-checked against the healthy MS
  text layer; a per-page corrections ledger with evidence), staged as
  `UPLOAD/ocr/2019-06-1P/qp-pNN.txt` + `ocr-pages.json` (sha256-pinned, converter
  verifies, page_norm spliced — page anchors work end-to-end). G1 footer law holds on
  the recovered census: 12 questions, every part-sum exact, 110/110. The converter's
  empty-footer-census crash is now an honest machine-readable G1 FAIL attribution
  (fail-closed; the Task 15 ValueError is retired) — chemistry parity receipt:
  questions.md byte-identical, topic.json/validation-report identical modulo the
  version/timestamp headers, 7/7 assets byte-identical.
- **2023-06 2P — the repair-reconversion wave (F102)**: the Task 15 pastpapers
  mislabel-repair (the Examiners'-Report bytes that G0 could not see; the Paperlords
  plain QP, content-verified: cover 4PH1/2P June 2023, log P71957A, footer sum 70,
  sha-pinned in the archive manifest) is verified and consumed: G0 identity PASS on the
  repaired bytes, G1 footer law holds (8 questions, every part-sum exact, 70/70), the
  G0-D cover probe clean. The slice's 36 parts are G5-linked, 34 spec-tagged + 2
  terminal no-spec-point, and its 'grid' false-mention pair is eyeballed: the 6(a)(i)
  crop (the Q6 stem photograph served for the National Grid mention — the F99
  false-mention class recurring) is REJECTED to an honest stub; the 3(a)(i) 'grid'
  (the oscilloscope's positively charged grid component, a stem-owned figure) is
  stub-accepted per the lane's no-stem-figures convention.
- **The F99 crop verdicts stand corpus-wide** (65 eyeballed, Task 21) plus the Task 22
  tranche: 10 F45 manual crops on the 1P raster pages (every replacement rect
  proof-rendered and eyeballed before shipping; emitted PNGs byte-identical to the
  proofs), 2 accepted crops + 1 rejected + 1 stub-accepted on the 2P vector pages.

## Coverage (58 census dirs → 55 landed, 3 dispositioned)

All 17 series (2019-06 … 2026-06) are represented. The 3 non-landed dirs, each with a
standing receipt:

| dir | disposition | evidence |
|---|---|---|
| 2020-11 1PR / 2P / 2PR | **NO-QP** — the archive holds manifest + ms.pdf + er.pdf but no qp.pdf; `na:pmt-not-listed` (COVID print-reuse session; PMT never listed them) | Task 13 census + `docs/ledger/file-gap-sweep.csv` (pastpapers); Task 22 one-round source probe: the XtremePapers 2020-Nov deep path is session-gated, a Scribd document names a 4PH1 2PR que-20201124 scan but is not a clean archival source, the aggregator site is gated — the standing rule (repair only from a clean source) holds them |

## What is served vs withheld (the learner surface)

- **Served**: verbatim stems and problems, choices as printed, page-anchored provenance per
  part (the OCR slice anchors through the spliced page_norm; 20 of 2254 parts across the
  corpus carry no source_page under the same probe convention, disclosed), marks
  corroborating the printed QP totals, verbatim MS answer blocks for all 2254 linked parts
  (corpus-complete), keyed answers on **142/142** MCQ parts, spec codes where the
  registry resolved them (G6), figure crops for resolved mentions.
- **Withheld (disclosed): nothing.** The withheld surface is empty and the asset review
  flags are zero (Task 21 closed the human-review surfaces; Task 22 closed the two
  conversion gaps).
- **Provenance fields**: schema `syllabai.official-paper-questions/0.2`; every part
  carries `edit_status: "extracted"` and `value_trace` (no serving edits were made in
  any wave; the OCR layer IS the page's source layer of record, sha-pinned end to end).

## Figures

545 assets: 520 `kind:"crop"` + 25 `kind:"crop-required"` stubs. **0 assets carry
`review: true`** — all eyeball verdicts hold CROP-REVIEW homes (the Task 21 34 + the Task 22
2 `4ph1-<series>:<paper>` homes: the 1P's 10 accepted manual crops and the 2P's 2 accepted
+ 1 rejected + 1 stub-accepted). The 25 stubs are the chemistry-convention
disclosure class (eyeballed no-croppable-figure decisions, withdrawn wrong-region crops,
and stem-owned figures the lane does not serve).

## Spec tagging

**2254 of 2254 parts terminal**: 2187 carry registry-validated `llm-spec-wave` codes
(per-slice LLM adjudication against the 186-code SME registry over each part's printed
stem, problem, choices and verbatim MS answer block, hand-verified per part against the
published wordings — the F100 discipline; the Task 22 tranche added 0 near-miss
corrections: all LLM tags held) and 67 carry terminal `no_spec_point` decisions (pure
graph/table skills, apparatus choice, safety, design critiques, graph-type justifications,
data-relationship tests, and the Task 22 additions: scale-reading on the printed trace and
equipment recall — the F38 wave convention, reasoned per part in the labels files). **0
parts pending-llm.** The 55 wave files `spec-labels/4ph1-<series>[-<paper>].json` are the
labels of record; C101 pins the terminal state 4-papers-wide with bidirectional
labels↔corpus agreement.

## Converter provenance (v0.25.0 = v0.24.0 + F101/F102)

This lane's outputs were produced by **v0.25.0** = the Task 21 v0.24.0 state + the Task 22
waves: (1) the OCR source-layer consumption was already wired (F41); this wave stages the
1P layer and converts the slice; (2) the empty-footer-census branch fails closed with a
machine-readable G1 attribution instead of a bare ValueError (the Task 15 crash class);
(3) the physics EXPECT_QUESTIONS count registry now carries the two footer-verified
seeds 2019-06 1P = 12 and 2023-06 2P = 8 alongside the standing 2023-06 1P = 12 /
2024-06 2P = 8. Every change is lane-inert by construction: chemistry 2023-06 1C parity
receipt (v0.25.0 vs v0.24.0 on identical staging): questions.md byte-identical, 7/7
assets byte-identical, topic.json/validation-report.json identical modulo
`generated_utc` + the generator version string.

## Canaries

Battery of record: **104 canaries (99 + 6 Task 22 additions − the C4 chemistry pin
unaffected); the physics battery (20) holds 20/20 on the Task 22 corpus** — the local
filtered battery ran with only the 4ph1 lane present, so the chemistry/maths/whole-corpus
canaries could not resolve locally; the CI corpus-gates run judges them on the full
checkout. Task 22 additions: **C102** (2019-06 1P G1 PASS 110/110 — the OCR layer and the
1P footer law), **C103** (2019-06 1P question count 12 — the new EXPECT_QUESTIONS seed),
**C104** (2023-06 2P G1 PASS 70/70 — the repaired slice of record), **C105** (2023-06 2P
question count 8), **C106** (the 2023-06 2P 6(a)(i) National-Grid false-mention rejection
stays a crop-required stub — the F99 rejected demotion on its second corpus occurrence).
Standing pins: C74 (`no_pua_served`, spec 4ph1), C75 (2P footer law), C76 (2023-06 1P 12
questions), C83–C85, C89–C93, C99–C101.

## Open waves (prioritized)

1. ~~**Hub export + handover**~~ **CLOSED (Task 22, F103)**: the H1 baseline census
   receipted, the H2 comparison clean (55 official rows vs 43 SME provenance rows, 0
   blockers), and the **H3 cutover LANDED** — v2 PR #403 merged c89c71e64aee:
   `official-papers.json` (55 official sets, 540 questions / 2,254 parts / 4,970 marks)
   serves the Past Papers plane (first-match-wins over the SME reconstructions; the SME
   legacy 4PH0-era sessions keep SME as their source), the manifest pin is stamped to the
   data cut main@6298eb94479a25e3f3d22d66a51c29eb8b67e071, and the exporter/verifier of
   record are lane-generalized (`--spec 4ch1|4ph1`; chemistry parity byte-identical). The
   G8 post-completion audit of record: 55/55 slices fully PASS (G0–G7 + NC 3/3), the full
   CI battery green on PRs #183/#184, the F-187 verify + self-test green on both lanes,
   0 asset review flags, spec tagging terminal corpus-wide, and the served state
   re-read post-merge (55 sets / 4,970 marks / pinned ref) — the course is DONE under
   ADR-037/039 with the chemistry precedent complete.
2. **Chemistry re-staging wave** (F86): EXECUTED as the F111 corpus-wide re-receipt
   (2026-10-28, converter v0.29.2) — the current staging of record reproduces the served
   corpus modulo the seven named data-only curation classes (AUDIT-2026-10-28-f86-corpus-
   re-receipt.md); the C56 pin misses + C61 exception are CLOSED (the trio reproduces under
   the v0.29.1 lexeme fix). The txt-layer regeneration variant stays closed unless a future
   pdftotext/poppler change moves the line shapes (the receipt pins the current state). The
   physics analog closed WITH Task 21.
3. **run_all.sh / report aggregator generalization** (unchanged): both remain
   chemistry-scoped; the physics lane runs via the converter's `--spec 4ph1` interface
   with its own report generator for now.

## Receipts (local, cited not committed — F63)

`physics-intake/ocrwave/` (Task 22: the 600-dpi renders `pages600/` + the 200-dpi
reading set `pages200/` + the grid overlays `grids/`, the tesseract drafts `drafts/`,
the crop rect derivations + proofs `proofs/` and `crop_rects*.json`, the corrected
2P proofs `proofs2p/`, the LLM tag outputs `llmtags-1p.json`/`llmtags-2p.json`, the
F101 negative-control receipt `negtest/out.json`, the chemistry parity sandboxes
`v024/` + `run/parity-lane` + `parity_v2*.txt`, the upstream converter copies
`upstream/`, the handover receipt `receipts/`), `physics-intake/qpwave2/` (Task 21),
`physics-intake/census-4ph1.json` (Task 13), and the workspace worklog Tasks 13–22.
Rollback anchor: the Task 21 state is merge `bfea1450addc`; this wave's delta is the
converter (v0.25.0, the F101 fail-closed branch + the two EXPECT_QUESTIONS seeds),
the 2 new slices (2019-06/4PH1-1P + 2023-06/4PH1-2P), the 2 new spec-labels wave
files, the 2 new CROP-REVIEW homes, CANARIES.json (+6), the prep script
`scripts/prep_ocr_layer_1p_2019.py` (committed), and the lane docs.

## 2026-10-31 — F127: the corpus back-sync + questions.md regen (T-OEQ-PHYS-FORMAT-1 run-006)

The 4PH1 corpus of record now carries the five serving-plane format-restoration
runs (run-001..005, previously v2-side only): 339 pids / 766 field writes across
54 slices (every problem_md a wrap decomposition — the exporter-emitted stem
prefix + figure suffix subtracted via the exporter's own sentinel machinery, so
the corpus keeps the converter's field semantics; 7 stem_md regions synced where
a restoration reached the stem prose), every write accepted only when the
of-record r2-proof-era exporter rebuild round-trips the v2 plane of record
(22eda30) byte-exactly — the exporter re-export is a G-E1 no-op (55/55 slices,
0 deltas). The questions.md human renders regenerated with the of-record
renderer: restored presentation now served corpus-side (0 → 117 $-segments,
1 → 129 superscript restorations, the 2022-06 nuclear-decay line verbatim;
untouched slices byte-identical; double-render determinism proven; synced stems
render exactly once). The 766-pin zero-network battery (B1-B7) is CI-enforced.
The standing F121 group-stem evolution census (421 pids — the physics serving
twin of the chemistry wave) is disclosed
(`scripts/exporter-disclosures/2026-10-31-f127-groupstem-evolution-4ph1-standing.json`)
for the operator's ruling, NOT executed by this wave.

## 2026-10-31 — F128: the F121-groupstem serving wave (T-OEQ-PHYS-FORMAT-1 run-007)

The operator ruled ("F121-groupstem", trace 1a19135ba51a454d) and the physics
twin of the chemistry F121 wave is executed: the v2 plane of record (PR #548)
learned all 421 question-group intros — single-insertion problemMd writes (318
end-prepends + 103 mid-insertions after served question stems, the exporter's
print order preserved), problemMd-only, the class purely mechanical (zero 4PH1
ledger keys; G-E7 groups=421/served=421/splice=0), group intros
$-free/PUA-free; sha256 06d1848f... -> f0945d29.... Closure at both laws: the
r2-proof-era exporter (438aacb6) re-export is a no-op vs the PRE-serve plane
and the current-law re-export is a byte-level no-op vs the POST-serve plane
(G-E1 no-op, G-E7 421/421 in-run). The corpus of record is unchanged (a
plane-side serve; the manifest ref stays main@8f6a6a80). The f127 standing
disclosure retires by consumption (the r2-consumed twin) and the 421-pin
zero-network group-stem battery (B0-B5) is CI-enforced. Hygiene: the stray
F127 conflict-marker line removed; the f126-named disclosure path ref
corrected to the f127 file.

## 2026-11-01 — F129: the R1+R3 table-format corpus wave (T-OEQ-PHYS-FORMAT-1 run-008 W2)

Operator order: "W2 (R1+R3 in the resources corpus, page-evidence law, questions.md regen
rides)". The audit's pre-registered census gate re-verified fresh at the branch base
(origin/main 168b8582; physics corpus byte-identical to the census anchor): R1 = 29
degenerate one-column blocks / 26 SME parts (audit number reproduced exactly), R3 = the 3
official flattened/corrupt-header MCQ parts (2022-01 1P 1(a), 2024-06 1P 2(a), 2021-11 2P
1(b) — official-papers.json byte-identical since the audit, sha256 f0945d29…), 0
math-pipe conflicts. W2 lands corpus-side only (the v2 plane of record is untouched; the
serving leg rides the next converter run per the corpus-first law).

- **R1 (26 parts / 29 blocks, 12 SME subtopics)**: every 1-col degenerate pseudo-table
  rebuilt page-evidenced — 17 single-line word banks → true N-col GFM tables (terms =
  cells, scrape bold/italic verbatim), 6 multi-line banks (<br> line structure = rows) →
  N-col tables with explicit padding, 5 prose/label boxes (WARNING labels, student
  response, lifting-sheet explainer, italic sentence box) → blockquotes, 1 two-token
  label → 2-col table. Eyes-on evidence: live SME pages of record rendered headless
  (13 pages, 52 box crops, 7 contact sheets in
  `scripts/oeq_phys_run008w2/`); one DRIFT disclosed (3-3-sound — live SME reworded the
  question post-scrape 2026-09-17; rebuilt from the corpus's own gap+<br> transcription,
  no invention).
- **R3 (3 official MCQ parts)**: 2024-06 1P 2(a) and 2021-11 2P 1(b) — the flattened
  header tails removed and the printed tables restored as GFM tables in the stem
  (page-evidenced vs the QP pdf renders; the 2024-06 crop asset_2_a_table.png dropped
  from the registry per the maths-B Mode-A precedent, file kept); 2022-01 1P 1(a) — the
  four field-pattern DIAGRAMS restored as one composite page-evidenced crop
  (asset_1_a_diagram_choices.png); all three parts' choices go letter-only (text_md := ""
  — the hub's own mcqOptionsVisible/letterOnly convention: option content lives in the
  stem; labels + attested keys unchanged). edit_status "repaired:run008-w2-f129" +
  value_trace stamps per part.
- **R4 rider (2 pids, disclosed at pre-registration)**: the fresh census surfaced 2
  corpus-lag pids absent from every run-006/007 pins file (qstnprt_JHSpcZfPW7RxDt6t
  backtick nuclear-notation cells; qstnprt_qq3VPGgCZtyWTqzV $\text{square}$ tick cell) —
  corpus := v2 plane of record byte-exact (the run-006 field law), closing a live
  exporter-regression trap for the next serving leg. One benign transform pid
  (rFWG5Qh543f8GNmQ, asset-path rewrite) disclosed as NOT drift.
- **questions.md regen rides**: 15 files — official 3 via the of-record write_questions_md
  renderer (byte-fidelity proven on an untouched paper first), SME 12 via surgical block
  replacement (the shipped SME renders predate the current renderer and are not
  byte-reproducible by it — full re-render refused by design).
- **Gates GREEN**: post-census == pre-registration exactly (SME 1COL_DEGENERATE 29 → 0,
  MULTI_COL_OK 122 → 146; official corpus 0 → 2; math-pipe 0/0); G3 zero
  PUA/U+FFFD/C0 corpus-wide; T1 JSON round-trip on every touched file; T2 untouched
  slices byte-identical (36 modified files + 1 new asset = exactly the edited set);
  55 field/file pins (`scripts/oeq_phys_run008w2_pins.json`); plane of record v2
  untouched. Zero DB/Neon/prod contact.
- **Standing**: R2 (93 SME flattened parts, audit of record) + the june-2026-4ph1-1p
  single-paper inspection (absorbed into the census: zero pipe tables and zero flattened
  parts on that paper — the official trio above is the complete official-side defect set)
  + the serving leg (corpus → v2 plane re-export + manifest re-stamp) all remain for the
  operator's next orders. The tick-table `square` backtick residual (qq3VPGgCZtyWTqzV
  rows 2-4, corpus ≡ plane) is filed, not executed.
## 2026-11-02 — F131: the run-008 W2 serving leg + the 2022-01 1(a) corpus fix

The W2 corpus wave (F129, #269) is served: the of-record exporter re-export at the
declared data cut passes G-E1 (3 disclosed deltas = the 3 restored official MCQ parts,
exactly), G-E1b/G-E3/G-E4/G-E6/G-E7 (identity, constants, SME passthrough byte-identical,
labels, 421 group stems), and G-E5 (staging topics content-identical to the cut). The
exporter run surfaced one corpus defect — the 2022-01 4PH1-1P 1(a) problem_md kept an
inline image line against the official field semantics, doubling the figure on the
served plane; sole occurrence corpus-wide (scanned). Fixed here corpus-first: clean stem
in problem_md, the page-evidenced composite crop serves via the assets registry per the
field semantics; questions.md echo dropped. The SME leg (26 W2 parts / 29 degenerate
blocks → true N-col tables and prose boxes, per the F129 transforms of record) is
consumed surgically on the v2 plane in the same wave. Post-serve census expectation:
SME 1COL_DEGENERATE 29 → 0, MULTI_COL_OK 122 → 146; official plane pipe blocks 0 → 2;
math-pipe 0; untouched parts byte-identical. R2 (93 SME flattened parts) remains the
standing next wave.

## 2026-11-03 — F132: the run-012 wave-C L4 mapping-repair (corpus<->plane closure)

The run-012 reconciliation's last open population is closed. The definitive
per-question census (`scripts/oeq_phys_run012/wave-c/`) proves all 22 cross-id
fields are ONE mechanism: since T-CONSUME-EDX-2 (v2 c2388bca, 2026-10-21) the
serving plane's SME bank carried the LAST part's md content under earlier
parts' ids for 17 questions (18 solution_md + 2 problem_md+solution_md pairs);
the plane bank was born clean (seed 3a92153e) and stayed clean through EDX-1 —
the corruption site is the EDX-2 run's post-build stack, not the standing
importer (field-faithful). The corpus of record was correct at every visible
sha since 2026-09-17 and is UNTOUCHED by this wave.

Repair (RULE-1 L4, mapping-repair): the v2 serving leg writes the corpus of
record's own per-part content back under the right ids — plane := corpus
verbatim, asset hrefs hotlinked at data cut main@79b437615ac2 (the exporter's
own hotlink semantics; the reverse of L1, justified per L4). 22 fields / 20
parts / 17 questions / 10 topics; gates T1/G1–G6 green in-run; L6 drift-delta:
non-benign 22 → 0, raw drift 750 → 732 fields / 565 → 554 parts. Learner
impact: the 7-1 Po-210 grid question (with the run-011-m3-repaired isotope
notation) and the 5-3 molecules/sentences question serve again for the first
time since 2026-10-21, and the 15 solution-collapsed questions serve their
true per-part solutions again.

Ledger: RES-1 CLOSED (reconciled by run-010-m2/run-011-m3; residual benign);
DISC-5a "boilerplate reuse" superseded (same collapse mechanism); DISC-6 filed
(the EDX-2 stack attribution + the re-run-census-before-rebuild guard for the
platform lane). The cross-id population of the RULE-1 law is extinct
bank-wide; the corpus↔plane reconciliation is COMPLETE (0 non-benign drift).

## 2026-11-03 — F133: the DISC-6 hand-off (EDX-2 stack attribution + the census guard)

DISC-6 is closed from this lane's side: the EDX-2 stack sub-step is ATTRIBUTED
and the standing guard is DELIVERED. Verdict: the corruption step is the 23a
residual chain's clean-segment grafts V1 pass (of record in the EDX-2 receipt
as "321 (v1) + 36 (v2 gate-exact pairing)"); the v1 clean-source pool was
keyed per QUESTION+kind (last-write-wins), so every residual target field
received its own question's LAST part's content. Target selection is
quantified at the build pin aa0b4de1: 22/22 physics-19 targets' true contents
carry 23a-class pollution (18 prose-form speech-text + 4 unconvertible
multiline), while the 139 polluted non-last non-targets are ALL span-form =
the dictionary-repairable class. EDX-1's path-aligned grafts are the
counterfactual (bank stayed clean).

The delivered census guard (v2 `apps/hub/scripts/import_corpus/census_guard.py`
+ `CENSUS-GUARD.md`) scanned all 106 banks at v2 main fa8059d7 (44,502
questions / 148,978 md fields): igcse-physics-19 ZERO findings (the wave-C
repair holds bank-wide); 5 FURTHER EDX-2-corrupted fields confirmed in
igcse-physics-modular-24-unit-2 + igcse-science-double-award-17-physics (both
the radiation-family middle part, problem+solution) and ial-maths-20-decision-1
(post-patch pool variant) — per-field history walks flip every group at
exactly c2388bca (2026-10-21). Those 5 fields are the wave-D candidate
(plane := corpus L4 repair, wave-C shape; operator ruling requested). Benign
groups: cie-as-chemistry-25 (corpus-attested duplicate), ial-maths-20-
statistics-2 (of-record twin, born pre-EDX-2); the 20 maths-b fetch-bank
groups are corpus-free by the no_topic_questions ruling and stay owned by the
fetch-bank lane. Process findings of record: the v1/v2 graft scripts were
never committed (P1); the EDX-2 "reproducible path" still contains the
defective v1 pass — replay hazard (P2); the corruption was gate-invisible —
23a read ZERO after the grafts (P3).

Dossier: `scripts/oeq_phys_run012/wave-c/disc6/` (edx2-attribution.md +
3 census/walk artifacts); ledger DISC-6 → ATTRIBUTED + HANDED OFF. The v2
side carries the guard, the mandate, the hand-off receipt at
`.syllabai/receipts/T-CONSUME-EDX-2/DISC-6-handoff.md` and the baseline
receipt in this lane's artifacts dir. The corpus of record is untouched by
this wave.
