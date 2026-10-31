# P2 alignment tracker — igcse-biology-19 video map

**Task:** T-VIDEOMAP-P2 · **Updated:** 2026-10-31 · **Base:** main @ `4141571` (P1 merged)
**Draft:** `Videos/drafts/igcse-biology-19/video-map.draft.json` (`syllabai.video-map-draft/1`, `reviewState: draft-p2`)
**Gates:** referential integrity · id shape · dup ids · draft law (0× `reviewed:true`) · census recompute · live spot-check 5/5 — ALL GREEN

Append-only, LEDGER style: new facts go down; nothing is silently rewritten.

---

## Headline (P2 draft exit)

| Metric | Value |
| --- | --- |
| Course | `igcse-biology-19` (4BI1, Edexcel International GCSE Biology) |
| Working set | 75 guest-visible lessons / **73 distinct video ids** (76 id references) on `b2-gcse-iedexcel` |
| Spec points drafted | **137 / 176 (78%)** |
| Videos mapped | 72 / 73 (1 honest unmapped: `1.4 Magnification & Units` — no spine statement) |
| Mapping rows | 105 = 73 high / 30 medium / 2 low — **all `reviewed: false`** |
| Guest-gated (D1) | 34 lessons excluded by the draft law, listed in the review file |

## What was done

1. **Enrichment** (`align-extract-lessons.mjs`): fetched the 75 video-carrying
   lesson pages (resumable cache in gitignored `Videos/.cache/p2/`), extracted
   the RSC payload's lesson `description` + `keyPoints` →
   `lesson-enrichment.json` (75/75 descriptions, 71/75 keyPoints).
2. **Deterministic pass** (`align-deterministic.mjs`): lexical evidence scorer
   (title/description/keyPoints token overlap vs spine statements). Refs
   deliberately ignored — see amendment A6: Cognito's chapter numbering is not
   the 4BI1 spec numbering (25/109 ref coincidences, several misleading, e.g.
   Cognito `3.1 Photosynthesis` vs spec `3.1` meiosis).
3. **LLM curation pass** (`align-curation.json`): 74 of 75 lessons mapped with
   per-row confidence + one-line evidence, grounded in keyPoints/description.
   Confidence law: high = statement directly evidenced; medium = in-scope but
   partial/inferred; low = adjacency, must be reviewed.
4. **Build** (`align-build-draft.mjs`): draft video map in `hub.video-map/1`
   shape (distinct-video `videos[]`, per-lesson-binding `mappings[]` with
   draft-only `lessonRef`/`lessonUrl` — amendment A7), coverage block
   **recomputed from mappings** (never hand-written), review file sorted
   low→high, coverage report in the content-maps `_report` style.
5. **Live spot-check** (`align-spotcheck.mjs`): 5/5 random rows — pages
   resolve and still embed the recorded id.

## Honest gaps & anomalies

1. **1 unmapped video** — Cognito `1.4 Magnification & Units`: the 4BI1 spine
   of record has no magnification/units statement (skills content). Not forced.
2. **34 guest-gated lessons** on this shelf (full list in review file §D1):
   the whole of Cognito ch. 11 (skills), most core practicals (10.2–10.15
   except 10.1/10.4/10.8/10.13), all food-production lessons (9.1–9.4,
   9.8–9.9), and singles (2.1, 3.4, 4.4, 6.6, 7.4, 7.5, 7.15, 7.18, 7.19, 8.7,
   8.10, 8.11). This is why T5 (Use of biological resources) sits at 7/20 —
   the gap is D1, not the pipeline.
3. **42 spec points with no video** (honest list in the coverage report,
   grouped by topic): mostly gated-lesson casualties + genuinely uncovered
   statements (e.g. 2.7/2.8 biological molecules — gated lesson 2.1;
   3.26/3.27 sex determination — gated lesson 7.15).
4. **Cognito re-embeds videos** across adjacent lessons (3 pairs) — handled
   per amendment A7; each binding is its own review row.
5. Enrichment `keyPoints` absent on 4 core-practical lessons (10.1, 10.4,
   10.8, 10.13) — descriptions carried the alignment; all four map to
   `practical:` statements cleanly.

## Review load (blocking P2 Step 5 — commit)

| Confidence | Rows | Review mode |
| --- | --- | --- |
| high | 73 | batch-approvable (evidence spot-check) |
| medium | 30 | individual review |
| low | 2 | individual review (`4.16`←8.8, `3.32`←7.7) |

The owner review (plan §5 Step 4) flips rows to `reviewed: true`; the Step 5
commit then writes `content/video-map/igcse-biology-19.json` into the hub via
the house-style patch flow (§5 Step 5, gates §8).

## Next (P3 / P4)

- **P3** — hub surface (`lib/video-map.ts`, Videos tile + lane, flag) can be
  built against this draft behind the flag while review proceeds; the lane
  renders only `reviewed: true` rows, so it ships honest even if review
  shrinks the map.
- **P4** — remaining 10 shelves; the CIE IGCSE biology shelf
  (`b2-gcse-cie`, 75 guest-visible lessons) is the natural second course
  (`cie-igcse-biology-23` spine). The A6 numbering-trap finding likely
  applies to all GCSE shelves — same method, re-verified per shelf.

## Decisions needed (blocking nothing in the P2 draft)

| # | Decision | Blocks | Owner |
| --- | --- | --- | --- |
| D1 | Guest-gated videos (unchanged from P1 tracker) — now concretely costs T5/T3 coverage on this course | Step 5 scope; P4 | owner |
| D4 | Review mode for the 73 high-confidence rows: batch-approve on evidence spot-check, or full per-row pass? | Step 5 | owner |

---

## Ledger 2026-10-31 · caption/transcript re-validation attempt (owner-requested)

**Question:** re-validate the 30 medium + 2 low rows (+ 5 high calibration
samples) against *spoken content* instead of page summaries.

**Result: spoken-content re-validation NOT possible from this environment.**
12 distinct fetch paths attempted, all bot-walled or auth-walled (full log in
`drafts/igcse-biology-19/caption-validation.md` §attempt log): YouTube
datacenter-IP bot wall (python API, 4× yt-dlp clients, real headless Chromium
— watch page renders but `get_transcript` → HTTP 400), Invidious/Piped mirror
network (track lists only; caption bodies empty — no POT upstream), 5
third-party transcript services (429/401/login-wall/Cloudflare loop),
platform-side WebFetch (unsigned timedtext dead). **oEmbed (unsigned)
worked: 73/73 draft videos resolve live with official titles** (new script
`align-oembed-check.mjs` → `drafts/igcse-biology-19/oembed-identities.json`).

Identity cross-check per reviewed row (37 rows,
`caption-validation.json/.md`, worksheet `caption-worksheet.json`):
video-title ↔ lesson-title ↔ spec-statement tokens. Computed 20 consistent /
13 partial / 4 conflict; after manual inspection: **2 conflicts confirmed**
(both 8.8 rows — video `cickRHnPKvc` is officially "How Humans Reduce
Biodiversity", which supports 4.3B-high but weakens 4.12-medium and
4.16-low), 1 re-embed partial (9.7), rest adjudicated consistent (5 high
calibration samples: none flagged). **Recommendation recorded in the
validation report: reject 4.16, treat 4.12 as reject-unless-scanned.**

**Unblock path for transcript-grounded verdicts:** owner-side fetch from a
residential IP (one yt-dlp command in `caption-validation.json`
§unblockPath) → drop `.vtt` files into `Videos/.cache/p2/transcripts/` →
re-run; the worksheet is ready. **No `reviewed` flags touched by any of
this** — draft law intact.
