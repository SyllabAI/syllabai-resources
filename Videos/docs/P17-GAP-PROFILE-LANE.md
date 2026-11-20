# P17 — GAP-PROFILE LANE (fresh residual sweep over the post-P15/P16 corpus)

**State: SHIPPED 2026-11-20 — filing (resources PR #360 commit `9982b750`) + judgment/builder emit (commit `4887c4f5`) → hub PR #1142 (`t-videomap-p17/run-001`); both merged by owner 'review + merge' 2026-11-20 (resources `3a889a0e`, hub `cb0f9c3f`) with the independent review receipts in the merge commits. Judgment: 2,574 owner-reviewed rows onto 36 courses; exactly-once 8,927, 0 collisions; census 96 courses / 19,006 rows / 63,447 refs / 0 violations; tests 16/16 (9,413 expects). One review finding of record — see 'Post-merge review finding' at the end.**
**Authorization: owner, this session — "P17 profile" (2026-11-20), opening the next search round after P15 and the P16 lit-21 opening.**

## Why

The P15 receipt's gap numbers (4,711 unmapped) predate P15's own 1,899 rowsApproved and P16's 100. The fresh profile at hub main `466f23e3` (scripts/p17/p17_gap_profile.py over the 96-course corpus, committed as `gap_profile_p17.json`) computes the CURRENT residual: **10,814 spec points, 7,146 mapped — 3,668 unmapped across 86 courses** (0 courses at zero rows; the gap is still whole-register breadth).

## Gap profile of record (computed 2026-11-20)

Top unmapped spec-point deficits at main:

| course | register | mapped/total |
| --- | --- | --- |
| igcse-geography-19 | Edexcel **4GE1** (Geography A) | 12/202 (190 left, 6%) |
| ial-chemistry-17 | Edexcel IAL WCH | 150/319 (169 left, 47%) |
| cie-igcse-biology-23 | CIE 0610 | 244/388 (144 left, 63%) |
| cie-igcse-environmental-management-25 | CIE 0680 | 24/142 (118 left, 17%) |
| ial-physics-19 | Edexcel IAL WPH | 54/171 (117 left, 32%) |
| igcse-ict-17 | Edexcel **4IT1** | 22/138 (116 left, 16%) |
| ial-biology-18 | Edexcel IAL WBI | 61/170 (109 left, 36%) |
| igcse-maths-a-18 higher / foundation | Edexcel 4MA1 | 85/188 + 65/162 (200 left) |
| igcse-maths-a-modular-24 units x4 | Edexcel **4XM** | ~205 left combined |
| cie-igcse-english-literature-21 | CIE 0475 | 101/203 (102 left — the unseen/skills spine beyond the P16 set-text binds) |
| cie-igcse-economics-20 + -25 | CIE 0455 | 31/129 + 21/113 (190 left) |
| cie-igcse-geography-25 / -20 | CIE 0460 | 19/113 + 74/113 (133 left) |
| cie-igcse-science-co-ordinated-23 trio | CIE 0654 | 150/230 + 142/221 + 141/181 (199 left) |
| cie-igcse-accounting-25 | CIE 0452 | 101/177 (76 left) |
| cie-a-level-economics-23 | CIE 9708 | 180/253 (73 left) |
| cie-as-english-general-paper-21 | CIE 8021 | 3/73 (70 left, 4%) |
| cie-as-environmental-management-20 | CIE 8291 | 62/126 (64 left, 49%) |
| igcse-chemistry-19 | Edexcel **4CH1** | 120/182 (62 left, 66%) |
| igcse-maths-b-16 | Edexcel **4MB1** | 44/98 (54 left, 45%) |
| cie-igcse-maths-international-maths-23-extended / further-maths-additional-25 | CIE 0607 / 0606 | 53 + 53 left |

## Register corrections of record (codes verified against the spine curricula at main)

The P15 sweep carried three wrong register codes, and this lane corrects the record — the likely cause of P15's weak geography/ICT deltas:

1. **igcse-geography-19 is Edexcel IGCSE Geography A = 4GE1** — the P15 doc and queries said 4GE0 (Geography B). `curriculum.json` at main carries 4GE1.
2. **igcse-ict-17 is 4IT1** — P15 swept 4IT0.
3. **Modular families**: maths 4XM, science double-award modular 4WS/4XS, biology modular 4WB/4XB, chemistry modular 4WC/4XC; Maths B 4MB1; Chemistry 4CH1 (not 4CH0); international maths 0607.

## Sweep (scripts/p17/p17_sweep.py, evidence `sweep.json`)

- **24 gap clusters / 75 register+code-targeted queries** via ytsearch (the P15 query law), cache-resumable to work/p17/sweep.json.
- **292 distinct channels harvested: 146 truly new**, 39 inventoried/legacy-known (deduped), **107 flagged `p15-swept-uninventoried`** — harvested by the P15 sweep but never shortlisted there; flagged, not hidden, and re-proposable WITH disclosure under the corrected-code clusters (nothing silently dropped).
- **Dedupe hardening of record**: 5 legacy inventories (Amoeba Sisters / Cognito / Doodle Science / Freesciencelessons / Malmesbury Education) carry no channelId — the known-set now also matches by normalized channel title; Cognito was silently "new" under UC-only dedupe until this fix. Exam Essentials surfaces at 36 hits and stays **excluded-of-record** (P2F pool of record — the P15 exclusion).

## Register gate (classify.json)

- 2 **DROPS**: henry-brand (sweep hits were search-position noise — 0 geography-code tokens in 232 uploads, GCSE-advice register) and science-shorts (AQA A-level physics register, NT). Both stay in the committed sweep evidence as swept-not-shortlisted.
- 1 **PROMOTION**: gcse-ready — full families 0475 x129 / 4MA1 x64 / 0625 x41 / 0620 x33 / 0610 x29 / 0460 x19 plus genuine "International GCSE Geography A" (4GE1) content (71 geo-token titles).
- 1 **FAMILY ADDED**: `IAL unit-session (Pearson)` — the `A level | Biology | Unit 5 | June 2025 | Pearson Edexcel` title format (the P11 Assil unit-paper anchor class) that the WBI/WCH/WPH token regexes miss; chem-bio-math-revision-hub carries 237 such titles.

## Pools of record (21 — p17_pools.json)

| pool | UC | uploads | register evidence (classify.json) | gaps targeted | provenance |
| --- | --- | --- | --- | --- | --- |
| chem-bio-math-revision-hub | UC1Yi4o8pQZ12h86TQV_0ohA | 376 | IAL unit-session x237, WCH x12 | ial-bio-18, ial-chem-17, 4CH1 | new |
| wilson-chong | UCUwxW512TZyCzWgpGDrxf0w | 415 | 4XM modular maths x279 | modular units ~205 | new |
| daniyal-aslam | UCx8Uv9obmqXwJ2LYF08p-Ww | 522 | 9708 x374, 0455 x126 | econ-AL 73, econ-IGCSE 190 | new |
| edexcel-science-channel | UC3fRQyqqRLtznVRnqeZ-Pwg | 266 | WPH x128, Ed-sciences x47, WCH x35 | ial-phys, ial-chem, 4CH1 | p15-swept |
| gcse-ready | UCTu2EgdQHkeVU5r0Elv5x5g | 633 | 0475 x129, 4MA1 x64, 0625 x41, 0620 x33, 0610 x29, 0460 x19, 4GE1 content | geography-19 (190), lit, maths, trio | new |
| adebayo-business-abt | UCtwKSiCvEu2k_jkmuDn3ouA | 3,260 | 4BS1 x39, 0455 x30, 9708 x19 | business-19, econ | new |
| business-teacher-t | UCalKFSMBi-782SP9EozzR3A | 493 | 9609 x152, 4BS1 x20 | business-19/-23/-25, AL business | new |
| aravinth-physics-maths | UCCa6DOv6u5SA1mG2-1IJ2jA | 163 | WPH x78 | ial-phys 117 | new |
| a2z-physics | UCNT2iVV-Uc1W0e7H8qT0KfQ | 381 | WPH x50, 0625 x12 | ial-phys, 0625 | p15-swept |
| nevdoes-econ | UCePqxoXsRrYYgATSfoRYy_g | 186 | 9708 x147 | econ-AL 73 | p15-swept |
| biology-zhan-xuan | UC8J8N1zdAYAsI_dtJXiflVQ | 116 | 0610 x110 | bio-23 144 | p15-swept |
| mrimmoaee-ahmed | UC5AbF_N8ix53fyCCq6LjBnA | 109 | 4IT1 x25, 0417 x23 | ict-17 116 | p15-swept |
| state-of-math | UCRFIBwcMQS_jlFwv4ng7LSA | 449 | 4MA1 x64 | maths-a-18 200 | p15-swept |
| first-rate-tutors | UCtc9J1mVP5OuMEbGF8djo3g | 815 | 0475 x63 | lit-21 unseen spine | new |
| fundoo-tutor | UCmjfgk_-bT3EnzH7cnY1DJA | 162 | 0610 x41, 0455 x26, 0625 x23, 0620 x19 | bio/econ/phys/chem IGCSE | p15-swept |
| team-elevare | UCIo5KFHEgrWq8Q7bf8YtU4Q | 181 | Ed-sciences x27, 0620 x18, 4MA1 x12, 4MB1 x7, WCH x7 | mixed | p15-swept |
| mathman-oa-levels | UClyfhbpXhNHrJraMBqbzNQQ | 246 | 0606 x65 | further-maths-additional 53 | new |
| pinnacle-education | UC-gjRy0RJ8lZM8d2gKPFSvw | 27 | 4MB1 x10 | maths-b-16 54 | new |
| dr-sarah-biology | UCTx7c2jzHD5FGufHXl_kVMw | 26 | WBI x15 | ial-bio-18 109 | new |
| click-ict | UCa-sO0Yfyu2H6njN8UCkHsg | 17 | 4IT1 x5, 0417 x4 | ict-17 116 | new |
| mr-quakers-teaches | UC5pXYQanj4ARLeAm7Rt8iZQ | 84 | 0475 x2 (small) | lit-21 102 | new |

Tiering at judgment time (owner to confirm): T1 judgment-ready = the register-pure and register-dense pools (wilson-chong, daniyal-aslam, chem-bio-math-revision-hub, biology-zhan-xuan, nevdoes-econ, aravinth, a2z-physics, edexcel-science-channel, mrimmoaee, gcse-ready, adebayo/business-teacher-t business slices, mathman, state-of-math, first-rate, fundoo, team-elevare); T2 small = pinnacle, dr-sarah, click-ict, mr-quakers.

## Identity gate + enumeration

- **Resolve 23/23** (externalId + og:title agree on every candidate incl. the 2 later dropped) — `resolve.json` in the work record.
- **8,927 uploads enumerated** over the UU uploads playlists (P14/P15 methodology, cap 15,000), `enumeratedUtc 2026-11-20T04:23:36Z`, inventories x21 in the P11–P15 shape (+ one additive `provenance` key per pool, disclosed). The largest enumeration (adebayo 3,260) was **re-run to completion and byte-verified — identical id sequence** (the P14 transient-early-stop check).

## Overlap law — ALL PASS

- 0 overlap vs the **hub shipped union at main (10,248 ids over 96 courses incl. P15+P16)**
- 0 overlap vs **all prior lane inventories (44,364 ids)**
- **0 intra-P17** (8,927 uploads, all distinct)

## Filing-only status

No judgment, no oEmbed sweep, no builder emit in this tranche. The owner admits pools (or says "run it"), then the judgment micro-lane runs under the committed laws (Tier B paper-code anchors per unit-session format; Tier A spec rows; oEmbed identity; skips ledger; P4 inherit loop; hub emit + tests).

**Reserved slots unchanged**: 7 lost recon pool names + Skip the Tutor / Bizcon Sessions / Dr Demina stay reserved pending owner re-supply. **PAT rotation still outstanding.**

## Post-merge review finding (2026-11-20, owner order "P17 disclosure fix")

The independent review of PRs #360/#1142 (owner "review + merge" 2026-11-20) reproduced every gate from the raw artifacts — exactly-once re-derived from the inventories (8,927 distinct; 0 overlap vs the prior union 44,364, the hub union 10,248, intra-P17 0); oEmbed full sweep author==channel-of-record 0 mismatch; drafts sum == 2,574 rows; hub tests 16/16 at 9,413 expects; the committed census re-run 96 courses / 19,006 rows / 63,447 refs / 0 violations — and caught ONE claim-vs-artifact mismatch of record:

- **The shipped claim text said "0 thumb fallbacks" (flags.videoMap.status + PR bodies + commit messages — the latter immutable) while the committed honest artifact `scripts/p17/oembed-p17.json` records 3 of the 2,474 routed videos with method `thumb-fallback` (oembed HTTPError): `SV-3cSIc-go` (business-teacher-t → cie-igcse-business-23), `ozy72GpnBVA` (aravinth-physics-maths → ial-physics-19), `uk86cQ8K-Ys` (mr-quakers-teaches → cie-igcse-english-literature-21). Identity for these rests on the channel-of-record upload provenance + thumbnail liveness per the P2D law — the P14 precedent (1 thumbnail-liveness fallback disclosed) applied. The 3 rows ship unchanged; the artifact is honest; the claim text was the bug. Corrected hub-side by the disclosure-fix PR (`t-videomap-p17-disclosure/run-001`).**
- `scripts/p17/p17_summary.json`'s oembed block (`verified: 2,614, bad: 0`) is the stale run-1 snapshot taken before the 30 further-maths wrong-register re-adjudications shrank the routed set to 2,474; the FINAL oEmbed evidence of record is `oembed-p17.json` (2,474 entries = 2,471 oembed + 3 thumb-fallback, 0 bad). The summary file is left untouched as the historical run-1 record; this note is the correction of record.
