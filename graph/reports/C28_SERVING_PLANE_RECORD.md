# C28 — Serving-Plane Record & D2–D5 Resolutions (Stage 4)

| | |
|---|---|
| **Task ID** | T-C28 (stage 4) |
| **Date** | 2026-09-21 |
| **Operator directive** | "Proceed with the next steps: D2–D5 remain open — serving plane, explorer mode, subject #2 (notes-corpus-gated …), batch-5 sequencing. Subject-#2 K1 is now just a registry entry + new graph/<qual>/ stores." (2026-09-21) |
| **Baseline** | `9e65d66` — stages 1–3 complete (registry, migration, record; D1=(a) executed) |
| **Content head** | `0c8c60f` — stage-4 commit (emitter + artifacts + S8) |
| **Battery** | **95 PASS / 0 FAIL / 0 WARN — ALL_STORES_CLEAN @ `0c8c60f`** (87 C27+C28 gates + 8 new S8 gates) |
| **Predecessor** | `C28_GRAPH_LAYOUT_MIGRATION_RECORD` (stages 1–3), `C28_MULTI_SUBJECT_EXPANSION_SPEC` (landed v1.1, byte-identical) |

---

## 1. Operator decision points — resolutions

| # | Decision | Resolution | Basis |
|---|----------|------------|-------|
| **D1** | Migration timing | **(a) EXECUTED** (stages 1–3: `639e38b` → `9e65d66`) | Operator ruling "a" on the staged a/b offer; see `C28_GRAPH_LAYOUT_MIGRATION_RECORD` |
| **D2** | Serving-plane location | **(a) ADOPTED + EXECUTED this stage** — serving plane = `Official-Specifications/parsed/_derived/graph/<qual>/` (extended; never a new `graph/_views/`) | Spec recommendation adopted under the proceed directive; the surface already exists, is 23/23 contract-pass, and is the established KG-loader face |
| **D3** | Explorer data mode | **(a) ADOPTED (near-term)** — per-qual self-contained HTML (v77 pattern). The blob is mode-agnostic by contract (spec §4.3): switching to a multi-qual HTML (b) or runtime fetch (c) later is a build change, not a data change | The v78 HTML build is a FileUpload-lane release with its own pins (follow-up §6); this stage delivers the data contract it consumes |
| **D4** | Subject #2 | **OPEN — gate RED (K0(ii))**. Notes-corpus-gated: no equivalent notes corpus exists for any candidate (`ial-chemistry` 319 SPs, `igcse-physics` 171 SPs, `igcse-biology`, …). Chemistry's own SME corpus is tracked in-repo (359 files) but is not materialized in this sparse workspace — the c13 in-repo corpus-presence guard fires (C28-F1); sandbox mode remains the supported path. Commissioning sequence: operator secures + names the corpus → K0 directive → K1 (which is now just a registry entry + new `graph/<qual>/` stores, per the operator's own framing) | Spec §6-K0(ii); measured this stage |
| **D5** | Batch-5 sequencing vs migration | **RESOLVED BY EVENTS** — the migration already executed, so "batch 5 first on current layout" is moot. T-C11 batch 5 (S2 Inorganic) will run on the post-migration layout: outputs land at canonical `graph/igcse-chemistry/` paths, registry-resolved. Its gates are unchanged and remain operator-held: "run batch 5" directive + own S1↔S2 and S3↔S2 cross-slice boundary rulings + per-batch verdicts | D1=(a) execution; spec §11 |

All four resolutions are reversible by operator errata before dependent work fires; nothing in this stage forecloses any future option (D3 modes share one data contract by design).

## 2. What landed (`0c8c60f`)

**Emitter — `scripts/c28_emit_explorer_blob.py@1.0.0`** (zero-LLM, deterministic; all store paths resolve through the C28 registry — no-hardcode scan clean). Emits, per K2-commissioned qual (P3), into the serving plane:

| Artifact | Content | sha256_16 |
|---|---|---|
| `parsed/_derived/graph/igcse-chemistry/concepts.yaml` | 113 node rows verbatim (98 CONCEPT / 15 MISCONCEPTION) + §5 provenance header | `a72f36c8af381727` |
| `parsed/_derived/graph/igcse-chemistry/concept_edges.yaml` | 275 edge rows verbatim (270 HUMAN_VALIDATED / 2 REVIEW_REQUIRED / 3 SUGGESTED) + §5 header | `57731243cfba2c1b` |
| `parsed/_derived/graph/igcse-chemistry/explorer_blob.json` | schema `explorer-blob/1.0`, `graph_contract: 1.0`, header with 6 source pins, counts block, full content (topics 4, subtopics 28, specification_points 182, relationships 210, assessment_objectives 3, papers 2, concepts 113, concept_edges 275) | `fb4fadef72451784` |

