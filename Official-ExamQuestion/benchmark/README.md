# benchmark/ — the G9 Learner-Surface Quality gate (rendered-question benchmark)

> **Naming of record.** The repository already had a **G8 — POST-COMPLETION AUDIT**
> (AGENTS.md): the course-completion product audit. The learner-surface *rendered*
> gate proposed by the operator's mission ("G8: Learner-Surface Quality") is
> **not equivalent** (it exercises the actual renderer, carries per-question
> receipts, and tests interaction/marking), so it lands as **G9** to avoid a
> gate-id collision. The gate catalog reads: G0–G7 conversion → G8 post-completion
> audit → **G9 learner-surface rendered gate**. Semantics required by the mission
> are preserved exactly.

## What G9 proves (and what it refuses to claim)

G9 validates content **as students actually encounter it**, through the **real
`syllabai-v2` hub** (the production Next.js app — `apps/hub`, deployed of record
at the Vercel hub URL; a local `next dev` of the same app is the same component
tree, not a mock). It never accepts JSON validity, extraction success, or a
standalone prototype as evidence of a working learner surface.

Outcomes per check and per case — `PASS` / `REVIEW` / `FAIL` / `NOT_RUN`:

| Outcome | Meaning | Law |
|---|---|---|
| `PASS` | the check actually ran and passed | — |
| `REVIEW` | a material issue needs a human/authorized decision | surfaced to the operator queue |
| `FAIL` | a required correctness/integrity/rendering/interaction check failed | blocks release |
| `NOT_RUN` | the check did not execute (renderer unreachable, dependency missing, exporter-side property not visible at this leg) | **never treated as PASS**; a case whose every check is `NOT_RUN` dispositions `NOT_RUN`; an aggregate where any case could not be established rises to `REVIEW` |

## The two legs (plus the serving-leg bundle mode)

1. **Static leg** — `scripts/official_examq_g9_static_check.py` (deterministic,
   browser-free, CI-able). Verifies the frozen contract against the **corpus of
   record** (`--corpus`, the resources slices: marks law, count law, MCQ key law,
   asset files on disk) and against the **serving bundles** (`--bundles`, the
   `syllabai-v2` `official-papers.json`: the same laws + the frozen semantic
   facts and MCQ interaction specs, which are exporter/authored-layer text).
2. **Rendered leg** — `scripts/official_examq_g9_render_check.py` (drives
   `agent-browser` against a running `syllabai-v2` hub). Per case: question
   blocks + marks meta + images actually decoded, frozen facts visible in the
   rendered text, zero `.katex-error` / raw-TeX / markdown artifacts, MCQ
   radiogroup select→submit→deterministic feedback (correct AND distractor
   passes), solution reveal carrying the frozen solution fact, screenshot
   evidence. The receipt records the renderer class (`syllabai-v2-local-runtime`
   | `syllabai-v2-vercel`) — a static or mock run can never masquerade as it.

A green static leg **never** implies the rendered leg ran. The aggregate G9
disposition is `PASS` only when the required legs report `PASS`.

## Layout

    benchmark/cases.json      the FROZEN benchmark contract (versioned; anti-gaming law below)
    benchmark/receipts/<run>/ committed receipts + DOM audits + screenshots (evidence of record)
    scripts/official_examq_g9_casegen.py        derivation of cases.json (provenance)
    scripts/official_examq_g9_static_check.py   static leg
    scripts/official_examq_g9_render_check.py   rendered leg

## Run it

