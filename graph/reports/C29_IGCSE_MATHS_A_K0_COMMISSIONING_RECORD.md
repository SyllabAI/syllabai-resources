# C29 — Subject-#2 K0 Commissioning Record — igcse-maths-a (4MA1 Higher)

| | |
|---|---|
| **Task ID** | T-C29 (K0 of the C28 per-subject commissioning playbook, spec §6) |
| **Version** | 1.0 — commissioning record. Gate state K0(i)–(iv) assessed and recorded; nothing downstream of K0 is executed by this task. |
| **Date** | 2026-09-30 |
| **Operator directive** | "① commission K0/T-C29 for igcse-maths-a" (2026-09-30, zai-web, inline) — this is the K0(iii) commissioning directive, naming the qual |
| **Prior operator decision (D4 selection)** | "I want Maths A Higher." — subject #2 = Edexcel International GCSE Maths A **Higher** tier, code **4MA1**, qual `igcse-maths-a`, course lane `igcse-maths-a-18-higher` |
| **Baseline** | syllabai-resources `origin/main` @ `4ad1673` (local == remote, tree clean at assessment time); hub evidence: syllabai-web `content/` @ `132c15a` (the layer-3 import run itself was certified at hub `bdb7a3a`, resources `1245df0`, 2026-09-28) |
| **Predecessors** | `C28_MULTI_SUBJECT_EXPANSION_SPEC` (landed v1.1) + `C28_GRAPH_LAYOUT_MIGRATION_RECORD` + `C28_SERVING_PLANE_RECORD` (D4 gate state); layer-3 subject-#2 import tooling `4ad1673` (s104/s105 + verifier, PASS 6,372 checks + core ingest test) |
| **Verification** | `scripts/c29_k0_check.py@3530ff80c3810b2e` → `graph/reports/C29_K0_CHECK.json@6286341eb5556561` (G1–G6, all PASS) |

---

## 1. What this record does (and does not do)

K0 is the commissioning gate: it verifies the four §6-K0 conditions for
`igcse-maths-a` and puts the qual on the K1–K4 program. Per C28 design
principle **P3 (folders follow commissioning)**, a K0 record is exactly the
act that authorizes the qual's program to *begin* — it does not itself create
any ratified-plane state. Accordingly this task touches **zero** bytes in
`graph/` stores, `parsed/**` canonical JSON, or the SME corpora: its footprint
is this record, its JSON twin, the checker, and the checker's report. Gate G6
of the verification battery asserts the P3 discipline live (no
`graph/igcse-maths-a/`, no registry entry, no ratified-extensions in the
serving plane for the qual).

The commissioning sequence this record sits in: the operator selected Maths A
Higher as subject #2 (D4 selection, recorded above), the layer-3 Smart Mark
import package for 4MA1 landed 2026-09-28 (`4ad1673`: curriculum draft 6/39/188
= 234 node codes; question package 2,701 questions, verifier PASS, core ingest
test green), and this directive now opens the knowledge-graph program for the
same qual. Layer-3 and the KG program share the curriculum spine: the s105
draft's tree shape (6 units S1–S6 / 39 topic nodes / 188 spec points, node
codes `4MA1-S<section>-<letter>[-<point>]`, mirroring the 4CH1 precedent
`4CH1-S1-c`) is the shape K1's stores must agree with.

## 2. K0 gate assessment (spec §6, the four conditions)

