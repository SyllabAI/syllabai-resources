# run-012 wave-C — the L4 mapping-repair dossier (T-OEQ-PHYS-FORMAT-1)

Date: 2026-11-03. Closes the last open population of the run-012 reconciliation
(RULE-1): the 22 cross-id fields / 20 parts / 17 questions / 10 topics.

## 1. What the definitive per-question census found

The run-012 census classified the 22 fields as "id-swap" (direction uniformly
`plane == corpus@other`, same topic) and split them into a "boilerplate reuse"
sub-class (DISC-5a) and "true mapping drift" (2 pairs, RES-1/DISC-5b). The
wave-C per-question census (`dup-census-post-wave-b.json`, all 2,270 md fields
over 489 questions) refines that picture decisively:

**Every one of the 22 fields is the same mechanism: the plane serves the LAST
part's content under an earlier part's id of the same question.**

- 18 `solution_md` fields across 17 questions: each affected part carries the
  solution of the LAST part of its own question (in `qstn_K6yxfXjpJXp5sSyG`,
  parts 0–3 ALL carry part 4's solution).
- 2 of the 17 questions additionally have the affected part's `problem_md`
  collapsed the same way (`qstnprt_Vn36YRgjsBNv8BK2`, `qstnprt_ZTrm3d8Qwgth5z94`
  — the middle parts of 3-part questions carry the last part's problem+solution).
- 0 fields unmatched: every plane value resolves EXACTLY (post-L3
  canonicalization) to a corpus sibling's content. Zero invention, zero ambiguity.

The census's "boilerplate reuse" reading is thereby superseded: the "generic
solution shared by 4 plane parts" (`qstnprt_PnYK8tkCjzCjtwG3`) is simply the
last part of `qstn_K6yxfXjpJXp5sSyG` whose content the build wrote into all five
parts. The corpus's per-part solutions are distinct and of record.

Consequence: the corpus of record is complete and correct on both sides of every
"class-B pair" (ZTrm↔CZmG, Vn36↔hV5T) — there was never a symmetric swap. The
plane lost the earlier part's content and duplicates the last part's.

## 2. Mechanism confirmation (per the L4 law): when and where

| evidence | commit / state | ZTrm content | 9PZG solution | verdict |
|---|---|---|---|---|
| corpus 7-1/5-3 topic.json, earliest visible state | 5f2ee275 (2026-09-17) | Po-210 ✓ | per-part ✓ | corpus mapping original |
| corpus at every later sha (09-18, 10-19 ×4, 10-24, 10-30, 11-01..03, 6ee5ada) | — | Po-210 ✓ | per-part ✓ | corpus stable, never swapped |
| v2 bank at birth | 3a92153e (2026-10-04 seed, hub import @ 93226a43) | Po-210 ✓ | per-part ✓ | plane born CLEAN |
| v2 bank after T-CONSUME-EDX-1 | 2ece53bf (2026-10-20, re-import @ 6ee5ada) | Po-210 ✓ | per-part ✓ | still CLEAN |
| v2 bank after T-CONSUME-EDX-2 | c2388bca (2026-10-21, "49 Edexcel packs rebuilt + the full EDX-1 post-build stack re-applied") | gamma ✗ | last-part ✗ | **COLLAPSE INTRODUCED HERE** |
| v2 bank at every later sha (10-22 MCQ backfill, 10-27 cutover, 10-30 G-E4 normalize, 11-01..02 RN-DEBRIS 3–9, run-009-r2, F131) | — | gamma ✗ | last-part ✗ | collapse persisted untouched |

- The current importer of record (`apps/hub/scripts/import_corpus/build_bundles.py`)
  is field-faithful (1:1 verbatim `problem_md→problemMd` per part; no collapse
  logic) — the corruption site is the **T-CONSUME-EDX-2 run's post-build stack**
  (its "span patch / fix_tail / clean-segment grafts" parallel-tree pairing), not
  the standing build path. Sub-step attribution inside that run is a platform-lane
  follow-up (receipt of record: v2 `.syllabai/receipts/T-CONSUME-EDX-2/`).
- Pre-wave anchor proof (`dup-census-pre-wave-a.json` @ the run-012 census merge
  63c23d0a): the COPY-of-sibling set is exactly the same 22 (pid, field) pairs as
  post-wave-B — waves A/B never touched this population (their 105 adopted fields
  appear there as the pre-wave "OTHER" bucket, 62+43=105 ✓).

## 3. Repair law applied

RULE-1 L4 says the cross-id class is "mapping-repair, never field-verbatim
adoption" — written for adoptions INTO the corpus. Here the corpus of record is
the correct side, so the repair restores the true id→content pairing ON THE
PLANE: **plane := corpus of record verbatim** (the reverse of L1), with asset
hrefs hotlinked at the declared data cut using the exporter's own `hotlink()`
semantics (the plane's URL-pinning convention, L3). 22 field writes.

## 4. The serving leg (v2 PR)

- `questions.json`: 22 fields / 20 parts / 17 questions / 10 topics; T1
  serialization preserved (indent=1, ensure_ascii=False, no trailing newline).
- Gates T1/G1–G6 all green in-run (see the v2 serve payload:
  `.syllabai/lane-artifacts/T-OEQ-PHYS-FORMAT-1/run012-wavec-serve-payload.json`).
- L6 drift-delta: raw drift 750→732 fields / 565→554 parts; **non-benign 22→0**.
  18 of 22 served fields raw-equal; 4 asset-bearing fields canon-equal (benign
  URL-encoding); zero unrelated movement (G1 deep-diff).
- Learner impact: the two questions whose part-(b) was unserved since 2026-10-21
  (`qstn_hXjpCk7PMZPn2xst` 7-1 Po-210 grid question — the run-011-m3 M3-repaired
  isotope notation reaches students for the first time — and `qstn_x3gPVCnBWZZS5Dd4`
  5-3 molecules/sentences question) plus the 15 solution-collapsed questions serve
  their true per-part content again.

## 5. Cross-course observations (recorded, out of lane scope)

- **Chemistry SME bank** (28 sets / 524 questions / 1,404 parts, same census
  semantics): 542 differing fields, NONE carrying the exact sibling-copy
  signature — the EDX-2 collapse class is not detected there. Chemistry's own
  corpus↔plane drift surface stays owned by the chemistry lanes.
- **Official physics bank** (`official-papers.json`): born 2026-10-27 (post-EDX-2)
  from the exporter of record and continuously G-E1/G-E4 gate-verified since —
  structurally protected; not touched by this wave.

## 6. Ledger deltas carried by this wave

- RES-1 (`qstnprt_KK5wsxWXhgZcnNFV`, 7-2 camera-lens): CLOSED — reconciled by the
  run-010-m2/run-011-m3 adoptions; the run-012 residual classifies benign-style
  (LRM/URL encoding), canon-equal at main.
- DISC-5a ("boilerplate reuse"): SUPERSEDED by the definitive census (§1) — same
  collapse mechanism, no benign shared-boilerplate sub-class exists.
- RES-2: unchanged (qmd re-baseline discipline; wave-C touches no corpus/qmd
  bytes — the corpus of record is untouched by this wave).
- New: the EDX-2 stack attribution (§2) — filed for the platform lane; any future
  re-import/rebuild of the physics bank must re-run this census before shipping.
