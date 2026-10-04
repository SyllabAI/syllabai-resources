# C42 R5 — §18 Substrate Apply — igcse-maths-a (operator gate 3)

**Generated:** 2026-10-04T03:33:15+00:00  |  **Baseline:** `0ce8610afeb73654dde797e206b3e4bd1656a63d`
**Operator directive:** "Fire r5" (2026-10-04, discord (gateway trace ea5e3ae2488d59498dcc801859715415)).
The directive is the operator command the C42 scope's gate 3 requires; the
gate-2 evidence is the R21 re-gate (Part A 457/3/4, per-class 92.5% / 100% /
100% ≥ 90%; Part B 82/82 decided; mechanical 464/464; X1–X13 all 13/13 PASS).

## What this is

The §18 substrate apply of `C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md` (§4 R5,
§7 gate 3), executed under the C41 exact-identity mechanics fused with the
C13 apply discipline. **832 anchored rows** (the R21-authorized surface:
839 anchored − 3 REJECT − 4 HOLD = 832 = 457 sampled CONFIRM +
375 gate-passed unsampled) now carry
`validation_status: HUMAN_VALIDATED` + a per-row `promotion:` block in
`graph/igcse-maths-a/spec_chunk_mappings.yaml`. Every promoted row was
mechanically re-verified at apply time against a fresh re-chunking
(quote-in-chunk under the shared norm(), chunk sha256_16/heading/chars,
registry membership). The 3 REJECT rows, the 4 H3 HOLD rows and the 82
worklist rows stay SUGGESTED — recorded, never forced. Provenance tiers
are unchanged (RULE_DERIVED); no code attribution moved.

## Mechanics

- `scripts/c42_r5_promote.py` (the only writer of
  `scripts/c42_r5_promotions.yaml`): exact row identities only
  (mapping_id + spec_code + note_path + ordinal + heading + chunk sha256_16);
  every evidence quote byte-verified under the c40 norm before anything was
  written; attribution gate (AI self-attribution fails closed); idempotent;
  atomic write.
- `scripts/c42_r5_promotion_apply.py@1.0.0` (the gated merge point): gate-2 evidence asserts,
  reproduction proof (c40 tool re-run byte-identical to the input store),
  G4-at-apply re-verification of all 832 rows, round contract
  (832/832), and a rewrite of ONLY the validation fields — a
  structural diff over all 921 rows asserts the non-validation delta is
  exactly zero; meta gains the promotion fields; the header status line is
  re-dated (lines 1–2 verbatim).
- `scripts/c42_r5_promotion_check.py` (the c11.13 analog): two-way
  store ⟷ promotions-record audit against the real repo files, with the
  structural re-proof against the pinned baseline blob.

## Anti-forgery posture

- The promotions record carries `validated_by: operator` (the c11 precedent);
  AI-name patterns fail closed in both tools.
- The store carries HUMAN_VALIDATED only on exact row identities with a
  matching promotion entry and exact attribution (the promotion check
  enforces this continuously).
- Zero silent promotion, zero silent repair: the loop's discipline holds at
  the apply — the REJECT/HOLD/worklist surfaces are recorded verbatim below.

## Remaining defect inventory (returns to the operator — scope §7)

REJECT rows (stay SUGGESTED):
- `4MA1-2.6B` — notes/3-sequences-functions-and-graphs/graphs-of-functions/graphical-solutions.json ord 1 (How do I find the coordinates of points of intersection?)
- `4MA1-4.8D` — notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json ord 4 (How do I find the angle between a line and a plane?)
- `4MA1-2.2F` — notes/2-equations-formulae-and-identities/factorising/difference-of-two-squares.json ord 3 (How can the difference of two squares be made harder?)

HOLD rows (c42-heading-only-convention-1 H3 fail-closed — ride a future
round only with explicit per-row operator sign-off; stay SUGGESTED):
- `4MA1-1.7B` — notes/1-numbers-and-the-number-system/ratio-problem-solving/multiple-ratios.json ord 0 (Multiple ratios)
- `4MA1-6.3J` — notes/6-statistics-and-probability/probability-toolkit/relative-and-expected-frequency.json ord 4 (Expected frequency)
- `4MA1-2.2C` — notes/2-equations-formulae-and-identities/expanding-brackets/expanding-single-brackets.json ord 0 (Expanding one bracket)
- `4MA1-3.3F` — notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json ord 0 (Drawing linear graphs)

## Pins

| Artifact | sha256_16 |
|---|---|
| `spec_chunk_mappings.yaml` (pre-apply) | `e2604d6fda06bef7` |
| `spec_chunk_mappings.yaml` (post-apply) | `1cbb9c87fc1be7bf` |
| `c42_r5_promotions.yaml` | `9bad739bd79e5899` |
| `specification_points.yaml` (untouched) | `33d3e5313d37464a` |
| `concepts.yaml` (untouched) | `f4c02fd7d023090d` |
| `concept_edges.yaml` (untouched) | `3cd7470a1c2307e8` |

