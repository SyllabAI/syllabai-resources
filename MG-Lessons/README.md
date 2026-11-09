# MG-Lessons — MathsGenie lesson content

**Status:** LIVE (T-MG-LS-1 run-001) — `gcse-maths-edexcel` lane of record ({'steps': 688, 'quiz_questions': 398, 'figures': 186, 'files': 431, 'bytes': 23572901}); other waves follow under `T-MG-LS-*`
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
  "grade": "1", "tier": null,
  "steps": [                             // source content cards, in source `order`
    {"heading": "…", "body": "… (verbatim math, markdown)",
     "figure_refs": ["assets/001-….png"]}   // multiple figures per step allowed (amendment)
  ],
  "quiz": [                              // source mcq cards (check-yourself)
    {"id": "…", "question": "…",
     "options": [{"id": "…", "text": "…", "is_correct": true}],
     "explanation": "…"}
  ],
  "videos": [],                          // links-of-record: captured only if the lesson page embeds one — GCSE lessons of record embed none (video content lives in MathsGenie's separate `videos` mode; never downloaded, never re-hosted)
  "is_published": true,
  "source_url": "https://www.mathsgenie.co.uk/…",
  "source_sha256": "…", "extracted_at": "…", "extractor": "…", "task_id": "…",
  "source_meta": {"lesson_id": "…", "topic_id": "…", "figures": 3}
}
```

## Coverage law — sparse modes are first-class

1. The `lessons` mode is sparse and lane-asymmetric of record (catalog verified at fetch): GCSE maths Edexcel 122/134 topics, IGCSE maths Edexcel 97/104, A-Level maths Edexcel 55/57 publish lessons. (The GCSE-only mode is `revision-guides`; IGCSE and A-Level lanes publish **no** revision-guides and no lessons topics are invented for them.)
2. A lesson folder exists **only** for topics that actually publish a lesson. `manifest.json` records `lesson_count` and `topics_without_lessons[]` with reason. Never manufacture coverage (repo `AGENT.md` rule 3).
3. The ~660 non-maths catalog courses get **no** lane here.
4. **Exclusion of record:** the six A-Level "lessons" in `SyllabAI/MathsGenie/data/a-level-maths/lessons-edexcel.json` are original-composition UI-demo content written for the recreation (their own `note` says no text is sourced from mathsgenie.co.uk) — they are **not** MathsGenie resources and are **not** extracted here.

## Provenance & licensing

- Every artifact carries `source_url`, `source_sha256`, `extracted_at`, `extractor`, `task_id`.
- Operator authorization entry in [`../LICENSE-DATA.md`](../LICENSE-DATA.md) required before the first extraction wave (same law as SME-*).

## Governance

- Task-ID'd runs (`T-MG-LS-1`, …), worklog evidence, `LEDGER.md` wave entry, receipt JSON, gates green; scripts as `mg_*.py` in `../scripts/`.
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}`.

## Coverage of record

| lane | lessons | notes |
|---|---|---|
| `gcse-maths-edexcel` | 122/134 catalog topics | T-MG-LS-1 run-001 — {"steps": 688, "quiz_questions": 398, "figures": 186, "files": 431, "bytes": 23572901} |
