# MG-Lessons — MathsGenie lesson content

**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-LS-*`
**Source chain:** `mathsgenie.co.uk` → `SyllabAI/MathsGenie` catalog crawl → this plane
**Sibling planes:** [`../MG-QuestionBank/`](../MG-QuestionBank/) · [`../MG-RevisionGuides/`](../MG-RevisionGuides/) · [`../MG-Flashcards/`](../MG-Flashcards/) — identical lane grammar everywhere.

## Purpose

The **teach plane**: MathsGenie lesson content (the `lessons` mode — the "TeachGenie"-style step-by-step lesson pages). This is the MathsGenie analogue of `CourseLessons/`.

## Lane layout

```text
MG-Lessons/
└── {qual}-{subject}-{board}/              # e.g. gcse-maths-edexcel
    ├── manifest.json                      # lane identity + coverage + provenance
    └── {topic-slug}/                      # grade-{g}-{n}-{name} …
        ├── lesson.json                    # lesson of record (grammar below)
        ├── lesson.md                      # render (script-generated)
        └── assets/                        # numbered figures, only if the lesson has images
```

### lesson.json grammar

```jsonc
{
  "topic": "grade-1-1-1-addition-and-subtraction",
  "lane": "gcse-maths-edexcel",
  "grade": "1", "tier": "foundation",
  "minutes": 8,
  "objectives": ["…"],
  "key_idea": "…",
  "steps": [
    {"heading": "…", "body": "…", "formula": "…", "figure_ref": "assets/001-….png"}
  ],
  "video_url": "https://…",              // embedded video lessons are LINK-of-record — media is never re-hosted
  "source_url": "https://www.mathsgenie.co.uk/…",
  "source_sha256": "…", "extracted_at": "…", "extractor": "…", "task_id": "…"
}
```

## Coverage law — sparse modes are first-class

1. The `lessons` mode is the **sparsest** MathsGenie mode: of record it appears on GCSE maths lanes; A-Level maths explicitly does **not** offer lessons (`modes_absent: ["lessons", "mini-tests", "45-min-tests"]` with reason `not-offered`). IGCSE / AS lanes are re-verified at run-000.
2. A lesson folder exists **only** for topics that actually publish a lesson. `manifest.json` records `lesson_count` and `topics_without_lessons[]` with reason. Never manufacture coverage (repo `AGENT.md` rule 3).
3. The ~660 non-maths catalog courses get **no** lane here.
4. **Exclusion of record:** the six A-Level "lessons" in `SyllabAI/MathsGenie/data/a-level-maths/lessons-edexcel.json` are original-composition UI-demo content written for the recreation (their own `note` says no text is sourced from mathsgenie.co.uk) — they are **not** MathsGenie resources and are **not** extracted here.

## Provenance & licensing

- Every artifact carries `source_url`, `source_sha256`, `extracted_at`, `extractor`, `task_id`.
- Operator authorization entry in [`../LICENSE-DATA.md`](../LICENSE-DATA.md) required before the first extraction wave (same law as SME-*).

## Governance

- Task-ID'd runs (`T-MG-LS-1`, …), worklog evidence, `LEDGER.md` wave entry, receipt JSON, gates green; scripts as `mg_*.py` in `../scripts/`.
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}`.
