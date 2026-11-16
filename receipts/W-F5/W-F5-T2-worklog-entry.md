# W-F5-T2 worklog entry (append-ready block)

```yaml
task: W-F5-T2 (build + local land — issue-2 presentation layer for the 34 CIE bundles)
wave: W-F5
origin_trace: 1a1e5c7c2499bf51
trace_id: 1a1e5c7c2499bf51
executed_utc: 2026-11-16
operator: SyllabAI operator (zai-web 1a1e5c7c2499bf51)
order: "W-F5-T2"
verdict: BUILD_STAGED_AND_LANDED_LOCALLY — 15/19 source PDFs re-fetched with exact
  sha1 matches (4 Cambridge re-issues documented as honest unrecovered); R2
  geometry-driven re-recovery restored 40 unique damaged rows from the pinned PDFs
  (42 verdicts; 7 further rows T6-proven for render-side hyphen rejoin; 29 rows
  honestly unrecovered); issue-2 re-issue of the 34 spec_points.json adds text_render
  to all 6,920 rows; gates G-F5-C1..C6 ALL PASS (de-render identity 6920/6920);
  census 0.5 -> 0.6 rider (seq 8, additivity CLEAN). Commits built locally on the
  remote tip; PUSH PENDING OPERATOR ORDER (no fresh credential delegated).
```

## What was done

- Phase A — fetch: 19 quals' syllabus PDFs fetched from the Cambridge URL pattern and
  sha1-verified against the parse_report pins (cache/w-f5/fetch-manifest.json). 15
  exact matches; 4 SHA1-MISMATCH (Cambridge re-issued those files) — their rows are
  NOT recoverable from an unverified source and stay verbatim.
- Phase B — re-recovery: geometry-driven engine (fitz span extraction; sub/sup
  classification by size ratio + baseline offsets vs the line's dominant span;
  column-gap spacing law; artifact-space strip around sub/sup glyphs). Acceptance
  gates: STRICT (insertions only from verified sub/sup span chars; deletions only
  spaces/control-glyphs) and RELAXED (additions from verified evidence only, no
  content lost, reorder receipted). 40 unique rows recovered — e.g. respiration
  equations 'C H O + 6O → 6CO + 6H O' -> 'C6H12O6 + 6O2 → 6CO2 + 6H2O', Avogadro
  '6.02 × 10 particles' -> '6.02 × 1023 particles' (render 10²³), 'CuSO •5H O' ->
  'CuSO4•5H2O'. De-render identity proven 42/42. 29 rows honestly unrecovered
  (multi-column interleaves without clean geometry + the 4 unverified PDFs).
- Phase C — emit: issue-2 emitter (scripts/wf5t2_emit.py) adds `text_render` to every
  row (T1 degree spacing ×6, T4 fraction LaTeX ×1, T5 footer strip ×28, T6 rejoin ×7,
  R2 unicode sub/sup ×40), preserves key/row order, bumps issue to "2", recomputes
  counts honestly; byte-format-identical serialization; per-row position receipts
  embedded in swap-manifest.json. Swap staged at download/w-f5-swap/ with SWAP.md
  sha256 pins.
- Phase D — gates: G-F5-C1..C6 ALL PASS (scripts/wf5t2_gates.py) — de-render identity
  on all 6,920 rows, determinism re-run byte-identical, flags additive-only, topics
  byte-identical, 34-file swap discipline, R2 receipts complete.
- Phase E — census: 0.5 -> 0.6 rider (seq 8) — 34 CIE rows gain bundle_issue "2" +
  text_render true; deep-compare additivity CLEAN (cache/w-f5/census-rider-result.json).
- Phase F — land: commit 1 = exactly 34 modified spec_points.json (one revertible
  commit); commit 2 = records (this receipt + worklog, the T1 design receipts, the
  W-F3 land-confirm receipts, task file status, LEDGER Waves 41-42). Local main
  advanced. PUSH PENDING — no fresh credential delegated this round.
- Filed: receipts/W-F5/W-F5-T2-build-receipt.json + this block.

## Findings recorded, not repaired

- Flags of record undercounted the loss class (5 flagged rows vs 54+ evidenced);
  flags stay untouched; recovered rows carry reparse-2.0 additively.
- 29 candidate rows stay verbatim (multi-column interleaves without clean geometry;
  4 quals with sha1-mismatched PDFs). Their receipts name the evidence gap.
- Operator credential rotation (PAT) remains OUTSTANDING.

## Operator actions (repo-side)

1. Push the two W-F5-T2 landing commits (fresh PAT delegated here, or manual push).
2. Rotate the PAT.
