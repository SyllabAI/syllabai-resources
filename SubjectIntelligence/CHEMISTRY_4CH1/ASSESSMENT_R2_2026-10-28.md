# CHEMISTRY_4CH1 — SIB-ASSESS-r2: post-repair honest re-assessment of the 95 artifacts

**Status:** DELIVERED (2026-10-28, operator order "Go" on the queued backlog — trace
`1a17eb6123855fc9`). Supersedes the *queue position* of SIB-ASSESS-r1 (which was
delivered in-chat 2026-10-27 on the pre-RUN-012 tree @ `720245a98e18`); this edition
re-measures the library **after** RUN-012 (D1/D5), RUN-013 (D2), RUN-014 (D4), and
RUN-015 (CUR/GAP citation grammar + the 7 OPTIONAL-HIS backlog + docs), on local main
@ `f65758e8` (origin/main FF'd; the 3-commit advance — a book-parse lane — touched
zero SubjectIntelligence paths, isolation proven; validator pin `357ace0a` unchanged).

**Purpose:** verify the repairs held, re-measure the corpus, sweep for debt the
run-scoped gates could not see, and issue the GO/NO-GO that gates the D7
staging/publication pass (RUN-016).

## Verdict

**GO.** The library is verifiably honest and traceable at every layer probed; every
SIB-ASSESS-r1 repair held; the corpus grew where the operator ordered growth (HIS)
without regressions elsewhere. r2 adds two new registered findings — **D8** (6
grammar-form debt tokens in gate-legal artifacts) and **D9** (CUR-01's 5 debt forms +
never-gated status) — both mechanical, both scheduled into RUN-016's pre-stage repair,
because repairing them *after* publication would force new artifact versions. One
structural limit (**F4**) is registered for the upstream validator lane. D6 (the
single-pipeline self-attestation structural limit) is unchanged by definition of the
pipeline and remains operator-level.

## Method — four independent instruments

