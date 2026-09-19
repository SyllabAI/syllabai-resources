# T-SPEC-9 — operator round: the no-guess tail resolved in-house

Operator instruction (Nawaf Al Hussain Khondokar, 2026-09-19, IM):
**"Dont upstream. Fix it yourself like before."** — i.e. resolve the
remaining no-guess tail with our own verdicts, exactly like the
T-SPEC-2e chemistry overrides; **no new upstream tickets were filed**.
PMT (PhysicsMathsTutor) excluded as a source throughout.

## 1. Starting point

After T-SPEC-8 the verify allowlisted **1,109 uncoded parts** across 23
lanes (390 distinct SME tags). Three honest categories:

1. tags whose target statements exist but were never verdicted
   (T-SPEC-7 index-repair recoveries, conservative 'no standalone
   statement' pendings later shown to be wrong);
2. tags whose content the published print genuinely lacks
   (PDF-verified) — nearest-neighbour override territory;
3. one qualification with a true parse gap (economics).

## 2. igcse-economics parse repair (t_spec_9_parse_repair.py)

The v1 lettered-table extractor only matched `a)` at visual-line start,
but the 4EC1 print sets each topic's FIRST lettered sub-statement inline
after the topic heading (e.g. "1.1.1 The economic problem a) The problem
of scarcity ..."). Those 14 rows were silently dropped, which is exactly
why the T-SPEC-7 economics verdicts pended fiscal policy, the basic
economic problem, factors of production, cost types, macro objectives
and friends. Repair: the 14 rows inserted verbatim (page + oy provenance,
flag `t-spec-9-parse-repair`), canonical bundle + graph YAMLs rebuilt;
registry 94 -> **108** rows. Existing ids untouched.

## 3. Verdicts (t_spec_9_verdicts.yaml + t_spec_9_apply.py)

- **148 tag ids** verdicted across 22 lanes, **171 (tag, lane)
  resolutions** in total, tiered:
  - `P2_operator_content_join`: 116
  - `S0_operator_override`: 35
  - `R1_parse_repair_statement_join`: 20
- econ joins land on the restored rows (verbatim wording);
- maths-a / english-lit / geography / business joins are operator content
  joins onto existing statements (tier `P2_operator_content_join`);
- content absent from the published print takes `S0_operator_override`
  (nearest neighbour, documented mismatch note) — including the
  corrections of two wrong T-SPEC-7 claims: graph transformations
  (translations/reflections/stretches of y=f(x)) ARE covered by 4MA1
  3.3B/3.3C, and distribution comparison by 6.2B;
- unit-pool pendings on the modular lanes resolve cross-unit where the
  parts' content lives in the sibling unit's statement list
  (verify's full-registry code check supports this; each case is
  flagged `cross_unit`).

## 4. Part-level overrides (t_spec_9_part_overrides.yaml, 2e pattern)

- **71 parts** in ial-physics-19 (WPH13/WPH16 experimental-method
  questions) plus 4 per-part refinements (2 electrostatics, 1 Van der
  Graaff, 1 economics opportunity-cost definition). The IAL print
  carries no numbered unit-3/6 statements (PDF-verified, T-SPEC-5), so
  each part carries the operator-approved nearest neighbour — the
  core-practical/theory statement of its experiment in context — while
  the 56 practical-skills tag ids stay honestly unresolved in the
  sidecars.

## 5. Result

- verify: **ALL GATES PASSED** — 39 courses, 27,700 parts, allowlisted
  no-guess tail **1,109 -> 0** (every exam part now carries codes);
- spec-links rebuilt: 45,501 items, **36,743 coded** (was 35,555;
  question parts 26,867/26,867 = 100%);
- unresolved tag ids remaining: 258 — every one references
  **zero** uncoded parts (0 learner impact); they stay pending with
  honest reasons (no-guess discipline), dominated by the 56 IAL
  practical-skills tags, english-lit aspect-only pages and
  GCSE-bridge content absent from the printed specifications.

## 6. Per-lane resolutions (method T-SPEC-9) and remaining tail

| lane | T-SPEC-9 resolves | unresolved ids (0 parts) |
|---|---|---|
| ial-biology-18 | 0 | 0 |
| ial-chemistry-17 | 1 | 0 |
| ial-further-maths-18-further-pure-1 | 0 | 0 |
| ial-maths-20-decision-1 | 4 | 3 |
| ial-maths-20-mechanics-1 | 2 | 2 |
| ial-maths-20-mechanics-2 | 1 | 1 |
| ial-maths-20-pure-1 | 5 | 1 |
| ial-maths-20-pure-2 | 3 | 1 |
| ial-maths-20-pure-3 | 1 | 0 |
| ial-maths-20-pure-4 | 1 | 1 |
| ial-maths-20-statistics-1 | 0 | 0 |
| ial-maths-20-statistics-2 | 0 | 0 |
| ial-physics-19 | 0 | 56 |
| igcse-accounting-17-financial-statements | 2 | 3 |
| igcse-accounting-17-introduction-to-bookkeeping-and-accounting | 9 | 8 |
| igcse-biology-19 | 0 | 1 |
| igcse-biology-modular-24-unit-1 | 0 | 0 |
| igcse-biology-modular-24-unit-2 | 0 | 1 |
| igcse-business-19 | 4 | 12 |
| igcse-chemistry-19 | 0 | 0 |
| igcse-chemistry-modular-24-unit-1 | 0 | 4 |
| igcse-chemistry-modular-24-unit-2 | 0 | 4 |
| igcse-economics-17 | 22 | 10 |
| igcse-english-literature-16 | 25 | 77 |
| igcse-further-maths-19 | 0 | 2 |
| igcse-geography-19 | 4 | 8 |
| igcse-ict-17 | 0 | 4 |
| igcse-maths-a-18-foundation | 11 | 5 |
| igcse-maths-a-18-higher | 21 | 4 |
| igcse-maths-a-modular-24-foundation-unit-1 | 7 | 4 |
| igcse-maths-a-modular-24-foundation-unit-2 | 7 | 5 |
| igcse-maths-a-modular-24-higher-unit-1 | 15 | 3 |
| igcse-maths-a-modular-24-higher-unit-2 | 16 | 2 |
| igcse-physics-19 | 0 | 2 |
| igcse-physics-modular-24-unit-1 | 8 | 0 |
| igcse-physics-modular-24-unit-2 | 2 | 1 |
| igcse-science-double-award-17-biology | 0 | 0 |
| igcse-science-double-award-17-chemistry | 0 | 1 |
| igcse-science-double-award-17-physics | 0 | 32 |

## 7. Mechanics

- decision records: `scripts/t_spec_9_verdicts.yaml` (id_verdicts,
  T-SPEC-8 format + official_id/official_wording/cross_unit) and
  `scripts/t_spec_9_part_overrides.yaml` (2e pattern, idempotent);
- applier: `scripts/t_spec_9_apply.py` (fail-closed: pair-checked
  registries, population closure, no-overwrite protection with an
  explicit `refinement` escape for the 4 per-part upgrades);
- parse repair: `scripts/t_spec_9_parse_repair.py` +
  `build_canonical.py igcse-economics` + `emit_graph.py igcse-economics`;
- audit trail: `graph/reports/T_SPEC_9_PARSE_REPAIR.json` (14 added rows
  with before/after text) and `graph/reports/T_SPEC_9_APPLY.json`
  (idempotency re-run as committed proof).
