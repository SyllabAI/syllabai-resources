# AUDIT — F86 corpus-wide re-receipt (2026-10-28, converter v0.29.2)

> Operator order: "F86 corpus-wide re-receipt". Closes the item F110 left open:
> *"the corpus-wide re-receipt stays open — 52 untouched slices keep of-record
> bytes, the battery guards them."* The wave re-emits the whole chemistry corpus
> fresh from the staging of record, diffs every byte against the corpus of
> record under a stated normalization law, classifies every delta, and files
> the receipt. Machine twin: `AUDIT-2026-10-28-f86-corpus-re-receipt.json`
> (schema `syllabai.official-examq.reemission-rereceipt/0.1`).

## Method

- **Emission**: all 54 chemistry slices (16 series × 1C/2C + 11 × 1CR/2CR) re-emitted
  fresh with the converter of record from the staging of record
  (`EXAMQ_UPLOAD_DIR=/home/z/my-project/upload`, pdftotext -layout txt layers).
  G0 sha-verifies the staged PDFs against the manifest pins in every slice run.
  Fail-closed: 54/54 exit 0 (verified twice — once at v0.29.1, once at v0.29.2).
- **Normalization law** (the prior parity receipts' exemption, made explicit):
  `generated_utc` and the converter version string (the `generator` field and
  `edits[].tool`) are the only exempt bytes. `questions.md` compares byte-raw;
  assets compare by sha256; `validation-report.json` compares semantically
  (per-gate statuses, negative controls, review queue, applied-override listings).
- **The corpus of record is NOT modified by this wave** (the F110 standing
  decision). The census diffs the worktree emissions against HEAD; the tree is
  restored afterwards and the battery re-proven on the restored state.

## Headline results

| Measure | Result |
| --- | --- |
| Slices byte-clean after normalization | **22/54** |
| Assets | **407/407 byte-identical corpus-wide**, 0 added, 0 removed |
| questions.md | **0 topic-independent deltas** (every delta renders its slice's topic deltas) |
| Gate states | every gate PASS on both sides in all 54 slices — no gate regression |
| validation-report semantic deltas | 8 slices (all attributed, below) |
| Unexplained deltas | **zero** |

## The F86 trio: CLOSED

The three staging-boundary items F86 documented — C61's positional key on
2019-06 1CR 5(a)(ii); C56's pins on 2019-06 2C 7(a) and 2021-01 2C 3(a)(i) —
**all reproduce from the current staging** under the F110 row-rebuttal lexeme
fix. C61 and C56 PASS against the fresh tree. In F86's era C61 was the 1-of-91
battery exception, exonerated only by the A/B receipt; the exception is now
retired — the current staging + converter reproduce the served keys outright.

## Defect found and fixed in this wave (converter v0.29.2)

**The F108 leg-0 × MS-LINK-OVERRIDES interaction.** The geometry-aware
bare-numeral keep (F108 leg 0) resurrected the marks-column digits / Total-footer
fragments as the *only* linkage content of the two printed-image answer cells —
2023-06 2CR 7(c)(i) served the fabricated `'1'` and 2025-06 2CR 7(c)(ii) served
`'1' + '15'` on every fresh emission. That all-fragments block defeated the
`not lines` override precondition, so the F47/F107 eyeballed transcriptions
never fired and `answer_key_source` was lost. This is the same cross-wave
interaction class F110's follow-through was ordered for — and neither C97 nor
C109 had been able to see it (both assert the linkage state, which stayed
`linked` either way; only the census caught it).

**Fix**: an all-marks-fragments linkage block (every line a bare 1–2 digit
fragment, optionally behind an abbreviated `Total … =` prefix) no longer
defeats the override precondition (`_MS_MARKS_FRAGMENT_RE` +
`_all_marks_fragments`). Blast radius: the 7 ledger entries only — legitimate
F90 bare-numeral restorations are not ledger parts and never enter this path.

**Result**: 2025-06 2CR 7(c)(ii) reproduces the of-record learner surface
byte-exactly; 2023-06 2CR 7(c)(i) fires the ledger again (linked, ledger
attribution, no fabricated digit; C97/C109 PASS on the fresh tree). The longer
curated transcription the corpus carries for 7(c)(i) stays a disclosed
data-only class (below).

## The classified delta universe (32 slices; of-record bytes unchanged)

1. **Drawing-strip remains — 19 problem_md parts.** The Task-20 drawing-strip
   patches and the 0.23.0 propene-equation strips are data-only corpus edits;
   regeneration re-introduces the atom labels/bonds text-layer fragments
   (fresh text longer by 4–45 chars of letter/digit soup). Positive
   confirmation of the F98 mechanism: the two slices whose fragment lines ARE
   registered in `official_examq_text_repairs.json` (2021-06 1C, 2023-06 1CR
   10(c)(i)) are **absent** from this class — they now reproduce.
2. **Exponent-restore (Finding 8b) — 23 parts / 51 field deltas.** The corpus
   carries Unicode superscript exponents (data-only restorations); fresh
   emissions emit the text-layer flattened forms (`10⁻²⁴` → `10-24`).
   **Guard proven live**: the fresh tree fails exactly one canary,
   C95-flat-exponent-free (109/110) — the designed guard that would block an
   uncurated regeneration from shipping.
3. **F90 restoration not yet landed — 2022-06 2C 6(a).** The fresh emission is
   *more correct* than the of-record: the printed M1 reads a stacked fraction
   (20 × 10⁶ over 80); pdftotext drops the denominator `80` to its own line and
   the F90 keep-law preserves it. The of-record predates the keep-law for this
   slice. Eyeballed on the 150 dpi MS p11 render. Landing it = a corpus sync
   wave with exporter disclosure, not this receipt.
4. **Furniture residue — 2020-11 1C 3(c)(ii).** The fresh emission keeps a lone
   `marks` token (the tail of `Total for Q3 = 8 marks`): the F88 mid-text law
   keeps <2-furniture-token lines fail-closed, while the of-record carries the
   exporter's serve-time strip form — the F88 reconciliation's remaining half.
5. **Image-answer curated form — 2023-06 2CR 7(c)(i).** The of-record
   solution_md/mark_points carry the longer curated F107 transcription
   (+ `value_trace.solution`, `edit_status: corrected`, `edits[]`); the fresh
   emission serves the ledger `ms_lines` form — the same space-collapsed form
   the two structure-transcription ledger parts (2021-01 2CR 7(d),
   2025-06 1CR 9(d)(ii)) already serve and reproduce with. The fabricated `1`
   is gone either way.
6. **Surgical-repair metadata — 3 parts** (2021-11 2C 1(d) F97 bare-answer;
   2025-06 2C 5(c)(i) F92 tick-glyph; 7(c)(i)). The repairs' learner-facing
   bytes reproduce (the F97/F92 converter machinery is in place); only the
   `edit_status`/`edits[]` disclosure metadata differs (data-only).
7. **F94 shared-asset curation — 5 part-level asset-field deltas.** 2020-11 2CR
   1(b) drops its shared ref on regeneration (the asset file is byte-identical;
   the reference's home is the stem part), 2021-11 1C 1(a)(i)–(iii) carry the
   F94 follow-up mention strings, 2020-01 2C 6(d)(ii) recomputes
   `text_coverage` 0.3 → 0.305; `wave20.stem_figure_stubs` +1 on 2019-06 1CR.

## Battery columns

| Tree | check_canaries | g9-static |
| --- | --- | --- |
| of-record (HEAD, restored) | **110/110 PASS** | PASS (8/8) |
| fresh emissions (v0.29.2) | **109/110** — the 1 exception is C95, the designed exponent-restore guard | PASS (8/8) |

On the fresh tree the F86 trio and image-answer guards all hold: C61 PASS,
C56 PASS, C97 PASS, C109 PASS.

Review-queue drift: the fresh reports raise 3 new honest F95 mark-point-gap
items (2019-06 2C 2(a), 2019-06 2C 6(d)(ii), 2025-11 1C 5(c) — printed-drawing
answers) plus the wave20 stub counter on 2019-06 1CR — fail-visible census
drift; corpus bytes unaffected.

## Verdict

**REPRODUCTION-GUARDED.** Every regeneration delta is (i) fixed in this wave
(the F86 trio; the override precondition), (ii) a named data-only curation
class with its guard canary named, or (iii) an F90-class improvement the corpus
has not landed. Zero unexplained deltas. The corpus of record bytes are
untouched; landing the fresh bytes would be a separate exporter-disclosure +
v2-sync wave. The F86-queued item is closed: the corpus-wide re-receipt exists,
and the lexeme fix's corpus-wide consequences are measured, classified, and
guarded.
