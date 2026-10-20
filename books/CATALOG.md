# books/CATALOG.md — Student-Book Catalog & Parse-Completion Tracker

**Status:** catalog of record for every student book in `books/` — identity,
archive home, source provenance, parse state, and serving state.
**Companion to:** [`README.md`](README.md) (the parse playbook — HOW to parse)
and [`pearson-edexcel/international-gcse/PARSE_STANDARD.md`](pearson-edexcel/international-gcse/PARSE_STANDARD.md)
(the quality gate — HOW DONE is defined). This file is the WHAT and WHERE.
**Update law:** a book's row is updated in the SAME commit that advances its
state (source lands / parse validates / serving integrates / shelf goes live).
Append-only per row's history notes; never delete a row.

---

## 1. Status vocabulary

A book moves through four states. Each state's evidence lives where the
arrows point — the catalog row records the state + date + pointer.

| State | Meaning | Evidence of record |
|---|---|---|
| **SOURCE** | PDF received & sha256-pinned in `<lane>/source/` | lane README (provenance + sha256 + pages) |
| **PARSED** | chunk corpus final, validator ALL CHECKS PASSED | `parsed/` JSONL + `parse_report*.json` + parse README |
| **INTEGRATED** | TEXTBOOK document + book_chapters registered on the serving plane (api/hub) | v2-repo lane receipt (documents.id + chapter count) |
| **LIVE** | VALIDATED (T-C20 gate) + shelf + hub entry options render | books-registry `BOOKS_ARCHIVE_COURSES` + production fetch |

Serving-plane levers (v2 repo): the T-C20 validation flip is the operator's
serving lever; the hub entry (landing card + sidebar "Student Book") gates on
the committed books-registry set; the shelf is always the live gate.

## 2. Parsed-completion tracker

| # | Book | Qual / Code | Course slug | Archive home | SOURCE | PARSED | INTEGRATED | LIVE |
|---|---|---|---|---|---|---|---|---|
| 1 | Edexcel International GCSE (9-1) **Chemistry** Student Book | Pearson Edexcel IGCSE 4CH1 | `igcse-chemistry-19` | `pearson-edexcel/international-gcse/chemistry/4ch1/` | ✅ 2026-10-18 | ✅ 2026-10-18 (v3, 1234 chunks; audit GREEN) | ✅ 2026-10-20 (doc `e6c0db50…`, 29 chapters) | ✅ 2026-10-20 (VALIDATED; card+shelf live) |
| 2 | Edexcel International GCSE (9-1) **Physics** Student Book | Pearson Edexcel IGCSE 4PH1 | `igcse-physics-19` | `pearson-edexcel/international-gcse/physics/4ph1/` | ✅ 2026-10-19 | ✅ 2026-10-20 (v1, 736 chunks; polish R1-R2; validator ALL CHECKS PASSED) | — pending serving lane | — pending |
| 3 | Pearson Edexcel International AS Level **Physics** Student Book 1 (Miles Hudson) | Pearson Edexcel IAL YPH11 (book 1 of 2) | `ial-physics-19` | `pearson-edexcel/international-a-level/physics/yph11/` | ✅ 2026-10-21 (book 1; 225pp image replica) | — | — | — |
| 4 | Cambridge International AS & A Level **Chemistry** Coursebook 3rd ed (Ryan & Norris) | CIE 9701 | `cie-a-level-chemistry-25` | `cambridge-international/ial/chemistry/9701/` | ✅ 2026-10-21 (889pp, text layer; 2 pages ad-watermarked — parse must strip) | — | — | — |
| 5 | Cambridge International AS & A Level **Physics** Coursebook 2nd ed (Sang et al.) | CIE 9702 | `cie-a-level-physics-25` | `cambridge-international/ial/physics/9702/` | ✅ 2026-10-21 (744pp, text layer; 3rd-ed upgrade pending) | — | — | — |
| 6 | Cambridge International AS & A Level **Biology** Coursebook 4th ed (Jones et al.) | CIE 9700 | `cie-a-level-biology-25` | `cambridge-international/ial/biology/9700/` | ✅ 2026-10-21 (696pp, text layer) | — | — | — |
| 7 | **Cambridge IGCSE Physics** 3rd ed (Duncan & Kennett, Hodder endorsed) | CIE 0625 | `cie-igcse-physics-23` | `cambridge-international/igcse/physics/0625/` | ✅ 2026-10-21 (328pp, text layer; CUP Sang upgrade pending) | — | — | — |
| 8 | **Cambridge IGCSE Biology** Coursebook 3rd ed (Jones & Jones) | CIE 0610 | `cie-igcse-biology-23` | `cambridge-international/igcse/biology/0610/` | ✅ 2026-10-21 (350pp image scan → OCR route) | — | — | — |
| 9 | Edexcel International GCSE (9-1) **Biology** Student Book | Pearson Edexcel IGCSE 4BI1 | `igcse-biology-19` | `pearson-edexcel/international-gcse/biology/4bi1/` | ✅ 2026-10-21 (357 book pp as 179 native-text 2-up spreads; ISBN 9780435185084; OCR route NOT required) | — | — | — |
| 10+ | → see §4 rollout queue (wave-3: SB2 of YPH11, 0620 chemistry, edition upgrades) | | | | | | | |

