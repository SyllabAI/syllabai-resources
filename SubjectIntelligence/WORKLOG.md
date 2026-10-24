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
