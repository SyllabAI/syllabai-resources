# MG-Flashcards — MathsGenie flashcard decks

**Status:** LIVE (T-MG-FC-1 run-001) — `gcse-maths-edexcel` lane of record ({'cards': 2514, 'cards_with_mc_options': 2503, 'files': 252, 'bytes': 5640399}); other waves follow under `T-MG-FC-*`
**Source chain:** `mathsgenie.co.uk` → `SyllabAI/MathsGenie` catalog crawl → this plane
**Sibling planes:** [`../MG-QuestionBank/`](../MG-QuestionBank/) · [`../MG-RevisionGuides/`](../MG-RevisionGuides/) · [`../MG-Lessons/`](../MG-Lessons/) — identical lane grammar everywhere.

## Purpose

Per-topic flashcard decks (MathsGenie's `flashcards` mode). This is the recall plane of the MG corpus — the analogue of `SME-Flashcards/`.

## Lane layout

Decks are small, so the default is a **flat file pair per topic** (mirrors `SME-Flashcards`); a folder variant is used only when a deck needs its own images.

```text
MG-Flashcards/
└── {qual}-{subject}-{board}/              # e.g. gcse-maths-edexcel, a-level-maths-edexcel
    ├── manifest.json                      # lane identity + coverage + provenance
    ├── {topic-slug}.json                  # deck of record (grammar below)
    ├── {topic-slug}.md                    # render: front/back table (script-generated)
    └── {topic-slug}/                      # EXCEPTION folder variant, only if the deck carries images
        ├── deck.json  ·  deck.md  ·  assets/001-….png
```

### {topic-slug}.json grammar

```jsonc
{
  "topic": "grade-6-6-3-simultaneous-equations",
  "lane": "gcse-maths-edexcel",
  "grade": "6", "tier": null,
  "title": "…",                         // source deck title
  "cards": [
    {"id": "…",
     "card_type": "basic|cloze",          // of record: source cardType (cloze gaps rendered as [ ___ ])
     "front": "…", "back": "…",
     "options": [                        // MC amendment of record — multiple-choice cards only
       {"text": "…", "correct": true, "explanation": "…|null"}
     ],
     "points": 1}                        // source points value, when published
  ],
  "card_count": 12,
  "source_url": "https://www.mathsgenie.co.uk/…",
  "source_sha256": "…", "extracted_at": "…", "extractor": "…", "task_id": "…"
}
```

**Grammar amendment (T-MG-FC-1):** MathsGenie flashcards are predominantly **multiple-choice** (source `mcqOptions`): of record each card carries `options[]` with the verbatim `text`, the `correct` flag and the per-option `explanation`. The scaffold-era `card_kind`/`source_ref` fields are superseded by the extracted `card_type` (`basic|cloze`) — no fields are invented.

## Coverage law — sparse modes are first-class

1. A deck file exists **only** for topics that actually publish flashcards on the source site; the lane's `manifest.json` lists `deck_count` and `topics_without_flashcards[]` with reason.
2. Of record (catalog verified per lane at fetch): GCSE maths Edexcel 125/134 topics publish flashcards, IGCSE maths Edexcel 104/104, A-Level maths Edexcel 57/57. The ~660 non-maths catalog courses get **no** lane here.
3. Never manufacture coverage for absent types (repo `AGENT.md` rule 3).

## Provenance & licensing

- Every artifact carries `source_url`, `source_sha256`, `extracted_at`, `extractor`, `task_id`.
- Operator authorization entry in [`../LICENSE-DATA.md`](../LICENSE-DATA.md) required before the first extraction wave (same law as SME-*).

## Governance

- Task-ID'd runs (`T-MG-FC-1`, …), worklog evidence, `LEDGER.md` wave entry, receipt JSON, gates green; scripts as `mg_*.py` in `../scripts/`.
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}`.

## Coverage of record

| lane | decks | notes |
|---|---|---|
| `gcse-maths-edexcel` | 125/134 catalog topics | T-MG-FC-1 run-001 — {"cards": 2514, "cards_with_mc_options": 2503, "files": 252, "bytes": 5640399} |
