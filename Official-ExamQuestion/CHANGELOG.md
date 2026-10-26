# CHANGELOG — official_examq_extract.py (ADR-037 converter)

## 0.23.0 — 2026-10-27 · Task 19: the deep-audit shape-hygiene wave (F92–F98) — the drawing-linearization class opens and the 2026-06 2C tranche closes

A user-served report ("It has so many issues", `june-2026-4ch1-2c`) drove a corpus-wide deep
audit beyond the furniture universe (battery v3: furniture families + NEW shape families +
consistency re-checks over all 54 slices / 2,607 parts). The audit found the NEXT blind-spot
class: **drawing-linearization** — printed structures/equations whose text layers serve as
atom-run garbage (`H H H H H H A C C C B C C C ...`) with no figure asset — plus four smaller
classes. Task 18's CONTINUES finding had already closed at 0.21.1 (F87); this wave closes the
shape class the furniture battery could never see.

- **F92 — the tick-glyph mojibake sub**: `ticks (ü)` → `ticks (✓)` (the printed tick surfaces
  as Latin-1 ü in the text layer; F48/F033 family). Scoped to the instruction phrase — the
  printed table-cell tick (2025-11 2C 1(a) grid) is question content and stays verbatim.
  Census: 3 instruction instances (2025-06 2C 5(c)(i), 2025-11 2C 1(a), 2026-06 2C 2(d)(i)).
  **The F92 mirror law**: the sub is mirrored into the page-normalized anchoring text (the F70
  BEL-strip pattern) — found live: without the mirror the subbed parts lose their page anchor
  (2025-06 2C 5(c)(i) and 2025-11 2C 1(a) both dropped to source_page None + crop-required
  downgrade in the first run).
- **F93 — the third footer word order**: `Total for question = N marks` (number after the
  equals) joins the F87 pair. Found in the re-run reconciliation (2022-01 1C Q9 tail).
- **F94 — G3 drawing-option MCQ candidates**: parts asking "Which structure/diagram..." with a
  bare A–D run but no `choices[]` are now censused in G3 details + review queue. The v0.22.0
  gate reported "0 MCQ parts" for 2026-06 2C while Q1(b) is one — a vacuous pass, now visible.
- **F95 — G7 mp_answer_gap census**: parts whose EVERY mark_point is a margin-note fragment or
  the marks-digit leak (the MS-answer-is-a-drawing class the sum law cannot see — G7 passed
  2026-06 2C 5(a) while its served MPs were "If M1 and M2 not fully" / "max 1 mark"). Census +
  review queue, never a FAIL (the fragments are verbatim; the missing half is a drawing only an
  MS-side crop can restore — filed follow-up).
- **F96 — G4 drawing-linearization census**: problem_md carrying ≥4 single-letter atom-token
  runs or bond-fragment triples with NO figure asset is censused + queued. The v0.22.0 gate
  counted only table/diagram/grid/apparatus MENTION nouns — the same mention-driven blind spot
  the G8 figure queue inherited, which is why ~15 untracked garbage parts never entered any
  queue.
- **F97 — the bare-answer fallback**: a linked part with marks>0, empty solution_md, and real
  (non-fragment) mark_point text re-emits its OWN verbatim MP text as the solution body,
  disclosed through edits[] (structural-repair). Census: 2021-06 1C 2(b)(ii) '25', 2021-11 2C
  1(d) '73'. Refuses the marks-digit-leak class (2023-06 2CR 7(c)(i): MP "1" == part marks —
  the real answer is a printed drawing; re-emitting would fabricate an answer).
- **F98 — text-repairs table generalized to file-scoped + the chemistry tranche**: the v0.22.0
  lane-gate (`igcse-maths-b-16`) becomes file-scoped (rule keys ARE exact staged filenames —
  cross-lane contamination impossible; maths-B behavior byte-identical by construction). 18 new
  sha1-guarded line rules blank the drawing-linearization remains of 2026-06 2C QP 1(b)/1(c)/
  1(c)(ii)/1(c)(iii) — each line's printed figure is served by an eyeballed crop asset.
- **The 2026-06 2C crop tranche** (user-reported paper): 4 part-level crops via the wave-20
  stemFigure + F45 manual_crop path — `asset_1_b_structures` (the four poly(propene) option
  structures), `asset_1_c_displayed-formula`, `asset_1_c_ii_equation`, `asset_1_c_iii_polyester`;
  rects eyeballed against 150 dpi page renders and re-verified on the rendered PNGs. STEM-
  RESTORE `2026-06/4CH1-2C:Q1` + CROP-REVIEW `2026-06:2C` + FIGURE-QUEUE cropped 25→29.
