# ADR-037 corpus run — 4CH1/1C complete (all series in syllabai-pastpapers)

> generated 2026-10-20T22:38:00Z · baseline 2020-11 · gate suite G0–G6 + negative controls N1–N3 per paper
> 16 series · 169 questions · 930 parts · 1754/1760 marks (6 lost to 2019-06 archive damage) · 14 series fully PASS

| series | G0 | G1 | G2 | G3 | G4 | G5 | G6 | NC | questions | parts | marks | MCQ keyed | review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019-06 | PASS | REVIEW | PASS | PASS | PASS | REVIEW | PASS | 3/3 | 14 | 53 | 104/110 | 3/3 | 27 |
| 2020-01 | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | 3/3 | 10 | 60 | 110/110 | 1/3 | 2 |
| 2020-11 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 64 | 110/110 | 6/6 | 4 |
| 2021-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 11 | 53 | 110/110 | 3/3 | 4 |
| 2021-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 54 | 110/110 | 2/2 | 3 |
| 2021-11 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 11 | 67 | 110/110 | 1/1 | 4 |
| 2022-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 11 | 65 | 110/110 | 2/2 | 5 |
| 2022-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 57 | 110/110 | 3/3 | 3 |
| 2023-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 12 | 60 | 110/110 | 7/7 | 1 |
| 2023-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 55 | 110/110 | 3/3 | 3 |
| 2023-11 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 66 | 110/110 | 2/2 | 8 |
| 2024-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 56 | 110/110 | 4/4 | 1 |
| 2024-11 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 11 | 56 | 110/110 | 2/2 | 6 |
| 2025-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 49 | 110/110 | 6/6 | 2 |
| 2025-11 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 10 | 59 | 110/110 | 6/6 | 3 |
| 2026-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 3/3 | 9 | 56 | 110/110 | 5/5 | 4 |

## Terminal states

- **14/16 series: all gates PASS** — every mark accounted for, every MCQ keyed, negative controls detected 3/3.
- **2020-01: G3 FAIL is honest** — the printed MS interleaves Q7(a)(ii)/(iii) marker rows; a wrong auto-key was refused (it would have keyed C where the notes prove A). Two MCQ keys need a human. Canary: `7(a)(iii)` must stay unkeyed.
- **2019-06: G1/G5 REVIEW reflect real archive damage** — 5 rasterized content pages; Q7 wholly lost (6 marks), Q1/Q11/Q12/Q15 partial. Content needs OCR/manual re-ingest; nothing was invented to fill the gaps.

## Independent-parse cross-diff (strongest correctness evidence)

- part-level marks vs repo parsed/questions.json layer (independent parser, same PDFs)
- 2024-06: **56/56 part marks agree, 0 mismatches** (letter-group totals recorded only by the parsed layer: 14)
- 2025-06: **49/49 part marks agree, 0 mismatches** (letter-group totals recorded only by the parsed layer: 6)
- 2026-06: **56/56 part marks agree, 0 mismatches** (letter-group totals recorded only by the parsed layer: 12)

## Generalization findings (cross-series quirks -> parser/gate fixes)

- **F1** (2019-06): question start lines are indented (QSTART required leading-space tolerance) → _QSTART_RE allows leading whitespace_
- **F2** (2019-06): 8 rasterized (image-only) pages in archive PDF; 6 content pages lost: Q7 gone entirely (its footer too), Q1/Q11/Q12/Q15 partial → _image-only page census + defect attribution to questions + G1 REVIEW path (never silent, never invented)_
- **F3** (2019-06): Q7 footer absent from PDF text layer → _footer census detects the gap; review item names the lost pages_
- **F4** (2019-06): paper has 15 questions (early 4CH1 format), not 10 → _per-series question-count registry; paper-level invariant kept at 110 marks_
- **F5** (2020-11 vs 2020-01): MS note phrasing differs: 'is not correct' vs 'is incorrect' → _unified note filter covering both phrasings_
- **F6** (2020-01): MS marker column drifts one row early in Q7(a): note rows leak into adjacent entries; naive keying would emit C for 7(a)(iii) where the printed notes prove A (astatine) → _answer-row analysis keyed only when exactly ONE distinct candidate; ambiguous entries -> human review_
- **F7** (2019-06): MS sub-letters printed bare without parentheses ('b      they have...') → _MS_BARE_LETTER_RE with branch precedence over the catch-all row regex_
- **F8** (2019-06/2020-01): three 'DO NOT WRITE IN THIS AREA' phrases share one extracted line → _phrase-level substitution instead of whole-line filter_
- **F9** (2019-06): damaged Q1 region begins with a part marker '(c) ...' as line 0 → _segment_question lets the loop classify line 0 instead of forcing it into the stem_
- **F10** (2020-01): marker-only MS row carries a trailing marks digit ('(iii)   1') which glued to the answer → _strip leading marks digit only when followed by a choice letter_
- **F11** (2023-06): MS continuation rows indented 11+ spaces; marker-row regex allowed only 10 — all roman parts after the first went unlinkable (G5 76%) → _MS_ROW_RE / MS_BARE_LETTER_RE indent allowance widened to 20_
- **F12** (2021-01 (and 2021+ MS style)): MCQ keys phrased '<L> is the correct answer because...' plus '<L> is not THE correct answer because...' rebuttals — the inserted 'the' defeated the note filter, all four letters became candidates, guard refused every key → _positive-statement keying ('<L> is (the) correct' is authoritative) + note filter extended to 'is not the correct'_
- **F13** (2026-06): manifest schema drift: series.printed / series.source / variant.official_code absent in gap-fill-wave manifests — converter crashed in G0 instead of flagging → _manifest reads use .get() with explicit 'absent in schema v2' annotation in G0 summary_
- **F14** (2023-06/2025-06/2025-11/2026-06): rebuttal-style MCQ MS: explicit rebuttal for every wrong option ('A is incorrect...', 'B the charges are incorrect', 'B is X incorrect', '<L> (answer)' cells, glued 'B4' answer+digit cells) — single-candidate logic insufficient → _elimination keying: sole un-rebutted option keyed only when corroborated by exactly one answer row; anything ambiguous stays unkeyed (2020-01 canary still refuses)_

## Self-improvement loop

Every finding above is (1) fixed in the converter, (2) recorded in `LEDGER.md`, and (3) guarded by a canary in `CANARIES.json`
that `run_all.sh` re-verifies on every future run. See `AGENTS.md` for the protocol new agents must follow.

