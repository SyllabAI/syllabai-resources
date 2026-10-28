# AUDIT — the F88 reconciliation's remaining half (2026-10-29, converter v0.30.1)

> Operator order: "F88 reconciliation's remaining half". Closes the F111
> delta-class item: *"furniture residue: 2020-11 1C 3(c)(ii) keeps a lone
> `marks` token (the F88 <2-token fail-closed keep vs the exporter's
> serve-time strip — the reconciliation's remaining half)."*
> Machine twin: `AUDIT-2026-10-29-f88-furniture-reconciliation.json`
> (schema `syllabai.official-examq.ab-reconciliation/0.1`).

## What the remaining half was

The F88 hygiene-v2 wave (Task 19, v0.21.1) reclaimed the MS-grid furniture
universe corpus-wide (151 solution + 84 mark-point blocks) using the
unambiguous classes only, keeping bare `answer`/`mark`/`marks`/`Number` lines
fail-closed (the wrap-ambiguity doctrine: "1 mark" splits across lines). The
exporter's serve-time F-W15-2 strip (trailing-only, up to 4 lines) had produced
the serve-clean form at the original authoring. F111's corpus-wide re-emission
census then found the two laws disagreeing on exactly ONE line corpus-wide:
2020-11 1C 3(c)(ii), where the of-record is serve-clean but every fresh
emission re-inserted a lone `marks` line **mid-text** (between `electrons` and
`- -` — which is why the trailing pop never ate it).

## Root cause of record

The staging layer prints the page footer `Total for Q3 = 8 marks`
(`official-2020-11-1C-ms.txt` L229). The F87 abbreviated-footer sub (v0.21.1)
matched only `Total for Q3 = 8` — its ` marks` tail survived the raw layer and
rode into the assembled entry text. Corpus-wide staging census: exactly 4
abbreviated-footer-with-marks lines exist (Q1=7, Q2=6, Q3=8, Q10=13 — all in
this one file). The Q1/Q2/Q10 tails landed at text end, where the trailing pop
ate them (the same path the exporter's serve strip had taken at authoring);
3(c)(ii)'s tail landed mid-text, where the F88 keep law correctly refused it.
So the leak is an INCOMPLETENESS in the F87 sub, not a defect in the F88 keep
law: the sibling F93 sub and the exporter's spelled-form trailing law both
already consume their ` marks` suffixes.

## The fix (two lines, one law, v0.30.1)

1. **F87 sub completed**: `\bTotal\s+for\s+Q\d{1,2}\s*=\s*\d{1,3}(?:\s+marks)?\b`
   — the printed footer line is page furniture verbatim, tail included.
2. **`MS_TOTAL_LINE_RE` consistency**: the abbreviated alternative recognizes
   the marks suffix (`(?:\s+marks)?$`), matching the printed footer verbatim.
   With (1) such lines never reach the strip — A/B-proven zero live firing.

The F88 wrap-ambiguous keep class is **untouched**. The 12 standing
lone-`marks` keeps (corpus + mirror renderings) are wrapped guidance fragments
— content continues after every one of them (`Alternative method`, `and either
of the following points:`, `(graphite is soft because)`, `ALLOW M1×2.5`,
`sign required to score`, `M2 strong (ionic) bonds …`, `M1 (28 ÷ 80) × 100`)
— and remain kept by law; C110's carve-out is unchanged.

## Method

- **Emission A**: all 54 chemistry slices emitted fresh with the converter at
  HEAD (v0.30.0) from the staging of record (`EXAMQ_UPLOAD_DIR=/home/z/my-project/upload`;
  G0 sha-verifies the PDFs against the manifest pins in every run). 54/54 exit 0.
- **Emission B**: the same 54 slices with v0.30.1. 54/54 exit 0.
- **A/B diff** under the F111 normalization law (`generated_utc` and the
  converter version string in `generator`/`edits[].tool` are the only exempt
  bytes; `questions.md` byte compare modulo the generated stamp; assets sha256;
  validation-report semantic). Drivers were session-workbench copies (the F111
  precedent — not committed): the emit driver loops the 54 registry slices
  through `official_examq_extract.py` (same skip law as run_all.sh's convert
  leg); the differ applies the normalization law and asserts the EXACT verdict.

## Results

| Measure | Result |
| --- | --- |
| Files compared | **578** (54 slices × topic.json + questions.md + validation-report.json + assets) |
| Identical after normalization | **576** |
| Content deltas | **2 — both the reconciliation target**: `2020-11/4CH1-1C` topic.json `questions[2]/parts[6]/solution_md` (fresh-A carries the lone `marks` line; fresh-B matches the of-record) and the same slice's `questions.md` blockquote mirror (fresh-A line 275 `> marks`; fresh-B without) |
| A/B verdict | **EXACT** — the law's blast radius is the disclosed target, nothing else |
| F111 class-4 census entry | **VANISHES**: fresh-B 3(c)(ii) solution_md == HEAD of-record bytes; the slice's only fresh-vs-HEAD deltas are `spec_point_codes`/`tagging` (the llm-spec curation replay absent from the A/B workbench — converter-deterministic `pending-llm`, byte-equal across BOTH emissions per the A/B, so converter-version-independent) |

## Gates

- **Canaries**: 117/117 on the of-record tree (twice — before and after the
  A/B overlay restore). Fresh tree 114/117: C95-flat-exponent-free (the
  DESIGNED Finding-8b guard, the F111 precedent) + C32/C33-spec-tag-terminal
  (the curation-replay artifact above — not a converter regression).
- **Exporter plane** (unchanged by law, proven no-op): exporter rc=0 against
  the v2 bundles of record — G-E1 byte-level no-op (0 deltas), G-E1b 54/54
  identity byte-equal, G-E2/G-E3 constants hold, G-E4 questions.json
  byte-identical passthrough (2,605,409 B, 28 SME sets); verifier rc=0
  ("census matches the disclosure of record exactly (0 parts)"); self-test 4/4
  seeds refused. No exporter disclosure filed and no v2 companion needed —
  the corpus of record is NOT modified (the F110 standing decision) and the
  serve plane is byte-unchanged (the F111 precedent for zero-corpus-byte waves).
- **Unit battery of record** (new, zero-network, CI-pinned):
  `scripts/official_examq_strip_law_tests.py` — 29/29 green. Pins: the leak
  closed at source on all 4 staging footer lines; the 12 standing keeps
  preserved by name (raw layer + strip law); the `MS_TOTAL_LINE_RE`
  consistency leg; the trailing pop; the fail-closed refusal; and the
  upstream-not-strip-patch law (the strip refuses to create the of-record
  form from the leaky text — the fix lives in the raw layer).

## Scope discipline

The 12 standing keeps are NOT reconciled away here: they are the F88 standing
law (wrap-ambiguous keeps, disclosed and C110-guarded), corpus == hub == serve
consistent. The remaining half was the fresh-vs-record DISAGREEMENT — the one
line where regeneration re-introduced what the serve plane had stripped. That
disagreement is closed: a full re-run now reproduces the corpus of record for
2020-11 1C 3(c)(ii) byte-exactly, and the F111 classified delta universe loses
its class 4 entirely.
