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
