# LEDGER — Official-ExamQuestion improvement ledger

> Append-only. One entry per distinct cross-series pattern, in discovery order.
> Each finding is: diagnosed at raw-text level → fixed generically → guarded by a
> canary in `CANARIES.json` → whole-corpus re-run. New agents: read this before
> changing any regex; every entry is a scar someone already earned.

| id | date | series | finding (what defeated the parser/gate) | fix | canary |
|----|------|--------|------------------------------------------|-----|--------|
| F1 | 2026-10 (multi-series wave) | 2019-06 | question start lines are indented; QSTART assumed column 0 | QSTART_RE allows leading whitespace | corpus: 2019-06 questions segmented |
| F2 | 2026-10 (multi-series wave) | 2019-06 | 8 rasterized (image-only) pages in the archive PDF; 6 content pages lost — Q7 gone entirely, Q1/Q11/Q12/Q15 partial | image-only page census + defect attribution + G1 REVIEW path; nothing invented to fill gaps | 2019-06: G1=REVIEW, marks=104/110, Q7 attributed |
| F3 | 2026-10 (multi-series wave) | 2019-06 | Q7's footer absent from the PDF text layer (rasterized with the page) | footer census detects the gap; review item names the lost pages | same as F2 |
| F4 | 2026-10 (multi-series wave) | 2019-06 | early 4CH1 format prints 15 questions, not 10 | per-series question-count registry `EXPECT_QUESTIONS`; paper invariant stays 110 marks | registry now covers all 16 series |
| F5 | 2026-10 (multi-series wave) | 2020-11 vs 2020-01 | MS note phrasing differs: 'is not correct' vs 'is incorrect' | unified note filter covering both | 2020-01 canary (below) |
| F6 | 2026-10 (multi-series wave) | 2020-01 | MS marker column drifts one row early in Q7(a); note rows leak into adjacent entries; naive keying emits C for 7(a)(iii) where printed notes prove A | key only when exactly ONE distinct candidate; ambiguous → human review | **2020-01 7(a)(iii) must stay unkeyed; G3=FAIL is the correct state** |
| F7 | 2026-10 (multi-series wave) | 2019-06 | MS sub-letters printed bare without parentheses ('b   they have...') | MS_BARE_LETTER_RE with branch precedence over the catch-all row regex | 2019-06 G5 REVIEW unchanged (damage-linked) |
| F8 | 2026-10 (multi-series wave) | 2019-06/2020-01 | three 'DO NOT WRITE IN THIS AREA' phrases share one extracted line | phrase-level substitution instead of whole-line filter | corpus-wide G2 verbatim |
| F9 | 2026-10 (multi-series wave) | 2019-06 | damaged Q1 region begins with a part marker '(c) ...' as line 0 | segment_question classifies line 0 instead of forcing it into the stem | 2019-06 Q1 partial-loss attribution |
| F10 | 2026-10 (multi-series wave) | 2020-01 | marker-only MS row carries a trailing marks digit ('(iii)   1') gluing to the answer | strip leading marks digit only when followed by a choice letter | 2020-01 G3 refusal intact |
| F11 | 2026-10 (batch wave) | 2023-06 | MS continuation rows indented 11+ spaces; marker-row regex allowed `^ {0,10}` — every roman part after the first became unlinkable (G5 76%, 13 unmatched) | indent allowance widened to `^ {0,20}` in MS_ROW_RE / MS_BARE_LETTER_RE | 2023-06: G5=PASS, 55/55 linkage |
| F12 | 2026-10 (batch wave) | 2021-01 + 2021+ style | MCQ keys phrased '<L> is the correct answer because…' with rebuttals '<L> is not THE correct answer because…' — the inserted 'the' defeated the note filter; all four letters became candidates; guard refused every key (G3 FAIL on 6 series) | positive-statement keying ('<L> is (the) correct' is authoritative) + note filter extended to 'is not the correct' | 2020-11 6/6 keyed (its affirmative 'D Group 0 is correct…' rows must not be mistaken for notes) |
| F13 | 2026-10 (batch wave) | 2026-06 | manifest schema drift in gap-fill-wave manifests: `series.printed`, `series.source`, `variant.official_code` absent → converter crashed in G0 instead of flagging | manifest reads use `.get()` with explicit 'absent in manifest schema v2' annotation in the G0 receipt | 2026-06: G0=PASS with schema-v2 annotation |
| F14 | 2026-10 (batch wave) | 2023-06/2025-06/2025-11/2026-06 | rebuttal-style MCQ MS: explicit rebuttal for every wrong option ('A is incorrect…', 'B the charges are incorrect', 'B is X incorrect' [sic], '<L> (answer)' cells, glued 'B4' answer+digit cells) — single-candidate logic insufficient | elimination keying: the sole un-rebutted option is keyed only when corroborated by exactly one answer row; anything else stays unkeyed | 2023-06 9(a)(i)=B; 2025-06 4(a)(ii)=B, 6(b)=A; 2025-11 3(a)(ii)=A; 2026-06 1(a)=D, 1(b)=B |
| F15 | 2026-10 (verification wave) | all (tooling) | clean-checkout run of `run_all.sh`: converter/cross-diff/report wrote to hardcoded `/home/z/my-project/download/...` mirror instead of the checkout — canaries then verified the *committed* copies, not the regenerated ones (silent no-op on the original machine; crash on any other). Golden-master parity was perfect (56 files byte-identical mod `generated_utc`), proving the corpus is reproducible even though the plumbing was not portable | all output roots derived from `Path(__file__)`; staging via `EXAMQ_UPLOAD_DIR` env override; spec registry read from the repo tree (canonical) with staged-copy fallback; `CONVERTER_VERSION` 0.4 | C12-no-hardcoded-output-root |
| F16 | 2026-10 (verification wave) | all (tooling) | `run_all.sh` hard-required `upload/pp-tree.json` (never documented how to obtain it — cold start impossible). Related hazard found while building the clean checkout: the recursive `git/trees` API TRUNCATES on this repo (~39k entries, `truncated: true`) and silently omitted the whole `scripts/` subtree | `run_all.sh` self-bootstraps the series index via one contents-API call on the 4CH1 series dir when `pp-tree.json` is absent; contents API is truncation-proof | operational: cold-start run with an empty staging dir must go green end-to-end |
| F17 | 2026-10 (reveal+crop wave) | all (tooling) | PyMuPDF `Rect` defines `__or__` but NOT `__ior__`: the crop pass's `hit \|= b` re-bound a new local object and the union never landed in the cluster list — every intersecting seed was silently DROPPED, so tables/graphs fragmented into sub-minimum slivers and whole pages yielded zero clusters | union re-bound into the list explicitly (`merged[i] = merged[i] \| b`); caught by rendering page 3 of 2024-06 (the Q1(a) table produced no crop) | C14-figure-crops (crop count floor + file existence) |

