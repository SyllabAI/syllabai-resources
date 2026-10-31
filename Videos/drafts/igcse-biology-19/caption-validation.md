# Caption validation — igcse-biology-19 video map (P2 review support)

**Question this run answers:** do the medium/low bindings hold up against *spoken content* rather than page summaries?
**Honest answer: it could not be tested from this environment.** Every transcript path is bot-walled or auth-walled (12 attempts logged below). What WAS achieved: an **oEmbed identity sweep — 73/73 draft videos resolve live**, and a video-title↔lesson-title↔spec cross-check per reviewed row.

| Identity check | Rows |
| --- | --- |
| consistent | 20 |
| partial | 13 |
| conflict | 4 |

## What the identity check can and cannot prove

- **Can:** each video id is live; each video is a Cognito upload (author: Cognito); the video's own title matches the lesson topic and the bound spec statements. It catches wrong-video and mislabeled bindings.
- **Cannot:** verify clause-level coverage of a statement inside the video runtime (e.g. whether the 46/23 counts are spoken in `fy2F8yFxqOI`). **The medium/low confidence labels stand unchanged; owner review (plan §5 Step 4) is untouched by this file.**

## Transcript attempt log (2026-10-31, all failed or partial)

| # | Path | Result |
| --- | --- | --- |
| 1 | youtube-transcript-api (python) | FAIL — IpBlocked / RequestBlocked (datacenter-IP bot wall) |
| 2 | yt-dlp, player_client=web + android_vr + tv_embedded + web_embedded | FAIL — 'Sign in to confirm you're not a bot' on all variants |
| 3 | real headless Chromium (agent-browser) → youtube.com watch page | PARTIAL — watch page + description render, 'Show transcript' mounts panel, but POST /youtubei/v1/get_transcript → HTTP 400 (bot wall at innertube level) |
| 4 | Invidious inv.nadeko.net | PARTIAL — caption track LIST ok (en auto-generated present), caption BODY always 0 bytes (no POT token upstream) |
| 5 | Invidious yewtu.be / f5.si / privacyredirect / jing.rocks / tux.pizza / dhusch.de / datura / nerdvpn / melmac | FAIL — 403/530/404/DNS-unreachable |
| 6 | Piped pipedapi.kavin.rocks / adminforge / private.coffee / ducks.party / reallyaweso.me / ggtyler / nosebs | FAIL — 5xx / DNS / no route |
| 7 | kome.ai transcript API | FAIL — HTTP 429 persistent; UI behind Vercel Security Checkpoint |
| 8 | tactiq API | FAIL — HTTP 401 (auth required since 2025) |
| 9 | notegpt.io API | FAIL — code 164003 'login expired' (auth required) |
| 10 | youtubetotranscript.com (plain HTTP, then real browser) | FAIL — Cloudflare 403; challenge loop 'Just a moment…' for headless fingerprint |
| 11 | platform-side WebFetch (different egress) | FAIL — unsigned /api/timedtext → 404; watch page served without ytInitialPlayerResponse/captionTracks |
| 12 | YouTube oEmbed (unsigned) | SUCCESS — 73/73 videos resolved (official title + author) |

## Unblock path (10 minutes, owner-side)

YouTube blocks datacenter egress but not residential IPs. Run the one-liner in `caption-validation.json` §unblockPath locally, drop the `.vtt` files into `Videos/.cache/p2/transcripts/`, and the worksheet (`caption-worksheet.json`) + this pipeline re-run verdicts as transcript-grounded.

## Findings from the identity sweep (owner-review relevant)

1. **8.8 binding set re-weighted by the video's own title.** `cickRHnPKvc` is officially "How Humans Reduce Biodiversity" — supports `4.3B` (high), but the `4.12` medium row (CO/haemoglobin) and `4.16` low row (sewage/eutrophication) now look like page-keyPoints bleed-through rather than video content. **Recommend: reject 4.16; treat 4.12 as reject-unless-scanned.**
2. **Re-embed title coverage confirmed for 3.5+3.6** ("Transpiration & Translocation" names both mechanisms) — the two medium rows there can be approved with more confidence than their page evidence alone implied.
3. **9.7 stays medium** — its shared video is titled "Genetic Engineering | GMO" (9.6’s topic); the 5.15 benefits/risks binding rests on keyPoints only.
4. All other computed conflicts (2 rows) were tokenization artifacts (singular/plural, ratio penalties) — adjudicated `consistent` on inspection, notes in the JSON.

## Per-row identity cross-check (37 rows)

