# C28 — Multi-Subject Expansion & Graph Layout Spec

| | |
|---|---|
| **Task ID** | T-C28 |
| **Version** | 1.1 — **PROPOSAL**. Nothing in this document executes without an explicit operator directive. *v1.1 (D1 prep finding): stage-2 also canonicalizes 185 internal store refs via a recorded repair; registry legacy-path resolver added.* |
| **Date** | 2026-09-21 |
| **Baseline** | syllabai-resources `origin/main` @ `175ffc1` (local == remote, tree clean; C27 final sweep 85 PASS / 0 FAIL, ALL_STORES_CLEAN) |
| **Enabling landing** | T-SPEC-NORM-1 (`7ca311a`): all 23 parsed bundles normalized to one 13-field point schema (4,278 points), PDF fidelity sha1 23/23, KG-loader contract 23/23 |
| **Predecessor patterns** | `C26_SIBLING_STORE_PDF_REFRESH_SPEC` (phase-gated proposal), `C25`/`C27` records (verification battery), T-C10/C11/C13/C19 (ratified-work sequence) |
| **Scope** | Target repository layout for ratified graph stores as subjects are added; the serving/projection plane that feeds the KG explorer; drift protection for every derived copy; the per-subject commissioning playbook; the single migration window for the existing igcse-chemistry store. |

---

## 0. Operator decision points (read first)

This spec is executable only after the operator rules on five points. Recommendations are stated; each is reversible before execution.

