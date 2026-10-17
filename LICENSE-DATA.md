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
