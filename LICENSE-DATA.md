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

## Related internal policy

- `SyllabAI/syllabai` → ADR-013 (license wall), `PROJECT_CONTEXT.md` (Approved technology direction — license wall), and the corpus charter in `syllabai-pastpapers` (README).
