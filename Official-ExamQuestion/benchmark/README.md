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

Outcomes per check and per case — `PASS` / `REVIEW` / `FAIL` / `NOT_RUN` / `NOT_APPLICABLE`:

| Outcome | Meaning | Law |
|---|---|---|
| `PASS` | the check actually ran and passed | — |
| `REVIEW` | a material issue needs a human/authorized decision | surfaced to the operator queue |
| `FAIL` | a required correctness/integrity/rendering/interaction check failed | blocks release |
| `NOT_RUN` | the check did not execute (renderer unreachable, dependency missing, driver error) | **never treated as PASS**; a case whose every required check is `NOT_RUN` dispositions `NOT_RUN`; a case with ANY unestablished required check can never disposition `PASS` (mixed cases rise to `REVIEW`) |
| `NOT_APPLICABLE` | the property is genuinely not checkable at this validation layer **and the contract explicitly names the responsible layer(s)** in the check's `responsibility` field | excluded from that layer's required set; **never silently counts as a pass** — the overall gate stays blocked until every named responsible leg itself runs and passes |

## The aggregation law (F105 — `scripts/official_examq_g9_semantics.py` is its executable form)

The aggregation semantics are code, not prose: `official_examq_g9_semantics.py`
defines them; both leg checkers and `official_examq_g9_aggregate.py` consume
them. The law:

1. **Required checks that pass** contribute to a `PASS`ing case.
2. **Required checks that fail** fail the case (`FAIL` dominates everything).
3. **Required checks that did not run** (`NOT_RUN`) can never yield `PASS` —
   a case with any unestablished required check dispositions `REVIEW` (or
   `NOT_RUN` when nothing at all was established), and the leg + overall gate
   rise accordingly. Missing evidence is never masked by successful unrelated
   checks.
4. **A check not applicable to one layer** may be excluded from that layer's
   required set ONLY when the contract explicitly identifies the responsible
   validation layer — recorded as `NOT_APPLICABLE` with a `responsibility`
   field naming the owning mandatory leg(s). Delegations currently of record:
   - `figures-inlined-count` (corpus leg): crops are inlined into problemMd at
     export time → counted at the **static-bundles** leg; actually loading is
     proven at the **rendered** leg;
   - `fact:*` / `solfact:*` absent from the verbatim corpus layer: served text
     is the exporter/authored layer → required and verified at the
     **static-bundles** leg and the **rendered** leg.
5. **Overall learner-surface gate** (`official_examq_g9_aggregate.py` over the
   receipts): `PASS` only when EVERY mandatory leg (`static-corpus`,
   `static-bundles`, `rendered`) and every required check completed
   successfully, AND every delegation is covered by a responsible leg that ran
   and passed. Any leg `FAIL` → `FAIL`; any leg `REVIEW` or any mandatory leg
   `NOT_RUN`/missing or any uncovered delegation → `REVIEW`; nothing ran →
   `NOT_RUN`.

A green static leg can therefore never promote a missing or blocked rendered
leg, and a corpus-leg `PASS` can never launder a required check that did not
run.

## The two legs (plus the serving-leg bundle mode)

1. **Static leg** — `scripts/official_examq_g9_static_check.py` (deterministic,
   browser-free, CI-able). Verifies the frozen contract against the **corpus of
   record** (`--corpus`, the resources slices: marks law, count law, MCQ key law,
   asset files on disk AND byte-valid per the F104 guard) and against the
   **serving bundles** (`--bundles`, the `syllabai-v2` `official-papers.json`: the
   same laws + the frozen semantic facts and MCQ interaction specs, which are
   exporter/authored-layer text).
2. **Rendered leg** — `scripts/official_examq_g9_render_check.py` (drives
   `agent-browser` against a running `syllabai-v2` hub). Per case: question
   blocks + marks meta + images actually decoded, frozen facts visible in the
   rendered text, zero `.katex-error` / raw-TeX / markdown artifacts, MCQ
   radiogroup select→submit→deterministic feedback (correct AND distractor
   passes), solution reveal carrying the frozen solution fact, screenshot
   evidence. The receipt records the renderer class (`syllabai-v2-local-runtime`
   | `syllabai-v2-vercel`) — a static or mock run can never masquerade as it.

A green static leg **never** implies the rendered leg ran. The OVERALL gate
(`official_examq_g9_aggregate.py`) is `PASS` only when all three mandatory legs
report `PASS`.

