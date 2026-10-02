# C40 — maths-a Chunk→SP Mapping Substrate: Construction Report (span-marker construction)

**Status:** CONSTRUCTED — deterministic, zero-LLM, fail-closed; all rows `SUGGESTED`
(RULE_DERIVED tier); promotion to HUMAN_VALIDATED is the operator review-sheet gate,
never this tool.
**Task:** T-C40 — K2 Lane B (chunk substrate) for igcse-maths-a, the C31 §6
instantiation of the T-C13/C13 pattern; the ninth and final K2 store.
**Upstream (recorded honestly per C31 §4.5):** the T-C32 K2-A notes-join —
202 joins / 1 unresolved, validation tier **AI_VALIDATED (operator-delegated
chain)**. Chemistry's Lane B refined a HUMAN_VALIDATED T-C10 quote store; the
maths-a join carries NO evidence quotes, so the anchoring axis is the corpus's
OWN structure: each note is a sequence of SP spans introduced by the corpus's
`spec_point` blocks (203 markers / 191 notes), the join resolves each marker to
the ratified code, and the row's evidence quote is the chunk's own verbatim
self-slice. Nothing invented; the tier difference is carried on every row.
**Tool:** `scripts/c40_maths_a_chunk_sp_substrate.py@1.0.0` — deterministic; two independent constructions
byte-identical (gate G7); corpus read disk-first with the persistent cat-file
fallback (the c32 convention).
**Corpus:** `SME-RevisionNotes/igcse-maths-a-18-higher` (manifest sha256_16 `cc470d40873f51a4`)
**Join artifact:** `Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`

## Census

| Measure | Value |
|---|---|
| Notes | 191 |
| SP spans (spec_point markers) | 203 |
| Chunks total (intro / section) | 862 (0 / 862) |
| Anchored rows (resolved spans) | **860** |
| Worklist rows — unresolved span | 2 (`spcpt_QWXhzVp2S3VYZdZc` 'Discrete & Continuous Data', the C32 §3 residual — operator adjudication pending) |
| Worklist rows — uncovered SPs | 77 |
| SP codes covered | **111 / 188** (the C31 §3 notes-coverage bound, exactly) |
| Anchored rows by join tier | P1_name_fragment_join 357, S1_name_match 203, P2_page_context_join 139, R1_parse_repair_statement_join 87, P2_operator_content_join 39, S2_name_ambiguous 35 |
| Convention | `c40-chunk-convention-1` |

The anchored surface spans the notes corpus: one row per content section chunk
of every resolved span (median chunk 566 chars; heading-only chunks kept — the
section heading is itself retrievable content, chemistry-parity behavior).
Coverage is bounded by the notes corpus's 111-code census exactly as C31 §6
forecast; the worklist lanes are recorded, not forced.

## Gates (fail-closed, all green at construction)

| Gate | Asserts |
|---|---|
| G1 corpus shape | 191 notes; 203 spec_point markers; every note's first block is its marker; manifest anchor counts == blocks |
| G2 join shape | 202 resolved + 1 unresolved; note-block anchors == join anchors ∪ THE residual; every join note_path in corpus |
| G3 code validity | every emitted code ∈ the ratified 188-point store (0 foreign) |
| G4 anchor fidelity | every row re-verifies quote-in-chunk + chunk sha256_16 against a fresh re-chunking after emit |
| G5 anti-forgery | zero HUMAN_VALIDATED rows; tier RULE_DERIVED; upstream tier recorded verbatim as AI_VALIDATED (operator-delegated chain) |
| G6 worklist completeness | every uncovered SP + every unresolved-span chunk enumerated with a disposition |
| G7 idempotency | two independent constructions byte-identical |

**Evidence-quote discipline:** the self-slice is deterministic (first ≤240
chars, whitespace-cut) and markdown-safe — the cut walks back over whitespace
boundaries until `norm(quote) ⊆ norm(chunk)` verifies (a raw prefix can land
inside a link/emphasis span where normalization diverges; the quote is only
ever shortened, never rewritten).

## Forward contract

Chunk identity (note_path, ordinal, heading, sha256_16 of chunk text) must
survive T-C06 ingestion — the converter/ChunkingService must reproduce
`c40-chunk-convention-1` or the rows fail closed at join time.

