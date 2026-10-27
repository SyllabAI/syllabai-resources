# Course Onboarding — adding ANY course to SubjectIntelligence

**Status:** OPERATIONAL (2026-10-25). Implements the operator directive of record:
*"SubjectIntelligence will host all courses not just 4ch1."*
**Catalog of record:** `../COURSES.yaml` (generated from
`Official-Specifications/manifest.json` — 56 qualifications covering 93/93 SME platform
courses — plus legacy declarations such as 4CH0).
**Worked example of record:** `../CHEMISTRY_4CH1/` (the validated first library).

## 0. The three laws

1. **One library per qualification.** The library unit is the spec *document*, not the
   platform course slug: modular/linear variants with distinct spec PDFs get distinct
   libraries (verified precedent: igcse-chemistry Issue 3 sha1 `3ad641b7…` vs
   igcse-chemistry-modular Issue 2 sha1 `9df406d3…`), while a genuinely shared document
   is served by one library. Naming contract: `<SUBJECT>_<SPEC>` (e.g. `CHEMISTRY_4CH1`,
   `BIOLOGY_4BI1`, `MATHS_4MA1`); legacy specs keep their own code (`CHEMISTRY_4CH0`)
   and are classified `LEGACY — HISTORICAL` throughout.
2. **No speculative libraries.** A library directory exists only once onboarding is
   operator-ordered (the §21 no-speculative-folders discipline, applied to SI). Planned
   courses live in `../COURSES.yaml` with status `PLANNED` — that is their home until
   ordered.
3. **Inventory first, gaps disclosed, never fabricated.** No artifact generation before
   `source_manifest.yaml` exists; absent sources become `source_gaps` rows, not silence
   and not invented evidence (requirements template §5 limitation law).

## 1. Scaffold (step 1)

```bash
python3 pipeline/new_course.py BIOLOGY_4BI1 \
    --subject "Biology" --qualification "International GCSE" \
    --curriculum-version 2017 --taxonomy <path-to-SyllabAI/syllabai-checkout>
```

The instantiator: creates `<LIBRARY>/{manifest.yaml, source_manifest.yaml,
curriculum_registry.yaml}` from the templates, creates the five work dirs
(`artifacts/ qa-reports/ staged/ published/ chunks/`), and — with `--taxonomy` —
generates the 95-row artifacts section straight from `tools/sib/taxonomy.py` of record
(HIS family `OPTIONAL`, all others `REQUIRED` by default; the pin commit is recorded in
the manifest header). It refuses to overwrite an existing library and rejects names that
violate the `<SUBJECT>_<SPEC>` contract.

**Certification of record (2026-10-25):** a test instantiation (`BIOLOGY_4BI1`) validated
against `tools/sib.cli validate-manifest @ aa32db1413ea` produced the exact validated
precedent shape — 95 rows, 88 REQUIRED / 7 OPTIONAL, 0 shape issues, 88 × `SIB-MANI-007`
(the truthful empty-library disclosure; see `docs/PIPELINE.md` §5).

## 2. Inventory-first sweep (step 2 — before anything else)

Sweep the canonical repos **read-only** for this course's sources and fill
`source_manifest.yaml`:

- `syllabai-resources`: `Official-Specifications/<slug>/` (spec + `spec.json` provenance),
  `books/` (CATALOG.md rows), `QP/` / `MS/` quadrants, `SME-ExamQuestion/` topic banks,
  `graph/<course-slug>/` (curriculum plane + spec-links mappings)
- `syllabai-pastpapers`: the course's QP/MS/ER subtree — **walk case-insensitively**
  (the 4CH0 corpus was briefly "missing" of record because of a lowercase-subtree miss;
  corrected in the BL-002 addendum), including examiner-report placements and their
  manifest material rows
- the core data plane (read-only): validated `SpecificationPoint` rows, SME revision
  notes and their mappings/validation state, question assets

Classify every source with the five-class vocabulary, record type / issuing body /
spec / version / coverage / provenance / limitations, and pin git object ids at a stated
tree. Cover the six minimum-corpus groups (requirements template §5) plus the legacy
group where a predecessor spec exists. Every absent source becomes a `source_gaps` row
in both `source_manifest.yaml` and `manifest.yaml`.

## 3. Curriculum registry pin (step 3)

Pin `curriculum_registry.yaml` from the course's authoritative curriculum plane
(e.g. `graph/<course-slug>/specification_points.yaml`): the pinned codes power SIB-ANCH
anchor resolution. The live registry stays authoritative.

## 4. Applicability review (step 4 — mandatory, subject-specific)

Review every manifest row against the subject reality. Default is REQUIRED (HIS
OPTIONAL); flip with a justification comment, and register every unfillable REQUIREMENT
as a source gap. Do not delete rows — the taxonomy is universal.

## 5. Validator gate (step 5)

```bash
python3 -m tools.sib.cli validate-manifest <SubjectIntelligence>/<LIBRARY>
```

Shape must be CLEAN (only `SIB-MANI-007` empty-landing-zone rows and designed
`SIB-MANI-011/012` gap/backlog disclosures allowed at this stage). Record the gate
result in the library worklog.

## 6. Generation onward (step 6)

Proceed exactly as `docs/PIPELINE.md` §3: run preflight → evidence packs →
generation passes (provider-neutral SIB-GEN run; legacy NotebookLM alternative) →
QA → stage → publish → chunks → report. All transitions operator-ordered; the validator
owns every lifecycle transition.

## 7. Operational hygiene (step 7 — read `docs/LESSONS_REGISTER.md` before ANY run)

The CHEMISTRY_4CH1 runs (RUN-001..015) paid for a set of operational laws that the
next course library inherits instead of re-deriving. `docs/LESSONS_REGISTER.md` is
the authoritative statement; its non-negotiables are wired into `docs/PIPELINE.md`
§8. The onboarding-time subset:

1. **Sparse surface:** expand the sparse checkout to cover every cone this course's
   sources live in (specifications, graph plane, legacy corpus, past-paper subtree)
   BEFORE preflight, and diagnose "missing" paths with `git ls-tree` first — the
   worktree lies under sparse rules (register §1.2).
2. **Fetch-first:** fetch and prove advance isolation before the first branch cut,
   and again at the git phase; file an `advance_disclosure.json` on any advance
   (register §1.3).
3. **Citation grammar from day one:** author every artifact directly in the r4
   grammar (path-qualified locators, `pN` page specs, one citation per paren,
   RUN-COMPUTED labels outside citation parens) and respect the r1 quote-binding
   law (quote only from pack excerpts you have read, preserving the source's own
   punctuation) — do NOT inherit the pre-r4 styles that 4CH1's RUN-002-era artifacts
   had to be repaired out of (register §2).
4. **Gate staged bodies before stamping:** the evidence-claim QA runs on the staged
   body first; a failed gate must never reach `artifacts/` (register §2.4).
5. **Pack caps and window math:** plan packs under the 60/1600/40k caps, compute
   md-query hit lines before writing `lines N-M` locators, and probe byte-identity
   before any full pack rebuild (register §3).
6. **Persist scripts + receipts:** every census/repair/gate script is saved under a
   persistent path and re-runnable; the run record carries census.json, the repair
   receipts, and the advance disclosure (register §1.1, §4).
7. **Debt discipline:** adjacent defects found mid-run get a `register_note` in the
   run receipt, not an unrequested scope expansion (register §6.1).

A new course that follows §1-§7 starts where CHEMISTRY_4CH1 ended, not where it
began — that is the point of this file and of the register.