## Layout

    benchmark/cases.json      the FROZEN benchmark contract (versioned; anti-gaming law below)
    benchmark/receipts/<run>/ committed receipts + DOM audits + screenshots (evidence of record)
    scripts/official_examq_g9_casegen.py        derivation of cases.json (provenance)
    scripts/official_examq_g9_static_check.py   static leg (corpus + serving-bundle modes)
    scripts/official_examq_g9_render_check.py   rendered leg (real syllabai-v2 hub)
    scripts/official_examq_g9_semantics.py      the aggregation law (F105) as code
    scripts/official_examq_g9_aggregate.py      the OVERALL gate over the three mandatory legs
    scripts/official_examq_g9_tests.py          aggregation-law + asset-guard test battery
    scripts/official_examq_asset_bytes.py       the F104 asset-byte guard (see below)

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

# the OVERALL learner-surface gate (F105): PASS only when all three mandatory
# legs are green — missing receipts block (REVIEW), never promote
python3 scripts/official_examq_g9_aggregate.py \
  --static-corpus <run>/g9-static-corpus.receipt.json \
  --static-bundles <run>/g9-static-bundles.receipt.json \
  --render <run>/g9-render.receipt.json --out <run>/g9-aggregate.receipt.json

# the F104 asset-byte guard (CI-safe): every assets/ file + every referenced
# crop, format-truth validated, dangling references reported
python3 scripts/official_examq_asset_bytes.py --scan-corpus Official-ExamQuestion

