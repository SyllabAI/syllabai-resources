# CHANGELOG — official_examq_extract.py (ADR-037 converter)

Semantics: outputs embed `generator: official_examq_extract.py v<version>`, so any
topic.json traces to exactly this behaviour. Every version bump must follow the
AGENTS.md improvement loop: ledger entry (F#) + canary + full-corpus re-run.

## 0.14.0 — 2026-10-22 · wave-20: the stem-figure tranche (the wave-19 backlog closes)

The wave-19 stem restore (F53) carried 50 keep-verdicts flagged for figures the stems
introduce but no part ever mentions — 38 qp-fig, 2 interleaved tables, 9 formulae
letter-runs, 1 box-ok (handled) — plus 2 already-served figures and 1 retired mis-flag
found during reconciliation (2023-11 1C Q7: no displayed formulae exist in that question;
QP pp.18-19 eyeballed). This wave crops them all.

- **Converter (F57)**: the question-stem figure pass reads `stemFigures` specs from
  STEM-RESTORE.json (id/page/rect/mention/target, the eyeballed crop tranche) and emits
  a crop-required stub on the target part (first part unless `target` names one); the
  EXISTING F45 manual_crop branch renders it at verdict time — the box is the human
  decision, the render deterministic at CROP_DPI. Fail-closed: malformed spec or asset-id
  collision aborts the run.
- **Eyeball evidence (48 crops)**: every rect derived from document geometry (intro-sentence
  bottom → first-part top band; figure clusters inside the band; label-absorption for
  callouts; raster pixel-profiling for 2019-06 p12) and eyeballed against the printed page
  — 37 of 48 first-candidate rects needed manual correction (clipped callout labels,
  prose swallowed by absorption, band slivers from label-bottom layouts), fixed and
  re-eyeballed to final. Converter renders are byte-identical to the evidence renders.
- **Exporter v6 (F-W20-1/F-W20-2)**: stem-figure assets on a question's first part render
  INSIDE the stem block (prose → figure → part text); assets targeted at a later part
  (2019-06 2C bond-energy tables → 5(a)(i)) render in that part's normal figure slot;
  `stemFigureRef` inlines an already-cropped figure (2022-06 1C Q4, 2022-01 2CR Q3 — both
  F28 share-ref collapses resolved through ref_part). `entry.dropSpan [from, to)` removes
  the mid-stem flattened label run; `entry.dropTail` removes the tail soup the crop now
  serves visually — both anchors verbatim, fail-closed.
- **Corpus effect**: exactly 30 of 54 slices change; 48 new crop assets (43 stem-figure
  crops + 5 part/extra figures incl. the 2019-06 2C three-figure split); ZERO changes to
  any other extraction field (marks, problem_md, solutions, spec codes, links all
  byte-identical); 24 slices byte-identical. The exporter's own census: 48 changed parts
  (46 {assets, problemMd} + 2 {problemMd}-only refs), 0 new/gone ids.
- **Canaries**: 68 hold — C66 corpus-wide bidirectional stem-figures ledger check,
  C67/C68/C69/C70 pins (chromatogram, bond tables, raster structures, formulae letter-runs).
  Floor 0.14.
- **Part C — solution enrichment (F60, exporter F-W20-3)**: SOLUTION-ENRICH.json
  (syllabai.official-solution-enrichment/0.1) — 124 authored worked answers for every
  part of the two flagship sets (2019-06 1C: 64 parts, 2020-01 1C: 60 parts), MS-terse
  median 165 chars → SME-style narrative walkthroughs (median authored ~700 chars). The
  doctrine rules hold: values are never invented — the build-time review pass runs a
  numeric-token census (printed data must appear in the question/QP evidence; derived
  values must verify as correct arithmetic on printed data via an equation scanner that
  re-computes every a×b=c / a÷b=c / a−b=c chain in the authored text) plus
  enrichment-vs-marking-scheme coverage and PUA/junk checks — 0 problems at ship.
  The MS-derived solution_md and mark_points stay verbatim in the corpus and the
  markPoints the hub serves; the authored text replaces only the learner-facing
  solutionMd at export (C71 pins the export-only law). 124/124 entries resolve;
  68→69 canaries.
- **Tooling**: run_all.sh gains the F-178 registry skip guard (2021-06/2021-11/2023-11/
  2024-11/2025-11 never printed 1CR/2CR — the runner no longer crashes in G0 on them);
  a rebuilt-from-clean staging area reproduces all 54 committed topics byte-identical
  (modulo the converter header) before the wave's changes — baseline receipt.

## 0.13.1 — 2026-10-22 · F52: the corpus-wide ǻH → ΔH normalization (operator dispatch, trace 1a163a753e3bd999)

The 0.13.0 known-artifact carry note is superseded: the artifact is FIXED corpus-wide. MyriadPro-It's
custom encoding renders the printed italic Delta as **U+01FB** (bytes C7 BB; visually confusable with
U+01DF — the first codepoint guess was wrong and the no-op parity run caught it: a wrong-char mapping
produces zero content deltas across all 54 slices, a deterministic disproof). `normalize_pua` gains the
evidenced non-PUA mapping U+01FB → U+0394 **before the PUA gate** (and on both G2 sides — the line scan
and the page-level norm — so verbatim overlap is unaffected).

- **Census of record**: 5 raw-layer hits (2020-01 1CR ×2, 2020-01 2CR ×3), all immediately before 'H';
  the 32-set 1C/2C corpus and every other R slice is clean (C7 BB absent corpus-wide outside these 5).
- **Evidence**: 2020-01 1CR p18 renders 'Calculate the molar enthalpy change, ΔH, in kJ/mol.' and
  'ΔH = ...... kJ/mol'; 2020-01 2CR pp19-20 render '...the enthalpy change, ΔH.' and 'ΔH = ...'
  (font trace MPEIOE+MyriadPro-It, Type 1C Custom encoding; renders eyeballed).
- **Whole-corpus re-run parity**: 158 files normalized-identical (generator/timestamp-normalized);
  exactly 4 content-diff files — the two 2020-01 R slices' topic.json + questions.md (ǻ→Δ ×5). The
  surgical-change proof; no census count moves (79Q/423P/770M tranche unchanged; part ids unchanged, so
  the wave-16 disclosure remains exact).
- **Canary**: C65 pins the law — corpus-wide U+01FB absence (the `no_pua_served` checker gains the
  optional `extra_chars` [[bad, good], ...] field, v0.13.1) + the three fixed parts' exact ΔH strings.
  CANARIES floor 0.13.1; 63 canaries hold.

## 0.13.0 — 2026-10-22 · the 2CR tranche: the second R-variant corpus + evidenced PUA extensions (trace 1a16373bc7d373fd)

The R-VARIANT SCHEDULE's second tranche converts: 11 × 4CH1/2CR papers (2019-06 → 2026-06,
79 Q / 423 P / 770 marks, every series G0–G7 PASS with Σ=70/70 footer-enforced), staged
from the archive of record (r2cr staging: qp/manifests from the footer-verified r-verify
set, ms.pdf fetched fresh per series, text layers regenerated; every PDF sha256-pinned
against its manifest, 22/22). All parts enter `pending-llm` under the anchor law — the
spec-label waves are the next step (636 1CR parts already waiting). The improvement loop
is QUIET this tranche: no parser law changed; every series passed G0–G7 + NC 3/3 on the
first or second pass (the two first-pass refusals were the F48 fail-closed PUA law doing
its job). The 43-set corpus of record is byte-identical modulo generator/timestamp —
parity evidence: the exporter's wave-16 census reproduces the wave-15 1CR slug part
lists IDENTICALLY, and G-E1b identity holds on all 32 common sets.

