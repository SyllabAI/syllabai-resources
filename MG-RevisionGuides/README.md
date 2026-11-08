# MG-RevisionGuides — MathsGenie revision notes

**Status:** LIVE (T-MG-RG-1 run-001) — `gcse-maths-edexcel` lane of record (132/132 guides); other waves follow under `T-MG-RG-*`
**Source chain:** `mathsgenie.co.uk` → `SyllabAI/MathsGenie` catalog crawl → this plane
**Sibling planes:** [`../MG-QuestionBank/`](../MG-QuestionBank/) · [`../MG-Flashcards/`](../MG-Flashcards/) · [`../MG-Lessons/`](../MG-Lessons/) — identical lane grammar everywhere.

## Purpose

The **learn plane**: per-topic revision guides (MathsGenie's "revision notes" mode). This is the MathsGenie analogue of `SME-RevisionNotes/` and follows the same corpus law: typed blocks in JSON, faithful math, rendered markdown as a derivative, assets preserved with provenance.

## Lane layout

```text
MG-RevisionGuides/
└── {qual}-{subject}-{board}/              # e.g. gcse-maths-edexcel, a-level-maths-edexcel
    ├── manifest.json                      # lane identity + coverage + provenance
    └── {topic-slug}/                      # grade-{g}-{n}-{name} · as-pure-mathematics-{n}-{name} …
        ├── revision-guide.json            # typed blocks (see grammar below)
        ├── revision-guide.md              # render (derivative of the JSON, script-generated)
        └── assets/                        # numbered figures: 001-….png …
```

### revision-guide.json block grammar

```jsonc
{
  "topic": "grade-4-4-14-cylinders",
  "lane": "gcse-maths-edexcel",
  "blocks": [
    {"kind": "heading",        "text": "Volume of a cylinder"},
    {"kind": "paragraph",      "text": "…"},
    {"kind": "formula",        "math": "V = \\pi r^2 h", "math_format": "latex|wiris-verbatim"},
    {"kind": "worked-example", "steps": ["…"], "figure_refs": ["assets/003-….png"]},
    {"kind": "exam-tip",       "text": "…"}
  ],
  "source_url": "https://www.mathsgenie.co.uk/…",
  "source_sha256": "…", "extracted_at": "…", "extractor": "…", "task_id": "…"
}
```

Math stays **verbatim** (Wiris MathML or LaTeX as found) — same rule as `SME-RevisionNotes`.

## Coverage law — sparse modes are first-class

1. A topic folder exists **only** if that topic actually has a revision guide on the source site.
2. A lane exists **only** if the course carries the revision-guides mode at all. Of-record expectations: GCSE maths ×6 boards and A-Level maths Edexcel expose `revision-guides`; IGCSE / AS lanes' mode presence is re-verified at run-000 before any bulk landing.
3. `manifest.json` per lane records `guide_count` / `topics_without_guides[]` (with reason). Never manufacture coverage (repo `AGENT.md` rule 3).
4. The ~660 non-maths catalog courses get **no** lane here.

## Provenance & licensing

- Every artifact carries `source_url`, `source_sha256`, `extracted_at`, `extractor`, `task_id`.
- License status: operator authorization entry in [`../LICENSE-DATA.md`](../LICENSE-DATA.md) required before the first extraction wave (same law as SME-*).

## Governance

- Task-ID'd runs (`T-MG-RG-1`, …), worklog evidence, `LEDGER.md` wave entry, receipt JSON, gates green; scripts as `mg_*.py` in `../scripts/`.
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}`; GCSE maths lanes are new corpus territory (no SME equivalent).

## Coverage of record

| lane | guides | notes |
|---|---|---|
| `gcse-maths-edexcel` | 132/134 catalog topics (2 not-offered) | T-MG-RG-1 run-001 — 1,680 blocks (135 worked examples, 292 mcq-sets), 312 figures; grammar amended with `figure` + `mcq-set` blocks |
