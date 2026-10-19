# C13 — Chunk→SpecificationPoint Mapping Substrate: Construction Report (quote-anchor construction)

**Status:** CONSTRUCTED — deterministic, zero-LLM, fail-closed; all rows `SUGGESTED` (RULE_DERIVED tier);
promotion to HUMAN_VALIDATED is the operator gate, never this tool.
**Upstream:** the T-C10 note-level store — 209 HUMAN_VALIDATED mappings living in the notes' `spec_map`
front matter (operator, 2026-09-11) — refined to chunk granularity per backlog/RETRIEVAL-DIAGNOSIS-2026-09-17.md (session-96), steps 1–2.
**Tool:** `scripts/c13_chunk_sp_substrate.py@1.0.0` — deterministic; double-run
byte-identical (gate G7); negative-tested by `scripts/c13_substrate_negative_test.py`.

## 1. What was built

The keystone data-construction step the diagnosis ordered: **a chunk→SP mapping store**. For every T-C10
note-level mapping, its verbatim evidence quote was anchored to the exact passage chunk it quotes, producing
a chunk-level row with full provenance. This is a granularity refinement of an already-validated store —
NOT a new mapping campaign.

- **Pinned chunk convention** (`c13-chunk-convention-1`): chunk 0 = intro (title + Excerpt + preamble);
  leaf sections cut at headings of level 2..4; **chunk text includes its own heading** (the C10 heading-quote
  lesson); anchoring targets content sections only — a quote that resolves only to the title/excerpt region
  is not a passage anchor and lands on the worklist instead.
- **Portable chunk identity**: `(note_slug, chunk ordinal, heading, sha256_16(chunk text))` — the forward
  contract the future T-C06 converter/ChunkingService must reproduce (fail-closed at join time otherwise).
- **Anti-forgery**: no row is emitted HUMAN_VALIDATED; every row carries `upstream.validation_status =
  HUMAN_VALIDATED` as a *reference* to the T-C10 store plus the derivation method and tool version.

## 2. Measured results

| Measure | Value |
|---|---|
| Notes chunked (all `spec_map`-bearing) | 112 |
| Chunks in the universe (intro + sections) | 779 (112 intro + 667 sections) |
| Upstream T-C10 mappings parsed | 209 (100% HUMAN_VALIDATED upstream) |
| **Anchored chunk-level rows** | **197 / 209 = 94.3%** |
| Worklist quote rows (unanchorable verbatim) | 12 |
| Worklist unmapped SPs | 1 (4CH1-4.15 — the registered C10 corpus gap) |
| Distinct SP codes covered by >=1 anchored row | 172/182 |
| Ambiguous multi-chunk matches (resolved: lowest ordinal, flagged) | 1 |
| Determinism (double-run) | byte-identical |

All 12 worklist quote rows resolve only to their note's **title/excerpt region** — i.e. the quote was taken
from the summary, not from a passage. The fix is enumerable: author a fresh verbatim section quote per row
(worklist below). No source-conversion corruption survived into the anchored set (the shared C10
normalization strips markdown escapes/links/emphasis on BOTH sides before matching).

## 3. Reconciliation with the session-96 audit

| Measure | Session-96 audit (harness never committed) | This construction (convention pinned) |
|---|---|---|
| Anchored mappings | 197/209 = 94.3% (196 exact + 1 fuzzy) | 197/209 = 94.3% (196 unique-exact + 1 exact-ambiguous, flagged) |
| Chunk inventory | 732 chunks (convention lost with the harness) | 779 chunks = 112 intro + 667 sections (convention pinned in the tool) |
| SP coverage | 169/182 | 172/182 |
| Worklist | ~25 rows (12 corrupted passages + 12 anchorless SPs + 4.15) | 12 excerpt-region quote rows + 1 unmapped SP (reason-classified per row) |

The headline reproduces exactly. The per-code worklist differs because the audit's chunker was never
committed — its split convention is unrecoverable. This construction therefore PINS the convention in the
tool (diagnosis step 3) and derives the worklist from the pinned convention, so the worklist is now
actionable and reproducible rather than historical.

## 4. The worklist (enumerable, not open-ended)

Worklist rows carry per-row reasons and dispositions in `graph/spec_chunk_mappings.yaml` (`worklist_reason`
+ `disposition`). Summary:

- **12 excerpt-region quotes** — author a fresh verbatim section quote per row (the notes
  teach these SPs; only the anchor is missing).
- **4CH1-4.15** — no note-level mapping exists (registered corpus gap: "no SME note teaches the formation
  explanation this point demands" — C10 GAP_ANNOTATIONS). Chunk-level mapping decision needed; C12 maps it
  at question level.

## Informational cross-check vs the frozen gold set (NOT a bench claim)

- Distinct gold spec points across labeled gold-v1 queries: **63**
- Gold spec points with >=1 anchored chunk-level row on the NOTES surface: **58**
- Caveat: the bench snapshot (snap-001) carries the 2,333 PAPER chunks only; the notes surface becomes scoreable end-to-end only after T-C06 ingestion + snapshot v2. This cross-check is context for the operator, never a §8(d) resolution number.
- Covered gold codes: 4CH1-1.10, 4CH1-1.11, 4CH1-1.16, 4CH1-1.17, 4CH1-1.18, 4CH1-1.26, 4CH1-1.27, 4CH1-1.28, 4CH1-1.29, 4CH1-1.3, 4CH1-1.30, 4CH1-1.31, 4CH1-1.32, 4CH1-1.33, 4CH1-1.34C, 4CH1-1.39, 4CH1-1.4, 4CH1-1.44, 4CH1-1.45, 4CH1-1.46, 4CH1-1.47, 4CH1-1.48, 4CH1-1.57C, 4CH1-1.58C, 4CH1-1.5C, 4CH1-1.6C, 4CH1-1.9, 4CH1-2.12, 4CH1-2.14, 4CH1-2.28, 4CH1-2.31, 4CH1-2.34, 4CH1-2.40C, 4CH1-2.4C, 4CH1-2.8C, 4CH1-2.9, 4CH1-3.1, 4CH1-3.10, 4CH1-3.11, 4CH1-3.12, 4CH1-3.13, 4CH1-3.21C, 4CH1-3.22C, 4CH1-3.4, 4CH1-3.6C, 4CH1-3.7C, 4CH1-4.13, 4CH1-4.14, 4CH1-4.19, 4CH1-4.29C, 4CH1-4.3, 4CH1-4.34C, 4CH1-4.37C, 4CH1-4.4, 4CH1-4.41C, 4CH1-4.45, 4CH1-4.46, 4CH1-4.5

## 5. What this does NOT claim

- **No row is HUMAN_VALIDATED.** The operator review sheet is the only promotion path (ruling-3-style
  spot-check with verdict boxes; <90% class precision → rework before any promotion).
- **The bench spec-resolution axis is NOT yet scoreable.** snap-001 carries the 2,333 paper chunks only;
  scoring flips only after T-C06 note ingestion (step 4) + snapshot v2 — recorded, never patched.
- **No production change.** This store is resources-repo graph-as-code, like T-C09/T-C10 before it.
- No new retrieval provider, no serving change, no core change.

## 6. Forward contract (T-C06)

When the notes corpus is ingested (`scripts/c13_build_note_package.py` → backend), the chunker MUST
reproduce `c13-chunk-convention-1` or the chunk identities fail closed at join time. The store's
`meta.convention_spec` is the normative text to pin in the production ChunkingService.