- **PUA map additions (F48 evidence standard)** — 2019-06 2CR prints the Wingdings2 tick
  `\uf050` ('Add ticks (✓) to the table...', p16 render) → U+2713 (the corpus's third tick
  glyph, after F033 ZapfDingbats + F0FC Wingdings). 2023-01 2CR prints the Symbol
  big-bracket RIGHT trio `\uf8f9/\uf8fa/\uf8fb` (the 4(b)(ii) repeat-unit answer scaffold,
  p9 render, positional top/mid/bottom pairing with the mapped left trio) →
  U+23A4/23A5/23A6 — this retires the v0.12.0 right-column mirror caveat with direct
  evidence: the 6-piece bracket pair is now fully mapped. C56 pins both corpus-wide.
- **F45 manual-crop pass (three stubs → real crops, eyeballed)** — 2020-01 2CR 1(a)(ii)
  five particle boxes (the MCQ options reference box numbers; particle drawings are
  unrecoverable from text), 2020-01 2CR 6(c) displayed-formulae + bond-energy table block
  (the text layer loses the bond glyphs: 'C C 612'), 2023-01 2CR 8(a) energy-axis scaffold
  (same printed-skeleton class the automatic pass crops elsewhere in this tranche). Rects
  derived from fitz drawing/word geometry, eyeballed against 150 dpi renders; live in
  CROP-REVIEW.json (`2020-01:2CR`, `2023-01:2CR` homes), re-render deterministically.
- **Review close-out** — 11 queue items eyeballed: 8 emitted crops accepted as-is, 3
  crop-required stubs became the F45 manual crops above; final state 0 review flags on
  the 2CR tranche, 11 `:2CR` CROP-REVIEW homes of record.
- **Known artifact carried (documented, not normalized)** — 2020-01 2CR prose carries
  `ǻH` where ΔH prints (MyriadPro-It custom encoding renders italic Delta as U+01DF);
  the landed 2020-01 1CR corpus carries the same artifact, so both tranches are
  consistent and G2-verbatim-faithful to their source layers. A future normalization
  (→ U+0394 corpus-wide) is an operator-level improvement item touching both 2020-01
  slices together.

## 0.12.1 — 2026-10-22 · exporter F51: the data-cut stamping law (G-E5)

Exporter-only follow-up (converter stays 0.12.0; zero corpus changes; 65 canaries
untouched; no corpus file is read or written differently):

- **The wrinkle of record (v2 PIN-TIGHTEN-1, fc7a5dc2)** — the pilot hub manifest's
  `importSource.ref` named the exporter-of-record commit (main@bf8d56c3, F44's landing)
  while the wave-14 run actually consumed 855cddcf; the pin under-claimed and had to be
  tightened forward by hand. Root cause filed open there: the exporter of record left
  the ref untouched every run ("importSource.ref stays"), so the pin could only drift
  from the data.
- **G-E5, the data-cut law (runs first, whenever a manifest is staged)** — the run
  declares `--source-cut main@<40-hex>` (REQUIRED with --manifest, refused without it,
  format fail-closed); the exporter then proves every consumed staging topics file
  content-identical to that cut's committed topic.json (modulo the generated_utc/
  generator converter header — the data plane must match canonicalized byte-exact;
  git-show against the repo of record, missing staging file or unknown cut aborts) and
  STAMPS the declared cut into the staged manifest's `importSource.ref`. Fail-closed,
  no disclosure path: identity is a law (the G-E1b precedent) — a runner whose staging
  copies are not the declared cut re-stages or re-declares; it can no longer stamp a
  pin the data cannot prove.
- **Note text stays the per-wave hardcode of record** — the wave description bump
  remains a reviewed-PR act (the F44 law); the stamped ref no longer depends on it.
- **Negative controls verified live** (all refused before any write): malformed
  --source-cut format; a well-formed 40-hex cut absent from the repo; a one-byte-
  tampered staging copy. Positive control: the full 43-slice run against the hub
  bundle of record with the wave-15 disclosure + --allow-new-official — G-E5 +
  G-E3/G-E2/G-E1/G-E1b/G-E4 all green, staged manifest ref = the declared cut.

## 0.12.0 — 2026-10-22 · the 1CR tranche: registry + first R-variant corpus + QSTART/marker repairs (F49–F50)

The R-VARIANT SCHEDULE's first tranche converts: 11 × 4CH1/1CR papers (2019-06 → 2026-06,
118 Q / 636 P / 1210 marks, every series G0–G7 PASS with Σ=110/110 footer-enforced), staged
from the archive of record (qp/ms PDFs sha256-pinned against the archive manifests; MS files
fetched for this run). All parts enter `pending-llm` under the anchor law — the spec-label
waves are the tranche's next step. Corpus of record (32 sets) byte-identical modulo
generator/timestamp after every change below.

