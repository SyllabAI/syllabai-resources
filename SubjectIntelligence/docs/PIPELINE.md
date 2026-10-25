# SIB Pipeline — per-course operating procedure (ALL courses)

**Status:** OPERATIONAL (2026-10-25; provider-neutral edition r0 — SIB-GEN program).
Generalized from the validated CHEMISTRY_4CH1 single-course pipeline per the operator
directive that SubjectIntelligence hosts **all courses**, not just 4CH1. The r0
edition removes the single-provider assumption: generation runs are executed by the
**zai_agent** class through the SIB-GEN run pipeline; NotebookLM is a **legacy
provider reference** (`SIB_NOTEBOOKLM_PROMPTS_V1.md`, OPTIONAL-HIS), retained for
historical drops whose v1 provenance stays valid.
**Applies:** `SUBJECT_INTELLIGENCE_BUILD_V1.md` (protocol) + `SIB_ARTIFACT_SCHEMA_V1.md`
(schema) + `SIB_ARTIFACT_SCHEMA_V2.md` (provenance evolution), all copied in this
`docs/` directory of record.
**Onboarding a new course:** `docs/COURSE_ONBOARDING.md` (scaffold instantiator
`pipeline/new_course.py`, inventory-first sweep, registry pin, applicability review,
validator gate). **Worked example of record:** `CHEMISTRY_4CH1/`.

## 0. Roles and boundaries (every course)

