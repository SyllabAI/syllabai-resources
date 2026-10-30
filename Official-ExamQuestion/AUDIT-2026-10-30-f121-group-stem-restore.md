# AUDIT-2026-10-30-f121-group-stem-restore — the group-stem restore wave (+ the class-1 closure re-verification)

**Wave:** F121 (operator order: "19-part drawing-strip wave, group-stem restore") ·
exporter **v5** (converter unchanged at v0.33.0) · branch `t-oeq-groupstem-1`

## The order, resolved

The operator order named two items. Forensics at the current heads
(resources `5f170f987`, v2 `3245de7c9`) resolved them:

1. **The 19-part drawing-strip wave (F111 class-1) was ALREADY CLOSED of record** —
   commit `d8fd8acb` (PR #220, merged 2026-10-29): 73 per-line text-repair
   registrations over the 16 staged QP layers of record (the F98 mechanism, sha1-12
   guarded, repaired=null structural absorption), corpus bytes untouched, zero served
   deltas. This wave re-proved the closure **independently at the current cut**
   rather than trusting the commit message (verify-don't-trust):
   - all 54 chemistry slices re-emitted fresh at converter v0.33.0 from the
     sha-verified staging of record (54/54 exit 0, G0 PDF-sha checks PASS);
   - **20/20 of the C147–C166 of-record pins reproduce on the fresh tree**
     (19 strip guards + the C165 class-2 problem_md guard), each sha256-checked
     against the pinned `problem_md` bytes;
   - the fresh-vs-record census: 42/54 slices clean; the sole topic.json field delta
     is the ONE pre-existing `source_page` artifact the F117 wave already adjudicated
     as local staging drift (2024-06 1C 3(b) prints on p6); assets 414/414
     byte-identical; the remaining questions.md / validation-report deltas are the
     known frozen-report classes (the F113 MS-answer mirrors the of-record reports
     predate, review-queue prose drift — classified, reports frozen per C57/F66/F110).
   No strip work remained. The AGENTS.md Task-25 "remaining reproducibility debt"
   line is superseded by this closure (Task-27 entry records the supersession).

2. **The group-stem restore was still open** — the exporter restored QUESTION stems
   only (F-W15-1): `groups[<letter>].group_stem_md` (567 corpus-wide, all non-empty)
   never reached the learner surface. This wave closes it.

## The group-stem restore

### The census

567 group stems across all 54 slices; 0 unresolvable (every non-empty group stem
maps to a group-first part — the live census law, battery section E); 0 splice-guard
hits (no group stem is already folded into its first part's `problem_md`).

### The adjudication of record (eyeball-gated, fail-closed)

A conservative soup detector flagged 111 stems; every flagged stem was adjudicated
from (a) the stem text itself, (b) the crop-asset inventory of its question
(id/mention/page/part), and (c) — for every verdict that hinged on the crop serving
the SAME printed object — a 150 dpi render of the printed QP page (16 pages,
4-up contact sheets, read at the wave). Verdicts:

- **36 cut verdicts of record** (35 drop-tail + 1 dropSpan+dropTail) in
  `STEM-RESTORE.json` under the group key space `Q<n>.<letter>`: every cut's printed
  object is served by a crop asset of record — bond-energy tables (2019-06 2C 5(a),
  2020-01 2C 5(c), 2020-11 2CR 7(b), 2022-06 2C 7(d), 2023-01 2C 7(b), 2023-11 2C
  7(d), 2024-06 2CR 7(b)), results/data tables whose printed form is cropped
  (2020-01 1C 4(a)/9(d), 2020-11 1CR 9(c), 2020-11 2C 4(c), 2022-01 1C 4(b),
  2023-01 1C 8(a), 2023-11 1C 2(b), 2024-06 1CR 9(a)/12(b), 2024-11 1C 6(a),
  2024-11 2C 5(b), 2026-06 1CR 6(a), 2026-06 2C 2(d)/6(e)), printed graphs/grids
  (2021-01 1CR 6(b), 2021-06 1C 9(b), 2022-01 1C 9(c), 2022-01 2C 3(a),
  2023-11 2C 4(c), 2024-06 1C 9(b), 2024-06 1CR 7(b), 2025-06 1C 9(a), 2026-06 1C
  3(f), 2024-11 1C 5(c)), displayed formulae served by crops (2020-01 2CR 7(c),
  2023-06 2CR 7(c), 2024-11 1C 10(b), 2025-06 1C 9(a)), boxes/particle labels
  (2020-01 2CR 1(a), 2021-11 1C 1(a), 2021-11 1C 6(a)).
- **75 keeps** — the wave-19/20 law: a cut needs crop corroboration, never the
  reverse. The keep set includes every DATA table with no serving crop (isotope
  abundances, percentage compositions, bond energies, results tables the parts plot
  from), every displayed formula with no crop (the only representation), and 8
  detector false positives (clean prose/equations). Spot-verified live:
  2020-11 2CR 2(c)(i) isotope data intact verbatim; 2024-11 1C 9(d)(i) equation
  false-positive restores clean.
- Two presentation laws enforced by the battery: a cut whose pre-cut context dangles
  mid-sentence is refused (2020-01 2CR Q7(c)'s anchor was extended to the intro
  sentence so the served stem ends in complete prose); a non-punctuated complete
  sentence needs the `complete-sentence-keep` marker (2022-06 2C Q7(d) — the
  extraction lost the printed period before the soup; the sentence completes with
  its bond list).
- **3 group entries declare `figures[]`** (2019-06 2C Q5.a, 2021-11 1C Q1.a/Q6.a):
  stem-figure crops re-render AFTER the group stem — the served order matches the
  print (battery section F pins 2019-06 2C Q5(a)(i): stem < aircraft fig < group
  stem < formulae fig < bond-tables fig).

### The exporter (v5)

- `restore_group_stem()` — mirrors F-W15-1: ledger verdicts (dropSpan/dropTail
  fail-closed verbatim anchors, replace) then mechanical cleaning; splice-guard
  against the group-first part's own `problem_md`; group keys
  `<series>/4CH1-<paper>:Q<n>.<letter>`.
- Composition: question stem → undeclared stem figures → group stem → declared group
  figures → part text (print order); group-first parts that are not `parts[0]`
  receive their group stem alone.
- Fail-closed wiring: a group stem with no resolvable part refuses; declared
  `figures[]` must be stem-figure crops of the question's first part on the question's
  first part (else refuse); FIG placeholders refuse on group stems (v1).
- **G-E7 (`g_e7_group_stem_law`)** — the plane law: every group stem must reach the
  served set on its group's first part; a group stem can never vanish, be invented,
  or mis-attach; group ledger keys slice-scoped consumed (the F113 law, lane-scoped
  stale-key refusal); adjudicated cuts must actually cut (the raw soup-carrying stem
  must never reach the served bytes — scoped to the stem because a part's own
  pre-existing text may legitimately repeat soup tokens, the F94 drawing-option
  letter runs).
- Zero-network unit battery `scripts/official_examq_f121_tests.py` (101 checks) +
  CI step in `.github/workflows/scripts-tests.yml`.

## Proof

**Exporter run** at the data cut `main@5f170f98746f4bd21ce8e6b73af02e6a83fa4028`
(G-E5 54/54 staging topics content-identical) against the served bundle of record
(v2 `3245de7c9`):

| gate | result |
| --- | --- |
| G-E5 | 54/54 staging topics content-identical to the declared data cut |
| G-E3 | 54 slices match the MULTI-SERIES constants (4,860 marks) |
| G-E2 | part-sum, markPoints sum-law, spec-code shapes hold |
| G-E1 | **567 deltas == the disclosure exactly** (phase-1 run refused with 567 as designed) |
| G-E1b | set-level identity fields byte-equal, 54/54 |
| G-E6 | questionPart == id-derived label, 2,607/2,607 |
| G-E4 | questions.json byte-identical passthrough (2,605,409 B, 28 SME sets) |
| G-E7 | **567 group stems accounted: 567 restored, 0 splice-guarded, 36 cuts applied, 36 ledger keys consumed** |

Counts unchanged: 54 sets / 477 questions / 2,607 parts / 4,860 marks / 4,161
markPoints / 478 figure crops / 7 honest stubs.

**Disclosure** `scripts/exporter-disclosures/2026-10-30-f121-group-stem-restore-4ch1.json`:
`changed` == the 567 group-first part ids (set-equal both ways against the corpus
group-first universe); the delta field universe is **{problemMd: 567}** — the
group-stem class only; new=0 / gone=0.

**Verify harness** (the consuming-side law): G-E1 census matches the disclosure
exactly (567 parts, problemMd fields); G-E2/G-E3/G-E4 green; **self-test 4/4 seeds
refused**.

**Batteries on the edited tree**: F121 101/101; strip-law 29/29; F116, F117, F118,
F119 all green; G9 gate tests green.

## Standing decisions honored

- The F110 convention: a served-byte wave ships the exporter disclosure + the v2
  companion sync in the same wave (the v2 PR stages official-papers.json + the
  re-stamped manifest with the F121 note of record; importSource.ref = the consumed
  cut, G-E5-proven).
- The corpus of record is untouched: zero `topic.json` bytes move (the group stems
  were always IN the corpus — the exporter dropped them). validation-report.json
  files untouched (the C57/F66 lesson); MULTI-SERIES-REPORT.json untouched.
- The LEDGER.md F121 row + the wave-summary section + the AGENTS.md Task-27 entry
  record the wave; the Task-25 "remaining reproducibility debt" line is superseded
  by the d8fd8acb closure of record.

## Verdict

**The group-stem restore is CLOSED corpus-wide** (567/567 served on their group's
first part, 36 adjudicated cuts applied, the G-E7 plane law standing). **The F111
class-1 drawing-strip debt is VERIFIED CLOSED of record** (d8fd8acb; 20/20 pins
reproduce fresh). The F86-era lead list remains empty; the wave-22 open item is
retired.