- **1CR/2CR registry entries (F-178 protocol)** — `PAPER_TOTALS` gains 1CR=110/2CR=70;
  `EXPECT_QUESTIONS` gains the footer-verified per-series counts (1CR×11 + 2CR×11, tracker
  PR #32 receipts). The 2CR rows are filed with the registry per the filed protocol; their
  outputs land in the 2CR tranche.
- **PUA map additions (F48 evidence standard)** — 2019-06 1CR prints the ZapfDingbats tick
  `\uf033` ('Place ticks (✓) in three boxes') → U+2713; 2022-06 1CR prints the Symbol
  big-bracket trio `\uf8ee/\uf8ef/\uf8f0` (the drawn repeating-unit scaffold of 7(d)(i)) →
  U+23A1/23A2/23A3 with the documented right-column mirror caveat. C56 pins both.
- **QSTART first-match law (F49)** — the question-start driver now takes the region's FIRST
  `<N> <alpha>` line; the isotope-label false match that truncated 2023-06 1CR Q3 (its whole
  (a) group lost, G1 4/8) is structurally impossible. C59 pins the shape.
- **Degraded-marker MS branches (F50)** — `MS_DEGRADED_MARKER_RE` (fires only when a paren
  pair is missing), the glued `b(iv)` alternative, `MS_HALF_ROMAN_RE` and the gated
  `MS_SIDEBAR_LETTER_RE` heal all four marker degenerations of the R-era MS layouts; 14
  linkage refusals + 1 MCQ key refusal resolve with zero per-series special-casing, and the
  one genuine wrap-split answer cell (2022-01 1CR 8(b)(i)) is human-transcribed into
  MS-LINK-OVERRIDES per the F47 law. C60–C64 pin them; 15 crop/stub items eyeballed into
  CROP-REVIEW (11 accepted + 4 stub-accepted across 8 `<series>:1CR` homes).

## 0.11.0 — 2026-10-22 · wave 14: the 3 honest answer-linkage refusals + PUA→Unicode (F46–F48)

The corpus review queue empties of linkage items: G5 100% on 2019-06 1C (64/64) and
2023-11 1C (66/66); review_queue holds only the 4 documented genuinely-blank stub
verdicts corpus-wide.

- **Deep-indent roman MS rows (F46)** — the 2023-11 1C MS prints the 6(c)(ii)/6(d)(ii)
  answer rows at indent 22, past MS_ROW_RE's `{0,20}` window; both rows were absorbed
  into the (i)-blocks and the parts stayed honestly unmatched. New `MS_DEEP_ROMAN_RE`
  branch (indent 21–30, parenthesized romans only, ascending-sequence gate keyed on the
  current entry's roman). Corpus-wide scope audit: exactly the 2 target rows match.
- **MS-LINK-OVERRIDES ledger (F47)** — the MCQ-KEYS human-adjudication doctrine extended
  to structured parts: 2019-06 3(d)(ii)'s MS answer cell is a printed image (Property
  table with ticks); the ledger carries the rendered-page evidence and the verbatim
  tick-table transcription; converter applies it before solution emission, fail-closed
  (only when positional linkage found nothing, never for MCQ parts). The superseded
  staged design (interpretive summary + ms.pdf image asset) violated the verbatim
  doctrine and was declined.
- **PUA→Unicode pass (F48)** — 23 distinct Private Use Area chars in the source text
  layer (SymbolMT / Wingdings 1-2-3 / EuclidExtra / CID subsets), ~2.4k served-string
  occurrences, all mapped from per-glyph evidence (font trace + page render): → ×3,
  Δ ×2, ⇌, Σ, ✓, • ×3, °, ×, ÷, −, ─, ↑; dotted answer-line rules + 5 cover-page
  ornament pairs dropped as furniture. Normalization sits at text ingest (clean_lines)
  and on page_norm (same table both sides of the anchor probes) and is FAIL-CLOSED: an
  unmapped PUA char aborts the run. Four page anchors recover (2021-06 2C 7(c)(i),
  2022-06 2C 5(c)(ii), 2025-06 2C 6(a)(ii), 2026-06 1C 7(a)(ii) — each verified).
- **Corpus effect** — 256/256 gates PASS; parity vs v0.10.1 audited per-field: zero
  marks / spec-code / asset changes, part census 1548 unchanged; deltas are exactly the
  PUA strings + the 3 linkages (+ (i)-block de-pollution) + 4 anchor gains + gate-detail
  improvements. The exporter's G-E1 no-op law caught this run's first glyph draft
  (en dash / em dash) against the bundle of record; the corpus adopted the better-evidenced
  U+2212 (minus) and U+2500 (bond rule) instead; the final export discloses exactly one
  delta — the 3(d)(ii) corpus-of-record reconciliation.
- **Canaries** — 56 hold: C52 rewritten (refusal pin → adjudicated-linkage pin), C56
  no_pua_served (corpus-wide absence + 9 mapping pins), C57 ms_link_overrides_ledger
  (bidirectional), C58 deep-roman linkage; converter_version_floor 0.11.0.

## 0.10.1 — 2026-10-22 · optional crop pass: ledger-driven manual crops (F45)

The 8 crop-required stubs are dispositioned: 4 become real crops, 4 are re-verified
blank with fresh evidence.

- **Manual crop pass (F45)** — a CROP-REVIEW verdict entry may now carry
  `manual_crop: {page, rect}` (PDF points). At verdict-application time the converter
  renders that eyeballed box from qp.pdf at 150 dpi into `assets/<id>.png`, flips the
  stub to a real crop (`kind: "crop"`, `render: "raster"` when the box sits inside a
  page raster), and marks the asset `manual_crop: true`. Fail-closed: requires
  `verdict: "accepted"` on a `crop-required` stub, box page must equal the stub page,
  rect well-formed and ≥20pt per side, else the run aborts. The F19b doctrine is
  unchanged for the AUTOMATIC pass; the manual box is the eyeballed human decision
  and re-renders deterministically on every re-run.
- **Corpus effect** — 4 stubs → crops: 2020-11 5(b)(iv) CH₃Cl skeleton (p15), 2023-11
  6(b) H-O-O-H skeleton (p15), 2024-06 7(b) N-N skeleton (p14), 2019-06 15(a) tests
  table cropped straight from the rasterized p26 archive scan (no text anchors needed
  for a manual rect). 4 stubs re-verified genuinely blank at 150 dpi (2021-06 8(b)(iii),
  2025-06 9(a)(i), 2026-06 6(b), 2021-11 2C 5(c)) — stub-accepted stands, notes carry
  the re-verification. The corpus review queue now holds only the 3 honestly-unmatched
  answer linkages; zero "figure crop required" entries remain.
- **Canaries** — floor 0.10.1; C19 rewritten to pin the 7(b) manual scaffold crop
  (asset_state kind=crop on p14); C55 pins the 15(a) raster manual crop (kind=crop on
  p26); C22 ledger↔corpus consistency re-verified with the 4 flipped verdicts; C14
  recalibrated (byte floor 1000→250 B — the sparse scaffold class compresses small
  legitimately — plus a new explicit 60×40 px dimension floor read from the PNG IHDR,
  the degenerate-sliver guard the byte floor was proxying). 53 hold.

## 0.10.0 — 2026-10-22 · rasterization re-capture: OCR source layer (F41) + early-MS bare-marker linkage (F42)

The last honest REVIEW in the corpus is closed: 2019-06 1C goes G1 PASS 110/110.

- **OCR source layer (F41)** — image-only archive pages can now be recovered without
  inventing content: staged `UPLOAD/ocr/<series>-<paper>/qp-pNN.txt` (prepared page
  texts) + `ocr-pages.json` (sha256-pinned, tool + corrections documented). The
  converter fail-closes on any sha mismatch, splices the text into page_norm for
  page attribution, exempts recovered pages from the G1 image-only attribution, and
  emits `ocr_pages` receipts. Prep committed as `scripts/prep_ocr_layer_2019.py`
  (deterministic + idempotent). 2019-06: Q7 recovered whole, Q1/Q11/Q12/Q13/Q15
  heads recovered; G1 104/110 REVIEW -> 110/110 PASS; every recovered part eyeballed
  against the 600-dpi render; sub-OCR-floor spans (equation subscripts, table
  values) transcribed with MS-text-layer corroboration and canary-pinned (C49-C51).
- **Early-MS bare-marker linkage (F42)** — the 2019-06 MS prints two-level markers
  bare (`d   i`, `   ii`, glued `10ai`/`bi`), leaves 9(b)'s answer cell empty (the
  answer is a drawn diagram), sets `iii` at indent 0 after a page break, and its
  unit fragments (`(g)`) hijacked the marker state. Fixes: marker-column indent
  gate (<=12), three new gated row regexes (ascending-sequence invariant),
  end-of-line bare-letter rows, marks-digit-only rests open marker-only entries,
  repeated MS page-table headers are furniture, and a question-level-roman lookup
  fallback. G5: 32/53 -> 63/64; the residual 3(d)(ii) is honestly unmatched (its MS
  answer cell is a printed image — C52). Damage-repair renumber:
  11(iii)->11(b)(iii), 15(i..iii)->15(b)(i..iii) (spec-labels keys migrated, wave 2).
