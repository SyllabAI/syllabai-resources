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
| Source resolution + evidence packs + run records | `pipeline/source_resolver.py`, `pipeline/evidence_pack.py`, `pipeline/run_manifest.py` (fail-closed) | `<LIBRARY>/runs/<RUN_ID>/` (resolution + pack + run receipt) |
| Artifact generation | the Z.ai agent run of record (provider-neutral; prompts `docs/SIB_ZAI_PROMPTS_V1.md`, provenance `docs/SIB_ARTIFACT_SCHEMA_V2.md`); NotebookLM is an OPTIONAL-HIS path (`SIB_NOTEBOOKLM_PROMPTS_V1.md`) | `<LIBRARY>/artifacts/` (drops, status GENERATED, `generated_by: zai_agent`) |
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
│   ├── source_resolver.py                 resolve source_manifest ids against canonical repos (fail-closed)
│   ├── evidence_pack.py                   bounded, identity-preserving evidence pack for one artifact
│   ├── run_manifest.py                    run-record writer (inputs, outputs, generator pins, hashes)
│   ├── generate_artifact.py               emit/ingest the Z.ai agent task for one artifact
│   ├── run_build.py                       orchestrate a run (preflight → pack → generate → land)
│   ├── tests/                             fixture-driven suite (no network, no model calls)
│   └── templates/course/                  manifest / source_manifest / curriculum_registry /
│                                          evidence_policy templates
└── <SUBJECT>_<SPEC>/                      one library per qualification, e.g.
    ├── manifest.yaml                      95-row applicability map (subject-specific)
    ├── source_manifest.yaml               classified sources + gaps (inventory-first)
    ├── curriculum_registry.yaml           pinned spec-point codes (anchor resolution)
    ├── evidence_policy.yaml               per-family evidence law (primary sources + restrictions)
    ├── runs/                              run records + receipts + evidence packs (append-only)
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

1. **Preflight the sources**: `python3 pipeline/run_build.py --course <LIBRARY>
   --artifact <ID> --resources-repo <path> --pastpapers-repo <path> --dry-run` —
   the source resolver resolves every source the artifact's `evidence_policy.yaml`
   entry requires against the canonical repos at their current revisions, verifies
   pinned checksums/git object ids where the manifest declares them, and FAILS
   CLOSED on any missing, ambiguous, or identity-mismatched source. No generation
   starts on a failed preflight; the resolution record is written under
   `<LIBRARY>/runs/`.
2. **Run the generation wave**: same command without `--dry-run` — the run
   manifest is opened (`runs/<RUN_ID>/run_manifest.yaml`: base commits, source
   revisions, generator provider/model, prompt-pack version, settings), the
   bounded evidence pack is built (identity + locators + excerpts per item), and
   the Z.ai agent produces the artifact into `artifacts/` with the canonical
   filename `<SUBJECT>_<SPEC>_<ARTIFACT-ID>_<SLUG>.md` (schema §1; slugs =
   taxonomy defaults) and the 15-field front matter (schema V2 §2),
   `status: GENERATED`, `generated_by: zai_agent`, V2 provenance pinned from the
   run manifest — never invented.
   (OPTIONAL-HIS NotebookLM path: the pre-SIB-GEN §3 procedure remains valid for
   notebook-based research drops, `generated_by: notebooklm`, V1 provenance.)
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

The gates are layered; no single green line proves educational correctness:

| Gate | What it proves | Owner |
|---|---|---|
| Source preflight | required sources resolve at expected identity (checksums/pins) | `source_resolver.py` (fail-closed) |
| Run provenance | run record complete; artifact V2 provenance matches the run manifest | `run_manifest.py` + landing check |
| Structural validation | front matter, IDs, sections, anchors, record structure conform | `tools/sib.cli` (validator of record) |
| Evidence/claim QA | load-bearing claims cite resolvable pack locators; no invented ids/quotes/sessions; no claim beyond evidence | agent QA prompt (`SIB_ZAI_PROMPTS_V1.md` §4) + reviewer |
| Educational review | content is educationally accurate and useful for the artifact | human/agent review of record — **never** inferred from a green structural gate |
| Staging / publication | governed lifecycle transitions with evidence re-verified | validator (operator-ordered) |

`validate-manifest` against `tools/sib`: (semantics unchanged)

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
