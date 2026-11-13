# P9 — Mr Hassaan's Maths Channel completion

Status: **landed** (owner chat 2026-11-13: "There is this channel call Mr Hassan's maths" → recon → "file as lane P9").
Lane: `T-VIDEOMAP-P9 (Mr Hassaan's Maths Channel completion)`.

## 1. What shipped

**3,380 owner-reviewed rows onto 22 maths courses** — the largest video-map lane to date:

- **2,988 course anchors** (Tier B): bound by machine-checkable paper codes in titles, `method: paper-code`, `confidence: high`, `boardMismatch: false` (same qualification), `specs: []` + `anchor{level: course, ref: course}` + `kind: past-paper-walkthrough` — **zero spec weight** per docs/ANCHOR-GRANULARITY.md §4.
- **392 spec rows** (Tier A): the uncoded teaching/tutorial pool under the tightened distinctive-token binding rule (a spec binds only if the title's matched tokens include a token with in-course df ≤ 3), class decision tables with a verdict for every distinctive-candidate row. `method: llm-draft-external`, `boardMismatch: true` (title-only posture), `confidence: medium|low` — never high, so the P4 inherit posture holds.
- **13 maths courses leave the honest-empty set**: `ial-maths-20-pure-1..4`, `ial-maths-20-statistics-1`, `cie-a-level-maths-20-pure-1/2/3`, `cie-as-maths-20-pure-1/2`, `cie-a-level-maths-20-probability-and-statistics-1/2`, `cie-as-maths-20-probability-and-statistics-1` (new video-map files, created fresh) + 9 existing courses grew.

## 2. Pool

`inventory/channels/mrhassansmaths-uploads.json`: **3,150 public uploads** of `Mr Hassaan's Maths Channel` (`@MrHassaansMathsChannel`, channelId `UCTFUlHukTAHgjhS2HT6jNWg` verified by page-HTML `externalId` grep), enumerated flat via yt-dlp on 2026-11-13. **0 overlap** with the 1,556-video shipped union. The channel is **paper-code native** — titles carry the unit code (WMA11-14/WME01/WST01), the session code (9709/31/M/J/22, 0580/23/O/N/25, 9709/M/J/43/19), old-register codes (WMA01 C12 / WMA02 C34), Edexcel IGCSE codes (4MA1/2H, 4MB2, 4PM1) — plus the distinctive topic keywords after the question number.

## 3. Routing (deterministic, `scripts/p9/p9_route.py`)

| Disposition | Count | Detail |
| --- | --- | --- |
| Tier B anchors | 2,433 videos → 2,988 rows | WMA11-14 → pure 1-4 (802); WME01 → mechanics-1 (180); WST01 → stats-1 (141); C12/C34 → two units each, one row per anchored course (200); 9709 P1/P2 → cie a-level + as pair (P4 mechanics precedent), P3 → a-level pure-3, P4 → cie mechanics pair, P5 → p&s-1 pair, P6 → a-level p&s-2 (583); 0580 papers 2/4 → 25-extended (652 — **papers 1/3 (core) do not occur: the channel walks extended papers only, so `cie-igcse-maths-25-core` stays honest-empty at Tier B**); 4MA1/2H → a-18-higher (11); 4MB2 → b-16 (2); 4PM1 → further-19 (1) |
| Tier A spec-row pool | 476 videos | unit-marker routes (427) + board-restricted idf best-of (49) + 4XMA modular-sample (5, appended post-inherit) |
| Honest skips | 241 | Edexcel GCE/9MA0 papers 192 (incl. bare C1-C4 session walkthroughs; ANCHOR-GRANULARITY §6 — a GCE paper is evidence about the GCE qualification, no GCE course in the spine), OCR/AQA/MEI 4, CIE O-Level 4037 2, no-maths-vocabulary 43 |
| `ial-further-maths-18-further-pure-1` | **0 rows, honest** | all 4 idf-routed videos were IGCSE-textbook vectors (Rayner/Pimental) — dropped in judgment as misroutes; the verdicts ledger is the record |

## 4. Identity + judgment

- **oEmbed sweep 2,825/2,825** (`scripts/p9/p9_oembed.py`): every video entering a P9 draft verified live, author `Mr Hassaan's Maths Channel` — **0 mismatches, 0 dead, 0 thumb-fallbacks needed**. `identityMethod` recorded per video entry.
- **Judgment pass over every distinctive-candidate row** (`scripts/p9/p9_judgment.py`, 400 videos / 1,761 candidates): class decision tables per course (topic-marker → spec, verified against the deterministic pre-pass — rules refine, never invent); explicit verdicts: 391 keep + 1 rebind (9709 worksheet re-routed to cie-a-level-pure-1 1.8.4) / 8 full-row drops with reasons / 76 routed-but-unmapped (no distinctive token overlap at the tightened bar) — **84-entry honest reject ledger** per course in `owner-review-verdicts.p9.json`.
- Misbind classes caught: paper-part label tokens (`ii` → "Equation of a straight line" degenerate bind), word-adjacency (`arithmetic` series vs basic-arithmetic tutorial sections), cross-board idf routes (IGCSE-textbook vectors onto FP1, CIE textbook onto IAL), community content ("Answer to sequence question request").
- Rebinds validated against the target spine before write.

## 5. Builder + emit

- `build-content-map-external.mjs`: **P9 section** (22 courses, fresh-create for the 13 new courses, P5-shape append for the 9 existing) placed after P8 and **before the P4 inherit loop**; **P9B section** (the two inherit-CHILD courses with P9 rows — `cie-igcse-maths-25-core`, `igcse-maths-a-modular-24-higher-unit-1`) placed after P7B, the P7B shape. Gates: paper-code rows must carry `anchor{level:course, ref:course}` + `kind: past-paper-walkthrough` + `confidence: high` + `boardMismatch: false` + `specs: []`; spec rows medium/low + `boardMismatch: true` + spine membership.
- Full emit exit 0. Registry 66 courses; flags `videoMap.courses` 66; status template extended to `P3+P4+P5+P6+P7+P8+P9`.
- **Cascade**: P9 spec rows on `cie-igcse-maths-25-extended` and `igcse-maths-a-18-higher` cascade through the committed containment map (+49 inherited rows across their children).

## 6. Gates

| Gate | Result |
| --- | --- |
| Full emit exit 0 | PASS (22 P9 courses + P9B + cascade) |
| Hub `bun test src/lib/video-map.test.ts` | **16/16 pass, 4,227 expect() calls** (corpus-at-rest zod census over all 66 flagged courses; was 1,055 over 53) |
| Independent spec-join census (`scripts/p8/p8_spec_join_census.py`) | **66 courses, 7,622 mapping rows, 5,996 spec refs, 0 violations** (was 53 / 4,193) |
| Hub build + DOM check | see the hub PR receipt |

## 7. Honest-empty after P9

- `cie-igcse-maths-25-core`: stays honest-empty (no core-paper content in the pool; its 5 Tier A rows are topic rows routed by idf, appended post-inherit).
- `ial-maths-20-decision-1`: stays honest-empty (no D1 content in the pool).
- `ial-maths-20-mechanics-2`: stays honest-empty at native level (no WME02 content; the P4 cross-subject rows remain).
- `ial-further-maths-18-further-pure-1`: stays honest-empty (4 misroutes dropped, disclosed).
- Edexcel GCE (9MA0/6663-6666) and OCR/AQA/MEI paper content: no qualification courses exist in the spine — honest no-target skips per section 6 of the anchor granularity spec.
