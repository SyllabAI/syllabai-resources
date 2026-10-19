# T-C42 R2+R3 — Join Re-run + Substrate Re-build (igcse-maths-a, 4MA1 Higher)

- **Stage**: R2+R3 of the C42 K2-B rework scope (`C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.json`) — the two agent-deterministic lanes; no operator gate sits between R1 and R4.
- **Directive**: "fire R2-R3" (operator, 2026-10-02, zai-web), following the R1 verdict round (`6ade129`).
- **Executed by**: operator-delegate, deterministic construction only, every gate fail-closed. Zero promotion: the substrate stays SUGGESTED; the C41-promoted 73 HUMAN_VALIDATED edges are untouched.
- **Head before**: `6ade129`.

## 1. Input pins

| Input | Identity |
|---|---|
| Amended resolution (R1 product) | `SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json@05a57b056874e8dd` (pre-repair baseline `3a0b5dc48a65fb54`) |
| Pre-R2 join blob | `1fe9da180ad4ea5e411e35483ec3f9b52e8a908d` |
| Pre-R3 substrate blob | `f3b2cc2be76934ee3b547a9b4e75d41581ceb6a6` |
| Section override map | `scripts/c42_section_overrides.yaml` — 16 entries = 12 REATTRIBUTE + 4 RETAIN |
| Workspace | sparse cone extended by `SME-RevisionNotes/igcse-maths-a-18-higher` (local `.git/info` only, the R1 precedent); corpus byte-frozen |

## 2. R2 — T-C32 join re-run

Tool: `scripts/c32_notes_maths_a_join.py` under a **dated T-C42 R2 amendment** (P5: landed records never edited; the generator is re-pinned instead). The 202/1 census guard moved to **200/3 with the exact post-R1 unresolved id set pinned** — anything else fails closed.

Result (artifact `Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`):

- **200 joined / 3 unresolved / 203 anchors / 0 foreign codes** — exactly the census computed from the amended resolution before the run.
- **119/188 distinct codes** (was 111 under the defective mapping).
- Wording census **EXACT 175 / LEDGER_EXPLAINABLE 25** — the R1 Foundation re-pointing is visible in the join itself: AFFIRM anchors carry bare official ids (`IGCSE_MATHS_A:2.2B`) with Foundation wording and read LEDGER_EXPLAINABLE against the Higher-operative store wording, while genuinely-Higher anchors on the same codes keep `H-` ids and read EXACT. The C30 tier-dedupe ledger structure surfacing exactly as the R1 key finding predicted.
- Unresolved = the C31 §3 residual (`spcpt_QWXhzVp2S3VYZdZc`, KEPT UNRESOLVED at R1) + the 2 anchors the R1 verdict cleared (`spcpt_8Wtthy9gt8B5xsVW` Mathematical Symbols, `spcpt_3fMGfNtg3hXMg6gC` Problem Solving with Areas). All three carry PROPOSAL-ONLY candidates from the same deterministic scorer; they bind nothing; no code was forced.
- All 22 CORRECT codes landed verbatim (spot-verified: Exchange Rates → 1.10C, Negative Numbers → 1.1C, Length of a Line → 4.8A, Angles in the Same Segment → 4.6C).

## 3. R3 — C40 substrate re-build

Tool: `scripts/c40_maths_a_chunk_sp_substrate.py@2.0.0` under a **dated T-C42 R3 amendment**. G2 re-pinned to 200+3 (exact id set); the **operator section-override map is consumed FAIL-CLOSED**; coverage + worklist recomputed. The chunker, `c40-chunk-convention-1`, the evidence-quote discipline and every anti-forgery gate are untouched.

Result (artifact `graph/igcse-maths-a/spec_chunk_mappings.yaml`):

- **928 rows = 854 anchored + 8 unresolved-span worklist + 66 uncovered-SP worklist** (was 939 = 860 + 2 + 77).
- **Coverage 111 → 122 of 188**: gained 13 (corrected codes 1.1C, 1.7A, 1.8A, 1.11A, 2.3A, 3.2D, 3.3A, 4.4F, 4.10E, 6.3C, 6.3D + override codes 2.8C, 4.10C); lost 2 (`1.5C`, `6.3B` — wrong T-SPEC-7-era codes no other anchor covers). The C40-era 111-code bound stays on its own record as a measurement under the defective mapping.
- **Worklist recomputed**: unresolved-span rows 2 → 8 (residual keeps 2; the 2 cleared spans contribute 6 content chunks); uncovered-SP rows 77 → 66. Every row carries a disposition naming its surface (C32 §3 residual vs C42 R1 surface 1).

### Chunk identity invariant — HOLDS

