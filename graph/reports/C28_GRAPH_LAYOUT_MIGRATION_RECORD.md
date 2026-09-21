# C28 — Graph Layout Migration Record (D1 option a)

| | |
|---|---|
| **Task** | T-C28 stage execution — single-window `graph/` layout migration per `C28_MULTI_SUBJECT_EXPANSION_SPEC.md` §7 |
| **Directive** | Operator one-letter ruling **"a"** (2026-09-21): fire the 3-stage migration now, push per stage (per-directive push convention). D1 option (a) supersedes the spec's (b)-batch recommendation; D2–D5 remain open |
| **Baseline** | `175ffc1` (C27 final sweep 85 PASS / 0 FAIL, ALL_STORES_CLEAN; local == origin/main) |
| **Stages** | `639e38b` stage-1 (registry-first no-op refactor) → `75639a3` stage-1b (S4 tooling pins + pycache hygiene) → `b3bca02` stage-2 (move + registry flip + 185-ref canonicalization) → `869bcf6` stage-2b (S2 ledger join fix) → this commit (record + spec landing) |
| **Battery** | **87 PASS / 0 FAIL / 0 WARN / 7 INFO — ALL_STORES_CLEAN @ `869bcf6`** (85 C27 gates + 2 new C28 S0 gates: no-hardcode, registry consistency) |
| **Spec landed** | `graph/reports/C28_MULTI_SUBJECT_EXPANSION_SPEC.md` (v1.1, byte-identical to the draft; D2–D5 sections remain proposal-status until ruled) |

## 1. Path map (old → new)

All ten ratified stores moved `graph/<store>.yaml` → `graph/igcse-chemistry/<store>.yaml` via `git mv` (byte-preserving). `graph/reports/` stays SHARED at `graph/reports/` (never per-qual). Target layout per spec §3.1: `graph/<qual>/` appears only when that qual's ratified program is commissioned (K1); `parsed/**`, `graph/reports/**`, syllabai-core, node states, 2012-Jan escalations, data bridge — untouched.

## 2. Per-store sha256 (pre → post; 40-hex)

| Store | Pre (at `175ffc1`) | Post (at `869bcf6`) | Disposition |
|---|---|---|---|
| specification_points | `956d276f6e4354fa7f5319ca320744f86fbb6ce086efb4a798b3a83f15aaaeb3` | same | **PIN-CARRY** (byte-identical) |
| topics | `81a4745760bcce2ccc198ba3843a4ccd25d09c84b3faa7e93248c8b467ccf13d` | same | **PIN-CARRY** |
| practicals | `8e0ab9c4719376886b59f74dbf6222b56332cf87c7bba93d64b14c65e54d5285` | same | **PIN-CARRY** |
| assessment_objectives | `3dc670176f2f55290ac95990f35f82b5888ffa568349f96c32cb9e30e6f352e7` | same | **PIN-CARRY** |
| command_words | `824c50ee0625672c7207827bfeef57899b4ed84a64ecde311dd825f930d9c537` | same | **PIN-CARRY** |
| relationships | `6bd3f8236ac2120a81b1db0a6097583e9e7d484fbd93cef8d772c2f6fd62ba94` | same | **PIN-CARRY** |
| spec_command_kinds | `1464540b1df29a3c00088be629d18a67344c594d2e9ee6d757009e2de48639aa` | same | **PIN-CARRY** |
| concepts | `634a743b65d1612bb6c078668d709ca31835fbced1ef916e271403db9034c27f` | `5904c7bc956d68586f6f606f7a9fd86868cd381a7a445b032bab2e79e0290634` | **RE-ISSUED** (92 path refs canonicalized) |
| concept_edges | `ccc674cf3a94b8e47d3df68ef011ac4c345ed3962d445d488369edf77182d737` | `ca73f7077ba82cc055a3f272a68198a0adb0a23a13dd31154c1c48e2e41eaafb` | **RE-ISSUED** (92 path refs canonicalized) |
| spec_chunk_mappings | `f36910450bd50726655a1e9fc1e01a28fdd838769236da28c4f1d316c451ce77` | `e8b58a7109104bb70bd37ef8244f3e5b86b61e8cd175ddf37f8c356ec39be567` | **RE-ISSUED** (1 meta-note ref canonicalized) |

Byte-identity for the move itself was verified for **10/10 stores** immediately after `git mv` (all ten sha256-identical pre-move → post-move); only then was the recorded canonicalization repair applied to the 3 anchor-carrying stores. Every changed line was pattern-verified to be exactly a `file: graph/specification_points.yaml` SPEC-evidence anchor (92 + 92) or the `sp_title_wording_source:` meta note (1) — 185 refs on 185 lines, zero other deltas.

## 3. Registry (the mechanism that ends hard-coding)

- `scripts/graph_paths.yaml` — schema `graph-path-registry/1.0`: per-qual store templates (`graph/{QUAL}/<store>.yaml`), `reports_dir`, `core_sync_target`, `layout.qual_prefix` stage resolution, `legacy_map` (10 entries, filled at stage-2), `legacy_allowlist` (6 immutable ledgers).
- `scripts/graph_paths.py` — the one resolver: `store/store_rel/qual_dir/reports_dir/legacy_rel/resolve_rel`. `resolve_rel` maps every historical root-form path to its canonical location; all checkers re-verifying landed pins go through it.
- `scripts/check_no_hardcode.py` — the §3.2 mechanical check (legacy-form `graph/<store>.yaml` extinct from `scripts/` outside the allowlist) + registry consistency gate (store paths resolve on disk; `legacy_map` must equal the derived mapping). Wired as two permanent **S0 gates** in `c27_final_all_store_sweep.py`.

