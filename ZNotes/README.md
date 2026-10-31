# ZNotes Revision Notes (CAIE + Edexcel — znotes.org web notes)

Scraped from ZNotes' web revision notes (T-ZNOTES-1, fetched 2026-10-31, base commit `992bf84b`), via the public `api.znotes.org` content API — boards `caie` + `edexcel`, every level, including WIP subjects. Mirrors `../SME-RevisionNotes/` conventions: per note `<leaf>.json` (metadata + provenance + image manifest) + `<leaf>.md` (render; upstream markdown kept verbatim incl. `$…$` LaTeX and inline HTML tables), with all referenced images downloaded into a flat per-course `assets/` folder and markdown links rewritten to `../../../assets/<file>`.

- **97 courses** (CAIE IGCSE/AS/A2/O-Level/Checkpoint, Edexcel IGCSE/IAL/GCSE) · **293 note modules · 1701 chapters · 8322 leaf notes** · 3694 assets (130 MB) · 16.3 M markdown chars.

- Slugs/subject codes are the upstream ZNotes values verbatim (`courses_index.json` is the capture of `/v1/boards` + `/v1/subjects`); nothing invented. Where ZNotes has no code on record (e.g. `edexcel-igcse-economics`), the folder keeps the bare slug — do not hand-fill codes.

- Upstream response shapes preserved: a chapter with no content returns `{message: 'No cards found for this chapter'}` → recorded as an empty leaf list (103 such WIP chapters). `content_arabic`/`content_chinese` card translations exist upstream; English `content` is what we store (`has_translations` flags it).

- **72 image failures** across the corpus, all third-party hotlink rot (discord/imgur/bing/researchgate/wikimedia → 404/403/429, 2 `blob:` editor artifacts): each is listed in the course `manifest.json` `failures.images` and left pointing at its original URL in the `.md`. Nothing invented to fill gaps.

- Provenance per leaf: `note_id`, source `url`, `author`, `created_at`/`updated_at`, `chapter_outcomes`, module metadata (incl. upstream `updated_to` syllabus years and `syllabus_guide` links). PDF/video modules are out of scope (notes only).

- License: upstream content © ZNotes (znotes.org), captured for internal study-platform use — not for redistribution. See `../LICENSE-DATA.md` for the corpus-wide licensing frame; flag to the operator before any external serving.


## Rebuild / refresh

```bash
python3 ZNotes/scripts/zn_fetch.py --index        # refresh course index from the API
python3 ZNotes/scripts/zn_fetch.py --all            # resumable scrape (skips complete courses)
python3 ZNotes/scripts/zn_fetch.py --manifest       # rebuild the global manifest
```
stdlib-only; resumable; courses with `fetch_failures > 0` are automatically re-fetched on the next run. Upstream empty-chapter responses are treated as data, not errors.


## Coverage

