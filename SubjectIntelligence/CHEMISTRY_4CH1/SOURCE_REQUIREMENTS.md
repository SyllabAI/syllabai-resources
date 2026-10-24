# Source Requirements — 4CH1 Subject Intelligence Build

**Status:** OF RECORD (operator directive, 2026-10-25 — "For SIB, there are requirements. I want you to create a folder in syllabai-resources folder. called SubjectIntelligence. There create docs/copy existing docs. Create the pipeline.")
**Provenance note:** requirements body below is the operator-provided assessment (ChatGPT-drafted), filed verbatim in substance. The inline marketplace/image proxy links from the chat export were dead weight and are stripped; their role (indicative source types) is preserved in the tables. The key-next-step instruction was executed the same day — see `INVENTORY_2026-10-25.md` (same directory). Moved here 2026-10-25 (SIB-LIBRARY-003): course-specific docs live inside the course library per the all-courses architecture; the generalized template is `../docs/SOURCE_REQUIREMENTS_TEMPLATE.md`.

---

For SyllabAI's 4CH1 Subject Intelligence Build, Z.ai needs more than the student book, official specification, and past papers. It needs enough evidence to understand what students must learn, how the subject is taught, how examiners assess it, where students struggle, and how learning should be supported.

The source corpus is organized into required, strongly recommended, and optional materials. The agent inventories what already exists in the repositories before asking the operator to collect anything else.

## 1. Core sources

| Source | Priority | What it is used for |
| --- | --- | --- |
| Official specification | Required | Curriculum boundaries, specification points, command words, practical requirements and assessment objectives |
| Current student book / textbook | Required if available | Detailed explanations, worked examples, terminology, diagrams and topic sequencing |
| Official question papers (QP) | Required | Question archetypes, contexts, topic combinations, exam demands and recurring patterns |
| Official mark schemes (MS) | Required | Required answer elements, acceptable alternatives, partial credit and mark-loss patterns |
| Official examiner reports | Strongly recommended | Common errors, misconceptions, weak answers, examiner expectations and advice |
| SyllabAI's validated curriculum and SpecificationPoint data | Required | Stable curriculum anchors and consistent mapping to SyllabAI's authoritative curriculum model |

For the exam corpus, include all available relevant sessions, not just a few recent papers. Keep question papers and mark schemes identifiable by paper, session, variant and document type.

## 2. Other documents Z.ai should have

A. **Examiner reports** — High priority. Reports covering multiple exam sessions help distinguish recurring student difficulties from isolated mistakes. Especially valuable for `MIS`, `MS`, `EXM`, `PED` and `TUT` artifacts.

B. **Practical and experimental materials** — High priority for Chemistry. Practical guidance, required practical statements, experimental methods, apparatus, safety guidance, observations, results, calculations, limitations and sources of experimental error. These support `PRA`, `PRO`, `EXP` and `MIS`.

C. **SyllabAI's SME revision notes** — Available source to prioritize. The 112 SME revision notes already in the resource corpus are useful supporting material for explanations, pitfalls, examples and curriculum-linked teaching. Preserve their existing SpecificationPoint mappings and validation status.

D. **Formula sheets, data tables and reference material** — Include the official periodic table, any permitted data sheet, formula/reference tables, relevant constants and other examination resources. Record which materials apply to which specification and examination sessions.

E. **Glossaries, diagrams and worked examples** — Help build terminology, concept distinctions, mental models, explanation alternatives and calculation guidance. Include the original source context and page or section references where available.

F. **Legacy specification and assessment materials** — Include the older 4CH0 specification, textbooks and papers when historical comparison is useful. These support the `HIS` family and can reveal persistent concepts or changes in assessment, but must remain explicitly historical.

## 3. Additional sources that can improve the library

| Material | Why it matters | Priority |
| --- | --- | --- |
| Official teaching guide or scheme of work | Intended topic sequencing and teaching emphasis | Recommended |
| Official subject support materials | Clarifications and guidance not fully covered by the specification | Recommended |
| Official command-word definitions and assessment-objective guidance | Better interpretation of what questions demand | Recommended if separately published |
| Validated concept/prerequisite graph | Helps ground relationships and distinguish known relationships from research hypotheses | Use existing SyllabAI data |
| Question-to-SpecificationPoint mappings | Enables assessment coverage and question archetype analysis | Use validated mappings first |
| Anonymized learner responses and marking outcomes | Helps investigate real learner errors and diagnostic signals | Later phase; governed learner evidence only |
| Existing tutor conversations and feedback | May reveal recurring questions and explanation needs | Optional; use extracted, provenance-bearing evidence |
| Subject-specific external research | Can enrich explanations where official sources are insufficient | Optional; independently label and validate |

## 4. What the source corpus should look like

For 4CH1, build a source manifest **before** generating any SIB artifacts:

```
research/sib/CHEMISTRY_4CH1/
├── manifest.yaml
├── source_manifest.yaml
├── curriculum_registry.yaml
├── artifacts/
├── qa-reports/
├── staged/
├── published/
└── chunks/
```

The actual source files remain in their existing canonical repositories. The manifest points to those sources using stable identifiers, repository paths, versions, session metadata and checksums where available. Nothing is copied into a new directory just for the sake of duplication.

The source manifest classifies each source as:

- `CURRENT — AUTHORITATIVE`
- `CURRENT — ASSESSMENT EVIDENCE`
- `SUPPLEMENTARY`
- `LEGACY — HISTORICAL`
- `RESEARCH / INFERRED`, where applicable

For each source, capture its type, issuing body, specification, version or date, coverage, provenance and known limitations.

## 5. Recommended minimum corpus for 4CH1

Before starting the full 95-artifact build, check that these six groups are accessible:

1. Official 4CH1 specification and validated SpecificationPoint registry.
2. Current student book and any relevant official teaching/support material.
3. Complete available 4CH1 QP/MS corpus, with paper and session identities preserved.
4. Official examiner reports for the available sessions.
5. SyllabAI's validated SME revision notes and existing question-to-specification mappings.
6. Practical guidance, official data sheets and other examination reference materials relevant to 4CH1.

Then inventory 4CH0 as a separate legacy group for longitudinal analysis.

**Limitation law:** the absence of an optional source is not a blocker. If examiner reports or a teaching guide are unavailable, record the gap and proceed where the available evidence is sufficient. Never fabricate missing evidence to make an artifact appear complete.

**Key next step:** inspect the actual repositories and report which sources are already accessible. That inventory determines what needs collecting, rather than making the operator manually gather material SyllabAI already holds. *(Executed 2026-10-25 → `INVENTORY_2026-10-25.md`; live status lives in `source_manifest.yaml`, same directory.)*
