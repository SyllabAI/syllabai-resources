# MG-QuestionBank — MathsGenie per-topic exam questions

**Status:** ACTIVE (corpus landing under `T-MG-QB-1` run-001) — scaffold law per `T-MG-SCAFFOLD-1` run-001 (PR #314, merged 2026-11-07)
**Source chain:** `mathsgenie.co.uk` GCSE Maths (Edexcel) — classic page `old.mathsgenie.co.uk/gcse.html` (asset host `old-asset.mathsgenie.co.uk`) joined 134/134 against the new-site lanes (`mathsgenie.co.uk/gcse/maths/edexcel`) and the `SyllabAI/MathsGenie` catalog crawl.
**Sibling planes:** [`../MG-RevisionGuides/`](../MG-RevisionGuides/) · [`../MG-Flashcards/`](../MG-Flashcards/) · [`../MG-Lessons/`](../MG-Lessons/) — identical lane grammar everywhere.

## Purpose

Canonical storage for the **per-topic exam-question bank**: every MathsGenie topic's exam-question sheet (`…-ws.pdf`), its companion booklet (`….pdf`) and worked solutions (`…ans.pdf`), extracted into structured data + question crops. **Full paper banks are out of scope** (see Exclusions of record). Learn-side planes (guides/flashcards/lessons) are siblings.

## Scope exclusions of record (operator decision, 2026-11-07)

| Excluded | Reason |
|---|---|
| Past-paper banks (`papers/past/…`, question papers + mark schemes as PDFs) | operator decision: **no past-paper PDFs in the corpus** |
| Predicted/practice paper banks (`papers/predicted/…`) | same decision — no full-paper PDFs |
| Mini-tests / 45-minute tests | same decision; live-site interactive, link-of-record only |

The lane `site_lane` URL remains the link-of-record for everything excluded here.

## Lane layout

```text
MG-QuestionBank/
└── gcse-maths-edexcel/                     # course lane {qual}-{subject}-{board}
    ├── manifest.json                       # lane identity + coverage + scope exclusions + provenance
    ├── INDEX.md                            # human-readable topic table (code · name · slug · counts)
    └── grade-{band}-{g}-{n}-{name}/        # site-native topic slug, e.g. grade-8-9-8-3-proof, grade-3-3-12-best-buy
        ├── topic.json                      # identity: name, code, grade_band, site_slug, source URLs + sha256, modes
        ├── questions.md                    # human-readable render (crops embedded)
        ├── questions.json                  # structured: questions[] {number, marks, parts[], text, crops[], pdf_page}
        ├── answers.md / answers.json       # worked solutions: per-question crops when anchored, else per-page
        └── assets/                         # q{NN}.png question crops · a-p{NN}.png solution-page images
```

Slug grammar is the **site-native topic slug** (verified join 134/134 against the live lane), not a re-invention: `grade-{band}-{g}-{n}-{name}`, where `band` is the MathsGenie grade section (`1`–`7`, `8-9`) and `g.n` is the topic code shown on the site. Grade/tier stays data in `topic.json` (`grade_band`, `grade`, `code`) — no `foundation/`/`higher/` directory split.

## Coverage law — sparse modes are first-class

MathsGenie is **not uniform**. Within GCSE Maths Edexcel (the deep bank), resource types vary per topic:

| Lane | Topics | With question sheets | With solutions link | Notes |
|---|---|---|---|---|
| `gcse-maths-edexcel` | 134 (bands 1–7, 8-9) | 133 (120 ws + 13 booklet-only) | 133 | 5.13 Midpoint of a Line Segment: **nothing published** — recorded absent, no stub dir |
| `igcse-maths-edexcel` | 118 (bands 1–7, 8-9) | 118 (82 ws + 36 booklet, incl. 21 booklet-fallback) | 118 | extracted by `T-MG-QB-2/run-001`; no revision-guides / question-rush mode in this lane; 3.1 + 3.17 carry `question_count: 0` (image-only / fraction-fragment text layers — honest gaps, never padded) |
| `as-level-maths-edexcel`, `a-level-maths-edexcel`, other boards | — | — | — | later runs under `T-MG-QB-*`; mode presence re-verified at run-000 of each |

Rules (enforce in every extraction run):

1. A topic folder exists **only** where question resources genuinely exist. Unpublished topics live in `manifest.json` with `reason: not-published` — never as stub dirs.
2. `manifest.json` records `modes_present` / `modes_absent` **with reason** (`not-offered` | `not-published` | `pending-extraction`) and `scope_exclusions` (operator decisions, dated).
3. Never manufacture coverage for absent resource types (repo `AGENT.md` rule 3). A topic whose solutions asset 404s at source is recorded as `answers.present = false` with the failing URL — not padded.
4. Marks/part structure are data extracted from the sheets; where a sheet prints no marks, `marks` stays `null` — never inferred.

## Provenance & licensing

- Every artifact carries: `source_url` (original mathsgenie.co.uk page/PDF), `source_sha256`, `extracted_at` (UTC), `extractor` (script + version), `task_id`.
- **Source PDFs are never stored in this repo**: each PDF is fetched at extraction time, processed into JSON/crops, and discarded — only its sha256 and URL are kept. Crops/renders are derivatives regenerated only by script.
- License status: MathsGenie site content is third-party material. The operator attestation entry lives in [`../LICENSE-DATA.md`](../LICENSE-DATA.md) (Amendment 2026-11-07) — landed together with the first extraction wave.

## Governance

- Extraction lands as task-ID'd runs (`T-MG-QB-1`, …) with worklog evidence, a `LEDGER.md` wave entry and a receipt JSON, per repo `AGENT.md`.
- Extraction scripts live in `../scripts/` as `mg_*.py` (`mg_flight_decode.py`, `mg_fetch_catalog.py`, `mg_probe_pdf.py`, `mg_qb_extract.py`, `mg_manifest.py`, `mg_upload.py`).
- Crosswalk: `igcse-maths-edexcel` ↔ SME lane `igcse-maths-a-18-{foundation,higher}` (join field in manifest.json); GCSE maths lanes have no SME equivalent and are new corpus territory.