**Blob source pins — cross-validated against the sweep's S4 pins (6/6 identical):**
`specification_points 956d276f6e4354fa` · `topics 81a4745760bcce2c` · `assessment_objectives 3dc670176f2f5529` · `relationships 6bd3f8236ac2120a` · `concepts 5904c7bc956d6858` · `concept_edges ca73f7077ba82cc0`

**Content mapping** (spec §4.2, preserved in `EB.CONTENT_MAP` as the single mapping source): `topics.yaml → topics/subtopics`; `specification_points.yaml → specification_points`; `relationships.yaml:edges → relationships`; `assessment_objectives.yaml → assessment_objectives/papers`; `concepts.yaml:nodes → concepts`; `concept_edges.yaml:edges → concept_edges`. Rows are verbatim — the projection adds no content (P1/P6). Command words, practicals, chunk-maps and command-kinds are intentionally not blob content: they are not v77 `GRAPH_CONTRACT` data (command words are a presentation-layer concern of the HTML build; chunk-maps/kinds are K2 analytic substrates; practicals are a possible v78+ node-family extension — noted, not assumed).

## 3. S8 — the drift gate, operational (C28 §5)

Wired as 8 permanent battery gates; the battery re-emits to a **temp dir only** (the repo is never written by a sweep):

1. **inventory (P3)** — projection artifacts exist exactly for K2-commissioned quals (today: `igcse-chemistry` only), 0 stray.
2. **G1 freshness, concepts projection** — recorded `source_sha256_16` == live source hash; header schema + `projection_of` resolve through the registry.
3. **G1 freshness, concept_edges projection** — same.
4. **G1 freshness, explorer_blob (6 sources)** — every pinned source path exists and hashes to its pin.
5. **blob header** — `explorer-blob/1.0` + `graph_contract 1.0` + qual match + emitter id.
6. **G2 re-emit idempotency** — re-emission reproduces all 3 artifacts structurally, `emitted_at` being the sole volatile field (documented normalization per §5). A hand-edited projection fails here.
7. **serving-artifact damage scan** — C27 damage classes, 0 hits.
8. **blob counts == ratified stores** — every content count and the validation-status distribution recomputed from the live stores via `EB.CONTENT_MAP`.

Anti-F2 basis: any edit to a ratified store without re-emission fails G1; any hand-edit to a serving artifact fails G2. Drift is now mechanically impossible to miss.

## 4. Scope guards respected

- Ratified plane: **0 store bytes changed** this stage — serving plane only (P2). No verdict gates consumed (none required for emitter-owned surfaces).
- Records, ledgers: untouched (P5). **Errata: none this stage** — no legacy-path edits were needed.
- `parsed/**` canonical JSON untouched; syllabai-core untouched (its refresh rides the core-sync contract, registry `core_sync_target`); explorer v77 untouched (its embedded data is unaffected until the v78 build).

## 5. Effect on subject-#2 commissioning (K-playbook state)

- **K0** — checklist unchanged; K0(ii) is the binding constraint (D4, gate RED). K0(i) parsed bundles stand ready (T-SPEC-NORM-1); K0(iv) scope estimate available on demand via the batch-forecast model.
- **K1** — now literally: add the qual's block to `scripts/graph_paths.yaml` (registry entry) + emit `graph/<qual>/` stores via the c23-pattern emitter. No tooling edits expected (registry-resolved).
- **K3** — serving/emission path already built and S8-gated by this stage: a new commissioned qual gets its projections + blob by running the emitter once the registry entry exists (emitter enumerates `commissioned_quals()` from ratified-store presence).
- **K4** — the battery already generalizes: S8 inventory, G1/G2 and counts gates loop over commissioned quals without code change.

## 6. Follow-ups (non-blocking)

1. **Explorer v78 build** (FileUpload lane): embed `explorer_blob.json` per D3=(a); release record pins HTML sha256 + embedded blob sha256s (spec §4.4; v77 precedent `b975298`).
2. **`DIFF_VS_RATIFIED.json` regeneration** with post-C25 framing (standing equality check, not a convergence tool) — spec §3.3 hygiene, deferred to keep this stage's diff reviewable.
3. **22 non-commissioned quals**: no projections/blobs until their own K3 (P3) — the S8 inventory gate enforces this polarity.
4. **snap-002 re-freeze / 4CH1-4.15 WORKLIST / PAT rotation**: unchanged, operator-held.
