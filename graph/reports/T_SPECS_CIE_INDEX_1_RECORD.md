# T-SPECS-CIE-INDEX-1 — SME-native spec-point index harvest record

- Date: 2026-10-19 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace
  `1a153238abda24e1`)
- Operator directive: *"ignite the SME-native spec-point index harvest lane"* — fires
  NEXT lane #1 of the T-SPECS-CIE-VERDICT-1 record ("resolves the EQ-referenced dangling
  spcpt ids and gives the name-only substrates a real index to join against — the designed
  cure for most of the 4,386 structured pendings").
- Base commit: `c8eb6399` (T-SPECS-CIE-VERDICT-1, on origin/main).
- Lane script: `scripts/cie_spcpt_index_harvest.py` (deterministic engine, fixed stamp
  `2026-10-19T09:00:00Z`, byte-idempotent), battery `scripts/cie_index_harvest_check.py`.

## What was built

**44 per-course SME-native spec-point indexes** `SME-ExamQuestion/<cie-lane>/spec_point_index.json`
— one per CIE SME course lane — in the EXACT `syllabai.sme-spec-point-index/1.0` shape of
the 49-file Edexcel precedent (`scripts/sme_spcpt_harvest_all.py`), byte style mirrored
(indent=1, ensure_ascii=False, no trailing newline, fixed key order):

- `spec_points`: harvested from the notes' embedded spec_point blocks (`type`
  `spec_point`/`specPoint`, id `spcpt_*`) — `name`/`definition` verbatim, `notes` = the
  embedding note's `rn_*` id, `subtopic_slugs` = the note page stem. Name-only records keep
  `definition: ""` — nothing manufactured (AGENT.md rule 3).
- `notes_base` from the lane's notes manifest (fail-closed: exactly one manifest with
  `notes_base` required); `source_pages` = note JSON files read; `fetch_failures: []`
  (corpus-derived — zero fetching, unlike the Edexcel scrape-time harvest).
- `coverage`: the EQ question-part `spec_point_ids` references vs the index —
  **`missing_from_index` IS the explicit, machine-readable form of the corpus's dangling
  EQ-referenced spcpt ids** (previously an implicit pending state in the join sidecars,
  recorded as "corpus reality" by J6). This is the lane's designed resolution of the
  dangling accounting; no definitions are invented for the definition-less remainder.

## Results

- Universe: **8,651 spcpt ids** summed per lane (== the join lane's universe, sidecar
  `anchors.universe_ids` reconciled 44/44), **7,905 unique** across lanes (SME reuses ids
  across course trees); 2,179 with definitions / **6,472 name-only**.
- EQ coverage: **32,085 part refs → 5,540 unique ids → 5,218 covered / 322 missing**.
- Dangling 322 = **54 cross-lane curable** (defined in another CIE lane's notes — the
  designed input for a later cross-lane join round) + **268 definition-less in the entire
  CIE corpus** (no embedded definition anywhere — now explicit and machine-readable in
  each lane's `missing_from_index`).
- Top dangling lanes: igcse-business-25 198 (EQ references the 2027–2029 redeveloped
  syllabus ids its thin 51-id notes universe cannot cover), igcse-economics-25 43,
  igcse-maths-25-core 26, igcse-economics-20 20, a-level-maths-20-ps-2 16.

## Mechanism (deterministic, zero-LLM)

1. Enumerate the 44 lanes from `spec-links/cie-*.json`; per lane enumerate notes JSONs +
   notes manifest + EQ `topic.json` from the git trees.
2. Stream-read 5,622 blobs via parallel `cat-file --batch` (6 workers × 64-oid chunks,
   5-pass retry for promisor lazy-fetch lock contention; no worktree materialization of
   the corpus).
3. Harvest blocks (both `spec_point` and TipTap `specPoint` shapes), collect EQ part
   references, build the doc, serialize deterministically, stage via `git add --sparse`
   (the target dirs sit outside the sparse cone; the worktree write is the blob-delivery
   vehicle, the index entry is the deliverable).
4. Fail-closed sidecar reconciliation per lane (universe == `anchors.universe_ids`).

## Checks

Battery `scripts/cie_index_harvest_check.py` **H1–H10: 10/10 PASS**
(`graph/reports/T_SPECS_CIE_INDEX_1_CHECK.json`):

| id | check |
|----|-------|
| H1 | 44/44 well-formed (schema/stamp/key-order/course_slug/notes_base/fetch_failures/no-trailing-NL) |
| H2 | universe conservation vs fresh blob re-derivation + sidecar anchors, sum 8,651 |
| H3 | coverage arithmetic per lane + sums (32,085 refs / 5,540 = 5,218 + 322) |
| H4 | all 8,651 spec_point entries deep-equal vs fresh re-derivation (name/definition/notes/slugs) |
| H5 | notes/subtopic provenance internal to the lane corpus; source_pages == note files |
| H6 | dangling honesty (missing ∩ universe == ∅) + cross-lane cure analysis (54/268) |
| H7 | 49 Edexcel indexes byte-untouched; SME-ExamQuestion delta == exactly the 44 CIE files |
| H8 | footprint guard: status ⊆ declared set; spec-links/SME-RevisionNotes/Official-Specifications/SME-Flashcards untouched |
| H9 | engine fixed-stamp re-run byte-identical across all 44 files (sha256) |
| H10 | 2-lane independent in-battery rebuild (biology-23, maths-25-extended) == staged bytes |

Battery defect caught and fixed en route (recorded honestly): **H10's rebuild initially
emitted `spec_points` in encounter order** (`spec.items()`) while the engine emits sorted
order — json.dumps preserves insertion order, so the rebuild diverged byte-wise from the
staged files (the engine output was correct; H9's re-run determinism was green throughout).
Rebuild fixed to `sorted(spec.items())`; H10 then pinned the two sample lanes exactly.

## Footprint

- Added: `SME-ExamQuestion/<cie-lane>/spec_point_index.json` (44),
  `scripts/cie_spcpt_index_harvest.py`, `scripts/cie_index_harvest_check.py`,
  `graph/reports/T_SPECS_CIE_INDEX_1_RECORD.md`,
  `graph/reports/T_SPECS_CIE_INDEX_1_HARVEST.json` (engine stats),
  `graph/reports/T_SPECS_CIE_INDEX_1_CHECK.json`.
- Byte-untouched: all 49 Edexcel spec_point_index.json files (H7), all spec-links files
  (H8), SME-RevisionNotes/**, SME-Flashcards/**, Official-Specifications/** (H8).

## NEXT (operator-gated, NOT fired by this directive)

1. **Cross-lane join round for the 54 curable dangling ids** — a join/verdict round
   consuming the per-lane indexes (the index is now the canonical join substrate the
   name-only substrates lacked).
2. **Re-join against the index to cure the structured pendings** — the 4,386 verdict
   pendings (and the coded lanes' text pendings) can now fire against a canonical
   per-course index instead of blob-reconstructed universes; the 268 definition-less ids
   stay pending honestly (nothing invented, rule 3).
3. Learner-UI consumption (verdict semantics + T2_near hint) — unchanged from the verdict
   record.
4. R41-shaped re-gate — explicit instruction only; PAT rotation still CRITICAL-OVERDUE
   (fingerprint `a8ccee736aa8c75b`, 14 recorded plaintext transits).
