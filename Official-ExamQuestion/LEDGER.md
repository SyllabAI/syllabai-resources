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

## Wave summaries

- **Wave 1 — prototype (2020-11 baseline)**: converter + gates G0–G6 + negative controls built; 7 iterations; NC 3/3.
- **Wave 2 — multi-series generalization (6 series)**: F1–F10; 2019-06 archive damage honestly attributed; 2024-06 cross-diff 55/55 vs repo parsed layer.
- **Wave 3 — full-corpus batch (16 series, this run)**: F11–F14; 14/16 full PASS; 169 questions; 930 parts; 1754/1760 marks; cross-diff 161/161 on all three series with a parsed layer (2024-06, 2025-06, 2026-06).

## Entry format (append below; never rewrite history)

    | F<max+1> | <date> | <series> | <finding — what defeated the parser/gate, at raw-text level> | <generic fix> | <canary id / new canary added> |