| # | Decision | Options | Recommendation |
|---|----------|---------|----------------|
| **D1** | Migration timing for `graph/` → `graph/igcse-chemistry/` | (a) now, (b) batched into subject-#2 commissioning | **(b)** — churn rides on work that must touch tooling anyway; until then every pin stays valid |
| **D2** | Serving-plane location for explorer feeds | (a) extend `parsed/_derived/graph/<qual>/`, (b) new `graph/_views/<qual>/` | **(a)** — it already exists, is 23/23 contract-pass, and is the established KG-loader surface |
| **D3** | Explorer data mode for multi-subject | (a) per-qual self-contained HTML (v77 pattern), (b) single multi-qual HTML with qual switcher, (c) runtime fetch | **(a) near-term**, with the blob schema designed so (b) is a later build change, not a data change |
| **D4** | Subject #2 | ial-chemistry / igcse-physics / igcse-biology / other | Gated by **notes corpus availability**, not parsed data (see §6-K0). Operator to confirm which corpus exists |
| **D5** | T-C11 batch 5 sequencing vs layout migration | (a) batch 5 first on current layout, (b) migrate first | **(a)** — batch 5 is operator-gated and independent; the migration window carries its outputs (paths re-pointed, pins errata'd) |

---

## 1. Verified current state (inputs to this spec)

All facts below were re-verified against `origin/main` @ `175ffc1` immediately before this draft.

**Ratified plane — `graph/` (single subject: igcse-chemistry).** Ten stores: `specification_points.yaml` (182 points, PDF-direct lineage, `statement_text_policy` verbatim-from-PDF), `topics.yaml` (4 + 28 subtopics), `practicals.yaml` (12), `assessment_objectives.yaml` (3 AOs, papers 2, ratified overlay), `command_words.yaml` (25), `relationships.yaml` (210 edges, per-edge provenance), `concepts.yaml` (113 nodes, SPEC evidence quotes re-anchored to definitive wording), `concept_edges.yaml` (275 edges, 153 HUMAN_VALIDATED), `spec_chunk_mappings.yaml` (211 rows / 210 mapped quotes), `spec_command_kinds.yaml` (82 verbs). Plus `graph/reports/` — the complete audit chain (~90 files: T-SPEC verdict rounds, C10–C13, C19, C23–C27 records, review sheets, verdict ledgers).

**Source plane — `Official-Specifications/parsed/` (23 quals, uniform).** Post T-SPEC-NORM-1: one 13-field point schema across 4,278 points; `parse_report.json` 23/23 ALL_PASS; per-PDF sha1 23/23; token fidelity ≥95.9% (100% on 14 quals). Per-qual bundles: `spec_points/topics/practicals/assessment_objectives/command_words/equations` JSON + raw parse.

**Existing per-qual projection surface.** `parsed/_derived/graph/<qual>/` — 23 quals × 4 files (`topics/relationships/practicals/specification_points` YAML), KG-loader contract verified 23/23 (C27 gate S5; 4,274 point rows). igcse-chemistry additionally carries `DIFF_VS_RATIFIED.json` (182/182 wording-identical, 0 diffs — its framing note predates the C25 swap and is historical).

**Consumer — syllabai-core.** `src/main/resources/concept-graph/` mirrors the ratified stores; `ConceptGraphSeedService` / `ConceptDependencyGraphLoader` consume them. The resources repo is the upstream source of truth for that copy.

**Explorer — v77 KG HTML.** Tracked on the FileUpload origin (`b975298`), mirrored to `download/`. **Self-contained: zero runtime fetches** — the entire graph (nodes incl. `SpecificationPoint`, edges, labels, codes) is embedded inline as minified consts (`GRAPH_CONTRACT={version:'1.0', nodeTypes:[Subject,Section,SubTopic,SpecificationPoint,ExamPaper], edgeTypes:[hier,pre,rel,assess], learnerOverlay:{...}}`). It is a **build artifact**, regenerated from store data — it never reads `graph/` at runtime.

**Hard-coding exposure.** ≥550 hardcoded `graph/` path occurrences across 60+ scripts/verdict/ledger files (incl. ratified ledgers `c11_promotions.yaml` ×155, `c19_promotions.yaml` ×118). Records are immutable — path references inside them can only be re-pointed via an errata layer, never edited in place.

**Open items unaffected by this spec:** T-C11 batch 5 (S2 Inorganic; needs its own S1↔S2 + S3↔S2 cross-slice rulings), snap-002 re-freeze (operator credential boundary), chunk-map `4CH1-4.15` WORKLIST row (owner-held), PAT rotation (advised).

---

## 2. Design principles (non-negotiable)

- **P1 — Single source of truth per qual.** A ratified store exists exactly once. Redundancy is provided by *regenerable projections*, never by hand-maintained copies. (Empirical basis: C27 Finding F2 — a copy surface drifted 84/211 rows from its source within one cycle.)
- **P2 — Two planes.** The **ratified plane** (`graph/`) holds verdict-gated work product and is written only through operator gates. The **serving plane** (projections, explorer blobs) is emitter-owned, regenerable, and never authoritative.
- **P3 — Folders follow commissioning.** A `graph/<qual>/` directory appears when that qual's ratified program is commissioned — not when its PDF is parsed. Parsed data for 23 quals ≠ ratified work for 23 quals.
- **P4 — Provenance trust boundary.** `parsed/` = "what the official PDF says" (zero-LLM, RULE_DERIVED, regenerable). `graph/` = "what was built and ratified on top" (HUMAN_VALIDATED, operator verdicts). The two stay in separate trees so cross-verification (C25/C26/C27 methodology) remains an independent check.
- **P5 — Records immutable.** Landing records and verdict ledgers are never edited; corrections and path re-pointings ride an errata section in the newer record.
- **P6 — Every derived copy is emitter-owned and drift-checked** (§5). Hand-edits to any projection fail the gate.

---

## 3. Target layout convention

### 3.1 Ratified plane

```
graph/
  igcse-chemistry/                  ← post-migration home of the current 10 stores (§7)
    specification_points.yaml ... spec_command_kinds.yaml
  <qual>/                           ← created only at that qual's K1 landing (§6)
    specification_points.yaml ... (same 10-store shape, as the program earns them)
  reports/                          ← SHARED, single audit trail (cross-qual records incl.)
```

- **Qual-id vocabulary** = the `parsed/` bundle names (`igcse-chemistry`, `ial-chemistry`, `igcse-physics`, …). One vocabulary, both planes.
- `graph/reports/` stays shared: record filenames already carry task/qual context, and fragmenting the audit trail per-qual would make cross-qual sweeps and the errata chain harder.
- The 10-store shape is a *target shape*, not a boilerplate: a qual's store set grows as its program earns each store (K1 emits the 5 spec-text stores; K2 adds concepts/edges/chunk-maps/kinds).

### 3.2 Path registry (the mechanism that ends hard-coding)

New file `scripts/graph_paths.yaml`:

```yaml
schema: graph-path-registry/1.0
quals:
  igcse-chemistry:
    stores:
      specification_points: graph/igcse-chemistry/specification_points.yaml
      # ... all 10
    reports_dir: graph/reports/
    core_sync_target: syllabai-core/src/main/resources/concept-graph/
```

Every tool that touches store paths — emitters, `graph_check.py`, the sweep harness, CI wiring, the core-sync step, the KG build — reads the registry. The ≥550 hardcoded references become a **one-time refactor** (mechanical, machine-verifiable: after refactor, `grep -r 'graph/[a-z_]*\.yaml' scripts/` should only hit the registry and the migration errata), not a recurring tax.

### 3.3 Serving plane

```
parsed/_derived/graph/
  <qual>/                                  ← exists today ×23 (4 files)
      topics.yaml relationships.yaml practicals.yaml specification_points.yaml
      concepts.yaml concept_edges.yaml     ← NEW: emitted only for quals with ratified work
      explorer_blob.json                   ← NEW: per-qual explorer feed (§4)
```

- Projections of ratified stores are **emitted from** them (same emitters, registry paths), carrying the §5 provenance header. They add no content of their own.
- `DIFF_VS_RATIFIED.json` is regenerated with post-C25 framing (ratified store is PDF-direct; the diff is now a standing equality check, not a convergence tool).

### 3.4 What does NOT move

- `Official-Specifications/parsed/**` canonical JSON — untouched (source plane).
- `graph/reports/**` records — untouched (P5); only the errata section of *new* records may map old paths to new.
- `parsed/_derived/**` existing 92 files — regenerated by tooling only, never relocated by hand.
- syllabai-core node states, 2012-Jan escalations, data bridge — untouched (standing scope guards).

---

## 4. Explorer projection contract

**Current fact (v77):** data is baked at build time; the HTML is self-contained; one qual per artifact.

**Contract (applies from the next explorer build, v78+):**

1. **Feed = `explorer_blob.json` per qual**, emitted by the projection emitter. Header is mandatory:

```json
{
  "schema_version": "explorer-blob/1.0",
  "qual": "igcse-chemistry",
  "graph_contract": "1.0",
  "sources": [
    {"path": "graph/igcse-chemistry/specification_points.yaml", "sha256_16": "…"},
    {"path": "graph/igcse-chemistry/concepts.yaml", "sha256_16": "…"}
  ],
  "emitted_at": "…", "emitter": "scripts/c28_emit_explorer_blob.py@1.0.0"
}
```

2. **Content mapping** (v77 `GRAPH_CONTRACT` v1.0 preserved): `Subject/Section/SubTopic` from `topics.yaml`; `SpecificationPoint` from `specification_points.yaml` (13-field schema, definitive wording); `hier/pre/rel` from `relationships.yaml` + `concept_edges.yaml`; `assess` from AOs/papers overlay; concepts/misconceptions included when the qual has ratified K2 work. Learner overlay fields remain placeholder-null at the resources layer (serving-side enrichment is a core-lane concern).
3. **Build modes** (D3): the blob is identical under all three modes — (a) per-qual HTML embeds its blob; (b) a multi-qual HTML embeds the set and adds a switcher; (c) runtime fetch serves the same blobs. Changing mode is a build change only; the data contract does not move.
4. **Release discipline:** each explorer build records the blob sha256s it embedded; the C-record pins HTML sha256 + source blob pins (the v77 precedent: `b975298` + mirror).

---

## 5. Drift-check gate (the anti-F2 mechanism)

**Rule:** every derived copy — `_derived/graph/**` projections, `explorer_blob.json`, any future `_views/` copy — carries `{source path, source sha256_16, emitted_at, emitter version}` and is verified two ways at every sweep:

- **G1 — source freshness:** recorded `sha256_16` == live source file hash. A source that changed without re-emission ⇒ FAIL.
- **G2 — re-emit idempotency:** re-running the emitter reproduces the artifact byte-for-byte (or semantics-for-semantics with a documented normalization). A hand-edited projection ⇒ FAIL.

This becomes sweep gate **S8** in the C27 battery shape (S0–S7 unchanged). C27's F2 (84/211 stale labels, 4 with retired-lineage damage) is the standing justification: drift is not hypothetical, it already happened once.

---

## 6. Per-subject commissioning playbook

Each new subject = one gated program. Nothing mass-generates; every promotion is operator-gated (the chemistry sequence, replayed per qual).

| Phase | Content | Gate |
|---|---|---|
| **K0 — Prerequisites & authorization** | (i) parsed bundle exists, `parse_report` ALL_PASS; (ii) **notes corpus secured for the qual** — the binding constraint: chemistry's ratified layers stand on the SME 4CH1 notes corpus, and no equivalent corpus ⇒ no K2; (iii) operator commissioning directive; (iv) scope estimate via the batch-forecast model (pilot ratios 2.4 nodes/SP, 2.75 edges/SP; observed discipline-adjusted actuals ~1.0/~1.6) | Operator directive names the qual |
| **K1 — Spec store build** | c23-pattern emitter: canonical JSON → `graph/<qual>/specification_points.yaml` + 4 sibling stores, explicit meta/lineage (no `dict(old_meta)` inheritance — the C26 root-cause rule), registry-registered paths | Canonical equality 1:1; damage-class scan 0; counts == parse_report; `graph_check` extended to the new paths; single commit + record |
| **K2 — Ratified enrichment** (chemistry sequence per qual) | T-C10-pattern note-level mapping (human-validated) → T-C13-pattern chunk substrate (review-sheet gate, ≥90% class precision) → T-C11-pattern concept pilot + §16-style batches (authoring → diff-review bundle → **operator verdicts** → §18 promotion) → T-C19-pattern concept→SP substrate | Every batch: operator verdict gate; zero silent promotion; held quarantine preserved |
| **K3 — Serving & explorer** | Projection emitter run for the qual (incl. concepts/edges if K2 produced them); `explorer_blob.json` emitted + S8-gated; explorer build per D3; release vX with pins | S8 G1+G2 PASS; HTML + blob pins recorded |
| **K4 — Acceptance** | Extended sweep: S1 now covers N quals × store sets; S5/S8 grow accordingly; all pins green | Full battery ALL_GREEN before the qual is declared served |

**Subject-#2 candidates (parsed side ready, D4):** `ial-chemistry` (319 SPs, 3 practicals), `igcse-physics` (171 SPs), `igcse-biology`, `igcse-maths-a`, … — selection is operator's; K0(ii) is the real gate for each.

---

## 7. Migration plan — single window (D1)

**Trigger:** operator directive, or subject-#2 K1 completion, whichever the operator chooses.

**Key safety property:** the migration is a *path* migration — `git mv` preserves file bytes. For the **7 stores without internal path refs**, every existing sha256 pin remains valid. The remaining **3 stores carry 185 internal refs** to `graph/specification_points.yaml` (92 SPEC evidence `file:` anchors in `concepts.yaml`, 92 in `concept_edges.yaml`, 1 meta note in `spec_chunk_mappings.yaml`) — canonicalized inside stage-2 by a recorded repair commit (per-store pre/post sha256 in the migration record). Immutable ledgers and landed records are never edited; a single registry resolver maps legacy paths when checkers re-verify them.

1. **Registry-first:** land `scripts/graph_paths.yaml` + tooling refactor (emitters, `graph_check`, sweep, CI, core-sync contract, KG build) while paths still point at current locations — a verified no-op commit.
2. **Move:** `git mv graph/*.yaml graph/igcse-chemistry/` (10 stores; reports stay).
3. **Re-point:** tooling reads the registry; the mechanical no-hardcoding check (§3.2) goes green.
4. **Record:** `C28_GRAPH_LAYOUT_MIGRATION_RECORD.md/.json` — old→new path map, per-file sha256 pre/post (identical), tooling touch list, registry content.
5. **Errata:** the record's errata section maps every legacy pinned path (`graph/specification_points.yaml` → `graph/igcse-chemistry/specification_points.yaml`, etc.). C25/C26/C27 records stay byte-untouched (P5).
6. **Post-migration sweep:** full battery ALL_GREEN on the new layout **before** any new-qual K1 lands.

**Explicitly out of scope for the migration:** syllabai-core's copy is re-synced via its existing contract (registry `core_sync_target`); the explorer rebuild rides the next v78 build (its embedded data is unaffected until then).

---

## 8. Rejected alternatives (with reasons)

| Alternative | Why rejected |
|---|---|
| Merge `graph/` into `Official-Specifications/parsed/` | Mixes ratified work product + audit trail into the source plane; destroys the P4 trust boundary that makes C25/C26/C27-style cross-verification meaningful; half of `graph/` (concepts, chunk-maps, records) has no per-PDF meaning |
| Hand-duplicate `graph/` as a second igcse-chemistry truth | F2 precedent: duplicates drift (84/211 in one cycle); two sources of truth makes every future sweep ambiguous |
| Migrate layout now | ≥550 hardcoded refs churned across 60+ files + immutable-record errata, with no second subject commissioned — pure cost today; batched at K1 it rides work that must touch tooling anyway |
| Mixed convention (igcse-chemistry at root, new quals in `graph/<qual>/`) | Permanent special-casing in every checker/loader/glob, forever; worse than one clean migration |
| Explorer reads ratified stores at runtime | Couples serving to the ratified plane, breaks the self-contained artifact property, and turns every store edit into a live-explorer change with no build gate |

---

## 9. Scope guards (standing)

Node states byte-untouched; 2012-Jan escalations and the data bridge not approached; C25/C26/C27 records unedited (errata-only); `parsed/**` canonical JSON untouched; all ratified-plane writes flow through operator verdict gates; no core serving behavior changes from this repo (core sync is a documented contract, owned core-side).

---

## 10. Execution deliverables (when directive given)

1. `scripts/graph_paths.yaml` (registry) + no-op tooling refactor commit.
2. On D1 trigger: migration commit series + `C28_GRAPH_LAYOUT_MIGRATION_RECORD.md/.json` + errata (§7).
3. `scripts/c28_emit_explorer_blob.py` + `_derived/graph/<qual>/concepts|concept_edges` emitter extension + S8 gate added to the sweep harness (§4, §5).
4. This spec lands at `graph/reports/C28_MULTI_SUBJECT_EXPANSION_SPEC.md` in the same series; worklog updated; download/ mirrors restocked.
5. Per-subject: K0–K4 records as the operator commissions each qual (separate task IDs, e.g. T-C29+ per qual).

## 11. Interaction with open items

- **T-C11 batch 5 (S2 Inorganic):** independent of layout (D5). If it lands before migration, its outputs live at current paths and are carried by §7; cross-slice rulings S1↔S2 + S3↔S2 remain its own gate.
- **snap-002 re-freeze:** unaffected — `concept_attachments` joins on spec codes, not store paths; the migration record notes the path remap for the bench record when the operator takes the freeze.
- **4CH1-4.15 WORKLIST row:** unaffected; owner-held decision unchanged.

## 12. Landing plan for this spec

Draft lives at `download/C28_MULTI_SUBJECT_EXPANSION_SPEC.md`. On operator directive it lands to `graph/reports/` via the standard single-commit + record protocol (as the C26 spec did). Until then, no repository bytes change.
