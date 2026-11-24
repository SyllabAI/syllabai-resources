# P19 — GAP-PROFILE LANE (fresh residual sweep over the post-P18 corpus)

**State: PROFILE FILED 2026-11-25 — owner order "run the P19 profile lane" (2026-11-25) filed the tranche (the P18 convention: sweep + register gate + filing; the judgment gate stays closed until the owner admits the pools per the P15/P17/P18 convention). Resources PR open, merge receipts to follow.**
**Authorization: owner — "run the P19 profile lane" (2026-11-25).**

## Why

The P18 filing profile (3,268 unmapped) predates P18's own 1,943 rowsApproved + the P4-inherit cascade. The fresh profile at hub main `1c83ba48` (scripts/p19/p19_gap_profile.py over the 96-course corpus, committed as `gap_profile_p19.json`) computes the CURRENT residual: **10,814 spec points, 7,882 mapped — 2,932 unmapped across 86 courses** (0 courses at zero rows; P18 moved the residual 3,268 → 2,932 — its anchor-heavy pools moved registry counts, but anchors carry zero spec weight, so the CONTENT-class deficits remain).

## The residual of record (top deficits)

igcse-geography-19 **4GE1** 183 left (9%) · ial-chem WCH 164 (49%) · ict-17 **4IT1** 109 · ial-bio WBI 107 · ial-phys WPH 102 · 4MA1 higher 100 · lit-21 unseen spine 96 · 4MA1 foundation 95 · EM-25 **0680** 91 · econ-25 **0455** 75 · accounting-25 **0452** 74 · GP-21 **8021** 70 · 8291 64 · co-ordinated-23 physics 64 · chem-19 62 · modular 4XM1/4XW1/4XS1/4XB1/4XC1 58+50+49+42+35+32+29 · physics-23 **0625** 54 · econ-20 52 · geo-25 **0460** 48 · a-level-business **9609** 44 · maths-B **4MB1** 44 · intl-maths **0607** 43 · double-award-17 **4SD0** 38+34+32 · ict-21 **0417** 30 · business-25 **0450** 27 · 0610 tails 24.

## Sweep

28 gap clusters / **84 NEW-angle queries via ytsearch** (p19_sweep.py, register-aware: 4GE1/4IT1/0417/WCH-WPH-WBI/4MA1-H+F/0475-unseen/0680/0455/0452/8021/8291/0654/0620/4XM/4XS+4XB+4XC/0625/0460/9609/4MB1/0607/4SD0/0610 — **every query string new vs the P15/P17/P18 caches**, so the deduped channels are sentinel resurfacing, not re-harvest) → **389 distinct channels: 173 truly new + 216 known-deduped** (dedupe vs ALL inventoried channels — now including the P17 pools ×21 + the P18 pools ×21 — PLUS the committed sweep sentinels P15 231 / P17 292 / P18 299: flagged, re-proposable WITH disclosure, nothing silently dropped). Exam Essentials still excluded-of-record (8 hits). Cache-resumable (`sweep.json` 389 channels / 84 queries).

## Identity gate + enumeration

Identity gate **43/43 resolved** (externalId + og:title agree). Enumeration over all 43 candidates: **16,672 uploads** (uploads-playlist method, cap 15,000).

## Register gate

