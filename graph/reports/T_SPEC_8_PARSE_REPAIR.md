# T-SPEC-8 — Parse Repairs for the Flagged Parse-Gap Pendings

Repairs the parse defects flagged by the T-SPEC-6 (IAL maths) and T-SPEC-7
(humanities + maths) verdict rounds, then re-verdicts the pendings those flags
were blocking. Every extracted row is PDF-direct (span-geometry provenance,
page + oy), zero-LLM, and carries flag `t-spec-8-parse-repair`. Existing ids
are never renumbered; lanes reference only ids that exist before and after.

## 1. ial-maths — Appendix-7 notation rows wrongly scoped to D1

The IAL Mathematics spec prints its `Appendix 7: Notation` tables (PDF pages
93-98) as numbered entries `N.M`. The v1 parse attributed them to the
last-seen unit (D1), producing **119 bogus `D1-*` rows**; three of those codes
(3.4, 4.2, 4.4) shadowed the real D1 unit-content rows, whose texts were lost
from the parse entirely. Repair:

- **removed** all 119 notation rows (reference-checked: no lane map,
  spec-link, or verdict record references them);
- **restored** the three real D1 rows from the PDF left column (pages 70-71):

| id | restored text | page |
|---|---|---|
| `IAL_MATHS:D1-3.4` | The nearest neighbour algorithm. | 70 |
| `IAL_MATHS:D1-4.2` | Completion of the precedence table for a given activity network. | 71 |
| `IAL_MATHS:D1-4.4` | Total float. Gantt (cascade) charts. Scheduling. | 71 |

- **re-extracted** the two statements whose text had interleaved the
  right-column Guidance prose (D1-2.1, S2-4.6) and cleared S2-4.6's
  assessment-copy `sub_items`:

| id | repaired text |
|---|---|
| `IAL_MATHS:D1-2.1` | The minimum spanning tree (minimum connector) problem. Prim's and Kruskal's algorithm. |
| `IAL_MATHS:S2-4.6` | Hypothesis tests for the parameter p of a binomial distribution and for the mean of a Poisson distribution. |

The D1 registry is now exactly the 15 real unit-content rows
(1.1-1.2, 2.1-2.2, 3.1-3.4, 4.1-4.4, 5.1-5.3).

## 2. igcse-geography — topic content walks restored

The `heading_bullets` strategy never matched the 4GE1 content pages: detailed
content is printed as a two-column table (Key ideas `N.M` left, lettered
statements `a) b) c)` right), with no bold `N.M` pairs and no `•` statement
bullets. The parse therefore carried only aims/skills fragments and the
topic-descriptor lines used by the T-SPEC-7 T3-style joins.

Repair (`t_spec_8_parse_repair.py`, banded two-column walk): appended **87
statements** across all nine topics (10 per topic for Topics 1-6, 9 for
Topics 7-9), **75 key-idea subsections**, and the six full-width required
case-study lines (e.g. "Case studies of river management in a developed
country and a developing country or an emerging country."). Integrated-skills
footnotes stay excluded (page furniture); the `(N)` markers printed at the end
of statement lines are kept verbatim. Synthesised ids continue the document
counter (`S1.156` … `S9.242`); topic dicts reuse the committed `T1..T9` rows.

## 3. igcse-accounting — content walk restored

Same heading_bullets miss, aggravated by false `Topic N:` matches on the
contents/overview pages (which had mis-attributed the surviving bullet
fragments — `S4.069-S4.072` ratios, `S5.073-078` concepts — to topics 4/5).
Repair: appended the full 4AC1 content walk — **67 statements** (Topics 1-5,
24 `N` subsections, 47 bullet sub-items) with verbatim lettered-statement
text. The old fragment rows are kept (lanes reference them).

## 4. igcse-maths-a / igcse-maths-a-modular — record correction, no parse change

The T-SPEC-7 parse_notes claim that "the igcse-maths-a parse dropped a block
of Higher content-walk statements (surds, …, sectors)" is **wrong**, and this
report supersedes it: every quoted statement was verified verbatim in the
committed linear *and* modular parses (`H-1.4A/B`, `H-1.3A`, `H-2.2C/E`,
`H-2.8A`, `H-3.1C`, `H-4.6A`, `H-4.8B/C`, `H-4.9A`, `H-6.1A-C`, `H-6.3A-D`,
and the `U1H-`/`U2H-` twins). What actually happened: the T-SPEC-7 evidence
packs omitted the Higher-scope rows from the per-lane pools, so the verdict
pass believed the statements were missing and pended 48 (tag, lane) records
on a false justification. The parse is untouched; the verdicts are corrected
instead (below), including `Factorising Harder Quadratics`, whose pending
looked for a Higher `2.2F` that the published walk does not print — the
un-limited Higher statement is `2.2B`.

## 5. Stage-2 re-verdicts (`t_spec_8_verdicts.yaml` + `t_spec_8_apply.py`)

Tier `R1_parse_repair_statement_join` — every resolve quotes the statement
text it joins on (verbatim from the repaired registry); PMT excluded as
source. Foundation-lane and genuinely-absent tags stay pending with corrected
reasons (no-guess discipline).

| lane | resolved before → after | tail before → after |
|---|---|---|
| igcse-maths-a-18-higher | 172 → **197** (+25) | 50 → 25 |
| igcse-maths-a-modular-24-higher-unit-1 | 72 → **87** (+15) | 33 → 18 |
| igcse-maths-a-modular-24-higher-unit-2 | 71 → **79** (+8) | 26 → 18 |
| igcse-maths-a-18-foundation / modular F units | unchanged | reasons corrected (Higher-only statements) |
| ial-maths-20-decision-1 (T-SPEC-6 tail) | 43 → **46** (+3: Total Float, Gantt Charts, Scheduling → restored `D1-4.4`) | 10 → 7 |
| igcse-accounting-17-financial-statements | 6 → **28** (+22) | 27 → 5 |
| igcse-accounting-17-introduction-to-bookkeeping-and-accounting | 42 → **93** (+51) | 68 → 17 |

Accounting tails that honestly remain: aggregation/guide tags (Summary of
Adjustments), content the published spec does not print (mark-up, direct &
indirect costs, discounts, imprest, accounting equation, drawings, bank
statements as documents, limited companies beyond LLP, transfers to the
income statement, recovery of debts written off, cheques/paying-in slips,
balancing off), and the two index-repair-recovered tags without verdict
records.

## 6. Verification

- `sme_spcpt_verify.py`: **ALL GATES PASSED** — 39 courses, 27,700 parts,
  allowlisted no-guess tail 2,062 → **1,109** parts.
- `build_learner_spec_links.py --all`: 45,501 items, **35,555 coded**
  (was 34,521; +1,034).
- Canonical bundles + derived graph YAMLs regenerated for igcse-geography
  (242 points), igcse-accounting (185), ial-maths (243; 239 emitted after the
  pre-existing excluded-points rule).

## 7. Mechanics

- v1 parses (`parsed/<qual>/*.parsed.json`) patched by
  `scripts/t_spec_8_parse_repair.py`; canonical bundles rebuilt with
  `build_canonical.py`; Layer-A YAMLs re-emitted with `emit_graph.py`.
- Full audit trail: `graph/reports/T_SPEC_8_PARSE_REPAIR.json` (every
  added/patched/removed row with before/after text and provenance) and
  `graph/reports/T_SPEC_8_APPLY.json` (per-lane verdict application).
- Ids: existing ids untouched; new ids are doc-order continuations of the
  existing synthesised counters, collision-checked at write time.