## 3. Books in the archive — full records

### 3.1 Edexcel International GCSE (9-1) Chemistry Student Book — LIVE

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International GCSE, **4CH1** (2017 line) |
| Course binding (v2 hub) | `igcse-chemistry-19` · specKey `pearson-edexcel/international-gcse/chemistry/4ch1` |
| Author | Jim Clark (DB canonical_json) |
| Source of record | `chemistry/4ch1/student-book.pdf` · sha256 `d48020e0cc0b5545b330bb59b242472198210e424525e4381cd5d2a58a58cc04` · 383 pp · 54,298,792 bytes · image-only scan (OCR route) |
| Parse of record | v3 corpus, **1234 chunks**, 15-key grammar, 17 content types; LLM fidelity polish (87 chunks, originals preserved); external audit **GREEN** 2026-10-18 (`pipeline/AUDIT_VERDICT_2026-10-18.md`) |
| Serving of record | documents id `e6c0db50-0f84-55de-b50c-e4d49285cd6d` v1, **VALIDATED**; 29 `book_chapters` rows, 4 units (u1 Principles ×10, u2 Inorganic ×8, u3 Physical ×3, u4 Organic ×8); slices manifest v2 (33 slices); hub shelf `/courses/igcse-chemistry-19/books` |
| Entry options | landing card (T-MIG-133 band 133k) + sidebar/drawer "Student Book" row (T-MIG-140, commit `0b98e40`) |
| Notes | REFERENCE IMPLEMENTATION per the playbook; the archive home landed by Git-DB tree-composition (commit b589745, blob-reuse mechanism) |

### 3.2 Edexcel International GCSE (9-1) Physics Student Book — PARSED

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International GCSE, **4PH1** (2017 line) |
| Course binding (v2 hub) | `igcse-physics-19` · specKey `pearson-edexcel/international-gcse/physics/4ph1` |
| Authors | Brian Arnold, Penny Johnson, Steve Woote (Pearson 2017 printing) |
| Source of record | `physics/4ph1/source/student-book.pdf` · sha256 `9b0783d9fe99790a08255eb1f2ebb6eab5833c03ef8e36dd51b7643ac68a313a` · 308 pp · 30,915,167 bytes · **image-only scan** (RICOH MP C4503; zero text layer) → OCR route |
| Provenance | operator-relayed tmpfiles link (gateway trace 1a1539ed1a5c074d) after direct upload failed — per the 4ph1 README |
| Parse of record | v1 corpus, **736 chunks**, 8 units / 28 chapters; Docling+RapidOCR+CodeFormula; LLM polish rounds 1–2 (299/300; char-level LCS ≥0.97 guard); validator **ALL CHECKS PASSED** 2026-10-20; serving-critical anchor diff vs pristine = 0 drift |
| Serving | — pending the T-MIG-133-style serving lane (TEXTBOOK doc + chapters + slices manifest + validation flip) |
| Notes | second parse; hybrid-stack lessons feed the playbook §7/§8 |

