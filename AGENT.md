# SyllabAI Resources — Multi-Agent Rules

The project-wide multi-agent operating system is canonical in `SyllabAI/syllabai` (`AGENT.md` + `.syllabai/`).

Resource/corpus-specific rules:

1. Validated resources and SpecificationPoint mappings are authoritative only at their explicit validation state.
2. Agent-generated mappings, aliases and KG candidates remain suggestions until the existing review/promotion gate accepts them.
3. Do not manufacture coverage for intentionally uncovered or rejected SpecificationPoints through semantic similarity.
4. Preserve provenance, source/version identity and review state for every corpus artifact.
5. Coordinate authoritative KG promotion through the KG owner/operator gate; retrieval relationships are not educational truth.
6. Record task ID/base commit and durable evidence for material corpus milestones.
7. Continue independent corpus work on green gates; quarantine genuine ambiguity rather than blocking unrelated work.