- **MS page-table headers are furniture (F43)** — the G-E1 export gate's first run
  surfaced a latent v0.6-era defect: 278 served solution blocks (corpus-wide) carried
  the repeated 'Question / Answer Notes Marks / number' header inside solution_md /
  mark_points, because a marker row near a page break swallowed the next page's
  header rows. G5 never caught it (linkage counts were right; only block contents
  were polluted). Fixed by the header furniture rule; C54 pins the law corpus-wide.
  The hub bundle of record carried the same pollution plus 10 mis-linked 2019-06 1C
  solution blocks (wrong answers served since v0.6) — corrected by the wave-12 hub
  re-export under the G-E1 frozen census (F41b).
- **Canaries 45 -> 52** (C4 retired -> C4-archive-damage-repaired; C48-C53 added;
  new checker verbs parts_all_linked / part_answer_status / part_problem_md_contains /
  ocr_pages_receipt). Parity vs v0.9.0: 31/32 slices extraction-identical with
  identical G5 summaries; the 2019-06 1C diffs are exactly the 11 recovered + 4
  renumbered parts. Corpus: 941 parts, 0 pending-llm, 4 terminal no-spec-point.

## 0.9.0 — 2026-10-22 · 2C wave: crop-eyeball fixes (F40), ledger keying (F39), 2C spec-label wave

The 2C backlog opened by the 0.8.0 enablement wave is closed end-to-end.

- **Crop-review ledger keying (F39)** — the converter now loads
  `reviews["<series>:<paper>"]` for non-1C papers (the documented convention that
  C22 and AGENTS.md already enforced; the load site was still reading the bare
  series key, so non-1C verdicts were silently ignored).
- **Nine crop-resolution fixes (F40 a-i)** — every first-pass 2C review item was
  eyeballed against its source page and traced to a generic mechanism: adjacent
  whole-stem fallback restricted to definite references (a); two reference-up
  direction shapes added (b); stem-sentence glyph-glue retried from the noun
  phrase (c); drawn-axis scaffold rescue with zero-width-rect normalisation (d);
  PUA-stripped page anchors (e); sentence-initial noun post-context probes (f);
  '<noun> in your answer' student-provided suppression with a definite-reference
  guard (g); marks-matched sub-numbered MS block fallback + roman case
  normalization (h,i). 1C extraction fields stay byte-identical; 9 adjudicated
  1C improvements (5 previously-unmatched parts now linked, 3 wrong figure
  bindings corrected, 1 stem asset retired) — each eyeballed.
- **2C spec-label wave (first wave)** — 607/607 parts resolved: 584 tagged with
  registry-validated codes (G6: 0 invalid) + 23 terminal no-spec-point parts
  decided against the published 4CH1 spec PDF (F38 evidence standard). 2C
  coverage is terminal like 1C; C33 pins it.
- **Verdicts** — 17 2C verdicts across 10 `<series>:2C` CROP-REVIEW homes
  (16 accepted crops + 1 stub-accepted). 45 canaries (C33-C47 added); floor 0.9.0.

## 0.8.1 — 2026-10-21 · MCQ-key adjudication ledger + terminal no-spec-point state

Both long-standing 1C human-decision items closed with evidence (LEDGER F37/F38):

- **MCQ-KEYS.json (F37)** — the printed Jan 2020 MS itself misplaces the Q7(a)
  answer rows, so the converter's honest refusal (F6) was correct and no parser
  change can recover the keys. The new human-adjudication ledger carries the
  eyeballed keys + corrected verbatim MS rows: 7(a)(ii)=C chlorine (palest
  colour), 7(a)(iii)=A astatine (least reactive), and 7(a)(i)'s block completed
  with the rebuttal the MS prints one row too low. The converter applies the
  override before solution emission, so `solution_md` / `mark_points[]` /
  `choices[].is_correct` all derive from the adjudicated block; the printed
  typo ("C is incorrect as iodine is dark grey") is corrected to D with the
  verbatim text preserved in the ledger. 2020-01 G3 returns to PASS — 1C MCQ
  keys are now 58/58 corpus-wide (2C was already 27/27). Canaries: the C1/C2
  refusal pins retire, replaced by C28-adjudicated-key-ii,
  C29-adjudicated-gate (G3 PASS), C30-adjudicated-key-iii, C31 (ledger↔corpus
  bidirectional).