| Role | Who | Writes |
|---|---|---|
| Library scaffold, manifests, registry | agent (onboarding lane) | `pipeline/new_course.py` → `<LIBRARY>/{manifest.yaml, source_manifest.yaml, curriculum_registry.yaml}` |
| Artifact generation | the SIB-GEN run pipeline (`pipeline/run_build.py`) executed by the **zai_agent** class; legacy alternative: NotebookLM notebook `<SPEC>-SIB-NOTEBOOK-001` per `SIB_NOTEBOOKLM_PROMPTS_V1.md` | `<LIBRARY>/artifacts/` (drops, status GENERATED, schema v2 provenance) + `<LIBRARY>/runs/` (run records) |
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
│   ├── evidence_policy.yaml               per-family evidence law (machine-readable)
│   ├── source_resolver.py                 resolve + hash-verify the operator source manifest
│   ├── evidence_pack.py                   build bounded, identity-preserving evidence packs
│   ├── run_manifest.py                    run-record model + validation
│   ├── generate_artifact.py               provider-neutral artifact stamping + pre-validation
│   ├── run_build.py                       run orchestrator (preflight → packs → generate → QA → record)
│   └── templates/course/                  manifest / source_manifest / curriculum_registry templates
└── <SUBJECT>_<SPEC>/                      one library per qualification, e.g.
    ├── manifest.yaml                      95-row applicability map (subject-specific)
    ├── source_manifest.yaml               classified sources + gaps (inventory-first)
    ├── curriculum_registry.yaml           pinned spec-point codes (anchor resolution)
    ├── artifacts/ qa-reports/ staged/ published/ chunks/     (work dirs)
    ├── runs/                              SIB-GEN run records (run manifests + receipts)
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
# fetch once per run (pin the sha of record; aa32db1413ea validated this pipeline;
# the schema-v2 provenance one-of lands in the master PR paired with this edition)
git clone --depth 1 --filter=blob:none https://github.com/SyllabAI/syllabai.git /tmp/sib_master
# CLI surface
python3 -m tools.sib.cli --help            # validate-artifact | validate-manifest | qa | stage | publish | chunks | report
```

## 3. Operating procedure (per course)

1. **Run preflight (SIB-GEN)**: resolve the library's `source_manifest.yaml` against
   the canonical repositories (`pipeline/source_resolver.py` — existence + of-record
   checksum verification, fail-closed per source). A generation run may not start on
   unresolved primary evidence; gaps stay disclosed, never filled.
2. **Generate (provider-neutral)**: for each artifact id in the wave (protocol §4
   order), the run pipeline builds a bounded **evidence pack** (`pipeline/evidence_pack.py`,
   family law from `pipeline/evidence_policy.yaml`), the generator authors the artifact
   from that pack alone, and `pipeline/generate_artifact.py` stamps the 15-field
   front matter with schema **v2** provenance (`generated_by: zai_agent`, run id,
   generator block, source revisions), canonical filename, `status: GENERATED`.
   Legacy alternative (unchanged semantics): a NotebookLM drop with v1 notebook-shape
   provenance.
3. **QA**: `python3 -m tools.sib.cli qa <LIBRARY> <artifact-id>` — writes the
   deterministic `qa-reports/<ARTIFACT-ID>.qa.json`. Incomplete provenance fails QA with
   a machine-readable reason; the validator never invents source identifiers. The run
   pipeline additionally runs the **evidence-claim QA** (§5): every citation in the
   artifact must resolve to an entry of its own evidence pack.
4. **Run record**: the run manifest (`pipeline/run_manifest.py`) records evidence-pack
   hashes, artifact hashes, per-artifact outcomes, retries and QA verdicts under
   `<LIBRARY>/runs/<RUN-ID>/` — the receipt of record for the wave (same receipts
   culture as every other SyllabAI lane).
5. **Stage**: `python3 -m tools.sib.cli stage <LIBRARY> <artifact-id>` (operator-ordered).
6. **Publish**: `python3 -m tools.sib.cli publish <LIBRARY> <artifact-id>` (operator-ordered).
7. **Chunk**: `python3 -m tools.sib.cli chunks <LIBRARY> <artifact-id>` for the
   retrieval-side JSONL.
8. **Report**: `python3 -m tools.sib.cli report <LIBRARY>` — completion metrics per
   protocol §9.

## 4. Grounding law for generation (per course)

- Evidence selection per family is law, not taste: `pipeline/evidence_policy.yaml`
  declares, for each of the 12 families, the primary source classes, the permitted
  supplementaries, and the forbidden substitutions. A run deviating from the policy
  fails preflight.
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

## 5. Gate semantics (per course, layered)

A generation wave passes through layered gates; each layer produces evidence in the
run record:

1. **Source preflight** — every source the wave needs resolves with of-record
   checksums intact; unresolved → the wave is blocked for the affected families.
2. **Structural** — `tools.sib.cli` validate/qa: front matter, sections, record ids,
   determinism (the validator's own law, unchanged).
3. **Evidence-claim QA** — every claim's citation resolves to the artifact's evidence
   pack (source id + locator); uncited claims are research/inferred at best and are
   either labeled `RESEARCH / INFERRED` or removed.
4. **Educational review** — accuracy, current/legacy separation, output usefulness
   (the pilot acceptance criteria: citation resolution, source coverage,
   current/legacy separation, educational accuracy, output usefulness).
5. **Staging / publication** — operator-ordered, validator-executed (unchanged).

`validate-manifest` against `tools/sib@<pin of record>`:

- **Shape: CLEAN** required — taxonomy-valid rows, correct applicability counts, gaps +
  backlog surfaced as `SIB-MANI-011` WARN / `SIB-MANI-012` INFO (designed disclosures,
  not defects).
- **Completeness:** REQUIRED artifacts missing from the landing zone report
  `SIB-MANI-007` ERROR — the truthful scoreboard; the count is the completion meter,
  and `report` is its metric view. Re-run after each generation wave; the gate is the
  scoreboard.
- Certification of record: the `pipeline/new_course.py` test instantiation
  (`BIOLOGY_4BI1`, 2026-10-25) reproduced the validated CHEMISTRY_4CH1 shape exactly
  (95 rows / 88 REQUIRED / 7 OPTIONAL / 0 shape issues).

## 6. Evidence-pack licensing law

Evidence packs are **bounded excerpts with identity preserved** — the same class of
permission the book lanes already operate under (chapter-question banks are
page-jump-only by precedent). A pack may carry: source id, classification, file
identity (path, sha256), and excerpts bounded by the pack builder's caps, each with
its page/question/line locator. A pack may NOT carry: bulk corpus export, full
documents, or re-licensed derivatives. Packs are run-scoped artifacts stored under
the run record, cited by hash.

## 7. Change law

Manifest edits (applicability flips, gap additions) are operator-ordered and regenerate
via the generator of record rather than hand-editing where possible. New course
libraries are scaffolded only by `pipeline/new_course.py` (never hand-mkdir'd). Every
library state change of record ships with a worklog entry in this repo and, where
material, a receipt.