| F18 | 2026-10 (eyeball wave) | 2019-06 (+ all PMT-striped archives) | two independent cluster-detection defects: (a) full-height margin-stripe IMAGES (x1=57 — past the 45pt margin rule) acted as merge bridges chaining border rules + answer rules + tables into one page-sized mega-cluster, which the 0.80 full-page filter then discarded — table pages produced ZERO clusters (2019-06 p7 Property table, p14 Halon 1301 formula); (b) footer-barcode clusters (y0 ≥ ph−80) were croppable, so 13(b)(i)/(ii) 'on the grid in part (a)' anchored the page FOOTER | (a) furniture rule: images with h ≥ 0.5·ph and w ≤ 60 are margin stripes; (b) post-merge footer-band filter y0 ≥ ph−80 | C21 (3(d)(ii) Property table crop), C15 |
| F18b | 2026-10 (eyeball wave) | 2019-06/2021-06/2022-01/2023-01/2025-11/2026-06 | 38-char page-anchor fragments COLLIDE across questions with identical opening wording ('The diagram shows the displayed formula…' opens both Q8(c) and Q9(b)) — Q9(b) anchored to p13 while its figure prints on p14; 6 more parts carried drifted anchors | progressive-length anchoring: the shortest fragment (38/60/90/110) matching EXACTLY ONE page wins; short problem_md no longer skipped | parity shifts (7 verified): 2019-06 9(b) 13→14, 2021-06 8(b)(ii) 14→19, 2022-01 9(b) 21→23, 2023-01 3(b)(iii) 5→7, 2025-11 9(a) 21→22, 2026-06 9(a)(ii) 21→24, 2021-01 11(b)(iv) 35→36 |
| F19 | 2026-10 (eyeball wave) | 2020-11/2023-11/2024-11/2025-11/2026-06 | figure-mention keyword matched NON-figural phrases: 'Periodic Table', 'Draw a dot-and-cross diagram', 'Sketch a labelled diagram', 'You may use a diagram', 'piece of apparatus', 'set up the apparatus' — 9 spurious crop-required stubs entered the review queue | figure_mentions() suppresses a noun only when EVERY occurrence sits in a non-figural phrase; scaffold exception: 'Draw a dot-and-cross diagram' followed by printed element tokens ('H C Cl H H', 'N N') keeps its stub; G4 dangling check uses the same semantics | C16 (2020-11 5(a) has no assets) |
| F20 | 2026-10 (eyeball wave) | 2021-01 + corpus-wide | backward figure references ('Use the graph to…', 'Explain the trend shown by the graph.') re-anchored with nearest-below on the part's OWN page — 10(a)(iii) cropped the 10(b) isomers diagram; 13(b)(i)/(ii) 'on the grid in part (a)' cropped the page footer | resolution order: explicit 'in part (x)' back-ref → stem/group-stem figure (F21) → sibling crop of the same figure class → adjacent page (F23) → own-page rescue (review-flagged) → honest stub; directional noun anchors (instructions point DOWN, 'on/from/in the X' references point UP) | C15 (13(b)(i) shared→13(a)(i)), C18 (10(a)(iii) shared→stem graph, not the isomers) |
| F21 | 2026-10 (eyeball wave) | 2024-11/2022-01/2021-01/2020-11 + corpus-wide | figures introduced by QUESTION/GROUP STEMS ('The table gives the student's results.', 'A student uses this apparatus…', 'The graph shows…') were never cropped — the pass only anchored from part text, so every referencing part stubbed (2024-11 7(c), 2(c); 2022-01 9(c)(iii)/(iv); 2021-01 11(b)(iii)) | lazy per-(question, group, noun) stem-figure crops: intro sentence → its page → nearest cluster below → one stem asset shared by all referencing parts; stem sentences may glue into sibling parts' problem_md (scanned too) | C17 (7(c) shares asset_7_c_table_stem) |
| F22 | 2026-10 (eyeball wave) | 2025-06/2025-11/2026-06/2019-06 | crop rectangles absorbed neighbouring TEXT: (a) the +16pt label ring swallowed instruction lines ('ake sure that the two lines cross.'), mark tags '(2)', the part's own question line, and — on 2025-06/2019-06 — WHOLE-PAGE text blocks that PyMuPDF returns as one giant block; (b) '(Total for Question 3 = 6 marks)' rode in with the dotted answer-line block | foreign-text exclusion: blocks outside the pre-expansion rect that match part-marker / mark-tag / total-for-question / dot-run patterns or contain the part's own text are never absorbed; blocks must also sit within the ring inflated by 66pt (kills whole-page blocks) | eyeball re-pass on all flagged crops |
| F23 | 2026-10 (eyeball wave) | 2025-11/2022-01/2021-01 | figures printed on the page ADJACENT to the referencing part (grid on p9 for parts on p8; gas-tube diagram on p8 referenced from p9) produced stubs — own-page-only anchoring cannot see across the page break | adjacent-page pass: stem/class-noun sentence anchored on pg±1; a page with exactly ONE unclaimed figure is taken (review-flagged), multi-figure pages are never guessed; question-scoped claims (F24) prevent cross-question theft | C20 (2025-11 3(c)(i) crops the p9 grid) |
| F24 | 2026-10 (eyeball wave) | 2021-01/2025-06 (tooling) | cluster claims were per-PAGE sets: a part of question N could claim (and mis-crop) a figure belonging to question N+1 sharing the page, starving the real owner | claims keyed (page, cluster) → question number; same-question reuse = shared reference (review-flagged), cross-question claims invisible; directional noun anchors stop 'The box gives… Complete the table' parts picking the box instead of the table | eyeball: 2021-01 1(a)/5(a)/6(a), 2024-11 1(a) tables resolve to their own tables |

| F25 | 2026-10 (Task 9 wave) | 2022-06/2021-01/2025-06/2023-06/2022-06 | adjacent-page pass too permissive: (a) 2-word fallback anchors matched unrelated lines ('The student' on p14 for a stem printed on p15) — 2022-06 6(c)(i) 'grid' cropped the p14 results TABLE; (b) the single-unclaimed-cluster rule grabbed reference pages — the printed Periodic Table was cropped for 2021-01 1(a) AND 2025-06 1(b); (c) numbered figures ('table 1') went cross-page before trying their own page — 2022-06 4(b) 'table 1' cropped the p8 stem apparatus | resolution order rebuild: numbered mentions anchor own-page first (per NOUN, not per part); own-page rescue (both noun directions) runs before adjacent; adjacent requires a >= 4-word prefix hit and is plot-class-guarded; single-cluster fallback removed; question-scoped plot fallback (exactly one low-cov unclaimed cluster within p±1) claims grids printed beside parts that never name them | C20 updated (2025-11 3(c)(i) still crops the p9 grid via the >=4-word stem anchor), plus eyeball: 2022-06 4(b)/6(b)(iii)/6(c)(i), 2021-01 1(a), 2025-06 1(b), 2023-06 10(a)(ii) |
| F26 | 2026-10 (Task 9 wave) | 2020-01/2022-06 | directional heuristics blind inside forward sentences: 'Plot the data values FROM the table on the grid' anchored the table mention at the grid below (9(d)(i) emitted a duplicate of the grid as its 'table' asset); 'The syringe IN the diagram shows…' was classed as a fresh introduction and anchored at Table 1 below (4(b)) | (a) a noun whose head ends 'from the/this/…' points UP even inside a forward sentence; (b) INTRO_RE matches are context-guarded: an intro noun preceded by a possessive preposition ('in the diagram shows') is a REFERENCE; (c) the part-start below-anchor is only used when the noun phrase itself gives no evidence (never overrides a directional noun anchor) | eyeball: 2020-01 9(d)(i) table = shared ref to asset_9_d_table_stem (p24), 2022-06 4(b) diagram = shared ref to the p8 stem apparatus |
| F27 | 2026-10 (Task 9 wave) | 2020-11/2024-11 | (a) callout labels extending >66pt from a drawing ('sodium thiosulfate solution', 'paper with cross drawn on it') were rejected by the contain ring — the 7(b) apparatus crop clipped both labels mid-word; (b) paired figures (Mg + Cl atom dot-diagrams, solid/liquid/gas boxes row) stayed separate clusters, so the mention cropped only the nearer half (2024-11 6(b) cropped the chlorine atom only); (c) the crop rect sliced through the stem caption line, rendering clipped text | (a) callout side-pass: short (<=34pt tall), unpunctuated, <=8-word blocks vertically inside the figure span are absorbed up to 130pt away; (b) same-row merge: y-overlap >= 60%, x-gap <= 90pt, combined width <= 0.85 page → one cluster; (c) never slice a text block: a short block >= 40% inside the final rect is absorbed whole | eyeball: 2020-11 7(b) apparatus complete with all labels; 2024-11 6(b) shows BOTH atoms; 2024-11 1(b)(i) shows all three boxes |
| F28 | 2026-10 (Task 9 wave) | 2020-01/2020-11/2021-01/2021-11 | same-question cluster reuse re-RENDERED the cluster to a second file: byte-identical twin PNGs with `shared: true, ref_part: null` — a schema violation of the AGENTS.md shared-ref semantics (render the referenced path, do not expect a second file) | claimed_asset map (page, cluster) → owning asset; every reuse path (own_page_pick scored/single, stem_figure, plot fallback) returns a share_ref to the existing crop instead of rendering; twin files pruned as orphans | C22 + corpus stats: 57 shared refs carry ref_part; no twin files remain |
| F29 | 2026-10 (Task 9 wave) | corpus-wide | eyeball verdicts had no durable home: converter confidence flags regressed on every re-run ('re-flag after any converter change' left accepted crops flagged forever), and hand-editing validation-report.json would be overwritten by the next run | CROP-REVIEW.json verdict ledger (schema syllabai.crop-review/0.1): 'accepted' entries clear `review` and set `review_verdict` on every re-run, applied AFTER all confidence overrides (render_crop-time clearing was clobbered by force_review/stem/adjacent flags); new assets keep their converter flags | C22-crop-review-ledger (both directions: ledger→asset exists, asset verdict→ledger accepted) |
| F30 | 2026-10 (Task 9 wave) | 2022-06/2023-06 | class-blind geometry: a plotting surface and a data table are both 'clusters', so (a) the 2025-11 3(c)(i) 'grid' mention (text ABOVE, grid on the NEXT page) scored the p8 data table (coverage 0.398) via the above-anchor; (b) 2022-06 6(b)(iii) 'graph' anchored by the question stem on p13 cropped the apparatus (coverage 0.207) | plot-class coverage guard: a candidate with text_coverage > 0.30 is never a plotting surface (every verified plot crop is <= 0.05) in own_page_pick; the adjacent pass applies the same guard (> 0.15) for stem-anchored picks | eyeball: 2025-11 3(c)(i) = the p9 grid via the question-scoped plot fallback; 2022-06 6(b)(iii) = the p14 grid |
| F31 | 2026-10 (Task 9 wave) | 2020-11 (seed audit) | four of the six v0.5 demo seeds were mis-assigned against the spec registry: 4(c)(ii) is an Mr calculation (seeded 1.25 = write equations), 8(c)(ii) a molar enthalpy calc (seeded 3.9 = measuring rates), 10(b) an empirical-formula determination (seeded 1.31 = formulae by experiment), 1(b)(i) the noble-gas group (seeded 1.20 = metal/non-metal classification) | seeds corrected to 1.26 / 3.4 / 1.33 / 1.24; G6 continues to validate registry membership | G6 + registry cross-check (all 1,180 wave codes validate; 0 invalid) |

| F32 | 2026-10 (wave-10 stub sweep) | 2024-11 + corpus-wide | (a) the stub verdict had no vocabulary: crop-required stubs could never be cleared, so eyeballed honest stubs stayed flagged forever; (b) rule 0 stubbed every dot-and-cross prompt whose text ends in the element-letter signature — but 2024-11 6(c)(i) prints a DRAWN scaffold (N circle + three overlapping H circles as vector art) | (a) `stub-accepted` verdict kind: clears review on crop-required stubs, C22 enforces accepted↔crop / stub-accepted↔crop-required both ways; (b) `drawn_scaffold_below`: a substantial non-furniture vector drawing at/below the instruction un-stubs the prompt and lets the normal anchoring path crop it (fail-closed: unanchorable → stub) | C24 (6(c)(i) = real crop on p19); 6 stub-accepted verdicts |
| F33 | 2026-10 (wave-10 stub sweep) | 2024-11/2023-01 (silent, unflagged) | instruction-below-figure: 'Complete the table' printed BELOW the table picked the nearest cluster below the instruction — 2024-11 6(a)(i) cropped the NEXT part's Mg/Cl electron diagram (cov 0.108, never flagged) and the real formulae table was never cropped; 6(b) then rode the wrong owner's file; 2023-01 1(b) 'table' shared 1(a)(i)'s diagram the same way | forward-branch stem-first promotion (4a-pre): the part's OWN group/question stem naming the noun's class on the part's page resolves before the below-pick, gated by (1) INTRO_RE on the part text (2019-06 3(d)(ii) 'The table lists…' introduces its own figure) and (2) all-down noun anchors (2025-06 1(a) 'Label … on the diagram' references up); stem_figure gained own_group_only/same_page strictness so sibling sentences cannot hijack (the first F33 draft's 6(c)(i) defect) | C23 (6(a)(i) = asset_6_a_table_stem, distinct from 6(b)); 2023-01 1(a)(i)/1(b) re-bound to the three-box row / changes-of-state table |

## Wave summaries

- **Wave 1 — prototype (2020-11 baseline)**: converter + gates G0–G6 + negative controls built; 7 iterations; NC 3/3.
- **Wave 2 — multi-series generalization (6 series)**: F1–F10; 2019-06 archive damage honestly attributed; 2024-06 cross-diff 55/55 vs repo parsed layer.
- **Wave 3 — full-corpus batch (16 series, this run)**: F11–F14; 14/16 full PASS; 169 questions; 930 parts; 1754/1760 marks; cross-diff 161/161 on all three series with a parsed layer (2024-06, 2025-06, 2026-06).
- **Wave 4 — clean-checkout verification (this run)**: kit proven reproducible from `main` (parity 56/56 mod timestamps) but not portable (F15) nor cold-startable (F16); both fixed, C12 added, converter bumped to 0.4, full corpus re-run green from an empty staging dir.
- **Wave 7 — verdict ledger + spec-tagging waves (this run)**: the 24 v0.6 still-tagged crops were re-eyeballed (14 accepted as-is, 10 defective) and their verdicts persisted in CROP-REVIEW.json (F29); the 10 defects drove F25–F30 (resolution-order rebuild, directional nouns, callout labels, paired-figure merge, wrong-class guards, shared-ref dedup). Corpus: 135 crop assets (57 shared refs), 7 honest stubs, 0 twin files, extraction parity 930/930 vs v0.6. Spec-tagging waves then labelled 922 parts across 16 series (1,180 registry-valid codes; 927/930 parts tagged, 3 honest pending-llm) — unlocking learner-model ingestion of the official problem set. Canaries C22 added; floor 0.7.
- **Wave 6 — crop review + serving semantics (this run)**: the 10 review-flagged v0.5 crops and all 32 pending stubs were eyeballed against rendered source pages (every flagged PNG + every stub's page). Verdicts drove F18–F24: footer/stripe furniture filters, anchor disambiguation, mention semantics, anaphora resolution (back-refs, stem figures, sibling shares), foreign-text exclusion, adjacent-page continuation figures, question-scoped claims. Corpus after the wave: 134 crop assets (52 shared references — anaphoric parts no longer duplicate PNGs), 8 honest stubs (dot-and-cross prompts whose scaffolds are text-only, plus 2022-06 6(b)(iii) where the plotted grid cannot be attributed without guessing), 24 review-flagged crops queued for human eyes. 7 source_page anchors disambiguated (each independently verified). Parity vs v0.5: extraction fields byte-identical in all 16 series; gate matrix unchanged (2019-06 G1/G5 REVIEW, 2020-01 G3 honest FAIL). Canaries C15–C21 added; floor 0.6.
- **Wave 8 — wave-10 stub sweep (this run)**: every remaining review-flagged item
  eyeballed against its source page; the "17 new flags" the queue was believed to
  hold reconciled to 7 crop-required stubs (v0.7 AGENTS.md had a mid-wave count).
  6 stub-accepted + 1 accepted (2024-11 6(c)(i), which F32 turned into a real
  crop). F32/F33 fixes surfaced two SILENT mis-bindings on main (2024-11 6(a)(i)
  table→diagram, 2023-01 1(b) table→diagram) — both fixed and canary-pinned.
  Corpus: 0 review flags; 25 ledger verdicts; 24 canaries; 930/930 extraction
  parity vs v0.7; gate matrix unchanged.
- **Wave 5 — render-reveal + Smart Mark (this run)**: v0.5 additive layer — `solution_md` + `mark_points[]` on all 895 linked parts (347 atomic M1..Mn splits; G7 proves coverage + sum invariant; MS marks-column census agrees with QP marks everywhere except known marker-drift layout cases, e.g. 2024-06 3(c) where the (d) row's digit prints inside the (c) block), and the figure crop pass (F17): 126/158 stubs cropped at 150 dpi (14 shared sibling figures, 10 review-flagged), 32 honestly pending (blank-to-complete diagrams like 2024-06 7(b) dot-and-cross, rasterized 2019-06 pages). Parity vs v0.4: extraction fields byte-identical, every gate state preserved. Canaries C13/C14 added; floor 0.5.

## Entry format (append below; never rewrite history)

    | F<max+1> | <date> | <series> | <finding — what defeated the parser/gate, at raw-text level> | <generic fix> | <canary id / new canary added> |
| F34 | 2026-10-21 (2C enablement wave; operator GO ruling trace 1a15ebd93809a525) | corpus-wide (variant layer) | the converter hard-coded the 1C variant everywhere: staging filenames (official-4CH1-1C-*), the manifest name (manifest-<series>-1C.yaml), PAPER_TOTAL=110, the per-series question-count registry, the output dir (4CH1-1C), and the report/canary/cross-diff tooling — the GO'd 2C tranche (ADR-037 GO ruling, 38-paper schedule) could not run at all | generic --paper parametrization: PAPER_TOTALS {1C:110, 2C:70} + per-paper EXPECT_QUESTIONS (2C counts footer-verified 16/16 series: 8/7×13/6, Σ=70 every series); paths_for(series, paper) with paper-suffixed staging names (legacy 1C .txt names still honored); G0 now also asserts manifest paper_number_variant == requested paper; run_all.sh loops papers; report auto-discovers 4CH1-* slices; canary checker paper-aware (per-series canaries carry optional "paper", default 1C; corpus loops cover every variant; CROP-REVIEW ledger keys stay bare-<series> for 1C and use <series>:<paper> for new variants); cross_diff --paper (parsed/ layer is 1C-only today — 2C SKIPs honestly) | C25 (2C slice count), C26 (2C G1 @70 marks); 1C extraction parity 930/930, gate matrix unchanged |
| F35 | 2026-10-21 (2C enablement wave) | 2022-06 2C (then 2022-01 1C regression during verification) | MS content rows can BEGIN with short numerals: the 5(a)(i) Mr working '12   1   16' (relative atomic masses, ≤20-space indent) matched MS_ROW_RE's optional leading qn group and hijacked cur_q 5->12 — every later Q5 marker row inherited question 12, Q5(b)-(d) went unlinkable (G5 79%); conversely, the first guard draft (strict +1 sequence) stalled on the 2022-01 PMT front-matter blurb '70 countries, in 100 languages' (numeral 70 accepted as first question, real markers 1..11 rejected forever, G5 0/65) and broke 2019-06's damaged sequence (rasterized Q10; bare-letter rows '11 a calculate moles…' legitimately skip) | a numeral is a question-number marker when EITHER (a) the same row carries letter/roman marker evidence — evidence wins because damaged papers skip numbers — OR (b) it advances the strict sequence (bootstrap at question 1, then +1 or same-question re-print); numeral-only rows that skip are content | C25/C26 hold; 2022-06 2C G5 39/39 (100%); 2022-01 1C restored to all-PASS; 2019-06 1C back to the shipped 32/53 REVIEW; cross-diff 161/161 |
| F36 | 2026-10-21 (2C enablement wave) | 2021-11 2C | sentence-form MCQ positives: the MS opens with 'The only correct answer is D as francium is the most reactive…' — the F12 pattern ('<L> is (the) correct') misses that word order and F14 elimination keying cannot corroborate because sentence-style 2C entries carry no '<L> <text>' answer rows, so the key was refused (G3 FAIL, 1(e) unkeyed) | positive-statement keying extended to the 'correct answer is <L>' sentence family (guarded against 'answer is not <L>'); still subject to the single-distinct-positive rule, so ambiguous entries keep refusing | C27 (2021-11 2C 1(e) keyed D); 2020-01 7(a)(iii) canary still refuses (C1/C2) |
| F37 | 2026-10-21 (MCQ-key adjudication wave) | 2020-01 1C | the PRINTED Jan 2020 MS itself misplaces the Q7(a) answer rows: (ii)'s answer block ('C chlorine (as it is pale green)' + A/B/D darker-colour rebuttals) prints under (iii), a stray (i) rebuttal ('D is incorrect as iodine is a solid') prints under (ii), and the (iii) 'least reactive' block follows — so positional linkage found no answer row for (ii) and smeared (ii)+(iii) rows into (iii)'s entry (the F6 honest refusal that G3 pinned as FAIL) | human-adjudicated key ledger `MCQ-KEYS.json` (schema syllabai.mcq-keys/0.1): rendered MS p12 viewed, keys decided from QP stem + printed rebuttal pairing + Group-7 chemistry — 7(a)(ii)=C chlorine, 7(a)(iii)=A astatine, 7(a)(i) block completed with its misplaced rebuttal; converter applies the ledger (key + corrected verbatim MS rows) BEFORE build_solution so solution_md/mark_points/choices all derive from the adjudicated block; printed typo 'C is incorrect as iodine is dark grey' corrected to D (iodine IS option D; a MS cannot rebut its own key), verbatim preserved in the ledger | C28 (7(a)(ii)=C), C30 (7(a)(iii)=A), C29 (G3 PASS — the old C1/C2 FAIL pins retired), C31 (ledger↔corpus bidirectional) |
| F38 | 2026-10-21 (spec-tag completion wave) | 2019-06 5(a), 2020-01 10(c)(ii), 2022-01 3(b)(iv) (1C) | the 3 pending-llm 1C parts have NO clean spec point: the published 4CH1 specification itself gives no numbered point for gas density / properties of hydrogen (airship question), for industrial nitrogen chemistry / recycling a process stream (Ostwald-style nitric acid question), or for hazard/safety precautions (safety appears only as the un-numbered practical-work statement) — verified against the official spec PDF (density: 0 hits; Ostwald/Haber: 0 hits; safety: only the general statement) | terminal `no-spec-point` tagging state: the decision + per-part spec-PDF evidence documented in the series spec-labels files (`no_spec_point` map); converter emits the state instead of pending-llm; on the spec-labelled 1C tranche pending-llm becomes a must-not-persist state (coverage stays 927/930 tagged by design — a wrong code would corrupt learner-model mastery attribution); 2C keeps its honest pending-llm until its first wave | C32 (1C: 0 pending-llm; no-spec-point ↔ labels-file entries bidirectional; entries resolve to real parts and carry no codes) |

| F41 | 2026-10-22 (rasterization re-capture wave) | 2019-06 1C QP pages 4/12/16/18/20/26 (144-dpi archive scan; Q7 lost entirely, Q1/Q11/Q12/Q13/Q15 heads lost; G1 honest REVIEW 104/110 since the multi-series wave) | the archive scan's image-only pages carry no text layer, so pdftotext cannot see Q7 or the heads of Q1/Q11/Q12/Q13/Q15; the pipeline honestly REVIEWed the damage instead of inventing content | OCR source-layer path, fail-closed end to end: staged `UPLOAD/ocr/<series>-<paper>/qp-pNN.txt` (prepared page texts) + `ocr-pages.json` manifest pinning sha256 + tool + corrections per page; the converter verifies every sha and the source-PDF sha before use (mismatch aborts), splices the prepared text into page_norm so mentions anchor with page attribution, excludes recovered pages from the G1 image-only defect attribution, and emits `ocr_pages` receipts; page texts are agent transcriptions from the 600-dpi render cross-checked against the tesseract 5.5.0 draft and, where noted, the MS text layer (equation subscripts CH4/2O2/CO2/2H2O + table values 20.0/14.2 are below the 144-dpi OCR floor — transcribed with dual-source evidence and pinned by canaries C49-C51); prep committed as `scripts/prep_ocr_layer_2019.py` (deterministic, idempotent: regenerates the staged qp.txt from the archive PDF and re-splices) | C4 retired -> C4-archive-damage-repaired (G1 PASS 110/110); C48 receipts; C49 Q7 stem; C50 equation; C51 table values |
| F42 | 2026-10-22 (rasterization re-capture wave) | 2019-06 1C MS: 21 parts whose answers print as early-format bare marker rows — `d   i` (bare letter + bare roman: 3(d)(i), 13(b)(i), 14(f)(i), 15(b)(i)), `   ii` (bare roman continuation: 3(d)(ii), 5(c)(ii), 6(b)(ii), 8(c)(ii), 10(a)(ii), 13(b)(ii), 14(f)(ii)), glued `10ai`/`bi` (10(a)(i), 10(b)(i)), end-of-line bare letter with an image answer cell (9(b) dot-and-cross), and indent-0 bare roman after a page break (11(b)(iii)) — plus one unit fragment `(g)` in the answer column that MS_MARKER_ONLY read as a letter marker and re-pointed the marker state | the 2019-06 MS predates the parenthesised marker convention; all four bare shapes fell to content, 21 parts stayed unmatched (G5 60%), and the pre-existing `(g)` hijack became load-bearing once roman continuation rows needed the correct letter context | generic fixes, all gated: (1) marker-column indent gate (<=12) on every marker-row regex — marker rows live in the marker column, answer-column fragments like `(g)` are content; (2) MS_BARE_LETTER_ROMAN_RE (letter + spaces + bare roman), MS_GLUED_MARKER_RE (unspaced qn+letter+roman / letter+roman, letter-ascending gate), MS_BARE_ROMAN_RE (indent 0-12, ascending-sequence gate: the roman must be exactly the next one for the (question, letter) — content tokens can never hijack); (3) end-of-line lookahead on MS_BARE_LETTER_RE (9(b) opens its entry, solution = the printed notes block); (4) a rest that is ONLY a marks-column digit opens a marker-only entry (3(d)(ii)'s digit must not become its answer); (5) repeated MS page-table headers are furniture (a marker row near a page break no longer inherits `Question / Answer Notes Marks / number` as its solution); (6) question-level-roman lookup fallback (exactly-one-letter rule). Damage-repair renumber: 11(iii)->11(b)(iii), 15(i..iii)->15(b)(i..iii) — the recovered group headers restore the true nesting; spec-labels keys migrated. G5: 32/53 (60%) -> 63/64 (98%); the one residual unmatched is 3(d)(ii), whose MS answer cell is a printed IMAGE (eyeballed on the rendered MS page) — honest terminal state, pinned by C52 | C52 (3(d)(ii) honest state), C53 (7 parts linked + renumber pin); corpus-wide parity: the other 31 slices extraction-identical with identical G5 summaries |
| F43 | 2026-10-22 (rasterization re-capture wave — surfaced by the new G-E1 export gate) | corpus-wide (all 32 slices): 278 served solution blocks carried the repeated MS page-table header ('Question / Answer Notes Marks / number') inside solution_md / mark_points text — e.g. 2020-01 2C 1(c)(iii) served 'sulfur ALLOW S\nQuestion\nAnswer Notes Marks\nnumber' | the MS is one table and every printed page repeats its header; a marker row near a page break opened an entry that then swallowed the next page's header rows as content, and G5 never noticed because the linkage COUNTS were right — only the block contents were polluted. Found within hours of the G-E1 export gates existing: the gate's part-level bundle comparison flagged every one of the 278 blocks | repeated MS page-table headers are furniture (FURNITURE_LINE), so no entry can inherit them; the fix also shaved stray 'Additional guidance' header variants | C54 (solution_blocks_header_free, corpus-wide scan) |
| F41b | 2026-10-22 (same wave) | the v2 hub bundle of record carried the same 278-block pollution plus 10 mis-linked 2019-06 1C solution blocks (e.g. 1(c) served a protons/neutrons block that belongs to no 2019-06 1C part; 2(c) served a halogen-displacement block) — wrong ANSWERS served since the v0.6 wiring | the bundle was a palimpsest of sync generations and nothing ever deep-compared it against a fresh export until G-E1 | the wave-12 hub sync re-exports the whole official block under G-E1 with the frozen delta census (scripts/exporter-disclosures/2026-10-22-wave12.json); post-sync, G-E1's default zero-delta law holds | verified in the G-E1 census (16 re-linked + 10 mis-linked corrections on 2019-06 1C) |
| F44 | 2026-10-22 (exporter namespace-hardening follow-up) | the exporter of record (both the PR#31 v1 and the wave-12 G-E v2) emitted `topicSlug: 'official-past-papers'` on every official set, while the hub bundle of record carries the per-paper namespace (`topicSlug := the set's own slug` — v2 0776f8dea7, the run-003 shim-gate fix of record: one shared topicSlug with per-set restarting orders collided 12 base refs (35 duplicate emitted forms) and the frozen package-global seenRefs gate refused the bundle) | the G-E1 gate compared sets at PART level only; set-level identity fields (topicId/topicSlug/name/section/curriculum/source/schema/...) were an invisible blind spot, so the exporter of record would have silently reverted the namespace law on the very next bundle sync | exporter v3: (1) `topicSlug := the set's own slug`; (2) official-set detection by slug prefix (`is_official`) — the old `topicSlug=='official-past-papers'` filters silently selected ZERO sets after the namespace law landed, making G-E2 vacuous; (3) G-E1b identity closure: the 11 set-level identity fields must be byte-equal vs the bundle of record, with NO disclosure path (identity is a law, not a wave artifact — a real namespace change must land in the exporter of record and the bundle in the same reviewed PR) | negative control verified live: a bundle with one set reverted to the shared topicSlug is REFUSED by G-E1b; the wave-12 sync then ran 5/5 gates green (G-E3/G-E2/G-E1/G-E1b/G-E4) |
## Wave summaries (continued)

- **Wave 9 — 2C enablement (this run)**: the operator's GO ruling (ADR-037, trace
  1a15ebd93809a525) scheduled the remaining 4CH1 variants; the 2C tranche (16
  papers) is converted end-to-end by the same unchanged gate suite. Converter
  v0.8.0 = F34 (paper parametrization) + F35 (question-number marker discipline)
  + F36 (sentence-form positives). Corpus after the wave: **1C 169 Q / 930 parts /
  1754/1760 marks (unchanged; 14/16 all-PASS, honest 2019-06 REVIEW + 2020-01
  refusal)** + **2C 110 Q / 607 parts / 1120/1120 marks / 27/27 MCQs keyed /
  16/16 all-PASS** — 2C scans are cleaner than 1C (no rasterized pages). 27
  canaries hold; cross-diff 161/161 (1C parsed layer; 2C has no parsed layer
  yet — honest gap). 2C spec tagging: no labels authored yet, all 607 parts
  honestly `pending-llm`; 2C figure crops: 22 review-queue items awaiting
  eyeballs (first-pass converter flags, per the CROP-REVIEW protocol).
- **Wave 10 — MCQ-key adjudication + 1C spec-tag completion (this run, v0.8.1)**:
  the two 1C human-decision items left open since the multi-series wave are
  closed with rendered-page evidence. (1) The 2020-01 Q7(a) MCQ keys were
  adjudicated into MCQ-KEYS.json (F37) — the printed MS itself misplaces the
  answer rows, so the pipeline's honest refusal was correct and the fix is a
  durable human ledger, not a parser change; G3 for 2020-01 returns to PASS
  (1C fully keyed 58/58), and the C1/C2 refusal-state pins were replaced by
  adjudicated-state pins C28/C29/C30/C31. (2) The 3 pending-llm 1C parts were
  decided as terminal `no-spec-point` (F38) after verifying the official spec
  gives them no numbered point (C32). Parity vs v0.8.0: exactly 6 1C parts
  touched (3 MCQ parts in 2020-01, 3 tagging states), every 2C slice
  byte-identical; 30 canaries; all gates at their v0.8.0 states except
  2020-01 G3 FAIL→PASS.
| F39 | 2026-10-22 (2C wave: crop-eyeball + spec-labels + hub export) | corpus-wide (variant layer) | the F34 wave documented the `<series>:<paper>` CROP-REVIEW ledger keying convention (AGENTS.md + C22 both use it) but the converter's load site kept reading the bare `reviews[series]` map — non-1C verdict homes were silently never loaded, so 2C verdicts could never clear anything | load site paper-aware: 1C keeps the legacy bare `<series>` home, other variants read `<series>:<paper>`; C22 already enforced the documented convention in both directions, so the mismatch was invisible until the first non-1C verdict wave | C22 exercises the 2C homes for the first time (17 verdicts across 10 `<series>:2C` homes) |
| F40 | 2026-10-22 (2C wave) | 2C: 2021-11 5(c)/7(c), 2023-01 7(b)(i), 2024-11 5(b)(i), 2022-06 7(d)(i)/3(c), 2023-11 3(c)/7(d)(i), 2025-06 2(e), 2025-11 6(a)/6(b), 2019-06 5(c), 2022-01 6(a)(iii), 2026-06 4(c); 1C: 2021-01 1(b)-family, 2025-06 1(b)(ii)-family, 2022-01 3(b)(ii), 2021-11 11(b), 2023-06 8(c)(ii), 2022-06 10(c)(ii) | nine defect mechanisms behind the 22 first-pass 2C review items, each diagnosed at raw-text level: (a) adjacent_crop's whole-stem fallback anchored ANY stem text printed on the neighbour page, so create/data mentions ('Draw an energy level diagram', 'Complete the table') stole unrelated data figures (reactivity box, bond tables, burette diagram, stem apparatus); (b) noun_anchor_y direction heuristics missed two reference-up shapes ('the shape OF THE graph', 'the data/values IN THE table'); (c) stem linearizations glue displayed-formula glyph junk into the intro sentence ('...H O O H The table gives the bond energies.') so page_of_text/figure_anchor_y miss every page and the stem table is silently lost; (d) drawn-axis scaffolds (thin vertical Energy line + arrowhead, no cluster) fell to 'no croppable figure' stubs — and fitz treats the line's zero-width rect as EMPTY, collapsing expand_with_labels to just the absorbed 'Energy' label; (e) PUA furniture bullets glued to short problem_md poison every F18b page probe ('Explain the shape of the graph. \uf0a2...' → 0 hits → page None); (f) noun_anchor_y's pre-noun 6-word window is ambiguous for sentence-INITIAL nouns ('The table shows...' probes as bare 'the table' and lands on a LATER line below the figure); (g) 'apparatus in your answer' (student-provided) was unsuppressed, while the first suppression draft over-fired on 'use information from THE TABLE in your answer' (a printed-figure reference); (h) the printed MS sometimes sub-numbers a part the QP leaves undivided ('1 (b) (i)' for the QP's 1(b), Jan 2021 both papers) or sets romans in caps ('(II)', Summer 2025) — linkage missed both shapes and 1(b)(i)'s block swallowed (ii)'s rows | generic fixes, all fail-closed: (a) fallback survives only for DEFINITE references ('the diagram shows') and never for create/data-source mentions; (b) 'of the <noun>' and 'data/values in/on/from the <noun>' point UP; (c) stem probes retry from the noun phrase then bounded 10/6-word windows; (d) axis_scaffold_crop crops a substantial thin-vertical drawing below the instruction (min-stroke normalisation before union), gated to FORWARD draw/complete instructions with figure-class nouns; (e) PUA stripped from anchor probes only (verbatim problem_md untouched); (f) post-context probes (noun + following words, sentence-bounded) tried before the pre-noun window; (g) '<noun> in your answer' suppressed only for non-definite occurrences; (h) marks-matched sub-numbered block fallback when the letter-group has exactly one part + roman case normalization in every MS row branch. En-route adjudications (1C effects of (f)/(c)/(h), each eyeballed): 2021-11 11(b) 'Table 2' now crops Table 2 (was Table 1's stem), 2023-06 8(c)(ii) crops its own mass-readings table (was 8(b)'s), 2023-11 2(b)(i-iii) own the numbered table (same figure, stem asset retired), 2022-06 10(c)(ii) kept its stem table after the (g) guard, and 5 previously-unmatched parts gained correct MS blocks (2021-01 3(a)/3(b), 2021-06 7(a), 2022-01 5(a), 2023-01 10(a)) | C33 (2C spec-tag terminal), C34-C37 (stem tables), C38-C40 (axis rescues), C41 (PUA anchor), C42-C44 (sentence-initial anchors), C45 (mention suppressed), C46/C47 (MS linkage) |

| F41 | 2026-10-22 (rasterization re-capture wave) | 2019-06 1C QP pages 4/12/16/18/20/26 (144-dpi archive scan; Q7 lost entirely, Q1/Q11/Q12/Q13/Q15 heads lost; G1 honest REVIEW 104/110 since the multi-series wave) | the archive scan's image-only pages carry no text layer, so pdftotext cannot see Q7 or the heads of Q1/Q11/Q12/Q13/Q15; the pipeline honestly REVIEWed the damage instead of inventing content | OCR source-layer path, fail-closed end to end: staged `UPLOAD/ocr/<series>-<paper>/qp-pNN.txt` (prepared page texts) + `ocr-pages.json` manifest pinning sha256 + tool + corrections per page; the converter verifies every sha and the source-PDF sha before use (mismatch aborts), splices the prepared text into page_norm so mentions anchor with page attribution, excludes recovered pages from the G1 image-only defect attribution, and emits `ocr_pages` receipts; page texts are agent transcriptions from the 600-dpi render cross-checked against the tesseract 5.5.0 draft and, where noted, the MS text layer (equation subscripts CH4/2O2/CO2/2H2O + table values 20.0/14.2 are below the 144-dpi OCR floor — transcribed with dual-source evidence and pinned by canaries C49-C51); prep committed as `scripts/prep_ocr_layer_2019.py` (deterministic, idempotent: regenerates the staged qp.txt from the archive PDF and re-splices) | C4 retired -> C4-archive-damage-repaired (G1 PASS 110/110); C48 receipts; C49 Q7 stem; C50 equation; C51 table values |
| F42 | 2026-10-22 (rasterization re-capture wave) | 2019-06 1C MS: 21 parts whose answers print as early-format bare marker rows — `d   i` (bare letter + bare roman: 3(d)(i), 13(b)(i), 14(f)(i), 15(b)(i)), `   ii` (bare roman continuation: 3(d)(ii), 5(c)(ii), 6(b)(ii), 8(c)(ii), 10(a)(ii), 13(b)(ii), 14(f)(ii)), glued `10ai`/`bi` (10(a)(i), 10(b)(i)), end-of-line bare letter with an image answer cell (9(b) dot-and-cross), and indent-0 bare roman after a page break (11(b)(iii)) — plus one unit fragment `(g)` in the answer column that MS_MARKER_ONLY read as a letter marker and re-pointed the marker state | the 2019-06 MS predates the parenthesised marker convention; all four bare shapes fell to content, 21 parts stayed unmatched (G5 60%), and the pre-existing `(g)` hijack became load-bearing once roman continuation rows needed the correct letter context | generic fixes, all gated: (1) marker-column indent gate (<=12) on every marker-row regex — marker rows live in the marker column, answer-column fragments like `(g)` are content; (2) MS_BARE_LETTER_ROMAN_RE (letter + spaces + bare roman), MS_GLUED_MARKER_RE (unspaced qn+letter+roman / letter+roman, letter-ascending gate), MS_BARE_ROMAN_RE (indent 0-12, ascending-sequence gate: the roman must be exactly the next one for the (question, letter) — content tokens can never hijack); (3) end-of-line lookahead on MS_BARE_LETTER_RE (9(b) opens its entry, solution = the printed notes block); (4) a rest that is ONLY a marks-column digit opens a marker-only entry (3(d)(ii)'s digit must not become its answer); (5) repeated MS page-table headers are furniture (a marker row near a page break no longer inherits `Question / Answer Notes Marks / number` as its solution); (6) question-level-roman lookup fallback (exactly-one-letter rule). Damage-repair renumber: 11(iii)->11(b)(iii), 15(i..iii)->15(b)(i..iii) — the recovered group headers restore the true nesting; spec-labels keys migrated. G5: 32/53 (60%) -> 63/64 (98%); the one residual unmatched is 3(d)(ii), whose MS answer cell is a printed IMAGE (eyeballed on the rendered MS page) — honest terminal state, pinned by C52 | C52 (3(d)(ii) honest state), C53 (7 parts linked + renumber pin); corpus-wide parity: the other 31 slices extraction-identical with identical G5 summaries |
| F43 | 2026-10-22 (rasterization re-capture wave — surfaced by the new G-E1 export gate) | corpus-wide (all 32 slices): 278 served solution blocks carried the repeated MS page-table header ('Question / Answer Notes Marks / number') inside solution_md / mark_points text — e.g. 2020-01 2C 1(c)(iii) served 'sulfur ALLOW S\nQuestion\nAnswer Notes Marks\nnumber' | the MS is one table and every printed page repeats its header; a marker row near a page break opened an entry that then swallowed the next page's header rows as content, and G5 never noticed because the linkage COUNTS were right — only the block contents were polluted. Found within hours of the G-E1 export gates existing: the gate's part-level bundle comparison flagged every one of the 278 blocks | repeated MS page-table headers are furniture (FURNITURE_LINE), so no entry can inherit them; the fix also shaved stray 'Additional guidance' header variants | C54 (solution_blocks_header_free, corpus-wide scan) |
| F41b | 2026-10-22 (same wave) | the v2 hub bundle of record carried the same 278-block pollution plus 10 mis-linked 2019-06 1C solution blocks (e.g. 1(c) served a protons/neutrons block that belongs to no 2019-06 1C part; 2(c) served a halogen-displacement block) — wrong ANSWERS served since the v0.6 wiring | the bundle was a palimpsest of sync generations and nothing ever deep-compared it against a fresh export until G-E1 | the wave-12 hub sync re-exports the whole official block under G-E1 with the frozen delta census (scripts/exporter-disclosures/2026-10-22-wave12.json); post-sync, G-E1's default zero-delta law holds | verified in the G-E1 census (16 re-linked + 10 mis-linked corrections on 2019-06 1C) |
| F44 | 2026-10-22 (exporter namespace-hardening follow-up) | the exporter of record (both the PR#31 v1 and the wave-12 G-E v2) emitted `topicSlug: 'official-past-papers'` on every official set, while the hub bundle of record carries the per-paper namespace (`topicSlug := the set's own slug` — v2 0776f8dea7, the run-003 shim-gate fix of record: one shared topicSlug with per-set restarting orders collided 12 base refs (35 duplicate emitted forms) and the frozen package-global seenRefs gate refused the bundle) | the G-E1 gate compared sets at PART level only; set-level identity fields (topicId/topicSlug/name/section/curriculum/source/schema/...) were an invisible blind spot, so the exporter of record would have silently reverted the namespace law on the very next bundle sync | exporter v3: (1) `topicSlug := the set's own slug`; (2) official-set detection by slug prefix (`is_official`) — the old `topicSlug=='official-past-papers'` filters silently selected ZERO sets after the namespace law landed, making G-E2 vacuous; (3) G-E1b identity closure: the 11 set-level identity fields must be byte-equal vs the bundle of record, with NO disclosure path (identity is a law, not a wave artifact — a real namespace change must land in the exporter of record and the bundle in the same reviewed PR) | negative control verified live: a bundle with one set reverted to the shared topicSlug is REFUSED by G-E1b; the wave-12 sync then ran 5/5 gates green (G-E3/G-E2/G-E1/G-E1b/G-E4) |
## Wave summaries (continued)

- **Wave 11 — 2C crop eyeball + spec-label wave + MS-linkage fixes (this run, v0.9.0)**:
  the 2C backlog opened by wave 9 is closed end-to-end. (1) All 22 first-pass review
  items eyeballed against their source PDF pages: 6 crops accepted as-is, the rest
  traced to 9 defect mechanisms (F40 a-i) — every fix generic, every re-emitted crop
  re-eyeballed (12 new crops + 1 honest stub accepted). The v0.8.1 ledger-keying bug
  (F39) surfaced when the first 2C verdicts were written and is fixed; 17 verdicts now
  live under 10 `<series>:2C` homes. Corpus: 607 parts / 86 assets (85 crops + 1
  stub-accepted) / 0 review flags on the 2C tranche beyond the documented honest stub;
  1C parity: extraction fields byte-identical, 9 adjudicated improvements (5 unmatched
  parts now linked, 3 wrong figure bindings corrected, 1 stem asset retired) — every
  one eyeballed. (2) The 2C spec-label wave (first wave, labels only): 607/607 parts
  resolved — 584 tagged with 1,014 registry-validated codes (G6: 0 invalid) + 23
  terminal no-spec-point parts decided against the published spec PDF (safety
  precautions, ester/fuel definitions, investigation-design and graph-skills parts —
  same evidence standard as F38); C33 pins the terminal state. (3) 45 canaries hold;
  cross-diff 161/161 (1C parsed layer); all gate states equal-or-better than v0.8.1.

- **Wave 12 — rasterization page re-capture + early-MS linkage (this run, v0.10.0)**:
  the last honest REVIEW in the corpus is closed. (1) The 2019-06 archive scan's six
  content-bearing image-only pages were re-captured through the F41 OCR source layer:
  Q7 recovered whole (3 parts / 6 marks), the heads of Q1/Q11/Q12/Q13/Q15 recovered
  (stems, methods, results tables, 8 further parts / 14 marks), every recovered part
  eyeballed against the 600-dpi render, transcription deviations from the OCR draft
  enumerated in the staged corrections ledger with dual-source evidence (MS text layer
  corroborates the equation subscripts and the 20.0/14.2 table values). G1 returns to
  PASS 110/110 (15 questions, footer-verified). (2) F42 fixes the 2019-06 early-MS
  bare-marker shapes: 20 of the 21 long-unmatched parts now link (G5 32/53 -> 63/64);
  the last one, 3(d)(ii), is honestly unmatched — its MS answer cell is a printed
  image, and the pipeline refuses to fabricate text for it (C52 pins the state).
  15(a)'s tests-table stub is verdict-documented in CROP-REVIEW (stub-accepted, C22).
  Part census: 941 parts corpus-wide (930 -> 941: +11 recovered, corpus marks 104 ->
  110 on the affected slice). Parity vs v0.9.0: 31/32 slices extraction-identical
  with identical G5 summaries; 2019-06 1C diffs are exactly the 11 recovered + 4
  renumbered parts. 51 canaries hold; NC 3/3 on every slice.
  Wave 12 amendment (F43/F41b): the G-E1 export gate's first run earned its keep —
  beyond the documented wave-12 deltas it surfaced (a) 278 solution blocks carrying the
  MS page-table header corpus-wide (cleaned; C54 pins the law) and (b) 10 mis-linked
  2019-06 1C solution blocks in the HUB BUNDLE of record (wrong answers served since
  the v0.6 wiring; corrected by the wave-12 re-export with the frozen census). Marks
  and problem_md are untouched everywhere: the changed-key census is exactly
  {markPoints+solutionMd} ×278, {answerStatus+markPoints+solutionMd} ×16, and the
  2019-06 1C structural set. Zero part marks changed anywhere.
- **Wave 12 amendment 2 (F44)**: exporter v3 — the per-paper topicSlug namespace of record
  (v2 0776f8dea7) adopted; official-set filters moved to slug-prefix detection (the old
  topicSlug filter silently selected zero sets post-law, making G-E2 vacuous); G-E1b closes
  G-E1's set-level identity blind spot (11 fields byte-equal, no disclosure path — negative
  control verified). The wave-12 delta census is committed of record at
  `scripts/exporter-disclosures/2026-10-22-wave12.json`, making the G-E1 --expected-deltas
  disclosure reproducible from the repo itself. No corpus changes; 52 canaries untouched.


## Wave 19 — exporter v5, the UX-doctrine wave (F53–F56; operator wave-15)

Doctrine change of record (operator, 2026-10-22): **best experience for the learner is the
governing law; verbatim transcription is retired as the governing constraint** — values are
still never invented (every number, equation and option text is the corpus's own; presentation
may be re-formed). The wave compared how an SME set renders vs the equivalent official part and
fixed the four structural gaps found. No corpus changes; 63 corpus canaries untouched; the
served bundle PR carries a full disclosure census.

- **F53 stem restore (the headline)**: every prior exporter version silently dropped ALL
  upstream `stem_md` — 427 stems, so every official question opened cold at part (a)
  ("After a short time, the crystal becomes smaller…" with no crystal). The exporter now
  restores each stem onto the question's first part (SME's own pattern). Stems pass the
  eyeballed **`Official-ExamQuestion/STEM-RESTORE.json`** ledger (92 verdicts: 26 authored
  rebuilds — data tables, substance boxes, reaction flows, method steps, values verbatim;
  16 drop-tail verdicts — flattened diagram-label runs redundant with a figure/table the
  learner sees on some part; 50 keep + tranche flags). Mechanical cleaning: control chars
  (BEL \x07 in 2022-06 1CR Q10), •/● method runs → markdown bullets, "Step N" runs → lines.
  Splice-guard: 16 stems the converter already folded into part 1 are not duplicated.
  Result: 411/427 stems visible on first parts (the other 16 were never missing).
- **F54 id-collision fix**: `offp_<series>_<part>` collided **631×** across the 1C/2C/1CR/2CR
  sets of the same series (`offp_2019-06_1-a` named four different parts), cross-wiring saved
  MCQ answers, typed-answer drafts and attempt keys between papers. Ids now carry the paper:
  `offp_<series>_<paper>_<part>` (2607 parts, all unique). Full old→new rename map disclosed
  per slug in `scripts/exporter-disclosures/2026-10-22-wave19-ux-stems.json`; the verify
  harness walks the disclosure through the lattice (any unrenamed drift still refuses). The
  core identity bridge is unaffected (joins by topicSlug + positional order, ADR-029; verified
  1:1 over the SME corpus only — official sets do not bridge).
- **F55 MS-furniture strip (exporter-side law)**: trailing answer-grid header lines
  ("Question / Answer Notes Marks / number", up to 4, glue digits tolerated) are stripped from
  solutionMd and markPoints textMd at export. The 21 upstream furniture carriers now serve
  clean. (The corpus keeps the raw extraction; this is a serving-format law like F15.)
- **F56 honest stub note**: the crop-required figure line no longer says "queued for human
  verification" (the wave-13 CROP-REVIEW verdicts settled that queue); it now tells the
  learner the truth: no printed figure accompanies the part — the answer IS the diagram you
  draw in the paper's answer space.
- **F-W15-3 reflow RETIRED before ship**: joining PDF hard-wraps was render-identical (the hub
  renders single newlines as soft breaks — react-markdown, no remark-breaks) and disturbed the
  wave-14 verbatim pins (2019-06 3(d)(ii) tick-table). Line breaks stay as extracted.
- **Verification**: exporter gates G-E1 (5214-delta rename census), G-E1b (identity fields
  byte-equal ×54), G-E2 (sum laws), G-E3 (census constants, 4860 marks), G-E4 (SME prefix
  byte-identical, 2605414 bytes), G-E5 (data cut main@1f2aab451bf4 proven against staging);
  verify harness green (lattice through renames, 661 content deltas = disclosure exactly,
  mark law 2607 parts). 2019-06 3(d)(ii) solutionMd/markPoints byte-identical through the
  wave (C52 state preserved). Zero PUA in the exported bundle. Ids unique 2607/2607.
- **Wave-20 backlog (filed in STEM-RESTORE.json tranche flags)**: ~28 stem figures/tables to
  crop (chromatograms, apparatus, structure diagrams the stems reference but no crop carries),
  9 displayed-formulae letter-runs (crop tranche), 3 interleaved property tables to eyeball.

- **T-UGM-MODE1-1 — UGM mode-1 lane enrichment, quadratics pilot (this run)**: first
  landing from the Underground Mathematics reverse-engineering track
  (SyllabAI/syllabai-experimental @ 915bfa8c; ADR-UGM-0001 Accepted 2026-10-22,
  operator-ratified). New `UGM-Enrichment/` domain, schema
  `syllabai.ugm-spec-enrichment/1.0`, `review_state` SUGGESTED per AGENT.md rule 2
  (LLM-assisted alignment candidates with per-row confidence — not verbatim joins;
  no coverage manufactured). `cie-a-level-maths-20-pure-1-quadratics.json`: 61 aligned
  rows over official codes 1.1.1–1.1.5 (56 of 59 station resources aligned = 95%;
  3 explicit non-overlaps recorded as such, not collapsed — rule 3), provenance
  strings preserved, 5 `primaryPick` markers. FACTS ONLY: slugs/titles/types/levels/
  relations/provenance — no UGM text bodies; rights © Cambridge/UCLES unchanged
  (licensing block in-file + dir README). Mode-2 deep-link rendering was dropped by
  operator directive 2026-10-22 before implementation (syllabai-v2#305 closed
  not_planned) — these rows land as data of record only. Base commit 1f2aab45.

- **T-UGM-IMPORT-1 — UGM text corpus import, quadratics lane (this run)**: second
  landing from the Underground Mathematics reverse-engineering track
  (SyllabAI/syllabai-experimental @ aa13533a; ADR-UGM-0001 as amended 2026-10-23).
  New `UGM-Resources/` corpus family: the **text bodies** of the 59 quadratics-station
  resources as YAML-front-matter markdown (`pure-1-quadratics/`), under the operator's
  permission attestation of 2026-10-23 (LICENSE-DATA.md Amendment 2026-10-23 — the
  landing path the `UGM-Enrichment/` README anticipated for text of record).
  Text-only import law: math preserved byte-true in UGM's native `\( \)` / `\[ \]`
  delimiters (build-time audit: 6,434 = 6,434, zero files differing); UGM section
  structure/panel titles/provider spellings preserved; 57 image + 24 interactive
  references recorded in front-matter, NOT fetched; MANIFEST.json carries SHA-256 per
  file + source URL + capture date. Spec-point mappings are the P3c cross-map of
  record, landed `SUGGESTED` (AGENT.md rule 2; no coverage manufactured — 3 honest
  non-overlaps) with `primaryPick` cross-referenced to `UGM-Enrichment/` #55. Rights
  © Cambridge/UCLES unchanged per file; takedown law unchanged. Base commit 3a1e99b.

- **T-UGM-MODE1-2 — UGM mode-1 lane enrichment, Functions lane (this run)**: second
  landing from the Underground Mathematics reverse-engineering track — P3c
  generalisation lane 2, the hop lane 1's own cross-map pre-flagged ("parabola
  families belong with P1 Functions (1.2) / transformations"). Cross-map of record:
  `cross-map-functions.json` @ `syllabai-experimental` e59276be (spine export 1.2
  rows 4a592ed0). New `UGM-Enrichment/cie-a-level-maths-20-pure-1-functions.json`,
  schema `syllabai.ugm-spec-enrichment/1.0`, `review_state` SUGGESTED per AGENT.md
  rule 2 (LLM-assisted alignment candidates with per-row confidence). UGM station
  `combining-functions` (38 resources) → CIE 9709 P1 subtopic 1.2 Functions: 50
  aligned rows over official codes 1.2.1–1.2.5 (27 of 38 station resources aligned
  = 71.1%, threshold ≥70% met; 11 explicit non-overlaps recorded as such, incl. 2
  interactive-only pages with no extractable text — rule 3), 5 `primaryPick`
  markers (forming-functions-defining-domains / compose / invertibles / r9824 /
  order-order), provenance strings preserved (24/38: 13 UCLES + 10 Oxford MAT +
  1 NRICH). Station scope: sibling station `thinking-about-functions` intentionally
  out of scope (modulus/asymptote/odd-even content → CIE P3 / IAL lanes). FACTS
  ONLY: slugs/titles/types/levels/relations/provenance — no UGM text bodies; rights
  © Cambridge/UCLES/MAT/NRICH unchanged (licensing block in-file + dir README).
  Mode-2 deep-link rendering remains dropped (operator directive 2026-10-22,
  recorded in `mode2Note`); the text route is the 2026-10-23 operator attestation.
  Base commit d89c2e6b.

- **T-UGM-IMPORT-2 — UGM text corpus import, Functions lane (this run)**: third
  landing from the Underground Mathematics reverse-engineering track, extending the
  `UGM-Resources/` corpus family to its second lane under the same operator
  attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23 — its subject
  is the corpus family built from the 2026-10-22 full-site crawl, so no new license
  amendment is required). New `UGM-Resources/pure-1-functions/`: the **text bodies**
  of the 38 combining-functions-station resources as YAML-front-matter markdown.
  Text-only import law: math preserved byte-true in UGM's native `\( \)` / `\[ \]`
  delimiters (build audit 1,993/1,993 inline + 235/235 block = 2,228 balanced, zero
  files differing); UGM section structure/panel titles/provider spellings
  preserved; the 2 interactive-only pages (`going-backwards`, `maths-for-dinner`)
  land as honest-empty bodies with full front-matter identity; asset/interactive
  references recorded in front-matter, NOT fetched. `MANIFEST.json` bumps to
  **v2 (multi-lane)**: one block per lane, lane-1 file rows re-verified
  byte-identical by re-hash at the v2 build (59/59), lane-2 38 rows fresh.
  Spec-point mappings are the P3c lane-2 cross-map of record, landed `SUGGESTED`
  (AGENT.md rule 2; no coverage manufactured — 11 honest non-overlaps) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-2. Rights
  © Cambridge/UCLES/MAT/NRICH per file; takedown law unchanged. Base commit
  d89c2e6b.

- **T-UGM-MODE1-3 — UGM mode-1 lane enrichment, Coordinate geometry lane (this run)**: fourth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Enrichment/` lane family to CIE 9709 P1
  subtopic 1.3 Coordinate geometry under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md`
  Amendment 2026-10-23). New file `cie-a-level-maths-20-pure-1-coordinate-geometry.json`: the first **two-station
  lane** (geometry-of-equations 34/38 + circles 27/47 = 61/85 aligned, 77 alignment rows), hub-spine parse
  fragments 1.3.1a/1.3.2a folded into parent codes 1.3.1/1.3.2 of record (spine export keeps all four rows
  verbatim); 24 honest non-overlaps with recorded reasons (the circles station's radian-mensuration/circle-theorem
  strands serve CIE 1.4 / IAL lanes, never forced); primary picks straight-line-pairs (1.3.1) and teddy-bear
  (1.3.2); provenance strings preserved (44/61 aligned rows with UCLES/MAT/UKMT/O&C tuples). FACTS ONLY:
  slugs/titles/types/levels/relations/provenance — no UGM text bodies; rights © Cambridge/UCLES/MAT/UKMT/O&C
  unchanged (licensing block in-file + dir README). Mode-2 deep-link rendering remains dropped (operator
  directive 2026-10-22, recorded in `mode2Note`); the text route is the 2026-10-23 operator attestation.
  Base commit cb947595 (syllabai-experimental).

- **T-UGM-IMPORT-3 — UGM text corpus import, Coordinate geometry lane (this run)**: fourth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Resources/` corpus family to its third
  lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23). New
  `UGM-Resources/pure-1-coordinate-geometry/`: the **text bodies** of the 85 geometry-of-equations + circles
  resources as YAML-front-matter markdown. Text-only import law: math preserved byte-true in UGM's native
  `\( \)` / `\[ \]` delimiters (build audit 85/85 files balanced, rendered delimiter census exactly equals the
  ugm-clean section census per file; questionWell verified 0/85 additive — a pre-normalised duplicate of the
  Question panel, excluded from the census); UGM section structure/panel titles/provider spellings preserved;
  figures and GeoGebra components recorded as front-matter/inline markers, NOT fetched. `MANIFEST.json` bumps to
  **v3**: lane-3 block fresh (85 rows, sha256 each), lane-1/2 rows untouched from v2. Spec-point mappings are the
  P3c lane-3 cross-map of record, landed `SUGGESTED` (AGENT.md rule 2; no coverage manufactured — 24 honest
  non-overlaps) with `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-3. Rights ©
  Cambridge/UCLES/MAT/UKMT/O&C per file; takedown law unchanged. Base commit cb947595 (syllabai-experimental).

- **T-UGM-MODE1-4 — UGM mode-1 lane enrichment, Circular measure lane (this run)**: fifth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Enrichment/` lane family to CIE 9709 P1
  subtopic 1.4 Circular measure under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md`
  Amendment 2026-10-23; operator instruction "extend channel 4"). New file
  `cie-a-level-maths-20-pure-1-circular-measure.json`: the **first strand lane** (no dedicated UGM station) —
  hub-spine parse fragment 1.4.1a folded into parent code 1.4.1 of record (spine export keeps both rows
  verbatim); corpus-wide sweep of all 25 stations (855 resources → 62 candidates) resolved as 17 aligned
  (3 new-text + 14 cross-lane circles-strand facts re-verdicted from lane 3's parked "1.4 territory"
  non-overlaps, incl. 2 one-to-many extensions of lane-3 1.3.2 rows) + 4 explicit non-overlaps + 41 routed to
  recorded homes with reasons — never forced (AGENT.md rule 3); clause-a (radian definition/conversion) corpus
  gap recorded, not filled; primary pick r5534 (Cambridge Colleges 1952 Q7). Cross-lane rows carry
  `textOfRecordUnder` pointers (corpus importer forbids duplicate `ugmId`s across lanes). FACTS ONLY: slugs/
  titles/types/levels/confidence/provenance — no UGM text bodies; rights © Cambridge/UCLES/MAT/Cambridge
  Colleges/O&C/NRICH unchanged (licensing block in-file + dir README). Mode-2 rendering remains dropped
  (operator directive 2026-10-22, recorded in `mode2Note`). Base commit b52cf1bf (syllabai-experimental).

- **T-UGM-IMPORT-4 — UGM text corpus import, Circular measure lane (this run)**: fifth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Resources/` corpus family to its
  fourth lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23). New
  `UGM-Resources/pure-1-circular-measure/`: **text bodies of the 5 new-text strand resources**
  (r5534, problem-areas, r8936 aligned to 1.4.1; circular-slice, r7115 as recorded boundary non-overlaps) as
  YAML-front-matter markdown. Text-only import law: math preserved byte-true in UGM's native `\( \)` /
  `\[ \]` delimiters (converter verified byte-identical against four of-record lane-1/3 files before
  generation: belt, r6164, sector-spirals, r6638; per-file delimiter parity audited 5/5); UGM section
  structure/panel titles/provider spellings preserved; figures and the GeoGebra embed recorded as
  front-matter/inline markers, NOT fetched. `MANIFEST.json` bumps to **v4**: lane-4 block fresh (5 rows,
  sha256 each), lane-1/2/3 rows untouched from v3 (187 files corpus-wide). Spec-point mappings are the P3c
  lane-4 cross-map of record, landed `SUGGESTED` (AGENT.md rule 2; no coverage manufactured — clause-a gap +
  non-overlaps + routings recorded) with `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-4.
  Rights © Cambridge/UCLES/MAT/Cambridge Colleges/O&C per file; takedown law unchanged. Base commit
  b52cf1bf (syllabai-experimental).

- **T-UGM-MODE1-5 — UGM mode-1 lane enrichment, Trigonometry lane (this run)**: sixth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Enrichment/` lane family to CIE 9709 P1
  subtopic 1.5 Trigonometry under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment
  2026-10-23; operator instruction "lane 5"). New file `cie-a-level-maths-20-pure-1-trigonometry.json`: the
  **two-station lane** (UGM's dedicated Trigonometry: Triangles to Functions + Trigonometry: Compound Angles
  stations) — spine rows 1.5.1–1.5.5 verbatim (no fold fragments, unlike lanes 3–4); corpus-wide sweep of all
  25 stations (855 resources → 299 candidates) resolved as 41 aligned (36 TTF + 3 TCA substrate + 2
  cross-station strays r7912/r7184; 55 alignment rows; primary picks going-round-in-circles / trig-tables /
  inverse-or-not / r5269 / r6138) + 36 explicit non-overlaps + 2 cross-lane fact joins (r9924, r8411 → 1.5.4
  against lane-2 bodies, `textOfRecordUnder` pointers) + 220 routed to recorded homes with reasons — never
  forced (AGENT.md rule 3). FINDING OF RECORD: the compound-angles station maps almost entirely to P3 2.3
  (24 non-overlaps) — the 2019 CIE revision moved compound/double-angle work out of Pure 1; five of lane 4's
  routed-1.5 preview pool are refined here to non-overlaps (preview was a substrate pointer, never a verdict).
  FACTS ONLY: slugs/titles/types/levels/confidence/provenance — no UGM text bodies; rights © Cambridge/UCLES/
  MAT/O&C and other boards per row unchanged (licensing block in-file + dir README). Mode-2 rendering remains
  dropped (operator directive 2026-10-22, recorded in `mode2Note`). Base commit f3ef5745 (syllabai-experimental).

- **T-UGM-IMPORT-5 — UGM text corpus import, Trigonometry lane (this run)**: sixth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Resources/` corpus family to its
  fifth lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23). New
  `UGM-Resources/pure-1-trigonometry/`: **text bodies of the WHOLE two-station substrate — 77 files** (41
  mapped: 36 TTF + 3 TCA + 2 strays; 36 recorded non-overlaps imported UNMAPPED with the coverage note, per
  the station-lane corpus law; 8 excerpt/title-only captures per the of-record bigger-picture/teacher-support
  law) as YAML-front-matter markdown. Text-only import law: math preserved byte-true in UGM's native
  `\( \)` / `\[ \]` delimiters (converter verified byte-identical against four of-record lane-1/3 files
  before generation: belt, r6164, sector-spirals, r6638; per-file delimiter parity audited 77/77); UGM section
  structure/panel titles/provider spellings preserved; figures and GeoGebra embeds recorded as
  front-matter/inline markers, NOT fetched. `MANIFEST.json` bumps to **v5**: lane-5 block fresh (77 rows,
  sha256 each), lane-1/2/3/4 rows untouched from v4 (264 files corpus-wide). Spec-point mappings are the P3c
  lane-5 cross-map of record, landed `SUGGESTED` (AGENT.md rule 2; no coverage manufactured — non-overlaps +
  routings recorded) with `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-5. Rights ©
  Cambridge/UCLES/MAT/O&C per file; takedown law unchanged. Base commit f3ef5745 (syllabai-experimental).

- **T-UGM-MODE1-6 — UGM mode-1 lane enrichment, Series lane (this run)**: seventh landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Enrichment/` family to its sixth
  lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23; operator
  instruction "lane 6 (CIE 9709 P1 1.6 Series)"). New file `cie-a-level-maths-20-pure-1-series.json`: the
  **second two-station lane** (UGM's dedicated Sequences + Counting and Binomials stations) — spine rows
  1.6.1–1.6.4 verbatim (no fold fragments); corpus-wide sweep of all 25 stations (855 resources → 137
  candidates) resolved as 49 aligned (43 substrate — 31 Sequences + 12 Counting-and-Binomials — plus 6
  cross-station strays r5640/r9404/r9916/r8260/r6592/r9312; 56 alignment rows; primary picks r7078 /
  sort-it-out / r8907 / square-spirals) + 50 explicit non-overlaps + 2 cross-lane fact joins (r7553, r9527
  → 1.6.3 against lane-2 bodies, `textOfRecordUnder` pointers) + 36 routed to recorded homes with reasons —
  never forced (AGENT.md rule 3). FINDINGS OF RECORD: the Sequences station maps 31/42 onto 1.6.2–1.6.4
  while Counting and Binomials is dominated by combinatorics/logic work (39 non-overlaps) around a tight
  binomial-expansion core (12/51); the general-index binomial questions (r6295/r6340/r7477 substrate
  non-overlaps + power-series r7436/r6601 routed) carry P3 Series bearings — the natural substrate preview
  for a future P3 lane, mirroring lane 5's P3 2.3 finding. FACTS ONLY: slugs/titles/types/levels/
  confidence/provenance — no UGM text bodies; rights © Cambridge/UCLES/MAT/O&C and other boards per row
  unchanged (licensing block in-file + dir README). Mode-2 rendering remains dropped (operator directive
  2026-10-22, recorded in `mode2Note`). Base commit 82964ce4 (syllabai-experimental).

- **T-UGM-IMPORT-6 — UGM text corpus import, Series lane (this run)**: seventh landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Resources/` corpus family to its
  sixth lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23).
  New `UGM-Resources/pure-1-series/`: **text bodies of the WHOLE two-station substrate — 99 files** (49
  mapped: 43 substrate + 6 strays; 50 recorded non-overlaps imported UNMAPPED with the coverage note, per
  the station-lane corpus law; 3 excerpt/title-only captures per the of-record bigger-picture/teacher-support
  law) as YAML-front-matter markdown. Text-only import law: math preserved byte-true in UGM's native
  `\( \)` / `\[ \]` delimiters (converter verified **byte-identical against all 77 of-record lane-5
  files** before generation — full-corpus verification, extending the four-file lane-5 check; per-file
  delimiter parity audited 99/99); UGM section structure/panel titles/provider spellings preserved; figures
  and GeoGebra embeds recorded as front-matter/inline markers, NOT fetched. `MANIFEST.json` bumps to **v6**:
  lane-6 block fresh (99 rows, sha256 each), lane-1/2/3/4/5 rows untouched from v5 (363 files corpus-wide).
  Spec-point mappings are the P3c lane-6 cross-map of record, landed `SUGGESTED` (AGENT.md rule 2; no
  coverage manufactured — non-overlaps + routings recorded) with `primaryPick` cross-referenced to
  `UGM-Enrichment/` T-UGM-MODE1-6. Rights © Cambridge/UCLES/MAT/O&C per file; takedown law unchanged.
  Base commit 82964ce4 (syllabai-experimental).

- **T-UGM-MODE1-7 — UGM mode-1 lane enrichment, Differentiation lane (this run)**: eighth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Enrichment/` family to its seventh
  lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23; operator
  instruction "Proceed Lane 7"). New file `cie-a-level-maths-20-pure-1-differentiation.json`: the **third
  two-station lane** (UGM's dedicated Introducing Calculus + Calculus of Powers stations) — spine rows
  1.7.1–1.7.4 verbatim (no fold fragments); corpus-wide sweep of all 25 stations (855 resources → 195
  candidates) resolved as 74 aligned (40 substrate — 9 Introducing-Calculus + 31 Calculus-of-Powers — plus 34
  cross-station strays; 107 alignment rows; primary picks r7692 / r9942 / r8065 / r9260) + 32 explicit
  non-overlaps + 3 cross-lane fact joins (r5640 vs lane 6; r7115, r8936 vs lane 4 — `textOfRecordUnder`
  pointers; the lane-4 non-overlap row for r7115 explicitly names 1.7 as the tested skill) + 86 routed to
  recorded homes with reasons — never forced (AGENT.md rule 3). FINDINGS OF RECORD: Calculus of Powers is the
  P1 workhorse (31/48 aligned — power rule with rational indices, tangents/normals, stationary points,
  canonical optimisations) while Introducing Calculus splits between gradient-concept building blocks (the
  zoom-in chord-limit construct) and the honest trapezium-rule/kinematics non-overlap cluster (15) — the
  trapezium rule is not in the 2023–2025 P1 spec; the chain-rule, product-rule and calculus-trig-log stations
  are P3-bearing (general chain rule with non-linear inner functions, product/quotient rule, trig/exp/log
  derivatives, parametric and implicit differentiation) — the natural substrate preview for future P3 lanes,
  mirroring lanes 5–6's P3 findings; lane 6's four 1.7 routing pointers are all resolved (r7692/r6509/r6920
  aligned, r5348/r9484 routed with P3 bearings). FACTS ONLY: slugs/titles/types/levels/confidence/
  provenance — no UGM text bodies; rights © Cambridge/UCLES/MAT/O&C and other boards per row unchanged
  (licensing block in-file + dir README). Mode-2 rendering remains dropped (operator directive 2026-10-22,
  recorded in `mode2Note`). Base commit 764ae1f9 (syllabai-experimental).

- **T-UGM-IMPORT-7 — UGM text corpus import, Differentiation lane (this run)**: eighth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Resources/` corpus family to its
  seventh lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23).
  New `UGM-Resources/pure-1-differentiation/`: **text bodies of the WHOLE two-station substrate — 106 files**
  (72 new-text substrate resources — 24 Introducing-Calculus + 48 Calculus-of-Powers, the 3 already-of-record
  Introducing-Calculus resources excluded — 40 mapped + 32 recorded non-overlaps imported UNMAPPED with the
  coverage note, per the station-lane corpus law; plus 34 mapped cross-station strays; 4 excerpt/title-only
  captures per the of-record bigger-picture/teacher-support law) as YAML-front-matter markdown. Text-only
  import law: math preserved byte-true in UGM's native `\( \)` / `\[ \]` delimiters (converter verified
  **byte-identical against all 99 of-record lane-6 files** before generation — full-corpus verification,
  extending the 77-file lane-5 and lane-6 checks; per-file delimiter parity audited 106/106); UGM section
  structure/panel titles/provider spellings preserved; figures and GeoGebra embeds recorded as
  front-matter/inline markers, NOT fetched. `MANIFEST.json` bumps to **v7**: lane-7 block fresh (106 rows,
  sha256 each), lane-1/2/3/4/5/6 rows untouched from v6 (469 files corpus-wide). Spec-point mappings are the
  P3c lane-7 cross-map of record, landed `SUGGESTED` (AGENT.md rule 2; no coverage manufactured —
  non-overlaps + routings recorded) with `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-7.
  Rights © Cambridge/UCLES/MAT/O&C per file; takedown law unchanged. Base commit 764ae1f9
  (syllabai-experimental).

- **T-UGM-MODE1-7 amendment (this run)**: station-scope census correction — `coverage.stationBreakdown`
  introducing-calculus `nonOverlap` 18 → **15**, aligning the per-station breakdown with the census of
  record (32 recorded non-overlaps = 15 Introducing-Calculus + 17 Calculus-of-Powers per `nonOverlapRows`,
  `stationScope.stations`, the PR #91 body and this LEDGER's T-UGM-MODE1-7 entry above). The 3
  already-of-record Introducing-Calculus resources (r6592, r7912, problem-areas) had been bucketed as
  station non-overlaps in the breakdown only; no row, body, mapping, or census of record changes —
  74 aligned / 107 rows / 32 non-overlaps / 3 cross-lane joins / 106 files unchanged. Caught by the hub
  importer's fail-closed stationScope↔stationBreakdown equality audit (T-UGM-HUB-CONSUME-7 pre-flight);
  the corpus-side build audit checked the census aggregates but not the per-station sc↔bk equality the
  importer enforces.

- **T-UGM-MODE1-8 — UGM mode-1 lane enrichment, Integration lane (this run)**: ninth landing from the
  Underground Mathematics reverse-engineering track, extending the `UGM-Enrichment/` family to its eighth
  lane under the same operator attestation of 2026-10-23 (`LICENSE-DATA.md` Amendment 2026-10-23; operator
  instruction: next lane per `INTEGRATION-PLAN.md` — 1.8 Integration). New file
  `cie-a-level-maths-20-pure-1-integration.json`: the **first strand lane on a spec section** (lane-4
  shape applied to 1.8, which has no dedicated UGM station — the substrate is the seven-station calculus
  family whose dedicated stations are fully of record via lanes 5–7) — spine rows 1.8.1–1.8.4 verbatim
  (no fold fragments); corpus-wide integration sweep of all 25 stations (855 resources → 91 candidates)
  resolved as 28 aligned (10 new-text strand — 7 calculus-meets-functions + 2 chain-rule + 1 product-rule —
  plus 18 cross-lane fact joins to `pure-1-differentiation/` bodies: 13 flipping the lane-7
  Calculus-of-Powers non-overlaps of record with reasons retained, 5 one-to-many beside standing 1.7
  alignments; 28 alignment rows; primary picks r8716 / r7734 / r6067 / r9357) + 0 new non-overlaps +
  32 routed (P3-technique honesty: trig/log/exp antiderivatives, substitution, parts, partial fractions
  are P3, not P1 1.8) + 31 rejected with reasons (trapezium-rule family not in the 9709 P1 spine; marker
  false positives; teacher-supports) — never forced (AGENT.md rule 3). FINDINGS OF RECORD: lane 7's
  "integration-dressed honesty" deferral is realised — 13 of 17 Calculus-of-Powers non-overlaps flip to
  1.8.x alignments (area-definite-integral and volume-of-revolution cores) while the 15
  Introducing-Calculus trapezium-rule/kinematics non-overlaps stay unmapped of record; the 9709 P1 1.8
  coverage is area/volume-dominated (12 of 28 rows are 1.8.4) and reverse-process/constant-of-integration
  coverage is thin (2 + 4 rows) — the honest shape of a station family built for differentiation-first
  teaching. Text of record: 10 new files under `UGM-Resources/pure-1-integration/` (T-UGM-IMPORT-8,
  below) with `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-8.

- **T-UGM-IMPORT-8 — UGM text corpus import, Integration lane (this run)**: ninth landing; the
  `UGM-Resources/` corpus grows by the `pure-1-integration/` directory — **10 files, all mapped**
  (strand-lane corpus law: new text only, no unmapped imports; the cross-lane 1.8 mappings live as facts
  in the enrichment with `textOfRecordUnder` pointers at `pure-1-differentiation/`). MANIFEST advances
  **v7 → v8** (file_count 469 → 479; lanes 1–7 rows carried forward untouched). Capture provenance:
  syllabai-experimental @ c04abfbd (cross-map lane 8 in the same commit). Rights © Cambridge/UCLES/MAT/O&C
  per file; takedown law unchanged. Base commit dc5ff598 (syllabai-experimental).

- **T-UGM-MODE1-8 amendment — crossLaneAligned primary-pick flags (this run)**: consume-phase facts-file
  fix for `T-UGM-HUB-CONSUME-8` (the T-UGM-MODE1-7 amendment pattern): the lane-8 enrichment declared its
  four 1.8 primary picks (r8716 → 1.8.1, r7734 → 1.8.2, r6067 → 1.8.3, r9357 → 1.8.4) on the
  `perSpecPoint` rows only, but all four picks ride the CROSS-LANE join — the first lane whose pick set
  is entirely joined text — and the hub importer's join law serves per-resource pick flags from the
  `crossLaneAligned` rows. The regenerated hub bundle therefore declared index-level picks that no
  resource row knew, failing the hub regression law's "every declared spec-point primaryPick resolves to
  a resource that knows it" invariant for all four 1.8 codes (an audit gap: the corpus-side build audit
  cross-checked pick membership but not cross-lane pick-flag parity with the perSpecPoint declarations).
  Amendment: the four `crossLaneAligned` rows gain `"primaryPick": true` — nothing else moves
  (perSpecPoint rows, censuses, sweep routing, texts and MANIFEST v8 untouched; 18 joins still 18, 28
  rows still 28). Unblocks T-UGM-HUB-CONSUME-8 at the amendment merge.

- **T-UGM-ASSETS-1 — UGM static-figure asset import (this run)**: tenth landing; the UGM corpus
  family gains its **image plane**. 976 static figures (37.7 MB, PNG/SVG) under `UGM-Assets/`,
  paths mirroring the live site (`<station>/<resource>/images/<file>`), per-file SHA-256 identity in
  `UGM-Assets/MANIFEST.json`; the figure map of record `UGM-Resources/figures-map.json` carries
  **1,233 figure occurrences across 275 resources**, each anchored to a body section name (cross-check:
  0 unmatched against body `##` headings) with a per-section ordinal (0 collisions). **Text bodies are
  byte-untouched** — the corpus conversion laws of record stay exact; images travel as first-class data
  (map + binaries), not as body re-conversions (the lanes 1–4 converter-era drift made body rewrites
  the wrong instrument; the map keeps `T-UGM-ASSETS-1` surgical). The hub consumer
  (`T-UGM-HUB-CONSUME-8a`) copies referenced files to `apps/hub/public/ugm-assets/` and injects figure
  references into the served bundle at deterministic section positions — the same index→row class of
  transform the T-UGM-MODE1-8 amendment established for pick flags. Scope of record: static images
  only — GeoGebra interactive embeds and printable/component PDFs stay excluded (Amendment 2026-10-23
  scope note carried forward); assets referenced only by solution/teacher-support variant pages outside
  the corpus sections are likewise excluded. Rights: operator attestation of 2026-10-24 — see
  `LICENSE-DATA.md` (Amendment 2026-10-24); © Cambridge/UCLES unchanged; takedown law unchanged.
  MANIFEST advances **v8 → v9** (lanes 1–8 rows and file_count 479 untouched; `assets` block + version
  note appended).

- **T-UGM-MODE1-9 — UGM mode-1 lane enrichment, Pure 3 Algebra lane (this run)**: tenth landing from the
  UGM corpus, and the **first lane on the pure-3 course plane** (`course: cie-a-level-maths-20-pure-3`).
  Target of record: CIE 9709 Pure 3 subtopic 3.1 Algebra, spec points 3.1.1–3.1.6, verbatim from the
  repaired hub spine parse (the parse warning documents `T-SPECS-CIE-PARSE-REPAIR-1`: official 2.1.1 split
  into the 3.1.1 meaning/graph limb + 3.1.2 relations limb; official bullets 2–5 recovered as 3.1.3–3.1.6) —
  no fold fragments. Facts file of record:
  `UGM-Enrichment/cie-a-level-maths-20-pure-3-algebra.json` (task `T-UGM-MODE1-9`, review_state SUGGESTED).
  Corpus sweep 855 → 97 raw hits → 90 candidates (deduped) → **47 aligned rows** (38 fresh rows over 35
  substrate resources + 9 cross-lane rows: 5 flips — r8427 from the lane-2 non-overlaps, r5245/r6295/r6340/r7477
  from the lane-6 non-overlaps whose P3 bearings were recorded at lane 6 — and 4 one-to-many joins r5362/r9523
  (lane-2), r9082 (lane-7), r9701 (lane-8), all riding bodies of record, join law unchanged) **+ 16 fresh
  non-overlaps recorded by reference only** (`bodyImported: false`, the lane-8 candidate-model law: no text
  import for resources whose tested skill sits outside the lane) **+ 30 of-record candidates rejected with
  reasons** (the integer-index binomial pool stays 1.6.1 of record — 3.1.6 is the rational-index `|x| < 1`
  expansion, realising the lane-6 P3 preview; the surd/distance squaring pool stays 1.1.x/1.3.2; vector norms
  are not scalar modulus). Primary picks of record: absolutely (3.1.1) / inequalities (3.1.2) / whats-left
  (3.1.3) / r6577 (3.1.4) / r7792 (3.1.5) / r7436 (3.1.6). Cross-map of record:
  `undergroundmathematics/resources/derived/cross-map-algebra.json` + narrative
  `undergroundmathematics/docs/cross-map-algebra.md` @ syllabai-experimental 3098d8eb.
  Text of record: 35 new files under `UGM-Resources/pure-3-algebra/` (T-UGM-IMPORT-9, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-9.
- **T-UGM-IMPORT-9 — UGM text corpus import, Pure 3 Algebra lane (this run)**: tenth landing; the
  candidate-model law continues (lane-8 shape): 35 fresh 3.1-bearing resources corpus-wide, converted from
  `ugm-clean` through the byte-proven converter (pre-flight: 10/10 byte-identity against the lane-8 of-record
  bodies), fm planes `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task:
  T-UGM-IMPORT-9`, `examProvenance` = acknowledgement first line verbatim (42/35... 24 of 35 carry
  acknowledgements). Filenames `{ugm_id}-{title-slug}.md` under the majority slug law (fitted 360/479
  against the fleet; of-record filename space is non-uniform across the lost lane builds — `ugm_id` remains
  the only join key). MANIFEST v10 (lane-9 block appended; lane-1..8 rows + v9 assets untouched;
  file_count 479 → 514). Fleet audits: sha256 35/35, delimiter parity 35/35, fm↔enrichment membership
  38/38 fresh rows, primaryPick 6/6 unique, 0 `ugm_id` collisions against lanes 1–8.

- **T-UGM-MODE1-10 — UGM mode-1 lane enrichment, Pure 3 Log-and-Exp lane (this run)**: eleventh landing from the
  UGM corpus, and the **second lane on the pure-3 course plane** (`course: cie-a-level-maths-20-pure-3`).
  Target of record: CIE 9709 Pure 3 subtopic 3.2 Logarithmic and exponential functions, spec points 3.2.1–3.2.4,
  verbatim from the hub spine parse (the dropped-math artifacts in the 3.2.2/3.2.3 titles are carried verbatim;
  no `T-SPECS` repair needed) — no fold fragments. Facts file of record:
  `UGM-Enrichment/cie-a-level-maths-20-pure-3-logarithmic-and-exponential-functions.json` (task `T-UGM-MODE1-10`, review_state SUGGESTED).
  Corpus sweep 855 → 71 raw hits → 71 candidates (pass-1 title/description + pass-2 body-text sweeps) →
  **39 aligned rows** (34 fresh rows over 34 substrate resources, all single-code + 5 cross-course rows: one-to-many
  joins r9824/r7607 (lane-2 functions), r6137/r8260 (lane-6 series), r7184 (lane-5 trigonometry), all riding bodies
  of record, join law unchanged; no flips) **+ 26 fresh non-overlaps recorded by reference only**
  (`bodyImported: false` — the lane-8 candidate-model law) **+ 6 of-record candidates rejected with reasons**.
  The dedicated exp-and-log station is the workhorse (31 of 34 fresh; it held only 2 of-record resources before
  this lane); the lane-5 pre-baked "2.2 Logarithmic and exponential functions" bearings land here (9 of 10 aligned);
  the 3.2.2 e/ln limb is structurally thin (2 fresh + 1 join — UGM's e/ln corpus rides the lane-7/8 recorded P3
  3.4/3.5 bearings, which stand); the lane-9 `to-log-or-not-to-log` nonOverlapByReference row flips to aligned
  (3.2.3 pick). Primary picks of record: proving-laws-of-logs (3.2.1) / an-irrational-inequality (3.2.2) /
  to-log-or-not-to-log (3.2.3) / how-far-did-the-earth-move (3.2.4). Cross-map of record:
  `undergroundmathematics/resources/derived/cross-map-log-and-exp.json` + narrative
  `undergroundmathematics/docs/cross-map-log-and-exp.md` @ syllabai-experimental 980556af.
  Text of record: 34 new files under `UGM-Resources/pure-3-logarithmic-and-exponential-functions/` (T-UGM-IMPORT-10, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-10.
- **T-UGM-IMPORT-10 — UGM text corpus import, Pure 3 Log-and-Exp lane (this run)**: eleventh landing; the
  candidate-model law continues (lane-8/9 shape): 34 fresh 3.2-bearing resources, converted from `ugm-clean`
  through the byte-proven converter (pre-flight: **45/45 byte-identity against the lane-8 AND lane-9 of-record
  bodies**), fm planes `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task: T-UGM-IMPORT-10`,
  `examProvenance` = acknowledgement first line verbatim (22 of 34 carry acknowledgements). Filenames
  `{ugm_id}-{title-slug}.md` under the majority slug law (the of-record filename space is non-uniform across
  the lost lane builds — `ugm_id` remains the only join key). MANIFEST v11 (lane-10 block appended; lane-1..9 rows
  + v9 assets untouched; file_count 514 → 548). Fleet audits: sha256 34/34, delimiter parity 34/34, fm↔enrichment
  membership 34/34 fresh rows, primaryPick 4/4 unique, 0 `ugm_id` collisions against lanes 1–9.

- **T-UGM-MODE1-11 — UGM mode-1 lane enrichment, Pure 3 Trigonometry lane (this run)**: twelfth landing from the
  UGM corpus, and the **third lane on the pure-3 course plane** (`course: cie-a-level-maths-20-pure-3`) — the
  **first mostly-mapping lane**. Target of record: CIE 9709 Pure 3 subtopic 3.3 Trigonometry, spec points
  3.3.1–3.3.2, verbatim from the hub spine parse (the parse artifacts in the 3.3.2 title — dropped math runs in
  the R-form/Pythagorean bullets and the mid-sentence truncation — are carried verbatim; no `T-SPECS` repair
  needed) — no fold fragments. Facts file of record:
  `UGM-Enrichment/cie-a-level-maths-20-pure-3-trigonometry.json` (task `T-UGM-MODE1-11`, review_state SUGGESTED).
  Corpus sweep 855 → 110 raw hits → 103 candidates (17 pass-1 title/description + 93 pass-2 body-text; 102 unique
  regex candidates + 1 pre-baked bearing r9740 the regex cannot reach) → **28 aligned rows** = 1 fresh row
  (r7616 → 3.3.1) + **27 cross-course rows by reference** (23 flips: the lane-5 pre-baked "P3 2.3" pool rows are
  lane-5 non-overlaps whose whole-station bodies of record live under `pure-1-trigonometry/` — the two-station
  lane law — so they flip to 3.3.2 by reference under the lane-9 flip law; 4 one-to-many: going-round-in-circles/
  muddled-trig/trig-tables (3.3.1) and r7021 (3.3.2) beside standing 1.5.x alignments; no flips of pure-3 rows,
  nothing duplicated) **+ 42 fresh non-overlaps recorded by reference only** (`bodyImported: false`; 9 riding
  prior bodies per the supersede law) **+ 33 of-record candidates rejected with reasons**. Primary picks of
  record: r7616 (3.3.1, fresh) / r6018 (3.3.2, rides a reference row — disclosed of record). Cross-map of record:
  `undergroundmathematics/resources/derived/cross-map-p3-trigonometry.json` + narrative
  `undergroundmathematics/docs/cross-map-p3-trigonometry.md` @ syllabai-experimental 4dbd50d5 (incl. the
  body-of-record correction commit — the first cross-map landed before the whole-import audit; corrected
  same-session per the lane-6/7 correction precedent).
  Text of record: 1 new file under `UGM-Resources/pure-3-trigonometry/` (T-UGM-IMPORT-11, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-11.
- **T-UGM-IMPORT-11 — UGM text corpus import, Pure 3 Trigonometry lane (this run)**: twelfth landing; the
  candidate-model law continues (lane-8/9/10 shape) with the lane-8 join law for the by-reference rows:
  1 fresh 3.3-bearing resource (r7616), converted from `ugm-clean` through the byte-proven converter (pre-flight:
  **79/79 byte-identity against the lane-8, lane-9 AND lane-10 of-record bodies**), fm planes
  `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task: T-UGM-IMPORT-11`,
  `examProvenance` in the enrichment/cross-map rows = acknowledgement first line verbatim. Filename
  `{ugm_id}-{title-slug}.md` under the lane-9 slug law (re-proved 35/35 against the lane-9 filenames; `<`/`>`
  join the dropped relation-symbol vocabulary). MANIFEST v12 (lane-11 block appended; lane-1..10 rows + v9 assets
  untouched; file_count 548 → 549). Fleet audits: sha256 1/1, delimiter parity 1/1, fm↔enrichment membership
  28/28 aligned rows (1 fresh + 27 by-reference), primaryPick 2/2 unique, 0 `ugm_id` collisions against lanes
  1–10, all 27 by-reference rows verified against the body map of record.

- **T-UGM-MODE1-12 — UGM mode-1 lane enrichment, Pure 3 Differentiation lane (this run)**: thirteenth landing
  from the UGM corpus, and the **fourth lane on the pure-3 course plane** (`course: cie-a-level-maths-20-pure-3`)
  — the **largest fresh-text lane since lane 9**. Target of record: CIE 9709 Pure 3 subtopic 3.4 Differentiation,
  spec points 3.4.1–3.4.3, verbatim from the hub spine parse (the parse artifacts — the dropped math run on `e`
  and the duplicated "tan x" in the 3.4.1 title; the dangling "e.g." in the 3.4.2 and 3.4.3 titles — are carried
  verbatim; no `T-SPECS` repair needed) — no fold fragments. Lane identity named of record by the lane-11
  bookkeeping next pointer ("next: 3.4 via the lane-11 P3-3.4 routings" @ `b2c31f9d`). Facts file of record:
  `UGM-Enrichment/cie-a-level-maths-20-pure-3-differentiation.json` (task `T-UGM-MODE1-12`, review_state
  SUGGESTED). Corpus sweep 855 → 189 candidates (pass-1 title/description + pass-2 section-text, plus the 21
  pre-baked lane-10/11 "P3 3.4 Differentiation" bearing rows — 11 from lane-10 incl. the two dual "P3 3.4/3.5"
  routings, 11 from lane-11, odd-one-out recorded in both) → **41 aligned rows** = 40 fresh rows over 40
  substrate resources (single-code each: 13 × 3.4.1, 12 × 3.4.2, 15 × 3.4.3) + **1 cross-course flip by
  reference** (r8931 → 3.4.2, the lane-7 non-overlap row whose whole-station body of record lives under
  `pure-1-differentiation/` — the two-station lane law — flipping under the lane-9 flip law; no one-to-many
  joins this lane: the lane-7 P1 alignments already hold the tangent/normal/optimisation embodiments) **+ 29
  fresh non-overlaps recorded by reference only** (`bodyImported: false`; 3 honest re-routings of lane-10
  bearings: r6620 and r8134 from the dual "P3 3.4/3.5" to 3.5, differentiating-exponentials declined for no
  extractable sections of record) **+ 119 of-record candidates rejected with reasons** (104 aligned of record
  under lanes 1–11 — dominated by lane-7's P1-differentiation law — and 15 standing prior non-overlap rows,
  incl. the two declined bearings odd-one-out and r6843). Of the 21 unique pre-baked bearing rows of record
  (11 lane-10 rows incl. the two dual "P3 3.4/3.5" routings + 11 lane-11 rows, odd-one-out recorded in both):
  16 promoted to aligned fresh bodies (7 of the lane-10 rows, 9 of the lane-11 rows), each superseding its
  stale row of record per the to-log-or-not-to-log law; 5 closed otherwise (2 dual rows re-routed to 3.5, 1
  declined for no extractable text, 2 declined on the merits). Primary picks of record: r6938 (3.4.1, fresh) /
  r6530 (3.4.2, fresh) / r8620 (3.4.3, fresh) — the fresh-pick convention holds. Cross-map of record:
  `undergroundmathematics/resources/derived/cross-map-p3-differentiation.json` + narrative
  `undergroundmathematics/docs/cross-map-p3-differentiation.md` @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4.
  Text of record: 40 new files under `UGM-Resources/pure-3-differentiation/` (T-UGM-IMPORT-12, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-12.
- **T-UGM-IMPORT-12 — UGM text corpus import, Pure 3 Differentiation lane (this run)**: thirteenth landing;
  the candidate-model law continues (lane-8/9/10/11 shape) with the lane-8 join law for the by-reference rows:
  40 fresh 3.4-bearing resources, converted from `ugm-clean` through the byte-proven converter (pre-flight:
  **80/80 byte-identity against the lane-8, lane-9, lane-10 AND lane-11 of-record bodies**), fm planes
  `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task: T-UGM-IMPORT-12`,
  `examProvenance` in the enrichment/cross-map rows = acknowledgement first line verbatim. Filename
  `{ugm_id}-{title-slug}.md` under the lane-9 slug law (re-proved **77/80** against the lane-8/9/10/11
  filenames — the three residuals are bare-underscore and command-brace constructs (`p_n` vs `f_k`,
  `\sqrt{...}` brace-keeping, `^{...}`-brace underscores) whose of-record treatment is internally
  inconsistent in the source data AND absent from the lane-12 title set; every construct class the lane-12
  titles exercise is verified against all of-record instances). MANIFEST v13 (lane-12 block appended;
  lane-1..11 rows + v9 assets untouched; file_count 549 → 589). Fleet audits: sha256 40/40, delimiter parity
  40/40, fm↔enrichment membership 40/40 fresh rows (both directions), primaryPick 3/3 unique all-fresh,
  0 `ugm_id` collisions against lanes 1–11, candidate closure exact 189 = 41 + 29 + 119, MANIFEST strictly
  additive (lanes 1–11 byte-identical).

- **T-UGM-MODE1-13 — UGM mode-1 lane enrichment, Pure 3 Integration lane (this run)**: fourteenth landing from the
  UGM corpus, and the **fifth lane on the pure-3 course plane** (`course: cie-a-level-maths-20-pure-3`) — the
  **first lane of record with an honest empty spec point**. Target of record: CIE 9709 Pure 3 subtopic 3.5
  Integration, spec points 3.5.1–3.5.6, verbatim from the hub spine parse (the parse artifacts in every row —
  interleaved/dropped math runs and fragments, incl. the 'k f l ^ x h' glyph debris in 3.5.3 — are carried
  verbatim; no `T-SPECS` repair needed) — no fold fragments. Facts file of record:
  `UGM-Enrichment/cie-a-level-maths-20-pure-3-integration.json` (task `T-UGM-MODE1-13`, review_state SUGGESTED).
  Corpus sweep 855 → 102 candidates (pass-1 title/description + pass-2 body-text, plus the 20 pre-baked
  lane-10/11/12 'P3 3.5 Integration' bearing rows) → **23 aligned rows** = 16 fresh rows (10 × 3.5.1 / 7 × 3.5.2 /
  3 × 3.5.3 / 0 × 3.5.4 / 6 × 3.5.5 / 9 × 3.5.6 by psp membership; 15 of the fresh rows promotions of the bearing
  pool, each superseding its stale row of record) + 1 cross-course flip (circular-slice → 3.5.6/3.5.2, riding its
  lane-4 body under `pure-1-circular-measure/`) + **6 one-to-many joins beside standing alignments of record**
  (r7616 → 3.5.1 riding the lane-11 3.3.1 pick; r8774 → 3.5.1 riding the lane-12 3.4.2 body — the bearing lane-12's
  own evidence disclosed; r9312 → 3.5.5 riding the lane-6 1.6.4 body — the twice-by-parts envelope integral;
  r9701 → 3.5.3/3.5.6 riding the lane-8 body; r8694 and r5126 → riding lane-9 bodies) **+ 11 fresh non-overlaps
  recorded by reference only** (`bodyImported: false`; 5 superseding stale bearing rows of record — r6622, r7106,
  r7461, r7903, r8836 — each declined honestly against its solution of record) **+ 68 of-record candidates rejected
  with reasons**. THE 3.5.4 GAP OF RECORD: no f'(x)/f(x) integration resource exists in the 25-station UGM corpus
  (the corpus-wide targeted sweep returned only rows already of record under other lanes); the spec point carries
  ZERO rows — no coverage is manufactured (rule 3, the lane-8 review-state law). Primary picks of record:
  r8679 (3.5.1, fresh) / r9297 (3.5.2, fresh) / r5126 (3.5.3 — rides its lane-9 body, the fresh-pick-impossible
  convention disclosed of record) / r8134 (3.5.5, fresh — the reduction-formula showcase) / r8890 (3.5.6, fresh —
  the exact CIE given-substitution task); 3.5.4 pick none (the honest gap). Cross-map of record:
  `undergroundmathematics/resources/derived/cross-map-p3-integration.json` + narrative
  `undergroundmathematics/docs/cross-map-p3-integration.md` @ syllabai-experimental 21845f3f.
  Text of record: 16 new files under `UGM-Resources/pure-3-integration/` (T-UGM-IMPORT-13, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-13.
- **T-UGM-IMPORT-13 — UGM text corpus import, Pure 3 Integration lane (this run)**: fourteenth landing; the
  candidate-model law continues (lane-8/9/10/11/12 shape) with the lane-8 join law for the by-reference rows:
  16 fresh 3.5-bearing resources, converted from `ugm-clean` through the byte-proven converter (pre-flight:
  **120/120 byte-identity against the lane-8/9/10/11/12 of-record bodies** — zero law drift across five lanes),
  fm planes `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task: T-UGM-IMPORT-13`,
  `examProvenance` in the enrichment/cross-map rows = acknowledgement first line verbatim. Filename
  `{ugm_id}-{title-slug}.md` under the lane-9 slug law (re-proved 117/120 against the of-record filenames; the
  same 3 source-data residuals as lane 12 — p_n/f_k subscripts, \sqrt brace-keeping, ^-brace underscores — all
  absent from every lane-13 title). MANIFEST v14 (lane-13 block appended; lane-1..12 rows + v9 assets untouched;
  file_count 589 → 605). Fleet audits: sha256 16/16, delimiter parity 16/16, fm↔enrichment membership 23/23
  aligned rows (16 fresh + 7 by-reference), primaryPick 5/5 unique non-gap codes, 0 `ugm_id` collisions against
  lanes 1–12. CLOBBER REPAIR OF RECORD: this run also restores the T-UGM-MODE1-12/T-UGM-IMPORT-12 LEDGER entries
  the #136 merge (e70a7140) had reverted — the bfd9a8f2 restore of record covered UGM-Resources/ + UGM-Enrichment/
  only and the root LEDGER.md reverted with the branch (recovered verbatim from the #134 head e75ba613; the
  #136/#133 failure mode's fourth documented occurrence, first root-level casualty).

- **T-UGM-MODE1-14 — UGM mode-1 lane enrichment, Pure 3 Numerical solution of equations lane (this run)**:
  fifteenth landing from the UGM corpus, and the **sixth lane on the pure-3 course plane** (`course:
  cie-a-level-maths-20-pure-3`). Target of record: CIE 9709 Pure 3 subtopic 3.6 Numerical solution of equations,
  spec points 3.6.1–3.6.3, verbatim from the served spine parse (SUB3.6 'Numerical solution of equations', orders
  22–24; parse artifacts carried verbatim; no `T-SPECS` repair needed) — no fold fragments. Facts file of record:
  `UGM-Enrichment/cie-a-level-maths-20-pure-3-iteration.json` (task `T-UGM-MODE1-14`, review_state SUGGESTED).
  Corpus sweep 855 → 48 candidates of record (tight pass-2 iteration/sign-change/convergence regex + pass-1
  title/description + four targeted angle patterns — decimal-places+root, rearrangement-form,
  trial-and-improvement, fixed-point, x=g(x), successive-approximations; NO pre-baked bearing pool this lane — no
  prior lane routed rows to 'P3 3.6') → **11 aligned rows** = 3 fresh rows (r8711 3.6.1 / r8013 3.6.1 /
  staircase-sequences 3.6.2+3.6.3) + **1 cross-course flip** (r8404 → 3.6.2/3.6.3, riding its lane-6 whole-station
  body under `pure-1-series/` whose `spec_points` were `[]` unmapped-by-design — the circular-slice precedent,
  first flip of record whose prior body carried no spec assertion) + **7 one-to-many joins beside standing
  alignments of record** (r8231 → 3.6.1/3.6.3 riding the 1.7.3 body — trial-and-improvement + the Newton-Raphson
  x_{n+1} formula to 3 d.p.; r8679 → 3.6.2/3.6.3 riding the lane-13 3.5.1 pick body — the numerical-canon survey +
  Newton-Raphson from first to second approximation; r7549 → 3.6.1 riding the 1.3.2 body — sign change + continuity
  to 1 d.p.; r5948 → 3.6.1 riding the 1.3.1/1.3.2 bodies — the chord-intercept linear-interpolation formula;
  to-log-or-not-to-log and see-the-power → 3.6.1 riding lane-10 bodies (medium); r9082 → 3.6.1 riding the
  1.7.2/3.1.4 body (medium)) **+ 1 fresh non-overlap recorded by reference only** (`bodyImported: false`;
  staircase-sequences-revisited, the companion disclosure) **+ 36 of-record candidates rejected with reasons**.
  NO honest gap this lane: 3.6.1 carries 8 rows, 3.6.2 three, 3.6.3 four. Primary picks of record:
  r8711 (3.6.1, fresh — the purest sign-change search) / r8404 (3.6.2 — rides its lane-6 body, the r6018
  fresh-pick-impossible convention disclosed) / r8231 (3.6.3 — rides its lane-3 body, disclosed). Cross-map of
  record: `undergroundmathematics/resources/derived/cross-map-p3-iteration.json` + narrative
  `undergroundmathematics/docs/cross-map-p3-iteration.md` @ syllabai-experimental 2d93dd7d.
  Text of record: 3 new files under `UGM-Resources/pure-3-iteration/` (T-UGM-IMPORT-14, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-14.
- **T-UGM-IMPORT-14 — UGM text corpus import, Pure 3 Numerical solution of equations lane (this run)**:
  fifteenth landing; the candidate-model law continues (lane-8..13 shape): 3 fresh 3.6-bearing resources,
  converted from `ugm-clean` through the byte-proven converter (pre-flight: **136/136 byte-identity against ALL
  lane-8..13 of-record fresh bodies** — zero law drift across six lanes), fm planes
  `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task: T-UGM-IMPORT-14`,
  `examProvenance` in the enrichment/cross-map rows = acknowledgement first line verbatim. Filename
  `{ugm_id}-{title-slug}.md` under the lane-9 slug law (re-proved across the 136; the known source-data residuals
  absent from every lane-14 title). MANIFEST v14 (lane-14 block appended; lane-1..13 rows + v9 assets untouched;
  file_count 605 → 608). Fleet audits: sha256 3/3, delimiter parity 3/3, fm↔enrichment membership 11/11 aligned
  rows (3 fresh + 8 by-reference), primaryPick 3/3 unique, 0 `ugm_id` collisions against lanes 1–13.

- **T-UGM-MODE1-15 — UGM mode-1 lane enrichment, Pure 3 Vectors lane (this run)**:
  sixteenth landing from the UGM corpus, and the **seventh lane on the pure-3 course plane** (`course:
  cie-a-level-maths-20-pure-3`). Target of record: CIE 9709 Pure 3 subtopic 3.7 Vectors, spec points
  3.7.1–3.7.7, verbatim from the served spine parse (SUB3.7 'Vectors', orders 25–31; parse artifacts carried
  verbatim — interleaved/dropped math runs in the notation rows; no `T-SPECS` repair needed) — no fold
  fragments. Facts file of record: `UGM-Enrichment/cie-a-level-maths-20-pure-3-vectors.json` (task
  `T-UGM-MODE1-15`, review_state SUGGESTED). Corpus sweep 855 → **136 candidates of record** (pass-1
  title/description 'vector' + tight pass-2 vector-machinery regex + targeted angle patterns — foot of the
  perpendicular, scalar/dot product, projection, angle between lines, skew, shortest distance, ratio-section +
  a station-membership audit recovering make-it-equal/where-did-it-land/r7982; NO pre-baked bearing pool this
  lane — no prior lane routed rows to 'P3 3.7') → **20 aligned rows, ALL FRESH BODIES — the FIRST lane of
  record with zero cross-lane joins and zero flips** (the vector stations were never mapped by lanes 1–14:
  CIE pure-1 carries no vectors; vector-geometry 15 + combining-vectors 5): 3.7.1 hit-the-spot + r9629;
  3.7.2 hit-the-spot, r5992, r8215, r8573, r8704, r8798, r8339, r5153, r7285, r8565, r8456; 3.7.3 r9629,
  r8215, r7285, r9575, r6007; 3.7.4 lots-of-vector-lines, three-lines, vector-squares; 3.7.5 r6007,
  lots-of-vector-lines, three-lines, vector-squares; 3.7.6 r8456, r6493, r7272, r5813 — psp rows 29 =
  2/11/5/3/4/4; **6 non-overlaps recorded as companion disclosures** (`bodyImported: false`): the plane class
  (is-it-a-plane, r6006, r9794, r7187 — P3 3.7 is a lines-only syllabus), r5089 (the corpus's vector-product
  showcase, rejected BY the 3.7.7 exclusion note — first of record), r8828 (the common-perpendicular
  construction the 3.7.5 row excludes) **+ 110 of-record candidates rejected with reasons** (the
  coordinate-method line r5202/r9702/r8449 — the example language matches, the method does not; the mechanics
  class forces-as-vectors; the Euclidean/trig-graph noise). **THE DESIGNED HONEST GAP: 3.7.7 is the spec's own
  exclusion row** ('Knowledge of the vector product is not required.') and carries zero rows by rule — the
  second honest gap of record after 3.5.4, this time by design rather than corpus poverty. **PROMOTION of
  record: r8456** (the λ/μ position-vector intersection + scalar-product angle exam question) supersedes its
  stale lane-3-algebra non-overlap row (the r8013 precedent). Primary picks of record (all riding fresh
  bodies — no r6018-style disclosure needed): hit-the-spot (3.7.1) / r8215 (3.7.2) / r9575 (3.7.3) /
  lots-of-vector-lines (3.7.4) / three-lines (3.7.5) / r6493 (3.7.6). Cross-map of record:
  `undergroundmathematics/resources/derived/cross-map-p3-vectors.json` + narrative
  `undergroundmathematics/docs/cross-map-p3-vectors.md` @ syllabai-experimental 16c5f802.
  Text of record: 20 new files under `UGM-Resources/pure-3-vectors/` (T-UGM-IMPORT-15, below) with
  `primaryPick` cross-referenced to `UGM-Enrichment/` T-UGM-MODE1-15.
- **T-UGM-IMPORT-15 — UGM text corpus import, Pure 3 Vectors lane (this run)**:
  sixteenth landing; the candidate-model law continues (lane-8..14 shape): 20 fresh 3.7-bearing resources,
  converted from `ugm-clean` through the byte-proven converter (pre-flight: byte-identity against ALL lane-8..14
  of-record fresh bodies — 139 prior files — zero law drift across seven lanes), fm planes
  `curriculum_code: CIE-9709-P3-2023`, `lane: cie-a-level-maths-20-pure-3`, `task: T-UGM-IMPORT-15`,
  `examProvenance` in the enrichment/cross-map rows = acknowledgement first line verbatim. Filename
  `{ugm_id}-{title-slug}.md` under the lane-9 slug law (re-proved across the fleet; the known source-data
  residuals absent from every lane-15 title). MANIFEST v15 (lane-15 block appended; lane-1..14 rows + v9
  assets untouched; file_count 608 → 628). Fleet audits: sha256 20/20, delimiter parity 20/20, fm↔enrichment
  membership 20/20 aligned rows (all fresh), primaryPick 6/6 unique, 0 `ugm_id` collisions against lanes 1–14.
- **T-UGM-MODE1-16 — UGM lane 16 cross-map, Pure 3 3.8 Differential equations (this run)**:
  fifteenth landing; operator order "lane 16" (trace 1a1774f478685021); lane-15 closure of record named "next 3.8 (then
  3.9)". FIVE sweep angles over the 855-resource corpus (title/desc regex; full-text regex; formulation
  signatures; the type-10 review-question rate scan — exactly ONE RQ of 569 mentions a rate: r6959; manual
  dossier reads) → 53 candidates closed exactly: 2 aligned BOTH cross-lane joins (r6959 rides its
  pure-1-differentiation 1.7.3 body — part (i) formulates `dA/dt = 5`, integrates with the initial condition,
  interprets via the chain rule; r7410 rides its pure-1-integration 1.8.2 body — part (ii) writes the DE from
  the proportionality statement, integrates, evaluates the constant from `y(2)=1`) + 4 non-overlap
  companion disclosures (the modelling-recognition class picture-the-process-i/ii — cooling/decay/logistic
  narrated or matched, never formulated; the beyond-spec separable-DE class weight-pulling +
  from-parabolas-to-catenaries — genuine separable skeletons, cosec/arcosh/cosh execution outside the 9709
  function set) + 47 rejections with reasons (prior-alignment riders, register class, mechanics class,
  exponential-fluency class, no-calculus noise). THE ZERO-FRESH LANE OF RECORD — the mirror of lane 15.
  Corpus-boundary audits fail-closed: raw main pages 855/855 parity with the clean wells; the site's own
  differential-equations station verified EMPTY on the live API (0 resources, id 11, created 2015-11-04 —
  control probe: vector-geometry 27); zero '3.8' mentions across all 15 prior enrichments (no pre-baked
  bearings). Cross-map of record: `undergroundmathematics/resources/derived/cross-map-p3-differential-equations.json`
  + narrative `undergroundmathematics/docs/cross-map-p3-differential-equations.md` @ syllabai-experimental
  b3700b809a9421364a3ab00a49e0cc057817a2ae.
- **T-UGM-IMPORT-16 — UGM text corpus import, Pure 3 Differential equations lane (this run)**:
  seventeenth landing; the candidate-model law continues (lane-8..15 shape) with the ZERO-FRESH adaptation:
  NO new body files (`file_count` 628 → 628 unchanged; `pure-3-differential-equations/` not created), the 2
  aligned rows recorded as cross-lane joins with `textOfRecordUnder`/`ofRecordLane` pointers (r6018-style pick
  disclosure lane-wide), MANIFEST v16 → v17 (lane-16 block appended; lane-1..15 rows + v9 assets untouched;
  strictly additive). Enrichment `cie-a-level-maths-20-pure-3-differential-equations.json` (schema 1.0,
  SUGGESTED, 53 candidates closed exactly, stationScope five-station-plus-rejects, corpus-boundary
  disclosure carried). Both README lane-16 sections. Audits fail-closed ALL GREEN (closure exact
  53 = 2 + 4 + 47; MANIFEST additive; 0 collisions trivially; spine rows verbatim).

- **T-UGM-MODE1-17 — UGM lane 17 cross-map, Pure 3 3.9 Complex numbers (this run)**:
  sixteenth landing; operator order "eyeball+merge on #391 → the pure-3 hub serve spans 8 lanes →
  lane 17" (trace `1a177fc5081804bd`; the lane-16 closure named "3.9 Complex numbers is the natural
  lane 17 per the spine's remaining SUB3.9 row, with lane 16's corpus-boundary caution applying").
  FOUR sweep angles over the 855-resource corpus of record (title/desc regex; full-text 12-signature
  regex; the de Moivre / √(negative) / number-system angle; the pre-baked-bearing check — none exist
  in the 16 enrichments of record) → 43 candidates closed exactly: **0 aligned (the FIRST
  ZERO-ALIGNED lane of record), 1 companion disclosure (absurder — the a²+b²=(a+ib)(a−ib)
  conjugate-pair factorisation derived from i²=−1 as a solution aside; the lane-9 non-overlap row
  stands), 42 rejections with reasons** carrying the six registers of record (the conjugate-pair
  aside; the optional ±i substitution in r7243; the teacher-facing discriminant link in
  discriminating(+TS); the x=√−4 notational shorthand in two-way-algebra; the elsewhere-deferral in
  domain-and-range-dominoes; the named-never-executed method in r5927). THE CORPUS-BOUNDARY FINDING,
  TOTAL: the site's complex-numbers substrate was never published — complex-numbers-faces (id 8) +
  complex-numbers-plane (id 9) are post-freeze AcademicReview shells with ZERO public resources
  (live API 0/0; ~7 KB station pages with zero resource links; controls vector-geometry 27 +
  differential-equations 0 re-verified; matrices-linear-transformations id 17 likewise 0) — all four
  never-captured stations are empty shells, nothing to crawl, the 855/25 corpus of record is final.
  All eight spec points 3.9.1–3.9.8 honest-empty, no picks; corpus-wide zeroes: argand 0,
  roots-of-unity 0, purely-imaginary 0, Re/Im(z) 0, de Moivre 0. Cross-map
  `cross-map-p3-complex-numbers.json` @ syllabai-experimental `2d6c5d6a` (spine export +3.9.1–3.9.8,
  35 → 43 — the pure-3 spine COMPLETE of record).
- **T-UGM-IMPORT-17 — UGM text corpus import, Pure 3 Complex numbers lane (this run)**:
  eighteenth landing; the candidate-model law continues with the ZERO-FRESH, ZERO-ALIGNED adaptation:
  NO new body files (`file_count` 628 → 628 unchanged; `pure-3-complex-numbers/` not created), no
  aligned rows to record, the ONE companion disclosure rides byref (`bodyImported: false`), MANIFEST
  v17 → v18 (lane-17 block appended; lane-1..16 rows + v9 assets untouched; strictly additive).
  Enrichment `cie-a-level-maths-20-pure-3-complex-numbers.json` (schema 1.0, SUGGESTED, 43 candidates
  closed exactly, stationScope eighteen-station-plus-rejects, the corpus-boundary disclosure carried).
  Both README lane-17 sections. Audits fail-closed ALL GREEN (closure exact 43 = 0 + 1 + 42; MANIFEST
  additive; 0 collisions trivially; spine rows verbatim).
