# TRACKER — the tracking doc of record

> One file that tracks everything: every course, every lesson, every stage.
> Human-readable projection of `tracker.yaml` (the machine twin). Regenerate
> with `python3 scripts/lessonctl.py report --all`. Hand-edits here are
> allowed for narrative notes only — status truth lives in `tracker.yaml`
> via `lessonctl.py tracker` transactions (receipt-anchored).

**Last regenerated:** 2026-10-23 (T-BOOK-039 r0 close chain — f-0011 CLOSED on its defined evidence (census 39951454372 six tables present + battery ALL GREEN 18/18 exit 0 N=7) + f-0013 filed+landed (B5 re-aim, v2 PR #333); prior: u1:c07 authored end-to-end S4 15/15 + law-7 flipped PUBLISHED + law-10 tx; join_set 1.37–1.43 pinned; also lands the regeneration debt: c06 phases-row DRAFT→PUBLISHED (the PR #76/77 flip of record) and the missing f-0012 digest row; trace 1a168863290424f1) · **Agent convention:** every status
change carries `receipt:` pointing at the lesson's `qa/receipt.yaml` (published flips: `qa/flip-published.yaml`).

---

## Course register

| Course | Board | Qual | Lessons | Stage | Notes |
|---|---|---|---|---|---|
| chemistry-4ch1 | pearson-edexcel | international-gcse | 29 planned | scaffold | Pilot of record; spine = 29 chapters ≈ spec sub-sections |

---

## chemistry-4ch1 — lesson board

| # | Lesson (chapter_key) | Folder | Stage | Sections done | Boxes | Lint | Last receipt | Owner (last agent) |
|---|---|---|---|---|---|---|---|---|
| 1 | u1:c01 States of matter | `lessons/u1-c01-states-of-matter/` | S4 (authored; **pack PUBLISHED**) | 13/13 | full allowlist coverage (key-point/exam-hint/misconception ×13; quick-check ×13; worked-example ×2; safety ×2; closing set) | PASS (0/0, stage S4) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S1-S4) | T-BOOK-032 r0 (author) / T-BOOK-033/flip r0 (publish) |
| 2 | u1:c02 Elements, compounds and mixtures | `lessons/u1-c02-elements-compounds-mixtures/` | S4 (authored; **pack PUBLISHED**) | 10/10 | full allowlist coverage (key-point/exam-hint/misconception/quick-check ×10; worked-example ×2; maths-skills ×2; safety ×1; prior-knowledge ×1; cross-curricular ×2; closing set; did-you-know honestly absent — 0 census chunks in chapter) | PASS (0/0, stage S4) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S1-S4) | T-BOOK-034 r0 (author) / T-BOOK-034/flip r0 (publish) |
| 3 | u1:c03 Atomic structure | `lessons/u1-c03-atomic-structure/` | S4 (authored; **pack PUBLISHED**) | 11/11 | full allowlist coverage (key-point ×10; exam-hint/misconception/quick-check ×11; worked-example ×2; maths-skills ×1; prior-knowledge ×1; cross-curricular ×2; closing set; did-you-know + safety honestly absent — 0 census chunks in chapter) | PASS (0/0, stage S4, V5/V6 gates ON) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S1-S4) | T-BOOK-035 r0 (author) / T-BOOK-035/flip r0 (publish) |
| 4 | u1:c04 The periodic table | `lessons/u1-c04-periodic-table/` | S4 (authored; **pack PUBLISHED**) | 12/12 | full allowlist coverage (key-point ×10; exam-hint/misconception/quick-check ×12; worked-example ×2; maths-skills ×1; prior-knowledge ×1; cross-curricular ×2; did-you-know ×2 (census-true); closing set; safety honestly absent — 0 census chunks in chapter) | PASS (0/0, stage S4, V5/V6 gates ON) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S1-S4) | T-BOOK-036 r0 (author) / T-BOOK-036/flip r0 (publish) |
| 5 | u1:c05 Formulae and calculations (part 1) | `lessons/u1-c05-formulae-calculations-1/` | S4 (authored; **pack PUBLISHED**) | 36/36 | full allowlist coverage (exam-hint/misconception/quick-check ×36; key-point ×9; worked-example framing on the book's 8 EXAMPLE sections (in prose — EXAMPLEs are section titles here); safety ×4 (census-true — first multi-safety chapter); prior-knowledge s01; cross-curricular s31; closing set; maths-skills folded into exam-hints (the chapter IS the maths chapter); did-you-know honestly absent — 0 census chunks in chapter) | PASS (0/0, stage S4, V5/V6 gates ON) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S1-S4) | T-BOOK-037 r0 (author) / T-BOOK-037/flip r0 (publish) |
| 6 | u1:c06 Formulae and calculations (part 2) | `lessons/u1-c06-formulae-calculations-2/` | S4 (authored; **pack PUBLISHED**) | 15/15 | full allowlist coverage (exam-hint/misconception/quick-check ×15; key-point ×4; prior-knowledge s01; cross-curricular s06; maths-skills s04+s07; summary+can-you s15 close; did-you-know + safety honestly absent — 0 census chunks in chapter); join_set 1.34C + 1.35C (BOTH C-suffixed — whole lesson is Paper-2-only, chem_only: true, paperRoute=chemistry-only) | PASS (0/0, stage S4, V5/V6 gates ON) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S0-S4) | T-BOOK-038 r0 (author; trace 1a167b943eeacae5) |
| 7 | u1:c07 Ionic bonding | `lessons/u1-c07-ionic-bonding/` | S4 (authored; **pack PUBLISHED**) | 15/15 | full allowlist coverage (exam-hint/misconception/quick-check ×15; key-point ×8 covering all 11 census key_point chunks + Tables 7.1/7.2 as GFM tables; prior-knowledge s01; cross-curricular s12 (lattice–tessellation); maths-skills s06 (LCM charge balancing) + s10 (crossover + totals audit); summary+can-you s15 close keyed to all seven spec points; did-you-know + safety honestly absent — 0 census chunks in chapter); join_set 1.37–1.43 (all seven non-suffixed — papers [1C,2C], double_award_shared true, chem_only: false, paperRoute=core); glossary 11 chips / 16 uses / 0 unresolved | PASS (0/0, stage S4, V5/V6 gates ON) | qa/flip-published.yaml (published flip; authoring receipt: qa/receipt.yaml S0-S4) | T-BOOK-039 r0 (author + flip; trace 1a168863290424f1) |

