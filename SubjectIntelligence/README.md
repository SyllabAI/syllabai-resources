# SubjectIntelligence — SyllabAI Subject Intelligence Build (SIB)

**Created:** 2026-10-25 (operator directive: "create a folder in syllabai-resources called
SubjectIntelligence. There create docs/copy existing docs. Create the pipeline.")
**Protocol:** SIB v1 — `docs/SUBJECT_INTELLIGENCE_BUILD_V1.md` (PROPOSED of record,
master-repo landed 2026-10-01). **Validator:** `SyllabAI/syllabai@tools/sib/` (IMPLEMENTED),
canonical, not vendored here — see `docs/PIPELINE.md` §2.

## What this is

The home of the Subject Intelligence research libraries: per-subject, NotebookLM-generated
research corpora that the Subject Tutor retrieves as **evidence**, subordinate to canonical
truth. Protocol §7 boundary is binding: research artifacts never mutate the authoritative KG,
mastery, SpecificationPoints, validated assessment identity, or learner evidence.

## Layout

```
SubjectIntelligence/
├── README.md                     this charter
├── docs/
│   ├── SUBJECT_INTELLIGENCE_BUILD_V1.md    protocol of record (copy, pinned master@aa32db1413ea)
│   ├── SIB_ARTIFACT_SCHEMA_V1.md           artifact schema + lifecycle (copy)
│   ├── SIB_NOTEBOOKLM_PROMPTS_V1.md        NotebookLM prompts (copy)
│   ├── SIB_VALIDATOR_IMPLEMENTATION_V1.md  validator implementation record (copy)
│   ├── SOURCE_REQUIREMENTS_4CH1.md         operator requirements of record (2026-10-25)
│   ├── SOURCE_INVENTORY_2026-10-25.md      repo inventory findings (the requirements' key next step)
│   └── PIPELINE.md                          how to run the pipeline end-to-end
└── CHEMISTRY_4CH1/               first subject library (scaffold validated)
    ├── manifest.yaml             95-artifact applicability map (88 REQUIRED / 7 OPTIONAL)
    ├── source_manifest.yaml      12 inventoried sources, classified + identified
    ├── curriculum_registry.yaml  182 pinned spec-point codes for anchor resolution
    └── artifacts/ qa-reports/ staged/ published/ chunks/     (empty work dirs)
```

## Law of this directory

1. **The docs/ copies are pinned snapshots**, not live surfaces: the protocol/schema/prompts of
   record live in `SyllabAI/syllabai@docs/research/`, the validator in `tools/sib/`. Any
   upstream change is re-copied here with a new pin noted in the file header + worklog.
2. **Sources stay in their canonical repos.** The library points at them
   (`source_manifest.yaml`); nothing is duplicated for duplication's sake.
3. **The validator owns every lifecycle transition.** Landing artifacts self-declaring
   `QA_PASSED`/`STAGED`/`PUBLISHED` are rejected; staging/publishing are explicit, operator-ordered.
4. **Gaps are disclosed, never fabricated.** Absent optional sources (examiner reports, 4CH0
   legacy, teaching guide, standalone data sheet) live as `source_gaps` in both
   `source_manifest.yaml` and `manifest.yaml` until acquired.
5. **Canonical planes are read-only to this pipeline** (`graph/igcse-chemistry/`,
   `spec-links/`) — AGENT.md rules 1/3/5 and protocol §7, enforced by the validator's
   path confinement.

## Current state

- Scaffold + manifests + registry landed and validated (shape CLEAN; completeness honestly
  0/88 REQUIRED until generation starts — the gate is the scoreboard).
- Corpus verdict: assessment + explanation evidence strong (54 official papers / 16 sessions,
  validated book parse, validated graph + mappings); examiner reports and 4CH0 legacy absent
  and disclosed.
- Next runs (operator-ordered): BL-003 notebook provisioning → CUR-01..CUR-08 first wave.