# the test battery (aggregation law + asset guard; zero network)
python3 scripts/official_examq_g9_tests.py
```

## The cases (benchmark_version 3)

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
controls are permanent: a mutated fact MUST `FAIL` (the corpus CLI
`--negative-control` control, honest receipt via `--receipt-out`), a mutated
printed label MUST be refused (the corpus CLI `--negative-control-label`
control, F120), an unreachable renderer MUST `NOT_RUN`
(`g9-notrun-control.receipt.json`).

**Version history.** v1 → v2 (F106, this wave): the post-#191 maths-B run-012
figure wave (073639f) + its v2 serving sync moved `maths-02r-2019-06` from
10 crops + 1 stub to 11 crops + 0 stubs (one new gap: 7(b) `asset_7_7-b.png`),
so the frozen v1 counts no longer described the serving bundles of record.
Re-derived via the committed casegen; every other case byte-identical. Source
evidence in LEDGER F106.

**Version history.** v2 → v3 (F120, this wave): the LABEL-VISIBILITY contract.
The F119 wave served the printed part label (`sourcePaper.questionPart`) and
rendered it inline, but G9 had NO case asserting the label is actually VISIBLE
on the learner surface — the blind spot that let the original defect (labels
nowhere, aria-only by design) ship through a fully green gate suite. v3 freezes
per case: `part_labels` samples (one roman-nested label — the (a)(i) class the
original defect mislabelled, one labelled MCQ part, one further labelled part,
plus up to one NULL path-less part — the fail-closed class that must render NO
chip) and the `labelled_parts` census. Enforced at all three legs: the served
field + id-slug pin at static-bundles, the derivation source (part_number tail)
at static-corpus, and ACTUAL VISIBILITY (chip exists, is rendered, sits in a
flex items-baseline row geometrically on the first text line) + the whole-page
chip census at the rendered leg, via the stable `data-part-row` / `data-part-label`
hooks (the same pattern as `data-question-block`; v2 side landed with the F120
renderer PR). One honest census movement rode the re-derivation:
`chemistry-2c-2019-06` crop_assets 7 → 9 (+ two `crop_inline_gaps` — the F113
ms_answer printed-drawing-answer crops for 2(a)/6(d)(ii) served after cases v2
was frozen; derived from the bundles of record). Every other v2 expectation is
carried over byte-identical (the F119 label emission moved zero content bytes,
G-E1). Source evidence in LEDGER F120.

## Evidence of record (2026-10-27-run0 — the G9 landing, validator 0.1/0.3)

| receipt | result |
|---|---|
| `g9-static-corpus.receipt.json` | 8/8 case PASS (corpus of record, main@d495810590 staging) |
| `g9-static-bundles.receipt.json` | 8/8 case PASS (serving bundles) |
| `g9-mutated-fact-negative-control.receipt.json` | pre-repair bundles run whose FAIL exposed the mojibake corpus (see F104); the DEDICATED mutated-fact control receipt (status `DETECTED`, corpus CLI `--negative-control --receipt-out`) landed at run1 |
| `asset-byte-census.slim.json` | the corpus-wide crop-asset byte census (see LEDGER F104) |

Honesty note (F105): the run0 directory also CITED `g9-render.receipt.json`,
`g9-render-vercel-spot.receipt.json` and `g9-notrun-control.receipt.json`, but
those three files were never committed — the rendered-leg evidence existed only
in the PR #191 description. Run1 (below) re-runs every leg under the F105
semantics and commits ALL receipts of record, including the renderer-unavailable
negative control.

## Evidence of record (2026-10-27-run1 — F105 semantics + asset-byte guard)

Filled from the actual runs of this wave; see the receipts in
`receipts/2026-10-27-run1/` (committed in the same PR as this table).

| receipt | result |
|---|---|
| `g9-static-corpus.receipt.json` | 8/8 case PASS (g9-static-check/0.2, F105 semantics: delegations recorded NOT_APPLICABLE with responsibility) |
| `g9-static-bundles.receipt.json` | 8/8 case PASS (serving bundles; fact/solfact checks REQUIRED and green) |
| `g9-render.receipt.json` | 8/8 case PASS through the real syllabai-v2 renderer (local runtime) |
| `g9-render-vercel-spot.receipt.json` | spot PASS through the deployed hub of record |
| `g9-mutated-fact-negative-control.receipt.json` | mutated fact → `DETECTED` (honest control receipt via `--receipt-out`) |
| `g9-notrun-control.receipt.json` | unreachable renderer → all `NOT_RUN`, overall `NOT_RUN`, exit 2 — never PASS |
| `g9-aggregate.receipt.json` | the OVERALL gate over the three mandatory legs (F105 law) |
| `asset-byte-scan.json` | corpus-wide asset-byte guard scan (files/records/errors) |

## Evidence of record (2026-10-30-run0 — the F120 label-visibility case)

The run that closed the F119 "QUEUED" gate gap: every leg re-run under the
benchmark v3 label contract; ALL receipts committed here. Rendered leg of
record = the real syllabai-v2 hub (local runtime of the F120 renderer branch,
v2 PR of record cited in LEDGER F120 — the `data-part-row`/`data-part-label`
hooks are part of the code under test).

| receipt | result |
|---|---|
| `g9-static-corpus.receipt.json` | 8/8 case PASS (g9-static-check/0.3; per-sample label derivation checks green, `labels-field-count` delegated to the serving legs) |
| `g9-static-bundles.receipt.json` | 8/8 case PASS (served field == frozen label == id slug per sample; `labels-field-count` REQUIRED and green) |
| `g9-render.receipt.json` | 8/8 case PASS (g9-render-check/0.5, renderer class `syllabai-v2-local-runtime`): 40 label checks green — whole-page chip census == `labelled_parts` per case (36/47/33/45/55/60/39/36), every chip on the attested grammar, per-sample visibility + same-line geometry, and the maths-B null part rendering NO chip |
| `g9-mutated-fact-negative-control.receipt.json` | mutated fact → `DETECTED` (permanent control, re-run under v3) |
| `g9-mutated-label-negative-control.receipt.json` | mutated label `(z)(i)` refused, original `(b)(i)` still derives from `1(b)(i)` → `DETECTED` (the F120 control) |
| `g9-notrun-control.receipt.json` | unreachable renderer → overall `NOT_RUN`, exit 2 — never PASS |
| `g9-aggregate.receipt.json` | the OVERALL gate: **PASS** over the three mandatory legs (benchmark_version 3) |

No `asset-byte-scan.json` in this run directory: the scan of record is
corpus-wide (1192 assets, run1) and this wave's checkout carries only the 8
case slices — a partial scan would be a dishonest census. The F104 scan stays
enforced by the CI corpus-gates job on every PR.

## The asset-byte guard (the F104 fix at the earliest reliable boundary)

The F104 corruption entered through the git-data API with UTF-8 TEXT encoding.
The durable fix (`scripts/official_examq_asset_bytes.py`, infrastructure layer
— no provider concepts in canonical content):

1. **Validate before commit/publish** — `validate_asset_bytes()` proves format
   truth by magic bytes + real decode (PNG: signature, chunk walk with CRC-32,
   IHDR sanity, IDAT zlib decompression, scanline-size law, IEND; JPEG/GIF/
   WEBP/PDF/SVG each by their actual format — never "assume every asset is a
   PNG"). Extension mismatch and UTF-8-mojibake binaries (the observed
   `C2 89 50 4E 47` signature class) are rejected with actionable, path-naming
   errors.
2. **Publish only through the guard** — `publish_git_blob()` validates BEFORE
   the POST, always base64-encodes binary (never text), then READS THE
   PUBLISHED BLOB BACK and demands sha256 byte-identity with the source.
   An HTTP 200 — from the API or the CDN — is by itself never evidence:
   byte-identity is. Both committed wave pushers (`official_examq_g9_asset_repair.py`,
   `_fixpaths.py`) route through it.
3. **Scan the corpus continuously** — `--scan-corpus` (CI-able) byte-validates
   every `assets/` file and reports dangling crop references; the static leg
   adds a required `asset-bytes-valid` check per benchmark case.
4. **Regression fixtures** — `scripts/official_examq_g9_tests.py` carries the
   valid/corrupt/mojibake/wrong-signature/empty + dangling-reference fixtures
   and the read-back-mismatch negative control (a lying API 200 is refused).

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
regression baseline — and the guard above now refuses the class at the
boundary.
