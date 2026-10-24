# SIB Pipeline — per-course operating procedure (ALL courses)

**Status:** OPERATIONAL (2026-10-25; generalized from the validated CHEMISTRY_4CH1
single-course pipeline per the operator directive that SubjectIntelligence hosts **all
courses**, not just 4CH1).
**Applies:** `SUBJECT_INTELLIGENCE_BUILD_V1.md` (protocol) + `SIB_ARTIFACT_SCHEMA_V1.md`
(schema), both copied in this `docs/` directory of record.
**Onboarding a new course:** `docs/COURSE_ONBOARDING.md` (scaffold instantiator
`pipeline/new_course.py`, inventory-first sweep, registry pin, applicability review,
validator gate). **Worked example of record:** `CHEMISTRY_4CH1/`.

## 0. Roles and boundaries (every course)

| Role | Who | Writes |
|---|---|---|
| Library scaffold, manifests, registry | agent (onboarding lane) | `pipeline/new_course.py` → `<LIBRARY>/{manifest.yaml, source_manifest.yaml, curriculum_registry.yaml}` |
| Artifact generation | NotebookLM / Gemini notebook `<SPEC>-SIB-NOTEBOOK-001` (per `SIB_NOTEBOOKLM_PROMPTS_V1.md`) | `<LIBRARY>/artifacts/` (drops, status GENERATED) |
| QA, staging, publication, chunking | the validator of record, operator-ordered | `<LIBRARY>/{qa-reports/, staged/, published/, chunks/}` |
| Canonical truth (KG, mastery, spec points, assessment identity) | SyllabAI core planes | **never written by this pipeline** |

The pipeline writes only inside library roots. All writes are path-confined by the
validator (`SIB-ING-001`); the library API exposes no canonical-write surface at all.

## 1. Library layout (the all-courses tree)

```
SubjectIntelligence/
├── README.md                              all-courses charter + law
├── COURSES.yaml                           registry of record (onboarded / legacy / planned)
├── WORKLOG.md                             lane worklog (append-only)
├── docs/                                  shared, course-agnostic protocol copies + procedures
├── pipeline/
│   ├── new_course.py                      instantiator (scaffold ANY course, fail-closed)
│   └── templates/course/                  manifest / source_manifest / curriculum_registry templates
└── <SUBJECT>_<SPEC>/                      one library per qualification, e.g.
    ├── manifest.yaml                      95-row applicability map (subject-specific)
    ├── source_manifest.yaml               classified sources + gaps (inventory-first)
    ├── curriculum_registry.yaml           pinned spec-point codes (anchor resolution)
    ├── artifacts/ qa-reports/ staged/ published/ chunks/     (work dirs)
    └── (course-specific docs: SOURCE_REQUIREMENTS, inventory findings)
```

Onboarded today: `CHEMISTRY_4CH1/` (validated precedent). Next libraries scaffold only
on operator order — `COURSES.yaml` holds the 56-qualification catalog (55 PLANNED) plus
the declared 4CH0 legacy corpus.

## 2. Validator of record (canonical location)

The validator is **`SyllabAI/syllabai@tools/sib/`** (Python, self-contained — vendored
`yamlmini`, no third-party deps). It is deliberately NOT copied here: one implementation,
no drift. Pin it by commit at run time:

```bash
# fetch once per run (pin the sha of record; aa32db1413ea validated this pipeline)
git clone --depth 1 --filter=blob:none https://github.com/SyllabAI/syllabai.git /tmp/sib_master
# CLI surface
python3 -m tools.sib.cli --help            # validate-artifact | validate-manifest | qa | stage | publish | chunks | report
```

## 3. Operating procedure (per course)

1. **Provision the notebook**: create NotebookLM notebook `<SPEC>-SIB-NOTEBOOK-001`;
   upload the sources listed `CURRENT — AUTHORITATIVE` / `CURRENT — ASSESSMENT EVIDENCE`
   in the library's `source_manifest.yaml`; label current vs legacy per protocol §2.
2. **Generate pass 1–2** (protocol §4 order): corpus orientation, then `CUR-01..CUR-08`.
   Drop outputs into `<LIBRARY>/artifacts/` with the canonical filename
   `<SUBJECT>_<SPEC>_<ARTIFACT-ID>_<SLUG>.md` (schema §1; slugs = taxonomy defaults) and
   the 15-field front matter (schema §2), `status: GENERATED`, `generated_by: notebooklm`.
3. **QA**: `python3 -m tools.sib.cli qa <LIBRARY> <artifact-id>` — writes the
   deterministic `qa-reports/<ARTIFACT-ID>.qa.json`. Incomplete provenance fails QA with
   a machine-readable reason; the validator never invents source identifiers.
4. **Stage**: `python3 -m tools.sib.cli stage <LIBRARY> <artifact-id>` (operator-ordered).
5. **Publish**: `python3 -m tools.sib.cli publish <LIBRARY> <artifact-id>` (operator-ordered).
6. **Chunk**: `python3 -m tools.sib.cli chunks <LIBRARY> <artifact-id>` for the
   retrieval-side JSONL.
7. **Report**: `python3 -m tools.sib.cli report <LIBRARY>` — completion metrics per
   protocol §9.

## 4. Grounding law for generation (per course)

- Curriculum claims: the course's `SRC-SPEC-*` wording + `SRC-GRAPH-*` anchors (registry
  pin `curriculum_registry.yaml`). Anchor tokens use the official curriculum codes of
  the course's board; resolution INFO/WARNING per `SIB-ANCH-*`.
- Assessment claims: the course's `SRC-QPMS-*` (paper/session identity preserved).
  Topic-grain banks (`SRC-SME-EXAMQ-*`, `SRC-PMT-*`) are supplementary texture, never
  official identity.
- Explanation/pedagogy texture: the course's `SRC-BOOK-*` chunks, `SRC-SME-NOTES-*`
  (preserving their mappings/validation state), external notes only after overlap
  adjudication.
- **Forbidden evidence substitutions (all courses):** no examiner sentiment synthesized
  from mark schemes; no legacy claims without legacy sources; no artifact grounding on
  un-adjudicated root book copies; nothing invented to fill any gap (requirements
  template §5 limitation law). Worked example with concrete source ids:
  `CHEMISTRY_4CH1/source_manifest.yaml` + `docs/PIPELINE.md` history (git).

## 5. Gate semantics (per course)

`validate-manifest` against `tools/sib@aa32db1413ea`:

- **Shape: CLEAN** required — taxonomy-valid rows, correct applicability counts, gaps +
  backlog surfaced as `SIB-MANI-011` WARN / `SIB-MANI-012` INFO (designed disclosures,
  not defects).
- **Completeness:** REQUIRED artifacts missing from the landing zone report
  `SIB-MANI-007` ERROR — the truthful empty-library state for a fresh scaffold (88 such
  rows on a default applicability map); the count is the completion scoreboard, and
  `report` is its metric view. Re-run after each generation wave; the gate is the
  scoreboard.
- Certification of record: the `pipeline/new_course.py` test instantiation
  (`BIOLOGY_4BI1`, 2026-10-25) reproduced the validated CHEMISTRY_4CH1 shape exactly
  (95 rows / 88 REQUIRED / 7 OPTIONAL / 0 shape issues).

## 6. Change law

Manifest edits (applicability flips, gap additions) are operator-ordered and regenerate
via the generator of record rather than hand-editing where possible. New course
libraries are scaffolded only by `pipeline/new_course.py` (never hand-mkdir'd). Every
library state change of record ships with a worklog entry in this repo and, where
material, a receipt.
