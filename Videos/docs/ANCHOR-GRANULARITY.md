# Anchor granularity: subject / course / topic / subtopic anchors (not only lessons)

Status: **proposal adopted for the P2F lane** (owner chat 2026-11-12: "we can just map videos to topics/subtopics as well… maybe the subject as well"). Builder v2 must land before any anchor row is emitted to content.

## 1. Problem

Today every mapping row must name a `lessonRef` (row key `lessonRef|video|rowIdx`, specs counted per row). Three real content classes do not fit that shape:

1. **Past-paper walkthroughs** — "June 2025 Unit 1 Chemistry Edexcel IGCSE Detailed Solution Paper reference 4CH1/1C … P78950A" is about the whole qualification, not one lesson.
2. **Topic-level revision** — "The whole of Unit 2" covers many lessons.
3. **Subject-level exam technique** — board-agnostic study/technique content.

Current behavior is force-fit (wrong lesson claimed) or drop (content lost). Both are dishonest; the anchor model fixes it without weakening coverage numbers.

## 2. The spine already has the anchors

`curriculum.json` node families: `SUBJECT` → `TOPIC` (e.g. `ial-chemistry-T1`) → `SUBTOPIC` (`ial-chemistry-T1:SUB_`) → `SPEC_POINT` (code `"1.1"`, with `applicability` prose that names the assessing unit code, e.g. "assessed by the Unit 1 examination (unit code WCH11/01)"). So every anchor level below resolves to an existing, validatable spine node — no new ID space is invented.

## 3. Schema

A mapping row gains an optional `anchor` object plus a `kind` tag:

```
anchor: { level: "lesson" | "subtopic" | "topic" | "course" | "subject", ref: "<spine-or-registry-id>" }
kind:   "teaching" | "topic-revision" | "past-paper-walkthrough" | "exam-technique"
```

- `anchor` **absent** → lesson level (fully back-compatible; `lessonRef` + `specs[]` required, as today).
- `topic` / `subtopic`: ref = spine `TOPIC`/`SUBTOPIC` node code, `specs: []`.
- `course`: ref = course id (e.g. `ial-chemistry-17`), `specs: []`.
- `subject`: ref = spine `SUBJECT` node code, `specs: []`.
- Row key v2: `anchorRef|video|rowIdx` (course-scoped as before; for lesson rows `anchorRef` = `lessonRef`).

## 4. Accounting rule — the guardrail that keeps coverage honest

**Only lesson-level rows count toward spec-point coverage.** Registry numerators, per-course "specs covered / total" and every dashboard number are computed exactly as today. Coarse anchors render but count **zero** spec points. A 20-minute topic video cannot claim 15 lessons; a paper walkthrough cannot claim a course's coverage. This preserves the P4 discipline (coverage not gamed, nothing forced) while still surfacing the content.

## 5. Evidence ladder (stronger identity verification, not weaker)

| level | binding evidence | confidence | notes |
| --- | --- | --- | --- |
| course (paper-code) | Edexcel paper/qualification code in the title: `4CH1/1C` → `igcse-chemistry-19`; `WCH11/01` → `ial-chemistry-17` U1; `WBI11` → `ial-biology-18`; `WPH12` → `ial-physics-19` U2; `P7xxxxA` paper refs corroborate | **high** | machine-checkable; the spine's own applicability prose names the unit codes, so code → course → unit scope is verifiable. `boardMismatch: false`, `method: "paper-code"` |
| course (multi-qualification paper) | one title, two codes — e.g. "4CH1/1C 4SD0/1C P78950A" (chemistry + double-award science) | high | the many-to-many ruling extends naturally: one video, one row per anchored course |
| topic / subtopic | title names the topic concept explicitly and the concept matches a spine `TOPIC`/`SUBTOPIC` | medium | `boardMismatch` per title evidence |
| subject | genuinely subject-wide, board-agnostic content ("How to revise A-level Chemistry") | medium (cap) | rare; **never** for paper-specific videos |
| lesson | unchanged: title names unique spec content | per current rules | existing P2B bar |

## 6. The owner's 4CH1 example, refined

Owner: "a video where they are solving 4CH1 chemistry past paper — we can just map that video to the subject, right?" — **Yes, map it; but the right anchor is the course, not the subject.** A 4CH1 paper is evidence about exactly one qualification. A subject-level anchor would surface an International-GCSE paper on `ial-chemistry-17` (WCH1x units) and any future GCE 9CH0 course, whose students sit different codes and different content. The paper code **is** the course — and it is *stronger* evidence than anything else in the pipeline (machine-checkable, `boardMismatch: false`). Subject anchors stay reserved for subject-wide technique/overview content, which is rare.

## 7. Render targets

- course rows → per-course videos page, "Past papers & walkthroughs" shelf (the hub already ships `/courses/[course]/past-papers`)
- topic/subtopic rows → topic sections of the course page
- subject rows → subject-level shelf (rare)
- lesson rows → unchanged

## 8. Sewage filter (extends the existing one)

Still filtered: mark-scheme read-alouds without worked explanation, paper-selling / portal promos, results-day and "guide to 2026 exams" marketing, unworked mark-scheme dumps. Passes: full-paper walkthroughs with worked explanations; unit revision with actual teaching.

## 9. Builder v2 delta

- accept `anchor{level,ref}` + `kind`; validate: topic/subtopic ref must exist in the course spine with the matching family; course ref must exist in the registry; subject ref must be a `SUBJECT` node; unknown anchor → **hard fail** (census assertion extended).
- lesson rows unchanged; coverage counters unchanged (lesson-level only).
- emit `anchor` + `kind` on hub rows; row key v2.

## 10. Draft law unchanged

Draft rows stay `reviewed:false` until verdicts; oEmbed identity verification per video (`identityMethod` recorded, thumbnail-liveness fallback per the embedding ban); `owner-review-verdicts.json` gates entry to `content/`.
