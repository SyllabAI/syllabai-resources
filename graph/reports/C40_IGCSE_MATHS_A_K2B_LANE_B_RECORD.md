# C40 — K2 Lane B (Chunk Substrate) — igcse-maths-a

**Generated:** 2026-10-02T07:46:12+00:00  |  **Baseline:** `d63262196586d77f3ff53242ecb98e9a40fd579f`
**Operator directive:** "fire K2-B (chunk substrate), run the §18 HUMAN_VALIDATED
promotion round over the 73 edges" (2026-10-02, zai-web) — this record covers the
K2-B half; the §18 round over the 73 authored semantic edges is the T-C41 record.

## What this is

The C31 §6 Lane B build replayed for subject #2: the T-C13/C13 chunk→SP
substrate constructed over the maths-a notes corpus, emitting
`graph/igcse-maths-a/spec_chunk_mappings.yaml` — **860 anchored rows** +
2 unresolved-span worklist rows + 77 uncovered-SP
worklist rows = 939 rows, **111/188 codes covered** (exactly the C31 §3
notes-coverage bound). Registry: maths-a 8 → **9 stores — the K2 exit shape.**

## The anchoring axis (the honest tier difference, recorded)

Chemistry's Lane B refined a HUMAN_VALIDATED T-C10 quote store (209 rows) into
passage chunks. The maths-a upstream is the **T-C32 K2-A notes-join —
AI_VALIDATED (operator-delegated chain)** — and carries no evidence quotes. The
construction therefore anchors on the corpus's own structure: every note is a
sequence of SP spans introduced by the corpus's `spec_point` blocks (203
markers), the join resolves each marker to the ratified code, and each row's
evidence quote is the chunk's own verbatim self-slice (markdown-safe, ≤240
chars). The upstream tier is recorded verbatim on every row and in the store
meta (C31 §4.5). Nothing invented; no fabricated quotes; the single unresolved
anchor (`spcpt_QWXhzVp2S3VYZdZc`) stays on the worklist, never forced.

## Construction

- Tool: `scripts/c40_maths_a_chunk_sp_substrate.py@1.0.0` — deterministic, zero-LLM, fail-closed; convention
  `c40-chunk-convention-1` (the c13-chunk-convention-1 analog for the JSON block
  corpus); two independent constructions byte-identical (G7).
- Census: 191 notes / 203 spans / 862 chunks
  (0 intro + 862 section).
- Gates G1–G7 all green at construction; landing battery P1–P10 ALL PASS
  (`graph/reports/C40_MATHS_A_K2B_LAND_CHECK.json`).

## The operator review sheet (the promotion gate)

`graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md` — **468 Part A**
anchored spot-checks (seeded stratified: join score <1.0 or absent at 100%,
score == 1.0 at ceil(20%); the span-marker construction has no ambiguous rows by
design) + **79 Part B** worklist decisions. Gate rule (the C13 rule): Part A
precision ≥ 90% per class AND every Part B row decided → the rows may flip
SUGGESTED → HUMAN_VALIDATED **in a recorded deterministic apply step** — which
is NOT executed by this task; it waits on the sheet's fill and the operator's
sign-off (the store lands at SUGGESTED, anti-forgery G5 holds).

## Not done (deliberate)

- No HUMAN_VALIDATED anywhere in the emitted store.
- No chemistry bytes touched; no corpus writes; no other store touched.
- No K3/K4 work (playbook-deferred).

## Pins

| Artifact | sha256_16 |
|---|---|
| `graph/igcse-maths-a/spec_chunk_mappings.yaml` | `bf11cf0e7bc98287` |
| `C40_MATHS_A_CHUNK_SP_SUBSTRATE_REPORT.md` | `ab7e15cb0ffa7f50` |
| `C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md` | `e3a1b65508cc784f` |