## 4. Tooling refactor (stage-1)

- **51 code-semantic edits across 18 files**: store I/O via `GP.store()/GP.qual_dir()`; git-path I/O (`git show HEAD:<path>`) via `GP.store_rel()`; data-value comparisons/writes against store `file:` anchor fields via `GP.store_rel()` (they follow the canonicalized data); download-mirror readers (`sme_spcpt_verify/resolve`, `chemistry_rediff`) use canonical mirror literals (no GP — different root). Reports-dir joins split from qual-dir constants (`c26_postcheck` ledger, `c26_emit` REPORTS).
- **62 legacy-form literals swapped to canonical form across 27 files** (docstrings, messages, diff labels, rendered-report text) — accurate post-migration text; the §3.2 pattern is pattern-immune to the canonical nested form.
- Sweep S4 tooling pins refreshed for the 3 refactored pinned scripts: c26_emit `c4ad56a1…→e9cbf844…`, c26_postcheck `b309c07b…→e506e0c9…`, c23 `135452dd…→886df716…` (pre-hashes in code comments).
- **Stage-2b lesson (recorded for the pattern library):** `os.path.join(GRAPH, "reports/...")` join-through-GRAPH forms are invisible to both the store-path pattern and bare-dir scans — one instance (S2 C26-ledger read) surfaced only when the sweep ran on the moved layout. Fixed via `GP.reports_dir()`; a full `GRAPH`-usage audit found no others.

## 5. No-hardcode check results

Pre-refactor: 34 tooling files carried 113 legacy-form refs (94 at `scripts/*.py` root + 19 in subdirectory files, occurrence-counted). Post-refactor: **0 outside the allowlist**. Allowlisted (immutable, P5 errata-bridged, byte-untouched): `c11_batch1/2/3/4_decisions.yaml` (24/18/29/24), `c11_pilot_decisions.yaml` (16), `c12_decisions/smoke-demo.agent-pass-1.yaml` (5) — 116 historical refs resolving via `resolve_rel`.

## 6. Errata — legacy path bridge (P5)

**Every historical pinned path below remains valid as a label; checkers resolve it to the canonical location via `scripts/graph_paths.yaml:legacy_map` / `graph_paths.resolve_rel()`. Landed records and verdict ledgers were NOT edited.**

| Legacy (historical, in C25/C26/C27 records & ledgers) | Canonical (live) |
|---|---|
| `graph/specification_points.yaml` | `graph/igcse-chemistry/specification_points.yaml` |
| `graph/topics.yaml` | `graph/igcse-chemistry/topics.yaml` |
| `graph/practicals.yaml` | `graph/igcse-chemistry/practicals.yaml` |
| `graph/assessment_objectives.yaml` | `graph/igcse-chemistry/assessment_objectives.yaml` |
| `graph/command_words.yaml` | `graph/igcse-chemistry/command_words.yaml` |
| `graph/relationships.yaml` | `graph/igcse-chemistry/relationships.yaml` |
| `graph/concepts.yaml` | `graph/igcse-chemistry/concepts.yaml` |
| `graph/concept_edges.yaml` | `graph/igcse-chemistry/concept_edges.yaml` |
| `graph/spec_chunk_mappings.yaml` | `graph/igcse-chemistry/spec_chunk_mappings.yaml` |
| `graph/spec_command_kinds.yaml` | `graph/igcse-chemistry/spec_command_kinds.yaml` |

Byte-untouched inventory: `graph/reports/**` (all prior records incl. C25/C26/C27), the 6 allowlisted ledgers, `parsed/**`, syllabai-core (`core_sync_target` registry-mapped; core-side layout is a separate core-lane decision), node states, 2012-Jan escalations, data bridge. Explorer v77 unaffected (self-contained build artifact; the next v78 build consumes registry paths per spec §4).

## 7. Findings during execution

1. **c13 negative-test in-repo mode — pre-existing, repaired + guarded.** `load_registry(repo_root)` read `<repo>/specification_points.yaml`, which never existed (pre-C28 regression; the mode crashed before its positive control). Stage-1 routes it via the registry. The positive control then exposed a second environmental fact: **the untracked SME notes corpus (`Chemistry IGCSE Revision Notes/`) is absent from this workspace** (untracked, wiped by workspace resets), so in-repo mode cannot run here; a corpus-presence guard now raises an actionable message, and sandbox mode remains the supported path. Flagged for the corpus owner alongside the snap-002/T-C06 notes-surface open item.
2. **Join-through-GRAPH blind spot** (§4 above) — closed; the S0 registry-consistency gate now guards store-path resolvability on every sweep.
3. Sweep battery grew 85 → 87 gates (two permanent C28 S0 gates); all green.

## 8. Interaction with open items

- **T-C11 batch 5 (S2 Inorganic):** unaffected; independent of layout (D5). Its outputs will land at `graph/igcse-chemistry/` going forward; cross-slice rulings S1↔S2 + S3↔S2 remain its own gate.
- **snap-002 re-freeze:** unaffected — `concept_attachments` joins on spec codes, not store paths; this record supplies the path remap for the bench record when the operator takes the freeze.
- **4CH1-4.15 WORKLIST row:** moved with its store; disposition WORKLIST, owner-held, quote gap unchanged.
- **D2–D5:** still open (serving plane, explorer mode, subject #2, batch-5 sequencing). The migration makes subject-#2 K1 a pure registry entry (`quals.<qual>`) plus new `graph/<qual>/` stores.
