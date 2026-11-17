# P14 — channel recon filing lane (the identified pool set)

**Task:** T-VIDEOMAP-P14 · **Authorized:** owner chat 2026-11-16 (the ~31-channel recon request; report
delivered same day: 24 new pools adjudicated T1 16,064 / T2 3,323 / NT 6,003 = 25,390 uploads, 0 overlap,
no new-course exits proposed) · owner chat 2026-11-17 "**Proceed**" (= file it as P14) · **Status:** FILED + PUSHED, **PR #357 opened 2026-11-17** (branch `videos/p14-channel-recon` → main;
the filing session had no write token — push/PR followed same day with an owner-supplied token) —
judgment, enrichment, identity sweep, builder emit and hub gates remain open.

## What was filed

**17 pools inventoried — 24,395 uploads**, enumerated fresh this session over each channel's **uploads
playlist** (the complete public set; the /videos tab alone under-counts channels publishing shorts/streams
— see method note), P11–P13 inventory shape, `enumeratedUtc` 2026-11-17. **0 overlap** against the shipped
union (5,884 video ids across the 96-course video-map corpus on main) **and** 0 overlap against all prior
lane inventories (15,028 ids under `inventory/channels/`) — every pool is genuinely net-new.

Verdicts: **T1 ×10** (8 recon-approved + 2 fresh re-derivations, flagged below), **T2 ×2** (both fresh),
**NT ×5** (recon-approved). Rule-based fresh verdicts came from the classification census
(`scripts/p14/p14_classify.py`): qualification-code regexes (CIE subject codes, Edexcel IAL W-codes,
Edexcel IGCSE 4-codes), textual register families (Edexcel IAL chemistry session units, "Edexcel IGCSE
<subject>", explicit CIE IGCSE literature), session/guidance registers, out-of-spine board markers
(AQA/OCR/IB/NCERT/GCSE...). Where the owner-approved recon verdict exists it STANDS; fresh derivation is
disclosed per pool.

## The pools

| Pool | UC | n | Spine-code titles | Dominant register → routing targets | Verdict |
|---|---|---|---|---|---|
| ETphysics | `UCsFE9IEJ3GfAMeDsbJKDxTQ` | 1,376 | 879 (9702) | CIE 9702 session walkthroughs → cie-a-level-physics-25 + cie-as-physics-25 | T1 (recon) |
| Prosperity Academy | `UCaTL2wQs9r6DJEfKd1S3pBQ` | 1,254 | 1,003 (9702 383 / 9701 338 / 9700 282) | CIE SOLVED session papers → physics + chemistry + biology, AS+A | T1 (recon) |
| Dr Hanaa Assil — Chemistry Teacher | `UCJRXXr3FXswyixXsNVFGXsw` | 432 | 221 (IAL-chem units 134 / Ed-IGCSE 87) | "Unit N <session> AS/A2 Chemistry Edexcel" → **ial-chemistry-17 (44/319 — the largest deficit in the spine)** + igcse-chemistry-19/modular | T1 (recon) |
| Zainematics | `UCRyJNmbPBI-EAVVPrtB7-ww` | 2,850 | 1,445 (0580 410 / 9709 376 / 0606 188 / 9618 158...) | CIE maths+CS umbrella → igcse-maths-25 core+extended, 9709 unit courses, **further-maths-additional-25 (3/77)**, CS AS+A (**7/227, 4/161**) | T1 (recon) |
| Craig'n'Dave | `UC0HzEBLlJxlrwBAHJ5S9JQg` | 946 | 108 (0478) | CAMBRIDGE 0478 numbered series ×108 → cie-igcse-computer-science-23 (26/104); AQA/OCR GCSE register (628 titles) = no-target | T1 (recon) |
| Science with Hazel | `UCMdb23cYgONtCG-zPaWigog` | 950 | 253 (Ed-IGCSE register: bio 81 / maths 72 / chem 46 / phys 46) | Edexcel IGCSE trio + modular-24 + maths-a-18 | T1 (recon) |
| Mega Lecture | `UCixOK6EMomHPJNwzBbvMxPw` | 4,433 | 542 (9701 285 / 9702 127 / 9709 34...) | mixed CIE aggregator + heavy non-qualifier remainder → per-title judgment at enrich | T1 (recon) |
| ExamSolutions | `UCtuvpPNTY1lKAoaVzBrzcLg` | 4,591 | 0 coded / **2,474 old-GCE unit tokens** (C1–C4/M1–5/S1–4/FP1–3), 4,411 session-register | the P9 law binds old-register titles to the IAL unit courses (cross-register) | T1 (recon) |
| Learn With Sir Faizan Pasha | `UC66vaRFHoZyOdpd4Ge9UPyA` | 247 | 119 (9702) | CIE 9702 past-paper walkthroughs → physics AS+A | **T1 (fresh)** |
| CK A-level Physics | `UClPiQq7yZ0-XACtbtGNF8Bw` | 244 | 114 (9702) | CIE 9702 teaching register → physics AS+A | **T1 (fresh)** |
| IGCSESUCCESS | `UCXxbJOZLFMEh304aa4rA-zg` | 279 | 11 (0475-lit 9 / 0500 4) | IGCSE Literature (0475) + First Language English → **cie-igcse-english-literature-21 has NO video-map file — first-content decision point (recon: keep terminal by default)** + english-language-20/25 | **T2 (fresh)** |
| MrAstburyMaths | `UCdtMhz0Yk1TxCFzRM6KXY_w` | 403 | 24 explicit (4MA1 8 / Ed-IG register 16; 162 titles carry the bare IGCSE marker) | Edexcel IGCSE maths predicted papers + tricky-question series → igcse-maths-a-18 (+modular) | **T2 (fresh)** |
| TLMaths | `UCCgGyPD6MYQcHuMIc-Kv-Uw` | 4,577 | 0 (2,843 AQA/OCR markers; 301 old-GCE module names) | OCR/AQA A-level maths — no spine qualification | NT (recon) |
| PHYSICS BY M ANWAR | `UCYGXsjLa0Y3ypLcOaJxHuew` | 1,521 | 0 | NCERT (India) register | NT (recon) |
| TakingTheBiz | `UCIlJ4pk3uzyWoeoBkGs0hxQ` | 155 | 0 | business guidance; no spine qualification | NT (recon) |
| Accounting Lecture | `UCFrY4HuR6uZpI7aG_fkQSAA` | 137 | 1 stray | no spine qualification | NT (recon) |
| The Econ Show | `UCKqc15CncviPGny0CAALcRA` | **0** | 0 | **channel EMPTY at re-verification** — recon observed 3 documentaries 2026-11-16; nothing enumerable now | NT (recon) |

Recon-vs-fresh count deltas (channel drift + methodology: the recon report mixed videos-tab and
uploads-playlist counts; this filing enumerates uploads playlists everywhere): Prosperity 1,149→1,254;
Zainematics 1,449 (videos tab)→2,850; Mega Lecture 3,859→4,433; ExamSolutions 4,551→4,591;
ETphysics 1,374→1,376; TLMaths 4,558→4,577; Craig'n'Dave 842 (videos tab)→946 (incl. 104 shorts);
Science with Hazel 949→950. Dr Hanaa Assil 432 unchanged.

## Re-adjudication groups (over EXISTING inventories, no re-enumeration of covered pools)

- **Allery Chemistry (P2F pool) — 41 candidates REPRODUCED exactly** (`\bCIE\b` over the 364-row pool of
  record): 35 "CIE Topic" revision series titles + 6 old CIE session papers (9701/2x–5x). These are the
  chem increment candidates the recon flagged (recon count 41 ✓).
- **EconplusDal (P11 §6 pool) — NOT REPRODUCED, closed no-change with evidence.** The P11 inventory
  (760) and a fresh enumeration this session (761, +1 new upload since P11) carry **0** CIE/9708/9706
  titles; the recon's claimed 38 CIE/9708 hits could not be re-derived from any enumeration of this
  channel. What the pool actually carries: 129 IB-econ titles (no IB course in the spine — no-target
  confirmed). If the owner's report drew on a different enumeration (shorts/streams, a second channel),
  point at it and the group reopens; `scripts/p14/p14_readjudication.json` carries the full evidence.

## Coverage baselines on main (what the lane moves)

| course | specs | videos | note |
|---|---|---|---|
| cie-a-level-physics-25 | 241/303 | 294 | ETphysics + Prosperity + CK + Sir Faizan + Mega Lecture all land here |
| cie-as-physics-25 | 125/145 | 204 | |
| cie-a-level-chemistry-25 | 267/356 | 141 | Prosperity + Mega Lecture |
| cie-as-chemistry-25 | 197/204 | 218 | |
| cie-a-level-biology-25 | 212/257 | 247 | Prosperity |
| ial-chemistry-17 | **44/319** | 99 | Dr Hanaa Assil unit series — biggest deficit in the spine |
| igcse-chemistry-19 | 119/182 | 109 | Assil + Hazel; modular-24 u1 64/100 |
| cie-igcse-maths-25-extended | 73/178 | 775 | Zainematics 0580 |
| cie-igcse-further-maths-additional-maths-25 | **3/77** | 6 | Zainematics 0606 ×188 |
| cie-a-level-computer-science-19 | **7/227** | 8 | Zainematics 9618 |
| cie-as-computer-science-19 | **4/161** | 5 | " |
| cie-igcse-computer-science-23 | 26/104 | 73 | Craig'n'Dave 0478 series |
| igcse-maths-a-18-higher | 32/188 | 71 | Astbury + Hazel |
| cie-igcse-english-language-20 / -25 | 5/18 · 4/18 | 21 · 18 | IGCSESUCCESS |
| cie-igcse-english-literature-21 | — no video-map file (terminal per P12) | | **owner decision point**: IGCSESUCCESS 0475 series ×9 is the first lit-21 content ever surfaced |

## Ledger — unreconciled recon rows

The 2026-11-17 filing session started from a sandbox recycle: the recon's raw artifacts and the report
file were lost, and 7 of the recon's 24 pool NAMES are not recoverable from the session summary (17 of
24 are filed above; their fresh verdicts were re-derived where the recon row was lost, flagged in the
table). **7 pool slots + 3 unresolved names are reserved pending owner re-supply** (the names are in the
owner chat recon report; no re-request needed beyond pasting them):

