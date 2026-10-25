# SubjectIntelligence — SyllabAI Subject Intelligence library (ALL courses)

**Created:** 2026-10-25 (operator directive: "create a folder in syllabai-resources called
SubjectIntelligence. There create docs/copy existing docs. Create the pipeline.")
**Scope directive:** 2026-10-25 — *"SubjectIntelligence will host all courses not just
4ch1."* This directory is the corpus warehouse for **every** course's Subject Intelligence
library; 4CH1 is the first onboarded course, not the template's boundary.
**Generation (2026-10-25 SIB-GEN, trace `1a1726b6684c4055`):** the provider-neutral
Z.ai agent pipeline of record — schema V2 provenance (`docs/SIB_ARTIFACT_SCHEMA_V2.md`),
prompt pack `docs/SIB_ZAI_PROMPTS_V1.md`, source resolver + evidence packs + run
records (`pipeline/`). NotebookLM is retained as an OPTIONAL-HIS research path
(`docs/SIB_NOTEBOOKLM_PROMPTS_V1.md`). **Protocol:** SIB v1 —
`docs/SUBJECT_INTELLIGENCE_BUILD_V1.md`. **Validator:** `SyllabAI/syllabai@tools/sib/`
(IMPLEMENTED), canonical, not vendored here — see `docs/PIPELINE.md` §2.

## What this is

The home of the Subject Intelligence research libraries: one library per qualification,
Z.ai-agent-generated (evidence-pack grounded) research corpora that the Subject Tutor
retrieves as **evidence**, subordinate to canonical truth. Protocol §7 boundary is
binding: research artifacts never mutate the authoritative KG, mastery,
SpecificationPoints, validated assessment identity, or learner evidence.

## Course catalog

- **Registry of record:** `COURSES.yaml` — generated from
  `Official-Specifications/manifest.json` (56 qualification documents covering 93/93 SME
  platform courses, missing: none), plus explicit legacy declarations (4CH0).
- **Library unit:** one SI library per qualification (spec *document*), not per platform
  course slug — modular/linear variants with distinct spec PDFs are distinct libraries
  (verified: igcse-chemistry Issue 3 sha1 `3ad641b7…` vs igcse-chemistry-modular Issue 2
  sha1 `9df406d3…`); a genuinely shared document is served by one library.
- **Naming contract:** `<SUBJECT>_<SPEC>` — `CHEMISTRY_4CH1` onboarded; `BIOLOGY_4BI1`,
  `MATHS_4MA1`, … follow the same contract; legacy specs keep their own code
  (`CHEMISTRY_4CH0`) and are classified `LEGACY — HISTORICAL` throughout.
- **Roster:** 1 ONBOARDED (`CHEMISTRY_4CH1`), 1 legacy declared (corpus PRESENT in
  canonical repos, library not scaffolded), 55 PLANNED. Planned libraries are never
  scaffolded speculatively — `COURSES.yaml` is their home until onboarding is
  operator-ordered (`docs/COURSE_ONBOARDING.md`).

## Layout

```
SubjectIntelligence/
├── README.md                     this charter
├── COURSES.yaml                  course registry of record (onboarded / legacy / planned)
├── WORKLOG.md                    lane worklog (append-only)
├── docs/                         shared, course-agnostic (pinned snapshots of master of record):
│   ├── SUBJECT_INTELLIGENCE_BUILD_V1.md    protocol of record (amended SIB-GEN 2026-10-25)
│   ├── SIB_ARTIFACT_SCHEMA_V1.md           artifact schema + lifecycle (V1: historical shapes)
│   ├── SIB_ARTIFACT_SCHEMA_V2.md           provider-neutral provenance schema (SIB-GEN)
│   ├── SIB_ZAI_PROMPTS_V1.md               Z.ai agent prompt pack of record (SIB-GEN)
│   ├── SIB_NOTEBOOKLM_PROMPTS_V1.md        NotebookLM prompts (OPTIONAL-HIS reference)
│   ├── SIB_VALIDATOR_IMPLEMENTATION_V1.md  validator implementation record (+ V2 appendix)
│   ├── SOURCE_REQUIREMENTS_TEMPLATE.md     generalized 6-group source requirements (all courses)
│   ├── COURSE_ONBOARDING.md                how to onboard ANY course (instantiator + gates)
│   └── PIPELINE.md                          per-course operating procedure (ALL courses)
├── pipeline/
│   ├── new_course.py             fail-closed instantiator: scaffold ANY course from templates
│   ├── source_resolver.py        resolve source_manifest ids vs canonical repos (fail-closed)
│   ├── evidence_pack.py          bounded identity-preserving evidence pack per artifact
│   ├── run_manifest.py           run-record writer (inputs/outputs/generator pins/hashes)
│   ├── generate_artifact.py      emit/ingest the Z.ai agent task for one artifact
│   ├── run_build.py              run orchestrator (preflight → pack → generate → land)
│   ├── tests/                    fixture-driven suite (no network, no model calls)
│   └── templates/course/         manifest / source_manifest / curriculum_registry /
│                                 evidence_policy templates
└── CHEMISTRY_4CH1/               first onboarded course library (validated worked example)
    ├── manifest.yaml             95-artifact applicability map (88 REQUIRED / 7 OPTIONAL)
    ├── source_manifest.yaml      17 inventoried sources, classified + identified (v1.2)
    ├── curriculum_registry.yaml  182 pinned spec-point codes for anchor resolution
    ├── evidence_policy.yaml      per-family evidence law of record (SIB-GEN)
    ├── SOURCE_REQUIREMENTS.md    operator requirements of record for this course
    ├── INVENTORY_2026-10-25.md   (+ ADDENDUM) course inventory findings
    ├── runs/                     run records + evidence packs + receipts (append-only)
    └── artifacts/ qa-reports/ staged/ published/ chunks/     (work dirs)
```

## Law of this directory

1. **The docs/ copies are pinned snapshots**, not live surfaces: the protocol/schema/prompts
   of record live in `SyllabAI/syllabai@docs/research/`, the validator in `tools/sib/`. Any
   upstream change is re-copied here with a new pin noted in the file header + worklog.
2. **Sources stay in their canonical repos.** Libraries point at them
   (`source_manifest.yaml`); nothing is duplicated for duplication's sake.
3. **The validator owns every lifecycle transition.** Landing artifacts self-declaring
   `QA_PASSED`/`STAGED`/`PUBLISHED` are rejected; staging/publishing are explicit,
   operator-ordered.
4. **Gaps are disclosed, never fabricated** — for every course. Absent optional sources
   live as `source_gaps` in the library's `source_manifest.yaml` and `manifest.yaml`
   until acquired.
5. **Canonical planes are read-only to this pipeline** (`graph/`, `spec-links/`, …) —
   AGENT.md rules 1/3/5 and protocol §7, enforced by the validator's path confinement.
6. **All-courses discipline:** new libraries are scaffolded only by
   `pipeline/new_course.py` (fail-closed, template-driven, validator-certified), only on
   operator order; the course roster lives in `COURSES.yaml`, not in improvisation.
7. **Generation is receipted (SIB-GEN law).** Every generation run opens a run record
   under `<LIBRARY>/runs/` (inputs: source revisions + evidence-pack hash; outputs:
   artifact hashes + per-artifact outcomes; generator provider/model + prompt-pack
   version). Artifact front matter carries schema V2 provenance pinned from the run
   record — never invented. Sources stay in canonical repos: SIB resolves and reads
   them; it does not copy the corpus. Skips are recorded; re-runs after input changes
   are explicit; published artifacts are never silently overwritten.

## Current state

- All-courses architecture landed 2026-10-25 (SIB-LIBRARY-003): `COURSES.yaml` registry
  (56-qualification catalog + legacy declaration), template pack + fail-closed
  instantiator **validator-certified** (test instantiation reproduced the validated
  CHEMISTRY_4CH1 shape exactly: 95 rows / 88 REQUIRED / 7 OPTIONAL / 0 shape issues),
  generalized requirements + onboarding + pipeline docs; 4CH1-specific docs moved into
  the course library.
- Corpus verdict (2026-10-25, BL-001/002/**005** executed): assessment + explanation evidence
  strong for the onboarded course (54 official papers / 16 sessions, validated book
  parse, validated graph + mappings); **examiner reports ACQUIRED** (24 official 4CH1 ERs
  over 8 sessions + 34 legacy 4CH0 ERs over 13 sessions — Pearson's own CDN,
  `SRC-ER-4CH1` / `SRC-ER-4CH0-LEGACY`); **teaching-and-learning corpus ACQUIRED** (30
  official docs incl. scheme of work, teaching guides, 211pp core practicals guide,
  command words, exemplars, SAMs — `SRC-TL-4CH1` / `SRC-SAMS-4CH1`); **4CH0 legacy corpus
  PRESENT** (complete QP/MS + official spec docs, `SRC-LEGACY-SPEC-4CH0`) — EXM evidence
  real, HIS family unlocked, **six-groups scoreboard 5 PRESENT + 1 PARTIAL** (ER group:
  residual sessions without a public ER are publishing gaps, disclosed, never fabricated —
  wave report: `syllabai-pastpapers@docs/ER-ACQUISITION-2026-10-25.md`; T&L addendum:
  `CHEMISTRY_4CH1/INVENTORY_ADDENDUM_2026-10-25-TL.md`).
- Generation pipeline landed 2026-10-25 (SIB-GEN, trace `1a1726b6684c4055`):
  provider-neutral provenance (schema V2 + validator V2 in `SyllabAI/syllabai@tools/sib`,
  suite 137/137), Z.ai prompt pack, source resolver + evidence-pack + run-record
  pipeline with fixture tests, `CHEMISTRY_4CH1/evidence_policy.yaml` family law,
  `runs/` receipts; NotebookLM demoted to OPTIONAL-HIS (docs re-copied from master of
  record per law 1).
- Next runs (operator-ordered): BL-007 pilot wave — CUR-01 + MIS-01 through the new
  pipeline (citation resolution, source coverage, current/legacy separation,
  educational accuracy checked before scaling) → then the full CUR-01..CUR-08 wave
  (BL-004); subsequent course onboarding via `docs/COURSE_ONBOARDING.md`.
