# P18 — GAP-PROFILE LANE (fresh residual sweep over the post-P17 corpus)

**State: JUDGMENT SHIPPED 2026-11-20 — owner order "run P18 judgment" (2026-11-20) admits the 21 filed pools (the P15/P17 convention) and opens the judgment gate. Judgment + oEmbed identity sweep + hub emit + gates landed this tranche; resources PR + hub PR open, merge receipts to follow.**
**Authorization: owner — "P18 profile" (2026-11-20) filed the tranche; "run P18 judgment" (2026-11-20) admitted the pools and ordered the judgment.**

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

## Judgment (2026-11-20, scripts/p18/p18_judgment.py)

Exactly-once disposition of all **5,843** accounts, 0 collisions machine-checked: **1,433 Tier B paper-code anchor rows over 1,056 videos** (method paper-code, high, zero spec weight) + **510 Tier A spec rows** (the P13/P15 gate ladder + the P16 Class W predicate; 4 lit-21 Class W rows) + **4,277 honest skips** ledgered by class (`work/p18/skips.json`, committed to `scripts/p18/skips.json`).

**New Tier B registers of record** (on top of the P15/P17 set): **4PM0/4PM1 Edexcel IGCSE Further Pure** (the NEW P18 register → igcse-further-maths-19 — 89 rows, the biggest further-pure find of any sweep); **8021 General Paper** (the NEW P18 register → cie-as-english-general-paper-21); **CIE A-level sciences 9700/9701/9702** papers 1-3 AS / 4-5 A2 (the P13/P14 paper-number routing law); **0580** papers 2/4 extended vs 1/3 core (the P9/P14 law, code-required — bare 'IGCSE Maths' titles skip honestly); **the International-GCSE-ICT register text** (ict-at-tda's 'Edexcel GCSE ICT' topic library — 44 anchors — and fiifi's dual '4IT1 + 0417/0983' lessons, both sides bound, disclosed).

**Honest register calls of record** (the false-density disclosure duty): indigo-education-group's '8021 x14' family read was tuition marketing — **0 binds**; no-waffle-gcse's '0475 x31' family read was UK GCSE lit — **1 genuine bind** ('Ozymandias', a work on BOTH the AQA Power & Conflict cluster and the CIE 0475 Songs of Ourselves list); the unit-summary pools (chemistry-that-counts WCH 'Summary (Unit N)' x104, really-academics 'Last Minute Revision' x45) bind only where tokens are distinctive at the df<=3 bar — the summary remainder ledgered honest-no-bind (the P17 team-elevare precedent); examcrack's 9709 maths walkthroughs skip per ANCHOR-GRANULARITY section 6 (the P9/P17 precedent); watchme-do-math's off-register vlog remainder skipped.

**P18 disclosed regex amendments** (the P17 Class W amendment precedent):
1. RE_GUIDE's bare 'vision' token — a substring match inside 'revision' (re-VISION) present since P14 — is **word-bounded**; the P17 skips ledger carries the same latent effect (disclosed, not re-opened — P17 is shipped).
2. RE_4IT0 gains the 'International GCSE ICT' register text (made explicit alongside the i?-optional form the committed law already accepted).
3. Class W **suffix-collision ledger** (the P16 NOBIND_CHARS precedent): a span tail naming a LONGER off-spine work whose name ends in a short on-spine work name must not suffix-bind the short work ('singh song' → Szirtes' 'Song' rejected; Nagra's 'Singh Song!' is the AQA Love & Relationships poem, not the CIE set text).
4. The O-Level gate generalizes the P14 zainematics law: spine-code tokens (0580/0606/0452/0455/0610/9708/...) take precedence over O-Level branding — the 4024/2281/5090/7707 duals exempt when a spine code is present.

## oEmbed identity sweep (scripts/p18/p18_oembed.py)

**1,566/1,566 routed videos alive, 0 bad**: 1,562 author_url channel == channel-of-record via UC id (0 mismatch) + **4 thumbnail-liveness fallbacks disclosed per the P2D law** — oembed HTTP 200 all-null payload (the restricted-embed form), identity rides on the channel-of-record upload provenance, liveness adjudicated by the thumbnail endpoint: K7A87pAXLaI / dak_yozkgZg / 5YuMWveG29o (igcse-a-level-examcrack), pf7vPcjH_yM (tsil-maths).

## Emit + gates (scripts/p18/p18_assemble.py, build-content-map-external.mjs P18/P18B)

**1,943 owner-reviewed rows onto 41 courses** (28 pre-inherit + 13 P4-children post-inherit via the P18B shape): 1,433 anchors + 510 spec rows. Hub gates: **tests 16/16 (10,884 expects; the four P2F at-rest pins updated for the P18 increment: ial-chem-17 639→654 mappings / 233→236 anchors, ial-phys-19 262→268, ial-bio-18 111→114, igcse-chem-19 86→91)**, census **96 courses / 21,248 rows / 69,233 refs / 0 violations** (`scripts/p18/specjoin-census-p18.json`; +2,242 rows = +1,943 direct + 299 P4-inherit cascade), corpus **12,722 → 14,288 distinct videos** (+1,566, exact), fresh residual **3,268 → 2,932 unmapped of 10,814**, flags videoMap.courses 96 (skip-if-current; the status template gained the P18 sentence and the P17 sentence's thumb-fallback disclosure was restored in the builder template itself — the P18 lane also fixed the builder's stale `statusCurrent` prefix check that had been silently rewriting flags.json on every emit since P15). Reserved slots unchanged; **PAT rotation still outstanding.**

## Next

Merge receipts; the 4GE1 183-point deficit stays open (no P18 pool carries the register — re-sweepable next lane); the drops stay re-sweepable; the owner may order the next search round.
