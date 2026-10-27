# SIB Lessons Register — operational laws of record (ALL courses)

**Status:** OPERATIONAL (2026-10-27, edition r1 — established by RUN-015's Stage C per
the operator directive *"update the docs of the SubjectIntelligence folder, so that in
the future when we add sib docs for other subjects, we wont face all these problems.
Basically a self improving pipeline"*).
**Source of record:** the CHEMISTRY_4CH1 run history RUN-001..RUN-015 (95 artifacts,
15 runs). Every law below was paid for by a real failure or a real repair; the
register exists so the NEXT course library inherits them at onboarding instead of
re-deriving them under gate pressure.
**Consumption contract:** read this file BEFORE the first generation run of a new
library, and again before any repair pass on an existing one. `COURSE_ONBOARDING.md`
§7 wires it into the onboarding checklist; `PIPELINE.md` §8 wires it into the per-run
procedure. New lessons are appended at the bottom with the run id that earned them.

## 1. Session preflight (before any work)

1. **Assume the sandbox was recycled.** Every session starts by verifying: creds
   (GitHub + any DB; restore from the operator snapshot if `~/.secrets` is gone),
   clone surfaces, sparse-checkout coverage, and validator pin. RUN-014 and RUN-015
   each began after a `/tmp` recycle that silently removed prior-run receipts and
   scripts. Persist every script under a `scripts/` path that survives the session
   and re-derive perishable outputs from scripts, not from memory.
2. **Sparse-checkout illusions are the default failure mode.** Paths can exist in
   `HEAD` yet be absent from the worktree (sparse rules), and `git status` will not
   tell you. Diagnosis order: `git ls-tree HEAD <path>` (tree-layer truth) → then
   fix the sparse set (`git sparse-checkout add <path>` + `reapply`). The `docs/`
   directory, the legacy corpus cones, and the graph plane have each been "missing"
   this way. A stale `index.lock` from an interrupted reapply is removed, not
   feared.
3. **Fetch-first is a gate, not a habit.** Before branch cut: fetch, compare
   `origin/main` to the pin of record. If origin advanced, prove advance isolation
   (is the diff on this lane's paths empty?), FF the local main, cut the branch from
   the advanced tip, and file an `advance_disclosure.json` in the run record.
   RUN-013/014/015 each caught a mid-flight advance; isolation was provable in every
   case. Fail closed if the advance touches your lane.
4. **Trace accounting.** The operator instruction's trace id (and any continuation
   trace ids) go into the run's worklog entries — both the library's own WORKLOG and
   the session worklog. The worklog is append-only; each agent appends its own
   section with Task ID, work log, and stage summary.

## 2. Identifier and locator grammar (write it right the first time)

1. **Artifact id law:** the artifact id is `stem.split("_")[2]` of the filename —
   `CHEMISTRY_4CH1_CUR-03_CONCEPT_TAXONOMY.md` → `CUR-03`. QA receipts are named
   `<ARTIFACT-ID>.qa.json`. Never parse the id from front matter alone; the filename
   is the law.
2. **Citation grammar (r4 binding, enforced by `pipeline/sib_evidence_claim_qa.py`):**
   - every citation is `(SRC-<ID>, <path-suffix> <page-spec>)` — the path-suffix
     must suffix-match a file IN THE ARTIFACT'S OWN PACK (case-insensitive; bare
     basenames work only when unique in the pack — cite enough path to be
     unambiguous, e.g. `<session>/<paper>/er.pdf` when several packs carry
     `er.pdf` files);
   - page specs are `pN` / `ppN-M` (`page N` does NOT parse); markdown ranges are
     `lines N-M` and expand to a closed range — EVERY line must be covered by the
     cited file's excerpts;
   - one citation per paren. Semicolon-joined multi-citations inside one paren
     fail-closed at the parser; split them: `(SRC-A, path lines 1-2); (SRC-B, path2 p3)`;
   - derivation labels are standalone parens OUTSIDE the citation:
     `(SRC-A, path lines 1-2) (RUN-COMPUTED: census.json, dotted.path)` — prose
     inside a citation paren is not machine-verifiable and will be rejected;
   - prose-paren hidden forms — `(some prose; SRC-X, locator)` — are invisible to
     the standard citation regex and therefore to the gate; sweep for them
     explicitly (`\([^()]*?;\s*SRC-`) during any citation pass (RUN-015 found two).
