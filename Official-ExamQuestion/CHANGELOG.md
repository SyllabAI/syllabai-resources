# CHANGELOG — official_examq_extract.py (ADR-037 converter)

Semantics: outputs embed `generator: official_examq_extract.py v<version>`, so any
topic.json traces to exactly this behaviour. Every version bump must follow the
AGENTS.md improvement loop: ledger entry (F#) + canary + full-corpus re-run.

## 0.11.0 — 2026-10-22 · PUA→Unicode mapping pass (F46) + wide-marker linkage (F47) + ANSWER-LINKS ledger (F48) + canonical probe matching (F49)

The two remaining human-decision items are closed: the source text layer is PUA-free
and the last 3 honest answer-linkage refusals are resolved.

- **PUA→Unicode mapping pass (F46)** — the converter-level mapping table AGENTS.md
  mandated (never ad hoc): 18 observed PUA codepoints map at the single text-ingestion
  choke point (`clean_lines`, covering QP + MS layers so problem_md, source_norm,
  solution_md, mark_points and stems stay consistent for G2). Every mapping is
  evidence-checked (get_texttrace font+glyph traces and region renders, wave 14):
  \uf0b4→×, \uf0b8→÷, \uf02d→− (ionic/superscript minus), \uf0e0/\uf0ae/\uf022→→,
  \uf083→⇌, \uf0b0→°, \uf0e5→Σ, \uf044/\uf072→Δ, \uf0b7/\uf09f/\uf097→•, \uf0fc→✓,
  \uf8e7→─ (horizontal bond stroke, SymbolMT displayed formulas), \uf0ad→↑ (Energy-axis
  arrowhead), \uf0a2→"" (Wingdings2 dotted answer-space separator — layout furniture,
  stripped). Parity run: 410 string diffs corpus-wide, EVERY one byte-exactly
  `de_pua(old)` modulo whitespace (scripts/parity_wave14_v2.py); zero unexplained chars.
- **Wide-marker MS rows (F47)** — MS_ROW_RE indent cap 20→30: the 2023-11 6(c)/(d)
  tables print inline `(ii) <answer>` rows at indent 22, so both parts fell to the
  previous entry's content (6(c)(ii)/6(d)(ii) unlinkable; 6(c)(i)/6(d)(i) carrying the
  (ii) blocks as verbatim pollution). Marker-ONLY rows stay gated at ≤12 (F42's hijack
  guard untouched); the wave parity pins the blast radius to exactly the 2023-11 Q6
  parts. G5 for 2023-11 1C: 64/66 → 66/66 (100%).
- **ANSWER-LINKS.json ledger (F48)** — human-adjudicated answer linkages for parts
  whose MS answer exists only as a printed IMAGE (the honest-refusal residue; C52's
  2019-06 3(d)(ii) terminal state). The ledger carries the rendered-MS-page evidence,
  the exact answer-image rect, and the transcription; the converter renders the crop
  deterministically at 150 dpi (`assets/asset_3_d_ii_ms_answer.png`, eyeballed: ticks
  on 'high melting point' and 'unreactive'), links the part fail-closed (must still be
  unmatched, mark_points must sum to part marks, rect well-formed, else abort), and
  marks it `answer_key_source: "answer-links-ledger"` + `manual_linkage: true` +
  `solution_source` disclosure. G5 for 2019-06 1C: 63/64 → 64/64 (100%, 1
  ledger-adjudicated). The corpus review queue now holds ZERO answer-linkage items.
- **Canonical probe matching (F49)** — F46 turned probes into real-Unicode needles
  ('Give the meaning of the symbol ⇌') while PyMuPDF's page layer still carried
  \uf083, silently un-anchoring 2020-01 1C 10(a)(ii) and 2023-01 1C 12(c)(i);
  page_norm now passes through the same PUA map (one canonical form on both sides).
  The fix also GAINED anchors for 4 parts whose glyph-carrying probes could never
  match the PUA-bearing page layer (2021-06 2C 7(c)(i), 2022-06 2C 5(c)(ii),
  2025-06 2C 6(a)(ii), 2026-06 1C 7(a)(ii)) — a pre-existing silent failure surfaced
  by the parity discipline.
- **Canaries** — floor 0.11.0; 53 → 62: C52 rewritten (3(d)(ii) ledger-linked, was the
  honest-unmatched pin); C56/C57 (2023-11 Q6 solutions), C58/C59 (✓/÷ mappings),
  C60 (no PUA anywhere, corpus-wide scan), C61 (ANSWER-LINKS ↔ corpus bidirectional),
  C62/C63 (restored anchors), C64 (gained anchors). All 62 hold.
- **Corpus effect** — 32 slices regenerated at v0.11.0, all gates PASS, 32/32
  full-pass, cross-diff 161/161 unchanged, review queue EMPTY corpus-wide.

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