```bash
# static: corpus of record (repo checkout; CI-safe)
python3 scripts/official_examq_g9_static_check.py --corpus Official-ExamQuestion

# static: serving bundles (needs a syllabai-v2 checkout)
python3 scripts/official_examq_g9_static_check.py --bundles <v2>/apps/hub/content

# rendered: local production runtime of syllabai-v2 apps/hub
cd <v2>/apps/hub && bun install && bun run dev &
python3 scripts/official_examq_g9_render_check.py \
  --base-url http://localhost:3000 \
  --cases Official-ExamQuestion/benchmark/cases.json \
  --out-dir Official-ExamQuestion/benchmark/receipts/<run-id>

# rendered: the deployed hub of record (spot checks)
python3 scripts/official_examq_g9_render_check.py \
  --base-url https://syllabai-hub-v2.vercel.app ... --only <case-ids>
```

## The cases (benchmark_version 1)

8 real corpus slices across the three lanes — physics (4), chemistry (3),
maths-B (1) — selected for risk classes, not convenience:

| case | lane | why it is in |
|---|---|---|
| physics-2p-2023-06 | 4PH1 | the F102 repair-reconversion slice: MCQ + multipart + crops + honest stubs |
| physics-1p-2019-06 | 4PH1 | the F101 OCR slice: damaged-source regression class, page anchors end-to-end |
| physics-2p-2024-06 | 4PH1 | graph-asset class |
| physics-1p-2023-06 | 4PH1 | heaviest crop surface (16 crops) + exact 110-mark law |
| chemistry-1c-2023-06 | 4CH1 | corpus of record: `ce{}` notation, multi-point mark schemes |
| chemistry-1c-2020-01 | 4CH1 | MCQ adjudication-ledger class (keys never auto-derived) |
| chemistry-2c-2019-06 | 4CH1 | rasterized-archive legacy slice |
| maths-02r-2019-06 | 4MB1 | LaTeX typesetting + M1/A1 MarkScheme codes, zero MCQ |

Anti-gaming law: expected facts are FROZEN in the committed `cases.json`
(derived by the committed casegen from the serving bundles of record); a
generation agent cannot rewrite expectations to pass its own output. Changing
expectations requires a `benchmark_version` BUMP + a LEDGER entry. Negative
controls are permanent: a mutated fact MUST `FAIL` (receipt
`g9-mutated-fact-negative-control.receipt.json`), an unreachable renderer MUST
`NOT_RUN` (`g9-notrun-control.receipt.json`).

## Evidence of record (2026-10-27-run0)

| receipt | result |
|---|---|
| `g9-static-corpus.receipt.json` | 8/8 case PASS (corpus of record, main@d495810590 staging) |
| `g9-static-bundles.receipt.json` | 8/8 case PASS (serving bundles) |
| `g9-render.receipt.json` | **8/8 case PASS through the real syllabai-v2 renderer** (local runtime, Next.js 16.3.8) |
| `g9-render-vercel-spot.receipt.json` | 2/2 spot PASS through the deployed hub of record |
| `g9-mutated-fact-negative-control.receipt.json` | mutated fact → FAIL (exit 1) as required |
| `g9-notrun-control.receipt.json` | unreachable renderer → all NOT_RUN, never PASS |
| `asset-byte-census.slim.json` | the corpus-wide crop-asset byte census (see LEDGER F104) |

## The defect G9 caught on its first run (LEDGER F104)

`physics-2p-2023-06` failed `images-loaded` on its first rendered run: 31 crop
PNGs across 16 physics slices had been **pushed through the git-data API as
UTF-8 text blobs** — every byte ≥ 0x80 UTF-8-encoded (0x89 → C2 89), so served
bytes start `C2 89 50 4E 47` and Chromium (`nosniff`) refuses them: broken
figures corpus-wide **while every URL still returned HTTP 200** — exactly the
class the exists+200 probes (G8 artwork audit item 6) cannot see. The transform
is byte-exactly reversible; PR #187 + #189 re-pushed the 31 corrected blobs and
committed the one dangling crop (`2023-01 4PH1-1P asset_3_b_i_diagram.png`,
rebuilt from the archive QP). After repair: 8/8 rendered PASS. The byte census
(1192 unique assets: 1161 valid / 31 mojibake / 1 dangling) is committed as the
regression baseline.