| Row | Conf | Specs | Video title (oEmbed, official) | Identity |
| --- | --- | --- | --- | --- |
| 1.1 → `aGDFNZ…` | high | 1.1 | GCSE Biology -  Characteristics of Living Things (Organisms) (2026/27 exams) | consistent |
| 1.2 → `Xzy4Ze…` | medium | 1.4 | Kingdoms of Life - Animals, Plants, Fungi, Protoctists, Bacteria and Viruses | consistent |
| 1.6 → `fp5H3S…` | medium | 2.5B,2.6B | GCSE Biology - What are Stem Cells? Difference Between Embryonic and Adult Stem  | partial |
| 1.14 → `GXGNR1…` | medium | 2.52 | GCSE Biology - Specialised Exchange Surfaces (2026/27 exams) | consistent |
| 2.3 → `YDDjkx…` | medium | 2.25 | GCSE Biology - Nutrition - Carbohydrates | Lipids | Proteins | Vitamins | Minera | consistent |
| 3.1 → `cucQta…` | medium | 2.43B | GCSE Biology - Photosynthesis (2027/28 exams) | consistent |
| 3.3 → `c9aUWH…` | medium | 2.42B,2.43B | GCSE Biology - Structure of a Leaf | Plant Cell Organisation (2027/28 exams) | partial |
| 3.5 → `s06FvG…` | medium | 2.52 | GCSE Biology - Transpiration & Translocation (2027/28 exams) | consistent *(computed: conflict)* |
| 4.1 → `xzDAZU…` | medium | 2.34,2.35 | Aerobic & Anaerobic Respiration (2027/28 Exams) | consistent |
| 4.2 → `Nn4ke0…` | medium | 2.46,2.40B | GCSE Biology - The Lungs & Gas Exchange (2027/28 exams) | consistent |
| 4.3 → `rsA-4T…` | medium | 2.46 | Ventilation Mechanism | How Breathing Works | Inspiration & Expiration (2027/28  | consistent *(computed: conflict)* |
| 4.5 → `3QIvix…` | medium | 2.50 | GCSE Biology - Exercise & Oxygen Debt (2027/28 exams) | partial |
| 5.1 → `c-6Zhc…` | medium | 2.62,2.60 | GCSE Biology - The Circulatory System | The Blood (2027/28 exams) | consistent |
| 5.2 → `k1oCiR…` | high | 2.62 | GCSE Biology - Immune System & Defences | Types of White Blood Cell (2027/28 exa | consistent |
| 5.7 → `gWnIFI…` | medium | 2.71 | GCSE Biology - How the Kidneys Work - (Kidneys Part 1/3) | partial |
| 5.8 → `sRZ7VO…` | medium | 2.73B,2.76B,2.77B | GCSE Biology - Structure of the Kidneys - (Kidneys Part 2/3) | consistent |
| 6.1 → `zvDwNd…` | medium | 2.80,2.82 | GCSE Biology - Homeostasis | Receptors, Coordination Centres, Effectors | Negati | consistent *(computed: partial)* |
| 6.2 → `BnsZo4…` | medium | 2.86 | GCSE Biology - The Nervous System | Reflex Arcs Explained (2027/28 exams) | partial |
| 6.5 → `2fctpb…` | medium | 2.86 | GCSE Biology - The Endocrine System (2027/28 exams) | consistent |
| 7.1 → `kSVKUN…` | medium | 3.2 | GCSE Biology - Sexual & Asexual Reproduction | Gametes (2027/28 exams) | consistent |
| 7.7 → `fy2F8y…` | low | 3.32 | GCSE Biology - DNA Part 1 | Chromosomes & Genome (2027/28 exams) | consistent |
| 7.8 → `T6_wKP…` | high | 3.16B | GCSE Biology - What is DNA? (Structure and Function of DNA) | partial |
| 7.9 → `ubdoUq…` | medium | 3.17B | How are Proteins Made? Transcription & Translation | consistent *(computed: conflict)* |
| 7.11 → `nRAwve…` | medium | 3.31 | GCSE Biology - Meiosis (2027/28 exams) | consistent |
| 7.14 → `uhKqmN…` | medium | 3.25 | GCSE Biology - Family Trees / Family Pedigrees (2026/27 exams) | consistent |
| 7.16 → `4PtOgT…` | medium | 3.22 | GCSE Biology - Variation and Evolution (2027/28 exams) | partial |
| 8.3 → `e8vzQW…` | medium | 4.6,4.8 | GCSE Biology - Food Chains & Predator-Prey Cycles (2027/28 exams) | partial |
| 8.4 → `D1In8W…` | medium | 4.7 | GCSE Biology - Trophic Levels - Producers, Consumers, Herbivores & Carnivores (2 | partial |
| 8.5 → `Tn0_L-…` | medium | 4.7,4.8 | GCSE Biology - Pyramids of Biomass (2026/27 exams) | consistent |
| 8.6 → `wSNSGc…` | high | 4.10 | GCSE Biology - Carbon Cycle & Water Cycle (2027/28 exams) | consistent |
| 8.8 → `cickRH…` | medium | 4.12 | GCSE Biology - How Humans Reduce Biodiversity (2027/28 exams) | CONFLICT-CONFIRMED *(computed: partial)* |
| 8.8 → `cickRH…` | low | 4.16 | GCSE Biology - How Humans Reduce Biodiversity (2027/28 exams) | CONFLICT-CONFIRMED *(computed: partial)* |
| 9.6 → `4Wu86A…` | medium | 5.13,5.16 | GCSE Biology - Genetic Engineering | GMO (2027/28 exams) | consistent |
| 9.7 → `4Wu86A…` | medium | 5.15 | GCSE Biology - Genetic Engineering | GMO (2027/28 exams) | partial *(computed: conflict)* |
| 10.4 → `8Yqbu5…` | medium | 2.13 | Enzymes - GCSE Science Required Practical | consistent *(computed: partial)* |
| 10.8 → `id0aO_…` | medium | 2.23 | Rates Of Photosynthesis - GCSE Science Required Practical | consistent |
| 10.13 → `RhMOCx…` | high | 4.2 | Sampling with Quadrats - GCSE Biology Required Practical | consistent |