- **no-spec-point terminal state (F38)** — the 3 pending-llm 1C parts (2019-06
  5(a) airship/hydrogen-density, 2020-01 10(c)(ii) NO-recycle, 2022-01 3(b)(iv)
  safety precaution) were decided against the published 4CH1 spec PDF: no
  numbered point covers them, so they are tagged `no-spec-point` with per-part
  evidence in the series spec-labels files. 1C coverage: 927/930 tagged (1,180
  codes, 0 invalid) + 3 terminal no-spec-point; 0 pending-llm on the labelled
  tranche (2C's 607 parts keep their honest pending-llm until their first
  wave). Canary C32 pins the state bidirectionally (1C-scoped).
- Validation reports now carry `mcq_keys_applied` + `spec_tagging` receipts.
- Parity vs v0.8.0: exactly 6 1C parts touched (3 MCQ parts in 2020-01, 3
  tagging states), every 2C slice byte-identical; negative controls 3/3.

## 0.8.0 — 2026-10-21 · 2C enablement wave (paper parametrization + MS marker discipline + sentence positives)

The operator's GO ruling (ADR-037, trace `1a15ebd93809a525`) scheduled the
remaining 4CH1 variants; this release runs the 2C tranche (16 papers) through
the unchanged gate suite. Three ledger entries land together (none was shipped
interim, so the corpus has exactly one v0.8.0 state):

- **F34 — paper parametrization.** `--paper {1C,2C}` (default 1C);
  `PAPER_TOTALS {1C:110, 2C:70}` + per-paper `EXPECT_QUESTIONS` (2C counts
  footer-verified 16/16 series, Σ=70 every series); paper-suffixed staging
  names with legacy-1C fallback; G0 additionally asserts the staged manifest's
  `paper_number_variant` equals the requested paper (a 2C run over 1CR bytes
  now fails closed); `run_all.sh` loops papers; the report auto-discovers
  `4CH1-*` slices; the canary checker is paper-aware (optional `"paper"` on
  per-series canaries, default 1C; corpus-wide loops cover every variant;
  CROP-REVIEW ledger keys: bare `<series>` for 1C, `<series>:<paper>` for new
  variants); `cross_diff_parsed.py --paper` (the repo parsed/ layer is 1C-only
  today — 2C SKIPs honestly).
- **F35 — MS question-number marker discipline.** Content rows that begin
  with short numerals (the 2022-06 2C Mr working `12   1   16`) previously
  hijacked `cur_q`; the first guard draft then regressed 2022-01 1C (PMT
  blurb `70 countries…` blessed as question one) and 2019-06 1C (damaged
  sequence needs skips). Final rule: numeral + letter/roman marker evidence
  on the row always wins; numeral-only rows must advance the strict sequence
  (bootstrap at 1, then +1 / re-print). 2022-06 2C G5 39/39; 2022-01 1C
  all-PASS restored; 2019-06 1C exactly the shipped 32/53 REVIEW.
- **F36 — sentence-form MCQ positives.** 'The only correct answer is D …'
  (2021-11 2C 1(e)) keys via the extended positive family, still gated by
  the single-distinct-positive rule; 2020-01 7(a)(iii) keeps refusing (C1/C2).

Corpus after the wave (32 slices): 1C 169 Q / 930 parts / 1754/1760 marks,
14/16 all-PASS (unchanged); **2C 110 Q / 607 parts / 1120/1120 marks / 27/27
MCQs keyed, 16/16 all-PASS**. All 607 2C parts are honestly `pending-llm`
(no spec-label wave authored for 2C yet); 22 2C figure items sit in the
review queues awaiting first eyeballs. 27 canaries hold; cross-diff 161/161
(1C). Canaries C25/C26/C27 added; floor 0.8.

## 0.7.1 — 2026-10 · wave-10 stub sweep (crop-review queue emptied) + drawn scaffolds + stem-first tables

The wave-10 sweep eyeballed every remaining review-flagged item against its
source PDF page. The queue the user saw as "17 new flags" was — reconciled
against the shipped corpus (topic.json, validation reports, hub bundle all
agree) — 7 crop-required stubs; v0.7's AGENTS.md had carried a mid-wave count.
Verdicts:

- **Stub verdicts (F32 ledger half)**: 6 of the 7 stubs are text-only dot-and-
  cross scaffolds or blank answer areas (bare element letters 'H C Cl H H' /
  'N N' / 'H O O H', or nothing at all) — nothing croppable exists; the new
  `stub-accepted` verdict records that decision durably and clears the flag on
  every re-run. C22 now enforces the verdict vocabulary both ways: accepted ↔
  kind crop, stub-accepted ↔ kind crop-required.
- **Drawn scaffold un-stubbed (F32 converter half)**: 2024-11 6(c)(i) prints a
  REAL drawn scaffold (an N circle + three overlapping H circles) that rule 0
  stubbed because the part text ends in the element-letter signature. Rule 0
  now checks for a substantial non-furniture vector drawing at/below the
  instruction (`drawn_scaffold_below`); drawn scaffolds crop, text-only
  scaffolds keep the honest stub. The fresh crop is ledger-accepted (C24).
- **Stem-first tables (F33)**: 2024-11 6(a)(i) 'Complete the table' printed
  BELOW the formulae table picked the next part's Mg/Cl electron diagram (the
  real table was never cropped, and 6(b) rode the wrong owner's file). The
  forward branch now resolves the part's OWN group/question stem introduction
  before the below-pick, gated twice: the part text must not itself introduce
  the figure (INTRO_RE — protects 2019-06 3(d)(ii)), and the part's own noun
  anchors must point DOWN (protects 2025-06 1(a)). Corpus effect: 2024-11 6(a)(i)
  = the formulae table (C23), 6(b) = both Mg/Cl atoms under its own id (the F27
  promise, now on the right record), 2023-01 1(a)(i) = the solid/liquid/gas
  three-box row via its stem and 1(b) = the changes-of-state table instead of
  sharing 1(a)(i)'s diagram (both HEAD mis-bindings fixed).
- **Ledger**: 25 verdicts (19 accepted + 6 stub-accepted) across 13 series;
  corpus review flags: 0. Canaries C23/C24 added (24 total). Parity vs v0.7:
  930/930 parts byte-identical on extraction fields; gate matrix unchanged
  (2019-06 G1/G5 REVIEW, 2020-01 G3 honest FAIL).

## 0.7 — 2026-10 · verdict-ledger + spec-tagging waves (24 still-tagged crops reviewed, 927/930 parts spec-tagged, shared-ref dedup)

All 24 v0.6 `human verify` crops were re-eyeballed against their source pages
(14 had been correct, 10 were wrong: wrong-cluster bindings, clipped callout
labels, twin duplicate files). The verdicts exposed six more defect classes
(F25–F30) plus a seed audit (F31); all fixes generic.

