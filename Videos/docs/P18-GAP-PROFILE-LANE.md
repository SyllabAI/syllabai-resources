# P18 — GAP-PROFILE LANE (fresh residual sweep over the post-P17 corpus)

**State: FILED 2026-11-20 — filing-only tranche. Judgment + builder emit GATED pending owner pool admission (the P15/P17 convention: no judgment, no emit until the owner admits the pools). Branch: `videos/p18-gap-profile` (resources). No hub-side changes in this tranche.**
**Authorization: owner — "P18 profile" (2026-11-20), the next search round after the P17 gap-profile judgment lane shipped (hub `cb0f9c3f`).**

## Why

The P17 filing profile (3,668 unmapped) predates P17's own 2,574 rowsApproved + the P4-inherit cascade. The fresh profile at hub main `cb0f9c3f` (scripts/p18/p18_gap_profile.py over the 96-course corpus, committed as `gap_profile_p18.json`) computes the CURRENT residual: **10,814 spec points, 7,546 mapped — 3,268 unmapped across 86 courses** (0 courses at zero rows; P17 moved the residual 3,668 → 3,268 — its anchor-heavy pools moved registry counts, but anchors carry zero spec weight, so the CONTENT-class deficits remain).

## The residual of record (top deficits)

igcse-geography-19 **4GE1** 183 left (9%) · ial-chem WCH 169 (47%) · EM-25 **0680** 118 · ict-17 **4IT1** 111 · ial-bio WBI 107 · ial-phys WPH 102 · 4MA1 higher 100 · lit-21 unseen spine 96 · 4MA1 foundation 95 · geo-25 **0460** 94 · econ-25 **0455** 92 · econ-20 87 · accounting-25 **0452** 76 · GP-21 **8021** 70 · physics-23 **0625** 68 · EM-20 **8291** 64 · chem-19 62 · chem-23 **0620** 59 · modular tails 4XM1/4XW1 58+50+49+42 · intl-maths **0607** 49 · maths-B **4MB1** 44 · double-award-17 39+34+32 · further pure **4PM0** 28.

## Sweep

24 gap clusters / **69 code-targeted queries via ytsearch** (p18_sweep.py, register-aware: 4GE1/4IT1/4XM/4XS/4XB/4XC/4MB1/4CH1/0607/0680/8291/8021/0460/0455/0452/9708/WCH-WPH-WBI-content classes) → **299 distinct channels: 124 truly new + 175 known-deduped** (dedupe vs ALL inventoried channels — now including the P17 pools ×21 — PLUS the P15 sweep's 231 and the P17 sweep's 292 harvested channels as sentinels: flagged, re-proposable WITH disclosure, nothing silently dropped). Exam Essentials still excluded-of-record (P2F, 16 hits). Cache-resumable (`sweep.json` 299 channels / 69 queries).

## Register gate

Identity gate **28/28 resolved** (externalId + og:title agree). Enumeration over all 28 candidates: **9,869 uploads** (uploads-playlist method, cap 15,000). Register classification (`classify.json`, 36 families incl. the new 4PM0 further-pure family). The gate: **21 filed (13 T1 judgment-ready + 8 T2 small/thin) + 7 honest drops of record** (`register_gate.json`): corbettmaths (UK GCSE 1MA1, 0 International tokens of 1,656), jspark-academy (0 density of 265), brainstorm-maths-science (NT-dominant), 1st-class-maths (0 4MA1 tokens of 332), english-with-issy (0 density of 631), the-a-level-english-guide (the 8291 sweep hits were noise), zphysics (WPH ×2/716 below the bar). Drops are register-level, not overlap-level — re-sweepable next lane.

**T1 highlights:** my-grade9-maths-tutor **4MA1 ×317/435** (the densest 4MA1-content find of any sweep); chemistry-that-counts **WCH11-16 ×104/135** (the IAL chemistry CONTENT class the P17 walkthrough pools did not carry; p17-swept resurfaced w/ disclosure); economics-by-abdul-hadi **9708 ×295 + 0455 ×109** (p15); watchme-do-math **4PM0 ×66/111**; omar-nassar-accounting **0452 ×59/59 (100%)**; ict-at-tda **4IT1 ×44/64**; fiifi-aubbin **0417 ×19 + 4IT1 ×14** (p17); the-maths-centre **0606 ×141 + 0452 ×36 + 4PM0 ×19**; brian-kemp **0455 + 4BS1 + 0460 + 4MA1** (p15); sense-business-studies **4BS1 ×85**; igcse-a-level-examcrack **4-sciences ×42 + 0625 ×40 + 4MA1 ×35** (p15); really-academics **WCH ×23 + WBI ×22** (p15); a-levels-revision-videos **9708 ×23/62**.

**T2:** jmr-teaching-tech 0680 ×13/26 · sir-usman-econ-business 0455 ×36/73 · indigo-education-group 8021 ×14/370 · tsil-maths 4PM0+4MB1 ×5/23 · tutoring-with-gavin 0475 ×19/74 · no-waffle-gcse 0475 ×31/578 (UK-GCSE-dominant, 0475 subset only, Class W posture) · scinova-education WPH ×15/100 · ial-science-notes-topicals ×2 (micro, disclosed).

## Enumeration + overlap law

Filed inventories ×21 in the P11–P17 shape (additive `provenance` key on the 6 resurfaced pools) → **5,843 uploads, enumeratedUtc 2026-11-20T06:05:00Z** (= 9,869 enumerated − 4,026 in the 7 dropped pools, exactly). **Overlap law ALL PASS: 0 vs the hub shipped union (12,722 ids over 96 courses incl. P17), 0 vs prior lane inventories (53,291 incl. P17's 8,927), 0 intra-P18** (`filing_stats.json`).

## Reserved slots unchanged

7 lost recon pool names + Skip the Tutor / Bizcon Sessions / Dr Demina stay reserved pending owner re-supply. **PAT rotation still outstanding.**

## Next

The owner admits the pools (or says "run it"), then the judgment micro-lane runs under the committed laws (Tier B paper-code anchors per the unit-session/family registers; Tier A spec rows via the P13/P15 ladder + the P16/P17 Class W predicate; oEmbed identity; skips ledger; P4 inherit loop; hub emit + tests).
