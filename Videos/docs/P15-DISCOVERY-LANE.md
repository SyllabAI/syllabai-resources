# P15 — DISCOVERY LANE (gap-targeted channel search sweep)

**State: SHIPPED 2026-11-20 — resources PR #358 → `c24da20e`, hub PR [`t-videomap-p15/run-001` #1121](https://github.com/SyllabAI/syllabai-v2/pull/1121) → `44058422`; both merged by owner order "Process it" with independent review receipts in the merge commits (resources gates R1–R7, hub gates G1–G8, bun video-map tests 16/16 at 7,191 expects; corrected receipt claims recorded in the receipts — see the corrections bullet below).**
**Authorization: owner, this session — "How about you search for channels and videos to map?" (2026-11-18), opening a discovery lane after the owner-supplied recon list was exhausted by P14.**
**Branch: `videos/p15-discovery` (resources, merged as `c24da20e`). Hub side: `t-videomap-p15/run-001` (merged as `44058422`).**

## Why

The 95-course corpus at hub main (d1aa0a30) carries **10,611 spec points of which 5,900 are mapped — 4,711 unmapped across 85 courses**; no course is at zero rows anymore (the P11–P14 long tail reached every course at least once), so the residual gap is a breadth problem: whole registers whose specialist channels have never been swept. The owner-supplied recon list (24 pools) was exhausted by P14 — 17 filed, 7 names + 3 URLs reserved. Rather than wait for re-supply, this lane searches directly.

## Gap profile of record (computed 2026-11-18, scripts/p15_gap_profile.py)

Top unmapped spec-point deficits at main:

| course | register | mapped/total |
| --- | --- | --- |
| cie-igcse-biology-23 | CIE IGCSE 0610 | 52/388 (336 left) |
| cie-igcse-science-co-ordinated-sciences-double-award-23-biology | CIE 0654 | 34/230 (196) |
| igcse-geography-19 | Edexcel 4GE0 | 10/202 (192) |
| ial-chemistry-17 | Edexcel IAL WCH | 150/319 (169) |
| ial-physics-19 | Edexcel IAL WPH | 10/171 (161) |
| cie-igcse-accounting-25 + -21 | CIE 0452 | 156 + 125 left |
| igcse-maths-a-18 higher + foundation (+ modular-24 units) | Edexcel 4MA1 | 294 + 238 left |
| cie-igcse-environmental-management-25 / cie-as-environmental-management-20 | CIE 0680 / 8291 | 140 + 64 |
| igcse-ict-17 / cie-igcse-ict-21 | Edexcel 4IT0 / CIE 0417 | 130 + 76 |
| cie-igcse-economics-20 + -25 | CIE 0455 | 227 |
| cie-igcse-physics-23 / -chemistry-23 | CIE 0625 / 0620 | 118 / 106 |
| ial-biology-18 | Edexcel IAL WBI | 116 |
| cie-igcse-geography-20 + -25 | CIE 0460 | 188 |
| english-language-20 / -25 | CIE 0500 FLE | 6/18 + 5/18 |
| further-maths-additional-25 | CIE 0606 | 24/77 (53) |
| cie-a-level-economics-23 / -business-23 | CIE 9708 / 9609 | 74 / 72 |

## Method

