# AGENTS.md — operating the Official-ExamQuestion pipeline

> Read this before touching anything in `Official-ExamQuestion/`.
> Doctrine (ADR-037, `syllabai` repo): **the converter extracts; it never authors.**
> Every character of question text is copied from the official source layer; the only
> generated fields are labels and links, and labels are registry-validated or flagged.
> Gates fail closed: a paper ships only when every gate passes, and anything the
> pipeline cannot prove becomes a human review item — never a guess.

## What lives here

```
Official-ExamQuestion/
  README.md                 what this directory is, storage-placement decision
  AGENTS.md                 this file — the operating manual for agents
  LEDGER.md                 append-only improvement ledger (findings F# -> fix -> canary)
  CANARIES.json             machine-checkable regression assertions
  check_canaries.py         canary checker (exit 1 on violation)
  run_all.sh                one-command full-corpus run + canary verification
  CHANGELOG.md              converter version history
  MULTI-SERIES-REPORT.{md,json}   per-series gate matrix + findings + cross-diff summary
  CROSS-DIFF.json           marks agreement vs the repo's own parsed/ layer
  igcse-chemistry-19/<series>/4CH1-1C/
    topic.json              syllabai.official-paper-questions/0.1 (the product)
    questions.md            human-readable render
    validation-report.json  G0–G6 receipts + negative controls + review queue
../scripts/
  official_examq_extract.py the converter (deterministic; no LLM in the extraction loop)
  make_multiseries_report.py report aggregator (auto-discovers series dirs)
  cross_diff_parsed.py      independent-parse marks agreement checker
```

Sibling corpus (NOT this pipeline): `../SME-ExamQuestion/` is the scraped Save My Exams
corpus. It is a **cross-check reference and spec registry source** for this pipeline,
never an input to verbatim extraction.

## Quickstart (per-series)

Inputs are staged under `/home/z/my-project/upload/` with fixed names (see
`official_examq_extract.py:paths_for`):

    official-4CH1-1C-<series>-qp.pdf / -ms.pdf     raw PDFs from syllabai-pastpapers
    official-<series>-qp.txt / -ms.txt             pdftotext -layout extractions
    manifest-<series>-1C.yaml                      manifest from the archive repo

Run one series (writes topic.json + questions.md + validation-report.json):

    python3 scripts/official_examq_extract.py --series 2020-11

Run the whole corpus and verify nothing regressed:

    bash Official-ExamQuestion/run_all.sh

## The iron rules

1. **Verbatim-first.** No paraphrase, no cleanup beyond whitespace, no "obvious" typo
   fixes. If the source says it, the output says it. G2 enforces this with 5-gram
   overlap against each part's own extracted source lines.
2. **Fail closed.** A gate that cannot prove success is a failure. Ambiguous MCQ keys
   are refused (see 2020-01: the pipeline refused to key 7(a)(iii) where a naive read
   of drifted marker rows would have emitted a wrong answer).
3. **Never fill gaps by invention.** Damaged/rasterized sources produce REVIEW states
   with page attribution (see 2019-06 Q7: lost to rasterization, marks honestly
   reported as 104/110), never synthetic content.
4. **Identity comes from the manifest, not the filename.** The canonical example: a
   paper labelled "June 2020" (a series that never ran — COVID) fingerprinted byte-for-
   byte as November 2020. G0 checks sha256 against `manifest.yaml`.
5. **Registry or review.** Spec-point codes must exist in the SME spec-point resolution
   registry (`spec_point_resolution.json`) or be documented gaps. Unresolved codes go
   to the review queue tagged `pending-llm` / `registry-gap-review`.

## Gate catalog

| Gate    | Proves                                   | Fails when                                          |
|---------|------------------------------------------|-----------------------------------------------------|
| G0 identity | the PDFs ARE the manifest's paper     | sha256 mismatch, manifest schema surprises (F13)     |
| G1 structure | Σ parts = printed Q total = 110/paper | mark-sum drift, missing footers, count-registry miss |
| G2 verbatim | emitted text == extracted source text | any post-hoc edit (≥1 5-gram below overlap)          |
| G3 MCQ     | options as printed, exactly one key   | option count drift, ambiguous/unresolved keys        |
| G4 figures | every table/diagram mention → asset   | mentions without page-anchored asset records         |
| G5 answers | positional linkage into the MS        | unmatched parts below threshold                      |
| G6 registry| spec codes exist or are documented    | unknown code without a documented gap                |

