# AUDIT-2026-10-30 — F119: the printed-part-label serving wave (T-OEQ-PARTLABEL-3)

Wave: exporter v4 label emission (converter **unchanged** — no version bump) ·
corpus head of record `main@3b2ce8da700b80f51700fb34fc721c90d6654d6b` ·
operator orders: "Proceed with Option B — hub-only interim" (superseded in scope by)
"run Option A and report to the self improving docs of 'Official-ExamQuestion'
pipeline, so future agents also know" + layout refinement "both being in the same
line" (trace `1a18a0eadead9239`) + "the font of the part number could be a little
smaller" (trace `1a18a2e461266b5d`).

## The finding

Operator-reported learner-surface gap: on **all three** Official-ExamQuestion courses
(igcse-chemistry-19 / igcse-physics-19 / igcse-maths-b-16) the hub question player
rendered parts as bare `problemMd` blocks with a right-aligned marks tag — the printed
part labels ((a), (c)(ii)…) appeared nowhere. Two-layer root cause:

1. **Data layer** — the exporter of record (`official_examq_export_hub.py`) hardcoded
   `"questionPart": None` at the official part emission site; the label survived only
   inside the part id slug (`offp_2019-06_1p_1-a-i`). The SME plane carries only
   top-level letters / glued forms.
2. **Renderer layer** — the player's `partLabel` prop was aria-only by design ("never
   rendered as a chip"), and its only synthetic label was an index letter that would
   have MISLABELLED sub-part sequences ((a)(i),(a)(ii),(b)(i) as a,b,c,d).

**Why no gate caught it (the standing lesson):** the corpus gates (G1–G7) verify the
label at the data layer (the corpus `part_number` always carried it); the exporter byte
gates (G-E1..E5) compare the exporter's output against its own historical bundle — a
field the exporter never emitted cannot drift; G9's rendered benchmark had no
part-label visibility case. The defect was invisible to every gate BY CONSTRUCTION.

## The fix (three stages, two repos)

