# LICENSE-DATA — Data Licensing & Provenance Notice

**Added:** 2026-09-15 (documentation audit reconciliation, audit item D9)
**Scope:** the corpus content in this repository. The repository's own tooling and scripts are code and follow the repository license; this notice covers the collected/derived content.

## What this repository contains

The RAG revision-note corpus: SME-authored IGCSE Chemistry (4CH1) revision notes derived from Save My Exams material, with per-note YAML front-matter carrying source URLs, capture dates, SHA-256 identity and spec-point mappings (T-C09/T-C10 governance); the 4CH1 specification document; PhysicsAndMathsTutor (PMT) Edexcel IGCSE Chemistry resources; and KG/graph build scripts.

## Source and provenance

- Examination material © Pearson Education Ltd (Edexcel); revision-note content derived from Save My Exams material © Save My Exams Ltd, with source URLs preserved in each note's YAML front-matter (capture date + provenance tier). All of it is used for a non-commercial, educational course project (an adaptive-learning research pilot for ~50 students); no commercial use is made of this content and no ownership is claimed.
- Provenance is machine-checkable: SHA-256 checksums, manifests and ledgers accompany the material (see the corpus manifests and `MANIFEST.json` / per-paper `manifest.yaml` records).

## Licensing position

- Internal pilot use under institution/own-use terms (ADR-013 posture). Re-check terms before any redistribution — redistribution is **not** authorized by this notice. *(Amended 2026-09-17 for Save My Exams material — see the amendment section below.)*
- Takedown / correction requests: open an issue on this repository or contact the repository owner via GitHub; affected material will be removed promptly.

## Amendment 2026-09-17 — Save My Exams authorization (operator attestation)

The operator (Nawaf Al Hussain Khondokar) attests that Save My Exams Ltd has
granted SyllabAI permission to use the SME-derived revision-note corpus in the
SyllabAI product, and that Save My Exams will sponsor the project. Recorded
verbatim in-session, 2026-09-17: "there is no licensing issue with SME, I have
their permission. (in fact they will be sponsoring me)".

Consequences of this amendment:

- The "redistribution is not authorized" position above is **amended for
  Save My Exams material only**: use and redistribution of SME-derived
  corpora inside SyllabAI surfaces (including this repository and the
  authenticated product) is covered by the rights holder's authorization
  as attested above. Covered corpora: the revision-note corpus
  (`Chemistry IGCSE Revision Notes/`) and the exam-questions corpus
  (`SME-ExamQuestion/`, scraped 2026-09-17 under the same attestation —
  questions, mark schemes, and question images).
- Pearson (Edexcel) examination material is **unaffected** — the attestation
  covers Save My Exams material only; the ADR-013 license-wall posture stays
  for exam-board content.
- Operator follow-ups (not blockers): retain the written permission /
  sponsorship agreement on file; decide whether to surface a sponsor credit
  ("Revision notes in partnership with Save My Exams") in the product UI.
- Provenance (front-matter source URLs, SHA-256 ledgers) remains in force
  unchanged; takedown / correction handling remains as stated above.

## Amendment 2026-10-17 — Cambridge (CAIE) extension of the SME corpora (operator directive)