- **Resolution order rebuild (F25)**: numbered figures ('table 1') anchor on
  their OWN page before any cross-page search (2022-06 4(b) was dragged to the
  stem apparatus on the previous page); the adjacent-page pass lost its
  2-word fallback anchor ('The student' matched unrelated lines) and its
  single-unclaimed-cluster rule (it grabbed the printed Periodic Table twice —
  2021-01 1(a) and 2025-06 1(b)); own-page rescue for backward references now
  runs BEFORE the adjacent search; a question-scoped plot fallback claims the
  grid printed beside earlier parts that never name it (2022-06 6(c)(i)).
- **Directional nouns inside forward sentences (F26)**: 'from the table' is a
  backward reference even in 'Plot the data values from the table on the grid'
  (2020-01 9(d)(i) now shares the p24 data table instead of duplicating the
  grid); an intro noun preceded by 'in the diagram' ('the syringe in the
  diagram shows…') is a reference, not an introduction (2022-06 4(b)); numbered
  mentions are per-noun, not per-part.
- **Callout labels + paired figures (F27)**: short unpunctuated text blocks at
  the side of a drawing ('sodium thiosulfate solution', 'Magnesium') are
  absorbed even beyond the ±66pt ring (2020-11 7(b) no longer clips its
  labels); same-row drawing pairs merge into one figure (2024-11 6(b) now
  crops BOTH the Mg and Cl atoms; 2024-11 1(b)(i) gets all three boxes); a
  text block the final rect would slice is absorbed whole (F27c).
- **Wrong-class guards (F30)**: plot-class mentions never bind to text-dense
  regions (coverage > 0.30 is a table, never a grid — every verified plot crop
  is ≤ 0.05); the adjacent pass applies the same guard (2022-06 6(b)(iii)
  claimed the question stem's apparatus, now claims the p14 plotting grid).
- **Shared-ref semantics (F28)**: a same-question re-pick now shares the
  owner's crop (`ref_part` set) instead of writing a byte-identical twin PNG
  with `ref_part: null`; stem crops reuse an already-claimed cluster. Corpus:
  135 crop assets (57 shared refs), 7 honest stubs, no orphan files.
- **Verdict ledger (F29)**: `CROP-REVIEW.json` records durable eyeball
  verdicts; an 'accepted' entry clears `review` on every re-run (applied after
  all confidence overrides); C22 pins ledger↔corpus consistency in both
  directions. The 24 flagged crops are now 18 flags → all 18 re-eyeballed and
  ledger-accepted.
- **Spec-tagging waves (labels only, G6-validated)**: `spec-labels/<series>.json`
  files tag 922 parts across 16 series (1,180 codes, 0 invalid against the
  SME spec registry); 927/930 parts carry `spec_point_codes` — the 3 remaining
  `pending-llm` parts have no clean spec point (airship density, recycle
  stream, safety precaution) and stay honestly queued. Demo seeds audited
  (F31): 2020-11 4(c)(ii) 1.25→1.26, 8(c)(ii) 3.9→3.4, 10(b) 1.31→1.33,
  1(b)(i) 1.20→1.24.
- Parity vs v0.6: **930/930 parts byte-identical** on extraction fields
  (marks, problem_md, solution_md, mark_points, source_page); gate matrix
  unchanged (2019-06 G1/G5 REVIEW, 2020-01 G3 honest FAIL). Canaries C22
  added; floor 0.7.

## 0.6 — 2026-10 · crop-review wave (eyeball of 10 flagged + 32 pending, serving semantics)

The 10 review-flagged v0.5 crops and all 32 pending stubs were eyeballed against
their rendered source pages. The verdicts exposed six defect classes (F18–F24)
in how figures are detected, attributed and shared; all fixes are generic
(pattern-named, corpus-wide), never per-series.

- **Furniture filters (F18)**: full-height margin-stripe images no longer bridge
  whole pages into one discardable mega-cluster (2019-06 table pages had ZERO
  clusters); footer-band clusters (barcode / Turn over) are never cropped — the
  13(b)(i)/(ii) footer-barcode crops are gone.
- **Anchor disambiguation (F18b)**: progressive-length page anchors (shortest
  fragment matching exactly one page) fix collided openings — 2019-06 9(b) now
  finds its Halon 1301 displayed formula on p14; 7 anchors shifted, each
  independently verified against the printed page.
- **Mention semantics (F19)**: 'Periodic Table', 'Draw a dot-and-cross diagram',
  'You may use a diagram', 'piece/set up the apparatus' no longer create
  crop-required stubs (9 spurious queue items removed); printed-scaffold cases
  ('N N', 'H C Cl H H') keep theirs.
- **Anaphora resolution (F20/F21)**: backward references resolve BEFORE any
  own-page anchoring — explicit 'in part (x)' back-refs, stem/group-stem figure
  intros (one lazy stem crop shared by every referencing part), sibling crops of
  the same figure class, then adjacent pages. 2021-01 10(a)(iii) now shares the
  stem graph instead of cropping the 10(b) isomers diagram; 13(b)(i)/(ii) share
  13(a)(i)'s grid; 2024-11 7(c)/2(c) share their stem tables.
- **Foreign-text exclusion (F22)**: crops no longer swallow instruction lines,
  mark tags, '(Total for Question…)' rows, dotted answer rules or whole-page
  text blocks.
- **Adjacent-page continuation figures + question-scoped claims (F23/F24)**:
  grids printed on the page after their referencing parts are cropped
  (2025-11 3(c)(i) p9 grid); a cluster claimed by another question is never
  taken, and same-question reuse emits a shared reference.
- **Corpus effect**: 134 crop assets (52 shared references — anaphoric parts no
  longer duplicate PNGs; 143 unique PNG files), 8 honest stubs (dot-and-cross
  prompts with text-only scaffolds; 2022-06 6(b)(iii) whose plotted grid cannot
  be attributed without guessing), 24 review-flagged crops queued for humans.
  Parity vs v0.5: extraction fields byte-identical in all 16 series (7
  verified source_page disambiguations excepted); gate matrix unchanged.
  Canaries C15–C21 added; floor 0.6.

## 0.5 — 2026-10 · render-reveal + Smart Mark wave (solution layer, figure crop pass)

Two additions requested to unlock frontend rendering and structured marking;
both are strictly additive (v0.4→v0.5 parity: extraction fields byte-identical
in all 16 series, every gate state preserved).

- **`solution_md` + `mark_points[]` per part (G7)**: every MS-linked part now
  carries the verbatim mark-scheme answer block (`solution_md`, whitespace-
  normalized, marks-column digits stripped) and awardable `mark_points[]`
  (`{id, marks, text_md}` — ids like `2024-06-3-c-MP2`). Points split ONLY on
  explicit ascending M1..Mn rows in the answer column, each worth 1, accepted
  only when n == part marks; everything else is one whole-block point; MCQ
  parts emit a label-style point referencing the keyed choice. Fail-closed:
  the splitter can only under-split, never invent. New gate **G7-solution-
  emission** proves coverage (895/895 linked parts) and the sum invariant;
  it also censuses the MS marks-column digit vs the QP marks (agreement
  recorded per series; drift cases are layout facts, not extraction errors).
- **Figure crop pass (G4 upgraded, canary C14)**: the 158 page-anchored
  `crop-required` stubs are now resolved against the QP PDF itself — vector-
  drawing + raster-image clusters (page frames, margin decorations and
  full-page scans removed pre-merge; horizontal ruling lines kept as table
  strokes; axis labels absorbed from a +16pt text ring; full-width ruled
  answer strips filtered) rendered to `assets/<asset_id>.png` at 150 dpi.
  126/158 emitted (4.1 MB), 14 as shared figures reused by sibling mentions,
  10 flagged `review` for human eyes; the 32 pending keep their stubs and
  review entries (blank-to-complete diagrams, rasterized 2019-06 pages).
  Deterministic assignment; clusters claimed per page in document order.
- `questions.md` now embeds the crops and renders the mark-scheme answer.
- New canaries **C13-solution-emission** and **C14-figure-crops**; floor 0.5.
- Tooling finding **F17** (LEDGER): PyMuPDF `Rect` has no `__ior__` — the
  crop pass's `hit |= b` silently dropped every intersecting box until the
  union was rebound into the list; caught by page-3 rendering diff, now
  canaried by C14's file-existence check.
- Known limitation recorded: PUA glyphs (`\uf0b4` for ×) in the source text
  layer pass through verbatim in both problem_md and solution_md (pre-v0.5
  characteristic; a PUA→Unicode mapping pass is future work).

Corpus totals: 169 questions · 930 parts · 895/895 linked parts with
solution_md + mark_points (347 atomic M-splits) · 126 figure crops ·
cross-diff 161/161 unchanged · 14/16 canaried non-PASS states preserved
(2020-01 honest refusal, 2019-06 archive damage).

## 0.4 — 2026-10 · clean-checkout verification wave (portability, F15/F16)

The kit was run from a clean checkout of `main` as shipped:
- **Reproducibility proven**: golden-master parity 56/56 output files byte-identical
  (modulo `generated_utc`) vs the committed corpus; all 11 canaries held.
- **F15 (fixed)**: converter/cross-diff/report had hardcoded output roots into a
  machine-specific mirror — regenerated outputs bypassed the canaries' own reads.
  All roots now derive from `Path(__file__)`; outputs are always written inside the
  checkout. Staging dir overridable via `EXAMQ_UPLOAD_DIR`; spec registry reads the
  repo-tree copy (canonical) with staged-copy fallback.
- **F16 (fixed)**: `run_all.sh` now self-bootstraps the series index via one
  contents-API call when `pp-tree.json` is absent (the recursive `git/trees` API
  truncates on large repos and silently omits subtrees — observed live).
- New canary **C12-no-hardcoded-output-root** guards F15; corpus re-run green with
  an empty staging dir (cold start: bootstrap → fetch 32 PDFs → gates → canaries).
- No extraction behaviour changed: identical question/part/mark/key output.

## 0.14.1 — 2026-10-24 · wave-22: enrichment tranche 2 — the corpus completes

The solution-enrichment corpus is COMPLETE: every solution-bearing part of the 54
official sets (1C+2C x16 series, 1CR+2CR x11 R-series) carries an authored,
verifier-clean SME-style worked answer. SOLUTION-ENRICH.json 1,275 -> 2,607 entries;
C71 floor raised to 2607.

- **Tranche 2 authoring (F62)**: 1,332 parts authored (the 1,115 unauthored + the 217
  repair-flagged tranche-1 drafts, re-authored from evidence — the withheld drafts'
  ephemeral staging did not survive the wave-21 session, and the committed harness is
  the stronger gate). Authoring ran in 32 question-grouped slices under the F60
  harness as the per-slice gate; corpus-wide re-verification over the FULL 2,607-entry
  ledger: 0 problems.
- **Tranche-1 repairs (30 latent defects)**: re-running the amended harness over the
  whole ledger surfaced 30 tranche-1 problems that predate the committed verifier's
  current rules (wave-20's 124 entries predate V6/V3 in their committed form; the
  wave-21 run never re-verified its base). Fixed in this wave: 6 MCQ entries gained
  the V6 why-wrong coverage for every non-keyed option (2019-06 1C 1-b-i/1-c/6-a,
  2020-01 1C 7-a-i/ii/iii), 1 process-language leak cleared, 2 mark-point coverage
  gaps closed (3-a/4-a), 2 entries' unshown intermediates re-chained (2020-01 1C 2-b,
  2021-01 2CR 6-c-iii).
- **Harness of record (F-W22-1..5)**: mark-point furniture/artifact strips before
  coverage (MS-table totals, Notes/Marks/Answer headers, the invisible "cler"
  PDF-layer fragment — verified blank on the rendered page); the symbol/label
  coverage routes now search original-cased text (they were dead on arrival —
  case-sensitive patterns against lowercased text, which is why pure-label mark
  points like "U"/"Br"/displayed grids could never pass and concentrated in the
  217 withheld drafts); "Any N from" enumeration headers fall through to the
  post-guidance content; the numeric tokeniser keeps 4+-digit decimals whole
  ("1.7255" no longer splits to "1.725"+"5" — the thousands-group ate ".725" on
  BOTH sides) and reads evidence numbers from an M-label-stripped evidence copy
  ("M2 1275" bridged to "2 127"+"5"); marker jargon ECF/ORA/ALLOW/IGNORE/ACCEPT
  matches uppercase-only (ordinary prose "ignore" is not a leak).
- **MCQ re-key (F37 doctrine, paper-scoped)**: 2020-01 2CR 1(b)(i) — the printed MS
  answer row reads "C number of protons" while the narrative says "The only correct
  answer is B ... proton number" AND "B is not correct ... neutrons" (self-
  contradictory; B's reason is C's content). QP options + chemistry of record: C.
  MCQ-KEYS.json gains the adjudication with a NEW "paper" field; the converter's
  override lookup is paper-scoped (legacy entries stay series-scoped — 7(a)(i)-(iii)
  exist only in 1C) and validation reports record paper-scoped application markers;
  C31 checks both forms. The export verify harness learns the new delta class —
  "choices" joins DISCLOSED_DELTA_CLASSES (the re-key is the first wave ever to
  change a keyed choice; anything outside the disclosed set still refuses).
  2020-01 2CR outputs regenerated through the converter of
  record (all gates PASS, review queue 0; parity: exactly 1(b)(i) changed).
