# C31 — Subject-#2 K2 Scope Record — igcse-maths-a (4MA1 Higher)

| | |
|---|---|
| **Task ID** | T-C31 (K2 scoping of the C28 per-subject commissioning playbook, spec §6) |
| **Version** | 1.0 — K2 scoped, NOT executed. Every store byte, join artifact and batch authoring this scope describes remains behind the operator gates it names (§8). |
| **Date** | 2026-10-01 |
| **Operator directive** | "want K2 scoped" (2026-10-01, zai-web, inline) — arming the T-C30 K1 landing |
| **Baseline** | syllabai-resources `origin/main` @ `2e57663f16a478c8a0f6670140e469c2bd902ac5` (T-C30 K1 @ `451d6c4` + the C11 projection-review verdict @ `2e57663`; local == remote, tree clean at scoping time) |
| **Predecessors** | `C29_IGCSE_MATHS_A_K0_COMMISSIONING_RECORD` (§3 names the join as the first K2-lane prerequisite); `C30_IGCSE_MATHS_A_K1_SPEC_STORE_BUILD_RECORD` (§5 arms K2, chemistry sequence replayed); `C28_MULTI_SUBJECT_EXPANSION_SPEC` §6-K2 gate definition |
| **Verification** | `scripts/c31_k2_scope_check.py@f271e5cfc6e001c5` → `graph/reports/C31_K2_SCOPE_CHECK.json@4d492fe28c77936d` (G1–G7 all PASS, exit 0) |

---

## 1. What K2 is (the playbook row, instantiated for subject #2)

C28 spec §6 defines K2 — **ratified enrichment (chemistry sequence per qual)** — as a
four-lane sequence, each lane with its own gate class:

| Lane | Pattern | Produces for `graph/igcse-maths-a/` | Gate |
|---|---|---|---|
| **A — note-level mapping** | T-C10 | the notes↔SP join artifact that every later lane anchors on | human-validated tier recorded honestly; 0 fabricated anchors; every mapped code ∈ the canonical 188 |
| **B — chunk substrate** | T-C13 | `spec_chunk_mappings.yaml` (c13 chunk→SP quote-anchor substrate) | review sheet, **≥90% class precision** |
| **C — concept pilot + §16 batches** | T-C11 | `concepts.yaml` + `concept_edges.yaml` + `spec_command_kinds.yaml` | **per-batch operator verdict gate** → §18 promotion; zero silent promotion; held quarantine preserved |
| **D — concept→SP substrate** | T-C19 | substrate rows + review sheet + apply record | review sheet + apply record |

The registry comment written at K1 is the store-level commitment this scope
fulfills: "concepts/edges/chunk-maps/kinds arrive with K2, relationships with
the ratified-hierarchy lane" — i.e. K2 exits with the maths-a registry entry
carrying **9** stores (5 + the 4 deltas), relationships deliberately absent.
For scale, the chemistry replay produced 193 concepts / 488 edges / 181
command-kinds / a 779-chunk mapping registry; the maths-a forecast is §5 below.

## 2. The scoping discovery: Lane A's substrate already exists

The K0 record (§3) carried forward one gap as the program's first K2-lane
prerequisite: *"No maths-a equivalent join exists — the qual's SME index is
name-only (203 `spec_point_links` in the manifest are unvalidated anchors), and
the parse_report prescribes mapping-stage name bridging."*

Scoping finds that statement is **correct as written but materially narrower
than the truth**: the corpus-side resolution substrate the chemistry join
consumed already exists for this qual.

