# P2F — delegated self-review record (T-VIDEOMAP-P2F)

Executed 2026-11-12 under the standing ruling (owner chat 2026-11-09 "approve and review yourself"; owner chat 2026-11-12 "Go").

## 1. Verdict

| course | rows | course-anchor (paper-code, high) | topic-anchor | rejected | notes |
| --- | --- | --- | --- | --- | --- |
| ial-biology-18 | 16 | 16 | 0 | 0 | topic lane honestly empty (see §4) |
| ial-chemistry-17 | 34 | 17 | 6 medium + 11 low | 0 | richest pool: Edexcel GCE topic-title matches |
| ial-physics-19 | 32 | 32 | 0 | 0 | topic lane honestly empty (see §4) |
| igcse-chemistry-19 | 8 | 8 | 0 | 0 | the owner's 4CH1 ask (Exam Essentials 6 + Sergei's 1 + A-star 1) |
| **total** | **90** | **73** | **17** | **0** | 90/90 oEmbed-verified |

Verdicts per course in `owner-review-verdicts.p2f.json` (task T-VIDEOMAP-P2F); approved rows flipped `reviewed:true` (reviewer `delegated-self-review`); drafts now `owner-reviewed-external`.

## 2. Programmatic checks (all rows)

- anchor invariants: level ∈ {course, topic, subtopic, subject}; course anchors ref = the course; topic/subtopic rows carry `specs:[]` + `lessonRef:null`
- paper-code rows: the claimed qualification code re-verified against the title by regex at review time; confidence high; `boardMismatch:false` (same-board)
- topic rows: containment evidence present in the row; confidence ∈ {medium, low}; `boardMismatch` consistent with the wording source (CIE/AQA/OCR/GCE-worded → true, disclosed in `boardNote` + evidence)
- identity: 90/90 oEmbed (`identityMethod:"oembed"`) + oEmbed **author-vs-provider cross-check** (every channel's author name matched its pool slug)
- sewage re-scan at review: promos, results-day, must-study, shorts/vlog/hashtag titles — zero hits among emitted rows
- duplicates: one p2f row per (video, course); row key `anchorRef|video|rowIdx`

## 3. Topic-anchor rows (17, all ial-chemistry-17)

medium (tier 1, ≥3 informative tokens): EDEXCEL Topic 1 Atomic structure and the periodic table → T2 (1.00) · EDEXCEL Topic 12 Acid-Base Equilibria → T14 (1.00) · OCR B (Salters) Equilibria (acid-base) → T14 (1.00) · OCR A 2.1.2/2.1.3 Amount of Substance… → T1 (1.00) · OCR B (Salters) Formulae, equations and amount of substance → T1 (1.00) · EDEXCEL Topic 5 Formulae, Equations and amounts of substance → T1 (0.75)

low (tier 2, ≥2 idf-distinctive tokens): Intermolecular Forces ×2 → T7 (1.00) · Calculating the pH of a buffer… / Buffers made from a weak acid and a strong base → T14 (0.86) · EDEXCEL Topic 15 Transition Metals → T17 (0.67) · AQA 2.5 Transition Metals → T17 (0.67) · Introduction to transition metals → T17 (0.67) · CIE Topic 9 The Periodic Table — Chemical Periodicity → T2 (0.56) · EDEXCEL Topic 4 Inorganic Chemistry and the Periodic Table → T2 (0.56) · OCR B (Salters) (DM)/(EL) Inorganic Chemistry and the Periodic Table → T2 (0.56)

Borderline kept, disclosed: the two `→ T2 (0.56)` partial-overlap rows share only "periodic table" with the IAL topic title — kept because topic anchors are zero spec weight, the board/wording mismatch is disclosed per row, and the evidence string states exactly what matched. A stricter owner ruling can reject them by video id (`9OabOx8-5uA`, `9S-BPnxa63Y`, `VHB4mjJltw0`, `mMyd3XUdd5Q`) without touching the rest.

## 4. Honest notes

- **Skipped pool**: 4BI1×10 and 4PH1×4 paper-coded Exam Essentials videos exist but their courses (igcse-biology-19, igcse-physics-19) are not P2F targets — available for a later pass.
- **Empty topic lanes (bio, physics)**: no channel in the pool titles IAL bio/physics teaching videos by topic name (unit/paper-session titles dominate; subject names are stopwords by design). Nothing forced; a future lane needs a topic-titled source.
- **Evidence posture**: title-only throughout; no row claims spec coverage; zero-weight enrichment by the granularity accounting rule (`docs/ANCHOR-GRANULARITY.md` §4).