- Skip the Tutor — unresolved in the recon (no handle/UC found); needs a URL.
- Bizcon Sessions — recon assumed = BizEdMadeSimple (P12 pool); confirm or supply URL.
- Dr Demina — unresolved in the recon (the UC candidate first tried was an unrelated Indonesian channel);
  needs a URL.
- + 4 further T1 pools (the recon's T1 tier was 14 pools; 10 are filed above) + 3 further small pools —
  names lost, ~1,459 T1 uploads + part of T2/NT unaccounted until re-supplied.

Nothing else in the recon's verdict set is silently dropped: every adjudicated pool either appears in the
table above or in this ledger.

## Method notes

- Enumeration: `yt-dlp --flat-playlist` over `UU<channelId>` uploads playlists, cap 15,000 (the recon's
  4,000-cap truncation fixed). Three transient early-stop fetches (MEGA 500 / Zainematics 300 / CK 100)
  were re-run to completion and cross-checked against playlist-count metadata. ExamSolutions' first
  100-row stop was likewise transient (same UC re-verified at 4,591 via playlist-count metadata).
- Identity: every pool page-verified (`externalId` + `og:title` on the channel page); two pools needed
  the ytsearch owner-reverse fallback (Dr Hanaa Assil, ExamSolutions — both then page-verified).
  The `@SirPasha` handle is a squat (title "rusol"); the pool of record is UC `UC66vaRFHoZyOdpd4Ge9UPyA`
  ("Learn With Sir Faizan Pasha"). "The Econ Show" resolves to og:title "Econ Show".
- The /videos /shorts /streams tab splits are recorded per pool in `work/p14/tabcounts.json` (not
  committed); the inventories carry the uploads-playlist sets.
- Classification + verdicts + overlap + baselines: `scripts/p14/p14_classify.py` → `analysis.json`
  (work dir); the committed re-adjudication artifact is `scripts/p14/p14_readjudication.json`.
- `the-econ-show-uploads.json` is filed with count 0 — the honest record of a channel gone empty.

## Pipeline

`Videos/scripts/p14/`: `p14_pools.json` (pool table) → `p14_resolve.py` (identity) → `p14_search.py`
(ytsearch fallback) → `p14_enumerate.py` (uploads playlists) → `p14_classify.py` (codes/registers/
overlap/verdicts/re-adjudication) → `p14_inventory.py` (inventory JSONs ×17 + readjudication artifact).
Inventories: `inventory/channels/<pool>-uploads.json` ×17.

## Open work (in lane order)

1. Owner: re-supply the 7 lost pool names + 3 unresolved URLs (ledger above); decide the CIE lit-21
   question (open it to IGCSESUCCESS's 0475 series, or keep terminal).
2. Judgment lane (P11/P12/P13 class tables over the T1 pools first: ETphysics, Prosperity, Assil,
   Zainematics, Craig'n'Dave, Hazel, Mega Lecture, ExamSolutions, then T2): route → candidates →
   per-row judgment with the degenerate-bind re-adjudication bar.
3. Enrichment + oEmbed identity sweep + honest-skip ledger (exactly-once disposition of all 24,395).
4. Builder P14 section (before the inherit loop; video-keyed idempotency), hub gates
   (`video-map.test.ts` 16/16 + spec-join census), hub PR — **PR #357 carries the filing; merge needs
   owner review**; the judgment/enrich/builder phases follow on this branch or successors.

**Security note of record:** no token was used or available in the filing session itself (amended
2026-11-17: the push and PR #357 were subsequently opened with the owner-supplied token). The recurring
reminder stands, now **higher** priority: `ghp_rW7z…71xD` is a classic PAT with an extremely broad scope
set (repo, admin:org, admin:*, delete_repo, workflow, ...) exposed in chat repeatedly — **rotation to a
short-lived fine-grained token (contents read/write on the two repos only) is still outstanding** —
replace it before the next ship.
