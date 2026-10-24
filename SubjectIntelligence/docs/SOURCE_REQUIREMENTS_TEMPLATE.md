# Source Requirements — SIB Course Libraries (general template)

**Status:** OF RECORD (2026-10-25). Generalization of the operator's 4CH1 requirements
(`../CHEMISTRY_4CH1/SOURCE_REQUIREMENTS.md`, the validated filled example) to **every**
course library, per the operator directive that SubjectIntelligence hosts all courses.
Instantiate per course during onboarding (`docs/COURSE_ONBOARDING.md` step 2); keep the
filled per-course version inside the course library directory.

---

For any course's Subject Intelligence Build, the corpus must hold enough evidence to
understand what students must learn, how the subject is taught, how examiners assess it,
where students struggle, and how learning should be supported. The source corpus is
organized into required, strongly recommended, and optional materials. The agent
inventories what already exists in the repositories before asking the operator to
collect anything else.

## 1. Core sources (all courses)

| Source | Priority | What it is used for |
| --- | --- | --- |
| Official specification | Required | Curriculum boundaries, specification points, command words, practical requirements and assessment objectives |
| Current student book / textbook | Required if available | Detailed explanations, worked examples, terminology, diagrams and topic sequencing |
| Official question papers (QP) | Required | Question archetypes, contexts, topic combinations, exam demands and recurring patterns |
| Official mark schemes (MS) | Required | Required answer elements, acceptable alternatives, partial credit and mark-loss patterns |
| Official examiner reports | Strongly recommended | Common errors, misconceptions, weak answers, examiner expectations and advice |
| SyllabAI's validated curriculum and SpecificationPoint data | Required | Stable curriculum anchors and consistent mapping to SyllabAI's authoritative curriculum model |

For the exam corpus, include all available relevant sessions, not just a few recent
papers. Keep question papers and mark schemes identifiable by paper, session, variant
and document type.

## 2. Other document classes

A. **Examiner reports** — High priority. Reports covering multiple exam sessions help
distinguish recurring student difficulties from isolated mistakes. Especially valuable
for `MIS`, `MS`, `EXM`, `PED` and `TUT` artifacts.

B. **Practical and experimental materials** — High priority for the sciences. Practical
guidance, required practical statements, experimental methods, apparatus, safety
guidance, observations, results, calculations, limitations and sources of experimental
error. These support `PRA`, `PRO`, `EXP` and `MIS`. (Non-science courses substitute the
subject's equivalent applied/ Skills material and mark it as such.)

C. **SyllabAI's SME revision notes** — Available source to prioritize. The platform's
SME revision notes for the course are useful supporting material for explanations,
pitfalls, examples and curriculum-linked teaching. Preserve their existing
SpecificationPoint mappings and validation status.

D. **Formula sheets, data tables and reference material** — Official data sheets,
formula/reference tables, set texts, anthologies, case studies or other permitted
examination resources, as the subject demands. Record which materials apply to which
specification and examination sessions.

E. **Glossaries, diagrams and worked examples** — Help build terminology, concept
distinctions, mental models, explanation alternatives and calculation guidance. Include
the original source context and page or section references where available.

F. **Legacy specification and assessment materials** — Where a predecessor specification
exists (e.g. 4CH0 for 4CH1), include its specification, textbooks and papers when
historical comparison is useful. These support the `HIS` family and can reveal
persistent concepts or changes in assessment, but must remain explicitly historical
(`LEGACY — HISTORICAL` classification).

## 3. Additional sources that can improve a library

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

## 4. What each course's source corpus should look like

Build the course's source manifest **before** generating any SIB artifacts:

```
SubjectIntelligence/<SUBJECT>_<SPEC>/
├── manifest.yaml
├── source_manifest.yaml
├── curriculum_registry.yaml
├── artifacts/
├── qa-reports/
├── staged/
├── published/
└── chunks/
```

The actual source files remain in their existing canonical repositories. The manifest
points to those sources using stable identifiers, repository paths, versions, session
metadata and checksums where available. Nothing is copied into a new directory just for
the sake of duplication.

The source manifest classifies each source as:

- `CURRENT — AUTHORITATIVE`
- `CURRENT — ASSESSMENT EVIDENCE`
- `SUPPLEMENTARY`
- `LEGACY — HISTORICAL`
- `RESEARCH / INFERRED`, where applicable

For each source, capture its type, issuing body, specification, version or date,
coverage, provenance and known limitations.

## 5. Recommended minimum corpus (per course) + limitation law

Before starting the full 95-artifact build, check that these six groups are accessible
for the course:

1. Official specification and validated SpecificationPoint registry.
2. Current student book and any relevant official teaching/support material.
3. Complete available QP/MS corpus, with paper and session identities preserved.
4. Official examiner reports for the available sessions.
5. SyllabAI's validated SME revision notes and existing question-to-specification
   mappings.
6. Practical guidance / official data sheets / other examination reference materials
   relevant to the course.

Then inventory any predecessor spec as a separate legacy group for longitudinal
analysis.

**Limitation law:** the absence of an optional source is not a blocker. If examiner
reports or a teaching guide are unavailable, record the gap and proceed where the
available evidence is sufficient. Never fabricate missing evidence to make an artifact
appear complete.