- `SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json`
  (sha256_16 `3a0b5dc48a65fb54`) — **222 ids, 218 resolved, 4 unresolved**;
  validation string: **AI_VALIDATED (operator-delegated chain)** via the
  T-SPEC-7/8/9/10 operator-verdict rounds (2026-09-19, "mappings reasoned
  directly against the committed registries and the official Pearson PDFs, no
  scripted matching, no upstream tickets, PMT excluded as source"). Each
  resolved row carries `resolved_code`, `official_id`, `official_wording`,
  `sme_name`, `tier`, `method`, `score`.
- The notes corpus (`igcse-maths-a-18-higher`, 191/191 pages, 0 failures,
  sha256_16 `cc470d40873f51a4`) anchors **203 `spcpt_*` ids** across its 191
  note JSONs — the same id namespace the resolution file defines.

So the maths-a Lane A is **primarily a deterministic id-lookup join plus
validation against the ratified store**, not a from-scratch fuzzy name bridge.
The P5 disposition: K0's sentence stands unedited in its own record; this
record is the dated correction that narrows its scope. Nothing was weakened —
K0(ii) cleared corpus securing then, exactly as it does now.

## 3. Lane A census (machine-verified this assessment)

From `C31_K2_SCOPE_CHECK.json` G2–G4 (all reads disk-first with git-show
fallback, methods recorded per read):

| Measure | Value |
|---|---|
| Notes anchors (sum over 191 note JSONs) | **203**, all distinct, every page carries ≥ 1 |
| Resolved deterministically by id lookup | **202 / 203** |
| EQ-unresolved ids reached by notes anchors | **1** — `spcpt_QWXhzVp2S3VYZdZc` "Discrete & Continuous Data" (the other 3 EQ-unresolved ids have null `sme_name` and are not referenced by the notes) |
| Notes ids absent from the resolution file | **0** |
| Foreign official_codes (∉ canonical 188) | **0** — hard-fail class, zero hits |
| Distinct anchored official_codes | **111 / 188** coverage (57 Foundation-applicability rows + 54 Higher) |
| Uncovered codes | **77** (51 Foundation-only + 26 Higher) |
| Wording crosscheck, resolution vs K1 store | **202 / 202 exact** after whitespace normalisation — 0 ledger-explainable, 0 divergent |

Two scope-shaping facts fall out of the census. First, the wording crosscheck
being **100% exact** means the resolution file and the K1 store agree on the
operative Higher-preferred statements for every anchored code — the 54-row
tier-dedupe ledger (`C30_MATHS_A_TIER_DEDUPE_LEDGER.json`, sha256_16
`7f9322a8a05d3767`) needs no reconciliation work inside Lane A. Second, the
**coverage profile (111/188)** becomes a standing input to Lane C: batches over
uncovered spans author from the ratified spec-text store alone, and each batch
packet must state its coverage profile so the operator's per-batch verdict is
made on visible evidence, not assumption.

## 4. Lane A execution shape (first prerequisite, now concrete)

1. **Build `scripts/sme_notes_maths_a_join.py`** — mirror of
   `sme_notes_chem_join.py`, zero-LLM, deterministic, verbatim preservation:
   join each note's `spec_point_ids` to the EQ resolution **by id**, attach
   `resolved_code` / `official_id` / `official_wording` / `method` / `tier`
   with provenance copied 1:1; nothing re-derived, nothing downgraded.
2. **Validate against the ratified store** — every mapped code ∈ the 188
   canonical set (foreign = fail); wording crosscheck re-run as a gate
   (exact / ledger-explainable / divergent census; divergent ≠ fail but each
   row dispositioned in the lane record).
3. **Residual disposition** — the single unresolved anchor
   ("Discrete & Continuous Data") plus any future drift: RECORDED, never
   fabricated (the chemistry rule). Its disposition (deterministic
   name→code match with score/margin gates, or operator adjudication) is
   decided at the K2-A gate.
4. **Output location (default)** — the **derived lane**, not the corpus: the
   standing K0/K1 scope guards hold SME corpora byte-frozen, so the join
   artifact lands outside `SME-RevisionNotes/**` (exact directory settled at
   build time; the parsed `_derived/` lane is the working precedent). Writing
   corpus-side is possible only as an explicit operator exception that amends
   the guards first (P5: dated amendment, not silent override).
5. **Validation tier recorded honestly** — chemistry's join stands on an
   operator HUMAN_VALIDATED legacy `spec_map`; maths-a has no equivalent. The
   lane record must state the actual tier achieved (AI_VALIDATED
   operator-delegated, plus whatever spot-check round the operator runs), and
   the "unvalidated anchors" phrase from K0 retires only when that tier is on
   record.

## 5. Batch plan (Lane C, §16 replayed)

Recomputed live at G5 and equal to the K0 §2 table: SP base **188**; pilot
envelope **451 nodes / 517 edges** (2.4 / 2.75 per SP); discipline-adjusted
forecast **188 concepts / 301 edges** (1.0 / 1.6 per SP — the chemistry
actuals ran 193 / 488, inside the pilot envelope); **16 batches** at the
sanctioned 12 SP/batch shape.

- **Slicing**: `B01..B16` cut on the ratified store's `global_order` windows
  (1–12, 13–24, … 181–188) — the canonical walk, mirroring chemistry's
  code-range slices. Exact per-batch code lists are emitted by the batch
  tooling at authorization time, not frozen here.
- **Per-batch pipeline** (the chemistry §16 shape, already proven across 11
  batches): intake-drift check → preverify → quote probe → term-audit probe →
  boundary check → review build → pass-2 review → **operator verdicts** →
  ruling finalize → verdict check → decisions → apply.
- **Standing batch discipline**: every batch passes an operator verdict gate
  before any promotion; zero silent promotion; held quarantine preserved
  (held SPs contribute quarantined rows only); provenance namespaces and the
  C27 damage scan (0 hits) apply to every store row.
- **Authorization shape**: one `c11_s16_authorization.yaml`-equivalent per
  batch commissioning, stored under `scripts/`.

## 6. Lanes B and D in brief

**Lane B (T-C13 pattern)** re-runs the chunk-convention-1 construction over
the maths-a notes corpus (chemistry reference: 112 notes → 779 chunks, 209
quote-anchored mappings, anchor rate 1.0, 181 codes covered) and emits
`spec_chunk_mappings.yaml` behind a review sheet whose class precision must
reach **≥90%** before apply. The maths-a anchor census (§3) sets expectations:
the chunk substrate spans the notes corpus, while its SP coverage is bounded
by the 111-code notes coverage — the worklist lanes (quotes, unmapped SPs)
are expected to be materially larger than chemistry's and are recorded, not
forced.

**Lane D (T-C19 pattern)** builds the concept→SP substrate rows after Lane C
has promoted concepts to work against, ships them as a review sheet + apply
record pair (the `C19_SUBSTRATE_ROWS.yaml` / `C19_CONCEPT_SP_SUBSTRATE_REVIEW_SHEET.md`
/ `C19_APPLY_RECORD` shape), and inherits the same zero-silent-promotion
discipline. Lane ordering follows the chemistry sequence: **A → B → C → D**,
with Lane B constructible in parallel with early Lane C batches if the
operator prefers (chemistry ran T-C13 strictly before T-C11; the replay
defaults to the same order).

## 7. Scope guards (standing through K2 execution)

Zero bytes in `graph/igcse-chemistry/**`, `parsed/**` canonical JSON, or the
SME corpora (unless §4.4's explicit corpus-side exception is granted first);
the C25–C30 records unedited — all corrections land as dated records of their
own; no core or hub serving behavior changes from this repo; no K3/K4 work
(projection re-pointing to the ratified stores, explorer build, release pins —
deferred by the playbook); the s105 title divergence stays a core-lane item as
recorded at K1 §2; the parallel chemistry C11 program (batch-11 verdict
session @ `2e57663`) is untouched by every lane. All ratified-plane writes
flow through the operator gates below.

## 8. The operator gate sequence this scope requests

| Gate | Authorizes | Evidence the operator sees |
|---|---|---|
| **K2-A** | Lane A build: join script + derived-lane artifact + lane record | the §3 census re-run on the joined output; the residual anchor's proposed disposition; the achieved validation tier |
| **K2-B** | Lane B build (chunk substrate) | chunk census + review sheet, ≥90% class precision |
| **K2-C-1..16** | each §16 batch in turn (commission → author → review → verdict) | per-batch packet: slice codes, coverage profile, diff-review bundle, held-quarantine state |
| **K2-D** | Lane D substrate apply | substrate review sheet + apply record |

K2 exit state: maths-a registry entry carries **9 stores**; `graph_check.py`
and `check_no_hardcode.py` green across both quals; a lane/batch record
series (C32+) with per-record sha pins; and the next natural gate is K3
(serving & explorer) exactly as the C28 machinery prescribes.

## 9. Verification battery (this assessment)

`scripts/c31_k2_scope_check.py` — zero-LLM, deterministic, read-only toward
`graph/`, corpora and `parsed/**` (writes only its own report; 199 reads, 193
served by the persistent git-show channel, 6 disk):

| Gate | Asserts |
|---|---|
| **G1** `k1_stores_present` | registry resolves exactly the 5 K1 stores; 188 rows / 188 unique codes; the 8 flagged rows alive with `math-fragment-assembly`; topics 6/39; K1 record + check + ledger present |
| **G2** `lane_a_substrate` | EQ resolution 222/218/4 declared == observed; AI_VALIDATED + operator-delegated + PMT-excluded in the validation string; notes manifest 191/191/0/203 |
| **G3** `anchor_join_census` | 203 anchors / 202 resolved / 1 EQ-unresolved / 0 absent / 111 codes covered / **0 foreign** (hard-fail class) |
| **G4** `wording_crosscheck` | 202 anchored rows classified: 202 exact, 0 ledger-explainable, 0 divergent |
| **G5** `batch_forecast_recompute` | 451/517 pilot; 188/301 adjusted; 16 batches; SP base 188 — equal to the K0 record's table |
| **G6** `registry_k2_target_shape` | maths-a == the 5 K1 stores; chemistry == the 10-store shape; K2 deltas + relationships absent for maths-a; shared reports dir |
| **G7** `state_snapshot` | HEAD == `2e57663f…`; `graph/` == chemistry + maths-a + reports; chemistry still 10 store files; battery read-only |

Result: **G1–G7 all PASS, exit 0** — `graph/reports/C31_K2_SCOPE_CHECK.json`
(sha256_16 `4d492fe28c77936d`, the landing run) at baseline `2e57663f16a478c8a0f6670140e469c2bd902ac5`.