Negative controls (N1 mark-bump, N2 one-word paraphrase, N3 fake spec code) run every
session and MUST be DETECTED 3/3 — otherwise the run is void.

## Review queue taxonomy (what humans decide; agents must NOT decide)

| reason prefix            | meaning                                    | agent may? |
|--------------------------|--------------------------------------------|------------|
| `MCQ key unresolved`     | MS layout ambiguous (e.g. 2020-01 Q7a)     | never auto-key |
| `figure crop required`   | asset stub exists, needs the crop pass     | produce crop, keep stub |
| `spec code ... not in registry` | registry gap or invalid code        | propose, human accepts |
| `Q<N> ... image-only`    | rasterized source pages, content lost      | re-ingest via OCR, re-run gates |
| `pending-llm`            | spec tagging not yet seeded for this series| seed via LLM **only as labels**, re-validated by G6 |

## The self-improvement loop (MANDATORY protocol when a gate fails)

Every gate failure is either a **source defect** (the paper/manifest really is that
way) or a **parser gap** (our regex/assumption doesn't cover a new layout). The loop:

1. **Diagnose at the raw-text level.** Reproduce with `parse_ms`/`clean_lines` in a
   REPL; find the exact lines that defeat the current rule. Never fix against the
   parsed output alone.
2. **Classify.** Source defect → review-queue attribution (G1's image-only census is
   the model). Parser gap → step 3.
3. **Fix generically, not per-series.** A fix must name the *pattern*, not the paper
   (see LEDGER F11–F14: indent tolerance, positive-statement keying, manifest schema
   drift, elimination keying). Reject your own fix if it would key the 2020-01 canary
   or any other canary differently.
4. **Record the finding** in `LEDGER.md` (next `F<max+1>`): series, finding, fix.
   One finding per distinct pattern. This is the ledger that makes the pipeline
   self-improving — new agents inherit every scar.
5. **Add a canary** to `CANARIES.json` that would FAIL if the bug regressed (e.g.
   "2023-06 9(a)(i) keyed B", "2020-01 7(a)(iii) unkeyed"). Canaries are the tests.
6. **Re-run the whole corpus** (`run_all.sh`) — a fix that helps one series and breaks
   another is not a fix (F12 briefly regressed 2020-11 exactly this way; the canary
   caught it). All canaries must pass; per-series gate states must be equal-or-better.
7. **Bump `CONVERTER_VERSION`** in the converter + append `CHANGELOG.md`. Outputs
   embed the generator string, so any topic.json can be traced to converter behaviour.

## Conventions

- Output dirs mirror the archive: `<course>/<series>/<paper>/`. Never write into
  `syllabai-pastpapers` (byte-frozen archive of record; see README).
- Add a new series: stage the 3 input files with the standard names, verify printed
  question count against footers (must sum to 110), add the count to
  `EXPECT_QUESTIONS`, run, then follow the improvement loop for whatever the gates
  surface.
- Add a new course (beyond igcse-chemistry-19): parametrize `PAPER_TOTAL`,
  `EXPECT_QUESTIONS`, footer regex, and the spec registry path; the ADR's UNVERIFIED
  list (§6) lists what must be proven for a new course (modular 4XCH1, 4SD0 shared
  papers are known next candidates).
- Commit outputs and pipeline changes together; a converter change without regenerated
  outputs (or vice versa) is an inconsistent state.

## Known open work (pick up from here)

- Human review queues: MCQ keys for 2020-01 Q7(a) (2 keys), figure crops for all
  series (asset stubs are page-anchored and ready), spec-tagging seeds (`pending-llm`)
  for all series except the 2020-11 demo set.
- 2019-06 archive damage: re-ingest from a better PDF if one surfaces, or OCR the 5
  rasterized content pages, then re-run gates (G1 must return to PASS with 110/110).
- 2020-06 never ran (COVID); do not "fix" its absence in the archive.
