# C41 — §18 HUMAN_VALIDATED Promotion Round — igcse-maths-a (the 73 authored edges)

**Generated:** 2026-10-02T08:10:58+00:00  |  **Baseline:** `2e7b23e3e85cc7b77d8e42390ee50400e04dd443`
**Operator directive:** "fire K2-B (chunk substrate), run the §18 HUMAN_VALIDATED
promotion round over the 73 edges" (2026-10-02, zai-web). The directive is the
operator command §18 requires; the ratifying review artifact is the C39
consolidated operator review (PASS WITH NOTES over all six Lane C packets, GO).

## What this is

The exact-identity §18 round of `C11_ARCHITECTURE.md` §18, executed as the
separate operator gate the C39 verdict record named. All **73 authored
semantic edges** (51
REQUIRES_PREREQUISITE + 11
WRONG_ANSWER_PATTERN + 11
REMEDIATED_BY) now carry `validation_status: HUMAN_VALIDATED` +
`validated_by` + `validated_date` in
`graph/igcse-maths-a/concept_edges.yaml`. The 84 derived PART_OF rows follow
node authority and stay SUGGESTED; the 45 held candidates stay quarantined;
the 82 nodes stay SUGGESTED (node promotion is a separate identity decision,
expansion round).

## Mechanics

- `scripts/c41_maths_a_promote.py` (the only writer of
  `scripts/c41_maths_a_promotions.yaml`): exact 3-token identities only;
  every evidence quote byte-verified under the T-C10 norm before anything was
  written; attribution gate (AI self-attribution fails closed); DC-04-aware
  identity mapping (the 3 store-side `*-SIMPLE-CASES` identities resolve to
  their decision-record origins); idempotent; atomic write.
- `scripts/c41_maths_a_promotion_apply.py` (the gated merge point, G13
  convention): validates every entry, enforces the round contract
  (73/73), and rewrites ONLY the validation fields —
  a structural diff over all 157 rows asserts the non-validation delta is
  exactly zero (T01c analog); meta gains `promotion_record` +
  `promoted_edges`/`human_validated_edges` counts; everything else is
  byte-identical.
- `scripts/c41_maths_a_promotion_check.py` (the c11.13 analog): two-way
  graph ⟷ promotions-record audit against the real repo files.

## Anti-forgery posture

- The AI decision records are byte-untouched (they may never carry
  HUMAN_VALIDATED — G10).
- The promotions record carries `validated_by: operator` (the c11 precedent);
  AI-name patterns fail closed in both tools.
- The graph carries HUMAN_VALIDATED only on exact triples with matching
  promotion entries and exact attribution (the promotion check enforces this
  continuously).

## Pins

| Artifact | sha256_16 |
|---|---|
| `concept_edges.yaml` (post-round) | `3cd7470a1c2307e8` |
| `concepts.yaml` (untouched) | `f4c02fd7d023090d` |
| `spec_command_kinds.yaml` (untouched) | `d3af40ffa36a7db5` |