3. **Quote binding (r1 law, same gate):** every quoted span ≥25 chars / ≥4 words in
   a record must appear VERBATIM (normalized) in the union of that record's own
   cited excerpts. Consequences:
   - never quote from memory — quote from the pack excerpt text you have read;
   - preserve the source's own punctuation: injected commas, single-vs-double quote
     nesting, and YAML `''` escaping all break binding (RUN-015 repaired four such);
   - a paraphrase presented in quotes is a violation — de-quote or restore the
     source wording;
   - an ellipsis inside a quote splits the scanner's fragment pairing and can
     manufacture violations from ADJACENT text (the post-ellipsis orphan close
     pairs with the next quote in the record) — prefer quoting through a clean
     endpoint, or split into separately-cited fragments;
   - do not quote a document that is not a pack source (e.g. the pipeline's own
     policy yaml) — de-quote and attribute in prose.
4. **The gate checks more than you think — gate EARLY.** RUN-014 and RUN-015 both
   discovered that first-time gating of an old artifact exposes debt (34 violations
   on CUR-02; 7 quote-binding violations on CUR-05/07/08). Budget for it: run the
   evidence-claim QA on the STAGED body BEFORE stamping/deploying, and keep the
   pre-repair census in the run receipt so pre-existing debt is provably not a
   regression of this run.

## 3. Evidence packs (caps, windows, re-spec)

1. **Caps of record** (`pipeline/evidence_pack.py`): 60 excerpts per source,
   1600 chars per excerpt, 40000 chars per source (accumulated ACROSS a source's
   files in plan order — the break can silently drop trailing files; keep plans
   well under the cap or front-load the files you cite), 40 files per source.
2. **Window math:** a markdown query hit at 0-based line h yields excerpt
   `lines (h-1)..(h+13)` (1-based, stripped, 1600-capped). When a citation must
   resolve at specific lines, compute the hit line FIRST, then write the locator.
   PDF excerpts are `page N` per requested page (pymupdf text, deterministic for
   the same pymupdf version).
3. **Full rebuilds are surface-unstable; surgical appends are the honest minimal
   diff.** `select_sources` is resolution-driven: a pack rebuilt on a different
   sparse surface can SWAP SOURCES (RUN-015: a CUR-06 rebuild replaced the
   disclosed-failed SRC-BOOK-4CH1-SB1 with the newly-resolved SRC-LEGACY-SPEC-4CH0).
   To widen a pack: append windows to the existing pack JSON (each byte-built by
   the builder's own rules from the sha-pinned files, per-file sha256 asserted),
   update `pack_spec.json` so the plan-of-document stays truthful, and prove the
   diff is exactly the added excerpts. A full rebuild is acceptable ONLY after a
   probe proves byte-identity (mod run_id) — RUN-015's HIS rebuild passed that
   probe and used the clean path; CUR packs did not and used appends.
4. **Re-spec is a disclosed precedent, not an improvisation** (RUN-007 precedent):
   widening a pack to make an already-cited locator resolvable is legitimate;
   document it in the run receipt with the diff proof. Adding windows is fine;
   editing excerpt TEXT is not (identity preservation law, `PIPELINE.md` §6).
5. **Carry-over discipline:** packs carried between runs must be byte-identical
   (sha256-asserted) unless disclosed as a re-spec. Chain-check carried packs
   against their origin run's receipts.

## 4. Run mechanics (stamps, receipts, manifests)

1. **Stamp flow:** stage edited bodies under `runs/<RUN>/bodies/`, stamp via
   `pipeline/generate_artifact.py` into `runs/<RUN>/staged/`, deploy to
   `artifacts/`, then assert deployed-body == staged-body and the version bumped.
   `generate_artifact.py` refuses to overwrite — clear `staged/` on any re-run
   (RUN-012 precedent).
2. **Version discipline:** repairs bump the patch version (v1.0 → v1.1) and the
   stage-2 front matter carries the repair run id. Read the CURRENT version from
   the artifact and assert it before editing; on any re-run after a partial
   failure, restore the artifacts from git HEAD first (partial runs leave stamps
   behind).
3. **Receipt refresh is library-wide:** after editing N artifacts, refresh the qa
   receipts of ALL 95 (qa writes `qa-reports/<ID>.qa.json` for unchanged artifacts
   too) and assert the whole library stays at 0 errors / 0 warnings. The unchanged
   count is `95 - N` — compute it, don't guess it (RUN-015 Stage B mis-guessed 82
   for 88).
4. **Run manifest receipts:** `run_manifest.py add-artifact` per artifact with
   pack sha + artifact sha + named gates, then `validate`. Gate strings are the
   human-readable audit trail — write them to state WHAT was done and WHY it is
   trustworthy, including the disclosed exceptions.
