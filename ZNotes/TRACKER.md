# ZNotes Corpus — Master Tracker

_Updated **2026-11-01** · repo `main @ 4b75272d` · registry `syllabai-v2/apps/hub/content/courses.json` (106 rows) · task **T-ZNOTES-3**_

Single source of truth for the revision-notes corpus in this folder: what is downloaded, from where, what is verified unavailable, and what image failures remain. Companion data: `ZNotes/manifest.json` (totals), per-course `manifest.json` (counts + failures ledger), `scripts/T-ZNOTES-2-resync-report.json` (per-URL resync record), `scripts/zn_resync_images.py` / `zn_resync_integrate.py` (resync tooling), `scripts/zn_fetch.py` (original downloader).

---

## 1. At a glance

| Metric | Value |
|---|---:|
| Corpus courses (one dir per course) | 97 |
| Cards (leaf notes) | 8,322 |
| Images downloaded | 3,718 |
| Assets on disk | ~133 MB |
| Documented image failures remaining | 48 (all 48 unrecoverable-at-source, see §5) |
| Official subject lanes universe (scan basis) | 31 importable + 103 blocked + 106 registered |
| Lanes with notes in corpus but **not** yet in registry | 31 |
| Lanes verified **no web-ready notes** (2026-11-01 re-check) | 97 |

Corpus mix: caie / A2 Level: 14 · caie / AS Level: 18 · caie / Checkpoint: 4 · caie / IGCSE: 39 · caie / O Level: 4 · edexcel / GCSE: 3 · edexcel / IAL: 7 · edexcel / IGCSE: 8

## 2. Sources directory (status as of 2026-11-01)