1. **Gap-targeted sweep** (`scripts/p15/sweep.json`): 24 gap clusters × 1–5 register/code-targeted queries each (`yt-dlp ytsearch15`), harvesting `(channelId, channel, title)` rows; **231 distinct channels harvested, 208 new** after deduping against every prior lane inventory UC + the P14 pool set.
2. **Shortlist** by register density × gap weight → **19 pools** (`scripts/p15/p15_pools.json`). Exam Essentials excluded (P2F pool of record); known channels (Cognito, Omar's Biology Lab, A-star Solution…) skipped by UC.
3. **Identity gate** (`p15_run.py resolve`): every pool's UC verified via the page-identity gate (`externalId` + `og:title` agree) — **19/19 resolved**, zero squats.
4. **Enumeration** (`p15_run.py enum`): flat enumeration of each channel's UPLOADS PLAYLIST (`UU<id>`, cap 15,000) — the P14 methodology; **5,591 uploads across 19 pools, enumeratedUtc 2026-11-19T14:37:11Z**.
5. **Register classification** (`p15_run.py classify`, `classify.json`): textual register families (spine paper codes, session patterns, NT boards) over every title — the P14 textual-classification shape, case-insensitive, incl. the Ed-IGCSE sciences and ICT/CS families and content-level lit markers (`Study Guide for Cambridge iGCSE`).
6. **Inventory assemble** (`p15_file.py`): P11–P14 inventory shape ×19 under `inventory/channels/`.
7. **Overlap law — ALL PASS**: pool ids **0 overlap vs the hub shipped union at main (8,783 ids incl. P14's 2,899)** and **0 overlap vs all prior lane inventories (38,773 ids)** and **0 intra-P15 sharing** (5,591 uploads = 5,591 distinct ids).

## The 19 pools (filing disposition proposal)

**T1 — dense, on-register, judgment-ready (14):**

| pool | UC | uploads | top register families | gap targets |
| --- | --- | --- | --- | --- |
| chem bio by Hosni | UCbf_c1qzrFz6SahAs7TKJMg | 1,466 | 0610 ×342, 0620 ×302, WBI ×213, sessions ×216 | cie-igcse-biology-23 (336 left), ial-biology-18 (116), ial-chem tail |
| The Math Pad | UCNS-d_xDjlYKFINBaE-MWTg | 1,105 | 4MA1 ×197, sessions ×320 | igcse-maths-a-18 (294) + modular-24 units |
| Libra Maths | UCqOw2x-SLHVPc3neC8-XEPw | 859 | 4MA1 ×127, 0606 ×63, sessions ×511 | igcse-maths-a-18, 0606 |
| Learn Today IGCSE | UC0uoFY2OWbKiUqYEJN2EI-Q | 101 | 0625 ×60, 0620 ×27, 0610 ×6 | CIE IGCSE sciences trio |
| CAIE made easier | UC1ZKr11QGaIvcjqEhG24jdg | 140 | 0620 ×28, 0610 ×25, 0625 ×25 | CIE IGCSE sciences trio |
| Science and Stuff | UC_kTsxsNVqnymxIJAERYvuQ | 132 | 0610 ×32, 0625 ×30, 0620 ×28 | 0654 co-ordinated trio (368 left) |
| Nicos Paphitis | UC3M-4-rsKiVHOmxrbHtBvnQ | 234 | 0417 ×121 | cie-igcse-ict-21 (76) |
| Mark Harrison | UCqVek0zpwE2bCmVqQN85k5A | 231 | Ed-IGCSE ICT/CS ×93, 0417 ×58 | igcse-ict-17 (130) + CIE ICT |
| Doctor No Does Science | UCzPtQM9JT0rFC-arf5VTLhw | 175 | WPH ×74 | ial-physics-19 (161, 6%) |
| Taughtly | UCyl0zfsVhR160wDevc0soVg | 104 | 0500 FLE ×69 | english-language-20/25 |
| Dr. Maria Emam | UC0F7m4AzeFmkRuA5iPuBjpw | 59 | 0680 ×55 | cie-igcse-em-25 (140) |
| Everything E.M. | UCi_A5BxLfAsyeMxDj70bEEw | 13 | 0680 ×13 (pure) | cie-igcse-em-25 |
| GEO-HACKS | UCCpbgga572sArqmEzzNF3dQ | 67 | 0460 ×37 | cie-igcse-geography pair (188) |
| Keen Mindz | UCVsjSv0YLczDvKEWr6LHsSA | 64 | 0452 ×64 (100% register) | cie-igcse-accounting pair (281) |

**T2 — thinner / mixed register, judgment with honest-skip expectations (4):**

| pool | UC | uploads | note |
| --- | --- | --- | --- |
| Chemistry & Biology @ Belal Sir | UCSM3sgrTyxAhNsB2RUApIdg | 208 | Ed-IGCSE sciences ×26 + 0620 ×25, but NT(AQA) ×89 — mixed register, per-row judgment |
| Learn Economics with Anjuli | UC61QCkT521pMusL14b4jt1w | 161 | 0455 ×12 + 9708 ×1, rest topic lectures — four-gate class |
| Gilbert Phoon | UCiKFNQ8DfDMeM5d1CmRyw-Q | 126 | 4MA1 ×19 + 0606 ×11 over maths walkthroughs |
| Shawn Hew (maths & sciences) | UC13spM-Zm2weeVbElpDM6lg | 103 | 0620 ×48 + 0606 ×47 — dual subject |

**GATED (1):**

| pool | UC | uploads | note |
| --- | --- | --- | --- |
| Claire's Notes | UCDHUKn14qPhrkV6fBpyOBtw | 243 | 0475 register at content level (~200 poem/prose guides "for Cambridge iGCSE", textual family only ×12) — **folds into the lit-21 owner decision point** alongside IGCSESUCCESS's 9 RESERVED titles; no rows emit until the owner rules |

## Laws

- ANCHOR-GRANULARITY applies in full at judgment (GCE/9MA0, OCR/AQA, IB, NCERT out-of-spine; O-Level register skip; the P9 IAL-cross-register bar; the P13 gate ladder).
- Sweep is search-derived, so nothing here duplicates the reserved recon slots: the 7 lost pool names + Skip the Tutor / Bizcon Sessions / Dr Demina remain **reserved pending owner re-supply** and would join a follow-up tranche, not this one.

## Judgment run (2026-11-18)

The owner's "Continue working" ran the lane on the filed pool set as proposed (T1 x14 + T2 x4; claires-notes RESERVED):

- **Exactly-once disposition of all 5,591 accounts**: 1,033 Tier B anchor rows (over 836 videos) + 529 Tier A spec keeps + 3,983 honest skips + 243 RESERVED lit-0475 = 5,591 (0 collisions).
- **Identity: oEmbed 1,365/1,365 routed videos author == channel-of-record** via UC id (0 mismatch, 0 dead; split of record 1,356 direct oembed + 9 thumb-fallback — oembed HTTPError/URLError with identity verified via the fallback route, ok=true, the P14 XrTzkSfaJBI precedent; the hub-side videos[] entries record identityMethod thumb-fallback for those 9).
- **Emit: 1,562 rows onto 32 courses (21 pre-inherit + 11 P4-children post-inherit via P15B)**; emit exit 0 x2, full re-emit replay machine-checked a no-op modulo timestamps.
- **Coverage deltas of record**: ial-physics-19 10/171 -> 54/171, igcse-maths-a-18-foundation 20/162 -> 65/162, co-ordinated trio 34/230 -> 150/230 + 112/181 -> 141/181 + 118/221 -> 142/221, a-18-higher 36/188 -> 109/188, further-maths-additional-25 24/77 -> 65/77, ict-21 19/95 -> 39/95, ict-17 8/138 -> 22/138, EM-25 2/142 -> 12/142, geography pair +8 each, english-language 6/18 -> 14/18 + 5/18 -> 11/18.
- **Hub gates**: video-map tests 16/16 (7,191 expects; at-rest pins receipt-synced — ial-chemistry-17 517 rows/111 anchors, ial-biology-18 21, ial-physics-19 73, igcse-chemistry-19 66, anchorBuckets ial-physics-19 73); spec-join census 95 courses / 16,198 rows / 58,796 refs / 0 violations; flags status synced to P3..P15 (template + emitted file).
- **Review corrections of record (2026-11-20, independent review receipts in both merge commits)**: spec-confidence split is **319 medium / 210 low** (the run's receipts had said "529 low / 0 medium" — drafts and shipped data agree on 319/210); the P4 inherit loop cascaded **+337 rows onto 14 courses** beyond the 32 direct courses (modular-24 units, foundation via inherit.from igcse-maths-a-18-higher threshold 0.55, the combined-science children; rowsApproved 1,899 = 1,562 + 337, all reviewed:true); enumeratedUtc of record **2026-11-19T14:37:11Z**.

## Open work

1. ~~Merge both PRs (resources #358 + hub #1121)~~ DONE 2026-11-20 — resources #358 → `c24da20e`, hub #1121 → `44058422`, independent review receipts in the merge commits.
2. ~~lit-21 decision~~ **DECIDED 2026-11-20 — owner: "open lit-21"** — the P12 terminal declaration overturned for that course only; both reserved pools (IGCSESUCCESS 9 + Claire's Notes 243) adjudicated onto the freshly opened course by **lane P16** (`docs/P16-LIT21-OPENING-LANE.md`).
3. Residual recon slots stay reserved (7 lost names + Skip the Tutor / Bizcon Sessions / Dr Demina).

## Artifacts

- Inventories: `inventory/channels/<pool>-uploads.json` ×19 (5,591 uploads, enumeratedUtc 2026-11-19T14:37:11Z)
- Pipeline: `scripts/p15/` (sweep → pools → resolve → enumerate → classify → file)
- Evidence: `scripts/p15/sweep.json` (231 channels × query hits), `classify.json`, `filing_stats.json`, `p15_pools.json`
- Gap profile: `scripts/p15/p15_gap_profile.py` + the table above
