# Review file — external lane P8 (T-VIDEOMAP-P8, physics-trio honest-empty fill)

Owner anchor (chat 2026-11-13): *"the ~50 specs still honest-empty on the physics trio"* — a re-adjudication micro-lane: the ENTIRE remaining pool inventory (PhysicsOnline 1,081 + the four P7 pools 1,085) is re-surfaced against the physics trio's EMPTY spec points only (cie-a-level-physics-25, cie-igcse-physics-23, igcse-physics-19), because every prior lane (P2E/P6/P7) adjudicated pool videos against all specs — mapped ones included — under per-course routing, so empty-spec targets that lost their routing race were never individually dispositioned. Title-only posture + tightened binding rule carried (P2E/P5/P6/P7 law). Mapped specs are out of scope (multi-source enrichment is not this lane's goal).

## Surfaces and census

| stage | count |
| --- | --- |
| Pool uploads (5 channels) | 2,166 |
| Mapped across the 53-course union (excluded) | 1,030 |
| Unmapped pool remainder | 1,136 |
| Raw candidate pairs vs trio empty specs (distinctive token, df<=3 in-course) | 1,027 pairs / 467 videos |
| Strong surface after pool-rarity gate (token also rare across pool titles) | 369 rows / 240 videos / 127 targets |
| Agent judgment: keeps | **8 rows (M5/L3) onto 6 distinct specs** |
| Agent judgment: full-row drops | 232 videos with reasons (291 per-course reject entries incl. kept-elsewhere junk binds) |
| Pre-pass no-binding rejects (weak-token only) | 227 distinct videos / 316 per-course entries |
| Honest reject-ledger entries (owner-review-verdicts.p8.json x3) | **610** |
| No-candidate videos (never routed; no token overlap at df<=3) | 669 |

Per course:

| course | empty specs before | keeps | rows (M/L) | specs filled | reject ledger |
| --- | --- | --- | --- | --- | --- |
| cie-a-level-physics-25 | 155 | 2 | 2 (2/0) | 1.3.2, 13.2.2 | 245 |
| cie-igcse-physics-23 | 125 | 4 | 4 (3/1) | 3.2.4b (x3 videos), 1.1.7 | 224 |
| igcse-physics-19 | 43 | 2 | 2 (1/1) | 5.8P, 2.22P | 141 |
| **trio total** | **323** | **8** | **8 (5/3)** | **6 distinct** | **610** |

## Judgment pass (self-review, per the 2026-11-09 standing ruling)

Every strong-surface video adjudicated individually (decision table `scripts/p8_judgment.py`, 240 entries). Keep classes:

- **Prior-lane gap rescues (the honest core of this lane)**: the three lens-image videos (`4N6rPk9ucdI` real / `L3jgUZ9l8kY` virtual / `DkPLiQhDwms` diverging) — P6 dropped all three for AL25 on "no lens spec exists in CIE 9702 (removed from A-level)", which never adjudicated the CIE-IGCSE target 3.2.4b, empty on cie-igcse-physics-23 and exactly the image-characteristics spec the videos teach; `2kHCvtTjOJs` Resolving Vectors — P6 rejected only the AL25 4.2.3 equilibrium-triangle candidate as generic, the right-angle resultant spec 1.1.7 (empty on IG23) is the same skill in reverse; `9HyKNkXW9W0` Conductors/Insulators — P6 rejected the AL25 I-V candidate as generic, the Edexcel 2.22P conductors/insulators spec is the video's subject;
- **Never-routed genuine matches**: `Y0xvoeiRTA0` Accuracy/Precision/Errors/Uncertainty -> AL25 1.3.2 (empty); `4KTIxheE3bY` Big G and little g -> AL25 13.2.2 (empty, the G-bearing Newton's-law spec; 13.3.1 already mapped); `QMIcDNx36IQ` Changes of State shorts -> IG19 5.8P (empty; conceptual half, 5.11P practical NOT bound).

Drop classes (per-video reasons in the ledgers): **promo/announcement** (channel news, exam advice, celebrations), **drill** (worked examples, Daily Workout, maths-for-A-level series, natural logs, sphere maths), **technique** (MC strategy, practical-skills, formulae sheets), **adjacent** (word-adjacent nonsense: conductance 'anti' -> antiparticles, laser diode -> rectifier diode, Wheatstone bridge -> bridge rectifier, Feynman diagram -> HR diagram, cloud chamber -> planets, gamma absorption -> absorption spectra), **cross-subject** (all 33 Amoeba + FSL bio/chem revision videos), **sewage** (all 10 malmesbury non-science rows: maths/Spanish/French/English-Lit), **content-mismatch** (DNA mutations != radiation mutations), **no-target** (LIGO, Jeans mass). Prior P6/P7 rulings honored everywhere they cover the same (video, course, spec) pair; the rescues above are exactly the pairs the prior rulings did NOT cover.

Identity: 8/8 verified via oEmbed at adjudication time, author string **'Physics Online'** (the P6 expected-author law), titles match the pool inventory exactly. Confidence never high. All 8 rows carry `boardMismatch: true` (AQA/OCR/Edexcel-focused channel bound onto CIE/Edexcel specs on content match).

## Honest no-target census (what stays empty and why)

The trio still carries **317 empty spec points** after this lane (155-1 / 125-2 / 43-2 = 154 / 123 / 41 → 318 minus… exact: 323 - 6 = **317**):

- **137 bare**: no pool video title shares even one distinctive token — mostly Edexcel PAG practicals (IG19 5.11P-style apparatus specs), IG23 cosmology numerics, AL25 thermal-scale subtleties;
- **180 candidate-bearing but honestly rejected**: token overlaps are the classes above (junk-token sewage leaks: 'angles', 'their', 'present', 'remains', 'exposure'; physics-generic vocabulary: energy/force/field/current; drill/technique/promo titles);
- the user-quoted "~50" corresponds most closely to a per-course read of the P7-era remaining gap (IG19 alone was 43 after P7); the full trio honest-empty set is the 323 -> 317 above, every member now individually dispositioned by the 610-entry ledger.

Pool remainder after the lane: 1,136 - 8 = **1,128 videos stay unmapped, every one now ledgered or no-candidate** — the science pool inventory is exhausted under the tightened rule; future fills need new sources, not re-sweeps.
