# T-TEXTDEBRIS-1 — the `\text{}` / MathML-speech debris cleanup curation lane

Lane of record: the disclosed follow-up curation lane of RN-RECONSUME-1 /
EQFC-CONSUME-1 (syllabai-v2 worklog, operator trace 1a188fd1fe1ab249 chain):
"the `\text{}` debris cleanup = the follow-up curation lane (baseline refrozen
to the corpus-of-record meanwhile)" — the frozenNote of
`apps/hub/speech-baseline.json` @ v2 a3cf7a6e repeats it: "The
aria-label-to-LaTeX cleanup remains the disclosed follow-up curation lane."

Base commit: syllabai-resources origin/main `3b2ce8da` (PR #226 merge tip).
Executor: r0 (Super Z, session web-df0238cc-641e-4e8e-ae60-bc44c2aeec2e), trace 1a18a230b37c281d.

## What was cleaned

The gate census classes of `verify_corpus_23a.ts` (span / dollar / textwrap /
multiline / baretext), at corpus SOURCE, across SME-RevisionNotes,
SME-ExamQuestion and SME-Flashcards: Chrome-MathML speech debris
(`open parentheses x plus 5 close parentheses`, `fraction numerator … over
denominator … end fraction`, `presubscript/presuperscript` isotopes,
`circle enclose`, `straight/bold` font runs, `space`-token padding),
broken multi-line code spans, dangling `\text{}` speech-word wrappers
(`\text{numerator}`, `\text{denominator}`, `\text{of}`, `\text{apostrophe}`,
`\text{stretchy}`) and image-alt attributes carrying raw speech.

## Method (all of-record mechanics, zero invented math)

1. **Census-faithful scanner** — Python port of the hub gate's exact regexes;
   validated pre-lane by reproducing the frozen `speech-baseline.json`
   (span 655 / dollar 1 / textwrap 10 / multiline 107 / baretext 9) EXACTLY on
   the v2 content plane (321/321 files).
2. **Of-record engine** — the v2 23a chain imported BYTE-FAITHFULLY
   (`speech-math.ts speechToTexSafe` + `cie_math_extras.ts
   ciePreMap/cieTexRepair/ciePlainCollapse` + `speech-extras.ts
   hasResidualGrammar/stripSpaceTokens`), acceptance law unchanged:
   `katexOk(tex) && !hasResidualGrammar(tex) && !MARK.test(tex)`.
   Lane additions (documented gap-fills only): stretchy-curly-bracket tokens
   (symmetric with the of-record PHRASES siblings), end-script pre-strip
   before bare script words in the collapse (pure ordering), plain-collapse
   balance/banned-word guards, `\text{intersection|union}` → `\cap|\cup` in
   the repair path, and the 23b-style `\text{apostrophe}` → `'` +
   `\text{stretchy}` removal.
3. **Wrapping laws** — speech → `$tex$` (PR-#220 math-string convention);
   plain collapse stays in code spans (23a convention); alt-attribute context
   is plain-first (readable text), md-field lines tex-first (KaTeX-typeset).
4. **NO-GUESS held** — any string the engine cannot decode confidently stays
   verbatim and is filed. Convergence to fixpoint enforced by re-derivation
   rounds (5 rounds; later rounds exist because deterministic replace-all
   splices of identical debris substrings inside longer regions shift the
   longer regions' match).

## Results

Census (source plane, scanner of record): span 6,597 → **1**; dollar 37 →
**5** (all currency-`$` phantom pairs, left per the of-record currency
residual precedent); textwrap 26 → **0**; multiline 138 → **0**; baretext
947 → **67** files (residual engine-NULLs + protected prose false-positives).

Changed files: **1,826** (1,340 SME-ExamQuestion, 244 SME-Flashcards, 242
SME-RevisionNotes). Edits applied: **20,401**. Battery: 1,107 changed JSONs
parse clean (0 fails); fence parity and trailing-newline discipline 0
violations; independent KaTeX re-verification of all 1,603 unique converted
strings: **1603/1603 PASS**.

## Residuals (filed, not failures)

- **76 engine-NULLs** (73 alt-field speech lines + 1 span: the
  stretchy-curly/`bold intersection` set-builder) — left verbatim, enumerated
  in `T_TEXTDEBRIS_1_RESIDUAL.json`.
- **2 currency-`$` phantom pairs** (cie-as-business-23 costs: `$ 675 space
  over denominator $`, `$ 30 m over denominator $`) — left per the of-record
  rule that prose currency `$` signs in accounting/business/economics bodies
  are corpus-side content (RN-RECONSUME-1 disclosure).
- **22 prose false-positives** — lines where gate-vocabulary words appear in
  genuine biology prose ("the end cell walls"), a noise class baked into the
  gate's baretext census of record; protected, not touched.

## Not in this lane (queued separately of record)

- The v2 hub-content consume + `speech-baseline.json` re-freeze DOWNWARD —
  happens at the NEXT corpus consume (the derivation engines re-run); this
  lane makes zero v2 contact by design (fix-at-source doctrine, GATE-2
  precedent).
- The broken-`^{ }`/empty-`\frac{1}{ }` reconstruction class (e.g.
  igcse-further-maths-19 integration arrays) — speech artifacts removed
  census-side, structure untouched; reconstruction is a mark-scheme
  evidence lane, not a mechanical decode.