- **Canaries C96/C97/C98** (93→96): C96 tick-glyph canonical (no `ticks (ü)` in served
  problem_md), C97 bare-answer-solution law (no linked part with marks + real MP text serves an
  empty solution; the MP-gap refusal class is the disclosed exception), C98 the
  drawing-linearization open census PINNED at 15 (the disclosed crop-wave queue; moving the pin
  requires moving the disclosure in the same commit). C94's furniture regex gains the F93 order.
- **Surgical applications (the 0.21.1 pattern, no re-run)**: 2025-06 2C 5(c)(i) ü→✓ and the two
  F97 parts — because a v0.23.0 re-run of THOSE slices would regress unrelated committed state
  (see the reproducibility-debt lesson, AGENTS.md standing rule 5). 2025-11 2C and 2026-06 2C
  re-ran clean (their only deltas are this wave's).
- **Reproducibility debt found and disclosed (NOT fixed here)**: a full v0.22.0 re-run of the
  committed corpus diverges from the corpus of record on 14 slices (all default-paper 1C) —
  lost MCQ positional keys (choices[].is_correct dropped, "Answer B: 3" → raw MS block),
  re-flat-ened exponents where the committed corpus carries superscripts, and MS-grid residue
  classes the 0.21.1 wave deliberately deferred. The corpus of record is NOT re-derivable from
  HEAD inputs on those slices; a reconciliation wave (converter-side) is filed in
  AUDIT-2026-10-27 before any future full re-run ships.
- **Exporter disclosure**: `scripts/exporter-disclosures/2026-10-27-task19-deep-audit.json` —
  9 changed parts: 7 this wave (the 2C tranche + the two ü parts) + 2 CARRIED from wave-26
  (offp_2020-11_1c_9-c-ii, offp_2019-06_2cr_7-c — the wave-26 enrichment exponent
  normalization reached the corpus after the last v2 sync; consumed here). G-E1..G-E4 green;
  census constants unchanged (6,600 marks / 2,607 parts / 54 sets; figure crops 442→446).


## 0.22.0 — 2026-10-26 · T-OEQ-MATHSB-SERVE-1 run-001: the maths-B serve-hygiene wave (F91) — the broken-symbol-font text layers repair

The wave-25 serve card's G-S4 gate caught the maths-B emission carrying 35 C1
controls + 107 U+FFFD (run-003, trace 1a1777580eb2a10d); the operator ruled
option A — the resources-side hygiene wave (trace 1a177a00bc816e05). The root
cause class is wider than the gate caught: broken-symbol-font glyph slots in
the staged pdftotext layers (SymbolMT subsets mapping math glyphs into C0/C1,
broken TimesNewRoman subsets applying a uniform -29 ASCII shift — space->0x03,
'.'->0x11, digits->0x13..0x1c, lowercase->uppercase-29 — with the '=' glyph
becoming an invisible real space), U+FFFD unresolvable-OCR structures (the
2019-06/02 MS's fraction bars / radicals / matrix parens), RTL/bidi wrapper
marks, Cyrillic/Thaana/Latin-1/IPA oddball slots, and U+FFFC object
placeholders. This release:

- Adds `scripts/official_examq_text_repairs.py` + the committed table
  `scripts/official_examq_text_repairs.json` (256 per-line rules over 8
  staging files: the 7 serve-blocker sets' QP/MS layers + the 2019-06/02 QP).
  Every rule was adjudicated eyes-on against 150/300/600dpi page renders of
  the printed papers (evidence pack in the wave receipts, evidence-r2/) and
  the 2019-06/02 MS rules cross-checked against the SME twin's
  UIUX-TIER-B-RUN-004 lineage. Rules carry a sha1 guard per line: a drifted
  staged layer fails the run (fail-closed), never silently re-interprets.
- Applies the repairs at the txt read inside main() — the repaired text IS
  the extraction of record, so G2-D provenance, source_norm and the emission
  move together. Lane-scoped to igcse-maths-b-16; chemistry/physics runs are
  measured no-ops (byte-identity re-proven at this base: 2020-11 1C and
  2023-06 1P regenerate content-identical modulo generated_utc).
- G4 (F90-family hygiene): U+FFFC object placeholders strip corpus-wide
  (11 instances over 6 maths-B staging files; zero in chemistry/physics).
- The 12 affected maths-B sets re-emitted (11 rule sets + 2020-11/01 as the
  untouched-maths canary): every set G0-G7 ALL PASS; the corpus census is
  EXACT at 66 sets / 1281 q / 2443 p / 6600 marks with question/part/marks
  structure and part ids STABLE on all 12 changed sets; the emission diff
  audit shows repair-class changes only (the 2019-06/02 structured per-field
  audit: 40/122 field blocks, every hunk a repaired structure).
- Known residual (disclosed, NOT this wave): the 2023-2026 generation QPs
  carry the same slot class at lower density (~900 txt-layer lines across
  ~25 files: the \x1f inequality/angle/minus slots, i-acute minus, IPA-lambda
  pi) — outside the serve blocker, pre-existing corpus style, filed for a
  follow-up hygiene census.

## 0.21.1 — 2026-10-26 · Task 19: the hygiene-v2 wave (F87) — the CONTINUES-footer class closes; the deep-audit drive-bies land (F88/F89)

A user-served leak (`QUESTION 11 CONTINUES ON BACK PAGE` glued into 2026-06 1CR 11(c)'s problem
text) exposed the class the v0.18.0 battery never enumerated: the QP multi-page footer. Corpus
census: **9 parts / 9 papers in 5 print shapes**, corpus→hub→live end-to-end.

- **FURNITURE_SUBS — the CONTINUES family** (case-insensitive): `QUESTION \d{0,2} CONTINUES ON
  (THE)? (NEXT|BACK) (/ NEXT|BACK)? PAGE.?` — covers the caps, mixed-case, no-number, slash and
  trailing-period shapes — **plus the abbreviated `Total for QN = M` footer** the same sweep
  proved the v0.18.0 battery missed (it matched only the spelled-out "Question" word order).
- **FURNITURE_SUBS — the `\x08` backspace** joins the `\x07` BEL law (F70): one instance corpus-
  wide (2024-06 2C group stem `+\x08–`).
- **restore_flat_exponents (F89)** — the standard-form superscript restore (`× 1023` → `× 10²³`,
  `× 10-23` → `× 10⁻²³`), validity-ruled to keep the legit `× 100` / `× 1000` multipliers and
  refuse out-of-range tails; runs per-line after the furniture subs, **gated to
  `ACTIVE_SPEC_CODE == "4ch1"`** — the physics lane's own pin of record (C74) carries flat
  forms, so its lane decides its own tranche after its own census. Corpus census: 125
  instances across 19 slices + 68 hub strings.
- **Canaries C94/C95** — C94 widens the C77 furniture arm to the QP footer universe and to
  problem_md/stem/group-stem fields; C95 is the new `no_flat_exponent_forms` arm. Battery of
  record: 93 canaries.
- **Serve-side (exporter)** — `_strip_continues` now defends problemMd as well (strip_furniture
  covered only solution/markPoints); redundant second line of defense, never the only one.
- Deliberately NOT changed: the bare MS-grid line strip stays OUT of the converter this wave
  (the MS-table parser may anchor on header lines — queued with that caveat; the corpus of
  record is surgically clean and C94 guards it). Chemistry lanes untouched otherwise: the
  transforms fire only where the classes occur, so byte-identity holds for every unaffected
  string by construction; next full re-run must reproduce the 9+80+1+125 surgical strips
  (disclosure: `scripts/exporter-disclosures/2026-10-26-oeq-hygiene-v2.json`).

## 0.21.0 — 2026-10-26 · Task 18: the QP-side wave (F85) — the 4 QP-side structural G3 fails close; the lane goes 53/53 fully PASS

The Task 17 disclosure named exactly 4 QP-side fails ("open wave #1"). The F85 census
(instrumented re-parse of all 53 landed 4PH1 slices' QP text layers) proved the corpus law
and closed them with two 4PH1-gated parser changes, plus one drive-by repair the battery
assembly caught:

- **parse_mcq_block — the repeat-first-label print-defect completion** (4PH1-gated): 2020-01
  1PR 1(b) prints its 4th option row as `A S` where the run is A/B/C/D-S (Pearson typo; the
  MS of record keys `B – arrow Q` and rebuts `D is incorrect as arrow S`). The row previously
  leaked into problem_md and the run served labels A–C. The completion fires only when the
  final row of a 4-option run repeats the FIRST label at expect==3 (unique completion of the
  canonical A–D run); corpus census: exactly 1 instance. Disclosed on the part via
  `value_trace.choices` (popped from the choice record at the provenance block — it never
  serializes). Canaries C89/C90.
- **finalize_part — the marks-law structural disqualification** (4PH1-gated): the census
  proved every true 4PH1 single-select MCQ prints exactly 1 mark (129/138 option-run parts);
  the marks≥2 exceptions are exactly the structural shapes mis-typed as `multiple_choice` —
  2023-06 2PR 7(a) place-ticks-in-the-table (2 marks), 2022-06 2PR 1(a) draw-matching-lines
  (4), 2026-06 1PR 1(a) name-the-object labelling (4). Serving them as MCQs produced a FALSE
  served key (7(a) keyed `C 500 Hz` from the compound tick rule `C and D ticked…` + a false
  mark_point `Answer C: 500`) and dot-run answer lines served as choice texts (2026-06 1(a)).
  The option-run extraction is refused; the rows serve verbatim in `problem_md`; the part
  types `structured` and links its MS block through the ordinary G5 lane. Canaries
  C91/C92/C93 (new `part_structured` checker arm).
- **the F033 tick repair** (chemistry `pua_override`, the battery's drive-by catch — F86):
  run-004's global SymbolMT digit range clobbered chemistry's F48 tick mapping
  (`F033 → '3'` instead of the evidence-backed ✓). Repaired as a `4ch1` lane override —
  the union's own F068/F06a/F075 lane-split pattern; exactly 1 `F03x` occurrence across 54
  chemistry staging layers.
- **Corpus result (53/53 re-run fresh)**: every slice passes every gate — **53/53 fully
  PASS** for the first time (Task 16: 11; Task 17: 49). G3 MCQ keying 135/135 (the false
  key removed with its part), G5 linkage 2,171/2,171 unchanged, review queue 67 → 65.
  Serving corrections (all disclosed): 2020-01 1PR 1(b) gains its 4th choice (`D S`) keyed
  B; 7(a)'s false key + false mark_point removed; 3 parts re-typed structured with their
  printed rows verbatim. A/B of record: 49/53 slices byte-clean; 4 slices carry exactly the
  designed corrections.
- **Parity receipts**: chemistry 2023-06 1C pre (v0.20.0) vs post (v0.21.0) on identical
  ledger-complete staging: 10/10 files byte-identical (7 assets byte-exact; topic.json /
  validation-report.json / questions.md identical modulo `generated_utc` + generator
  string); gate stdout identical modulo the version string + sandbox path line. The 4MB1
  lane untouched by construction; C87 holds.
- **Battery**: 91 canaries (C89–C93 join); 90/91 hold on the freshly re-emitted chemistry
  (54) + physics (53) corpus with the maths lane fetched (untouched). The 1 exception (C61)
  is a pre-existing staging-era boundary, exonerated by the A/B — LEDGER F86 carries the
  full forensics incl. the dormant `\b\b` row-rebuttal quirk.

## 0.20.0 — 2026-10-26 · run-004: the maths-B line unions onto the spec-lane architecture (SPECS["4mb1"])

The desk-merge conflict check of PR #110 (trace 1a174ec1255522d9) found the maths-B
branch (t-oeq-mathsb-tranche1 @ 139ee931) a converter version-line fork: its own
v0.17.0 (COURSES registry, --course axis, F64-F75 + C72-C74 of the maths line) vs
this line's v0.19.0 (SPECS registry, --spec axis, F64-F72 + C72-C85 of the
chem/phys/hygiene line), with colliding ids on both axes. Operator approved the
reconciliation (trace 1a174f587f822f61). This release IS the union:

- SPECS gains **"4mb1"** — the branch's COURSES payload verbatim (lane
  igcse-maths-b-16, prefix 4MB1, totals 100 x4, the 'is marks?' footer regex, the
  66-set footer-verified expect_questions registry, spec_resolution=False for the
  no-registry G6 posture). The CLI axis migrates --course -> --spec 4mb1.
- The lane-collided codepoints (F068 up-arrow-vs-eta, F06a drop-vs-phi, F075
  drop-vs-brace) move to per-lane `pua_overrides` — both lanes' render evidence
  preserved. The sequence-first pre-pass, the §3.4 control-char census and the
  implicit-single-part laws are lane-scoped to 4mb1; the detached-'2a' furniture
  anchor reads the ACTIVE lane's footer regex.
- Three branch defects fixed and disclosed: the committed F82a ctx corruption
  (lost '[m'), the maths topic header course_id (stuck on the chemistry default),
  and chemistry's allowed_gaps leaking into maths reports.
- The full 66/66 corpus re-emitted under v0.19.0: every set G0-G7 ALL PASS,
  negative controls detected, and every file byte-identical to the branch corpus
  of record modulo the five disclosed classes (timestamps, generator version,
  F-renumber citations, course_id fix, allowed_gaps fix) — zero unexplained
  deltas; assets byte-identical.
- Canaries: C86/C87/C88 (renumbered from the branch's C72/C73/C74) join the
  battery of 86; C87's body adapted to the SPECS registry. The union battery
  holds 86/86 (chemistry 2020-11 1C and physics 2023-06 1P regenerate
  byte-identical modulo generated_utc/generator — the lane-scoping is proven).

## 0.17.0-maths-line — 2026-10-25 · the 8 residual loops close the maths-B drain (66/66)

The tranche-2 tail (8 GATE-FAIL residuals, C88 58/8) closes under the operator's
"8 residual loops" order. Three extraction laws + one OCR tranche:

- **F82a** text-glued QP marks markers (poppler seam-glue class) resolved by the
  question-level footer sum law as a unique exact-cover assignment; marker stripped
  from problem_md and source_norm together; every fill disclosed (edits[] + value_trace).
- **F82b** vector-drawn markers (absent from the text layer entirely) recover from a
  sha-pinned render+MS marks patch; converter verifies crop hashes, MS equality and the
  sum law fail-closed. The topic rebuild keeps explicit marks:null (the KeyError writer
  class is dead).
- **F83** the singular-mark footer ('is 1 mark') — footer_re accepts marks? on both courses.
- **F84** numeral-only MS rows (Working cell wrapped): clean_lines keeps column-0 bare
  numerals in the MS stream; parse_ms honours cur_q+1. G5 2021-06 01 23/33 -> 33/33.
- **F41 tranche**: prep_ocr_layer_2019mb.py transcribes the three rasterized 2019-01
  pages (agent vision @600dpi, tesseract draft, MS-arithmetic cross-check, sha-pinned,
  fail-closed in-converter); Q8/Q9/Q21 (01) and Q17 (01R) recovered whole.

Closing sweep: ALL 66 igcse-maths-b-16 papers G0-G7 ALL PASS under poppler 25.03.0 with
fresh deterministic extraction (scripts/sweep_maths_b_66.py); chemistry A/B byte-identical
at every law landing; all 72 canaries hold with C88 moved to 66/0 per LEDGER F82-F84 +
run-003. EXPECT_QUESTIONS grows the 7 footer-verified entries.


## 0.19.0 — 2026-10-26 · the MS-table parser wave (F72: the vertical marker census closes G5, G3 narrows to 4 structural classes)

The Task 17 corpus census (`physics-intake/ms-forensics/`, all 53 landed 4PH1 slices) proved
the v0.17.4 vertical state machine lost six further marker-row families, and the MCQ keyer
missed three answer shapes. `parse_ms_vertical` (4ph1-only) gains: triple rows
`4 (a)   (i)   A (friction);` (175 rows — the qn+letter rule swallowed the roman into the
entry's content), letter+content rows `(b)   galaxy;   allow named galaxy  [marks]` (842 rows
— the single largest linkage-loss class: the whole row appended to the PREVIOUS entry and the
letter never opened), qn+content rows `8   any six from:   [marks]` (the 2024-06 1P Q8 class;
accepted only under a triple gate — ascending question law AND a trailing marks-column digit
AND indent <=3, because 181 of 198 stripped-shape rows are numeric answer content), an indent
gate (<=3) on letter-only/roman-only rows (notes-column wraps of a bare paren token at indent
65-70 reset `cur_letter` and derailed the next roman gate — 2020-01 2P 3(b)(ii)), a paren-less
letter cell `b)   (i)   (Np/Ns) = ...;` (2019-06 2P, 1 row), continuation re-prints of glued
marker rows now APPEND (setdefault silently dropped them), and an orphan-roman re-anchor
(a marker-column letter+roman row for a fresh letter family can only be a marker — 2026-06 2P
prints Q4(c)(ii) with no preceding `(c)` cell because pdftotext merged it). MCQ keying
(vertical-gated; the row-layout lane's lexicon is hoisted BYTE-EXACT including its dormant
`\b\b` concatenation quirk — chemistry frozen, quirks and all): bare-key rows `B;` (2022-01
1P/2P print five keys this way), the negative lexeme searched after stripping parenthesized
spans (answer rows quote choice text containing 'is not'; rebuttal rows carry their negative
outside any parens — the first battery caught the naive first-paren split regressing 2025-11
1P 9(b) and it was fixed before shipping), 'does not/do not' joins the vertical lexicon, and
F14 gains the pure-elimination arm (MS rebuts every option but one and prints no answer row —
2025-11 2P 2(b)). The wave also CORRECTED a Task 16 mis-link its own pin had codified
(2024-11 1P 1(b)(ii) served the 1(c) block because the old parser never opened the (c) letter
entry; C74's pi pin re-anchored to 1(c), receipted in F72). Corpus of record after the wave:
G5-answer-linkage PASS 53/53 with 2,171/2,171 parts linked (Task 16 baseline: 1,235/2,171,
936 unmatched); G3 PASS 49 / FAIL 4 — the 4 are QP-side structural classes, disclosed not
guessed (2020-01 1PR 1(b) + 2023-06 2PR 7(a): choice-label extraction drops; 2022-06 2PR 1(a)
matching + 2026-06 1PR 1(a) labelling: non-MCQ questions the QP parser types as
multiple_choice); review queue 1,080 -> 67. The last unlinked part (2026-06 2P 4(c)(i)) is an
embedded equation image in the MS PDF — served via MS-LINK-OVERRIDES.json under the F42
doctrine (eyeballed from the 150 dpi render, never model guessed; the ledger's first physics
entry). Version note: this wave worked as 0.18.0 locally but wave-25's concurrent merge owns
that number on main (and ledger IDs F69-F71) — shipped as 0.19.0 / F72. Chemistry
bit-identity receipt: 2023-06 1C pre (main 0.18.0) vs post (0.19.0) on identical staging —
topic.json / validation-report.json / questions.md byte-identical modulo the version string,
7/7 assets byte-identical, gate stdout identical. Canaries C83-C85 pin the wave (triple-glue
MCQ keying, qn-content bootstrap, orphan-roman re-anchor); C57's corpus scan is lane-aware.

## 0.18.0 — 2026-10-26 · wave-25: the audit §4 text-hygiene + repo-hygiene wave

The G8 audit's three OPEN minor classes close at source. Census before ship grew
every one of them.

- **Converter (F69 — MS page-bottom furniture dropped at source)**: the audit's
  "57 footer lines" was the first census pass; the full census measured 362
  furniture lines across 245 corpus text blocks (153 parts, 50 slices) — the
  question-total footer in BOTH printed word orders, the paper-total line, the
  bare 'Total = N' fragment (2025-06 layouts), and the Pearson copyright block +
  its office continuation. `parse_ms` now skips every observed shape before the
  marker-regex battery (case-insensitive, truncation-drift tolerant, nothing
  else); the exporter's serve-time strip (F-W15-2) becomes a redundant second
  line of defense. 50 mark points that served furniture to learners are clean
  (44 footer tails + 3 footer-only blocks). The three footer-only blocks —
  2021-01 2CR 7(d) (printed answer: a drawn displayed formula), 2025-06 2CR
  7(c)(ii) (printed answer 'ethyl ethanoate' in a mis-attributed continuation
  row), 2025-06 1CR 9(d)(ii) (printed answer: two hand-drawn isomer structures)
  — are linked through the F47 MS-LINK-OVERRIDES ledger with eyeballed verbatim
  transcriptions (rendered-page evidence recorded per entry; canaries
  C77/C78/C79). The C71 enrichment gate refused the first of these mid-wave —
  the battery caught the design decision the honest way.
- **Converter (F70 — BEL at source)**: the 15 numbered-method-step strings
  carrying U+0007 (6 question stems + 9 group stems) are stripped in
  `clean_lines` AND the `page_norm` anchor index — removal without space
  insertion (the exact `_bulletize` semantics, served stems byte-identical) so
  part→page anchoring probes stay consistent; the corpus plane keeps no raw
  control bytes.
- **Repo hygiene (F71 — orphan crops pruned)**: the 57 PNGs referenced by no
  topic.json are deleted; a referenced-asset census runs to zero and the full
  battery re-run after the prune resurrects none.
- **Canaries**: 71 → 77 hold. C77 (furniture-free corpus), C78 (BEL-free
  corpus, the C56 extra_chars law), C79 (no orphan assets), C80/C81/C82 (the
  three ledger dispositions pinned linked).
- **Delta census (G-E1)**: serving delta = markPoints on exactly 50 parts
  across 48 slugs, filed as
  `scripts/exporter-disclosures/2026-10-26-wave25-sec4-hygiene.json`;
  problemMd, solutionMd (the authored layer), marks, choices and spec codes
  byte-identical everywhere else. Full 54-slice re-run at v0.18.0; battery
  6/6 PASS (bootstrap / convert-corpus / cross-diff / aggregate-report /
  enrich-verify / canaries), receipt cited from the LEDGER Wave 25 entry.## 0.17.4 — 2026-10-26 · F67: the F48 PUA gate reaches the vertical MS lane (4ph1)

The 4ph1 landing wave's corpus-wide canary (C74, `no_pua_served` with `spec: "4ph1"`)
caught the v0.17.0 vertical MS lane serving mapped PUA chars: `parse_ms_vertical` takes
the RAW layer (`clean_lines` bypassed by design, so `normalize_pua` was skipped with it)
and its three entry-append sites stored the raw line — U+F020 / U+F050 / U+F0B4 /
U+F0B7 / U+F044 / U+F070 / U+F068 leaked into 4ph1 `solution_md` on 16 slices (the
tick/arrow/pi glyph rows that mark keyed MCQ options and allowance notes). Fix: the loop
rebinds `ln = normalize_pua(ln)` — indentation preserved (`build_solution`'s
NOTES_COL_INDENT column logic reads it), all three append sites store clean text. The
gate stays fail-closed: an unmapped codepoint still aborts the run. Chemistry never
calls `parse_ms_vertical` (`ms_layout: "vertical"` is 4ph1-only) — bit-identity by
construction, same argument as v0.17.0. C74 pins the absence law corpus-wide; first
battery of record: 74/74 hold on the landing outputs.

## 0.17.3 — 2026-10-26 · physics PUA tranche (F48 evidence pass, first 4PH1 corpus wave)

> Drift note: this file's top entry was 0.14.0 while `CONVERTER_VERSION` had reached
> 0.17.2 — the spec-lane generalization (v0.16.0) and the v0.17.x parser waves shipped
> without CHANGELOG entries. Backfilling those belongs to their own waves; this entry
> documents only 0.17.3.

Five new evidenced `PUA_MAP` entries for the Edexcel IGCSE Physics (4PH1) corpus,
each from a PDF font trace (PyMuPDF rawdict) + page render, eyeballed
(census/evidence artifacts of the intake wave; trace 1a17463dfb7c99c9):

- `U+F020` → U+0020 — CIDFont+F12/F9 blank glyph: span `\uf050\uf020` (2021-11 1P MS p4)
  prints ONE tick + gap; `\uf0b4\uf0203.125` (p13) prints "× 3.125" — the CID font's space.
- `U+F068` → U+2191 (↑) — Wingdings3; 2021-06 1P MS p13 renders "clear e.g. allow +, ↑ for increase".
- `U+F06A` → "" — TransportMT train pictogram (2020-06 1P QP p6, size 64), decorative
  silhouette; the word "train" is in the stem text; drop like the cover ornaments.
- `U+F070` → U+03C0 (π) — CIDFont+F7 2022-01 1P MS p11 "(2 × π × 7100) / 5800" and
  SymbolMT 2023-06 1PR MS p5 "v = 2πr/T"; renders eyeballed in both.
- `U+F075` → "" — TransportMT aeroplane pictogram (2020-06 2P QP p14), decorative; drop like F06A.

No-op receipt: chemistry 2023-06 1C re-run pre (pure 0.17.2) vs post (0.17.3) on
identical staging — topic.json / validation-report.json / questions.md / gate stdout
all byte-identical modulo `generated_utc` + `generator` version string.

Physics corpus effect: 7 slices (2020-06 1P/2P, 2020-11 1P, 2021-06 1P, 2021-11 1P,
2022-01 1P, 2023-06 1PR) previously failed closed at MS parse on these glyphs; with the
tranche the full 4PH1 wave (53 of 58 paper dirs; 3 archive-gap slices dispositioned,
1 image-only scan crash receipted, 1 archive mislabel row) converts end-to-end.

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


## 0.17.4 — 2026-10-26 · F67: the F48 PUA gate reaches the vertical MS lane (4ph1)

The 4ph1 landing wave's corpus-wide canary (C74, `no_pua_served` with `spec: "4ph1"`)
caught the v0.17.0 vertical MS lane serving mapped PUA chars: `parse_ms_vertical` takes
the RAW layer (`clean_lines` bypassed by design, so `normalize_pua` was skipped with it)
and its three entry-append sites stored the raw line — U+F020 / U+F050 / U+F0B4 /
U+F0B7 / U+F044 / U+F070 / U+F068 leaked into 4ph1 `solution_md` on 16 slices (the
tick/arrow/pi glyph rows that mark keyed MCQ options and allowance notes). Fix: the loop
rebinds `ln = normalize_pua(ln)` — indentation preserved (`build_solution`'s
NOTES_COL_INDENT column logic reads it), all three append sites store clean text. The
gate stays fail-closed: an unmapped codepoint still aborts the run. Chemistry never
calls `parse_ms_vertical` (`ms_layout: "vertical"` is 4ph1-only) — bit-identity by
construction, same argument as v0.17.0. C74 pins the absence law corpus-wide; first
battery of record: 74/74 hold on the landing outputs.

## 0.17.3 — 2026-10-26 · physics PUA tranche (F48 evidence pass, first 4PH1 corpus wave)

> Drift note: this file's top entry was 0.14.0 while `CONVERTER_VERSION` had reached
> 0.17.2 — the spec-lane generalization (v0.16.0) and the v0.17.x parser waves shipped
> without CHANGELOG entries. Backfilling those belongs to their own waves; this entry
> documents only 0.17.3.

Five new evidenced `PUA_MAP` entries for the Edexcel IGCSE Physics (4PH1) corpus,
each from a PDF font trace (PyMuPDF rawdict) + page render, eyeballed
(census/evidence artifacts of the intake wave; trace 1a17463dfb7c99c9):

- `U+F020` → U+0020 — CIDFont+F12/F9 blank glyph: span `\uf050\uf020` (2021-11 1P MS p4)
  prints ONE tick + gap; `\uf0b4\uf0203.125` (p13) prints "× 3.125" — the CID font's space.
- `U+F068` → U+2191 (↑) — Wingdings3; 2021-06 1P MS p13 renders "clear e.g. allow +, ↑ for increase".
- `U+F06A` → "" — TransportMT train pictogram (2020-06 1P QP p6, size 64), decorative
  silhouette; the word "train" is in the stem text; drop like the cover ornaments.
- `U+F070` → U+03C0 (π) — CIDFont+F7 2022-01 1P MS p11 "(2 × π × 7100) / 5800" and
  SymbolMT 2023-06 1PR MS p5 "v = 2πr/T"; renders eyeballed in both.
- `U+F075` → "" — TransportMT aeroplane pictogram (2020-06 2P QP p14), decorative; drop like F06A.

No-op receipt: chemistry 2023-06 1C re-run pre (pure 0.17.2) vs post (0.17.3) on
identical staging — topic.json / validation-report.json / questions.md / gate stdout
all byte-identical modulo `generated_utc` + `generator` version string.

Physics corpus effect: 7 slices (2020-06 1P/2P, 2020-11 1P, 2021-06 1P, 2021-11 1P,
2022-01 1P, 2023-06 1PR) previously failed closed at MS parse on these glyphs; with the
tranche the full 4PH1 wave (53 of 58 paper dirs; 3 archive-gap slices dispositioned,
1 image-only scan crash receipted, 1 archive mislabel row) converts end-to-end.

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


## 0.17.0 — 2026-10-25 · wave-24: the first G8 audit closes (crops + the ambiguous MCQ)

The first post-completion audit (G8 — the new mandatory gate, igcse-chemistry-19,
2026-10-25, report: `AUDIT-2026-10-25-igcse-chemistry-19.md`) confirmed three
QP-verified missing figures, a 36-part figure-language review queue, and one
ambiguous MCQ. Wave-24 closes all three classes at source.

- **Converter (F64 — choice script restoration, v0.17.0)**: MCQ option text re-derived from
  the PDF span geometry — a small raised span is a superscript, a small lowered span
  a subscript, a floating charge span ("+" / "−") is picked up geometrically even at
  full size; visual rows are grouped around the option label anchors by baseline
  proximity (raised/lowered script spans often land in their OWN dict line, so dict
  lines under-group — the same-label-rows-on-one-page hazard dies with the
  label+flatten-match row selection). Fail-closed by construction: a rebuild only
  lands when it normalizes back to the extracted text (scripts stripped, dashes
  normalized, whitespace dropped); no candidate, no rebuild — a geometry mis-read can
  never ship, and a script-free rebuild (pure spacing artefacts) keeps the extracted
  text verbatim. Formula-length scope guard (≤32 chars — options only, never prose).
  55 choice strings restored across 14 parts corpus-wide (molecular subscripts, ionic
  charges; the 2026-06 1C 1(a) A NH⁴⁺ vs D NH₄⁺ duplicate-choice ambiguity is the
  pinned case — canary C72).
- **Figures (F65 — the 36-part queue closes)**: 26 new crops via the F57/F45
  stemFigure+manual_crop ledger path (the 3 confirmed G8 figures — 2019-06 1C Q11(b)
  apparatus, Q12 calorimeter, 2025-06 1C 9(a) chloroethene stub upgraded — plus 23
  queue figures across 20 papers); every rect derived from document geometry (vector
  band unions / raster ink profiling) and eyeballed against the printed page. The
  queue disposition of record is `FIGURE-QUEUE.json` (25 cropped + 10 served_via +
  12 dismissed with QP-page evidence — draw/recall tasks, printed equations); canary
  C73 keeps it bidirectionally consistent with the corpus.
- **G8 rule institutionalized**: AGENTS.md gains the post-completion-audit gate
  (checklist + gate-catalog row + the executed first-audit baseline). Re-run G8
  whenever a course re-exports.
- **Delta census (G-E1)**: serving delta = 40 parts / 29 slugs (26 {assets,
  problemMd} figure embeds + 14 {choices} restorations), filed as
  `scripts/exporter-disclosures/2026-10-25-wave24-g8-fixes.json`; marks, solutions,
  mark points and spec codes byte-identical everywhere else. Full 54-slice re-run;
  canaries C1–C71 green (C72/C73 added). NOTE: v0.16.0 was claimed mid-flight by the parallel spec-lane generalization (#128, chemistry bit-identical, landed first); this wave rebased F64 onto the spec-lane converter and re-ran the full 54-slice corpus under v0.17.0 — output identical to the pre-rebase run modulo the converter header (54/54).

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
- **Converter v0.15.0 (code wave, adjudications resolved):** G2 → G2-D disclosure checks (extracted parts keep the ≥0.95 5-gram assertion as a provenance-correctness check; corrected/enriched parts require complete `edits[]`; `value_trace` ↔ `edits[]` coherence enforced), N1 re-targeted at the value_trace violation and N2 at the missing `edits[]` entry (N3 unchanged), `edit_status` + `value_trace` emitted on every part, schema bump to `syllabai.official-paper-questions/0.2`, verifier `official_examq_enrich_verify.py` promoted corpus-wide in `run_all.sh` (all 1,275 SOLUTION-ENRICH entries in scope at build time), canary floor raised to 0.15. Adjudications of record (ADR-039 §7, both resolved): marking-integrity carve-out CONFIRMED (trace `1a16cdc9eda1a645`); regeneration timing = dedicated receipt run (trace `1a16ce03e8a9fe35`).
- **Transition receipt (this wave):** full-corpus re-run re-issues all 54 slices with explicit `/0.2` provenance fields (content byte-identical, provenance blocks added — the transition diff must be pure provenance additions, any content delta is a defect to be ledgered, never folded in); validation reports regenerate with G2-D receipts; MULTI-SERIES-REPORT refreshes; all canaries hold.

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