- **Corpus effect**: serving delta = solutionMd on 1,341 parts (1,332 tranche-2 +
  9 tranche-1 repairs) + the 1(b)(i) choices/markPoints re-key, G-E1-matched against
  the filed disclosure (scripts/exporter-disclosures/2026-10-24-wave22-solution-
  enrichment.json); extraction fields byte-identical everywhere else.
- **Canaries**: all 69 hold (C71 min_entries 2607 with the completed-corpus
  assertion; C31 paper-aware both directions).

## 0.14.1 — 2026-10-23 · wave-21 solution enrichment tranche 1 (no converter change)

- CONVERTER UNCHANGED (0.14.0): the wave is ledger + serving only — every topic.json is
  byte-identical; extraction parity trivially preserved.
- SOLUTION-ENRICH.json grew from 124 to 1275 authored-r0 entries: every shipped part
  carries an SME-style worked answer (wave-15 UX doctrine; values never invented).
- NEW script scripts/official_examq_enrich_verify.py — the F60 value-fidelity review
  pass, committed and reproducible: numeric-token census with a chemistry-calibrated
  equation scanner, PUA/process-language exclusion, MCQ key/why-wrong guards,
  marking-point coverage. --base-ledger scopes it to new entries; exit 1 on any problem.
- CANARIES: C71 grew min_entries: 1275 (tranche 2 raises it to 2607). Floor stays 0.14.
- Queued for tranche 2: 1332 parts (resumable driver checkpoints in the wave's
  working tree; REDO+HINTS repair mode ready).

