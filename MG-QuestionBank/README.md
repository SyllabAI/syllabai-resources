# MG-QuestionBank — MathsGenie exam questions, tests & past papers

**Status:** SCAFFOLD (run-001, organization law of record) — extraction waves follow under `T-MG-QB-*`
**Source chain:** `mathsgenie.co.uk` → `SyllabAI/MathsGenie` catalog crawl (RSC flight payloads → `data/*.json`) → this plane
**Sibling planes:** [`../MG-RevisionGuides/`](../MG-RevisionGuides/) · [`../MG-Flashcards/`](../MG-Flashcards/) · [`../MG-Lessons/`](../MG-Lessons/) — identical lane grammar everywhere.

## Purpose

Canonical storage for every **question-bearing** MathsGenie resource: per-topic exam-question booklets (+ their answer booklets), past papers, predicted/practice papers, mini-tests and 45-min tests. This is the practice plane of the MG corpus; learn-side planes (guides/flashcards/lessons) are siblings.

## Lane layout

```text
MG-QuestionBank/
└── {qual}-{subject}-{board}/              # course lane, e.g. gcse-maths-edexcel, igcse-maths-edexcel
    ├── manifest.json                      # lane identity + coverage + provenance (schema below)
    ├── {topic-slug}/                      # MG slug grammar preserved: grade-{g}-{n}-{name} · as-pure-mathematics-{n}-{name}
    │   ├── topic.json                     # identity: title, grade/tier or module, original href, modes_present, source URLs
    │   ├── questions.md                   # human-readable render of the question booklet
    │   ├── questions.json                 # structured: parts[] {label, prompt, marks, command_word?, figure_refs[], source_page}
    │   ├── answers.md / answers.json      # the companion answers booklet (MG publishes these separately per topic)
    │   └── assets/                        # numbered crops: 001-….png …
    └── papers/                            # ONLY for lanes with a paper bank (gcse-maths-edexcel is the first of record)
        ├── manifest.json                  # series index, paper_count, sha256 pins, pdf_policy
        ├── past/{series-slug}/{paper-slug}/    # paper.json + question-paper.pdf + mark-scheme.pdf + model-answers.pdf (whichever exist)
        ├── predicted/{series-slug}/…      # predicted/practice papers + worked solutions
        └── mini-tests/…                   # F/H mini-test sets + answer files
```

## Coverage law — sparse modes are first-class

MathsGenie is **not uniform**. The deep resource bank is Maths-only, and within maths not every lane carries every resource type:

| Lane | Questions | Papers bank | Expected in this plane |
|---|---|---|---|
| `gcse-maths-{edexcel,aqa,ocr,wjec,eduqas,ccea}` | 134 topics each | edexcel only (15 series + predicted + mini-tests) | yes |
| `igcse-maths-edexcel` | 119 topics | not captured yet | yes; mode presence re-verified at run-000 |
| `as-level-maths-edexcel` (8MA0) | 24 topics / 132 subsections | not captured yet | yes; same caveat |
| `a-level-maths-edexcel` (9MA0) | 44 topics in 6 modules | not captured yet | yes; same caveat |
| the other ~660 catalog courses | index-only | — | **no lane here** (catalog lives in `SyllabAI/MathsGenie/data/subjects.json`) |

Rules (enforce in every extraction run):

1. A lane folder exists **only** where the course genuinely carries question resources. No empty lanes, no stub topics.
2. `manifest.json` records `modes_present` / `modes_absent` **with reason** (`not-offered` | `not-published` | `pending-extraction`) and topic-level coverage counts.
3. Never manufacture coverage for absent resource types (repo `AGENT.md` rule 3). A topic without an answers booklet is recorded as such, not padded.
4. Grade/tier is data, not structure: GCSE topic folders keep the original `grade-{g}-{n}-{name}` slug; `topic.json` carries `grade`, `tier` (F spans grades 1–5, H spans 4–9) — no `foundation/`/`higher/` directory split, so cross-tier joins stay trivial.

## Provenance & licensing

- Every artifact carries: `source_url` (original mathsgenie.co.uk page/PDF), `source_sha256`, `extracted_at` (UTC), `extractor` (script + version), `task_id`.
- Papers: the canonical PDF is stored once with sha256 pin; `.md`/`.json` renders are derivatives and are regenerated only by script.
- License status: MathsGenie site content and awarding-body papers are third-party material. The operator authorization entry must be added to [`../LICENSE-DATA.md`](../LICENSE-DATA.md) **before** the first extraction wave lands (same law as SME-*).

## Governance

- Extraction lands as task-ID'd runs (`T-MG-QB-1`, …) with worklog evidence, a `LEDGER.md` wave entry and a receipt JSON, per repo `AGENT.md`.
- Gates `scripts-tests` + `asset-guard` stay green; extraction scripts live in `../scripts/` as `mg_*.py` with tests.
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}` (join field in manifest.json); GCSE maths lanes have no SME equivalent and are new corpus territory.