By operator directive recorded 2026-10-17 (zai-web session, gateway trace
`1a1472e1880cc011`: "similarly download Cambridge ones as well. Push it in
the repo"), the SME-attested corpora are extended to the Cambridge
International lanes of savemyexams.com: 44 lanes across `a-level/cie`
(full A Level incl. AS+A2; maths 20 as 5 unit lanes), `as/cie` (only where
a-level has no counterpart), and `igcse/cie` (incl. tier/strand variant
lanes mirroring the Edexcel lane model). The same rights holder (Save My
Exams Ltd) publishes this material on the same public site; the extension
is covered by the same attestation recorded above (operator: Nawaf Al
Hussain Khondokar).

- Acquisition channel: SME's own public site and sitemaps only — no
  aggregator hosts, no Pearson DAM, no access-control circumvention of any
  kind. The lane-level acquisition-track closure recorded 2026-09 (basis:
  unlicensed Pearson-copyright redistribution via aggregator/evasion
  channels) remains in force and untouched.
- Scrape tooling: `scripts/sme_cambridge_courses.py` (44-lane registry,
  scope decisions recorded in-file), `scripts/sme_cambridge_examq_scrape.py`,
  the existing registry-driven notes/flashcards scrapers, and
  `scripts/sme_cambridge_verify.py` (gates; verdict at
  `graph/reports/SME_CAMBRIDGE_VERIFICATION.json`).
- Courses with no SME content of a given kind are recorded honestly in the
  registries (`missing_on_sme` / `no_topic_questions_on_sme`), never
  synthesized. SME spec-point ids are preserved verbatim; resolution to
  official CAIE codes is NOT asserted anywhere.
- Pearson (Edexcel) examination material remains unaffected (ADR-013
  license-wall posture); the existing Edexcel corpora are byte-untouched
  by this extension (registry manifests/READMEs rebuilt additively).
- Provenance and takedown handling remain as stated above.

## Related internal policy

- `SyllabAI/syllabai` → ADR-013 (license wall), `PROJECT_CONTEXT.md` (Approved technology direction — license wall), and the corpus charter in `syllabai-pastpapers` (README).

## Cambridge International syllabus documents (T-SPECS-CIE-1, 2026-10-18)

The `Official-Specifications/cie-*` qualification directories hold official Cambridge International Education syllabus PDFs (IGCSE and AS/A Level editions matching the SME course lanes), downloaded from cambridgeinternational.org with the source URL, edition window and SHA-1 identity recorded per qualification (`spec.json` + `manifest.json`). Syllabus documents are © Cambridge University Press & Assessment; they are publicly provided documents used under the same non-commercial educational course-project posture as the rest of this notice, and no ownership is claimed. Redistribution beyond the pilot is not authorized by this paragraph. Takedown / correction requests: as above — affected material will be removed promptly.

## Amendment 2026-10-22 — Pearson Student Book hosting (operator attestation; the F-BOOK-0001 amendment of record)

The operator (Nawaf Al Hussain Khondokar) attests that he holds the rights to
host the Pearson Edexcel International GCSE (9-1) Chemistry Student Book for
the SyllabAI product. Recorded verbatim in-session at the package intake
run-001, 2026-10-18 (gateway trace `1a14f8bf97b983f1`): **"I have rights on
hosting"** (the intake covering the student book and the RAG corpora; the
assertion of record also carried in the consuming repository's
`packages/contracts/src/books.ts` header since T-MIG-133).

Subject of the attestation — the student-book PDF of record:

