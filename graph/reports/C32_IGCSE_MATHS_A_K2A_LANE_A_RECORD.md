# C32 — Subject-#2 K2-A Lane A Record — igcse-maths-a (4MA1 Higher)

| | |
|---|---|
| **Task ID** | T-C32 (Lane A build — gate **K2-A** of the C31 K2 scope, spec §4/§8) |
| **Version** | 1.0 — Lane A built. The notes↔SP join exists as a derived-lane artifact; 202/203 anchors joined deterministically, 1 residual RECORDED for operator adjudication. No store bytes, no registry change, no corpus write. |
| **Date** | 2026-10-01 |
| **Operator directive** | "K2-A (Lane A construction planning + connection artifacts)." (2026-10-01, zai-web, inline) — firing the first gate of the C31 scope |
| **Baseline** | syllabai-resources `origin/main` @ `49d71ba18e28a6e7d843bb2676e635b2b5276f62` (the T-C31 K2 scoping landing; local == remote, tree clean at build time) |
| **Predecessors** | `C31_IGCSE_MATHS_A_K2_SCOPE` (§4 Lane A execution shape, §2 substrate discovery); `C29_IGCSE_MATHS_A_K0_COMMISSIONING_RECORD` §3 (the join named as the first K2-lane prerequisite); `C30_IGCSE_MATHS_A_K1_SPEC_STORE_BUILD_RECORD` (the ratified store the join validates against) |
| **Verification** | `scripts/c32_k2a_check.py@ae273a287ad814f8` → `graph/reports/C32_K2A_CHECK.json@4b120a1429516122` (G1–G7 all PASS, exit 0) |

---

## 1. What landed

**Builder — `scripts/c32_notes_maths_a_join.py@4b164ba96b1dda39`** (zero-LLM,
deterministic, fail-closed; the `sme_notes_chem_join.py` mirror prescribed by
the scope, adapted to the substrate that actually exists). It walks the notes
corpus manifest + all 191 note JSONs, joins every `spec_point_ids` anchor to
the corpus-side resolution substrate **by id** (deterministic lookup, no fuzzy
matching anywhere in the resolved path), copies the resolved fields **1:1**
with `copied_1to1: true` / `fuzzy_matching_used: false` provenance on every
row, validates every mapped code against the ratified K1 store (foreign =
hard stop), and writes exactly one artifact:

| Artifact | Content | sha256_16 |
|---|---|---|
| `Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json` | schema `syllabai.notes-spec-point-join/1.0`; inputs pinned (manifest `cc470d40873f51a4`, resolution `3a0b5dc48a65fb54`, store, ledger `7f9322a8a05d3767`); **202** join rows + **1** unresolved row; census + validation-tier block | `7b428ea0b864abe4` |

**Directory decision** (left open by the scope, settled here): the artifact
lives at `parsed/_derived/notes-join/<course>.json` — inside the `_derived/`
lane (the working precedent for non-canonical artifacts), outside
`SME-RevisionNotes/**` (the byte-freeze guard holds), namespaced per course
so sibling quals can follow the same lane without collision.

## 2. The join census

| Measure | Value |
|---|---|
| Anchors walked (191/191 pages) | **203**, all distinct |
| Joined deterministically by id | **202** |
| Unresolved, RECORDED never fabricated | **1** (§3) |
| Ids absent from the resolution substrate | **0** |
| Foreign official_codes (∉ canonical 188) | **0** — hard-stop class, zero hits |
| Distinct official_codes covered | **111 / 188** (57 Foundation-applicability + 54 Higher — equal to the scoping census) |
| Anchor-level tier split | 86 Foundation-applicability / 116 Higher |
| Wording crosscheck vs the K1 store | **202 / 202 EXACT** (0 ledger-explainable, 0 divergent) |

**Substrate method census** (provenance copied verbatim from the resolution
file — the join adds no validation claims of its own): 83 × T-SPEC-7
operator-verdict name-fragment join; 54 × `name_to_statement_join`; 34 ×
T-SPEC-7 operator-verdict page-context join; 25 × T-SPEC-8 parse-repair
statement join; 5 × T-SPEC-9 operator verdict; 1 × T-SPEC-10 operator
reasoning round — 202 rows, every method string carrying "PMT excluded as
source".

**Validation tier on record** (the C31 §4.5 honesty rule): the artifact's
tier is **INHERITED AI_VALIDATED (operator-delegated chain)** on the
substrate + a deterministic 1:1 id-join machine-gated by `c32_k2a_check.py`.
**No HUMAN_VALIDATED claim is made.** The K0-era "203 unvalidated anchors"
phrase retires to this state: every anchor is now either joined through the
operator-worked substrate (202) or explicitly recorded as unresolved (1).
An operator spot-check round can upgrade the tier via a dated addendum — a
deterministic sample is provided in §5 for exactly that.

## 3. The residual anchor — RECORDED, never fabricated

