# TRACKER — the tracking doc of record

> One file that tracks everything: every course, every lesson, every stage.
> Human-readable projection of `tracker.yaml` (the machine twin). Regenerate
> with `python3 scripts/lessonctl.py report --all`. Hand-edits here are
> allowed for narrative notes only — status truth lives in `tracker.yaml`
> via `lessonctl.py tracker` transactions (receipt-anchored).

**Last regenerated:** 2026-10-23 (T-BOOK-037/flip r0 — u1:c05 pack flipped DRAFT → PUBLISHED, operator command trace 1a1658a2da08e5bd) · **Agent convention:** every status
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

(Sections column = `sections[].status: done` count vs spine length.
Boxes = V5 coverage %; Lint = last `lessonctl.py lint` verdict; both fill at S2+.)

### Phases

| Phase | Lessons | Status |
|---|---|---|
| Pilot gate | u1:c01–c05 | **c01 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a162e924c017891; hub re-bake same day); c02 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a163f5c9173aa49); c03 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a164915672f5ba5); c04 authored end-to-end (S4) + pack PUBLISHED (operator flip trace 1a164f4cfb54fb65, live-verified at the production origin); c05 authored end-to-end (S4, 36/36 — the big one) + pack PUBLISHED (operator flip trace 1a1658a2da08e5bd) — PILOT GATE COMPLETE: all five pilot lessons PUBLISHED** |
| Unit 1 rest | u1:c06–c10 | not started |
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

## Decisions log (operator-level, newest first)

| Date | Decision | Source |
|---|---|---|
| 2026-10-22 | Lesson = primary year-round surface; rail stays as PDF companion; PDF untouched | operator "both" (trace 1a1611a346d9725d) |
| 2026-10-22 | CourseLessons lives in syllabai-resources, organized by board/qual/subject; self-improving; any-agent | operator (trace 1a16138fde2c155d) |
| 2026-10-22 | Both scaffold PRs merged (syllabai-v2#291, syllabai-resources#39); operator ordered real authoring of u1:c01 + T-BOOK-033 renderer | operator (trace 1a16150be5190d31) |