5. **Census annex:** write the run's `census.json` (pack composition of record)
   before the evidence-claim QA — the gate loads it. RUN-COMPUTED citations must
   resolve inside it.
6. **Repair scripts are exact-match:** every rewrite is a whitespace-tolerant
   exact-match replace with an occurrence-count assert; every content edit asserts
   the substance multiset (sources/pages/ranges) is unchanged unless the change IS
   the substance, and then it is disclosed per-record. Outside-paren prose is
   asserted byte-equal (moved hedges accounted explicitly).

## 5. Git phase

1. Branch naming `sib/<lane>-pass<N>-r0`; commit with a message that IS the audit
   summary (what, why, gates, trace); PR; sha-pinned merge; FF local main;
   post-merge gates (validate-manifest, receipt validate, full live sweep).
2. The true diff of a repair run is SMALL. Verify it: `git diff <base> --stat` and
   reconcile every changed path against the run's declared scope. Unexpected paths
   mean a stray write.

## 6. Debt discipline (the self-improving part)

1. **Register, don't scope-creep.** A repair run that discovers adjacent debt
   files it in the receipt (`register_note`) and STOPS; the operator orders the
   follow-up run (RUN-014 registered the CUR-03..08/GAP grammar debt; RUN-015
   executed it and retired the GAP half as confirm-clean).
2. **Census before repair.** Enumerate every instance (token-level census,
   mechanical-vs-adjudicated classification), then repair from the table. Ad-hoc
   fixing misses the long tail (RUN-015's census found 131 pathless tokens across
   102 unique forms, including prose tails and chained components a hand-fix would
   have mangled).
3. **Confirm-clean is a deliverable.** Re-gating an untouched artifact that passes
   (RUN-015's GAP-01..08: 120 citations / 0 violations) retires a register item
   and is recorded with the same rigor as a repair.
4. **Append the lesson.** Any failure not covered here gets a numbered entry below
   with the run id, the failure, and the law that prevents it.

## 7. Register of earned lessons (append-only)

| # | Run | Lesson |
|---|-----|--------|
| 1 | RUN-003..014 | Sparse-checkout surfaces mislead preflight; resolution truth = manifest + disclosure, and the 6/17 sparse-surface state is disclosed run-wide, never repaired silently. |
| 2 | RUN-011 | Run-manifest provenance fields have ONE correct front-matter level; parse with an assert (`SRC-` prefix) or the validator fails closed after deploy. |
| 3 | RUN-012 | `generate_artifact.py` no-overwrite law catches stale stamps on re-run; clear `staged/` before re-stamping. |
| 4 | RUN-013 | Anchor registries resolve only under the loader's contract (namespace + extractor); pin the loader view, not the raw file, and prove unambiguity for any projection. |
| 5 | RUN-014 | First-time r4 gating of pre-r4 artifacts exposes grammar debt; gate staged bodies BEFORE deploy and file the debt register note. |
| 6 | RUN-015 | Full pack rebuilds swap sources across surfaces (select_sources is resolution-driven); probe byte-identity first, else surgical-append with a diff proof. |
| 7 | RUN-015 | `page N` does not parse in r4 — use `pN`; semicolon-joined citations must split one-per-paren; RUN-COMPUTED labels stand alone outside citation parens. |
| 8 | RUN-015 | Quote binding breaks on injected punctuation, quote-nesting, YAML `''` escaping, paraphrase, mid-quote ellipses, and quoting non-pack documents; quote only from read excerpts and prefer clean endpoints. |
| 9 | RUN-015 | Prose-paren citation forms (`(prose; SRC-X, loc)`) are invisible to the gate regex; sweep them explicitly in any citation pass. |
| 10 | RUN-015 | The r4 quote-binding gate can manufacture cross-pairing violations after ANY quote repair changes the record's fragment structure — re-gate after each repair round and expect the violation set to move. |
| 11 | RUN-015 | A partial-failure restore must be scoped to the artifacts the stage owns — restoring the whole `artifacts/` tree mid-run reverts OTHER stages' completed deploys (Stage B's restore reverted Stage A's 6 deployed stamps; re-deployed byte-identically from the staged bodies, receipt shas matched). |
| 12 | RUN-016 | The manifest validator models the landing lifecycle only: REQUIRED-presence reads artifacts/ alone (F4a) and the status rule rejects QA_PASSED/STAGED/PUBLISHED location-blind (F4b) — a fully staged/published library flips validate-manifest red and cannot re-validate its published files in place; the governed transition receipts (stage/publish, content-bound QA evidence) are the evidence chain of record. |