The gate: **25 filed (17 T1 judgment-ready + 8 T2 small/thin) + 18 honest drops of record** (`register_gate.json`): the-organic-chemistry-tutor (0 International families of 2,916 — the wide-audience US register), peekaboo-kidz (kids' science, 0 density of 1,133), justin-sung (study-skills, 0 density of 897), ammar-samana (code-less session tokens of 794 — cannot bind at judgment, the P18 0580 law), ict-computer-tution-class (0417+4IT1 ×2 of 628 — the name promises Edexcel, the titles do not carry it: register-suspect confirmed), the-gcse-maths-tutor (UK GCSE 1MA1 register of 518), jensenmath (Canadian curriculum of 501), science-shorts (NT ×122 dominant — re-drop consistent with the P17 AQA-register gate), 1st-class-maths (0 International tokens of 333 — re-drop consistent with the P18 gate), mathematics-gurukul-goln (0 International density of 321), internet-geography (0 0460/4GE1 tokens of 285 — UK geography register despite the name), grade-solution (0 density of 247), henry-brand (0 International families of 232 — re-drop consistent with the P17 gate), the-a-level-english-guide (0 8291 tokens of 134 — re-drop consistent with the P18 gate), geographer-online (0 0460/4GE1 tokens of 88), raiexclusive (0 density of 79), caitlin-jessica (0 families of 39 — the lit-21 unseen hits were noise), the-geography-guy (0 families of 14). Drops are register-level, not overlap-level — re-sweepable next lane.

**T1 highlights:** igbiocomplete **0610 ×272 + 0620 ×194 + 0625 ×48/514** (the densest CIE sciences-trio CONTENT find of any sweep); ginger-mathematician **4MA1 ×159 + 0607 ×52/665** (p15-swept resurfaced w/ disclosure); rapid-revision-with-shayan **0452 ×127 + 0455 ×31/275** (the accounting CONTENT class); the-visible-hand **9708 ×78 + 0455 ×59/156** (the econ theory class); edubbey **0417 ×81 + 0625 ×45 + 0455 ×37/636**; muzammil-ameer-acma **9609 ×59 + 0452 ×10 + 0450 ×9/140**; saifullah-ajaz **9609 ×33 + 0450 ×28/149**; your-igcse-tutors **0455 ×34 + 0606 ×14/64**; igcse-study-buddy **0620 ×43 + 0610 ×35 + 0625 ×11/92 (97% International)**; miss-tech-teacher **0417 ×73/73 (100%)**; mr-khan-ict-solutions **0417 ×72/74**; ict-with-tatchen **0417 ×48/55 + 4IT1 ×1** (dual ICT register); maths-with-mohaiminul **4MB1 ×46/58 (79%)**; sciencewithchun **0654 ×14/16 (88%)**; the-physics-examiner **WPH ×10/11 (91%)**; education-for-success **0680 ×64/1783** (the 0680 CONTENT class the P18 jmr pool did not carry at density); bookkeepers-journal **0452 ×49/68 (72%)**.

**T2:** precool-skillz 0417 ×31 + 0625 ×26 + 0620 ×25 + 0455 ×11/195 (dual ICT + sciences + econ) · save-my-exams 4MA1 ×57 + 0625 ×29 + 0620 ×26 + 0610 ×20 + 0475 ×15/786 (mixed-board, NT ×122 dominant — disclosed) · accounting-celebrity 0452 ×44/635 (44 absolute, 7% ratio disclosed) · revwise Ed-IGCSE ×15 + 0620 ×9 + 0610 ×8/134 (mixed NT — disclosed) · benzakademi 8291 ×13/44 · academic-plus 4BS1 ×10 + 9609 ×1/467 (thin-multi, the indigo T2 precedent) · easy-edu 4MB1 ×4/5 (micro, the P17 mr-quakers precedent) · the-revision-notebook 9609 ×3/3 (micro).

## Enumeration + overlap law

Filed inventories ×25 in the P11–P18 shape (additive `provenance` key on the 8 resurfaced pools: ginger-mathematician / igbiocomplete / igcse-study-buddy / revwise / your-igcse-tutors / edubbey / rapid-revision-with-shayan / sciencewithchun; the 4 re-proposed prior drops all re-dropped and documented in the gate — their pool provenance carries the priorDrop disclosure) → **7,098 uploads, enumeratedUtc 2026-11-25T05:30:00Z** (= 16,672 enumerated − 9,574 in the 18 dropped pools, exactly). **Overlap law ALL PASS: 0 vs the hub shipped union (14,288 ids over 96 courses incl. P18 @ `1c83ba48`), 0 vs prior lane inventories (59,134 incl. P18's 5,843), 0 intra-P19** (`filing_stats.json`).

## The 4GE1 183-point deficit (carried from P18)

The P19 sweep ran a dedicated 4GE1 cluster pair (6 queries: paper-2/fieldwork/physical-world/coasts/urban/grade-9 angles) and harvested only sub-threshold geography channels — the-geography-guy (×2, 0 families), geographypods + Five Minute Geography (×1 each, below the shortlist bar). **The register gate filed NO 4GE1 pool; the 183-point deficit stays open, re-sweepable next lane.**

## Reserved slots unchanged

7 lost recon pool names + Skip the Tutor / Bizcon Sessions / Dr Demina stay reserved pending owner re-supply. Cognito (×41 on the new queries) is documented excluded-of-record — legacy pool of record (P4/P5 shipped, inventoried by title), NOT re-proposed.

## Next

Merge receipts; the owner may order "run P19 judgment" (admits the 25 pools, opens the judgment gate — the P15/P17/P18 convention). **PAT rotation still outstanding.**
