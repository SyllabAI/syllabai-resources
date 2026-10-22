# TRACKER — the tracking doc of record

> One file that tracks everything: every course, every lesson, every stage.
> Human-readable projection of `tracker.yaml` (the machine twin). Regenerate
> with `python3 scripts/lessonctl.py report --all`. Hand-edits here are
> allowed for narrative notes only — status truth lives in `tracker.yaml`
> via `lessonctl.py tracker` transactions (receipt-anchored).

**Last regenerated:** 2026-10-22 (seed) · **Agent convention:** every status
change carries `receipt:` pointing at the lesson's `qa/receipt.yaml`.

---

## Course register

| Course | Board | Qual | Lessons | Stage | Notes |
|---|---|---|---|---|---|
| chemistry-4ch1 | pearson-edexcel | international-gcse | 29 planned | scaffold | Pilot of record; spine = 29 chapters ≈ spec sub-sections |

---

## chemistry-4ch1 — lesson board

| # | Lesson (chapter_key) | Folder | Stage | Sections done | Boxes | Lint | Last receipt | Owner (last agent) |
|---|---|---|---|---|---|---|---|---|
| 1 | u1:c01 States of matter | `lessons/u1-c01-states-of-matter/` | S1 | 1/13 (real spine pinned r1) | — | PASS (0/0) | qa/receipt.yaml (S0-L0 calibration) | T-BOOK-031 r1 |

(Sections column = `sections[].status: done` count vs spine length.
Boxes = V5 coverage %; Lint = last `lessonctl.py lint` verdict; both fill at S2+.)

### Phases

| Phase | Lessons | Status |
|---|---|---|
| Pilot gate | u1:c01–c05 | S0 scaffolded (c01 demo seed only) |
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

## Decisions log (operator-level, newest first)

| Date | Decision | Source |
|---|---|---|
| 2026-10-22 | Lesson = primary year-round surface; rail stays as PDF companion; PDF untouched | operator "both" (trace 1a1611a346d9725d) |
| 2026-10-22 | CourseLessons lives in syllabai-resources, organized by board/qual/subject; self-improving; any-agent | operator (trace 1a16138fde2c155d) |