(Sections column = `sections[].status: done` count vs spine length.
Boxes = V5 coverage %; Lint = last `lessonctl.py lint` verdict; both fill at S2+.)

### Phases

| Phase | Lessons | Status |
|---|---|---|
| Pilot gate | u1:c01–c05 | **c01 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a162e924c017891; hub re-bake same day); c02 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a163f5c9173aa49); c03 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a164915672f5ba5); c04 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a164f4cfb54fb65, live-verified at the production origin); c05 authored end-to-end (S4, 36/36 — the big one) + pack PUBLISHED (operator flip trace 1a1658a2da08e5bd) — PILOT GATE COMPLETE: all five pilot lessons PUBLISHED** |
| Unit 1 rest | u1:c06–c10 | **open — c06 authored end-to-end (S4, 15/15) + pack PUBLISHED (law-7 flip trace 1a167b943eeacae5 / law-10 tx PR #77; the SUBe split completes: part 1 = ten non-suffixed points, part 2 = 1.34C + 1.35C); c07 authored end-to-end (S4, 15/15) + pack PUBLISHED (law-7 flip + law-10 tx, trace 1a168863290424f1; join_set 1.37–1.43, all core, chem_only false); c08–c10 not started** |
| Unit 2 | u2:c11–c18 | not started |
| Unit 3 | u3:c19–c21 | not started |
| Unit 4 | u4:c22–c29 | not started |

---

## Findings digest (auto from findings.jsonl)

| id | type | lesson | severity | status | one-line |
|---|---|---|---|---|---|
| f-0001 | process | u1-c01 | warn | **closed (f-0003)** | section_map key-mapping UNCALIBRATED → calibrated 2026-10-22; full 29-chapter sweep GREEN (341 sections, pages pinned) |
| f-0002 | lint-false-positive | u1-c01 s01 | error | closed | V4 flagged misconception box quoting the wrong idea → lessonctl r0.2 strips :::misconception blocks before scan |
| f-0003 | process | u1-c01 | warn | closed | f-0001 closure receipt: schema of record documented in section_map.py r1; 29 section-maps pre-stored |
| f-0004 | tool-bug | u1-c01 | warn | closed | resume printed 'NEXT: S2 boxes' with 12/13 files missing → lessonctl r0.3 derives NEXT from per-section file reality |
| f-0005 | spec-gap | u1-c01 | warn | closed | box_allowlist omitted quick-check → appended (course.yaml r0.1) |
| f-0006 | tool-bug | u1-c01 | info | closed | tracker printed phantom 'report --write-md' instruction → message corrected; CLI output-instruction audit (lessonctl r0.3) |
| f-0007 | process | u1-c02 | warn | closed | course.yaml spine titles c02/c16 corrupted by unquoted YAML titles (title split into stray key) → both quoted+restored in this PR; system change: quote spine strings, yaml.safe_load before commit |
| f-0008 | process | u1-c03 | warn | **closed (premise invalid)** | hub serving URL of record misidentified — Render core retired by operator decision, serving migrated to syllabai-v2; 503 = retirement steady state, never a publish target (PR #63) |
| f-0009 | process | — | warn | closed | stale retired-origin citations in v2 docs (hub README + t097 workflow) stripped of record in v2 PR #314 with the production origin named: syllabai-hub-v2.vercel.app |
| f-0010 | lint-false-positive | u1-c05 s04/s06/s08/s31/s36 | warn | closed | V4 `\(l\)` regex fired on the legitimate liquid state symbol — chem.yaml r0.1 refines to `\([Ii]l+\)` (the copper(Il)/(Ill) OCR-misread class), in PR #65 |
| f-0011 | platform-regression | u1-c05 (course-wide serving) | **error** | **closed (2026-10-23)** | RESOLVED by the operator's DB work, close on its defined evidence: census re-dispatch run 39951454372 = ALL SIX tables PRESENT at the UNCHANGED endpoint (schema-void healed; 29 chapters ingested, textbook VALIDATED) + battery ALL GREEN 18/18 exit 0 --expect-packs 7 (7 packs published incl. c07); en-route blocker was the B5 probe defect → f-0013 (v2 PR #333 re-aim); blocks leg 0 rows = honest-empty rail-plane residual, not Lesson-blocking |
| f-0012 | tooling-defect | u1-c06 | warn | closed | lessonctl emit emitted contract-ILLEGAL glossarySlugs: null for `glossary: null` front-matter (books-lesson.ts zod = array) — null-safe coercion `fm.get('glossary') or []` (also blockIds/specRefs) fixed in the same PR; c06 pack re-emitted G4 GREEN |
| f-0013 | tooling-defect | — (v2 battery) | error | closed | T-C20 battery B5 probe overreach — probed chapters?chapter= on a route that reads no chapter param (per-chapter honest-absent lives on blocks/checks); B5 could never pass and blocked the f-0011 close; system change: v2 PR #333 re-aims B5 to blocks?chapter=u9:c99 → 200 [] (the route's own law); battery then ALL GREEN exit 0 |

## Decisions log (operator-level, newest first)

| Date | Decision | Source |
|---|---|---|
| 2026-10-22 | Lesson = primary year-round surface; rail stays as PDF companion; PDF untouched | operator "both" (trace 1a1611a346d9725d) |
| 2026-10-22 | CourseLessons lives in syllabai-resources, organized by board/qual/subject; self-improving; any-agent | operator (trace 1a16138fde2c155d) |
| 2026-10-22 | Both scaffold PRs merged (syllabai-v2#291, syllabai-resources#39); operator ordered real authoring of u1:c01 + T-BOOK-033 renderer | operator (trace 1a16150be5190d31) |
