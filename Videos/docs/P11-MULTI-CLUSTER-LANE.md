# P11 — Multi-cluster uncovered-course lane (fourteen channel pools)

**Task:** T-VIDEOMAP-P11 · **Authorized:** owner chat 2026-11-13 "lane P11" · **Status:** executed 2026-11-13

## What shipped

616 owner-reviewed rows onto 33 courses from **14 channel pools** (3,116 uploads, 0 overlap with
the shipped union), emitted in two builder sections (P11 before the inherit loop; P11B for the
inherit-child `cie-as-physics-25` after it, the P7B shape with the P2B video-keyed idempotency
wipe). Hub registry + flags: **90 courses**, status `live (T-VIDEOMAP-P3+P4+P5+P6+P7+P8+P9+P10+P11)`.

- **Tier B course anchors (33):** machine-checkable syllabus/paper codes in titles —
  `9708/41` exam walkthrough (EnhanceTuition → cie-a-level-economics-23), `0455` / `0620` session
  papers (IGCSE Online), `WDM11` (Mindful Maths → decision-1), `WMA11-14` (Mindful Maths → ial
  pure 1-4), `4MA1` papers (Mindful Maths → igcse-maths-a-18-higher). method `paper-code`,
  confidence high, boardMismatch false, specs [] (zero spec weight, ANCHOR-GRANULARITY §4/5/8).
- **Tier A spec rows (583):** distinctive-token pre-pass (df ≤ 3) + explicit-code class tables
  (IAL FP1 = the P10 table; D1 chapter table; CIE 0500 skill directs; 4EA1 paper-structure
  directs) + section-marker narrowing (`N.M` CIE chapter series) + Chapter-N narrowing (verified
  syllabus-structured igcse-online series). Teacher-guidance spine specs excluded as bind targets.
  Cross-register rows (Yi CP1 → IAL FP1; CIE content → Edexcel IGCSE ICT/Business/Geography)
  carry `boardMismatch: true`; confidence medium (distinctive) / low (disclosed higher
  title-only bar).

## The fourteen pools

| Pool | n | Disposition |
|---|---|---|
| EnhanceTuition | 307 | CIE 9708 econ → cie-a-level-economics-23 (73 rows); 9706 accounting → cie AS+A accounting |
| EconplusDal | 760 | **honest no-target** — UK Edexcel GCE econ 9EC0; no Edexcel econ qualification in the spine (§6, disclosed; GCSE-econ titles 0) |
| Yi MakesItEasy | 175 | 0460 geo, 0450 business, **Further Maths CP1 series → IAL FP1 cross-register (44)** |
| Cambridge IGCSE/AS/A Study Materials | 175 | 0450 business chapter series + 0417 ICT chapter series |
| James Gan | 136 | 9618 AS/A CS chapters, 9702 physics chapters (parent + P11B child), 9709 maths |
| IGCSE Online | 65 | 0455 econ chapters + Tier B papers, 0478 CS, 0620/0625/0580 increments |
| IGCSE Computer Science | 56 | 0478 topical past-paper solutions → cie-igcse-computer-science-23 |
| Purple Shirt History | 69 | 0470 rows re-adjudicated course-level (below); 0409/9489 honest no-target |
| Mindful Maths | 117 | **IAL D1 WDM11 chapter course → decision-1's first rows** + WMA/4MA1 paper anchors |
| Cambridge Accounting | 24 | 0452/9706 register-explicit |
| AR Accounting | 46 | 0452/9706 |
| EVM With Dr Mohamed Saber | 15 | 0680 EM chapters → cie-igcse-environmental-management-25 |
| Mr Salles Teaches English | 1,163 | CIE 0500/0522 series → cie-igcse-english-language-20/25; GCSE/AQA register honest skip |
| The iGCSE Geographer | 8 | 0460 case-study rows |

## Honest ledger

- Route skips 2,466 (exactly-once disposition of all 3,116): EconplusDal 760 (§6), GCSE-English
  register 170, CIE ESL 0510/0511 54, CIE A-level history 9489 + O-level US history 0409,
  predicted/guess papers, whole-subject summaries, no-marker misc.
- Judgment unmapped 429 (routed-but-unmapped, honest) + 36 re-adjudicated drops (degenerate
  single-token binds caught on review: `'behind'/'debate'/'big'/'time'/'russia'/'coding'/'issue'`
  class catches, incl. the teacher-guidance-spec attractor on cie-a-level-computer-science-19).
- **Three courses re-adjudicated course-level to honest unmapped** and stay honest-empty:
  `igcse-history-17`, `cie-igcse-history-18` (0470 content follows the 20th-century syllabus;
  this spine is the 19th-century-European core), `igcse-economics-17`.
- Zero-row P11 targets stay honest-empty with ledgered rejects: the three above plus
  `cie-a-level-maths-20-pure-1` / `cie-as-maths-20-pure-1` (whole-module summaries only).
- Still uncovered after P11 (16): igcse-accounting-17 ×2, igcse-economics-17, the three Edexcel
  IGCSE English Language A papers + igcse-english-literature-16, igcse-history-17,
  cie-a-level-business-23, cie-a-level-geography-21, cie-as-business-23, cie-as-english-general-paper-21,
  cie-as-environmental-management-20, cie-igcse-english-literature-21, cie-igcse-history-18,
  cie-igcse-religious-studies-23.

## Gates

- Identity: **oEmbed 439/439 author == channel-of-record** (0 mismatch, 0 dead, 0 thumb fallbacks).
- Hub tests: **video-map.test.ts 16/16 pass (4,368 expects over 90 courses)**. Five unrelated
  failures in the full suite (tutor SSE, UGM assets/render, regrade network) reproduce
  identically with the P11 data stashed — pre-existing, not lane-related.
- Spec-join census: **90 courses / 8,656 mapping rows / 6,964 spec refs / 0 violations**.
- Flags: videoMap.courses 90, status live (T-VIDEOMAP-P3+P4+P5+P6+P7+P8+P9+P10+P11).

## Pipeline

`Videos/scripts/p11/`: `p11_make_inventory.py` → `p11_recon_channels.py` (identity +
flat-enumeration) → `p11_route_census.py` (recon census) → `p11_route.py` (disposition) →
`p11_candidates.py` (pre-pass) → `p11_judgment.py` (class tables + narrowing + re-adjudication) →
`p11_oembed.py` (identity sweep) → `p11_assemble.py` (drafts + verdicts). Builder:
`build-content-map-external.mjs` P11 + P11B sections. Inventories:
`Videos/inventory/channels/<pool>-uploads.json` ×14.
