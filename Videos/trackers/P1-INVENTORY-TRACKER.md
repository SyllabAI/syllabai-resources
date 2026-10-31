# P1 inventory tracker — Cognito video map

**Task:** T-VIDEOMAP-P1 · **Updated:** 2026-10-31 · **Base commit:** `652ca2d`
**Inventory:** `Videos/inventory/cognito-lessons.json` (`reviewState: draft-p1`)
**Gates:** `validate-inventory.mjs --live 5` → ALL GATES GREEN (2026-10-31)

Append-only, LEDGER style: new facts go down; nothing is silently rewritten.

---

## Per-shelf state (P1 exit)

| Shelf | Syllabus lanes (F189 §3) | Subtopics (found/expected) | Lessons inventoried | Guest-visible videos | Guest-gated | P1 |
| --- | --- | --- | --- | --- | --- | --- |
| `b2-gcse-iedexcel` | `igcse-biology-19` (4BI1) + modular/double-award | 86/86 | 109 | 75 (76 ids) | 34 | ✅ |
| `c2-gcse-iedexcel` | `igcse-chemistry-19` (4CH1) + … | 78/78 | 93 | 64 (65) | 29 | ✅ |
| `p2-gcse-iedexcel` | `igcse-physics-19` (4PH1) + … | 99/99 | 113 | 82 (85) | 31 | ✅ |
| `m2-gcse-iedexcel` | `igcse-maths-a-18-*` (4MA1) | 142/142 | 142 | 117 | 25 | ✅ |
| `b2-gcse-cie` | `cie-igcse-biology-23` (0610) + … | 85/85 | 107 | 75 (76) | 32 | ✅ |
| `c2-gcse-cie` | `cie-igcse-chemistry-23` (0620) + … | 77/77 | 80 | 55 (56) | 25 | ✅ |
| `p2-gcse-cie` | `cie-igcse-physics-23` (0625) + … | 92/92 | 121 | 83 (85) | 38 | ✅ |
| `m2-gcse-cie` | `cie-igcse-maths-25-*` (0580), 0607 lanes | 145/145 | 145 | 117 | 28 | ✅ |
| `b3-alevel-cie` | `cie-as/a-level-biology-25` (9700) | 139/139 | 142 | 62 (63) | 80 | ✅ |
| `c3-alevel-cie` | `cie-as/a-level-chemistry-25` (9701) | 130/130 | 130 | **0** | 130 | ✅ (gated) |
| `p3-alevel-cie` | `cie-as/a-level-physics-25` (9702) | 93/93 | 93 | **0** | 93 | ✅ (gated) |
| **Total** | | **1,166/1,166** | **1,275** | **730 lessons / 740 ids** | **542** | |

Out-of-scope shelves captured anyway (39 total in `cognito-shelves.json`):
AQA/OCR-A/OCR-B/Edexcel-UK GCSE, AQA/OCR A-level, SQA, KS3 — adding boards
later is a config change, not a redesign (plan §3).

## Known gaps & anomalies (honest list)

1. **4 stale sitemap entries** (HTTP 404, recorded as rows with
   `httpStatus: 404`): `b3-alevel-cie_HsWgmekM`, `m2-gcse-cie-h_2.55`,
   `m2-gcse-iedexcel-h_2.55`, `m2-gcse-iedexcel-h_2.61`. Cognito's sitemap
   lists pages it no longer serves. 0.3% of scope.
2. **542 guest-gated lessons** — no video served to a logged-out session
   (render-probe verified; includes the **entire** A-level chemistry and
   physics shelves). See report §4.1 for the coverage table and the decision
   this forces.
3. **50 maths lessons read video-less after ≥ 2 render attempts** (h1 renders,
   no iframe mounts). Some of these may still be slow-hydration artifacts;
   they are marked `noVideoLesson: true` with `renderAttempts` on the row, and
   a re-crawl diffs them monthly (plan §11.4 cadence).
4. **Subtopic ref ≠ lesson ref** on the sciences (spec-section numbering vs
   `topic.lesson` numbering) — alignment must use the lesson's own
   `lessonRef`/title against the spine, never the subtopic ref.

## Decisions needed (blocking nothing in P1)

| # | Decision | Blocks | Owner |
| --- | --- | --- | --- |
| D1 | Guest-gated videos: accept partial coverage / crawl with an account (etiquette change) / ask Cognito (courtesy note → requirements) | P4 A-level chem+phys; P2 maths tail | owner |
| D2 | 0607 International Maths vs 0580 shelf overlap (F189 §11.5) — now has 117 guest-visible videos to diff against the spine | P4 maths | owner |
| D3 | Monthly diff re-crawl cadence (plan §11.4) — cron or manual? | maintenance | owner |

## Next (P2 — first course end-to-end, `igcse-biology-19`)

1. Deterministic pre-pass: `lessonRef` + title-prefix match against spine
   SUBTOPIC/SPEC_POINT codes → draft mappings with `confidence: high` (the
   75 guest-visible 4BI1 videos are the working set).
2. LLM draft pass for the remainder → `confidence: low|medium`, human review.
3. Review file + coverage report in the content-maps `_report` style; only
   `reviewed: true` rows ever reach `content/video-map/<slug>.json` (F189 §5
   Step 4; AGENT.md law 2).
4. House-style patch batch + gates (F189 §8) for the first committed course.