| Condition | State | Evidence (machine-verified unless noted) |
|---|---|---|
| **K0(i)** — parsed bundle exists, `parse_report` ALL_PASS | **PASS** | `Official-Specifications/parsed/igcse-maths-a/` carries the 6 canonical files + raw parse; `parse_report.json` gates G1_schema_present / G2_ids_unique / G3_provenance_complete / G4_id_prefix_valid all `true`, **ALL_PASS**; counts 242 spec points / 18 topics / 78 subsections / 0 practicals / **8 flagged**; the 242 rows dedupe to **188 unique `official_code`s** (54 codes listed in both tiers — the K1 store base is 188, matching the s105 draft and the hub manifest); flagged codes: `4.5D, 3.1A, 3.2B, 3.2D, 3.3A, 3.3B, 3.3E, 4.6C` (they stay for teacher review, confidence 0.95 in the draft — the s105 convention); spec-PDF provenance sha1 `b71a6432b8e34c155efb510d79a7b6e97611ba01`. Pins: parse_report `sha256_16` + spec_points `sha256_16` in the check report |
| **K0(ii)** — notes corpus secured for the qual | **PASS** (see the dated errata in §3) | Three evidence layers: **(a) upstream, in-repo** — `SME-RevisionNotes/igcse-maths-a-18-higher/` (schema `syllabai.sme-revision-notes-course/1.0`): manifest counts pages_expected **191 = pages_scraped 191**, fetch_failures **0**, assets **389**, asset_failures **0**, spec_point_links **203**, guided_study_pages 143, markdown_chars 864,016; 191 note `.json` + 191 `.md` pairs on disk in the committed tree (per-note schema `syllabai.sme-revision-note/1.0`, Wiris MathML kept verbatim per the corpus README); **(b) authorization** — `LICENSE-DATA.md` **Amendment 2026-09-17**: the operator attests Save My Exams permission ("there is no licensing issue with SME, I have their permission. (in fact they will be sponsoring me)"), recorded verbatim in-session; **(c) downstream mirror** — hub bundle `content/igcse-maths-a-18-higher/manifest.json` (importSource `SyllabAI/syllabai-resources@7575585`, upstreamSchemas incl. `sme-revision-note/1.0`, curriculum 4MA1/IGCSE/Maths/2016): counts 6 sections / 39 topics / **188 specPoints** / **191 notes** / 2,703 questions / 999 flashcards — agreeing with the upstream lane and with s105 on every count |
| **K0(iii)** — operator commissioning directive names the qual | **PASS** | This record's directive row: "① commission K0/T-C29 for igcse-maths-a" (2026-09-30), preceded by the D4 selection decision; checker G3 asserts the record names the qual, the task ID, and the directive verbatim |
| **K0(iv)** — scope estimate via the batch-forecast model | **PASS** | Model inputs (C28 spec §6-K0(iv), sourcing the §16 sanctioned pilot ratios and the chemistry program's observed actuals): pilot 2.4 nodes/SP, 2.75 authored-edges/SP, 1.0 held/SP; discipline-adjusted observed ~1.0 nodes/SP, ~1.6 edges/SP; ~12 SP/batch. Applied to SP base 188: **pilot model** nodes ≈ **451**, authored edges ≈ **517**, held ≈ **188**; **discipline-adjusted** nodes ≈ **188**, authored edges ≈ **301**; **≈ 16 batches** at the sanctioned ~12-SP batch shape (188/12 = 15.7). Checker G5 recomputes these from the live bundle so the record and the model cannot drift |

**Chemistry-precedent proportionality note (for planning, not a gate):** the
chemistry program ran 182 SPs → 12-SP pilot + 14 batches; the 188-SP base
projects to roughly the same program length (≈ 15–16 batches). Maths carries
**0 practicals** (chemistry 12) — the K1 practicals store will be empty-by-
parse for this qual — and its SME index is **name-only** (no definitions), so
the verbatim crossref lane that chemistry used is not applicable (this is
recorded in the qual's own `parse_report.json` `sme_crossref` note: "mapping-
stage name bridging").

## 3. Dated errata — the C28 serving-record D4 "gate RED" assessment

`C28_SERVING_PLANE_RECORD.md` (2026-09-21, stage 4) recorded D4 as
"**OPEN — gate RED (K0(ii))**: Notes-corpus-gated: no equivalent notes corpus
exists for any candidate". That assessment was a **sparse-workspace visibility
artifact, and is corrected here by this newer record** (per P5 the older
record stays byte-untouched): the SME revision-notes corpus had already landed
in-repo four days earlier — `9cb934a` (2026-09-17 09:40 UTC, "revision-notes
corpus — all 39 Edexcel courses, T-SME-NOTES-3..5", including
`igcse-maths-a-18-higher` at 191/191 pages), extended to 49/49 courses by
`9e6b2cd` (2026-09-19) — with the operator's Save My Exams authorization
attested the same day (LICENSE-DATA.md Amendment 2026-09-17). The stage-4
record's own parenthetical ("Chemistry's own SME corpus is tracked in-repo but
is not materialized in this sparse workspace — the c13 in-repo
corpus-presence guard fires") documents the same mechanism that produced the
miss for the candidate quals. Nothing was weakened by the correction: the
corpus bytes, the record, and the audit trail are untouched; only the gate
state moves, on evidence.

**K2-prerequisite work item recorded now (not yet built):** chemistry's
ratified concept layers stand on the notes corpus **joined to official 4CH1
spec_point_codes** (`sme_notes_chem_join.py`: AI_VALIDATED operator-delegated
+ operator-validated legacy `spec_map`). No maths-a equivalent join exists —
the qual's SME index is name-only (203 `spec_point_links` in the manifest are
unvalidated anchors), and the parse_report prescribes mapping-stage name
bridging. K0(ii) clears **corpus securing**; the notes↔SP join for
`igcse-maths-a-18-higher` is the first K2-lane prerequisite the program must
build before T-C10/T-C11-pattern authoring can start.

## 4. Verification battery

`scripts/c29_k0_check.py` (zero-LLM, deterministic, read-only toward graph/
corpus/parsed; writes only its own report):

| Gate | Asserts |
|---|---|
| **G1** `k0_i_parsed_bundle` | 6 canonical bundle files present; parse_report G1–G4 + ALL_PASS; counts 242/18/78/0/8; 188 unique official_codes; exactly the 8 flagged codes; PDF sha1 surfaced |
| **G2** `k0_ii_notes_corpus_secured` | Course manifest schema + counts (191/191/0 failures/389 assets/203 spec links); 191 json + 191 md note files in the committed tree; sample note schema/course_slug; corpus README row; LICENSE-DATA.md Amendment 2026-09-17 present |
| **G3** `k0_iii_operator_directive` | This record exists, names `igcse-maths-a`, `T-C29`, and quotes the directive verbatim |
| **G4** `hub_mirror_agreement` | (with `--hub-repo`) hub manifest counts 6/39/188/191/2703/999, curriculum code 4MA1, importSource + upstreamSchemas agreement |
| **G5** `k0_iv_scope_estimate` | The §2 scope table recomputed from the live bundle (451/517/188 pilot; 188/301 adjusted; 16 batches; SP base == live unique-code count) |
| **G6** `p3_folder_discipline` | `graph/` contains only `igcse-chemistry` + `reports`; registry has no `igcse-maths-a` qual entry; serving plane has no ratified extensions for the qual |

Result this assessment: **G1–G6 all PASS, exit 0** (G4 executed with the hub
checkout @ `132c15a`) — `graph/reports/C29_K0_CHECK.json` (sha256_16
`6286341eb5556561`, the landing run), run at baseline `4ad1673`. Sparse-workspace note: reads
are disk-first with `git show HEAD:` fallback (the C28-F1 mechanism); the
check report records which method served every read (the corpus lane reads
all resolved via git-show in this workspace). One defect was caught and fixed
during the battery's own shakedown before the landing run: G4's schema
membership test used list `in` (exact-element) against a namespaced element —
fixed to the strict full-name match; no gate was loosened.

## 5. K1 readiness (what this commissioning arms; not executed)

Per spec §6-K1, subject-#2 K1 is now "just a registry entry + new
`graph/<qual>/` stores" (the operator's own framing, adopted by C28 stage 4):
a c23-pattern emitter turns the canonical JSON into
`graph/igcse-maths-a/specification_points.yaml` + the 4 sibling spec-text
stores with explicit meta/lineage (no `dict(old_meta)` inheritance), the
registry gains the qual, `graph_check` extends to the new paths, and the gate
is canonical equality 1:1 with counts == parse_report (188/39-topic-node
shape agreement with the s105 draft) in a single commit + record. Expectations
to carry into K1: practicals store empty-by-parse (0); both-tier dedupe
already settled at 188 by `official_code`; the 8 flagged rows must survive
into the store flagged (they are teacher-review items, not defects to silently
drop). K2 (ratified enrichment) remains operator-gated per batch exactly as
the chemistry sequence, and its first prerequisite is the §3 notes↔SP join
work item. K3/K4 (serving + acceptance) reuse the C28 emitter/S8 machinery
unchanged.

## 6. Scope guards (standing)

Node states byte-untouched; 2012-Jan escalations and the data bridge not
approached; C25/C26/C27/C28 records unedited (the §3 errata lives here, not
there, per P5); `parsed/**` canonical JSON untouched; SME corpora untouched;
no explorer/projection changes (P3: no ratified work exists yet for the qual);
all ratified-plane writes beyond K0 flow through operator gates; no core or
hub serving behavior changes from this repo.
