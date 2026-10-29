# SubjectIntelligence — lane worklog

> Append-only. One entry per run. Record task ID, base commit, evidence (AGENT.md rule 6).

---

Task ID: SIB-LIBRARY-001 (operator directive trace 1a16f3bf0be35db9: "For SIB, there are requirements. I want you to create a folder in syllabai-resources folder. called SubjectIntelligence. There create docs/copy existing docs. Create the pipeline." + requirements body filed as docs/SOURCE_REQUIREMENTS_4CH1.md)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)
Base commit: 09842f9f (fetched-first pre-push; no divergence encountered)

Work Log:
- READ-ONLY INVENTORY (the requirements' "key next step", executed same day): syllabai-resources swept via local blobless clone `git ls-tree -r` = full 82,234-path tree (API truncation ~39k avoided per LEDGER F16); syllabai-pastpapers / syllabai-experimental / syllabai-parser tree-swept; ledgers cross-read (books/CATALOG.md row 1 + §3.1, Official-Specifications/igcse-chemistry/spec.json, LICENSE-DATA.md, graph/igcse-chemistry/specification_points.yaml header). Findings filed: docs/SOURCE_INVENTORY_2026-10-25.md. Headline: 54 official 4CH1 papers across 16 sessions (1C×16/2C×16/1CR×11/2CR×11), validated SB1 parse v3, validated 182-point graph + spec-links mappings all PRESENT; examiner reports ABSENT (GAP-SRC-001, HIGH), 4CH0 legacy ABSENT (GAP-SRC-002), teaching guide ABSENT (GAP-SRC-004), standalone data sheet ABSENT (GAP-SRC-003) — disclosed, not fabricated.
- DOCS: 4 SIB docs of record copied byte-exact from SyllabAI/syllabai@docs/research (pinned aa32db1413ea): SUBJECT_INTELLIGENCE_BUILD_V1 / SIB_ARTIFACT_SCHEMA_V1 / SIB_NOTEBOOKLM_PROMPTS_V1 / SIB_VALIDATOR_IMPLEMENTATION_V1.
- PIPELINE: docs/PIPELINE.md (validator of record stays canonical at syllabai@tools/sib — pinned, not vendored, zero drift surface; procedures, grounding law, forbidden substitutions, gate semantics).
- LIBRARY SCAFFOLD: CHEMISTRY_4CH1/{manifest.yaml, source_manifest.yaml, curriculum_registry.yaml, artifacts/, qa-reports/, staged/, published/, chunks/}. manifest.yaml generated against tools/sib/taxonomy.py of record (95 rows: 88 REQUIRED / 7 OPTIONAL — HIS family OPTIONAL pending 4CH0, EXM-01..05 REQUIRED with gap notes; 4 source_gaps + 4 backlog entries). source_manifest.yaml: 12 sources classified per requirements §4 with git tree/blob ids @ f42033e0 + of-record checksums (spec sha1 3ad641b7…, SB1 sha256 d48020e0…, RAG zip sha256 9efdd9d6…). curriculum_registry.yaml: 182 spec-point codes pinned from graph/igcse-chemistry/specification_points.yaml (the live registry stays authoritative).
- GATE: python3 -m tools.sib.cli validate-manifest @ master aa32db1413ea — shape CLEAN (95/95 taxonomy-valid, applicability recognized, gaps/backlog surfaced as designed WARN/INFO); completeness honestly 0/88 REQUIRED in landing zone (88 × SIB-MANI-007 = the truthful empty-library scoreboard). One repair during authoring: plain-scalar YAML notes broke on ': ' (SIB-MANI-001) — generator switched to quoted scalars, re-gate clean.
- SCOPE: pure-additive SubjectIntelligence/** only; zero bytes under any existing path; canonical planes untouched; sources remain in their canonical repos per requirements §4.

Stage Summary:
- SubjectIntelligence/ LANDED: protocol copies of record + operator requirements + inventory findings + pipeline doc + validated CHEMISTRY_4CH1 library scaffold. Corpus verdict recorded: build can START on present evidence (CUR/EXP/ASM/MS/MIS/PED/PRA/PRO/TUT grounded); examiner-report acquisition (BL-001) and 4CH0 legacy (BL-002) are the operator-side acquisitions that unlock EXM + HIS. Next runs: BL-003 notebook provisioning → CUR-01..CUR-08 first wave.
---

Task ID: SIB-LIBRARY-002 (operator order trace 1a16f5bd6146b01d: "acquire examiner reports + 4CH0 corpus" — the BL-001/BL-002 acquisitions this library queued)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)
Base commit: 2c33982b (fetched-first; no divergence encountered)

Work Log:
- SOURCE of record for both acquisitions: Pearson's own public CDN (qualifications.pearson.com/content/dam), discovered through Pearson's site search index (Algolia qualifications-uk_LIVE_master-content — the same index the qualifications site queries; every target = an issuing-body catalog row, zero third-party archives, zero URL guessing). Acquisition machine persisted at agent workspace: sib_er_acquisition.py (fetch → %PDF magic → pymupdf → printed-PDF-text identity [spec code + paper ref + session] → sha256 → qpdf state), sib_er_placement.py (surgical manifest insertions, fail-closed identity asserts), sib_legacy_spec_placement.py.
- BL-001 EXAMINER REPORTS: 54 ERs placed in syllabai-pastpapers @ 3632b0e6 (pushed of record) — 20 × 4CH1 (2019-06/2022-06/2023-11/2024-06/2024-11/2025-06) + 34 × 4CH0 legacy (13/16 sessions incl. Certificate-tree quartets 2014-06/2015-01/2016-06/2017-01); every paper manifest gained an examiner-report material (source_type official-board-site, source_url of record); 594 insertion lines, 0 deletions elsewhere. Pre-existing 2023-06 quartet (wave 8, Paperlords) left byte-untouched with Pearson's own URLs filed for future F15-class adjudication.
- BL-002 LEGACY 4CH0: first-hand re-walk CORRECTED the v1.0 inventory — the QP/MS archive was already complete in syllabai-pastpapers 4ch0/ (40 dirs / 16 sessions; v1.0's "zero 4CH0 hits" = case-sensitive miss of the lowercase subtree, disclosed in manifest_history + addendum). Added the missing doc classes: 34 legacy ERs (same wave) + official legacy spec corpus landed HERE: Official-Specifications/igcse-chemistry-legacy-4ch0/ (Issue 3 spec 32pp sha1 1ca8219b…, Issue 5 spec+SAMs 118pp 51e6505a…, 2009 SAMs 70pp 0853b039…) with spec.json provenance; dir deliberately OUTSIDE manifest.json (39-SME-course scope law) and documented in Official-Specifications/README.md.
- MANIFESTS: source_manifest.yaml v1.0 → v1.1 (3 new sources SRC-ER-4CH1 / SRC-ER-4CH0-LEGACY / SRC-LEGACY-SPEC-4CH0; GAP-SRC-001/002 → RESOLVED with honest residuals; minimum_corpus_check group 4 ABSENT→PARTIAL-covered; legacy_inventory ABSENT→PRESENT) + manifest.yaml (EXM-01..05 gap notes → evidence-present notes; HIS-01..07 enabled-with-LEGACY-labeling notes; BL-001/BL-002 marked DONE). Pre-existing YAML bug repaired of record: source_manifest SRC-EXT-NOTES-4CH1 title was invalid YAML (mid-scalar quote — v1.0 ship; the v1.0 gate only machine-validated manifest.yaml) — fixed + whole-file safe-load proven.
- ADDENDUM: docs/SOURCE_INVENTORY_ADDENDUM_2026-10-25-BL.md (inventory correction + residual disclosures + six-groups re-check).
- RESIDUALS DISCLOSED, NOTHING FABRICATED: no public ER exists for 4CH1 2020-01/2020-11/2021-01/2021-11/2022-01/2023-01 (zero Pearson catalog rows) + 2021-06 (cancelled) + 4CH0 2014-01/2015-06/2016-01 (soft-404, not published); Nov-2025 + June-2026 PEFs sit behind Pearson silver tier (401 anonymous) — operator queue; 4CH0 2018-06 CR ERs verified-but-placed-NOT (no QP/MS dir of record; no-speculative-folders §21; sha256s in wave report).
- GATE: python3 -m tools.sib.cli validate-manifest @ SyllabAI/syllabai aa32db1 (blobless shallow clone of the canonical validator) — manifest SHAPE CLEAN of record: 95 rows (88 REQUIRED / 7 OPTIONAL recognized), zero shape errors; issues = 88 × SIB-MANI-007 (the truthful empty-library scoreboard, unchanged semantics from SIB-LIBRARY-001) + 4 × SIB-MANI-011 WARNING (source_gaps surfaced as designed, incl. the two RESOLVED rows with full disclosure text) + 4 × SIB-MANI-012 INFO (backlog surfaced as designed).
- SCOPE: SubjectIntelligence/** (manifests, README, addendum, worklog) + Official-Specifications/igcse-chemistry-legacy-4ch0/** + Official-Specifications/README.md section only; canonical planes untouched (graph/, spec-links/, SME-*, books/ zero bytes); sources remain in their canonical repos (pastpapers archive points, resources spec docs point).

Stage Summary:
- BL-001 + BL-002 COMPLETE OF RECORD: EXM family evidence is real (24 4CH1 ERs / 8 sessions + 34 4CH0 / 13 sessions), HIS family unlocked (complete legacy QP/MS + 34 ERs + official spec corpus), six-groups check: examiner reports PARTIAL-covered, legacy PRESENT. Validator-gate note: source_manifest.yaml now safe-load-proven (pre-existing invalid-YAML title repaired). Next runs unchanged: BL-003 notebook provisioning → CUR-01..CUR-08 first wave; operator-side queue: silver-tier Nov-2025/June-2026 ERs if wanted.

---

Task ID: SIB-LIBRARY-003 (operator directive trace 1a16f9049652673d: "SubjectIntelligence will host all courses not just 4ch1")
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)
Base commit: 43fa8a61 (fetched-first; local == origin/main, no divergence)

Work Log:
- ALL-COURSES GENERALIZATION of record. Registry: COURSES.yaml generated programmatically from Official-Specifications/manifest.json of record (schema syllabai.official-specifications/1.0; 56 qualification documents / 93 SME courses covered, missing: none) — 1 ONBOARDED (CHEMISTRY_4CH1) + 55 PLANNED (spec_codes/issue quoted verbatim; exclusion by SLUG not spec-code containment, because modular/double-award share 4CH1 CODES but are distinct spec DOCUMENTS — verified igcse-chemistry-modular = own PDF, Issue 2, sha1 9df406d3… vs linear Issue 3 sha1 3ad641b7…) + 1 LEGACY declared (CHEMISTRY_4CH0: corpus PRESENT in canonical repos, library NOT scaffolded — no speculative dirs). Library-unit law codified: one SI library per qualification spec document. PyYAML safe-load gate GREEN; catalog arithmetic asserted (1+55=56).
- PIPELINE: templates/course/{manifest,source_manifest,curriculum_registry}.template.yaml (parameterized shapes mirroring the validated 4CH1 precedent; classification vocabulary + identifier law + six-groups guidance embedded) + pipeline/new_course.py (fail-closed instantiator: name-contract regex ^[A-Z][A-Z0-9]*_[A-Z0-9.]+$, overwrite refusal, placeholder-substitution guard, work dirs + .gitkeeps, optional --taxonomy <syllabai-checkout> generating the 95-row artifacts section straight from tools/sib/taxonomy.py with HIS=OPTIONAL default and the pin commit recorded).
- VALIDATOR CERTIFICATION: test instantiation BIOLOGY_4BI1 (in /tmp, NOT committed — no speculative library of record) validated against tools.sib.cli validate-manifest @ aa32db1413ea (fresh fetch, HEAD verified = pin of record): 95 rows / 88 REQUIRED / 7 OPTIONAL / 0 non-007 shape issues / 88 × SIB-MANI-007 truthful-empty-library — EXACT structural match to the validated CHEMISTRY_4CH1 gate. Negative tests GREEN (overwrite refusal; name-contract refusal). Test tree deleted after certification.
- DOCS: README.md rewritten as the all-courses charter (catalog section, library-unit law, naming contract, roster 1/1/55, six directory laws incl. the new all-courses discipline); docs/PIPELINE.md generalized to per-course operating procedure (parameterized <LIBRARY> roles/procedure/grounding law; certification recorded); docs/COURSE_ONBOARDING.md NEW (3 laws + 6 steps: scaffold → inventory-first sweep → registry pin → applicability review → validator gate → generation); docs/SOURCE_REQUIREMENTS_TEMPLATE.md NEW (the operator's 4CH1 requirements generalized to every course: 6 core sources, A–F document classes with subject-neutral wording, 8 additional-source rows, five-class vocabulary, six minimum groups + limitation law verbatim).
- REORGANIZATION (git mv, history preserved): the 4CH1-specific docs moved INTO the course library per the all-courses architecture — docs/SOURCE_REQUIREMENTS_4CH1.md → CHEMISTRY_4CH1/SOURCE_REQUIREMENTS.md; docs/SOURCE_INVENTORY_2026-10-25.md → CHEMISTRY_4CH1/INVENTORY_2026-10-25.md; docs/SOURCE_INVENTORY_ADDENDUM_2026-10-25-BL.md → CHEMISTRY_4CH1/INVENTORY_ADDENDUM_2026-10-25-BL.md. Stale references patched in the moved files + CHEMISTRY_4CH1/source_manifest.yaml header; grep-verified zero remaining stale paths (remaining ../CHEMISTRY_4CH1 hits in docs/ are intentional new-doc references). WORKLOG history entries keep their original paths of record (append-only law).
- SOURCES UNTOUCHED: canonical repos, other quadrants, mark_points — zero contact; all changes inside SubjectIntelligence/.

Stage Summary:
- SubjectIntelligence is now an ALL-COURSES library of record: registry (56-qualification catalog of record + legacy declaration), template pack + validator-certified instantiator, generalized requirements/onboarding/pipeline docs, and course-specific docs living inside course libraries. Onboarding any next course = docs/COURSE_ONBOARDING.md (one instantiator run + inventory sweep + gates). CHEMISTRY_4CH1 remains the validated worked example; no canonical plane, source file, or other library was touched.

---

Task ID: SIB-LIBRARY-004 / SIB BL-005 (operator trace 1a16fa5034655795: "There are some documents in official pearson website. (e.g …/coursematerials.html#filterQuery=…Teaching-and-learning-materials) what about these?")
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)
Base commit: 7dbdf2ba (fetched-first; sibling guided-lessons commit absorbed by pull --ff-only)

Work Log:
- CATALOG SWEEP: the operator-linked Pearson coursematerials page queried via its own embedded Algolia index (app L639T95U5A / qualifications-uk_LIVE_master-content / key read from the public page HTML — same issuing-body catalog class as BL-001, no third-party mirror); course filter Pearson-UK:Specification-Code/igcse17-chemistry (both path forms, quoted facet values). Full snapshot of record: 239 rows = 173 Exam-materials + 60 Teaching-and-learning-materials + 4 Specification-and-sample-assessments + 2 page rows (catalog json retained at the acquisition workspace).
- ACQUISITION (scripts/sib_tl_acquisition.py of record): 30 files placed — TIER-1 gap-closers (11): official SCHEME OF WORK docx, Getting Started guide 28pp, topic teaching guides Chemical bonding 9pp + Chemical equilibrium 7pp, CORE PRACTICALS guide 211pp, practical terminology guidance, COMMAND WORDS docx, exemplars with examiner commentary 89pp + 26pp, official SAMs 88pp, Jan→Nov series-structure change notice, linear course planner pptx; TIER-2 supplementary (19): maths-skills ×9, transferable-skills mappings ×2, cross-board/level mappings ×3, lab setup ×2, core-practical playlist, training transcript, sciences mapping guide. Placement: Official-Specifications/igcse-chemistry/teaching-and-learning-materials/ + 2 root files (SAMs, notice), per-file provenance teaching-materials.json (same pattern as spec.json; deliberately outside manifest.json scope by the legacy-dir law).
- VERIFICATION fail-closed: PDF magic + printed-text identity tokens / ZIP CRC + OOXML structure per class; 30/30 unique sha256; placement+sha re-verified post-copy ALL GREEN; Pearson soft-404 class N/A (all rows served real files); 0 silent rows — 209 catalog rows disclosed-not-taken with per-row dispositions (143 exam-materials already of record in syllabai-pastpapers; 35 teacher-training packs ungated-bulk-class awaiting operator order; 25 silver-gated 401 = operator queue; admin/page/already-held).
- REGISTRY v1.2: source_manifest.yaml 15→17 sources (SRC-TL-4CH1 CURRENT—AUTHORITATIVE/SUPPLEMENTARY + SRC-SAMS-4CH1 CURRENT—ASSESSMENT EVIDENCE, tier-1 sha256s pinned, full table by reference); GAP-SRC-004 RESOLVED; GAP-SRC-003 NARROWED (standalone data-sheet residual only, LOW); minimum_corpus_check: group 2 PARTIAL→PRESENT, group 6 PARTIAL→PRESENT — scoreboard 5 PRESENT + 1 PARTIAL (group 4 ER, residuals are publishing gaps); manifest.yaml gap texts synced; PyYAML safe-load gate GREEN; tools.sib.cli validate-manifest @ aa32db1413ea SHAPE CLEAN (95 rows, 88×-007 truthful-empty + 4 gap + 4 backlog designed disclosures, 0 shape errors).
- DOCS: Official-Specifications/README.md new T&L section (provenance table + scope note + disposition summary); course inventory addendum #2 (INVENTORY_ADDENDUM_2026-10-25-TL.md); README current-state synced (17 sources, six-groups scoreboard). One YAML lesson of record: EOL/inline ": " inside plain multi-line scalars breaks parsing — three occurrences repaired in place (safe-load proven whole-file).
- Sources stay canonical (pastpapers untouched); canonical planes, other quadrants, mark_points: zero contact.

Stage Summary:
- BL-005 COMPLETE OF RECORD: the operator-pointed Teaching-and-learning-materials category is inventoried (239 rows), the SI-relevant ungated set is acquired + verified (30 files incl. GAP-SRC-004 closers), and the six-groups scoreboard reaches 5 PRESENT + 1 PARTIAL — the only PARTIAL is the examiner-reports group where every session with a public ER is already covered (residuals = Pearson publishing gaps, disclosed). Required-source coverage for the 4CH1 build is now COMPLETE; next build run unchanged: BL-003 notebook provisioning → CUR-01..CUR-08. Standing queue: 35 training packs bulk intake + 25 silver-gated rows (operator), PAT rotation.

---

Task ID: SIB-GEN r0 / BL-006 + BL-007 (operator orders "Execute SIB-GEN" trace 1a1726b6684c4055 + "run BL-007" trace 1a172e0138191add)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)
Base commit: ba78155 (fetched-first after sandbox recycle; sparse clone SubjectIntelligence + pilot source cones; origin had advanced with glw wave-5 / T-BOOK-050/051 / UGM lane 10 — zero path overlap)

Work Log:
- BL-006 INFRASTRUCTURE (commit 59f1ba1): provider-neutral docs r0 edition — PIPELINE.md rewritten (generation = zai_agent SIB-GEN run pipeline; NotebookLM = legacy provider reference; layered gate semantics §5; evidence-pack licensing law §6; run-manifest law), NEW docs/SIB_ARTIFACT_SCHEMA_V2.md (generated_by vocabulary +zai_agent; provenance ONE-OF: v1 notebook-shape | v2 generator-shape with generation_run_id + generator{provider,model,agent_version} + source_revisions; additive, zero v1 fields removed), SUBJECT_INTELLIGENCE_BUILD_V1 + COURSE_ONBOARDING + SIB_VALIDATOR_IMPLEMENTATION_V1 de-NotebookLM'd, SIB_NOTEBOOKLM_PROMPTS_V1 retagged OPTIONAL-HIS (retained unchanged); pipeline modules source_resolver.py / evidence_pack.py / run_manifest.py / generate_artifact.py / run_build.py + evidence_policy.yaml (12-family primary/supplementary/legacy/forbidden law); BL ledger: BL-003 SUPERSEDED (history preserved), BL-004 gated open, NEW BL-006/007/008.
- PILOT BL-007 = run SIB-CHEMISTRY_4CH1-RUN-001 (commit 10043d1 + this commit): preflight (17 sources; 7 RESOLVED incl. all five pilot primaries SRC-SPEC/SRC-GRAPH/SRC-TL/SRC-QPMS/SRC-ER-4CH1; 10 disclosed FAILED outside pilot scope) -> evidence packs (CUR-01: spec pp1-15 + graph yaml structure + TL excerpts, 4 sources; MIS-01: 24 official ERs, all 8 held sessions, page-3 general commentary + question-level depth for 2023/2024/2025 1C, 33 excerpts / 32.4k chars bounded) -> authored CUR-01 (14.3k chars, 8 records) + MIS-01 (26.6k chars, 12 records) from packs alone -> stamped v2 front matter -> validator QA (tools.sib @ master PR branch): CUR-01 0/0/0 + MIS-01 0 errors/23 anchor warnings -> evidence-claim QA script: 22 ER citations + all page locators resolve -> run manifest receipts validate OK.
- REGISTRY DEFECT CAUGHT BY PREFLIGHT (first-run proof the gate works): source_manifest v1.2 identifiers for SRC-TL/SAMS (9 sha256s) did NOT match the actual repo files — shared first 20 hex chars, divergent tails (transcription-corruption class). First-hand verification: actual files EQUAL the per-file ledger of record (teaching-materials.json committed with BL-005) — acquired files intact; only the registry summary identifiers were wrong. Repaired v1.2 -> v1.2.1 with manifest_history disclosure (commit 10043d1).
- VALIDATOR DEFECT FIXED IN PAIRED MASTER PR (branch sib-schema-v2-provenance @ 3872bec): (1) schema v2 provenance one-of + zai_agent vocabulary + generator/source_revisions validation, 11 new tests; (2) anchors.py 'report or ...' falsiness bug — an empty shared ValidationReport (__len__==0) made validate_anchors silently DISCARD all anchor findings for otherwise-clean artifacts (found when the old artifact's 23 warnings appeared only alongside unrelated issues); identity-check fix + 2 regression tests. SUITE 139/139 GREEN.
- HONEST WARNINGS SHIPPED: MIS-01 carries 23 x SIB-ANCH-002 (anchors structurally valid, unresolvable) — root cause pre-existing scaffold defect: curriculum_registry.yaml pin key (spec_point_codes) does not match the validator CLI's registry key law (specification_points) and pins prefixed codes (4CH1-1.13) while the anchor law extracts bare dotted tokens (1.13); the validator's SPEC_POINT_RE also does not cover Edexcel 'C'-suffixed points. Repair queued operator-side; disclosed in artifact + run manifest; NOT silently patched mid-run.
- EXTRACTION DISCLOSURE: 2024-06 4CH1/1C ER pp3-6 glyph-garbled (embedded-font text-extraction failure) — NOT cited by any record; re-extraction candidate. MIS-01 covers exactly the 8 held sessions; the six no-public-ER sessions + silver-tier Nov-2025/June-2026 stay disclosed gaps, nothing fabricated.
- SCOPE: SubjectIntelligence/** only (docs r0, pipeline modules, BL ledger, source_manifest v1.2.1, artifacts/ 2 files, qa-reports/ 2 files, runs/SIB-CHEMISTRY_4CH1-RUN-001/ full receipts, WORKLOG). Canonical planes untouched; sources stay canonical; mark_points untouched; zero DB writes; zero deploys.

Stage Summary:
- BL-006 DONE + BL-007 PILOT EXECUTED OF RECORD on branch sib/sib-gen-r0 (3 commits: 59f1ba1 infra, 10043d1 registry repair + fixes, this commit = pilot receipts + worklog). Two artifacts GENERATED + QA_PASSED (0 errors both; warnings = the disclosed anchor-resolution degradation). Acceptance criteria: citation resolution PASS / source coverage 8-of-8 held sessions PASS / current-legacy separation PASS (fully CURRENT, validator contradiction checks green) / educational accuracy PASS (every record quotes its named ER excerpt) / output usefulness PASS (records carry diagnostics + interventions). BL-008 batch orchestration UNLOCKED on operator order only. Coordinated master PR branch sib-schema-v2-provenance @ 3872bec advances tools/sib of record.

---

Task ID: SIB-GEN r0 — coordinated-pair merge of record (operator order "merge resources #124 + master #54 together" trace 1a173123af970545)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)

Work Log:
- CI GATE FINDING (merge blocked per law, then repaired in-turn): master PR #54's first CI runs (40191937682 / 40191981272) were RED — 135 passed / 2 failed / 2 skipped, both v2-shape QA tests failing SIB-PROV-001 'required provenance field missing (v2 generator-shape): generator'. First-hand reproduced: the stdlib-only front-matter fallback (frontmatter._builtin_parse) supported only ONE-level nested mappings (its own docstring said so) and SILENTLY FLATTENED schema v2's provenance.generator block on PyYAML-less environments — CI runners ship no PyYAML so the fallback is the primary parser there, while the local '139/139 GREEN' verification rode the PyYAML path and could not see it. A silent misparse — the exact class yamlmini's docstring forbids. The RUN-001 artifacts were NEVER defective; the parser was.
- REPAIR @ 8ac5f02 (4th commit on the paired master branch, disclosed on PR #54 issuecomment-6397880458): fallback delegates to yamlmini.parse (full nested subset; YamlMiniError still surfaces as parse_error; parse_mode/'builtin' + FrontMatterResult contract unchanged; _builtin_parse removed as dead code); parity doctrine now actually tested via fixtures.no_pyyaml masking (sys.modules['yaml']=None): fallback metadata == PyYAML metadata for BOTH provenance shapes, nested generator + source_revisions preserved, validate_artifact QA passes stdlib-only for v1 and v2, one-of rejections intact on the fallback path. SUITE 143: PyYAML path 143/143; stdlib-only simulation 141 passed / 2 skipped / 0 failed. CI GREEN @ 8ac5f02 (guard + verify + sib-validator-tests x2).
- MERGE ORDER EXECUTED: master PR #54 merged FIRST as merge commit 357ace0a230f5e0095ad230320af587dca6bb71f (ls-remote verified) — tools/sib pin of record ADVANCES aa32db1413ea -> 357ace0a. This worklog's earlier 'validated @ aa32db1413ea / @ 3872bec' lines are historical gate receipts (append-only, untouched); runs/.../run_manifest.json source_revisions.syllabai=3872bec stays — the exact validator state that QA'd RUN-001, contained in the merge.
- PIN ADVANCE (this commit): PIPELINE.md validator-fetch note + README.md docs-tree pin now of-record @ 357ace0a (schema v2 provenance one-of + anchor-report fix + stdlib-only nested fallback; aa32db1413ea noted as the v1-era validator). Then resources PR #124 merges as the pair's second leg.

Stage Summary:
- COORDINATED PAIR LANDED OF RECORD: master #54 (357ace0a) + resources #124 (this branch) — SIB generation is provider-neutral with a validator of record that passes stdlib-only CI. BL-006 DONE, BL-007 pilot receipts landed (CUR-01 + MIS-01 GENERATED + QA_PASSED), BL-008 batch orchestration unlocked on operator order only; staging/publication remain operator gates. Queued operator-side: curriculum-registry anchor repair (spec_point_codes key law + prefixed codes + C-suffix), PAT rotation.

---

Task ID: BL-008 wave 1 — batch orchestration (operator order "BL-008 batch orchestration" trace 1a1733c96d40e6dd)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)

Work Log:
- Fetch-first after sandbox recycle: coordinated pair LANDED of record (master #54 @ 357ace0a = tools/sib pin of record; resources #124 @ cb28433); resources main fleet-advanced to ebe914b (zero SubjectIntelligence overlap). BL-008 of-record definition read from the manifest BL backlog verbatim: "full-wave generation runs (remaining REQUIRED families per protocol §4 order) via pipeline/run_build.py once BL-007 pilot acceptance is recorded. Operator-ordered per wave." BL-004 = the wave definition: CUR-01..CUR-08; pilot acceptance recorded -> wave 1 = CUR-02..CUR-08.
- REPAIR PAIR (commit 084a99c, shipped first): (a) source_manifest v1.2.1 -> v1.2.2 LOCATOR PRECISION REPAIR — SRC-BOOK-4CH1-SB1's evidence path was the lane DIRECTORY whose 1,234 parsed chunks sort before student-book.pdf and starve the resolver's 400-member digest cap (RUN-001's 'FAILED;DIGEST_UNMATCHED' was this locator+scan artifact, NOT file drift); first-hand verified the PDF @ ebe914b hashes to the pinned d48020e0cc0b…cc04 (54,298,792 bytes), byte-identical to books/CATALOG.md §3.1; locator now points at the exact file, CATALOG pointer row quoted so the resolver classifies it ALT; (b) pipeline/source_resolver.py dir scans now hash DIRECT CHILDREN FIRST then deep members (same 400 cap; members_total disclosed per entry). PREFLIGHT after repair: PASS for CUR — 8/17 RESOLVED (SPEC, GRAPH, TL, SAMS, BOOK, ROOT-BOOK-COPIES, QPMS, ER-4CH1), 9 FAILED all genuinely-absent corpora, disclosed never filled.
- RUN SIB-CHEMISTRY_4CH1-RUN-002 (branch sib/bl-008-batch-r0): agent-authored pack specs x7 committed to the run record (cap-aware: exemplar-code queries for the big stores; evidence_pack.py f_query dict collapses duplicate path_suffix entries — documented by first-hand hit, one entry per path); deterministic census annex (census.json, inputs sha256-pinned) so quantitative claims are RUN-COMPUTED and machine-verifiable; evidence-claim QA script (scripts/sib_bl008_evidence_claim_qa.py) generalized from the pilot: (SRC-*, locator) must resolve to pack excerpts (page/line-overlap), (census.json, path) must resolve to the annex (multi-path ';' splits; prose inside citations rejected).
- WAVE GENERATED: CUR-02 Specification Interpretation (9 records: demand classes, KNOW_TERM law, quantitative strand, practical demand, papers applicability law, wording authority + 2.31 verbatim typo, the 181/182 gap = 4.15 + explain delta, per-topic profile, verb taxonomy); CUR-03 Concept Taxonomy (7: node taxonomy, spec-point anchoring, aliases, MISCONCEPTION family w/ mark-scheme ground, AI_SUGGESTED tier law, coverage shape, not-the-canonical-KG); CUR-04 Concept Relationships (7: 8-relation vocabulary + frozen triple distinction, PART_OF, REQUIRES direction law, EXPLAINED_BY/RELATED_TO, confusion layer, error->remediation loop, per-edge provenance + 389/97/2 tiers); CUR-05 Prerequisite Knowledge Map (7: the COMPLETE 35-edge OPERATOR_RATIFIED store, S1/S2/S3/S4 chains, RELATED_TO complement, zero cross-topic at statement grain, consumption contract); CUR-06 Cross-Topic Connections (7: two-grain method, S1-as-foundation, S2<->S3 twist, bridge inventory law, spiral reading, boundary discipline, consumption contract); CUR-07 Terminology & Definitions (6: all 25 command words verbatim, four demand tiers, MCQ tier, KNOW_TERM bridge); CUR-08 Curriculum Boundaries (7: paper-content boundary, Double Award sharing, series/administration, AO boundary + repair note, practical boundary, coverage boundary, specimen boundary). 50 records total, family counter CUR-001..CUR-050 continuous.
- GATES x7: structural QA (tools.sib.cli @ 357ace0a): 0 errors / 0 warnings each (1 honest INFO anchor-registry notice, pre-existing operator-queued defect); evidence-claim QA: 209 citations checked, 0 violations (CUR-02 43, CUR-03 25, CUR-04 20, CUR-05 29, CUR-06 35, CUR-07 30, CUR-08 27); educational review PASS per artifact on the five pilot criteria; staging/publication NOT REQUESTED (operator gates). Run manifest populated (7 artifacts, attempts disclosed: CUR-02/03/04/05/06 = 2, CUR-07 = 1, CUR-08 = 3 — all within-run citation-format/pack-grounding re-stamps before receipts; no governed state overwritten) — validate OK.
- MANIFEST SCOREBOARD (designed truthful state): validate-manifest @ 357ace0a -> 79 x SIB-MANI-007 ERROR (REQUIRED artifacts not yet landed; 88 REQUIRED - 9 landed = 79; completion meter: CUR 8/8 COMPLETE, MIS 1/9), 4 x SIB-MANI-011 WARN (declared source gaps), 7 x SIB-MANI-012 INFO (backlog entries) — the designed-disclosure classes per PIPELINE.md §5.
- BL LEDGER STAMPS (append-only status updates): BL-004 DONE (wave landed), BL-007 ACCEPTED (pilot receipts merged of record), BL-008 WAVE 1 EXECUTED + remaining passes queued with their blockages named (EXP + TUT blocked on student-book text extraction — image-only scan; HIS blocked on legacy 4CH0 sources; MIS-02..09 + ASM/MS/EXM/PED/PRA/PRO evidence-unblocked).
- SCOPE: SubjectIntelligence/** only (source_manifest v1.2.2, source_resolver.py hardening, manifest BL stamps, artifacts/ +7, qa-reports/ +7, runs/SIB-CHEMISTRY_4CH1-RUN-002/ full receipts incl. pack specs + census annex + bodies, WORKLOG). Canonical planes untouched (read-only; graph defects disclosed not fixed); sources stay canonical (student-book.pdf materialized locally for digest verification only, never committed); mark_points untouched; zero DB writes; zero deploys; PAT one-shot helper for push (exposure +1).

Stage Summary:
- BL-008 WAVE 1 LANDED OF RECORD on branch sib/bl-008-batch-r0: the 4CH1 library holds 9 GENERATED artifacts (CUR-01..08 + MIS-01), CUR family COMPLETE at §4 pass 2, run receipts complete under runs/SIB-CHEMISTRY_4CH1-RUN-002/. The 4CH1 BL ledger: BL-001/002 DONE, BL-003 SUPERSEDED, BL-004 DONE, BL-006 DONE, BL-007 ACCEPTED, BL-008 wave 1 EXECUTED, BL-005 consumed by BL-001/002. Queued operator-side: curriculum-registry anchor repair, PAT rotation, student-book native-text purchase decision (EXP/TUT unlock), legacy 4CH0 digest repair (HIS unlock).

---

Task ID: BL-008 pass 4 — MIS-02..09 (operator orders "merge PR #131; then MIS-02..09 and what do you mean by 'student-book extraction decision'?" trace 1a173a17de8a2739 + one-shot PAT trace 1a1745ed7792709d)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)

Work Log:
- Operator one-shot PAT supplied in-chat; used via session-env credential helper ONLY (never written to file/URL/worklog). PR #131 (BL-008 wave 1) MERGED FIRST per operator order — merge commit 2453da5 (CI 'sync' green; mergeable clean; API 200).
- Fetch-first rebuild after sandbox recycle: the earlier pass-4 attempt (local branch @ 41603c07, run receipts and all) was confirmed NEVER pushed (HTTP 422 on the sha) and lost with the sandbox — this entry supersedes it as the run of record; 41603c07 stays unreferenced.
- Preflight (run_build.py) PASS for MIS: SRC-ER-4CH1 + SRC-QPMS-4CH1 primaries RESOLVED (7/17 sources; 10 genuinely-absent corpora disclosed, never filled). Resources main @ 2453da5, pastpapers @ 04df741d, validator of record @ 357ace0a (master main HEAD = pin; tools/sib byte-identical).
- RUN SIB-CHEMISTRY_4CH1-RUN-003: 8 agent-authored pack specs + packs (MIS-02..09; 22 unique ER inputs sha256-pinned; QPMS/TL identity rows; SB1 identity-only per image-only-scan law); authoring FROM THE PACKS ALONE; MIS-013..MIS-070 (58 records: MIS-02 Concept Confusion Atlas 8, MIS-03 Common Student Errors 8, MIS-04 Reasoning Errors 7, MIS-05 Calculation Errors 7, MIS-06 Terminology Errors 7, MIS-07 Exam Answer Errors 7, MIS-08 Misconception Diagnostics 7, MIS-09 Misconception Interventions 7).
- GATES x8: structural (tools.sib.cli qa @ 357ace0a): 0 errors x8; warnings (5-15 per artifact) = the PRE-EXISTING SIB-ANCH-002 anchor-registry degradation (registry key law + prefixed pins + C-suffix), same disclosed class as MIS-01's 23 — operator-queued repair unchanged; evidence-claim QA r1: 86 citations checked, 0 VIOLATIONS (every (SRC-*, locator) resolves to the artifact's own pack; per-record quote grounding; census paths resolve); educational review PASS on the five pilot criteria per artifact; staging/publication NOT REQUESTED (operator gates).
- REPAIRS SHIPPED IN THIS RUN (disclosed): (1) pipeline/sib_evidence_claim_qa.py r1 COMMITTED OF RECORD — the wave-1 script had NOT been committed with #131; r1 adds per-record quote binding + closes the single-page-citation fail-open hole (unparseable citations fail closed); (2) in-turn citation-binding repairs BEFORE receipts: 4 cross-pack misattributions + 3 ungrounded fragments caught by the r1 gate and fixed in bodies pre-stamp (no governed state overwritten); (3) qa-env incident: the validator was first invoked under a PyYAML-less interpreter, producing a false SIB-PROV-002 ERROR — re-run under the PyYAML-capable interpreter matching the landed precedent; environment fault, not artifact/validator fault.
- Scoreboard (validate-manifest @ 357ace0a): 71 x SIB-MANI-007 ERROR (88 REQUIRED - 17 landed = 71; completion meter), 4 x SIB-MANI-011 WARN (declared source gaps), 7 x SIB-MANI-012 INFO (backlog) — the designed-disclosure classes.
- SCOPE: SubjectIntelligence/** only (artifacts/ +8, qa-reports/ +8, runs/SIB-CHEMISTRY_4CH1-RUN-003/ full receipts incl. pack specs + census annex + bodies + evidence-claim report, manifest BL-008 PASS-4 stamp, pipeline/sib_evidence_claim_qa.py, WORKLOG). Canonical planes untouched; sources stay canonical; mark_points untouched; zero DB writes; zero deploys; PAT one-shot helper (exposure +1).

Stage Summary:
- BL-008 PASS 4 LANDED OF RECORD: MIS family 9/9 COMPLETE (MIS-01 pilot + MIS-02..09), 17 artifacts GENERATED + QA_PASSED in the 4CH1 library. Queued per §4: pass 3 EXP + pass 8 TUT (book-text gate), pass 5 ASM+MS+EXM, pass 6 PED+PRA+PRO, pass 7 HIS (legacy digests), pass 9 GAP. Standing operator-side: curriculum-registry anchor repair, PAT rotation, student-book native-text upgrade decision.

---

Task ID: BL-008 pass 3 — EXP-01..08 (operator order "order pass 3 EXP" trace 1a174ae7817182b9, channel zai-web, session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)
Agent: main (Super Z, zai-web session web-1f157e25-0ed7-4f18-8956-3b2a993bc646)

Work Log:
- Fetch-first after context rollover (no sandbox loss this time; local clones survived): resources origin/main @ c15fc292 (pass-4 merge e481cb47 verified ancestor; +1 unrelated Wave-8 T3 physics-chemistry commit, zero path overlap); pastpapers read state 04df741d (remote advanced to 29d88249, images-only lanes — disclosed, not consumed); validator of record @ 357ace0a (master main HEAD = pin; sib-master private, anonymous ls-remote fails — disclosed).
- BLOCKER LIFTED OF RECORD: pass 3 was queued BLOCKED on student-book text extraction. The books-plane v3 OCR parse (books/CATALOG.md §3.1: 1,234 chunks, audit GREEN 2026-10-18, serving doc e6c0db50) is the text of record; source_manifest v1.2.3 registers parsed/edexcel_igcse_chemistry_chunks_v3.jsonl as SRC-BOOK-4CH1-SB1 evidence (sha256 b2c67eaf… pinned; tree_sha 5fad9de7… re-verified at main via git rev-parse). The Pearson eBook purchase decision remains open ONLY for the TUT/pass-8 native-text upgrade lane.
- PIPELINE INCREMENTS (disclosed, deterministic, in this change): evidence_pack.py r0->r1 — _jsonl_locate (bounded per-record excerpts from JSONL corpora; locator = line N · chunk <id>; no query = identity-only; caps enforced) + md_query compiled case-insensitively (uppercase-only headings must not gate selection); sib_evidence_claim_qa.py r1->r2 — family-general record blocks (r1 was MIS-only), .jsonl path grammar, page/line locator grammar with locator-kind quote binding, alternation order fixed (jsonl before json). Both py_compile clean; smoke-tested before run use.
- RUN SIB-CHEMISTRY_4CH1-RUN-004: preflight PASS for EXP (7/17 sources; 10 genuinely-absent corpora disclosed, never filled). 8 agent-authored pack specs + packs: EXP-01..08, 64 records EXP-001..064 (Core/Simple/Deep/Alternative Explanations, Analogies & Mental Models, Conceptual Distinctions, Why It Works, Common Why Questions). Book grounding: 279 bounded chunk excerpts across the 8 packs (15,068-39,316 chars/pack, caps enforced); spec grounding: bounded pages 17-29 per pack; TL identity-level; authoring FROM THE PACKS ALONE.
- GATES x8: structural (tools.sib.cli qa @ 357ace0a): 0 errors, 0 warnings x8; INFO SIB-ANCH-003 (no curriculum registry supplied to qa) disclosed — cleaner than the pass-4 SIB-ANCH-002 warning class; evidence-claim QA r2: 253 citations checked, 0 VIOLATIONS (every (SRC-*, locator) resolves to the artifact's own pack incl. JSONL line locators; per-record quote binding); educational review PASS on the five pilot criteria per artifact; staging/publication NOT REQUESTED (operator gates).
- IN-TURN REPAIR CYCLE (disclosed in run manifest): first claim-QA pass caught (1) spec anchors cited outside their artifact's pack (spec-page plans expanded; packs rebuilt), (2) an OCR Roman-numeral 'repair' inside a quoted fragment (rewritten as paraphrase per the never-repair law), (3) two quotes without formal citations of their containing chunks (citations added), (4) an unparseable 'pp. 20 and 21' locator (grammar form fixed). All repairs pre-record; final state is the first fully-green state.
- Ledger: BL-008 PASS 3 EXECUTED stamped (the earlier PASS 3 BLOCKED note marked SUPERSEDED in place, not deleted); run manifest validate OK with 4 run-level disclosures (pastpapers read-state, pipeline increments, repair cycle, SIB-ANCH-003 class).
- SCOPE: SubjectIntelligence/** only (artifacts/ +8, qa-reports/ +8, runs/SIB-CHEMISTRY_4CH1-RUN-004/ full receipts incl. pack specs + packs + census annex + evidence-claim report + run manifest, source_manifest v1.2.3, manifest BL-008 PASS-3 stamp, pipeline/evidence_pack.py + pipeline/sib_evidence_claim_qa.py, WORKLOG). Canonical planes untouched; sources stay canonical; mark_points untouched; zero DB writes; zero deploys; NO credentials used this session (all work anonymous-read + local).

Stage Summary:
- BL-008 PASS 3 LANDED LOCALLY OF RECORD on branch sib/bl-008-pass3-r0 @ (see commit): EXP family 8/8 COMPLETE (64 records), 25 artifacts now GENERATED+QA_PASSED in the 4CH1 library (CUR 8 + MIS 9 + EXP 8). Push/PR PENDING the operator one-shot PAT (sandbox holds no credentials by law; exposure protocol as before — no PAT was needed for this session's local execution). Remaining queue: pass 5 ASM+MS+EXM (evidence-unblocked), pass 6 PED+PRA+PRO, pass 7 HIS (BLOCKED on legacy 4CH0 sources), pass 8 TUT (native-text upgrade lane open via Pearson eBook decision), pass 9 GAP. Standing operator-side: curriculum-registry anchor repair (SIB-ANCH-002/003 class), PAT rotation.

---

## BL-008 PASS 5 — SIB-CHEMISTRY_4CH1-RUN-005 (ASM-01..10, MS-01..08, EXM-01..06) — 2026-10-26

- Operator order: "order pass 5" (trace 1a174f651acee035, channel zai-web, session web-1f157e25-0ed7-4f18-8956-3b2a993bc646). Branch sib/bl-008-pass5-r0 cut from main @ 367b5d61 (pass-3 merge of record).
- Fetch-first: resources main @ 367b5d61 (fleet Wave-9 + T-BOOK-057/058 + YPH11 polish in ancestry); pastpapers read-state advanced to f61a5baf (images-only placement waves — not consumed for claims, disclosed in run manifest source_revisions); validator of record @ 357ace0a unchanged.
- Preflight PASS for ASM/MS/EXM (7/17 sources resolved; the 10 known-absent corpora disclosed; SRC-ER-4CH0-LEGACY absent locally — EXM stays 4CH1-only with the legacy availability disclosed).
- Pipeline increment of record: sib_evidence_claim_qa.py r2 -> r3 — markdown-range locator grammar (pack md excerpts carry `lines N-M` locators; r2 indexed only JSONL `line N `, making the MS family's mandatory QPMS md grounding ungroundable). r3 indexes range locators by expanding N..M, expands `lines N-M` citation specs to the closed range, and normalizes multi-line citation payloads. No rule loosened: every requested line must still exist as a covered excerpt line. Regression-checked vs RUN-004 (253/0 unchanged) before use.
- 24 pack specs + packs built deterministically (scripts of record in the run receipts): QPMS md grounding via per-file md_query on the embedded mark-scheme text; ER grounding via commentary-zone pages [3-6] across 23 usable reports (garbled 2024-06 1C ER excluded of record); SPEC pages 9/13/14/17/35 for ASM-01/05/10. Per-source caps (60 exc / 1600 chars / 40k chars / 40 files) concentrate excerpts on the head of each interleaved file list — file order IS the session-spread decision (disclosed).
- AUTHORING: 24 artifacts authored FROM THE PACKS ALONE (6 records each; family-global record numbering ASM-001..060, MS-001..048, EXM-001..036 continuing the MIS/EXP law), stamped via generate_artifact.py (v2 provenance: provider z.ai / model GLM / agent_version SIB-GEN-r0; run SIB-CHEMISTRY_4CH1-RUN-005; source_revisions 367b5d61 / f61a5baf / 357ace0a).
- GATES: validator qa @ 357ace0a 0 errors / 0 warnings x24 (INFO SIB-ANCH-003 disclosed); evidence-claim QA r3 246 citations / 0 violations (first fully-green state); educational review PASS on the five pilot criteria per artifact; run manifest validate OK with 24 receipts + qa-reports x24 + census annex (4 run-level disclosures).
- FAIL-CLOSED REPAIR CYCLE (all pre-record, disclosed): initial claim-QA pass caught (1) multi-line citation payloads truncated by the parser (grammar normalized in r3), (2) 180 line-window misalignments from cross-pack authoring views (mechanical re-anchor to each artifact's OWN pack windows; 15 re-ranged, 56 page-verified, 16 dropped), (3) 19 unbound quotes (re-pointed to their own-pack windows or deleted — never paraphrased into existence), (4) one truncated-quote mis-pairing pattern (ellipsis-inside-quotes) restructured (EXM-025). The over-broad first requote attempt damaged bodies mid-turn — RESTORED from the stamped artifacts of record (byte-exact pre-requote state) before the precise 20-violation fixer ran; the restore is itself part of this disclosure.
- MS family boundary: all mark-scheme analysis is SIB evidence-grounding on the parsed mark-scheme text of record (SRC-QPMS-4CH1); the canonical mark_points plane was NOT read for writes and NOT written (family law + standing ban respected).
- SCOPE: SubjectIntelligence/** only (artifacts/ +24, qa-reports/ +24, runs/SIB-CHEMISTRY_4CH1-RUN-005/ full receipts incl. 24 pack specs + packs + census annex + evidence-claim report + run manifest, manifest BL-008 PASS-5 stamp, pipeline/sib_evidence_claim_qa.py r3, WORKLOG). Canonical planes untouched; zero DB writes; zero deploys; credentials used only for push/PR/merge via API transport after all local gates (operator one-shot PAT, never written to any file).
- Scoreboard: ASM 10/10 + MS 8/8 + EXM 6/6 COMPLETE; 49 artifacts now GENERATED+QA_PASSED in the 4CH1 library (CUR 8 + MIS 9 + EXP 8 + ASM 10 + MS 8 + EXM 6). Remaining queue: pass 6 PED+PRA+PRO, pass 7 HIS (BLOCKED on legacy 4CH0 sources), pass 8 TUT (Pearson eBook operator decision), pass 9 GAP. Standing: curriculum-registry anchor repair (SIB-ANCH-002/003 class), PAT rotation.

## 2026-10-26 — SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6: PED+PRA+PRO) — zai_agent lane

Operator order 'order pass 6' (trace 1a17755d4b4c9ce9, zai-web session
web-1f157e25-0ed7-4f18-8956-3b2a993bc646). Run SIB-CHEMISTRY_4CH1-RUN-006 =
PED-01..09 + PRA-01..05 + PRO-01..07 (21 artifacts, 135 records) through the
full SIB-GEN chain: preflight PASS (primaries SRC-TL-4CH1 + SRC-BOOK-4CH1-SB1 +
SRC-SPEC-4CH1 + SRC-QPMS-4CH1 RESOLVED; 10/17 sources resolved, 7 absent corpora
disclosed), 21 agent-authored pack specs + packs (every policy-selected source
planned per artifact — no auto-pulled entries; legacy sources riding the
SRC-ER-* demotion held to 1-page identity presence, never cited for CURRENT
claims), authoring from packs alone, validator QA @ 357ace0a 0 errors x21 /
0 warnings, evidence-claim QA r3 283 citations / 0 violations (in-turn repair
cycle disclosed: citation-window alignment, cross-pack locator drift,
combined-parenthetical splitting, ambiguous er.pdf dir-qualification, one pack
re-spec PRO-03), run manifest validate OK, BL-008 ledger stamped.

Scoreboard: 70 x GENERATED (CUR 8 + MIS 9 + EXP 8 + ASM 10 + MS 8 + EXM 6 +
PED 9 + PRA 5 + PRO 7). Every REQUIRED artifact of the 95-artifact taxonomy now
exists. Remaining queue: pass 7 HIS (7 OPTIONAL artifacts; sources RESOLVED
since GAP-SRC-002/BL-002 2026-10-25), pass 8 TUT (sources PRESENT since SB1 v3 +
SRC-TL-4CH1; operator eBook upgrade lane optional), pass 9 GAP (final audit,
runs last by design). Staging/publication remain operator-ordered.

## 2026-10-26 — SIB-CHEMISTRY_4CH1-RUN-007 (BL-008 pass 7: HIS) — zai_agent lane

Operator order 'order pass 7' (trace 1a177bcd9bdac8f1, channel zai-web). Run
SIB-CHEMISTRY_4CH1-RUN-007 = HIS-01..07, the taxonomy's 7 OPTIONAL artifacts, 42
records HIS-001..042 (family-continuous numbering).

- Fetch-first: resources main @ 4920c464 (the pass-6 merge of record; no advance),
  master @ 357ace0a pin unchanged, pastpapers @ 2cb92fe5; sibling PR #145
  (UGM-Resources CIE lane) verified ZERO SubjectIntelligence overlap from its own
  commit diff; sparse clones rebuilt fresh.
- Preflight PASS for HIS: primaries SRC-LEGACY-SPEC-4CH0 + SRC-ER-4CH0-LEGACY +
  SRC-SPEC-4CH1 all RESOLVED; 10/17 sources resolved, 7 absent corpora disclosed
  (none a HIS primary).
- Packs: 7 agent-authored pack specs (every policy-selected source planned per
  artifact): page-located excerpts from Issue 3 (Oct 2009), Issue 5 spec+SAMs
  (Feb 2015), 2009 SAMs booklet; five legacy ER sessions (2011-06 1C/2C, 2012-01
  1C, 2013-06 1C, 2016-06 1C/1CR, 2018-06 2C, 2019-01 1C) as LEGACY witnesses;
  current-spec statement/assessment pages; QPMS structural index + one live-window
  plan (2019-06 1C Q1). Survey cache outside the repo; page picks first-hand.
- Authoring from packs alone; every record carries LEGACY — HISTORICAL /
  CURRENT — AUTHORITATIVE labeling; temporal_scope current+legacy on all 7;
  family law honored (legacy observations never phrased as current truth).
- IN-TURN FIXES (disclosed): (1) pipeline amendment sib_evidence_claim_qa.py
  r3 -> r4 — case-insensitive citation-extension + pack-path matching; the
  Issue-5 file's uppercase .PDF was a fail-closed dead end (r2->r3 precedent
  class); (2) HIS-04 pack re-spec (I3 p7 added) for the Edexcel-imprint page;
  (3) quote verbatim-alignment: numbered topic-map lists, instruction-bullet
  't' markers, curly-quote token avoided by sub-span.
- QA CHAIN: validator qa @ 357ace0a 7/7 qa_passed, 0 errors / 0 warnings (INFO
  SIB-ANCH-003 registry note disclosed; qa-reports/ x7 written by the validator
  of record); evidence-claim QA r4 89 citations / 0 violations; census.json
  (sib-run-census/1.0, family HIS, per-source-class counters); run_manifest
  add-artifact x7 + validate OK (source_revisions: master 357ace0a, pastpapers
  2cb92fe5, resources 4920c464).
- LEDGER: manifest.yaml BL-008 description appended with the PASS 7 EXECUTED
  entry (YAML re-parse verified; library validate-manifest issue set unchanged
  vs pre-edit — 18x SIB-MANI-007 standing TUT/GAP state + pre-existing
  MANI-011/012 notes). Scoreboard: 77/95 artifacts GENERATED — every REQUIRED
  artifact plus the OPTIONAL HIS family complete. Remaining queue: pass 8 TUT
  (10 REQUIRED; sources PRESENT; eBook upgrade optional), pass 9 GAP (last by
  design). Staging/publication remain operator-ordered.

## 2026-10-26 — SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8: TUT) — zai_agent lane

Operator order 'pass 8 TUT' (trace 1a1781fd0f57ada1, channel zai-web). Run
SIB-CHEMISTRY_4CH1-RUN-008 = TUT-01..10, the 10 REQUIRED Tutor Intelligence
artifacts, 60 records TUT-001..060 (family-continuous numbering).

- Fetch-first after sandbox recycle: resources main @ 7ff30654 (pass-6 and
  pass-7 merges of record in ancestry; sibling UGM PR #145 merged 2026-10-25,
  zero SubjectIntelligence overlap), master @ 357ace0a pin unchanged (= main
  tip), pastpapers @ 2cb92fe5; sparse clones rebuilt fresh (resources cone:
  SubjectIntelligence + books + Official-Specifications/igcse-chemistry;
  pastpapers non-cone: 4ch1 er.pdf only — 24 reports of record materialized).
- Preflight PASS for TUT: primary SRC-BOOK-4CH1-SB1 RESOLVED with both declared
  sha256 digests matched (student-book.pdf d48020e0…, chunks_v3.jsonl
  b2c67eaf…); SRC-SPEC-4CH1 also RESOLVED; 6/17 sources resolved, 11 absent
  corpora disclosed run-wide (none a TUT primary). SRC-SPEC-4CH1 x TUT
  feeds_families instantiation gap (v1.2.3 does not list TUT) disclosed in the
  run receipts; the machine-readable evidence_policy governs pack composition
  (RUN-006 precedent).
- Packs: 10 agent-authored pack specs (every policy-selected resolved source
  planned per artifact — no auto-pulled entries; two disclosed in-turn repair
  waves to that posture before any authoring: auto-pull suppression re-spec of
  all 10, then TUT-07 SB1 identity entry + TUT-10 ER presence entry; TUT-01 ER
  window extended for one corroborating 2024-11 citation). SB1 chunks cited by
  line+chunk locators; TL/ER/SPEC by page locators; caps enforced by the pack
  builder; census annex (sib-run-census/1.0, per-source-class counters).
- Authoring from packs alone; all 60 records CURRENT — AUTHORITATIVE (TUT
  legacy: none); tutor guidance grounded on the validated book spine per the
  family forbidden-law; OCR-garbled spans avoided by clean sub-span quoting
  (never-repair law).
- QA CHAIN: validator qa @ 357ace0a 10/10 qa_passed, 0 errors / 0 warnings
  (qa-reports/ x10 written by the validator of record); evidence-claim QA r4
  94 citations / 0 violations FIRST-PASS (no repair cycle — the runs 5-6
  citation-window failures were prevented by per-artifact pull-before-author);
  educational review PASS on the five pilot criteria per artifact; run manifest
  add-artifact x10 + validate OK (source_revisions: resources 7ff30654,
  pastpapers 2cb92fe5, master 357ace0a).
- LEDGER: manifest.yaml BL-008 description appended with the PASS 8 EXECUTED
  entry (YAML re-parse verified). Scoreboard: 87/95 artifacts GENERATED —
  every REQUIRED artifact plus the OPTIONAL HIS family complete except the GAP
  audit. Remaining queue: pass 9 GAP (8 REQUIRED — final audit, runs last by
  design). Staging/publication remain operator-ordered.
## 2026-10-26 — SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9: GAP) — zai_agent lane

Operator order 'order pass 9' (trace 1a17834d3ae5d5c1, channel zai-web). Run
SIB-CHEMISTRY_4CH1-RUN-009 = GAP-01..08, the 8 REQUIRED Gap Intelligence
artifacts (the final audit pass — runs last by design), 48 records
GAP-001..048 (family-continuous numbering).

- Fetch-first: resources main @ 6ef8c892 (the pass-8 merge of record, PR #166
  in ancestry), master @ 357ace0a pin unchanged, pastpapers @ 2cb92fe5;
  sparse cone unchanged (SubjectIntelligence + books +
  Official-Specifications/igcse-chemistry).
- Preflight PASS: GAP primary SRC-SPEC-4CH1 RESOLVED with declared digest
  matched; 6/17 sources resolved, 11 failed sources disclosed run-wide (same
  posture as RUN-006/007/008 — none is the GAP primary).
- Packs: 8 agent-authored pack specs. GAP law: primary SRC-SPEC-* + forbidden
  'gaps closed by invention rather than disclosure'; supplementary '*' selects
  ALL SIX resolved sources, so every pack explicitly plans all six —
  SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1 ride as one-page
  identity-presence entries consumed for identity claims only (root-copy law
  + SAMS identity law honored). GAP-03 carries the full 23-report ER census
  (every clean cover of record, deliberately without the garbled 2024-06 1C
  exclusion). GAP-03's SB1 query ('EXAM HINT') matched no chunk text — the
  parse v3 content-type label is not chunk text — entry resolved identity-only,
  disclosed, consumed for no claim.
- Authoring from packs alone with the family forbidden-law enforced in-text:
  every coverage gap is DISCLOSED (SRC-GRAPH-4CH1 absence grounds GAP-02 at
  source level; unaudited spans labeled unaudited; 17-of-23 report sampling
  labeled as sampling). 48 records all CURRENT — AUTHORITATIVE.
- QA CHAIN: validator qa @ 357ace0a 8/8 qa_passed, 0 errors / 0 warnings
  (qa-reports/ x8 written by the validator of record); evidence-claim QA r4
  120 citations / 0 violations FINAL after one disclosed in-turn repair cycle
  — the first pass reported 13 violations, every one a citation pointing
  outside its own artifact's pack window (GAP-02 SB1 line 8 + spec p29; GAP-04
  TL covers + ER 2019-06 1C cover + spec p15; GAP-05 SB1 1100/1078 + 2024-06
  2C cover; GAP-06 ellipsis quote-pairing artifact; GAP-08 fitz column-order
  reflow of the change-summary table) — all re-pointed to in-pack locators
  before any record was committed; deterministic rebuild; sha256s of record
  in census.json (sib-run-census/1.0).
- LEDGER: manifest.yaml backlog BL-009 description appended with the PASS 9
  EXECUTED entry (operator order 'order pass 9' trace 1a17834d3ae5d5c1); YAML
  re-parse verified. Scoreboard: 95/95 artifacts GENERATED — the 95-artifact
  SIB taxonomy for CHEMISTRY_4CH1 is COMPLETE (CUR 8 + MIS 9 + EXP 8 + ASM 10
  + MS 8 + EXM 6 + PED 9 + PRA 5 + PRO 7 + HIS 7 + TUT 10 + GAP 8). No
  remaining generation queue. Staging/publication remain operator-ordered.

## 2026-10-26 — SIB-CHEMISTRY_4CH1-RUN-010 (BL-010 pass 10: external-review remediation) — zai_agent lane

Operator order 'open the remediation pass (RUN-010) starting with items 1-2' (trace
1a178e533eaa1b81, channel zai-web). Run SIB-CHEMISTRY_4CH1-RUN-010 = the remediation
pair ASM-10 v1.1 + MIS-01 v1.1, arising from the operator-supplied external review of
the 95-artifact library (both P0 findings verified against main @ 295fb5b before any
edit).

- Verified defects of record: ASM-10 claimed Topic 1 carries SEVEN named sub-topics —
  its own evidence excerpt was truncated mid-word at '(g) Cov' and the count was taken
  from the truncated window; the official p17 list runs (a) States of matter through
  (i) Electrolysis (nine), matching CUR-01's S1-a..S1-i and the registry census
  (28 = 9+8+3+8). MIS-01 claimed '24 reports across the 8 sessions' while listing
  SEVEN sessions and counting the garbled 2024-06 1C file; the census of record
  (RUN-009 GAP-03) is 23 clean reports across seven sessions — re-verified at source
  against the materialized pastpapers tree @ 2cb92fe5 (24 physical er.pdf holdings,
  4+4+4+2+4+2+4).
- Fetch-first: resources main @ 295fb5b6 (unchanged from assessment clone), master
  @ 357ace0a pin unchanged, pastpapers @ 2cb92fe5. Sparse cones: SubjectIntelligence +
  Official-Specifications/igcse-chemistry + Official-ExamQuestion/igcse-chemistry-19
  (new for this run: ASM-10's QPMS citations) + pastpapers 4ch1 er.pdf-only sparse.
- Preflight PASS: 6/17 sources resolved, 11 absent corpora disclosed run-wide (same
  posture as RUN-006..009); ASM primaries RESOLVED (SRC-SPEC-4CH1 declared sha1
  matched; SRC-QPMS-4CH1 tree_sha verified; SRC-SAMS-4CH1 RESOLVED), MIS primaries
  RESOLVED (SRC-ER-4CH1 tree_sha verified; SRC-QPMS-4CH1).
- Packs: 2 agent-authored pack specs, every policy-selected resolved source planned
  explicitly (no auto-pulled entries). ASM-10: spec p17+p35; 7 QPMS paper files with
  targeted marker-window queries landing the exact cited locators (2019-06 2C
  lines 223-237 + 230-244; 2019-06 1CR 309-323; 2020-01 2C 69-83; 2020-11 1CR 129-143;
  2022-01 1CR 184-198; 2023-01 1CR 133-147; 2022-06 2C 186-200) so ASM-059's
  'seven of its held paper files' holds of the RUN-010 pack; SAMS + TL one-page
  identity-presence covers. MIS-01: the 23 clean ER reports (identity covers + p3
  introductions; June-2023 1C p6 and June-2025 1C pp4-5 deep pages), QPMS identity row
  (MULTI-SERIES-REPORT.md head), TL identity cover. Pack sha256s of record in the run
  manifest.
- Pre-author verification (fail-closed, before packs): every quote the remediated
  artifacts carry was checked against its cited page/window of the materialized
  sources. 6 candidate mismatches resolved before any pack was built: 2 checker
  session-mapping errors; 2 cross-document ellipsis spans (MIS-004's 'an on-going
  issue' grounds on the co-cited 2023-06 2CR p3); 2 quotes union-grounded on the
  correct co-cited page (MIS-008's practical-work quotes on 2023-06 1CR p3). NO
  attribution errors found in the v1.0 record quotes.
- Authoring from packs alone (surgical): ASM-10 — Exec Summary + ASM-055 count 7 -> 9
  with the full nine-item list quoted; ASM-059 examples upgraded to line-located
  windows (same files, same claim); Source Basis notes the full-list quote; Research
  Status carries the remediation record. MIS-01 — Scope/Source Basis/Limitations
  census statements aligned to 23 clean / seven sessions with the garbled-1C exclusion
  disclosed; all 12 records' substance byte-stable with citations upgraded from the
  wave-1 prose form '(er.pdf p3) - SRC-ER-4CH1:' to the r4 binding grammar
  '(SRC-ER-4CH1, <session>/<paper>/er.pdf pN)' (same sources, pages and quotes).
- QA CHAIN: validator qa @ 357ace0a — ASM-10 0 errors / 0 warnings; MIS-01 0 errors /
  23 warnings (the pre-existing SIB-ANCH-002 anchor-registry degradation disclosed
  since RUN-003: registry points live under spec_point_codes while the validator's
  loader reads specification_points/identifiers; reported, not repaired);
  qa-reports/ x2 written by the validator of record. Evidence-claim QA r4: 38
  citations / 0 violations FIRST-PASS (10 ASM-10 + 28 MIS-01). Educational review
  PASS: corrected claims re-verified against the sources of record. Run manifest
  add-artifact x2 + validate OK (source_revisions: resources 295fb5b6, pastpapers
  2cb92fe5, master 357ace0a).
- LEDGER: manifest.yaml BL-008 description appended with the PASS 10 EXECUTED entry
  (YAML re-parse verified). Scoreboard: 95/95 artifacts GENERATED with ASM-10 + MIS-01
  corrected at v1.1. Remediation queue remaining (operator-ordered, not yet
  scheduled): claim-type labels for the MIS family why-it-occurs/intervention
  sections; authority-stamp vocabulary definition; manifest.yaml notebook-field/status
  hygiene; coverage-status field; run-record publication posture; EXP-06 <-> TUT-08
  cross-family seam reference. Staging/publication remain operator-ordered.

## 2026-10-27 — SIB-CHEMISTRY_4CH1-RUN-011 (BL-011 pass 11: remediation-queue items 3-8) — zai_agent lane

- OPERATOR ORDER: 'items 3-8 of the remediation queue' (channel zai-web; the queue
  filed by the external-review assessment). Item 3 = MIS-family claim-type labels;
  item 4 = authority/classification vocabulary definitions; item 5 = manifest.yaml
  hygiene; item 6 = coverage-status field; item 7 = run-record/pack publication;
  item 8 = EXP-06 <-> TUT-08 seam cross-references. Items 1-2 were closed by
  RUN-010 (73d1c1a2).
- PREFLIGHT: run SIB-CHEMISTRY_4CH1-RUN-011 initialized (provider z.ai / GLM /
  SIB-GEN-r0; source_revisions resources a7a34cd9, pastpapers 2cb92fe5 — re-verified
  UNCHANGED from the RUN-010 pin, zero source drift, master 357ace0a). Families
  MIS/TUT/EXP: gate PASS (6/17 sources resolved — SRC-ER-4CH1 + SRC-QPMS-4CH1 +
  SRC-SPEC-4CH1 + SRC-SAMS-4CH1 + SRC-TL-4CH1 + SRC-ROOT-BOOK-COPIES-4CH1; 11 absent
  corpora disclosed run-wide incl. SRC-BOOK-4CH1-SB1 identity-only, per the RUN-010
  posture). resources base advanced 295fb5b -> a7a34cd9 mid-cycle (sibling maths-B
  serve-hygiene wave PR #165): diff vs RUN-010 merge on SubjectIntelligence/ is
  EMPTY — zero path overlap, fetch-first verified.
- EVIDENCE: grounding packs carried over BYTE-IDENTICAL from the origin runs
  (MIS-01: RUN-010; MIS-02..09: RUN-003; TUT-08: RUN-008; EXP-06: RUN-004) with
  every pack sha256 cross-checked against the origin run manifest receipt — items
  3-8 alter claim labels, governance files and cross-references only; zero new or
  altered source claims, so the packs of record are reused, not rebuilt.
- ITEM 3 (claim-type labels): legend block inserted in all 9 MIS artifacts defining
  OBSERVED_IN_SOURCE / SIB_INFERENCE / PROPOSED_INTERVENTION; field labels tagged
  family-wide — OBSERVED_IN_SOURCE x106 (Evidence 70, Motivating evidence 14,
  Examiner guidance 22), SIB_INFERENCE x126 (Why it occurs 49, Why the reasoning
  fails 7, Diagnostic signals 49, Signal tested 7, Fail pattern 7, Pass pattern 7),
  PROPOSED_INTERVENTION x49 (Intervention ideas 20, Intervention note 1,
  Intervention 7, Drill design 7, Success signal 7, Probe 7). Citation tokens
  byte-identical pre/post edit (enforced by the QA grammar regex). MIS-01 v1.2;
  MIS-02..09 v1.1. One in-turn repair disclosed: the EXP-06 seam's first draft
  quoted the TUT-046 title and was rejected by the r4 quote-binding law
  (1 violation); re-phrased without quote marks, re-run clean — the quote-binding
  gate working as designed on cross-artifact references.
- ITEM 4 (vocabulary definitions): SOURCE_REQUIREMENTS.md section 4.1 added —
  definitions of record for CURRENT — AUTHORITATIVE / CURRENT — ASSESSMENT EVIDENCE /
  SUPPLEMENTARY / LEGACY — HISTORICAL / RESEARCH / INFERRED (the 547-occurrence
  undefined-stamp finding) + the three claim-type labels.
- ITEMS 5+6 (manifest hygiene + coverage-status): header comment refreshed to the
  95/95 GENERATED state with the validator's empty-status law stated; notebook field
  reduced to the clean id (provisioning supersession noted per BL-003); top-level
  coverage_status block added (generated / families / disclosed_absent_sources /
  publication / updated) — unknown-top-level-key tolerance of the validator of
  record verified in tools/sib/manifest_model.py first. YAML re-parse verified.
- ITEM 7 (run-record/pack publication): CLOSED AS VERIFIED-OF-RECORD — the
  assessment-stage 'runs untracked' claim was corrected during RUN-010: runs
  RUN-001..010 with manifests, packs, bodies, censuses and preflight receipts are
  committed in-repo. runs/README.md added documenting the publication convention.
- ITEM 8 (family seam): TUT-08 (TUT-046) and EXP-06 (EXP-045) gained explicit
  cross-family seam lines for the strong-versus-weak-versus-concentrated duplication
  (same book passage, chunks line 1006); no new source citations introduced. Both
  artifacts v1.1.
- QA CHAIN: validator qa @ 357ace0a — 0 errors x11 (MIS warnings = the pre-existing
  SIB-ANCH-002 anchor-registry degradation, reported not repaired; TUT-08 + EXP-06
  0 warnings); qa-reports/ x11 written by the validator of record. Evidence-claim
  QA r4: 149 citations / 0 violations (the carried packs bound into the run dir).
  census.json annex + run manifest add-artifact x11 + validate OK.- LEDGER: manifest.yaml BL-008 description appended with the PASS 11 EXECUTED entry

## RUN-012 — SIB-ASSESS-r1 disclosure-truth repair + editorial nits (2026-10-27, BL-011 pass 12)

- Operator order: 'Proceed with RUN-012' (channel zai-web, trace 1a179c02d2750cf9).
  Scope of record: SIB-ASSESS-r1 finding D1 (manifest.yaml coverage_status
  materially misdescribed the corpus state) + finding D5 (editorial nits).
- D1 repair: coverage_status rewritten to the verified per-source state —
  grounding_consumed (11 classes incl. SRC-BOOK-4CH1-SB1's validated v3 parse,
  NOT identity-only), disclosed_not_consumed (6 classes, corpora present in-repo,
  never resolved by any SIB preflight, never pack-consumed), correction_of_record
  (the RUN-011 line was wrong; 6/17 preflight counts are sparse-clone surfaces).
- D5 repairs: TUT-08 v1.2 — the hydration-route conditions were presented as
  quotes but the book prints them as separate label/value lines
  ('Catalyst:' / 'phosphoric acid (H3PO)'); re-phrased as the paraphrase it is,
  citation tokens byte-identical. PRO-01 v1.1 — broken Purpose sentence repaired
  ('decision frameworks. Grounding: ...'). EXM-01 v1.1 — stray space before a
  colon in the Purpose. Parse-plane observation DISCLOSED, not repaired: chunk
  990 prints the phosphoric-acid formula as H3PO (book data tables print H3PO4)
  — books-plane parse lane's to adjudicate.
- Chain: preflight PASS (families TUT/EXM/PRO; 6/17 sources resolved on the
  sparse-clone surface, 11 disclosed run-wide), packs carried byte-identical from
  origin runs (TUT-08 <- RUN-011, EXM-01 <- RUN-005, PRO-01 <- RUN-006; sha256s
  cross-checked vs origin receipts), stamping x3, validator qa @ 357ace0a
  0 errors x3 / 0 warnings, citation QA r4 27 citations / 0 violations, census
  annex + run manifest add-artifact x3 + validate OK.
- SCOREBOARD: 95/95 artifacts GENERATED — 92 at prior versions-of-record,
  TUT-08 v1.2, EXM-01 v1.1, PRO-01 v1.1 (RUN-012). Staging/publication remain
  operator-ordered. SIB-ASSESS-r1 register: D2 anchor-registry repair (133x
  SIB-ANCH-002) and D4 derived-quantity labeling remain open lanes.

  (YAML re-parse verified). REMEDIATION SCOREBOARD: all 8 external-review queue
  items CLOSED (1-2 by RUN-010, 3-8 by RUN-011). 95/95 artifacts GENERATED:
  93 at v1.0/v1.1-of-origin, ASM-10 + MIS-01 v1.1 (RUN-010), MIS-01 v1.2 +
  MIS-02..09 v1.1 + TUT-08 v1.1 + EXP-06 v1.1 (RUN-011). Staging/publication remain
  operator-ordered.

## RUN-013 — D2 anchor-registry repair (2026-10-27, BL-011 pass 13)

- Operator order: 'D2 anchor-registry repair' (channel zai-web, trace 1a179cf5322a1b81).
  Scope of record: SIB-ASSESS-r1 finding D2 — 133x SIB-ANCH-002, unrepaired since
  RUN-003.
- Diagnosis of record (scripts/run013_diagnose.py): the 133 warnings decompose
  into (a) a registry-LOADER defect — curriculum_registry.yaml stored its ids
  under `spec_point_codes` in a `4CH1-`-prefixed namespace, but the validator
  loader (tools.sib.cli::_registry_ids) reads only `specification_points`/
  `identifiers` and the anchor extractor's namespace is bare-only — so the
  registry was silently ABSENT for every qa of record (SIB-ANCH-003 x95); and
  (b) an artifact-side defect — of the 32 unique referenced ids, 5 bare forms
  (1.5, 1.6, 1.7, 3.5, 3.14) are absent from the 182-point universe of record
  because the official statements are C-suffixed (Chemistry-only): 1.5C/1.6C/
  1.7C (solubility), 3.5C (energy level diagrams), 3.14C (reaction profiles).
  Official-spec PDF verified as the court of record: plain 1.5/1.6/1.7/3.5/3.14
  do NOT exist in 4CH1.
- Registry repair (zero invention): re-pinned to the loader contract —
  `specification_points:` = 234 quoted ids = the 182 official_code identifiers
  of record at pin tree f42033e01de3 (zero drift vs origin/main verified) + 52
  documented bare projections of the C-codes (unambiguity verified: no number
  exists both plain and C-suffixed). Legacy `spec_point_codes` block preserved.
  pyyaml + yamlmini(stdlib path) agree; loader view = 234; build_registry
  present.
- Artifact repair (per-record adjudication, NOT C-blind restoration): 13 anchor
  lines re-anchored across MIS-01/02/04/06/07/08 — the records' content maps to
  1.1 (arrangement/movement/energy of particles), 1.2 (interconversions),
  3.11 (collision theory), 1.25 (word + balanced equations incl. state symbols)
  and 3.14C; the old refs cited nonexistent plain-form points, wrong-locus
  points (3.3/3.5 = Q=mcΔT/energy-diagram statements; 1.21/1.22 = Periodic
  Table points), or dropped the C suffix. Per-record rationale committed at
  runs/SIB-CHEMISTRY_4CH1-RUN-013/evidence/anchor_reanchor_receipt.json.
- Chain: preflight PASS (families MIS/PRA; 6/17 sources resolved on the
  sparse-clone surface, 11 disclosed run-wide), packs carried byte-identical
  from RUN-011 (sha256s cross-checked vs origin receipts), stamping x6
  (MIS-01 v1.3; MIS-02/04/06/07/08 v1.2), validator qa @ 357ace0a 0 errors /
  0 warnings x6 edited + 89 unchanged receipts refreshed — 95/95 receipts at
  0 errors / 0 warnings, the first warning-free library sweep since RUN-003
  (anchor refs resolve as SIB-ANCH-004 INFO; the 2 pre-existing SIB-IDENT-005
  filename-canonicalization INFOs remain, out of D2 scope), citation QA r4
  79 citations / 0 violations, census annex + run manifest add-artifact x6 +
  validate OK.
- SCOREBOARD: 95/95 artifacts GENERATED — 89 at prior versions-of-record,
  MIS-01 v1.3, MIS-02/04/06/07/08 v1.2 (RUN-013). Staging/publication remain
  operator-ordered. SIB-ASSESS-r1 register: D4 derived-quantity labeling and
  D6/D7 (structural limits; staging/publication pass) remain open lanes.

---

## RUN-014 — SIB-ASSESS-r1 D4: derived-quantity labeling (BL-011 pass 14)

**Date:** 2026-10-27
**Operator order:** "D4 (derived-quantity labeling)" (channel zai-web, trace
1a17c30ca2b54219)
**Run:** SIB-CHEMISTRY_4CH1-RUN-014
**Status:** COMPLETE — QA_PASSED, receipts validated

**Scope.** The assessment's D4 finding: derived-quantity provenance gap — unquoted
numeric figures whose printed/derived/estimated status a reader cannot tell
(exemplar: "about 1 in ~75" in EXP-045, presented as a bare parenthetical).

**Diagnosis of record.** Char-level quote-span-masked sweep of all 95 artifacts:
225 unquoted-figure hits / 78 distinct figure sites. Every site verified against
its artifact's evidence packs (union across runs) and the book chunk corpus
(chunks_v3.jsonl, sha b2c67eaf...). Verdicts: the overwhelming majority
SOURCE-PRINTED with record-level or same-sentence binding (spec assessment
weightings 61.1/38.9, AO bands and per-paper matrix, legacy 66.6/33.3 and AO
bands, Haber 450 C / 200 atm — the legacy spec's own wording, TL guide's 0.20 cm3
concordance and 15 % pass yield, 2.67 g / 90.0 g / -1.8 C calorimetry figures,
11.00 cm3 / 0.05 cm3 reading rules, QP stem 77.78/22.22, ER's 0.00125, boron
20/80, 600 m/s / 0.01 s, 35.5/18.5, 36.5, -0.6/100.2 — the last two with the
book's own hedges). Exactly one RUN-COMPUTED census and one approximation found:
- CUR-02 demand-class percentage: 33.2% claimed, 60/181 = 33.1% per the RUN-002
  census of record (command_kinds.guide_class_distribution) — arithmetic rounding
  error; the RUN-COMPUTED derivation labels were already in place.
- EXP-045 "pH around 3-5": printed by no source (the book's printed figure is
  2.88 for 0.10 mol/dm3 ethanoic acid, chunk 571 — already in the same record).
- EXP-045 "about 1 in ~75": book-printed verbatim (chunk 1006) but presented as
  an unlabeled parenthetical.

**Repairs.** CUR-02 v1.1 (33.2% -> 33.1% x2); EXP-06 v1.2 (EXP-045 "the book's own
figure: about 1 in ~75 ..." attribution; the 3-5 band labeled as an approximate
band pointing at the printed 2.88). Citation tokens byte-identical pre/post for
the D4 edits.

**In-turn disclosed repair.** The r4 citation QA fail-closed on CUR-02 with 34
violations — on the UNEDITED base artifact too (verified at d4958105): the CUR
family was generated at RUN-002 before the r4 binding grammar existed and was
never re-gated. Repair (RUN-010 precedent): CUR-02's 31 tokens upgraded to the
r4 grammar — pack file paths inserted (spec_command_kinds.yaml /
specification_points.yaml / the spec PDF, per the pack excerpt locators covering
each cited range), semicolon-joined multi-citations split one-per-paren, "page N"
-> "pN", the census-mixed token split into citation + standalone RUN-COMPUTED
label. Sources/pages/line-ranges unchanged in substance. Post-repair: 54 tokens,
81 citations / 0 violations across the run's artifacts. Register note: the same
pathless citation style remains in CUR-03..08/GAP-family artifacts (outside this
run's edit scope) — library citation-grammar debt for a dedicated pass.

**Chain.** init RUN-014 -> preflight PASS (families CUR, EXP; 6/17 sparse-surface
resolved, 11 disclosed run-wide) -> packs x2 byte-identical (CUR-02 <- RUN-002;
EXP-06 <- RUN-011, chain-verified byte-identical to the RUN-004 origin) -> D4
edits + citation-grammar repair -> stamp x2 -> validator qa @ 357ace0a 0 errors /
0 warnings x2 edited + 93 unchanged receipts refreshed = 95/95 clean (library
holds the RUN-013 clean state) -> citation QA r4 81 citations / 0 violations ->
census annex -> add-artifact x2 + validate OK -> governance (this entry,
manifest.yaml header/coverage_status/BL-008 PASS 14 stamp,
SOURCE_REQUIREMENTS.md section 4.2 labeling law of record).

**Receipts.** runs/SIB-CHEMISTRY_4CH1-RUN-014/: run_manifest.json (validated),
evidence/d4_adjudication.json (3 repaired sites + 15 no-action figure families
with source pins), evidence/citation_repair_receipt.json, census.json,
evidence_claim_qa_report.json, preflight/).

---
## RUN-015 — CUR/GAP citation-grammar pass + the 7 OPTIONAL-HIS backlog artifacts + docs self-improvement (2026-10-27)

Operator order: "Proceed with CUR/GAP citation-grammar pass, and the 7 OPTIONAL-HIS
backlog artifacts. And also remember to update the docs of the SubjectIntelligence
folder, so that in the future when we add sib docs for other subjects, we wont face
all these problems. Basically a self improving pipeline" (channel zai-web, trace
1a17cb11a9858229; continuation traces 1a17d7ec94b4a7cd, 1a17e102c5190241).

**Stage A — citation-grammar pass (the RUN-014 register item).** Fetch-first caught
origin/main 6b9fe7d -> d9c94436 (4MB1/G9 lane; SubjectIntelligence diff EMPTY,
isolation proven, advance_disclosure.json filed; local main FF'd). Census of record:
131 pathless citation tokens across CUR-03..08 (GAP-01..08 already path-conformant).
Repair: r4 grammar upgrade (pack file paths per covering pack excerpt locators;
one-citation-per-paren splits; 'page N' -> 'pN'; prose hedges moved out of parens;
the CUR-07 chained 'through' connector dropped), 2 prose-paren hidden pathless forms
repaired, 4 CUR-08 multi-cover ranges content-adjudicated (51-65/93-107/141-155 ->
specification_points.yaml; 86-100 -> practicals.yaml). Pack re-specs (RUN-007
precedent, disclosed): CUR-06 +3 windows (152-166, 2779-2793, 3597-3611) and CUR-05
+1 window (8-22 direction contract) as surgical appends byte-built per _md_locate
rules — the full-rebuild path was PROVEN surface-unstable (select_sources swapped
BOOK->LEGACY-SPEC) and the HIS path was proven byte-stable by probe; the probe-then-
choose law is now in the register. First-time r1 quote-binding gating of the
RUN-002-era CUR family fail-closed at 7 + 3 violations across two rounds; 11 repairs,
all verbatim-verified (2 paraphrase-in-quotes restored, 2 injected-comma quotes
restored, 1 truncated quote completed, 1 contract quote completed with YAML
''-escaping and re-pointed to the true meta window, 1 false excerpt-cap narrative
removed, 1 policy wording de-quoted, 1 nested-quote restored, 1 MCQ quote split into
the store's own command-word + definition strings). CUR-03..08 stamped v1.1.
GAP-01..08 re-gated confirm-only: 120 citations / 0 violations — the RUN-014
register note's GAP mention retired.

**Stage B — the 7 OPTIONAL-HIS backlog artifacts (SIB-ASSESS-r1 D3 backlog).**
HIS-01..07 stamped v1.1: 28 new records (HIS-043..070; record-id continuity HIS-043..070
verified) grounded in widened legacy ER windows (SRC-ER-4CH0-LEGACY from 1-8 pages to
5-18 pages per artifact across up to 16 sessions, 2011-2019): documentary lineage
(HIS-01 cover series: Edexcel -> Pearson Edexcel imprint migration + the Level 1/Level 2
Certificate co-branding window + the 2013-2017 CR-variant window), demand-grammar
witnesses (HIS-02), assessment behaviour (HIS-03: embedded MCQs, mark-allocation-as-
detail-signal, AO doctrine, live mark-scheme adaptation), terminology policing
(HIS-04), question craft (HIS-05), pack-internal persistence pairs 2013->2019 (HIS-06),
technique relevance (HIS-07). Every quote verbatim-verified against the pack excerpts;
the 42 original records unchanged; packs rebuilt deterministically with byte-identity
proofs on every pre-existing excerpt.

**Stage C — the self-improving pipeline.** docs/LESSONS_REGISTER.md added (the
operational laws of record: session preflight, locator/quote grammar, pack caps +
re-spec law, run mechanics, git phase, debt discipline, 10 earned lessons with run
ids); PIPELINE.md r1 §8 (binding per-run laws pointer); COURSE_ONBOARDING.md §7
(onboarding-time hygiene checklist); README.md pointer. Future course libraries
inherit the laws instead of re-deriving them.

**Chain.** preflight PASS (families CUR/GAP/HIS; 9/17 resolved on the sparse surface —
legacy primaries SRC-LEGACY-SPEC-4CH0 + SRC-ER-4CH0-LEGACY live, stronger than the
RUN-012..014 6/17 state) -> packs carried (CUR/GAP <- origins byte-identical; HIS <-
RUN-007 base) -> Stage A/B packs -> stamps v1.1 x13 -> validator qa @ 357ace0a
0 errors / 0 warnings — 95/95 receipts clean -> citation QA r4: CUR 210 + GAP 120 +
HIS 138 citations / 0 violations -> run manifest add-artifact x13 + validate OK ->
governance (this entry, manifest.yaml header/coverage_status/BL-008 PASS 15 stamp) ->
validate-manifest + full live sweep. Register: D6 (single-pipeline self-attestation
structural limit) and D7 (staging/publication pass — 0 STAGED) remain operator-ordered.

---

## RUN-016 — the D7 staging/publication pass (pass 16, BL-011) + SIB-ASSESS-r2 (2026-10-28)

Operator order "Go" (trace 1a17eb6123855fc9) on the queued backlog: the honest
post-repair re-assessment, then the D7 pass it gates.

**SIB-ASSESS-r2** (`ASSESSMENT_R2_2026-10-28.md`, commit 1 of this lane): four
instruments — metrics (95/12 fams; 129,788 words +4,726, 644 records +28, 1,588
citations +185 vs the r1 baseline), the r3 evidence-claim gate swept over **94/95
artifacts** against the latest pack of record (1,514 citations / 0 violations;
CUR-01 the one fail-closed skip — RUN-001 predates the census-annex law), live
validator qa **95/95 at 0 errors / 0 warnings with receipts byte-identical across
sessions** (determinism proven), repair-hold probes + the HIS-066 human spot-read.
Verdict: every r1 repair HELD (D1/D2/D4/D5, CUR/GAP grammar, HIS quote binding); new
findings **D8** (6 grammar-form debt tokens that pass the gate — prose-parens in
CUR-05/CUR-08, semicolon-joined pairs in PRO-07, prose locators in EXP-01), **D9**
(CUR-01's 5 debt forms + never-gated), **F4** (structural: the manifest validator
models the landing lifecycle only); **GO**.

**RUN-016**: pre-stage repairs first (post-publication repairs would burn artifact
versions) — 11 exact-match edits across CUR-01 v1.1, CUR-05 v1.2, CUR-08 v1.2,
PRO-07 v1.1, EXP-01 v1.1, every new locator pack-verified, **CUR-01 gated for the
first time in the library's history** (census annex built from its RUN-001 pack of
record); validator qa 0/0 x5 + 95/95 receipt refresh; citation QA r4 **120 citations
/ 0 violations**; then the lifecycle: **stage x95 -> publish x95 -> chunks x95**
(1,404 deterministic retrieval chunks; artifacts/ landing zone EMPTY by design;
95x PUBLISHED; lifecycle_receipt.json). F4a/F4b structural disclosures filed with
the exact post-lifecycle scoreboard (88x MANIFEST_MISSING_REQ — the scoreboard
cannot model the state it certifies; OBSERVED + DISCLOSED, never worked around;
lesson 12 appended to docs/LESSONS_REGISTER.md). Advance disclosures x2 (both
SubjectIntelligence-isolated). **D7 CLOSED — the library is servable.**

Register: D3 (REQUIRED-core depth ceiling), D6 (single-pipeline self-attestation
limit), the F4 upstream validator fix, and the independent silver-tier ER review
before production reliance remain operator-ordered.

## RUN-017 — D3 REQUIRED-core depth pass, tranche 1: EXM family (2026-10-29)

Task ID: SIB-RUN017-r0; operator order trace 1a1838d0413b6fbd ("deepening the 88 REQUIRED-core
artifacts from skeleton to substance"), go traces 1a18391c47e89ddd / 1a183c01b1199779; the
SIB-ASSESS-r2 D3 disposition executed as tranches.

- PREFLIGHT: fetch-first held twice (b2057042->4c04603f->6162cc77; both advances proved zero
  SubjectIntelligence/ paths; advance_disclosure.json filed); local main FF'd to 6162cc77;
  validator pin 357ace0a unchanged; creds restored via the RUN-011 recipe (PAT API-verified,
  never printed). Scripts persisted under session scripts/ (d3_census, run017_scaffold,
  run017_append_packs, run017_author_bodies, run017_enrich_records, run017_stamp,
  run017_lifecycle, run017_governance, run017_gitphase).
- CENSUS (d3_census.py, from published/): 88 REQUIRED artifacts = 115,745 words / 574 records;
  depth-deficit order EXM 735w median < MS 758 < PRO 920 < ASM 950 < PRA 1031 < PED 1048 <
  TUT 1152 < GAP 1464 (MIS 1670 / CUR 1931 / EXP 2135 at depth). Tranche plan of record:
  T1 EXM (this run), T2 MS, T3 PRO+ASM, T4 PRA+PED, T5 TUT, T6 GAP; MIS/CUR/EXP confirm-clean
  only; the EXP/TUT SB1 publisher-eBook gate (RUN-011 register line) honored by ordering.
- T1 EXECUTION (EXM family, all 6 REQUIRED artifacts, +18 records EXM-034..051, family-unique
  block): packs of record carried byte-identical (EXM-01 <- RUN-012 re-spec; EXM-02..06 <-
  RUN-005); 10 ER windows appended to EXM-01/02/03/06 (2025-06 1C/2C p3, 2019-06 1C p3,
  2022-06 1C p3, 2019-06 2CR p3) byte-built per pipeline/evidence_pack.py rules, per-file
  sha256 asserted, diff_proofs.json adds-only proof; EXM-04/05 zero-append (cited spans already
  held; EXM-05 within 2.9k chars of the 40k cap); caps re-asserted post-append. Records authored
  ONLY from read excerpts: 36 quotes pre-bound to pack excerpts (r1 law) across two authoring
  passes (18 records + grounded enrichment); existing 36 records byte-unchanged (identity
  preservation); Limitations/Grounding/Primary-evidence/Research-Status lines updated truthfully.
  New-session evidence now grounding the family: 2019-06, 2022-06, 2025-06 introductions +
  2019-06 2CR question commentary.
- GATES: r3 evidence-claim QA on deployed bodies BEFORE receipts: 79 citations / 0 violations
  (EXM-01 16, EXM-02 14, EXM-03 14, EXM-04 12, EXM-05 12, EXM-06 11); validator qa 0 errors /
  0 warnings x6 (content-bound receipts); stage x6 (SIB-ING-002) -> publish x6 (QA re-verified)
  -> chunks x6 refreshed; run_manifest add-artifact x6 (7 gates each) + validate OK; census.json
  annex with final shas.
- POST-LIFECYCLE SCOREBOARD: validate-manifest qa_passed false, codes {SIB-MANI-007: 88,
  SIB-MANI-011: 4, SIB-MANI-012: 7} — byte-exact the F4a-disclosed RUN-016 state (landing zone
  empty BY DESIGN; evidence chain = governed transition receipts); OBSERVED + DISCLOSED, never
  worked around. Receipt: post_lifecycle_scoreboard.json in the run record.
- DEPTH OUTCOME (honest numbers): EXM median 735 -> ~1,092 words (+49%); EXM-01 798->1,257,
  EXM-02 734->1,106, EXM-03 678->1,039, EXM-04 724->1,038, EXM-05 736->1,186, EXM-06 739->1,077;
  REQUIRED-core words 115,745 -> ~117,663. The family remains below the r1 corpus median
  (~1.3k words/doc): D3 stays REGISTERED until tranches T2..T6 land; this run retires nothing.
- REGISTER NOTE (new debt observed, not repaired): EXM record ids are per-artifact sequences
  with PRE-EXISTING cross-artifact collisions (EXM-021..026 appear in EXM-02, EXM-04 and
  EXM-05); new records therefore took the family-unique block from EXM-034. An id-namespace
  law / dedup pass is operator-ordered material for a future run.
- Git phase: branch sib/bl-017-pass17-r0 off 6162cc77; true diff 20 paths (manifest.yaml +
  6 published + 6 qa-reports + 6 chunks + the RUN-017 run record), every path reconciled
  against lane scope.

## RUN-018 — D3 REQUIRED-core depth pass, tranche 2: MS family (2026-10-29)

Task ID: SIB-RUN018-r0; operator order trace 1a1838d0413b6fbd (the D3 REQUIRED-core depth
pass), go trace 1a183f5436432ed9; tranche 2 of the RUN-017 plan of record.

- PREFLIGHT: fetch-first held (b2057042->6162cc77->251b46ba; advances = this lane's own PR #211
  merge + the T-OEQ-MATHSB-SERVE-1 corpusSyncQueued lane, zero foreign SubjectIntelligence/
  paths; advance_disclosure.json filed); local main reconciled to 251b46ba (working tree proven
  mode-flips only, zero content delta, zero untracked, zero stashes); validator pin 357ace0a and
  pastpapers pin 2cb92fe5 verified. ENVIRONMENT-SPLIT INCIDENT (disclosed): the recycled sandbox
  left a stale pre-recycle working copy at /tmp/my-project (resources HEAD 03b88f54 — where the
  RUN-017 continuation executed); this session's first scaffold pass ran against that stale copy
  and was removed per the stray-write law (RUN-005 packs byte-identical across copies, sha256
  cross-checked x8; zero unique content); all RUN-018 work executed against the live tree at
  /home/z/my-project/resources. Scripts persisted under session scripts/ (run018_scaffold,
  run018_census, run018_dump_excerpts, run018_records, run018_records_b, run018_author_bodies,
  run018_stamp, run018_lifecycle, run018_governance, run018_gitphase).
- CENSUS of record (pre-run): MS = the thinnest REQUIRED family, median 758w, all 8 artifacts
  v1.0 at 6 records each (MS-001..048, collision-free namespace). Tranche plan of record
  predicted zero-append mining (RUN-005 packs' QPMS excerpt counts at/over the 60-per-source
  cap) — CONFIRMED: packs of record carried byte-identical (pack_carry.json), zero windows
  appended, caps untouched.
- T2 EXECUTION (MS family, all 8 REQUIRED artifacts, +24 records MS-049..072, family-unique
  block): 66 quotes pre-bound to raw excerpt text before the official gate (markup-transparent
  self-check: blockquote markers treated as parse scaffolding; per-quote binding to the citation
  that follows it; locator auto-heal pass verified every cited window against the artifact's own
  pack — 0 residual heals after record-side fixes). Record themes: two-level mark accounting +
  scaffolds + NOTE ceilings (MS-01); ECF mandates + either/or pairs + pool-backed points
  (MS-02); sign/value-floor requirements + disjunctive OR-routes + precision/unit envelopes
  (MS-03); synonym/scoped/numeric allowances (MS-04); cross-era rationale grammar + trace-amount
  rationales + graphical REJECTs (MS-05); subsumption + fallback awards + consequential chains
  incl. the 2026-06 window (MS-06); REJECT classes + DEP grammar + whole-item zero rulings
  (MS-07); ECF amnesties + expected-answer windows + precision-as-point (MS-08). One SUPPLEMENTARY
  ER texture citation (MS-064, 2019-06 1C er.pdf p25), labeled in-record. MS-04/MS-08
  Grounding/Primary/Limitations lines truthed to the packs of record (RUN-005-era drift
  disclosed in the run record).
- GATES: r3 evidence-claim QA on deployed bodies BEFORE receipts = 112 citations / 0 violations
  (per artifact: MS-01 14, MS-02 15, MS-03 14, MS-04 11, MS-05 11, MS-06 15, MS-07 14, MS-08
  14; the gate's second run after the in-run fix — see run record for the 3-violation
  fail-closed round and its repair); validator qa 0 errors / 0 warnings x8 (content-bound
  receipts); stage x8 (SIB-ING-002) -> publish x8 (QA re-verified) -> chunks x8 refreshed;
  run_manifest add-artifact x8 (7 gates each + MS-04/MS-08 disclosure gates) + validate OK.
- POST-LIFECYCLE SCOREBOARD: validate-manifest stays in the byte-exact F4a-disclosed red state
  (88x SIB-MANI-007 + 4 WARN + 7 INFO; landing zone empty BY DESIGN; evidence chain = governed
  transition receipts); OBSERVED + DISCLOSED, never worked around. Receipt:
  post_lifecycle_scoreboard.json in the run record.
- DEPTH OUTCOME (honest numbers): MS median 758 -> ~1,210 words (+58%); MS-01 879->1,342,
  MS-02 783->1,284, MS-03 807->1,280, MS-04 612->991, MS-05 766->1,196, MS-06 750->1,223,
  MS-07 717->1,120, MS-08 735->1,201. REQUIRED-core words ~118,039 -> ~121,200. D3 stays
  REGISTERED (tranches T3 PRO+ASM, T4 PRA+PED, T5 TUT, T6 GAP pending; MS/EXM now bracket the
  at-depth families' lower edge).
- STRUCTURAL NOTE (D6-adjacent, registered not repaired): the r3 gate's quote-capture whitelist
  (: ; ( - dash) does not capture Evidence-line lead quotes (preceded by '**Evidence:**' —
  trailing asterisk); those quotes are enforced by the authoring self-check law, not by the
  gate. The tranche's 66 quotes were ALL self-bound under the stricter markup-transparent
  standard; the gate's reach gap is upstream-validator material (tools/sib lane), filed with F4.
- Git phase: branch sib/bl-018-pass18-r0 off 251b46ba; true diff = manifest.yaml + 8 published +
  8 qa-reports + 8 chunks + the RUN-018 run record + library WORKLOG, every path reconciled
  against lane scope.

## RUN-019 — D3 REQUIRED-core depth pass, tranche 3: PRO+ASM families (2026-10-29)

Task ID: SIB-RUN019-r0; operator order trace 1a1838d0413b6fbd (the D3 REQUIRED-core depth
pass), tranche-3 order continued by the operator's RUN-019 order trace 1a1843f90f797b59;
tranche 3 of the RUN-017 plan of record.

- PREFLIGHT: fresh-sandbox recovery — live tree rebuilt at /home/z/my-project/resources
  (blob:none sparse clone at origin/main tip); advance cf5c0764 -> e3d648a1 isolated (1
  commit, YCH12 SB2 v2 polish lane, ZERO SubjectIntelligence/ paths); validator pin
  357ace0a verified (tools/sib 0-path diff at the syllabai tip 18a7e98); pastpapers pin
  2cb92fe5 -> e4c1960b disclosed with ZERO tranche exposure (no PRO/ASM pack path points
  at pastpapers). NEW SOURCE-PIN-STATE DISCLOSURE (not previously filed by RUN-017/018):
  the PRO/ASM packs of record pin BUILD-ERA source content — 133 pack file pins checked
  at this session: 51 byte-identical at the live tip; the 75 pin-vs-tip mismatches + 7
  books/ paths are the standing pre-RUN-018 state (git blob shas IDENTICAL
  cf5c0764..e3d648a1 on 45/45 distinct pinned paths — 0 new drift since the RUN-018
  merge; last QPMS corpus re-process = PR #197 converter v0.29.0, 2026-10-28, pre-dating
  that merge; books/ SB1 chunks jsonl pin verified byte-identical at the tip). The packs
  remain the immutable evidence plane; all quote binding operates on pack excerpts (the
  r3 gate's own standard). This is why the tranche is ZERO-APPEND.
- CENSUS of record (pre-run): PRO = 7 artifacts / median 920w / 44 records (PRO-001..044,
  with pre-existing PRO-030..032 cross-artifact collisions — registered debt, T1 law);
  ASM = 10 artifacts / median 950w / 60 records (ASM-001..060, collision-free). The two
  thinnest REQUIRED families after T1/T2. Packs of record carried byte-identical from
  their origin runs (PRO-01 <- RUN-012, PRO-02..06 <- RUN-006, PRO-07 <- RUN-016,
  ASM-01..09 <- RUN-005, ASM-10 <- RUN-010; pack_carry.json, per-file sha256 asserted);
  zero windows appended, caps untouched.
- T3 (RUN-019): +21 records PRO-045..065 (7 artifacts x3) + +30 records ASM-061..090
  (10 artifacts x3), family-unique blocks. 208 quotes pre-bound to raw excerpt text
  before the official gate via the markup-transparent self-check (per-quote binding to
  the citation that follows; locator auto-heal verified every cited window against the
  artifact's OWN pack — 1 heal, ASM-10's dual-window distractor rationale). Record
  themes: taxonomy meta-rows/weighting ranges/per-item precision envelopes (PRO-01);
  priced wrong-substitution routes/stoichiometric multiplier steps/catalyst null-effect
  pairs (PRO-02); show-that scaffolds/fail-closed reagent gates/cross-point crediting
  (PRO-03); equation-level route forks/conditional ECF/open-set allowances (PRO-04);
  octet-stability and octet-teleology misconceptions/ignored-observation stacks (PRO-05);
  withheld-mark verdicts/improvement guidance/non-creditworthy rulings (PRO-06);
  framework-selection evidence/skill-verb mappings/maths bridge (PRO-07); style-mix
  commitments/aims layers/Question-1 tariff bands (ASM-01); plot tolerances/expected-curve
  anchors/any-one-from pools (ASM-02); priced means/sentence completions/three-link
  ceilings (ASM-03); bounded Suggest ranges/describe pools/diagram conditionals (ASM-04);
  the UNMINED SAMS pool (zero prior SAMS citations library-wide): positivity law,
  boundaries-blind duty, senior-examiner escalation, bracket notation law (ASM-05);
  identification-run ignores/five-mark tables/priced no-working routes (ASM-06); CSQ
  flags/tick tables/contamination reasoning (ASM-07); dated scenarios/catalyst allow
  clusters/formula-count MCQs (ASM-08); nine-mark mid-paper pairs/validity tolls/MCQ
  reprises (ASM-09); numbered statement frames/weighting envelopes/distractor rationales
  (ASM-10).
- STAMP-PHASE INCIDENT (disclosed): two mis-flagged staging passes (a frontmatter
  nested-block parse bug set every source_scope flag false; the validator's own
  SIB-SRC-001 gate caught it before any QA transition), regenerated with flags
  reproduced from the published frontmatter; bodies byte-identical across passes.
- Gates: r3 evidence-claim QA on deployed bodies BEFORE receipts = 279 citations /
  0 violations across 17 artifacts; validator qa 0 errors / 0 warnings x17
  content-bound; stage x17 (SIB-ING-002) -> publish x17 (QA re-verified) -> chunks x17;
  run_manifest add-artifact x17 (7 gates each) + validate OK; post-lifecycle
  validate-manifest = the F4a-disclosed state (88x SIB-MANI-007 + designed
  gap/backlog WARN/INFOs; landing empty by design).
- Honest depth outcome: PRO median 920 -> ~1,330; ASM median 950 -> ~1,300 (final
  numbers of record in runs/SIB-CHEMISTRY_4CH1-RUN-019/ receipts + the post-merge
  census). D3 stays REGISTERED (T4 PRA+PED, T5 TUT, T6 GAP pending; MIS/CUR/EXP at
  depth; EXP/TUT gated on the operator SB1 eBook). Register beyond D3 unchanged: D6
  (single-pipeline self-attestation structural limit), F4 (upstream validator fix,
  master repo tools/sib lane), and the independent silver-tier ER review before
  production reliance.
- Library-side dual record: SubjectIntelligence/WORKLOG.md RUN-019 entry (this);
  repo run record runs/SIB-CHEMISTRY_4CH1-RUN-019/ complete (plan_of_record,
  advance_disclosure, pack_carry, census, evidence_claim_qa_report, lifecycle_receipt,
  post_lifecycle_scoreboard, run_manifest, staged/, bodies/, evidence/).

## RUN-020 — D3 REQUIRED-core depth pass, tranche 4: PRA+PED families (2026-10-29)

Task ID: SIB-RUN020-r0; operator order trace 1a1838d0413b6fbd ("deepening the 88 REQUIRED-core
artifacts from skeleton to substance"), go traces 1a18391c47e89ddd / 1a183f5436432ed9, recovery
brief trace 1a183c01b1199779; tranche-4 order continued by the operator's RUN-020 order trace
1a1873d0d870cb21. COUNTER EVOLUTION of record: the recovery brief specified "chemistry run
counter next = RUN-017"; the operator subsequently specified RUN-019 (trace 1a1843f90f797b59)
and then RUN-020 (trace 1a1873d0d870cb21); RUN-017/018 were consumed by continuation sessions
(worklog of record: RUN-017 = tranche 1 EXM, RUN-018 = tranche 2 MS); the operator's latest
specification governs — this run is RUN-020, tranche 4 of the RUN-017 plan of record.

- PREFLIGHT: fresh-sandbox recovery — the first full clone of syllabai-resources filled the
  sandbox disk (repo ~6.4 GB); re-cloned blob:none + sparse at SubjectIntelligence/ only
  (the RUN-019 recipe; .git 109 MB). Fetch-first held with DISCLOSED ADVANCE: the D3 brief
  pinned origin/main 4c04603f; the live tip at session start is 923232c7 — advance
  4c04603f..923232c7 = 31 commits, of which exactly 3 touch SubjectIntelligence/ and all 3
  are this lane's own tranche merges of record (RUN-017 PR #211 5e26dc9d2, RUN-018 PR #213
  faa2589da, RUN-019 PR #214 3c4d69699); the 28 foreign commits carry 0 SubjectIntelligence/
  paths (per-commit diff-tree census filed in the run record). Validator pin 357ace0a verified
  (tools/sib 0-path diff at the syllabai tip 18a7e98). NEW pastpapers advance disclosed:
  e4c1960b -> f39fc0fd (1 commit) — ZERO tranche exposure proven by content: the 3 distinct
  pastpapers-pinned ER files of the 9 PED packs are byte-identical (sha256) at BOTH the
  RUN-019 pin rev and the live tip (source_pin_state.json). Resources pin state: 17 distinct
  pack paths, 0 blob-oid drift across 4c04603f..923232c7, 14 byte-identical at the tip, 3
  pin-vs-tip mismatches = the standing pre-RUN-018 QPMS re-process state (2019-06 1C,
  2023-06 2C, 2022-06 2CR questions.md; last corpus re-process PR #197 pre-dating the RUN-018
  merge). Creds restored via the RUN-011 recipe with the operator's newly supplied PAT (the
  rotation response to the CRITICAL-OVERDUE standing order; API-probed HTTP 200, scope
  verified, token never printed). Scripts persisted under session scripts/ (run020_preflight,
  run020_dump_excerpts, run020_dump_uncited, run020_index_digest, run020_fetch_windows,
  run020_build_bodies, run020_bindcheck, run020_stamp, run020_gates).
- CENSUS of record (pre-run): PRA = 5 artifacts / median ~1,102 words / 32 records
  (PRA-001..032, collision-free contiguous per-artifact blocks); PED = 9 artifacts / median
  ~1,119 words / 62 records (PED-001..062, collision-free). The two thinnest REQUIRED
  families after T1-T3 (T1 census: PRA 1031, PED 1048). Packs of record carried byte-identical
  from their origin run (PRA-01..05 + PED-01..09 <- RUN-006; pack_carry.json, per-file sha256
  asserted vs origin copy and pack sidecar); zero windows appended, caps untouched.
- T4 EXECUTION (PRA+PED, all 14 REQUIRED artifacts, +42 records PRA-033..047 and PED-063..089,
  family-unique blocks above the family maxima): every record authored ONLY from read pack
  excerpts (unmined-window selection: per-artifact cited-locator census first, new claims
  mined only from windows the published records had never cited); quotes pre-bound under the
  markup-transparent self-check — blockquote scaffolding stripped, per-quote binding to the
  citation that follows, ALL quotes bound including the Evidence-line lead quotes the r3
  gate's whitelist cannot capture (the D6-adjacent reach gap, RUN-018 structural note) —
  0 unbound across all 14 artifacts; one gate-risk caught and repaired at authoring time
  (PRA-044's MS quote crossing a source hard-wrap with '> ' markers re-anchored to
  single-line spans). Existing records byte-identical (builder-verified per artifact).
  Record themes: result-processing law (chromatography Rf discipline, solubility processing
  route, apparatus pragmatics) (PRA-01); burette recording law + precision ceiling,
  calorimetry error budget with version tolerance, board terminology governance (PRA-02);
  controlled comparison with mole-matching fairness, solubility-gated method choice,
  quantitative electrolysis ladder (PRA-03); in-procedure data-processing law, approximation
  disclosure + instrument upgrade, exam-priced method improvement (PRA-04); preparation-route
  endpoint/purity disciplines, one calorimetry template across reaction classes, prerequisite
  sequencing (PRA-05); unit-opener framing, publisher topic essays importing named pedagogy
  scholarship, spec-point-anchored worked-example pedagogy (PED-01); command-word table as
  exam-literacy prerequisite, prior-knowledge hooks carrying new content, molar-mass
  derivation chain (PED-02); model-fidelity honesty (simplifications, quarantined depth,
  figure caveats), exam-technique defaults in-content, memorisation demand markers (PED-03);
  mechanism-first explanations, equilibrium ladder with visible demonstration,
  inference-from-observation pattern (PED-04); practice-design front matter, raw-data practice
  items, unseen-context transfer items (PED-05); summary checklists, drawing-notation hints,
  worked examples re-supplying their own data (PED-06); family re-derivation openers,
  classification by announced cross-chapter criteria, thread-gathering chapter openers
  (PED-07); observation-to-inference scaffolds, name-decoding scaffolds, origin-narrative
  scaffolds (PED-08); strictly-speaking approximation boundaries, diagnostic decision ladders,
  vocabulary-boundary warnings (PED-09).
- GATES: r3 evidence-claim QA on deployed bodies BEFORE receipts = 302 citations / 0
  violations across 14 artifacts; validator qa 0 errors / 0 warnings x14 content-bound;
  stage x14 (SIB-ING-002) -> publish x14 (QA re-verified) -> chunks x14; run_manifest
  add-artifact x14 (7 gates each) + validate OK; post-lifecycle validate-manifest =
  the byte-exact F4a-disclosed red state ({SIB-MANI-007: 88, SIB-MANI-011: 4,
  SIB-MANI-012: 7}; landing zones empty by design) — OBSERVED + DISCLOSED, never worked
  around.
- HONEST DEPTH OUTCOME: PRA median ~1,102 -> 1,693 words (+54%); PED median ~1,119 -> 1,696
  words (+52%); tranche totals 15,674 -> 24,094 words (+8,420); REQUIRED-core ~128,209 ->
  ~136,629 words; records 667 -> 709. Final numbers of record in
  runs/SIB-CHEMISTRY_4CH1-RUN-020/census.json (published-file shas).
- D3 STATUS: stays REGISTERED — tranches T5 (TUT) and T6 (GAP) pending; TUT (and EXP)
  gated on the operator-side SB1 publisher-eBook upgrade (RUN-011 register line), honored
  by tranche ordering; MIS/CUR/EXP confirm-clean only. Register beyond D3 unchanged: D6
  (single-pipeline self-attestation structural limit), F4 (upstream validator fix, master
  repo tools/sib lane), and the independent silver-tier ER review before production reliance.
- Library-side dual record: SubjectIntelligence/WORKLOG.md RUN-020 entry (this); repo run
  record runs/SIB-CHEMISTRY_4CH1-RUN-020/ complete (plan_of_record, advance_disclosure,
  advance_commits, pack_carry, source_pin_state, census_pre, census, stamp_receipt,
  evidence_claim_qa_report, lifecycle_receipt, post_lifecycle_scoreboard, run_manifest,
  staged/, bodies/, evidence/).

---

## RUN-021 — D3 REQUIRED-core depth pass, tranche 5: TUT (2026-10-30; operator traces 1a1838d0413b6fbd D3, 1a188a28859dc5c9 gate resolution "Option 1. And i dont have ebook")

- GATE RESOLUTION OF RECORD: the RUN-011 SB1 publisher-eBook upgrade gate (honored by tranche
  ordering T1-T4) is RESOLVED BY OPERATOR RULING (trace 1a188a28859dc5c9): the operator holds no
  eBook and rules the OCR-basis path (Option 1) — "Why do we need ebook? We already have the book
  parsed, cant we use that?" answered YES of record: the books-plane v3 OCR parse IS the text of
  record (SRC-BOOK-4CH1-SB1, chunks_v3.jsonl sha b2c67eaf, 1,234 chunks, audit GREEN 2026-10-18,
  pin byte-identical at the run tip), the eBook was only ever the optional native-text upgrade
  lane. T5 ran on that basis with the OCR-fidelity residual risk disclosed
  (runs/SIB-CHEMISTRY_4CH1-RUN-021/gate_resolution_sb1_ebook.json: quotes bind VERBATIM to the
  OCR text of record so the citation chain cannot fabricate notation; the residual risk is
  confined to the OCR text itself differing from the printed page — accepted by the ruling; any
  future native-text upgrade can re-bind by mechanical diff). EXP stays confirm-clean (the gate
  is never exercised); the eBook acquisition lane remains open operator-side only beyond D3.
- CENSUS of record (pre-run): TUT = 10 artifacts / 12,490 words / 60 records (TUT-001..060,
  contiguous); the thinnest remaining REQUIRED family after T1-T4. Packs of record carried
  byte-identical from their origin run RUN-008 (pack_carry.json, per-file sha256 asserted);
  zero windows appended, caps untouched; 15/15 distinct pinned paths verified (8 resources
  byte-identical at tip; 7 pastpapers ER paths byte-identical at the LIVE tip bc4740884 — the
  repo advanced f39fc0fd -> bc4740884 mid-lane and the pins held at the new tip, verified via
  the contents API; 0 blob-oid drift across the 7765e43f -> 7352d2ea resources advance).
- T5 EXECUTION (all 10 REQUIRED TUT artifacts, +30 records TUT-061..090, family-unique block
  above TUT-060): every record authored ONLY from read pack excerpts (unmined-window selection:
  per-artifact cited-locator census first — 339/431 excerpts unmined pre-run; TUT-07's unmined
  surface was exhausted and its +3 authored from held windows per the zero-append law with
  fresh claims); quotes pre-bound under the markup-transparent self-check — 102 quotes, ALL
  grounded pre-composition; existing records byte-identical (builder-verified). Themes:
  notation law (brackets, implied charges, coefficient-vs-subscript minimal pair),
  stability-energy ladder, method-law (smooth curves, calorimetry compromise, show-working
  floor), accepted-variant equivalence classes, error-anticipation + sanity-envelope hints,
  catalyst phrasing law, name-confusion repairs, the topic guide's public self-correction,
  particulate marking chains, examiner misapprehension autopsies, same-reaction-different-rate
  frames, two-carrier conduction deep-dives, discharge selectivity, theory-vs-observation
  confrontations with experimental fixes, explain-grammar, anomaly discipline, graph-language
  ladders.
- GATES: r3 evidence-claim QA on deployed bodies BEFORE receipts = 169 citations / 0 violations
  across 10 artifacts; validator qa 0 errors / 0 warnings x10 content-bound; stage x10
  (SIB-ING-002) -> publish x10 (QA re-verified) -> chunks x10; library-wide receipt
  verification 95/95 at 0 errors / 0 warnings via a temp GENERATED-status view (F4b-disclosed
  seam: published files cannot re-enter the qa seat in place; content byte-identical, only the
  status line flipped in the view); run_manifest add-artifact x10 (8 gates each incl.
  gate_resolution) + validate OK; post-lifecycle validate-manifest = the byte-exact
  F4a-disclosed red state ({SIB-MANI-007: 88, SIB-MANI-011: 4, SIB-MANI-012: 7}; landing
  zones empty by design) — OBSERVED + DISCLOSED, never worked around.
- HONEST DEPTH OUTCOME (census_post.json): TUT median ~1,224 -> ~1,965 words (+61%); tranche
  totals 12,490 -> 20,145 words (+7,655); REQUIRED-core ~136,629 -> ~144,284 words; library
  records 709 -> 739. Final numbers of record in runs/SIB-CHEMISTRY_4CH1-RUN-021/census_post.json
  (published-file shas).
- D3 STATUS: stays REGISTERED — tranche T6 (GAP, 8 artifacts, no gate) is the last tranche;
  MIS/CUR/EXP confirm-clean re-gating only. Register beyond D3 unchanged: D6 (single-pipeline
  self-attestation structural limit), F4 (upstream validator fix, master repo tools/sib lane),
  and the independent silver-tier ER review before production reliance.
- Library-side dual record: SubjectIntelligence/WORKLOG.md RUN-021 entry (this); repo run
  record runs/SIB-CHEMISTRY_4CH1-RUN-021/ complete (plan_of_record, advance_disclosure,
  advance_commits, gate_resolution_sb1_ebook, pack_carry, source_pin_state, unmined_census,
  census (gate-time), census_post, quote_selfcheck_tut, evidence_claim_qa_report,
  lifecycle_receipt, post_lifecycle_scoreboard, run_manifest, bodies/, evidence/, staged/).

---

## RUN-022 — D3 REQUIRED-core depth pass, tranche 6: GAP (2026-10-30; operator traces 1a1838d0413b6fbd D3, 1a188d61cef5bc5d "T6 (GAP, 8 artifacts)")

- TRANCHE OF RECORD: T6 = the last D3 tranche (8 REQUIRED GAP artifacts, no gate by the D3
  plan of record; the only operator-side gate in the register, RUN-011 SB1 publisher-eBook,
  was resolved by ruling trace 1a188a28859dc5c9 and is never exercised by the GAP family).
  Operator order trace 1a188d61cef5bc5d ("T6 (GAP, 8 artifacts)"). Packs of record carried
  byte-identical from their origin run RUN-009 (pack_carry.json, per-file sha256 asserted);
  zero windows appended, caps untouched; 32/32 distinct pinned paths verified (9 resources
  byte-identical at tip 1a5c37bc; 23 pastpapers ER paths byte-identical at the LIVE tip
  bc4740884; 0 blob-oid drift across the 1e427889 -> 1a5c37bc advance — 5 foreign commits,
  0 SubjectIntelligence/ paths, per-commit diff-tree census filed).
- CENSUS of record (pre-run): GAP = 8 artifacts / 12,161 words / 48 records
  (GAP-001..048, family-continuous). Unmined-window census first: 244/347
  excerpts unmined pre-run; GAP-03's unmined surface was EXHAUSTED (1/29) and its +3 records
  are authored from held windows with fresh claims per the zero-append law (TUT-07 precedent,
  disclosed); the other seven artifacts authored from their unmined windows.
- T6 EXECUTION (all 8 REQUIRED GAP artifacts, +24 records GAP-049..072, family-unique block
  above GAP-048): every record authored ONLY from read pack excerpts; quotes pre-bound under
  the markup-transparent self-check — 65 quotes, ALL grounded pre-composition
  (quote_selfcheck_gap.json). Themes: statement-level C-suffix completion for sub-topics
  (h)/(i) with the objective-grain chemistry-only banner, the formula-practical book-side
  surface against the unverified-pages boundary; objectives-node continuity, parameter-level
  node detail, and OCR-noise coordinates in the node surface; the closed two-paper mark
  ledger (no-scaling law), the skills-granularity gap, the 4SD0 joint-cover disclosure; the
  answer key's coefficient-misconception register, the spec's printed scope fences, and
  presentation-format demands; marking-law pre-publication and tolerance bands, the
  CHEMISTRY ONLY graded battery; question-block routing bands, stance-carrying hooks, the
  book-native skill taxonomy; apparatus-precision examiner law, the self-disclosed averaging
  boundary, examiner-commented failure modes; and three new research-backlog items (naming
  ledger, cross-discipline hooks, epistemology hooks).
- GATES: r3 evidence-claim QA on deployed bodies BEFORE receipts = 174 citations / 0 violations
  across 8 artifacts; validator qa 0 errors / 0 warnings x8 content-bound; stage x8
  (SIB-ING-002) -> publish x8 (QA re-verified) -> chunks x8; library-wide receipt
  verification 95/95 at 0 errors / 0 warnings via a temp GENERATED-status view (F4b-disclosed
  seam: published files cannot re-enter the qa seat in place; content byte-identical, only the
  status line flipped in the view); run_manifest add-artifact x8 (7 gates each — no
  gate_resolution: T6 carries no gate) + validate OK; post-lifecycle validate-manifest = the
  byte-exact F4a-disclosed red state ({SIB-MANI-007: 88, SIB-MANI-011: 4, SIB-MANI-012: 7};
  landing zones empty by design) — OBSERVED + DISCLOSED, never worked around.
- HONEST DEPTH OUTCOME (census_post.json): GAP median ~1,535 -> ~2,120 words
  (+38%); tranche totals 12,161 -> 17,013 words
  (+4,852); REQUIRED-core ~144,284 -> ~149,136 words; library
  records 739 -> 763. Final numbers of record in
  runs/SIB-CHEMISTRY_4CH1-RUN-022/census_post.json (published-file shas).
- D3 STATUS: CLOSED — all six tranches landed (T1 EXM RUN-017, T2 MS RUN-018, T3 PRO+ASM
  RUN-019, T4 PRA+PED RUN-020, T5 TUT RUN-021 on the operator-ruled OCR basis, T6 GAP
  RUN-022); MIS/CUR/EXP confirm-clean only. Register beyond D3 unchanged: D6 (single-pipeline
  self-attestation structural limit), F4 (upstream validator fix, master repo tools/sib lane),
  and the independent silver-tier ER review before production reliance.
- Library-side dual record: SubjectIntelligence/WORKLOG.md RUN-022 entry (this); repo run
  record runs/SIB-CHEMISTRY_4CH1-RUN-022/ complete (plan_of_record, advance_disclosure,
  advance_commits, pack_carry, source_pin_state, unmined_census, census (gate-time),
  census_post, quote_selfcheck_gap, evidence_claim_qa_report, lifecycle_receipt,
  post_lifecycle_scoreboard, run_manifest, bodies/, evidence/, staged/).