| course | subject | code | mods | chapters | notes | assets | img_fail | MB |
|---|---|---|---:|---:|---:|---:|---:|---:|
| caie-a2-level-accounting-9706 | Accounting | 9706 | 3 | 10 | 43 | 6 | 0 | 0.1 |
| caie-a2-level-biology-9700 | Biology | 9700 | 2 | 11 | 115 | 67 | 0 | 2.9 |
| caie-a2-level-business-9609 | Business | 9609 | 3 | 22 | 79 | 30 | 0 | 1.0 |
| caie-a2-level-chemistry-9701 | Chemistry | 9701 | 2 | 19 | 166 | 142 | 14 | 5.1 |
| caie-a2-level-computer-science-9618 | Computer Science | 9618 | 2 | 8 | 31 | 24 | 0 | 0.3 |
| caie-a2-level-economics-9708 | Economics | 9708 | 2 | 6 | 55 | 60 | 0 | 0.9 |
| caie-a2-level-english-language-9093 | English Language | 9093 | 0 | 0 | 0 | 0 | 0 | 0.0 |
| caie-a2-level-further-mathematics-9231 | Further Mathematics | 9231 | 3 | 17 | 83 | 117 | 0 | 0.9 |
| caie-a2-level-geography-9696 | Geography | 9696 | 2 | 4 | 19 | 53 | 0 | 8.7 |
| caie-a2-level-it-9626 | IT | 9626 | 2 | 9 | 39 | 12 | 0 | 0.0 |
| caie-a2-level-law-9084 | Law | 9084 | 2 | 8 | 36 | 0 | 0 | 0.0 |
| caie-a2-level-mathematics-9709 | Mathematics | 9709 | 2 | 14 | 63 | 26 | 0 | 0.9 |
| caie-a2-level-physics-9702 | Physics | 9702 | 3 | 19 | 132 | 54 | 0 | 1.7 |
| caie-a2-level-psychology-9990 | Psychology | 9990 | 3 | 15 | 51 | 26 | 2 | 5.3 |
| caie-as-level-accounting-9706 | Accounting | 9706 | 1 | 3 | 29 | 8 | 0 | 0.1 |
| caie-as-level-biology-9700 | Biology | 9700 | 3 | 21 | 119 | 48 | 1 | 4.7 |
| caie-as-level-business-9609 | Business | 9609 | 4 | 34 | 251 | 18 | 0 | 1.2 |
| caie-as-level-chemistry-9701 | Chemistry | 9701 | 6 | 59 | 197 | 176 | 3 | 3.9 |
| caie-as-level-computer-science-9618 | Computer Science | 9618 | 2 | 12 | 51 | 23 | 0 | 0.4 |
| caie-as-level-design-and-technology-9705 | Design and Technology | 9705 | 1 | 12 | 57 | 14 | 0 | 0.3 |
| caie-as-level-economics-9708 | Economics | 9708 | 3 | 15 | 47 | 14 | 0 | 0.4 |
| caie-as-level-english-general-paper-8021 | English General Paper | 8021 | 3 | 10 | 38 | 10 | 0 | 0.5 |
| caie-as-level-english-language-9093 | English Language | 9093 | 5 | 7 | 41 | 0 | 0 | 0.0 |
| caie-as-level-further-mathematics-9231 | Further Mathematics | 9231 | 1 | 7 | 49 | 38 | 0 | 0.5 |
| caie-as-level-geography-9696 | Geography | 9696 | 3 | 16 | 88 | 46 | 0 | 9.0 |
| caie-as-level-history-9489 | History | 9489 | 3 | 16 | 321 | 0 | 0 | 0.0 |
| caie-as-level-it-9626 | IT | 9626 | 3 | 21 | 80 | 89 | 1 | 1.0 |
| caie-as-level-law-9084 | Law | 9084 | 2 | 6 | 31 | 0 | 0 | 0.0 |
| caie-as-level-marine-science-9693 | Marine Science | 9693 | 1 | 5 | 35 | 9 | 5 | 0.3 |
| caie-as-level-mathematics-9709 | Mathematics | 9709 | 4 | 35 | 138 | 133 | 0 | 1.5 |
| caie-as-level-physics-9702 | Physics | 9702 | 2 | 19 | 49 | 19 | 2 | 0.5 |
| caie-as-level-psychology-9990 | Psychology | 9990 | 3 | 16 | 61 | 3 | 0 | 0.1 |
| caie-checkpoint-english | English | — | 3 | 4 | 19 | 0 | 0 | 0.0 |
| caie-checkpoint-english-as-second-language-undefined | English as Second Language | — | 3 | 9 | 30 | 0 | 0 | 0.0 |
| caie-checkpoint-mathematics | Mathematics | — | 5 | 18 | 66 | 47 | 5 | 0.7 |
| caie-checkpoint-science | Science | — | 3 | 30 | 193 | 90 | 1 | 2.2 |
| caie-igcse-accounting-0452 | Accounting | 0452 | 3 | 22 | 37 | 8 | 0 | 0.1 |
| caie-igcse-additional-mathematics-0606 | Additional Mathematics | 0606 | 1 | 14 | 65 | 27 | 1 | 0.3 |
| caie-igcse-arabic-as-a-foreign-language-0544 | Arabic as a Foreign Language | 0544 | 5 | 16 | 132 | 11 | 0 | 0.3 |
| caie-igcse-biology-0610 | Biology | 0610 | 3 | 49 | 209 | 135 | 5 | 6.5 |
| caie-igcse-business-0264 | Business | 0264 | 6 | 7 | 34 | 12 | 0 | 0.1 |
| caie-igcse-business-studies-0450 | Business Studies | 0450 | 4 | 12 | 99 | 18 | 0 | 0.1 |
| caie-igcse-chemistry-0620 | Chemistry | 0620 | 4 | 42 | 218 | 148 | 1 | 2.8 |
| caie-igcse-co-ordinated-sciences-0654 | Co-ordinated Sciences | 0654 | 3 | 24 | 56 | 11 | 0 | 0.3 |
| caie-igcse-combined-science-0653 | Combined Science | 0653 | 4 | 16 | 37 | 22 | 0 | 1.2 |
| caie-igcse-computer-science-0478 | Computer Science | 0478 | 2 | 10 | 52 | 38 | 1 | 0.3 |
| caie-igcse-design-and-technology-0445 | Design and Technology | 0445 | 4 | 20 | 66 | 165 | 0 | 4.1 |
| caie-igcse-economics-0455 | Economics | 0455 | 4 | 33 | 153 | 17 | 2 | 0.1 |
| caie-igcse-english-as-a-second-language-0510 | English as a Second Language | 0510 | 5 | 16 | 79 | 30 | 0 | 0.5 |
| caie-igcse-enterprise-0454 | Enterprise  | 0454 | 2 | 20 | 48 | 6 | 0 | 0.1 |
| caie-igcse-environmental-management-0680 | Environmental Management | 0680 | 1 | 9 | 57 | 85 | 0 | 16.1 |
| caie-igcse-first-language-english-0500 | First Language English | 0500 | 4 | 19 | 51 | 0 | 0 | 0.0 |
| caie-igcse-first-language-malay-0696 | First Language Malay | 0696 | 2 | 6 | 26 | 5 | 0 | 0.1 |
| caie-igcse-first-language-vietnamese-0695 | First Language Vietnamese | 0695 | 2 | 6 | 20 | 0 | 0 | 0.0 |
| caie-igcse-food-and-nutrition-0648 | Food and Nutrition | 0648 | 1 | 14 | 72 | 0 | 0 | 0.0 |
| caie-igcse-french-foreign-language-0520 | French - Foreign Language | 0520 | 7 | 32 | 197 | 2 | 0 | 0.0 |
| caie-igcse-geography-0460 | Geography | 0460 | 4 | 21 | 71 | 92 | 0 | 4.7 |
| caie-igcse-german-foreign-language-0525 | German - Foreign Language | 0525 | 4 | 37 | 186 | 13 | 1 | 0.3 |
| caie-igcse-global-perspectives-0457 | Global Perspectives | 0457 | 1 | 4 | 19 | 0 | 0 | 0.0 |
| caie-igcse-hindi-as-a-second-language-0549 | Hindi as a Second Language | 0549 | 2 | 5 | 25 | 14 | 0 | 0.6 |
| caie-igcse-history-0470 | History | 0470 | 5 | 30 | 129 | 11 | 0 | 2.4 |
| caie-igcse-ict-0417 | ICT | 0417 | 3 | 24 | 129 | 78 | 2 | 0.6 |
| caie-igcse-international-mathematics-0607 | International Mathematics | 0607 | 1 | 10 | 76 | 87 | 0 | 0.6 |
| caie-igcse-islamiyat-0493 | Islamiyat | 0493 | 2 | 8 | 67 | 3 | 0 | 0.1 |
| caie-igcse-literature-in-english-0475 | Literature in English | 0475 | 8 | 78 | 436 | 1 | 1 | 0.0 |
| caie-igcse-mandarin-chinese-foreign-language-0547 | Mandarin Chinese - Foreign Language | 0547 | 1 | 8 | 22 | 42 | 0 | 0.7 |
| caie-igcse-mathematics-0580 | Mathematics | 0580 | 5 | 42 | 269 | 228 | 5 | 6.7 |
| caie-igcse-pakistan-studies-0448 | Pakistan Studies | 0448 | 2 | 11 | 128 | 101 | 0 | 0.7 |
| caie-igcse-physics-0625 | Physics | 0625 | 4 | 27 | 112 | 145 | 0 | 1.5 |
| caie-igcse-psychology-0266 | Psychology | 0266 | 1 | 7 | 35 | 1 | 6 | 0.0 |
| caie-igcse-sociology-0495 | Sociology | 0495 | 1 | 5 | 82 | 4 | 0 | 0.2 |
| caie-igcse-spanish-as-a-foreign-language-0530 | Spanish as a Foreign Language | 0530 | 5 | 22 | 68 | 0 | 0 | 0.0 |
| caie-igcse-statistics-0479 | Statistics | 0479 | 1 | 12 | 69 | 3 | 0 | 0.0 |
| caie-igcse-travel-and-tourism-0471 | Travel and Tourism | 0471 | 1 | 5 | 26 | 0 | 0 | 0.0 |
| caie-igcse-urdu-as-a-second-language-0539 | Urdu as a Second Language | 0539 | 3 | 5 | 38 | 5 | 0 | 0.1 |
| caie-o-level-bangladesh-studies-7094 | Bangladesh Studies  | 7094 | 2 | 14 | 61 | 0 | 0 | 0.0 |
| caie-o-level-bengali-3204 | Bengali  | 3204 | 5 | 25 | 95 | 0 | 0 | 0.0 |
| caie-o-level-biology-5090 | Biology | 5090 | 0 | 0 | 0 | 0 | 0 | 0.0 |
| caie-o-level-english-language-1123 | English Language | 1123 | 3 | 9 | 36 | 0 | 0 | 0.0 |
| edexcel-gcse-english-literature-4xet1 | English Literature | 4XET1 | 4 | 11 | 10 | 0 | 0 | 0.0 |
| edexcel-gcse-physics-1ph0 | Physics | 1PH0 | 2 | 24 | 72 | 36 | 0 | 0.3 |
| edexcel-gcse-psychology-1ps0 | Psychology | 1PS0 | 6 | 23 | 183 | 25 | 0 | 0.5 |
| edexcel-igcse-accounting-4ac1 | Accounting | 4AC1 | 3 | 25 | 96 | 29 | 5 | 0.8 |
| edexcel-igcse-biology-4bi1 | Biology | 4BI1 | 1 | 5 | 28 | 41 | 0 | 1.2 |
| edexcel-igcse-business-4bs1 | Business | 4BS1 | 1 | 5 | 47 | 1 | 0 | 0.0 |
| edexcel-igcse-chemistry-4ch1 | Chemistry | 4CH1 | 4 | 28 | 111 | 22 | 1 | 0.4 |
| edexcel-igcse-economics | Economics  | — | 1 | 16 | 2 | 0 | 0 | 0.0 |
| edexcel-igcse-history | History | — | 2 | 10 | 9 | 0 | 0 | 0.0 |
| edexcel-igcse-mathematics-4ma1 | Mathematics  | 4MA1 | 6 | 11 | 56 | 0 | 1 | 0.0 |
| edexcel-igcse-physics-4ph1 | Physics | 4PH1 | 4 | 24 | 69 | 91 | 1 | 4.3 |
| edexcel-international-a-level-biology | Biology | — | 7 | 13 | 119 | 113 | 1 | 8.9 |
| edexcel-international-a-level-business-xbs01 | Business | XBS01 | 3 | 16 | 62 | 15 | 0 | 0.2 |
| edexcel-international-a-level-chemistry | Chemistry | — | 8 | 47 | 217 | 94 | 3 | 1.0 |
| edexcel-international-a-level-further-math | Further Math | — | 2 | 12 | 43 | 49 | 0 | 0.2 |
| edexcel-international-a-level-maths | Maths | — | 5 | 32 | 157 | 62 | 1 | 3.1 |
| edexcel-international-a-level-physics-xph11-and-yph11 | Physics | XPH11 and YPH11 | 3 | 18 | 75 | 146 | 0 | 1.8 |
| edexcel-international-a-level-political-science-9pl0 | Political Science | 9PL0 | 5 | 48 | 177 | 0 | 0 | 0.0 |
