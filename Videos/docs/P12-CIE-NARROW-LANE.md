# P12 — Narrow CIE cluster lane (9609 / 9696 / 8291 / 8021)

**Task:** T-VIDEOMAP-P12 · **Authorized:** owner chat 2026-11-13 "run P12" (after the P11 exit census: spine 106 → 90 covered / 16 honest-empty; owner approved the narrow-scope recommendation) · **Status:** SHIPPED 2026-11-14 — resources PR #353 merged (`ef49f405`) · hub PR #1020 merged (`7c460e93`, all 6 checks green); remote ancestry verified both sides

## What shipped

**119 owner-reviewed rows onto the five remaining CIE-native uncovered courses** from **eleven
channel pools** (3,642 uploads, 0 overlap with the shipped union), emitted by the builder's P12
section (fresh-create before the inherit loop, the P11 shape; **no P12B** — no inherit-child takes
P12 rows). Hub registry + flags: **95 courses**, status `live (T-VIDEOMAP-P3+…+P11+P12)`.

- **Tier B session/paper-code anchors (6):** machine-checkable codes in titles —
  `9609/42/O/N/26` (A-level, The Teaching Student), `9609/22|12/O/N/26` (AS, The Teaching
  Student), `8021` GP session papers May June 2026 Paper 2 / Oct Nov 2025 Paper 1 ×2 (English
  with Ms Irum). method `paper-code`, confidence high, boardMismatch false, specs [] (zero spec
  weight, ANCHOR-GRANULARITY §5/§8).
- **Tier A spec rows (113):** deduped distinctive-token binding rule (df ≤ 3; the duplicate-token
  inflation bug found and fixed on re-adjudication), the **four-gate topic-lecture class**
  (verbatim / multi-uniq / title-token / title-pair — a full-topic lecture binds its topic's
  SPEC_POINTs as ONE multi-spec row at confidence low, disclosed per row), and N.M
  section-marker narrowing (`1.3 River Channel Processes…` → SUB1.3's points). All spec rows
  carry the title-only posture (boardMismatch true, medium/low). Teacher-guidance and technique
  registers excluded as bind targets; degenerate single-generic-token binds ("issues",
  "changing", "rural") re-adjudicated to honest skips on review.
- **Identity:** oEmbed sweep **119/119** author_url channel id == channel-of-record (0 mismatch,
  0 dead, 0 thumb fallbacks).

## The eleven pools

| Pool | n | Disposition |
|---|---|---|
| Cambridge Business Essentials A-level & IGCSE | 143 | 9609 exam-technique register → mostly skips; unit-content rows where titles name specs |
| BizEdMadeSimple | 120 | 9609 topical explainers (Vroom, Boston Matrix, workforce planning…) → spec rows; IGCSE-marked 0450 titles skipped (covered by P11) |
| A Level Business \| Alt Academy | 75 | 9609 AS/A2 unit-content lesson series — the lane's cleanest register; AS-topic rows → cie-as-business-23, Strategy/A2 rows → cie-a-level-business-23 |
| The Teaching Student | 71 | 9609 session-paper predictions with machine-checkable codes (9609/12\|22\|42 O/N/26) → Tier B anchors; advice/prediction register otherwise |
| The Geography Academy | 141 | **9696 structured topic course** — topic-complete lectures bind topic points (four-gate class); N.M section markers; 0460 IGCSE pool skipped (out of lane scope) |
| Virtual Pathways | 349 | **8291 AS EM topic lecture series** (Intro EM ×3, Research & Data ×2, Human Population) → 6 rows onto the AS EM course's topics; the platform's other subjects (9700/9701/Edexcel physics) are out-of-lane honest skips available for future lanes |
| Polymath Institute | 56 | 8291/0680 preparation-course mentions → generic-register skips |
| Mini Lessons | 4 | 8021 short series → generic mention skip |
| English with Ms Irum | 132 | **8021 session papers** (M/J 2026 P2, O/N 2025 P1) → Tier B anchors; comprehension/essay strategy → guidance skips |
| Ace The Exam | 2,500 (cap) | GP topic-list revision guides ("Topic 1 Sport and Leisure" → S1.014 verbatim class) → spec rows; the rest of the mixed IGCSE/O-level pool out-of-lane |
| Miss Cutu Bilingual Help | 51 | 8021 essay/comprehension guidance → guidance skips |

## Honest skips (304, ledgered in `Videos/scripts/p12/skips.json`)

Out-of-lane IGCSE registers (0450/0460/0680 etc.) **118** · no distinctive/spec match at the
df ≤ 3 bar **133** · technique/guidance register **45** · advice/prediction without codes **5** ·
GP non-topic-list content **2** · generic course mention **1**.

## Terminal declaration

With these five exits the honest-empty set goes **16 → 11**, and the remainder is **declared
terminal** for the channel-hunt program: Edexcel IGCSE English language-a-16 papers 1/2/3 +
literature-16 (Mr Salles titles do not bind at spec level), CIE IGCSE English literature-21,
Edexcel igcse-history-17 + CIE cie-igcse-history-18 (ledgered rejects), Edexcel igcse-economics-17
(ledgered rejects), Edexcel igcse-accounting-17 units ×2, and cie-igcse-religious-studies-23
(zero candidates across every sweep). EconplusDal's UK GCE econ pool (760) stays a §6 no-target.

## Gates

- Hub `video-map.test.ts`: **16 pass / 0 fail / 4,389 expects** over the 95-course corpus.
- Spec-join census: **95 courses / 8,775 rows / 7,511 refs / 0 violations** (0 unreviewed,
  0 bad spec refs, 0 dangling videos).

## Exit census per course

| Course | rows | videos mapped | spec points mapped |
|---|---|---|---|
| cie-as-business-23 | 24 (2 anchors + 22 spec) | 24/24 | 16/62 |
| cie-a-level-business-23 | 12 (1 + 11) | 12/12 | 8/116 |
| cie-a-level-geography-21 | 71 (0 + 71) | 71/71 | 153/167 |
| cie-as-environmental-management-20 | 6 (0 + 6) | 6/6 | 62/126 |
| cie-as-english-general-paper-21 | 6 (3 + 3) | 6/6 | 3/73 |

## Ship status

**SHIPPED 2026-11-14.** Resources PR **#353** merged to main at `ef49f405` (sync check success,
33 min — the standard Drive-backup duration); hub PR **#1020** merged to main at `7c460e93`
(all 6 checks green: hub, verify, census, law-readback, coordination, Vercel Preview Comments).
Remote ancestry of both lane heads verified (`ab0ae28b` and `a41f44a0` are ancestors of the
respective mains); hub gate re-run on remote main post-merge: 16/16 pass, 4,389 expects,
registry 95 courses, flags `live (T-VIDEOMAP-P3+…+P11+P12)`. Lane branches:
resources `videos/p12-cie-narrow-uncovered`; hub `t-videomap-p12/run-001`.

**Security note of record:** the ship was executed with the token string `ghp_rW7z…71xD` — the
same string previously flagged for rotation. The owner supplied it again and authorized the
ship; **rotation is still outstanding and remains strongly recommended.**