0. **Option B interim (v2 #467, T-OEQ-PARTLABEL-1)** — `lib/part-label.ts`: fail-closed
   label derivation from the id slug / SME questionPart; null when off-grammar, never
   an index guess.
1. **Layout refinements (v2 #469 + this wave's -3)** — the label renders INLINE with
   the part text on the same line (flex items-baseline row — "(b) Explain why…", not a
   chip above the text), then at `text-sm` (the operator's smaller-font note).
2. **Option A data-side fix (this repo, this wave)** —
   - `printed_part_label(part_number)`: strips the leading question number
     ("1(a)(i)" → "(a)(i)"); fail-closed grammar: 1–3 parenthesized `[a-z0-9]{1,5}`
     groups; bare "7"-style whole-question numbers → null; anything off-grammar
     refuses (and G-E6 then refuses the part outright if its id slug disagrees).
   - The part emission serves it as `sourcePaper.questionPart`.
   - **G-E6 label-identity gate** (`g_e6_label_law`): every official part's
     questionPart must EQUAL its own id slug's path re-wrapped; null IFF path-less;
     fail-closed in BOTH directions (a vanished label and an invented one both raise).
   - Zero-network unit battery `scripts/official_examq_f119_tests.py` (30 checks) +
     CI step in `.github/workflows/scripts-tests.yml`.

## Per-course serving paths (they differ — read before touching maths-B)

### 4PH1 + 4CH1 — full exporter re-serve (serve == corpus, proven first)

Baseline proof: the PRISTINE exporter at `main@3b2ce8da` re-emits the served bundles
as a **byte-level no-op** (G-E1 "regeneration is a byte-level no-op", both lanes) —
the served planes were exactly at the corpus of record before this wave.

Patched runs (branch evidence at the same cut; the of-record runs re-run at the
merged pin in the v2 sync):

| gate | 4ph1 | 4ch1 |
|---|---|---|
| G-E5 pin-proof | 55/55 | 54/54 |
| G-E3 census | 55 slices / 4,970 marks | 54 slices / 4,860 marks |
| G-E1 | 2,239 deltas == disclosure exactly | 2,607 deltas == disclosure exactly |
| G-E1b | 55/55 identity | 54/54 identity |
| G-E6 | 841 one-level + 1,398 two-level + 15 path-less | 778 + 1,829 + 0 |
| G-E4 | byte-identical (2,057,977 B) | byte-identical (2,605,409 B) |

Disclosures: `scripts/exporter-disclosures/2026-10-30-f119-part-label-serving-4ph1.json`
+ `-4ch1.json` (the changed-set = the label class exactly; new=0, gone=0). Independent
byte check: the staged `questions.json` are byte-identical to the served files; the
staged `official-papers.json` differ ONLY in `sourcePaper` (deep field diff).

### 4MB1 — serve-plane field-write (the disciplined exception)

The maths-B serving plane is **AHEAD of its corpus**: the T-OEQ-MATHSB-SERVE-1
run-020..025 chain applied eyes-on, MS/QP-page-verified repair tuples to the SERVED
bytes (1,461-pid standing debt; corpus back-syncs rode resources PRs #225/#226 only
partially). Measured: a pristine-port re-export at the `a7a34cd9` pin yields **1,466
regressive content deltas** vs the served plane (classes: markPoints+solutionMd 434,
problemMd 282, markPoints+problemMd+solutionMd 187, solutionMd 182,
problemMd+solutionMd 122, assets+problemMd 120, assets+markPoints+problemMd+solutionMd
108, assets+problemMd+solutionMd 31 — census of record:
`scripts/exporter-disclosures/2026-10-30-f119-maths-b-corpus-lag-census.json`).
Re-exporting from the corpus would have RESURRECTED repaired defect classes on the
learner surface — refused.

The F119 law went to maths-B as a **serve-plane field-write** (the run-0xx pattern of
that lane): `sourcePaper.questionPart` written id-derived (the SAME rule G-E6
enforces), everything else byte-untouched. Battery 8/8 PASS, fail-closed:

1. G1 serialization identity — parse→compact dump == served bytes (1a479c05…, 3,718,164 B)
2. G2 census EXACT — 66 sets / 1,281 questions / 2,443 parts / 6,600 marks pre==post
3. G3 marks map identical · 4. G4 id plane identical
5. G5 changed-set deep-diff == questionPart only (1,723 writes; pre-state snapshotted
   by re-parse — the aliasing blind the battery itself caught and fixed)
6. G6 label law bidirectional — 1,594 one-level + 129 two-level + 720 path-less/null
7. G7 PUA/U+FFFD/dollar parity — 0→0 / 0→0 / 3,623→3,623
8. G8 output single-line compact, no trailing newline

Bytes: 3,718,164 → 3,720,356 (+2,192 — the label field only). The tool + receipt ship
in the v2 wave receipts (`T-OEQ-PARTLABEL-3/run-001/`).

## Corpus-wide census of record

| course | parts | labelled | null (path-less) |
|---|---|---|---|
| igcse-physics-19 | 2,254 | 2,239 | 15 |
| igcse-chemistry-19 | 2,607 | 2,607 | 0 |
| igcse-maths-b-16 | 2,443 | 1,723 | 720 |
| **total** | **7,304** | **6,569** | **735** |

The 6,569 = exactly the path-carrying id universe (the part-label.ts census of record);
the 735 whole-question slices stay honestly null (the card header number chip is their
whole printed label).

## Queued (not this wave)

1. **G9 rendered-benchmark case for part-label VISIBILITY** — the gap that let the
   defect ship; the benchmark now owes the case.
2. **Maths-B corpus back-sync** — the standing debt; the re-export MUST port
   `printed_part_label` + G-E6 into the maths-B exporter port FIRST (the F119 ledger
   section documents the exact risk).
3. **v2 companion** — the T-OEQ-PARTLABEL-3 card: data-first part-label consumption +
   the text-sm label + the re-stamped manifests + the field-write receipts.
