# Deep audit — igcse-chemistry-19 (Task 19 r2, 2026-10-27)

> Trigger: user-served report on `june-2026-4ch1-2c` ("It has so many issues"), following the
> Task 18 CONTINUES-footer finding (F87, closed at 0.21.1). Scope: all 54 slices / 2,607 parts,
> three layers (corpus topic.json + hub official-papers.json + live Vercel pages), battery v3 =
> 30 furniture families + 10 shape families + consistency re-checks. Head of record at audit
> start: resources `0261a2b90875…`, v2 `70ffa43db948…`. Receipt: `da-sweep.json` +
> `FA-AUDIT.json` lineage in the Task 19 session receipts.

## Finding 1 — the Task 18 CONTINUES class is CLOSED corpus→hub→live

The 9 defect parts of the Task 18 census carry zero CONTINUES-family strings at HEAD corpus,
in the served hub bundle, and on the live pages — the 0.21.1 hygiene-v2 wave (F87) closed the
class end-to-end. The only corpus-wide `continues` hit is authored prose ("rust prevention
continues to protect iron"). No regression.

## Finding 2 — drawing-linearization (F96): 18 parts / 14 slices, 15 still open

Printed structures/equations whose PDF text layers linearize into atom-run garbage
(`H H H H H H A C C C B C C C H H …`) served in problem_md/solution_md with NO figure asset.
The G8 figure queue (wave-24) tracked only figure-LANGUAGE mentions, so most of these never
entered any queue; G4's mention nouns share the blind spot; the hub mirrors the corpus
faithfully (user-visible); live SSR+RSC carry the strings twice per page.

Fixed this wave (crop + strip, eyeballed renders): 2026-06 2C 1(b) (four poly(propene) option
structures — also the F94 vacuous-MCQ case), 1(c) displayed formula (served on 1(c)(i)),
1(c)(ii) equation, 1(c)(iii) polyester.

Open (PINNED at 15 by C98; crop-wave queue with per-part page anchors in the session receipt
`drawing_linearization_open`): 2019-06 1CR 4(b)(iv); 2020-01 1CR 9(b)(ii); 2021-11 1C 6(a)(iii),
6(a)(iv); 2021-11 2C 6(e)(ii); 2022-01 1C 8(d)(i); 2022-01 2C 7(e); 2022-06 1CR 7(c);
2023-01 1C 6(a), 6(b); 2024-06 1C 8(a)(ii); 2024-06 2CR 7(c)(i); 2024-11 1C 10(c);
2025-06 1CR 9(d)(ii); 2026-06 1CR 8(c). Plus 4 solution_md-only residue parts
(2019-06 2CR 4(e)(i), 2020-11 1C 3(c)(ii), 2020-11 1CR 3(d)(ii), 2025-06 2C 4(c)(iv)).

## Finding 3 — drawing-option MCQs keyed blind (F94): 9 parts, 0 lost keys

Nine "Which structure/diagram…" parts serve no choices[] (options are drawings):
2020-11 2CR 1(b); 2021-11 1C 1(a)(i)–(iii); 2023-01 2C 2(a)(i)–(iii); 2026-06 2C 1(b).
Every one is answered by the enrichment layer and keyed in the MS verbatim block — no wrong
keys served — but G3's "0 MCQ parts" summary was a vacuous pass. G3 now censuses them.
Crop-wave follow-up attaches the option drawings (same machinery as Finding 2).

## Finding 4 — MS-answer-is-a-drawing (F95): 4 MP-gap parts + 2 related

2026-06 2C 5(a) (MPs = two fragments of one margin note), 2023-06 2CR 7(c)(ii) ("REJECT -OH
not displayed" only), 2024-06 1CR 10(b)(ii) ("allow it to dry" only), 2025-06 2C 5(d)(ii)
("allow the solution to cool…" only). Related: 2023-06 2CR 7(c)(i) (empty solution + marks-
digit MP "1"; the converter REFUSES to fabricate — F97 refusal class) and 2021-01 2CR 6(c)(i)
(the `/1000` dm3 conversion line absent from its solution block). The converter cannot crop
MS-side figures today (F45 renders QP pages only) — MS-crop support is the filed converter
follow-up; until then the class is fail-visible in G7 + review queue.

## Finding 5 — MS answer-grid linearization (2021-06 1C 1(a), 2023-06 1CR 4(a))

Two "match descriptions" parts serve their MS answer GRID as scrambled text with the
"Information/Substance" column headers glued in ("ALLOW correct\nInformation Substance
formulae\na good conductor of copper\nelectricity…"). The enrichment layer does not cover
these two (corpus MS block served verbatim on hub). Fix class: MS-box parser tranche (the
F68 physics vertical-parser lineage). Filed; not fixed this wave.

## Finding 6 — the empty-solution law (F97): closed for real answers, refused for drawings

2021-06 1C 2(b)(ii) → solution_md `25` (verbatim MP re-emission, disclosed); 2021-11 2C 1(d) →
`73`. 2023-06 2CR 7(c)(i) stays empty BY DESIGN (refusal; Finding 4). C97 pins the law.
This completes 2 of the 4 instances LEDGER F90 queued (hygiene-v2 r1); the corpus of record
now matches the hub serve-form for those two parts.

## Finding 7 — the tick-glyph mojibake (F92): 3 fixed, 1 verbatim by design

`ticks (ü)` → `ticks (✓)` at 2025-06 2C 5(c)(i) (surgical), 2025-11 2C 1(a) (regenerated),
2026-06 2C 2(d)(i) (regenerated). The printed grid-cell tick in 2025-11 2C 1(a) stays — it is
question content. The sub is mirrored into the anchoring text (page anchors survived: both
regenerated slices re-anchored identically).

## Finding 8 — reproducibility debt (NEW hazard, disclosed)

A full v0.22.0 re-run of the committed corpus diverges on 14 slices (all default-paper 1C:
2019-06 … 2026-06): (a) MCQ positional keys lost — choices[].is_correct dropped, MP form
"Answer B: 3" → raw MS block + review-queue (2023-11 1C 2(b)(i), 2025-06 2C 2(a)(ii),
2025-11 1C …); (b) committed superscripts re-flatten (`× 10²³` → `× 1023`) — the 0.21.1
restore pass does not fire on the staged layers as committed; (c) the deferred MS-grid
residue classes re-enter solution tails. Consequence: the corpus of record is NOT
re-derivable from HEAD converter + staged layers on those slices. This wave shipped
surgically; the reconciliation wave (converter-side MS-grid parser + restore-pass diagnosis)
must land before the next full re-run. C94/C95 and C13/C71 are red-on-main for exactly these
pre-existing classes — recorded, not worsened, by this wave.

## Fix-wave ship state (this document's wave)

- Converter 0.23.0: F92 (+mirror law), F93, F94, F95, F96, F97, F98; text-repairs file-scoped
  + 18 chemistry rules; canaries C96/C97/C98 (96 total); C94 regex extended.
- Data: 2 slices regenerated (2026-06 2C, 2025-11 2C), 3 surgical patches (2025-06 2C,
  2021-06 1C, 2021-11 2C), 4 new crop PNGs, STEM-RESTORE +1 verdict, CROP-REVIEW +4,
  FIGURE-QUEUE 25→29 cropped.
- Export: G-E1..G-E4 green; disclosure `scripts/exporter-disclosures/2026-10-27-task19-deep-audit.json`
  = 9 changed parts (7 wave + 2 carried from wave-26's exponent normalization).
- Verified: battery v3 re-run post-fix shows the 2C paper with zero shape hits; crops
  eyeball-verified; hub bundle spot-checked (1(b) clean + asset; `ticks (✓)`; 5(a) MPs
  honestly unchanged + queued).

## Task 20 closure (same day) — the Finding 2 queue executed

The C98-pinned 15 were cropped+stripped (16 crops incl. the F94 particles owner; rects
eyeballed against 150 dpi page renders, PNGs re-verified), and the closure re-census found
the census UNDER-INCLUSIVE: 6 further parts (2020-01 2C 6(d)(ii), 2021-01 1CR 8(b)(iii),
2021-06 1C 5(c)(i), 2022-06 1CR 7(d)(i), 2022-06 2CR 5(c)(ii), 2023-06 1CR 10(c)(i)) whose
atom runs are broken by multi-char tokens (`HO`/`CH3`/`COOCH3`/`C6H4`/bracket glyphs) were
cropped+stripped in the same wave. The F94 option-drawing follow-up landed as shared refs
(2020-11 2CR 1(b); 2023-01 2C 2(a)(ii)/(iii)) + the 2021-11 1C particles owner crop. C98's
checker arm (missing from this wave's ship — see LEDGER F104) now pins the census at 0;
C22 green via 4 backfilled ledger entries; C56's bracket pin re-homed. Canary suite 6→2 red
(C13/C71 recorded). The 4 solution_md-only residue parts remain open with the reconciliation
wave.