| Source | Notes coverage | Status / evidence |
|---|---|---|
| ZNotes | CAIE + Edexcel international — 97 courses | **Downloaded** (T-ZNOTES-1, PR #259; resync #262). Community-authored; license check per ADR-039 recorded in README |
| SaveMyExams | IGCSE/A-Level/IAL — mainstream subjects | **Live re-crawl 2026-11-01**: notes-subject sets unchanged vs 2026-10-31 baseline; zero notes for any blocked lane below (papers only) |
| Maths Genie | Maths family only | Verified 2026-10-31: 0 'Revision Notes' outside maths; no blocked lane is maths |
| Cognito | UK GCSE/A-Level boards | Verified 2026-10-31: no CIE/Edexcel-International alignment for any blocked lane |
| GCE Guide | was CIE notes hub | **DEAD** — domain now redirects to an unrelated gambling site (verified 2026-11-01) |
| Physics & Maths Tutor | UK boards + CIE sciences/maths | Cloudflare-gated to bots; public coverage overlaps lanes already covered; no evidence of notes for any blocked lane |
| PapersDaddy / thinka.ai | claim broad CIE notes | **Excluded** — bot-gated / AI-generated commercial content; provenance unverifiable → fails ADR-039 disclosure bar |
| TeachifyMe | CIE mainstream subjects | Notes only for already-covered lanes (chem/econ/maths/physics/islamiyat/pakistan-studies) |
| Cambridge Resource Plus | official teacher resources | Login-gated, not web-ready |

## 3. Corpus inventory (97 courses — ground truth from per-course manifests)

| Course dir | Board | Level | Subject | Code | Cards | Images | Img-fail | MB |
|---|---|---|---|---|---:|---:|---:|---:|
| `caie-a2-level-accounting-9706` | caie | A2 Level | Accounting | 9706 | 43 | 6 | 0 | 0.1 |
| `caie-a2-level-biology-9700` | caie | A2 Level | Biology | 9700 | 115 | 67 | 0 | 2.9 |
| `caie-a2-level-business-9609` | caie | A2 Level | Business | 9609 | 79 | 30 | 0 | 1.0 |
| `caie-a2-level-chemistry-9701` | caie | A2 Level | Chemistry | 9701 | 166 | 142 | 14 | 5.1 |
| `caie-a2-level-computer-science-9618` | caie | A2 Level | Computer Science | 9618 | 31 | 24 | 0 | 0.3 |
| `caie-a2-level-economics-9708` | caie | A2 Level | Economics | 9708 | 55 | 60 | 0 | 0.9 |
| `caie-a2-level-english-language-9093` | caie | A2 Level | English Language | 9093 | 0 | 0 | 0 | 0.0 |
| `caie-a2-level-further-mathematics-9231` | caie | A2 Level | Further Mathematics | 9231 | 83 | 117 | 0 | 0.9 |
| `caie-a2-level-geography-9696` | caie | A2 Level | Geography | 9696 | 19 | 53 | 0 | 8.7 |
| `caie-a2-level-it-9626` | caie | A2 Level | IT | 9626 | 39 | 12 | 0 | 0.0 |
| `caie-a2-level-law-9084` | caie | A2 Level | Law | 9084 | 36 | 0 | 0 | 0.0 |
| `caie-a2-level-mathematics-9709` | caie | A2 Level | Mathematics | 9709 | 63 | 26 | 0 | 0.9 |
| `caie-a2-level-physics-9702` | caie | A2 Level | Physics | 9702 | 132 | 54 | 0 | 1.7 |
| `caie-a2-level-psychology-9990` | caie | A2 Level | Psychology | 9990 | 51 | 26 | 2 | 5.3 |
| `caie-as-level-accounting-9706` | caie | AS Level | Accounting | 9706 | 29 | 8 | 0 | 0.1 |
| `caie-as-level-biology-9700` | caie | AS Level | Biology | 9700 | 119 | 48 | 1 | 4.7 |
| `caie-as-level-business-9609` | caie | AS Level | Business | 9609 | 251 | 18 | 0 | 1.2 |
| `caie-as-level-chemistry-9701` | caie | AS Level | Chemistry | 9701 | 197 | 176 | 3 | 3.9 |
| `caie-as-level-computer-science-9618` | caie | AS Level | Computer Science | 9618 | 51 | 23 | 0 | 0.4 |
| `caie-as-level-design-and-technology-9705` | caie | AS Level | Design and Technology | 9705 | 57 | 14 | 0 | 0.3 |
| `caie-as-level-economics-9708` | caie | AS Level | Economics | 9708 | 47 | 14 | 0 | 0.4 |
| `caie-as-level-english-general-paper-8021` | caie | AS Level | English General Paper | 8021 | 38 | 10 | 0 | 0.5 |
| `caie-as-level-english-language-9093` | caie | AS Level | English Language | 9093 | 41 | 0 | 0 | 0.0 |
| `caie-as-level-further-mathematics-9231` | caie | AS Level | Further Mathematics | 9231 | 49 | 38 | 0 | 0.5 |
| `caie-as-level-geography-9696` | caie | AS Level | Geography | 9696 | 88 | 46 | 0 | 9.0 |
| `caie-as-level-history-9489` | caie | AS Level | History | 9489 | 321 | 0 | 0 | 0.0 |
| `caie-as-level-it-9626` | caie | AS Level | IT | 9626 | 80 | 89 | 1 | 1.0 |
| `caie-as-level-law-9084` | caie | AS Level | Law | 9084 | 31 | 0 | 0 | 0.0 |
| `caie-as-level-marine-science-9693` | caie | AS Level | Marine Science | 9693 | 35 | 12 | 2 | 1.8 |
| `caie-as-level-mathematics-9709` | caie | AS Level | Mathematics | 9709 | 138 | 133 | 0 | 1.5 |
| `caie-as-level-physics-9702` | caie | AS Level | Physics | 9702 | 49 | 19 | 2 | 0.5 |
| `caie-as-level-psychology-9990` | caie | AS Level | Psychology | 9990 | 61 | 3 | 0 | 0.1 |
| `caie-checkpoint-english` | caie | Checkpoint | English | — | 19 | 0 | 0 | 0.0 |
| `caie-checkpoint-english-as-second-language-undefined` | caie | Checkpoint | English as Second Language | — | 30 | 0 | 0 | 0.0 |
| `caie-checkpoint-mathematics` | caie | Checkpoint | Mathematics | — | 66 | 50 | 2 | 0.8 |
| `caie-checkpoint-science` | caie | Checkpoint | Science | — | 193 | 90 | 1 | 2.2 |
| `caie-igcse-accounting-0452` | caie | IGCSE | Accounting | 0452 | 37 | 8 | 0 | 0.1 |
| `caie-igcse-additional-mathematics-0606` | caie | IGCSE | Additional Mathematics | 0606 | 65 | 27 | 1 | 0.3 |
| `caie-igcse-arabic-as-a-foreign-language-0544` | caie | IGCSE | Arabic as a Foreign Language | 0544 | 132 | 11 | 0 | 0.3 |
| `caie-igcse-biology-0610` | caie | IGCSE | Biology | 0610 | 209 | 140 | 0 | 7.6 |
| `caie-igcse-business-0264` | caie | IGCSE | Business | 0264 | 34 | 12 | 0 | 0.1 |
| `caie-igcse-business-studies-0450` | caie | IGCSE | Business Studies | 0450 | 99 | 18 | 0 | 0.1 |
| `caie-igcse-chemistry-0620` | caie | IGCSE | Chemistry | 0620 | 218 | 148 | 1 | 2.8 |
| `caie-igcse-co-ordinated-sciences-0654` | caie | IGCSE | Co-ordinated Sciences | 0654 | 56 | 11 | 0 | 0.3 |
| `caie-igcse-combined-science-0653` | caie | IGCSE | Combined Science | 0653 | 37 | 22 | 0 | 1.2 |
| `caie-igcse-computer-science-0478` | caie | IGCSE | Computer Science | 0478 | 52 | 38 | 1 | 0.3 |
| `caie-igcse-design-and-technology-0445` | caie | IGCSE | Design and Technology | 0445 | 66 | 165 | 0 | 4.1 |
| `caie-igcse-economics-0455` | caie | IGCSE | Economics | 0455 | 153 | 19 | 0 | 0.1 |
| `caie-igcse-english-as-a-second-language-0510` | caie | IGCSE | English as a Second Language | 0510 | 79 | 30 | 0 | 0.5 |
| `caie-igcse-enterprise-0454` | caie | IGCSE | Enterprise  | 0454 | 48 | 6 | 0 | 0.1 |
| `caie-igcse-environmental-management-0680` | caie | IGCSE | Environmental Management | 0680 | 57 | 85 | 0 | 16.1 |
| `caie-igcse-first-language-english-0500` | caie | IGCSE | First Language English | 0500 | 51 | 0 | 0 | 0.0 |
| `caie-igcse-first-language-malay-0696` | caie | IGCSE | First Language Malay | 0696 | 26 | 5 | 0 | 0.1 |
| `caie-igcse-first-language-vietnamese-0695` | caie | IGCSE | First Language Vietnamese | 0695 | 20 | 0 | 0 | 0.0 |
| `caie-igcse-food-and-nutrition-0648` | caie | IGCSE | Food and Nutrition | 0648 | 72 | 0 | 0 | 0.0 |
| `caie-igcse-french-foreign-language-0520` | caie | IGCSE | French - Foreign Language | 0520 | 197 | 2 | 0 | 0.0 |
| `caie-igcse-geography-0460` | caie | IGCSE | Geography | 0460 | 71 | 92 | 0 | 4.7 |
| `caie-igcse-german-foreign-language-0525` | caie | IGCSE | German - Foreign Language | 0525 | 186 | 13 | 1 | 0.3 |
| `caie-igcse-global-perspectives-0457` | caie | IGCSE | Global Perspectives | 0457 | 19 | 0 | 0 | 0.0 |
| `caie-igcse-hindi-as-a-second-language-0549` | caie | IGCSE | Hindi as a Second Language | 0549 | 25 | 14 | 0 | 0.6 |
| `caie-igcse-history-0470` | caie | IGCSE | History | 0470 | 129 | 11 | 0 | 2.4 |
| `caie-igcse-ict-0417` | caie | IGCSE | ICT | 0417 | 129 | 78 | 2 | 0.6 |
| `caie-igcse-international-mathematics-0607` | caie | IGCSE | International Mathematics | 0607 | 76 | 87 | 0 | 0.6 |
| `caie-igcse-islamiyat-0493` | caie | IGCSE | Islamiyat | 0493 | 67 | 3 | 0 | 0.1 |
| `caie-igcse-literature-in-english-0475` | caie | IGCSE | Literature in English | 0475 | 436 | 1 | 1 | 0.0 |
| `caie-igcse-mandarin-chinese-foreign-language-0547` | caie | IGCSE | Mandarin Chinese - Foreign Language | 0547 | 22 | 42 | 0 | 0.7 |
| `caie-igcse-mathematics-0580` | caie | IGCSE | Mathematics | 0580 | 269 | 231 | 2 | 6.8 |
| `caie-igcse-pakistan-studies-0448` | caie | IGCSE | Pakistan Studies | 0448 | 128 | 101 | 0 | 0.7 |
| `caie-igcse-physics-0625` | caie | IGCSE | Physics | 0625 | 112 | 145 | 0 | 1.5 |
| `caie-igcse-psychology-0266` | caie | IGCSE | Psychology | 0266 | 35 | 1 | 6 | 0.0 |
| `caie-igcse-sociology-0495` | caie | IGCSE | Sociology | 0495 | 82 | 4 | 0 | 0.2 |
| `caie-igcse-spanish-as-a-foreign-language-0530` | caie | IGCSE | Spanish as a Foreign Language | 0530 | 68 | 0 | 0 | 0.0 |
| `caie-igcse-statistics-0479` | caie | IGCSE | Statistics | 0479 | 69 | 3 | 0 | 0.0 |
| `caie-igcse-travel-and-tourism-0471` | caie | IGCSE | Travel and Tourism | 0471 | 26 | 0 | 0 | 0.0 |
| `caie-igcse-urdu-as-a-second-language-0539` | caie | IGCSE | Urdu as a Second Language | 0539 | 38 | 5 | 0 | 0.1 |
| `caie-o-level-bangladesh-studies-7094` | caie | O Level | Bangladesh Studies  | 7094 | 61 | 0 | 0 | 0.0 |
| `caie-o-level-bengali-3204` | caie | O Level | Bengali  | 3204 | 95 | 0 | 0 | 0.0 |
| `caie-o-level-biology-5090` | caie | O Level | Biology | 5090 | 0 | 0 | 0 | 0.0 |
| `caie-o-level-english-language-1123` | caie | O Level | English Language | 1123 | 36 | 0 | 0 | 0.0 |
| `edexcel-gcse-english-literature-4xet1` | edexcel | GCSE | English Literature | 4XET1 | 10 | 0 | 0 | 0.0 |
| `edexcel-gcse-physics-1ph0` | edexcel | GCSE | Physics | 1PH0 | 72 | 36 | 0 | 0.3 |
| `edexcel-gcse-psychology-1ps0` | edexcel | GCSE | Psychology | 1PS0 | 183 | 25 | 0 | 0.5 |
| `edexcel-igcse-accounting-4ac1` | edexcel | IGCSE | Accounting | 4AC1 | 96 | 34 | 0 | 1.0 |
| `edexcel-igcse-biology-4bi1` | edexcel | IGCSE | Biology | 4BI1 | 28 | 41 | 0 | 1.2 |
| `edexcel-igcse-business-4bs1` | edexcel | IGCSE | Business | 4BS1 | 47 | 1 | 0 | 0.0 |
| `edexcel-igcse-chemistry-4ch1` | edexcel | IGCSE | Chemistry | 4CH1 | 111 | 23 | 0 | 0.4 |
| `edexcel-igcse-economics` | edexcel | IGCSE | Economics  | — | 2 | 0 | 0 | 0.0 |
| `edexcel-igcse-history` | edexcel | IGCSE | History | — | 9 | 0 | 0 | 0.0 |
| `edexcel-igcse-mathematics-4ma1` | edexcel | IGCSE | Mathematics  | 4MA1 | 56 | 0 | 1 | 0.0 |
| `edexcel-igcse-physics-4ph1` | edexcel | IGCSE | Physics | 4PH1 | 69 | 91 | 1 | 4.3 |
| `edexcel-international-a-level-biology` | edexcel | IAL | Biology | — | 119 | 114 | 0 | 8.9 |
| `edexcel-international-a-level-business-xbs01` | edexcel | IAL | Business | XBS01 | 62 | 15 | 0 | 0.2 |
| `edexcel-international-a-level-chemistry` | edexcel | IAL | Chemistry | — | 217 | 94 | 3 | 1.0 |
| `edexcel-international-a-level-further-math` | edexcel | IAL | Further Math | — | 43 | 49 | 0 | 0.2 |
| `edexcel-international-a-level-maths` | edexcel | IAL | Maths | — | 157 | 63 | 0 | 3.1 |
| `edexcel-international-a-level-physics-xph11-and-yph11` | edexcel | IAL | Physics | XPH11 and YPH11 | 75 | 146 | 0 | 1.8 |
| `edexcel-international-a-level-political-science-9pl0` | edexcel | IAL | Political Science | 9PL0 | 177 | 0 | 0 | 0.0 |

## 4. Subject-lane universe & status

Join of: official CIE catalogs (page-sourced 2026-10-31), Pearson manual/SME-derived Edexcel universe, live registry, and the corpus. Statuses: **registered** (in syllabai-v2), **in corpus** (notes downloaded), **blocked** (no web-ready notes anywhere — verified), **twin/variant** (new-code twin of a registered subject).

### 4a. Importable lanes — notes in corpus, registry import pending

| Board | Level | Subject | Code | Corpus dir(s) | Note |
|---|---|---|---|---|---|
| CIE | IGCSE | Malay - First Language | 0696 | `caie-igcse-first-language-malay-0696` | reclassified from blocked — the ZNotes corpus covers this lane; registry import pending |
| CIE | IGCSE | Psychology | 0266 | `caie-igcse-psychology-0266` | reclassified from blocked — the ZNotes corpus covers this lane; registry import pending |
| CIE | IGCSE | Statistics | 0479 | `caie-igcse-statistics-0479` | reclassified from blocked — the ZNotes corpus covers this lane; registry import pending |
| CIE | IGCSE | Travel & Tourism | 0471 | `caie-igcse-travel-and-tourism-0471` | reclassified from blocked — the ZNotes corpus covers this lane; registry import pending |
| CIE | International A-Level | Design & Technology | 9705 | `caie-as-level-design-and-technology-9705` | reclassified from blocked — the ZNotes corpus covers this lane; registry import pending |
| CIE | International A-Level | Marine Science | 9693 | `caie-as-level-marine-science-9693` | reclassified from blocked — the ZNotes corpus covers this lane; registry import pending |
| CIE | IGCSE | Design & Technology | 0445 | `caie-igcse-design-and-technology-0445` | notes in corpus; registry import pending |
| CIE | IGCSE | Pakistan Studies | 0448 | `caie-igcse-pakistan-studies-0448` | notes in corpus; registry import pending |
| CIE | IGCSE | Enterprise | 0454 | `caie-igcse-enterprise-0454` | notes in corpus; registry import pending |
| CIE | IGCSE | Global Perspectives | 0457 | `caie-igcse-global-perspectives-0457` | notes in corpus; registry import pending |
| CIE | IGCSE | Islamiyat | 0493 | `caie-igcse-islamiyat-0493` | notes in corpus; registry import pending |
| CIE | IGCSE | Sociology | 0495 | `caie-igcse-sociology-0495` | notes in corpus; registry import pending |
| CIE | IGCSE | French - Foreign Language | 0520 | `caie-igcse-french-foreign-language-0520` | notes in corpus; registry import pending |
| CIE | IGCSE | German - Foreign Language | 0525 | `caie-igcse-german-foreign-language-0525` | notes in corpus; registry import pending |
| CIE | IGCSE | Spanish - Foreign Language | 0530 | `caie-igcse-spanish-as-a-foreign-language-0530` | notes in corpus; registry import pending |
| CIE | IGCSE | Urdu as a Second Language | 0539 | `caie-igcse-urdu-as-a-second-language-0539` | notes in corpus; registry import pending |
| CIE | IGCSE | Arabic - Foreign Language | 0544 | `caie-igcse-arabic-as-a-foreign-language-0544` | notes in corpus; registry import pending |
| CIE | IGCSE | Chinese (Mandarin) - Foreign Language | 0547 | `caie-igcse-mandarin-chinese-foreign-language-0547` | notes in corpus; registry import pending |
| CIE | IGCSE | Hindi as a Second Language | 0549 | `caie-igcse-hindi-as-a-second-language-0549` | notes in corpus; registry import pending |
| CIE | IGCSE | Food & Nutrition | 0648 | `caie-igcse-food-and-nutrition-0648` | notes in corpus; registry import pending |
| CIE | IGCSE | Sciences - Co-ordinated (Double) | 0654 | `caie-igcse-co-ordinated-sciences-0654` | notes in corpus; registry import pending |
| CIE | IGCSE | Vietnamese - First Language | 0695 | `caie-igcse-first-language-vietnamese-0695` | notes in corpus; registry import pending |
| CIE | IGCSE | English as a Second Language | 0510 | `caie-igcse-english-as-a-second-language-0510` | notes in corpus; registry import pending |
| CIE | IGCSE | English as a Second Language | 0511 | `caie-igcse-english-as-a-second-language-0510` | one ZNotes course serves both 0510/0511; registry import pending |
| CIE | International A-Level | Law | 9084 | `caie-a2-level-law-9084`, `caie-as-level-law-9084` | notes in corpus; registry import pending |
| CIE | International A-Level | English Language | 9093 | `caie-a2-level-english-language-9093`, `caie-as-level-english-language-9093` | notes in corpus; registry import pending |
| CIE | International A-Level | Mathematics - Further | 9231 | `caie-a2-level-further-mathematics-9231`, `caie-as-level-further-mathematics-9231` | notes in corpus; registry import pending |
| CIE | International A-Level | History | 9489 | `caie-as-level-history-9489` | notes in corpus; registry import pending |
| CIE | International A-Level | Information Technology | 9626 | `caie-a2-level-it-9626`, `caie-as-level-it-9626` | notes in corpus; registry import pending |
| CIE | International A-Level | Psychology | 9990 | `caie-a2-level-psychology-9990`, `caie-as-level-psychology-9990` | notes in corpus; registry import pending |
| Edexcel | IAL | Business Xbs01 | XBS01 | `edexcel-international-a-level-business-xbs01` | notes in corpus; registry import pending |
| CIE | International A-Level | Geography (skeleton completion) | 9696 | `caie-a2-level-geography-9696`, `caie-as-level-geography-9696` | registered (skeleton/newer row) — corpus fills it; avoid duplicate registration |

### 4b. Reconciliations found during this re-check

- CIE IGCSE **Malay - First Language 0696** was listed blocked but IS in the corpus (`caie-igcse-first-language-malay-0696`) — reclassified 'in corpus'
- CIE IGCSE **Psychology 0266** was listed blocked but IS in the corpus (`caie-igcse-psychology-0266`) — reclassified 'in corpus'
- CIE IGCSE **Statistics 0479** was listed blocked but IS in the corpus (`caie-igcse-statistics-0479`) — reclassified 'in corpus'
- CIE IGCSE **Travel & Tourism 0471** was listed blocked but IS in the corpus (`caie-igcse-travel-and-tourism-0471`) — reclassified 'in corpus'
- CIE International A-Level **Design & Technology 9705** was listed blocked but IS in the corpus (`caie-as-level-design-and-technology-9705`) — reclassified 'in corpus'
- CIE International A-Level **Marine Science 9693** was listed blocked but IS in the corpus (`caie-as-level-marine-science-9693`) — reclassified 'in corpus'
- Blocked-scan listed Edexcel IAL Business twice (it was already an importable lane, now in corpus: `edexcel-international-a-level-business-xbs01`) — deduplicated here
- Five lanes the scan listed importable — Latin **0480**, Arabic — First Language **0508**, CAIE AS English Literature **9695**, CAIE AS Sociology **9699**, Edexcel IAL English Literature (code pending) — have **no corpus dir**: the ZNotes API capture (all 97 upstream courses) contains no course for them; reverted to 'blocked'
- ESL **0511** shares the 0510 corpus course (`caie-igcse-english-as-a-second-language-0510`) — counted 'in corpus'
- CIE IGCSE Computer Science **0265** (blocked list) is the new-code twin of registered **0478** — classed twin/variant, not missing.
- US-variant lanes 0524 / 0409 / 0444 are US-specific twins of registered 0500 / 0470 / 0580.

### 4c. Blocked lanes — verified no web-ready revision notes (2026-11-01)

97 lanes. Class legend: **language** ×47 · **arts-practical** ×13 · **humanities** ×13 · **other** ×6 · **sci-tech** ×6 · **vocational** ×5 · **importable→blocked** ×5 · **skills** ×1 · **social-science** ×1.
Evidence (applies to every row): SME live re-crawl 2026-11-01 (no notes for any lane below — papers only), Maths Genie maths-only, Cognito UK-only, GCE Guide dead, PMT bot-gated with no blocked-lane coverage, PapersDaddy/thinka excluded on provenance, TeachifyMe covered-subjects-only. Language lanes are skills-based qualifications for which structured revision-note products do not exist free.

| Board | Level | Subject | Code | Class | Note |
|---|---|---|---|---|---|
| CIE | IGCSE | Afrikaans - Second Language | 0548 | language |  |
| CIE | IGCSE | Agriculture | 0600 | vocational |  |
| CIE | IGCSE | Art & Design | 0400 | arts-practical |  |
| CIE | IGCSE | Bahasa Indonesia | 0538 | other |  |
| CIE | IGCSE | Chinese - First Language | 0509 | language |  |
| CIE | IGCSE | Chinese - Second Language | 0523 | language |  |
| CIE | IGCSE | Commerce | 0715 | vocational |  |
| CIE | IGCSE | Drama | 0411 | arts-practical |  |
| CIE | IGCSE | French - First Language | 0501 | language |  |
| CIE | IGCSE | German - First Language | 0505 | language |  |
| CIE | IGCSE | IsiZulu as a Second Language | 0531 | language |  |
| CIE | IGCSE | Italian - Foreign Language | 0535 | language |  |
| CIE | IGCSE | Japanese - Foreign Language | 0716 | language |  |
| CIE | IGCSE | Malay - Foreign Language | 0546 | language |  |
| CIE | IGCSE | Marine Science | 0697 | sci-tech |  |
| CIE | IGCSE | Music | 0410 | arts-practical |  |
| CIE | IGCSE | Physical Education | 0413 | arts-practical |  |
| CIE | IGCSE | Physical Science | 0652 | sci-tech |  |
| CIE | IGCSE | Portuguese - First Language | 0504 | language |  |
| CIE | IGCSE | Sanskrit | 0499 | language |  |
| CIE | IGCSE | Setswana - First Language | 0698 | language |  |
| CIE | IGCSE | Spanish - First Language | 0502 | language |  |
| CIE | IGCSE | Spanish - Literature in Spanish | 0474 | language |  |
| CIE | IGCSE | Swahili | 0262 | language |  |
| CIE | IGCSE | Thai - First Language | 0518 | language |  |
| CIE | IGCSE | Turkish - First Language | 0513 | language |  |
| CIE | IGCSE | World Literature | 0408 | language |  |
| CIE | IGCSE | English (as an Additional Language) | 0472 | language |  |
| CIE | International A-Level | Afrikaans - Language (AS Level only) | 8679 | language |  |
| CIE | International A-Level | Arabic | 9680 | language |  |
| CIE | International A-Level | Arabic | 9865 | language |  |
| CIE | International A-Level | Arabic - Language (AS Level only) | 8680 | language |  |
| CIE | International A-Level | Art & Design | 9479 | arts-practical |  |
| CIE | International A-Level | Chinese Language (AS Level only) | 8238 | language |  |
| CIE | International A-Level | Classical Studies | 9274 | humanities |  |
| CIE | International A-Level | Digital Media & Design | 9481 | arts-practical |  |
| CIE | International A-Level | Drama | 9482 | arts-practical |  |
| CIE | International A-Level | European History | 9981 | humanities |  |
| CIE | International A-Level | French Language & Literature | 9898 | language |  |
| CIE | International A-Level | French Language (AS Level only) | 8028 | language |  |
| CIE | International A-Level | German - Language (AS Level only) | 8027 | language |  |
| CIE | International A-Level | Global Perspectives & Research | 9239 | humanities |  |
| CIE | International A-Level | Hinduism | 9487 | humanities |  |
| CIE | International A-Level | International History | 9982 | humanities |  |
| CIE | International A-Level | Islamic Studies | 9488 | humanities |  |
| CIE | International A-Level | Media Studies | 9607 | arts-practical |  |
| CIE | International A-Level | Music | 9483 | arts-practical |  |
| CIE | International A-Level | Portuguese - Language (AS Level only) | 8684 | language |  |
| CIE | International A-Level | Portuguese (A Level only) | 9718 | language |  |
| CIE | International A-Level | Spanish Language (AS Level only) | 8022 | language |  |
| CIE | International A-Level | Tamil | 9689 | other |  |
| CIE | International A-Level | Tamil - Language | 8689 | language |  |
| CIE | International A-Level | Thinking Skills | 9694 | skills |  |
| CIE | International A-Level | Travel & Tourism | 9395 | vocational |  |
| CIE | International A-Level | Urdu - Language (AS Level only) | 8686 | language |  |
| CIE | International A-Level | Urdu - Pakistan only (A Level only) | 9686 | language |  |
| CIE | International A-Level | US Government & Politics | 8293 | humanities |  |
| CIE | International A-Level | US History since 1877 | 8102 | humanities |  |
| CIE | International A-Level | US History to 1877 | 8101 | humanities |  |
| CIE | International A-Level | Biblical Studies | 9484 | other |  |
| CIE | International A-Level | Sport & Physical Education (AS Level only) | 8386 | arts-practical |  |
| Edexcel | IAL | Accounting | (page-source pending) | other | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Arabic | (page-source pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Economics | (page-source pending) | other | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | English Language | (page-source pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | French | (page-source pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Geography | (page-source pending) | other | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | German | (page-source pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Greek | (page-source pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | History | (page-source pending) | humanities | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Information Technology | (page-source pending) | sci-tech | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Law | (page-source pending) | humanities | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Psychology | (page-source pending) | social-science | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IAL | Spanish | (page-source pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IGCSE | Arabic | (code pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IGCSE | Art & Design | 4AD1 | arts-practical |  |
| Edexcel | IGCSE | Bengali | 4BN1 | language |  |
| Edexcel | IGCSE | Computer Science | 4CP1 | sci-tech |  |
| Edexcel | IGCSE | English Language B | 4EB1 | language |  |
| Edexcel | IGCSE | English as a Second Language | 4ES1 | language |  |
| Edexcel | IGCSE | French | 4FR1 | language |  |
| Edexcel | IGCSE | German | 4GN1 | language |  |
| Edexcel | IGCSE | Global Citizenship | 4GL1 | vocational |  |
| Edexcel | IGCSE | Greek | (code pending) | language | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IGCSE | Human Biology | 4HB1 | sci-tech |  |
| Edexcel | IGCSE | Music | 4MU1 | arts-practical |  |
| Edexcel | IGCSE | Physical Education | 4PE1 | arts-practical |  |
| Edexcel | IGCSE | Religious Studies | 4RS1 | humanities |  |
| Edexcel | IGCSE | Spanish | 4SP1 | language |  |
| Edexcel | IGCSE | Commerce | (code pending) | vocational | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IGCSE | Islamic Studies | (code pending) | humanities | syllabus code not yet page-sourced (Pearson manual pending) |
| Edexcel | IGCSE | Science (Single Award) | 4SS0 | sci-tech |  |
| CIE | IGCSE | Latin | 0480 | importable→blocked | NOT in corpus — ZNotes page seen at 2026-10-31 scan but the API capture contains no course (re-verified 2026-11-01) |
| CIE | IGCSE | Arabic - First Language | 0508 | importable→blocked | NOT in corpus — ZNotes page seen at 2026-10-31 scan but the API capture contains no course (re-verified 2026-11-01) |
| CIE | International A-Level | English - Literature | 9695 | importable→blocked | NOT in corpus — ZNotes page seen at 2026-10-31 scan but the API capture contains no course (re-verified 2026-11-01) |
| CIE | International A-Level | Sociology | 9699 | importable→blocked | NOT in corpus — ZNotes page seen at 2026-10-31 scan but the API capture contains no course (re-verified 2026-11-01) |
| Edexcel | IAL | English Literature | (code page-sourcing pending) | importable→blocked | NOT in corpus — ZNotes page seen at 2026-10-31 scan but the API capture contains no course; code also still unsourced |

### 4d. Twin/variant lanes (not missing)

| Board | Level | Subject | Code | Basis |
|---|---|---|---|---|
| CIE | IGCSE | Computer Science | 0265 | 9-1-style new-code twin of Computer Science 0478 (registered) |
| CIE | IGCSE | English - First Language (US) | 0524 | US-variant of English First Language (0500, registered) |
| CIE | IGCSE | History - American (US) | 0409 | US-variant of History (0470, registered) |
| CIE | IGCSE | Mathematics (US) | 0444 | US-variant of Mathematics (0580, registered) |

## 5. Image failures ledger

72 failures were documented across course manifests at T-ZNOTES-1 (third-party hotlink rot). T-ZNOTES-2 (PR #262, merged) re-sourced **24 byte-exactly** (wsrv.nl proxy ×14, Wayback ×4, URL repairs ×3, direct retry ×3; ~0.9 MB, 9 courses). The remaining **48 are dead at source** — expired signed Discord links (23+2), browser-internal `blob:` URIs (2), signed ChatGPT files (3), deleted imgur/S3/ZNotes-CDN uploads (9), bot-blocked ResearchGate (3), dead hosts (7), upstream placeholder defects (2) — with **no Wayback snapshot for any** (availability API checked per URL). They remain listed verbatim in the per-course `failures.images` and in `scripts/T-ZNOTES-2-resync-report.json`; leaf `.json` files keep the original URL and a `resourced_via` trail where recovered.

## 6. Task & PR history

| Task | PR | Merged | Content |
|---|---|---|---|
| T-ZNOTES-1 | #259 | 2026-10-31 | ZNotes CAIE + Edexcel corpus — 97 courses, 8,322 cards, 3,694 assets (~130 MB) |
| T-ZNOTES-2 | #262 | 2026-11-01 | Image-failure resync — 24/72 recovered byte-exactly, 48 documented unrecoverable; `resourced_via` trail + resync scripts |
| T-ZNOTES-3 | this PR | — | This tracker: corpus inventory reconciled to ground truth, lane universe re-verified against live sources, evidence trail for all remaining gaps |

## 7. Method & caveats

1. Inventory rows are read from per-course `manifest.json` at `main @ 4b75272d` — not re-derived.
2. Lane universe = CIE official IGCSE + AS/A-Level catalogs and Pearson-derived Edexcel IGCSE + IAL universe (page-sourced 2026-10-31, unchanged); CIE O-Level / Checkpoint / Edexcel UK-GCSE corpus dirs are bonus coverage outside that universe and are shown only in §3.
3. Registry join is by syllabus code; registry X-variants (e.g. 4XBI1) map to the base code lane.
4. Four Edexcel IGCSE lanes (Arabic, Greek, Commerce, Islamic Studies) still carry '(code pending)' — codes are never invented per the scan doctrine; verify against the Pearson Information Manual before registration.
5. AS-only corpus lanes (English Language 9093, English Literature 9695, History 9489, Sociology 9699): ZNotes has no A2 notes for these — flagged since the scan; no A2 source has emerged (re-checked 2026-11-01).
6. ESL 0510/0511 share one corpus course (`caie-igcse-english-as-a-second-language-0510`).
7. License/provenance doctrine (ADR-039) excludes unverifiable AI-content farms even when they claim coverage; if that bar is ever relaxed, PapersDaddy/thinka claims should be re-audited page-by-page first.