1. **Metrics pass** (`scripts/assess_r2.py`, r1's method re-run on the new tree):
   per-artifact words/records/citations/evidence-lines/cite-mix/status/version across
   all 95 artifacts, 12 families.
2. **Evidence-claim QA sweep** (`scripts/assess_r2_gate_sweep.py`): the r3 gate
   (`pipeline/sib_evidence_claim_qa.py` — citation resolution, page/line/range
   locator verification, quote binding) re-run for **94/95 artifacts** against each
   artifact's **latest pack of record** (origin or carrier run; RUN-001..015).
   CUR-01 is the one skip — its origin run (RUN-001) predates the census-annex law
   and the gate fails closed without it; disclosed, not shimmed.
3. **Live validator sweep** (`scripts/assess_r2_live_sweep.py`): `tools.sib.cli qa`
   re-run on all 95 from a fresh session at the pin of record, then receipt
   **byte-identity** against the committed qa-reports.
4. **Repair-hold machine probes + human spot-reads**: D1/D2/D4/D5 direct probes;
   one full new-record read (HIS-066) with an independent verbatim pack check.

## What held (the r1 repair ledger, re-verified)

| r1 finding | Repair run | r2 verification |
|---|---|---|
| D1 disclosure truth | RUN-012 | manifest `grounding_consumed` states the validated v3 SB1 parse "NOT identity-only" with the audit-green pin; `correction_of_record` block present naming the wrong RUN-011 line |
| D2 anchor registry (133× ANCH-002) | RUN-013 | **0** ANCH-002 across all 95 receipts; 128× ANCH-004 (INFO, resolved) + 2× IDENT-005 (INFO, known) |
| D4 derived-quantity provenance | RUN-014 | CUR-02 carries 33.1% (was 33.2%); EXP-045 attributes "about 1 in ~75" to the book and labels "pH around 3–5" as "an approximate band, not a printed range — the book's printed figure is the 2.88" |
| D5 editorial nits | RUN-012 | PRO-01 Purpose sentence reads clean; EXM-01 colon clean |
| CUR/GAP grammar debt (131 pathless) | RUN-015 | CUR-03..08 + GAP-01..08: **0** pathless tokens, 0 violations in the r2 gate sweep |
| Quote binding of the 28 new HIS records | RUN-015 | machine-bound by the r3 gate (HIS 138 citations / 0 violations) + HIS-066 independently verbatim-verified |

## Corpus after RUN-012..015 (vs the r1 baseline @ 720245a)

| Metric | r1 | r2 | Δ |
|---|---|---|---|
| Artifacts | 95 | 95 | — |
| Families | 12 | 12 | — |
| Words | 125,062 | 129,788 | **+4,726** |
| Records | 616 | 644 | **+28** (HIS-043..070, the OPTIONAL-HIS backlog) |
| Citations | 1,403 | 1,588 | **+185** |
| Evidence lines | 580 | 607 | +27 |

Family medians (words): EXP 2,150 · CUR 1,937 · HIS 1,960 · MIS 1,670 · GAP 1,488 ·
TUT 1,172 · PED 1,048 · PRA 1,031 · ASM 966 · PRO 920 · MS 766 · EXM 736. The depth
ceiling r1 flagged (D3, ~1.3k words/doc median) moved selectively: HIS rose from
~1.4k to 1,960 median on the operator's backlog order; the REQUIRED-core median is
unchanged by design (no depth order was given for it — D3 remains registered).

All 95 artifacts: `status: GENERATED`, applicability 88 REQUIRED / 7 OPTIONAL / 0
NOT_APPLICABLE — consistent with the manifest header's landing-zone law.

## New findings (r2)

**D8 — grammar-form debt, gate-legal (6 tokens, 5 artifacts).** The r3 gate extracts
citations only from record blocks and only from parens *starting* with `SRC-`, and it
verifies multi-citation parens by requiring every referenced page to exist — so the
following forms pass the gate while violating the documented r4 form law (one citation
per paren; prose outside parens; `pN` spacing):
- CUR-05: `(store meta law; SRC-GRAPH-4CH1, graph/igcse-chemistry/point_edges.yaml lines 8-22)` — prose-paren, pathed (the pathed sibling of the 2 hidden forms RUN-015 repaired).
- CUR-08: `(CUR-07's store census; SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p3)` — same class.
- PRO-07 ×2: `(SRC-TL-4CH1, <file>.pdf p 1; SRC-TL-4CH1, <file2>.pdf p 1)` — semicolon-joined multi-citations (plus `p 1` spacing nits).
- EXP-01 ×2: `(SRC-BOOK-4CH1-SB1, v3 chunk corpus)` and `(SRC-SME-NOTES-4CH1, SRC-SME-EXAMQ-4CH1)` — prose locators outside the gate's extraction reach (in artifact-level sections).
Disposition: **repair in RUN-016 pre-stage** (post-publication repairs would burn
artifact versions); full repair discipline applies (census table, exact-match
replaces, substance asserts, re-gate, receipts).

**D9 — CUR-01 debt set + never-gated (5 forms, 1 artifact).** CUR-01 (RUN-001 origin)
predates the census-annex law, so the r3 gate has never run on it (fail-closed skip,
disclosed above). Its citation set carries: `(SRC-SPEC-4CH1, spec p1)` and
`(SRC-TL-4CH1, gstt pp3–4)` / `(gstt pp3–5)` (abbreviation locators with en-dash
ranges — the real file is `gstt-int-gcse-chemistry.pdf` as CUR-08 cites it),
`(SRC-SAMS-4CH1, identity row)` ("identity" is law; "identity row" is not), and one
fully-hidden prose-paren carrying a graph citation mid-prose. Disposition: **repair in
RUN-016 pre-stage**, then CUR-01 gets its **first-time gate** via the RUN-016 census
annex (pack of record: RUN-001's evidence pack, carried unchanged).

**F4 — structural (upstream validator lane).** The manifest validator's
REQUIRED-presence check models only `artifacts/` (`MANIFEST_MISSING_REQ`), while
publication evidence correctly probes `staged/`/`published/`. A library that executes
the designed lifecycle (GENERATED → QA_PASSED → STAGED → PUBLISHED) therefore flips
validate-manifest red at the moment it becomes servable — the scoreboard cannot model
the state it exists to certify. This is the D6 class: OBSERVED + DISCLOSED, not
worked around. RUN-016 will file it as a register item and a new earned lesson; the
pre-stage validate-manifest green sweep (this assessment) is the last full-scoreboard
gate of record. The upstream fix (presence check should honor staged/published for
rows whose status advanced) belongs to `SyllabAI/syllabai@tools/sib/` — operator lane.

**F5 — nits folded into D8:** `p 1` spacing (r4 wants `pN`); en-dash page ranges
(`pp3–4` — r4 wants ASCII `pp3-4`); these are repaired with their parent tokens.

## Confirmations of structural integrity (r2 additions)

- **Validator determinism across sessions:** the live sweep reproduced all 95
  committed qa-reports **byte-identically** at pin `357ace0a` (0 drift) — receipts
  are reproducible evidence, not one-off artifacts.
- **Gate coverage honesty:** the 94/95 sweep re-verified 1,514 citations / 0
  violations against the packs of record — the largest single gate surface executed
  on this library (r1's verify pass sampled; r2 sweeps).
- **HIS depth is real:** the 28 new records average ~380 words with 2-4 quotes each,
  machine-bound and human-spot-checked (HIS-066: the mark-allocation misreading
  persistence pair 2015→2019, quotes verbatim in the legacy-ER excerpts).

## Disposition

RUN-016 (the D7 staging/publication pass, operator-ordered) proceeds: pre-stage
repairs of D8/D9 → stage ×95 → publish ×95 → chunks ×95 → governance + the F4
structural disclosure. The r1 recommendation's residual — an **independent silver-tier
ER review before production reliance** — remains the operator's next ordering after
RUN-016.

Receipts: `/tmp/sib-assess-r2/` (corpus_stats, family_aggregates, gate_sweep,
per-run QA reports, live_sweep, verdict); scripts persisted at
`/home/z/my-project/scripts/assess_r2*.py`.