## 0.15.0 — 2026-10-24 · ADR-039 doctrine amendment: verbatim-first → fix-and-disclose (docs wave; converter follows)

**Doctrine of record changes** (ADR-039, `syllabai` repo; operator directive trace `1a16ad28dae2ab99`): the verbatim-first and no-LLM constraints of ADR-037 are superseded. The pipeline improves; provenance discloses. Any tool may correct, clarify or enrich any serving field; every departure from the extracted source layer is machine-disclosed (`edit_status` + `edits[]` + `value_trace`, schema `/0.2`); graded values (marks, mark_points, MCQ keys) corroborate the MS of record or carry explicit correction evidence; G0/G1/G4/G5/G6 and the archive freeze are unchanged.

- **Docs (this commit):** README banner + G2-D/G3 gate rows + negative-control paragraph; AGENTS.md doctrine quote, iron rules 1–3, converter descriptions, PUA note, MCQ-ledger evidence bar, spec-tagging scope, review-queue taxonomy, improvement-loop disclosure step; ledger doctrine strings (MCQ-KEYS, MS-LINK-OVERRIDES, SOLUTION-ENRICH, STEM-RESTORE); CANARIES purpose + C9 re-worded to undisclosed-mutation targets. LEDGER.md history untouched.
- **No converter behaviour change yet** — outputs embed `generator: … v0.14.1` until the code wave lands: G2 → G2-D disclosure checks, N1/N2 re-specified (§5 of the ADR), `edits[]/value_trace` emission, schema bump to `syllabai.official-paper-questions/0.2`, verifier `official_examq_enrich_verify.py` promoted corpus-wide at build time, canary floor raised to 0.15.
- **Transition receipt (pending):** full-corpus re-run re-issues all 54 slices with explicit `/0.2` provenance fields (content byte-identical, provenance blocks added); validation reports regenerate with G2-D receipts; MULTI-SERIES-REPORT refreshes; all canaries hold.
- Two operator adjudication points gate the code wave, not the doctrine: the marking-integrity carve-out (marks/keys: propose freely, apply only with printed-MS or rendered-page evidence) and the regeneration timing (dedicated receipt run vs folded into the next content wave).

## 0.3 — 2026-10 · full-corpus batch wave (16/16 series of 4CH1/1C)

New findings fixed (LEDGER.md F11–F14):
- F11: MS continuation-row indent tolerance `{0,10}` → `{0,20}` (2023-06 G5 76% → 100%).
- F12: MCQ positive-statement keying — '<L> is (the) correct answer' is authoritative;
  note filter extended to 2021+ phrasing 'is not the correct answer'.
- F13: manifest schema-v2 tolerance — 2026-06 gap-fill manifests omit
  `series.printed`/`series.source`; G0 annotates instead of crashing.
- F14: elimination keying for rebuttal-style MS ('A is incorrect…' for every wrong
  option, '<L> (answer)' cells, glued 'B4' cells) — key the sole un-rebutted option
  only when corroborated by exactly one answer row.
- Question-count registry extended to all 16 series (9..12 verified against footers
  summing to 110; 2026-06 genuinely prints 9 questions).

Result: 14/16 series all-gates PASS · 169 questions · 930 parts · 1754/1760 marks ·
all MCQs keyed everywhere except the two honest 2020-01 refusals · negative controls
3/3 everywhere · independent-parse cross-diff 161/161 marks agree (2024-06, 2025-06,
2026-06 vs repo parsed/ layer).

## 0.2 — 2026-10 · multi-series generalization wave (6 series)

Findings F1–F10 (LEDGER.md): QSTART indent tolerance, image-only page census with
defect attribution + G1 REVIEW path, footer-gap census, per-series question-count
registry, MS note-phrasing unification, ambiguity-guard answer keying (2020-01 Q7a),
bare-letter MS rows, phrase-level DO-NOT-WRITE handling, damaged-region start
classification, glued marks-digit stripping.
Result: pipeline proven to generalize beyond the baseline; 2019-06 archive damage
honestly attributed; 2024-06 cross-diff 55/55 marks vs repo parsed layer.

## 0.1 — 2026-10 · prototype (2020-11 baseline)

Converter + gates G0–G6 + negative controls N1–N3; verbatim 5-gram gate; positional
MS linkage; MCQ keying from MS answer text; page-anchored asset stubs; spec seeds
validated against the SME spec-point resolution registry.
Result: 10 questions, 64 parts, 110/110 marks, G0–G6 PASS, 6/6 MCQ keyed, NC 3/3.