The `(note_path, ordinal, heading, sha256_16)` multiset of all **862 chunk rows is IDENTICAL** to the pre-R3 blob (W3). note_path/ordinal/heading/sha256_16 never moved; only code attribution changed.

### Override consumption (fail-closed)

Every entry hit exactly one emitted chunk row; every `current_code` matched the join-derived code — an **independent validation of the R1 override projection** against the refreshed join; REATTRIBUTE targets verified inside the ratified 188; census pinned 16 = 12 + 4; zero duplicates; zero overlap with verdict anchors. Applied rows carry `provenance.override {source (map sha), operator_round, action, evidence}` so the R4 re-fill sees exactly what the operator ruled. The 4 RETAIN rows are recorded verbatim (two heading-only chunks = the known R4 re-fill limitation; averages-from-tables mode = same wording-tier artifact class).

## 4. Re-attribution reconciliation

All 862 pre-R3 chunk rows replayed (W4): **89 rows re-pointed on the 22 CORRECT anchors; 82 rows code-unchanged on the 21 AFFIRM anchors** (upstream official_id/official_wording re-pointed to the Foundation statement; EXACT → LEDGER_EXPLAINABLE where applicable); 12 REATTRIBUTE + 4 RETAIN overrides; 6 rows demoted to worklist; the remaining **669 non-surface rows verified ZERO-DRIFT** (spec_code AND upstream fields).

Bookkeeping note: the scope record's "189 anchored store rows" was the C40 **fill-record** count (rejected verdict rows) over the 45 defective joins; the substrate-side measurement under the same 45 anchors is 177 (89+82+6). Both stand on their own records; the delta is bookkeeping base, not a defect.

## 5. Verification battery — ALL PASS 7/7

`scripts/c42_r2_r3_join_substrate_check.py` → `graph/reports/C42_R2_R3_CHECK.json`, exit 0, deterministic:

| Gate | Result |
|---|---|
| W1 join refresh | 200/3/203, 0 foreign, exact unresolved set, resolution pin == amended disk file, 22/22 CORRECT landed |
| W2 substrate shape | 928 = 854 + 8 + 66; covered 122; all SUGGESTED / RULE_DERIVED; upstream tier verbatim |
| W3 chunk identity invariant | 862-row identity multiset identical to pre-R3 blob `f3b2cc2b…` |
| W4 re-attribution audit | full replay: 89 + 82 + 12 + 4 + 6 + 669 = 862, zero unexpected drift |
| W5 coverage / worklist | 111 → 122, gained/lost as above; worklist complete; mapping_ids unique |
| W6 protected surfaces | dirty set == R2/R3 footprint exactly; Lane C stores byte-identical to `6ade129`; chemistry + spec-links + records untouched |
| W7 determinism | substrate re-run byte-identical; join re-run content-identical modulo generated_utc |

## 6. Staleness after this landing

- **Fresh**: T-C32 notes-join (R2); C40 chunk substrate (R3); coverage + worklist (R3).
- **Superseded at R4**: the C40-era fill verdict record (468 rows) and review sheet — R4 renders a FRESH re-stratified sheet over the rebuilt surface and re-fills under the C12/C13 convention.
- **Separate follow-up (not fired)**: spec-links refresh, armed by the R0 census; sme_spcpt_verify legacy BASE pointer (operator queue).

**Standing instruction for R4 (carried from R1)**: the re-fill MUST consult BOTH tier wordings — the store's Higher-operative wording AND the C30 tier-dedupe ledger's `foundation.text` — or it will re-reject exactly the 21 wording-tier artifacts and the ≥90% per-class gate can never pass.

## 7. Scope guards honored

`graph/igcse-chemistry/**`, `parsed/**` canonical JSON, the Lane C stores (concepts 82 / concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`, the C25–C41 records and the C42 scope/R0/R1 records, and both SME corpora — all byte-untouched (W6). The `c40-chunk-convention-1` forward contract survives (W3). No store row is anything other than SUGGESTED / RULE_DERIVED (W2).

## 8. Footprint

- `Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json` (R2 refresh)
- `graph/igcse-maths-a/spec_chunk_mappings.yaml` (R3 rebuild, 928 rows)
- `scripts/c32_notes_maths_a_join.py` (R2 amendment), `scripts/c40_maths_a_chunk_sp_substrate.py@2.0.0` (R3 amendment)
- `scripts/c42_r2_r3_join_substrate_check.py` (new battery) + `graph/reports/C42_R2_R3_CHECK.json`
- `graph/reports/C42_R2_R3_JOIN_SUBSTRATE_RECORD.{md,json}` (this record)

**Next gate**: R4 re-gate (OPERATOR EVIDENCE, gate 2) — fresh re-stratified review sheet, both-tier-wording fill, ≥90% per-class required, Part B re-decided. The operator's choice to fire.
