# MG-Flashcards — MathsGenie flashcard decks

**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-FC-*`
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
  "grade": "6", "tier": "higher",
  "cards": [
    {"front": "…", "back": "…", "card_kind": "definition|formula|method|quick-question",
     "source_ref": {"page": 1, "figure": "assets/001-….png"}}
  ],
  "card_count": 12,
  "source_url": "https://www.mathsgenie.co.uk/…",
  "source_sha256": "…", "extracted_at": "…", "extractor": "…", "task_id": "…"
}
```

## Coverage law — sparse modes are first-class

1. A deck file exists **only** for topics that actually publish flashcards on the source site; the lane's `manifest.json` lists `deck_count` and `topics_without_flashcards[]` with reason.
2. Of-record expectations: GCSE maths ×6 boards and A-Level maths Edexcel expose `flashcards`; IGCSE / AS lanes are re-verified at run-000 before bulk landing. The ~660 non-maths catalog courses get **no** lane here.
3. Never manufacture coverage for absent types (repo `AGENT.md` rule 3).

## Provenance & licensing

- Every artifact carries `source_url`, `source_sha256`, `extracted_at`, `extractor`, `task_id`.
- Operator authorization entry in [`../LICENSE-DATA.md`](../LICENSE-DATA.md) required before the first extraction wave (same law as SME-*).

## Governance

- Task-ID'd runs (`T-MG-FC-1`, …), worklog evidence, `LEDGER.md` wave entry, receipt JSON, gates green; scripts as `mg_*.py` in `../scripts/`.
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}`.
