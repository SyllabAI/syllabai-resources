# SIB Pipeline — CHEMISTRY_4CH1

**Status:** OPERATIONAL (scaffold validated 2026-10-25 against the validator of record)
**Applies:** `SUBJECT_INTELLIGENCE_BUILD_V1.md` (protocol) + `SIB_ARTIFACT_SCHEMA_V1.md` (schema),
both copied in this `docs/` directory of record.

## 0. Roles and boundaries

| Role | Who | Writes |
|---|---|---|
| Library scaffold, manifests, registry | agent (this lane) | `manifest.yaml`, `source_manifest.yaml`, `curriculum_registry.yaml` |
| Artifact generation | NotebookLM / Gemini notebook `4CH1-SIB-NOTEBOOK-001` (per `SIB_NOTEBOOKLM_PROMPTS_V1.md`) | `artifacts/` (drops, status GENERATED) |
| QA, staging, publication, chunking | the validator of record, operator-ordered | `qa-reports/`, `staged/`, `published/`, `chunks/` |
| Canonical truth (KG, mastery, spec points, assessment identity) | SyllabAI core planes | **never written by this pipeline** |

The pipeline writes only inside the library root. All writes are path-confined by the validator
(`SIB-ING-001`); the library API exposes no canonical-write surface at all.

## 1. Library layout (live)

```
SubjectIntelligence/
├── README.md                              charter + law
├── docs/                                  protocol copies of record + this pipeline + requirements + inventory
└── CHEMISTRY_4CH1/                        the subject library
    ├── manifest.yaml                      95 rows (88 REQUIRED / 7 OPTIONAL), 4 source_gaps, 4 backlog
    ├── source_manifest.yaml               12 inventoried sources, classified, with git ids + of-record checksums
    ├── curriculum_registry.yaml           182 pinned spec-point codes (anchor resolution)
    ├── artifacts/     (empty)             NotebookLM output lands here as GENERATED
    ├── qa-reports/    (empty)             deterministic QA JSON per artifact
    ├── staged/        (empty)             QA-passed, awaiting operator publication decision
    ├── published/     (empty)             terminal lifecycle state
    └── chunks/        (empty)             deterministic chunk JSONL per artifact
```

## 2. Validator of record (canonical location)

The validator is **`SyllabAI/syllabai@tools/sib/`** (Python, self-contained — vendored
`yamlmini`, no third-party deps). It is deliberately NOT copied here: one implementation, no
drift. Pin it by commit at run time:

```bash
# fetch once per run (pin the sha of record; aa32db1413ea validated this scaffold)
git clone --depth 1 --filter=blob:none https://github.com/SyllabAI/syllabai.git /tmp/sib_master
# CLI surface
python3 -m tools.sib.cli --help            # validate-artifact | validate-manifest | qa | stage | publish | chunks | report
```

## 3. Operating procedure

1. **Provision the notebook** (backlog BL-003): create NotebookLM notebook `4CH1-SIB-NOTEBOOK-001`;
   upload the sources listed `CURRENT — AUTHORITATIVE` / `CURRENT — ASSESSMENT EVIDENCE` in
   `source_manifest.yaml`; label current vs legacy per protocol §2.
2. **Generate pass 1–2** (protocol §4 order): corpus orientation, then `CUR-01..CUR-08`.
   Drop outputs into `artifacts/` with the canonical filename
   `CHEMISTRY_4CH1_<ARTIFACT-ID>_<SLUG>.md` (schema §1; slugs = taxonomy defaults) and the
   15-field front matter (schema §2), `status: GENERATED`, `generated_by: notebooklm`.
3. **QA**: `python3 -m tools.sib.cli qa <library> <artifact-id>` — writes the deterministic
   `qa-reports/<ARTIFACT-ID>.qa.json`. Incomplete provenance fails QA with a machine-readable
   reason; the validator never invents source identifiers.
4. **Stage**: `python3 -m tools.sib.cli stage <library> <artifact-id>` (operator-ordered).
5. **Publish**: `python3 -m tools.sib.cli publish <library> <artifact-id>` (operator-ordered).
6. **Chunk**: `python3 -m tools.sib.cli chunks <library> <artifact-id>` for the retrieval-side
   JSONL.
7. **Report**: `python3 -m tools.sib.cli report <library>` — completion metrics per protocol §9.

## 4. Grounding law for generation (what each family may cite)

- Curriculum claims: `SRC-SPEC-4CH1` wording + `SRC-GRAPH-4CH1` anchors (registry pin
  `curriculum_registry.yaml`, 182 codes). Anchor tokens use the Edexcel dotted official codes
  (`1.1`–`99.999.99`); resolution INFO/WARNING per `SIB-ANCH-*`.
- Assessment claims: `SRC-QPMS-4CH1` (paper/session identity preserved). Topic-grain banks
  (`SRC-SME-EXAMQ-4CH1`, `SRC-PMT-4CH1`) are supplementary texture, never official identity.
- Explanation/pedagogy texture: `SRC-BOOK-4CH1-SB1` v3 chunks, `SRC-SME-NOTES-4CH1`
  (preserving its mappings/validation state), `SRC-EXT-NOTES-4CH1` after overlap adjudication.
- **Forbidden evidence substitutions:** no examiner sentiment synthesized from mark schemes
  (GAP-SRC-001); no legacy claims without legacy sources (GAP-SRC-002); no artifact grounding
  on `SRC-ROOT-BOOK-COPIES-4CH1` before adjudication; nothing invented to fill any gap
  (requirements §5 limitation law).

## 5. Gate state at scaffold time (2026-10-25)

`validate-manifest` against `tools/sib@aa32db1413ea`:

- **Shape: CLEAN** — 95/95 rows taxonomy-valid, applicability 88 REQUIRED / 7 OPTIONAL,
  4 source gaps + 4 backlog entries recognized (surfacings as `SIB-MANI-011` WARN /
  `SIB-MANI-012` INFO are the designed disclosures, not defects).
- **Completeness: 0/88 REQUIRED in landing zone** — 88 × `SIB-MANI-007` ERROR is the truthful
  empty-library state; the count is the completion scoreboard, and `report` is its metric view.
- Re-run the same command after each generation wave; the gate is the scoreboard.

## 6. Change law

Manifest edits (applicability flips, gap additions) are operator-ordered and regenerate via the
generator of record rather than hand-editing where possible. Every library state change of
record ships with a worklog entry in this repo and, where material, a receipt.