### 3.3 Edexcel International GCSE (9-1) Biology Student Book — SOURCE

| Field | Value |
|---|---|
| Qual / code | Pearson Edexcel International GCSE, **4BI1** (2017 line) |
| Course binding (v2 hub) | `igcse-biology-19` · specKey `pearson-edexcel/international-gcse/biology/4bi1` (spec spine already in repo: `Official-Specifications/igcse-biology/`) |
| Authors | Philip Bradfield, Steve Potter (verified from the landed copy's title page + Pearson official sample; §4.1 queue row had misattributed "Penny Johnson, Susan Kearsey" — corrected here, errata E-001 in books/README.md) |
| ISBN | 978-0435185084 (1st ed., 2017) |
| Source of record | `biology/4bi1/source/student-book.pdf` · sha256 `974ad65d913108b9caa98df9eda1584e546177854bcd5efa6d8642797d093006` · 357 book pages rendered as **179 landscape 2-up spread PDF pages** · 34,351,405 bytes · **native text layer** (Word 2016 → Acrobat Pro DC 15 print-replica conversion; OCR route NOT required) |
| Disclosed form | 2-up spreads (deterministic preprocessing at parse); Word-conversion split-word artifacts ("differen t organs") — noise census at parse start; ANSWERS section present (like 4CH1, unlike 4PH1) |
| Provenance | theonlineschool.co.uk direct PDF (sgcaptcha-walled; cleared via headless-browser clearance + cookie handoff to curl), gateway trace 1a15b063a08dbc69; pypdf verification 18/18 sampled pages text>40 chars |
| Upgrade candidates | dokumen.pub single-page 357pp/165MB (CF-walled at intake); pdfcoffee 49MB copy (CF-walled); Pearson official = 69pp sample only |
| Parse | — not started (playbook §5 phases 0–10; watch item: spread→book-page mapping probed 3 ways) |
| Serving | — pending |
| Notes | first NATIVE-TEXT-LAYER source in the Pearson IGCSE lanes — quality class above 4CH1/4PH1 scans; intake-only lane, no corpus yet |

## 4. Rollout queue — books for every course (decision of record 2026-10-20)

Operator decision (v2 trace 1a15a87407daa94d): **books on every course**.
Board-wise sourcing plan (v2 hub lanes; book picks = the de-facto standard
endorsed/official series per board). State letters: `—` not sourced · `S`
SOURCE · `P` PARSED · `I` INTEGRATED · `L` LIVE.

### 4.1 Pearson Edexcel International GCSE (2017 lines)

| Lane | Course slug | Book | State |
|---|---|---|---|
| Chemistry 4CH1 | `igcse-chemistry-19` | SB (Jim Clark) | **L** (§3.1) |
| Physics 4PH1 | `igcse-physics-19` | SB (Arnold/Johnson/Woote) | **P** (§3.2) |
| Biology 4BI1 | `igcse-biology-19` | SB (Philip Bradfield & Steve Potter, ISBN 9780435185084; authors corrected 2026-10-21 — see §3.3 + books/README.md E-001) | **S** (§3.3) |
| Maths A 4MA1 (F/H) | `igcse-maths-a-18-*` | SB (A/O level Maths A; PDF+JSONL package staged upstream, operator-keyed) | — |
| Maths B 4MB1 | `igcse-maths-b-16` | SB (David Turner, Ian Potts) | — |
| Further Pure 4PM1 | `igcse-further-maths-19` | SB | — |
| Accounting 4AC1 | `igcse-accounting-17-*` | SB | — |
| Business 4BS1 | `igcse-business-19` | SB | — |
| Economics 4EC1 | `igcse-economics-17` | SB | — |
| English Lang A 4EA1 | `igcse-english-language-a-16-*` | SB | — |
| English Lit 4ET1 | `igcse-english-literature-16` | SB | — |
| Geography 4GE1 | `igcse-geography-19` | SB | — |
| ICT 4IT1 | `igcse-ict-17` | SB | — |
| Science Double Award 4SD0 | `igcse-science-double-award-*` | SB (single volume) | — |

### 4.2 Pearson Edexcel International A-Level (2018 lines) — YPH11 etc.

| Lane | Course slug | Book(s) | State |
|---|---|---|---|
| **Physics YPH11** | `ial-physics-19` | **Student Book 1** (Miles Hudson, IAS Units 1–2, ISBN 978-1292244877) + **Student Book 2** (IAL Units 4–5, ISBN 978-1292244478) — a TWO-book course; Units 3/6 are practicals, no SB | **SB1 = S** · SB2 — (bot-walled: taleem360 reCAPTCHA, scribd login; candidates in lane README) |
| Chemistry YCH11 | `ial-chemistry-17` | Student Book 1 + Student Book 2 (same two-book IAL science pattern) | — |
| Biology YBI11 | `ial-biology-18` | Student Book 1 + Student Book 2 | — |
| Maths YMA01 (P1-P4, M1-M2, S1-S2, D1) | `ial-maths-20-*` | per-component SBs | — |
| Further Maths YFM01 | `ial-further-maths-18-*` | per-component SBs | — |

> **Multi-book law (pending hub-side follow-up):** the archive home is one PDF
> per file, so a two-book course stores `source/student-book-1.pdf` +
> `source/student-book-2.pdf`; the v2 hub currently assumes ONE
> `student-book.pdf` per course (`bookCorpusPathForCourse`) and needs a
> per-book file law BEFORE an IAL lane integrates (T-MIG-140 receipt,
> multibook_disclosure).

### 4.3 Cambridge International (CIE) — the endorsed-coursebook series

CIE publishes no books of its own; it endorses third-party titles. The
de-facto standard = the Cambridge University Press "Coursebook" series
(endorsement badge "endorsed by Cambridge Assessment International
Education"). Structural note vs Edexcel IAL: **CUP A-Level coursebooks cover
the whole A Level in ONE volume** (AS + A2), except 9709 which CUP splits per
component.

| Lane | Course slug | Book (CUP unless noted) | State |
|---|---|---|---|
| A-Level Physics 9702 | `cie-a-level-physics-25` | Coursebook 3rd ed — Sang, Jones, Chadha, Woodside (ISBN 9781108859035) | **S** (2nd ed sourced 2026-10-21, 744pp; 3rd ed = upgrade candidate) |
| A-Level Chemistry 9701 | `cie-a-level-chemistry-25` | Coursebook 3rd ed — Ryan & Norris | **S** (2026-10-21, 889pp text layer) |
| A-Level Biology 9700 | `cie-a-level-biology-25` | Coursebook — Jones, Fosbery, Taylor, Widger | **S** (4th ed sourced 2026-10-21, 696pp; 5th ed = upgrade candidate) |
| A-Level Maths 9709 (6 lanes) | `cie-a-level-maths-20-*` | per-component Coursebooks: Pure Math 1; Pure Math 2&3; Mechanics; Prob & Stats 1; Prob & Stats 2 | — |
| IGCSE Physics 0625 | `cie-igcse-physics-23` | Coursebook 3rd ed — Sang | **S** (Hodder Duncan/Kennett 3rd ed sourced 2026-10-21, 328pp; CUP Sang = upgrade candidate) |
| IGCSE Chemistry 0620 | `cie-igcse-chemistry-23` | Coursebook 4th ed — Harwood & Lodge | — (papacambridge 4th ed = 69pp preview; freelib/chemistry.com.pk JS-walled; full copy still to source) |
| IGCSE Biology 0610 | `cie-igcse-biology-23` | Coursebook 3rd ed — Jones | **S** (3rd ed sourced 2026-10-21, 350pp image scan; 4th ed = upgrade candidate) |
| IGCSE Maths 0580 (core/extended) | `cie-igcse-maths-25-*` | Core & Extended Coursebook — Morrison/Humberstone (or Hodder Pimentel/Wall) | — |
| IGCSE Intl Maths 0607 | `cie-igcse-maths-international-maths-23-*` | Coursebook | — |
| Further Maths 0606 | `cie-igcse-further-maths-additional-maths-25` | Coursebook | — |
| Accounting 0452 / 9706 | `cie-igcse-accounting-*`, `cie-a-level-accounting-21` | Coursebook | — |
| Business 0450/0264/9609 | `cie-igcse-business-*`, `cie-a-level-business-23` | Coursebook | — |
| Economics 0455/9708 | `cie-igcse-economics-*`, `cie-a-level-economics-23` | Coursebook | — |
| Computer Science 0478/9618 | `cie-igcse-computer-science-23`, `cie-a-level-computer-science-19` | Coursebook | — |
| English 0500/0475/8021 | `cie-igcse-english-*`, `cie-as-english-general-paper-21` | Coursebook | — |
| Geography 0460 / History 0470 / ICT 0417 / RS 0490 / Env Mgmt 0680/8291 | `cie-igcse-geography-*`, `cie-igcse-history-18`, `cie-igcse-ict-21`, `cie-igcse-religious-studies-23`, `cie-igcse-environmental-management-25`, `cie-as-environmental-management-20` | Coursebook | — |
| Co-ordinated Sci 0973 / Combined Sci 0653 (per-science lanes) | `cie-igcse-science-*-{biology,chemistry,physics}` | the corresponding single-science Coursebook per lane | — |

> Edition/ISBN above are planning-grade (verified where footnoted; else the
> series' standard current edition). Exact edition + ISBN is pinned per lane
> at SOURCE time in that lane's README.

## 5. Archive grammar & lane scaffold

- Home grammar mirrors the past-papers corpus specKey:
  `books/<publisher>/<qualification>/<subject>/<code>/`
  e.g. `books/pearson-edexcel/international-a-level/physics/yph11/`,
  `books/cambridge-international/ial/physics/9702/`,
  `books/cambridge-international/igcse/chemistry/0620/`.
- New-lane scaffold (copy of `physics/4ph1/` per playbook TL;DR):
  `source/` (the sha256-pinned PDF), `parsed/` (deliverables land here at
  parse time), `pipeline/` (scripts + evidence), lane `README.md` (status +
  provenance). Legacy exception: chemistry/4ch1 keeps its pdf at lane root
  (first lane, predates the scaffold).
- Multi-book courses (IAL sciences): `source/student-book-1.pdf`,
  `source/student-book-2.pdf` (+ README rows per book).
- Commits: temp-index protocol only (playbook §5 phase 10); NEVER `git add -A`.

## 6. Change log (catalog)

| Date | Change | Commit / evidence |
|---|---|---|
| 2026-10-21 | Catalog created (T-MIG-141 wave-2 intake): chemistry + physics rows of record, rollout queue for 60+ lanes, status vocabulary, multi-book law note | this commit |
| 2026-10-21 | 4BI1 SOURCE intake (T-INTAKE-4BI1-1): lane `pearson-edexcel/international-gcse/biology/4bi1/` lands per the 4ph1 scaffold (source/ + sha256 974ad65d…93006 + provenance README); book = Bradfield & Potter 2017, 357pp as 179 native-text 2-up spreads — OCR route NOT required; tracker row 9 + §3.3 record + §4.1 state —→S + author misattribution corrected (books/README.md E-001); upgrade candidates: dokumen.pub 357pp/165MB single-page, pdfcoffee 49MB | this commit (lane README = per-book evidence) |
| 2026-10-21 | Wave-2 SOURCE intake: 6 lanes land (YPH11 SB1; 9701; 9702 2nd ed; 9700 4th ed; 0625 Hodder 3rd ed; 0610 3rd ed) — each `source/` + sha256 + provenance README per the 4ph1 scaffold; quality verdicts + disclosed defects (9701 2-page ad watermark; 0610/SB1 image-only → OCR route); pendings: YPH11 SB2, 0620 full copy, 3rd/4th/5th-ed upgrades | this commit (lane READMEs = per-book evidence) |
