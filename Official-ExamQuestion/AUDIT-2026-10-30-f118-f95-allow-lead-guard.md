# AUDIT-2026-10-30 — F118: the F95 ALLOW-lead guard (the F111 row's last review-queue item closes)

Wave: converter **v0.33.0** · corpus head of record `9db02bb758b7487dd6a5b32131d5413f7bc2c56b`
(#220 merged) · operator order "merge #220, and continue processing the remaining waves of
F88/F111".

## The item

The F111 row's review-queue drift filed three fresh-report F95 items:
`2019-06 2C 2(a)`, `2019-06 2C 6(d)(ii)`, `2025-11 1C 5(c)`. F113 closed the first two by
serving the printed drawing answers (both are in `MS-ANSWER-FIGURES.json`). The third —
**2025-11 1C 5(c)** — was never adjudicated. It was the F88/F111 families' last open item.

## The adjudication: FALSE POSITIVE of the F95 fragment law

- The printed MS answer cell of 2025-11 1C 5(c) legitimately begins **"Allow any two
  from:"**, and the part's single 2-mark MP1 is the **full six-M-row transcription**
  (M1 concentration of copper(II) sulfate … M6 Same (polystyrene) cup) with the two-column
  Notes weave (`IGNORE same mass/amount of metal W`, `If no reference to … for 1 mark`).
- The F95 fragment law's case-insensitive `^ALLOW\b` arm (re.I|re.S — designed for
  margin-note fragments like `ALLOW ORA`) swallowed the whole answer text, so the G7
  `mp_answer_gap` census filed a junk review item on **every fresh emission**.
- The of-record report shows `review_n = 0` while the fresh report shows `1` — the drift
  is reporter-side only; the fresh `topic.json` bytes are identical to the of-record (the
  F86 census's own `topic.json: same` line for this slice).
- **Eyeball of record** (the F113 method): the MS PDF sha256-verified against the
  manifest pin (`c8962567…c2e0da`, 386 895 B); the full MS p8 rendered at 150 dpi and
  read, then the 5(c) proof clip read against it. The band is **pure text**; the page
  carries **zero images**. (The F86 audit's blanket "printed-drawing answers" phrase was
  right for the two F113 parts and wrong for this one.)
- The of-record serving is already complete (`solution_md` == the MP copy). **Zero corpus
  bytes move** — no exporter disclosure, no v2 companion (the F110 convention attaches to
  served-byte changes).

## The fix (the ALLOW arm split out, v0.33.0)

`_mp_only_fragments`'s ALLOW arm refuses to fire when the text carries the printed
**M-marker row structure** (`\nM<digit>` at a line start — the answer cell's own content
skeleton per the F90/F108 MS-grid laws; a margin note carries inline M-references at
most: `ALLOW M1×2.5`, `If M1 and M2 not fully`, `dep on M1`).

## The A/B census of record (both predicates run over all 54 chemistry slices in one process)

| Law | Hits | Δ |
| --- | --- | --- |
| before (v0.32.0 law) | **19** | — |
| after (v0.33.0 law) | **18** | the sole exit is `2025-11/4CH1-1C:5(c)`; zero enters |

Every standing classification keeps its flag:

- the 6 F113-served drawing answers still in the census (2026-06 2C 5(a) exited at its
  own F113 serving — its of-record MPs are no longer fragment-shaped);
- the disclosed class-4 `scores`-arm residual unchanged, including its M-row members
  (2020-01 1CR 8(a), 2022-01 1C 6(a), 2024-06 2CR 7(b)(i), 2026-06 1C 8(b)(i)) — the
  guard is ALLOW-scoped by design;
- the F97 founding shapes, the bare-marks-digit leak, the `25` re-emission law, and the
  F108 answer-grid exemption all byte-identical in behavior.
- F97 site blast radius: **zero** empty-solution parts corpus-wide (0 → 0) — no emission
  can change. The fresh reports' drift closes (`review_n` 1 → 0 on 2025-11 1C).

## Proof

- Zero-network unit battery `scripts/official_examq_f118_tests.py` — **30/30 PASS**
  (the guard law in the source; the law alive on the of-record 5(c) bytes; the
  arm-scoping keeps; the 18-hit census; the F97 zero-flip). CI step added.
- **Canaries 214/214** on the workbench tree with v0.33.0 in the checkout (three lanes:
  54 chemistry + 55 physics + 66 maths slices; 1 292 assets fetched; C107's G9 static
  corpus leg and C108's mutated-fact negative control included).
- F116 / F117 / strip-law (29/29) / G9 gate batteries all green on the same tree; the
  f117 version assert promoted to a floor (≥ 0.32.0) per its own ledger note.
