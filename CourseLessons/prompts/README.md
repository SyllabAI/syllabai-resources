# prompts/ — versioned prompt registry

Every generated content receipt pins a prompt version from here.
Bump rules: style change = minor; content-rule change = major + findings entry
(SELF-IMPROVEMENT §6).

| Prompt | Version | Purpose |
|---|---|---|
| lesson-prose | 1.0.0 | Section prose from chunkRefs provenance |
| lesson-boxes | 1.0.0 | Additive boxes (prior-knowledge, cross-curricular, misconception, exam-hint, …) |
| lesson-glossary | 1.0.0 | Glossary entries with ms_accepts/ms_avoids from mark schemes |

(Files land here as `lesson-prose@1.0.0.md` etc. as agents first use them —
seeded empty so the registry starts honest.)
