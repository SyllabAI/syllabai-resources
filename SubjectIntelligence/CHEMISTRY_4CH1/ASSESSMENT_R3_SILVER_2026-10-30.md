# ASSESSMENT_R3_SILVER — Independent silver-tier ER review (2026-10-30)

**Mandate.** The r1 external-review recommendation's residual — an *independent
silver-tier ER review before production reliance* — executed by operator order
(trace `1a18bf09d58eea5d`, fresh PAT supplied same trace; the previously exposed
PAT is retired by this substitution). Silver tier = systematic full-corpus
verification (not the r1 sampled pass), executed independently of the authoring
pipeline's own gate code.

**Independence posture (disclosed).** The verifier
(`runs/SIB-CHEMISTRY_4CH1-ASSESS-R3/scripts/`) was written fresh for this
review: its own citation grammar, pack-chain, census and pin logic. No pipeline
validator code was executed; the pipeline's receipts are used only as
reconciliation comparators. The D6-class structural limit still applies: the
review shares the authoring agent's runtime, so independence is code-level, not
organizational. The pipeline's gate outputs were reproduced, not trusted.

**Surface of record:** tip `5f170f98` (syllabai-resources, main), 95 published
artifacts; pastpapers live tip `8003727c`; validator pin unchanged `357ace0a`.

## Results by leg

- **L1 — pack-of-record chain (zero-append):** 57/57 `pack_carry.json`
  assertions re-verified byte-exact (per-artifact sha256 + origin-run
  cross-check, D3 tranches RUN-017..022); 0 non-D3-identical packs; every
  artifact's D3-era pack copies byte-identical across all runs carrying it.
- **L2 — citation resolution (full corpus, independent grammar):** 1,992/1,992
  citation tokens in the 95 published files resolve against their pack of
  record (1,900 located + 92 identity; 0 violations; 0 unparseable; prose-form
  locators all path-resolved). Coverage law verified: page-grain, JSONL
  single-line, and cited markdown ranges ⊆ union of held windows.
- **L3 — quoted-span binding:** 852 prose-quote spans extracted independently;
  730 bound verbatim on first pass; 122 adjudicated three-way (pack → raw source
  → fuzzy, incl. hyphen-wrap join and PDF text extraction): 60 bind under
  aggressive normalization; **1 genuine finding (F-S1)**; 61 manually classified
  as non-verbatim-claim content — 17 author connective lead-ins ending where a
  real quote begins, 44 author-side quotes legal under the corpus's own grammar
  (MIS-family `[OBSERVED_IN_SOURCE]` = "quotes **or directly paraphrases**" per
  the RUN-011 legend; schematic templates; author arithmetic/fact quotes such as
  MIS-01's "24 reports across the 8 sessions", which is true per BL-001/BL-002)
  — **0 fabrications, 0 unexplained spans, 0 unadjudicated residue**.
- **L4 — census arithmetic:** REQUIRED-core recount = **88 artifacts /
  763 records / 149,136 words** — all three exact against the RUN-022 close-out
  claims; whole-file family medians reproduce of-record values (GAP 2,120,
  PED 1,696, PRA 1,693, TUT 1,965-rounded); total library 833 records.
- **L5 — T5 OCR caveat:** all 10 TUT artifacts carry the OCR-basis disclosure;
  `gate_resolution_sb1_ebook.json` present and wired (operator ruling trace
  `1a188a28859dc5c9`); TUT quotes bind to the OCR text of record (L3).
- **L6 — post-lifecycle red state:** all six D3 runs carry the identical F4a
  red state **{SIB-MANI-007: 88, SIB-MANI-011: 4, SIB-MANI-012: 7}** across
  three scoreboard encodings (full-issue list → counts → distilled receipt;
  encoding evolution disclosed); qa-reports 95/95 present.
- **L7 — pastpapers source plane:** 46/46 distinct pinned paths present at the
  live tip, **46/46 sha256 byte-identical** to pack pins (zero drift).
- **L8 — resources source plane:** 83/83 distinct pinned paths present at tip;
  **40/83 byte-identical**; **43 drifted, all in `Official-ExamQuestion/
  igcse-chemistry-19/`** (F-S2); 0 missing, 0 unexplained.
- **Reconciliation:** gate-time r3 counts (RUN-017..022: 79+112+279+302+169+174
  = 1,115 citations / 0 violations over re-gated deployed bodies) are consistent
  with the 1,992-token published surface (deepening runs re-gated whole family
  bodies; the published corpus accumulated pre-D3 + D3 content).

## Findings

- **F-S1 (low, citation-coverage gap — genuine):** ASM-014 (RUN-005-authored,
  pre-D3) quotes *"State what is meant by the term isomers."* with **no citation
  token of its own**; the neighboring token cites the next quote's file/window
  (`2020-01 … lines 274-288`), and the quoted sentence (raw
  `2019-06/4CH1-1C/questions.md` line 746) sits **outside all held windows** of
  ASM-03's pack of record. The quote is verbatim-true at the raw source (verified
  at tip) — a provenance-locator gap, not a fabrication. Fix path (operator
  order required): a pack-append run adding the covering window, or re-pointing
  the record; the zero-append law means packs change only through the append
  gate.
- **F-S2 (informational, benign drift):** 43/83 resources pins advanced at tip
  after pack build — uniformly `igcse-chemistry-19` parse debris removal by
  later oeq converter waves (stray header/footer fragments; 6 changed lines in
  the sampled file; zero chemistry-content change). The packs' build-era
  excerpts remain the immutable text of record; pastpapers plane untouched
  (46/46). Recommended: note the drift class in the next source_pin_state
  refresh; no repair required.
- **F-S3 (scope note):** quoted author-side content is not verbatim-source
  material under the corpus's own claim-type grammar — the MIS-family legend
  (RUN-011) defines `[OBSERVED_IN_SOURCE]` as quote-**or-paraphrase**; schematic
  templates and author arithmetic quotes make no verbatim claim. All such spans
  were classified (not failed) and are listed in the adjudication receipts.
  No action.

## Verdict

**CLEARED for production reliance at silver tier.** The evidence-claim chain is
real end-to-end: citations resolve, packs are byte-identical to their origins,
the census is exact, the red state is stable, and the source planes are intact
(one locator-coverage gap, one benign drift class, both disclosed above).
Residual beyond this review's tier: organizational independence (D6-class) and
the Pearson silver-gated ER acquisition queue (GAP-SRC-001, unchanged).

Receipts: `runs/SIB-CHEMISTRY_4CH1-ASSESS-R3/` (silver_receipt.json,
quote_adjudication.json, quote_hyphenjoin_recheck.json, pins_receipt.json,
scripts/).