`spcpt_QWXhzVp2S3VYZdZc` — "Discrete & Continuous Data" — the only
EQ-unresolved id the notes reach (the other 3 EQ-unresolved ids have null
`sme_name` and are referenced by no note). It lives in
`notes/6-statistics-and-probability/statistics-toolkit/discrete-and-continuous-data.json`
and is carried in the artifact with **no resolved code, no official_id, no
wording** — status `UNRESOLVED — RECORDED, NEVER FABRICATED`.

Per the scope (§4.3) its disposition is the operator's. The artifact carries
**PROPOSAL-ONLY** candidates from a transparent deterministic scorer
(0.5 × difflib(name, wording) + 0.5 × token overlap, +0.10 section prior
from the note's own tree section — the chemistry matcher's subsection-boost
pattern, binding nothing): top candidate `6.2C` at **0.6022**
("find the interquartile range from a discrete data set"), margin 0.1407.
Decisive discipline fact: **no proposal reaches the chemistry auto-join
floor of 0.75** — the scorer's honest verdict is that the sme_name is a
topic label, not a statement paraphrase, and the genuine mapping (if any)
needs operator reasoning of the T-SPEC-9/10 kind, not a scripted match. The
anchor stays unresolved until the operator rules; a T-SPEC-style operator
verdict can then be recorded corpus-side without touching this artifact
(it joins by id and would inherit the substrate on the next deterministic
re-run).

## 4. Verification battery (all PASS, exit 0)

`scripts/c32_k2a_check.py` — zero-LLM, deterministic, read-only toward the
graph, corpora and the parsed canonical plane (writes only its own report;
the EQ corpus reads serve through the C28-F1 disk-first/git-show fallback):

| Gate | Asserts |
|---|---|
| **G1** `artifact_schema_counts` | schema/task present; artifact re-censused from its own rows: 203 == 202+1; 111 distinct codes; tier split == the scoping census; declared counts == observed; validation-tier honesty block present |
| **G2** `provenance_verbatim` | all 202 rows × 10 copied fields byte-equal to the live substrate; resolution sha pin matches; `fuzzy_matching_used: false` and `copied_1to1: true` on every row |
| **G3** `store_agreement` | every code ∈ canonical 188; `store_row_code`/`store_global_order` agree with the live K1 store; every `wording_check` class recomputed and equal (202 EXACT) |
| **G4** `residual_not_fabricated` | exactly 1 unresolved; correct anchor; no resolved fields on it; PROPOSAL-ONLY method string; top proposal < 0.75 auto-join floor → operator adjudication required |
| **G5** `freeze_integrity` | HEAD == the T-C31 baseline; `git status -uall` shows **zero** tracked modifications and zero untracked paths outside the T-C32 footprint — corpora, canonical parsed bundle, chemistry and maths-a stores byte-identical to baseline |
| **G6** `no_store_or_registry_change` | registry sha unchanged (`e38965001ade4417`); nothing under `graph/` beyond this record's own report files (Lane A earns no store bytes — P3) |
| **G7** `standing_checkers_green` | `graph_check.py` exit 0; `check_no_hardcode.py` exit 0 on the post-build tree |

## 5. Operator spot-check sample (deterministic, every 20th join by store order)

| Code | sme_name → note | Substrate tier |
|---|---|---|
| 1.1F | Order of Operations (BIDMAS/BODMAS) → same-titled note | T-SPEC-7 name-fragment |
| 1.4D | Uses of Prime Factor Decomposition → same | T-SPEC-7 page-context |
| 1.8C | Bounds & Error Intervals → "Upper & Lower Bounds" | T-SPEC-7 name-fragment |
| 2.2E | Expanding Two Brackets → "Expanding Double Brackets" | T-SPEC-7 name-fragment |
| 2.8A | Solving Quadratic Inequalities → same | T-SPEC-8 parse-repair |
| 3.3G | Length of a Line → same | T-SPEC-7 name-fragment |
| 4.2D | Angles in Polygons → same | S2 name-ambiguous |
| 4.6C | Alternate Segment Theorem → "The Alternate Segment Theorem" (a **parse-flagged** code — flagged ≠ blocked) | T-SPEC-7 name-fragment |
| 4.11B | Maps → "Scale" | S1 name-match |
| 6.1B | Cumulative Frequency → same | T-SPEC-8 parse-repair |
| 6.3G | Relative Frequency → "Relative & Expected Frequency" | T-SPEC-7 page-context |

## 6. Scope guards honored

Zero bytes in `SME-RevisionNotes/**`, `SME-ExamQuestion/**`, the canonical
`parsed/igcse-maths-a/` bundle, `graph/igcse-chemistry/**`, or
`graph/igcse-maths-a/**` (G5 machine-verified); registry untouched (G6); no
core/hub serving behavior; no store bytes and no batch authoring (this gate
is Lane A only — K2-B/K2-C stay behind their own gates); the parallel
chemistry C11 program untouched. What Lane A arms: **K2-B** (chunk substrate
— the join gives chunk anchors their SP codes) and **K2-C-1** (first §16
batch — the join gives the coverage profile per slice: batches over the 77
uncovered codes author from the ratified spec-text store alone, stated in
each batch packet).
