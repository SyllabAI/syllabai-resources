# P2F — Edexcel-native channel lane (thin IAL science fills)

Mandate: P4 report §2c ("IAL sciences … a future Edexcel-native channel lane is the real fix, not threshold-lowering"); owner chat 2026-11-12 green-lights the lane and the anchor-granularity model (see `docs/ANCHOR-GRANULARITY.md`). Lane code: **P2F**.

## 1. Targets — today's honest thin

| course | specs | P4 state | parent containment (hi55) |
| --- | --- | --- | --- |
| ial-biology-18 | 170 | inherit, ~5–10 rows | 7/170 vs cie-a-level-biology-25 |
| ial-chemistry-17 | 319 | inherit, ~5–10 rows | 19/319 vs cie-a-level-chemistry-25 |
| ial-physics-19 | 171 | inherit, ~5–10 rows | 14/171 vs cie-a-level-physics-25 |
| igcse-chemistry-19 (4CH1) | — | mapped (lesson rows) | gains paper-walkthrough **course** rows (owner's example) |

Edexcel IAL wording diverges from CIE far beyond the containment threshold — that is why inheritance is thin and why an Edexcel-native source is the real fix.

## 2. Channel recon (2026-11-12, yt-dlp flat enumeration)

Artifacts: `Videos/inventory/channels/p2f-<slug>.tsv` + `p2f-summary.json` (analysis script `scripts/p2f_ednative_recon.py` outside the repo). Overlap baseline: **879** video IDs already present in shipped drafts.

| channel | videos | paper-code titles | units seen | overlap | role |
| --- | --- | --- | --- | --- | --- |
| Exam Essentials (`UC4qJbWvplEpYsKdc5X1hd9w`) | 169 | **69** — ial-chem 10, ial-bio 15, ial-phys 24, igcse-bio 10, igcse-chem 6, igcse-phys 4 | U1–U6 | 0 | full-paper walkthroughs → course anchors via `method: "paper-code"` |
| Sergei's Chemistry (`UClJ5oN30K8OegncMpH7p3tA`) | 61 | 6 (U1, U3–U6) | U1, U3–U6 | 0 | IAL chem detailed solutions + concept videos |
| Allery Chemistry (`c/AlleryChemistry`) | 364 | 0 (playlist-organized by Edexcel GCE topics) | — | 0 | Edexcel concept teaching → topic/lesson anchors, `boardMismatch` disclosed where wording is GCE-specific |
| Omar's Biology Lab (`UCEITENvnLnJ4bRpocLmvSow`) | 17 on /videos tab | 0 | — | 0 | IAL bio walkthroughs exist per search evidence (WBI11/01 titles) — tab undercounts; re-enumerate at execution |

Sample titles (evidence for paper-code binding):

- "May 2026 Edexcel IGCSE Biology Paper 1B (4BI1/1B) Complete Walkthrough | Every Question Explained"
- "Edexcel IAL Physics Unit 2 (WPH12/01) | May 2026 – Section B Walkthrough & Detailed Explanations"
- "June 2025 Unit 1 Chemistry Edexcel IGCSE Detailed Solution Paper reference 4CH1/1C 4SD0/1C P78950A" — multi-qualification paper (4CH1 chemistry + 4SD0 double-award): one video, one row per anchored course
- "Unit 6 Jan 2026 Edexcel IAL Chemistry Detailed Solutions P79138A WCH16/01"

## 3. Expected lane shape

- ~90–120 **course-anchor rows** (past-paper walkthroughs: 69 paper-coded on Exam Essentials + Sergei's coded solutions + Omar re-check), each with `method: "paper-code"`, `kind: "past-paper-walkthrough"`, confidence high, `boardMismatch: false`.
- Bounded **topic-level rows** from Allery/Sergei concept teaching where the title names the topic concept (bar: `ANCHOR-GRANULARITY.md` §5).
- Zero overlap with the 879 shipped IDs confirmed across all four channels.

## 4. Execution plan (next session)

1. Re-enumerate Omar's Biology Lab (search-discovered; /videos undercounts) and screen "A-star Solution" and the WPH11 walkthrough channel seen in search results.
2. oEmbed identity sweep on every selected video (fallback: thumbnail-liveness + uploads-playlist per the embedding ban); `identityMethod` per video.
3. Mapping: paper-code rows via the exact code→course table (`ANCHOR-GRANULARITY.md` §5); teaching rows at the topic/lesson bar; sewage filter extended (mark-scheme read-alouds, promos, results-day content).
4. Drafts: `video-map.draft.external-p2f.json` per target course with the anchor schema, `reviewed:false`; review file + delegated self-review per standing law.
5. Builder v2 (anchor support, `docs/ANCHOR-GRANULARITY.md` §9) → emit → hub verification.

## 5. Exit gate

Every thin IAL science course gains either paper-walkthrough course rows, topic-level rows, or a recorded honest reason; no row anywhere sits below its evidence-ladder level; coverage numerators remain lesson-level-only.