- `books/pearson-edexcel/international-gcse/chemistry/4ch1/student-book.pdf`
  (383 pages; sha256 `d48020e0cc0b5545b330bb59b242472198210e424525e4381cd5d2a58a58cc04`,
  pinned at T-BOOK-010 S0 in the consuming repository's `books/4ch1/meta/book.yaml`).

Consequences of this amendment:

- Hosting this student-book PDF and its page-exact derived surfaces (the
  chapter slices and the page-anchored interactive rail of the SyllabAI
  interactive-books pilot — the rail-over-spine posture of
  `ADR-BOOK-0001` in SyllabAI/syllabai-v2) inside SyllabAI surfaces
  (including this repository and the authenticated product) is covered by
  the operator's attestation above.
- Scope is the student book (textbook) only. Pearson (Edexcel)
  **examination** material remains unaffected — the ADR-013 license-wall
  posture stays for exam-board examination content; the SME amendments
  above are likewise untouched in their subject matter.
- The non-commercial educational pilot posture, provenance law and
  takedown handling stated above remain in force unchanged.
- Bookkeeping of record: this amendment discharges **F-BOOK-0001**
  (SyllabAI/syllabai-v2 → `books/4ch1/qa/findings.jsonl`), the release gate
  of ADR-BOOK-0001 §4 ("no full-book launch (Phase C flip) until
  `LICENSE-DATA.md` carries a Student-Book amendment").
- Operator follow-ups (not blockers): retain the underlying permission
  documentation on file.

## Amendment 2026-10-23 — Underground Mathematics text import (operator attestation; the T-UGM-IMPORT-1 amendment of record)

The operator attests that permission to ship the downloaded Underground
Mathematics text into SyllabAI is granted. Recorded verbatim in-session,
2026-10-23 (zai-web session, gateway traces `1a16492971f299a1` /
`1a164932141f882d`): **"Continue and downloaded text can ship into SyllabAI.
We have permission."** The preceding directive of the same session ("don't
need links to UGM. You already downloaded the resources, create them in
syllabai") established the direct-import intent; this amendment supplies the
licence position.

Subject of the attestation — the **text** of Underground Mathematics
resources captured 2026-10-22 by the research track's full-site crawl and
imported as this repository's `UGM-Resources/` corpus family (first lane
`UGM-Resources/pure-1-quadratics/`, 59 resources, task `T-UGM-IMPORT-1`;
per-file provenance in front-matter + `UGM-Resources/MANIFEST.json` SHA-256
identity). Underground Mathematics content is © University of Cambridge
(Cambridge Mathematics); sourced exam questions are © UCLES — rights and
attribution are unchanged and stated per file.

Consequences of this amendment:

- Serving/importing the captured UGM **text** inside SyllabAI surfaces
  (including this repository and the authenticated product) is covered by
  the operator's attestation above. This supersedes the prior position
  ("UGM text bodies stay research-repo-only") recorded in ADR-UGM-0001 and
  in the `UGM-Enrichment/` README (syllabai-resources#55), which anticipated
  precisely this landing path: text of record arrives as its own
  LICENSE-DATA.md amendment first.
- **Scope is the downloaded text.** Images, PDFs (e.g. GeoGebra
  constructions, component PDFs) and interactive embeds are NOT part of the
  import and are NOT covered by this paragraph; they are recorded as
  reference paths in front-matter (`assets:` / `interactive:`) and remain
  unfetched pending a separate decision.
- The non-commercial educational pilot posture, provenance law (source
  URLs, capture dates, SHA-256 manifest) and takedown / correction handling
  remain in force unchanged: takedown / correction requests → open an issue
  on this repository or contact the repository owner via GitHub; affected
  material will be removed promptly.
- Spec-point mappings carried by the corpus (`spec_map`) are agent-generated
  alignment candidates (`SUGGESTED`, AGENT.md rule 2); they are separate from
  the rights position and ride the normal review/promotion gate.
- Operator follow-ups (not blockers): retain the underlying permission
  documentation on file; decide the product-side attribution presentation
  (UGM's own acknowledgement strings are preserved in the corpus metadata).

## Amendment 2026-10-24 — Underground Mathematics static figures (operator attestation; the T-UGM-ASSETS-1 amendment of record)

The operator attests that the Underground Mathematics **static figures** (diagrams and images) may be
downloaded and shipped into SyllabAI alongside the text corpus. Recorded verbatim in-session,
2026-10-24 (zai-web session, gateway trace `1a16dc6786415249`): **"Did you download all the
figures/diagrams from UGM and saved it in github? I want the syllabai frontend to use those images
then. Currently not showing any images, just links to ugm"**. This is the "separate decision" that
Amendment 2026-10-23 anticipated for the image plane; that amendment's text-scope terms are otherwise
carried forward unchanged.

Subject of the attestation — the **static figure binaries** (PNG/SVG) referenced by the served corpus
sections, captured 2026-10-22 by the research track's full-site crawl and imported by
`T-UGM-ASSETS-1` as this repository's `UGM-Assets/` tree (976 files, 37.7 MB; per-file
SHA-256 identity + source URL in `UGM-Assets/MANIFEST.json`; figure→resource→section mapping in
`UGM-Resources/figures-map.json`). Underground Mathematics content is © University of Cambridge
(Cambridge Mathematics); sourced exam questions are © UCLES — rights and attribution are unchanged.

Consequences of this amendment:

- Committing and serving the captured UGM **static figures** inside SyllabAI surfaces (including this
  repository and the authenticated product) is covered by the operator's attestation above.
- **Scope remains static images only.** GeoGebra interactive embeds, printable/component PDFs, site
  chrome (logos/CSS/JS/fonts) and assets referenced only by variant pages outside the corpus sections
  are NOT part of this import and remain excluded.
- The non-commercial educational pilot posture, provenance law (source URLs, capture dates, SHA-256
  manifests) and takedown / correction handling remain in force unchanged: takedown / correction
  requests → open an issue on this repository or contact the repository owner via GitHub; affected
  material will be removed promptly.
