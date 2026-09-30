# C30 — Subject-#2 K1 Spec-Store Build Record — igcse-maths-a (4MA1 Higher)

| | |
|---|---|
| **Task ID** | T-C30 (K1 of the C28 per-subject commissioning playbook, spec §6) |
| **Version** | 1.0 — K1 executed. The 5 spec-text ratified stores exist; the qual's program earns its next stores only through K2+. |
| **Date** | 2026-10-01 |
| **Operator directive** | "the natural follow-on is firing K1 (c23-pattern emitter → 5 spec-text stores + registry entry)" (2026-10-01, zai-web, inline) — arming the K0/T-C29 commissioning |
| **Baseline** | syllabai-resources `origin/main` @ `8430547` (the T-C29 K0 landing; local == remote, tree clean at build time) |
| **Predecessors** | `C29_IGCSE_MATHS_A_K0_COMMISSIONING_RECORD` (all four §6-K0 conditions PASS); `C23_DEFINITIVE_SWAP_RECORD` + `C26_SIBLING_STORE_REFRESH_RECORD` (the c23 emitter pattern); `C28_MULTI_SUBJECT_EXPANSION_SPEC` §6-K1 gate definition |
| **Verification** | `scripts/c30_k1_check.py@b0ffbaff67f1b707` → `graph/reports/C30_K1_CHECK.json@d4e80ad7d0d0f362` (G1–G10 all PASS, exit 0) |

---

## 1. What landed

**Emitter — `scripts/c30_emit_maths_a_spec_stores.py@390c5ee8151cfe9c`** (zero-LLM,
deterministic — byte-identical re-run verified; all store paths resolve through
the C28 registry; fail-closed pre/post conditions; the c23/c26 pattern with no
`dict(old_meta)` inheritance — every row carries its own explicit lineage).

| Artifact | Content | sha256_16 |
|---|---|---|
| `graph/igcse-maths-a/specification_points.yaml` | meta + **188** point rows (code `4MA1-<official_code>`, e.g. `4MA1-1.1A`; section `4MA1-S1..S6`; subsection `4MA1-S<n>-<sub>`, e.g. `4MA1-S1-1.1`; wording verbatim; `ordering` = canonical walk ordinal verbatim; `global_order` 1..188 derived; applicability {tier, papers, rule} verbatim; the 8 parse-flagged rows carry `math-fragment-assembly` verbatim) | `33d3e5313d37464a` |
| `graph/igcse-maths-a/topics.yaml` | 6 topic rows (`4MA1-S1..S6`, **Higher-walk titles**) + 39 subtopic rows (`4MA1-S<n>-<sub>`, letter = the subsection code, titles **null** — the spec numbers content subsections without titles, recorded not invented; `spec_points` membership lists) | `9febc0f296343329` |
| `graph/igcse-maths-a/practicals.yaml` | empty by parse (0 practicals; canonical note carried verbatim) | `57bc13d247e16966` |
| `graph/igcse-maths-a/assessment_objectives.yaml` | 3 AO statements + 3 unit-weighting rows, verbatim (AO1 57–63%, AO2 22–28%, AO3 12–18%; unit tables for Papers 1F&2F / 1H&2H / Total, p. 49) | `8579017a208035a7` |
| `graph/igcse-maths-a/command_words.yaml` | empty by parse — "no command-word taxonomy table in source specification" (canonical note verbatim) | `610a29ded0017922` |
| `graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json` | the tier-dedupe ledger: rule + census + all **54** dup-code rows with BOTH tier variants (text + page + ordering) + the section-title variants | `7f9322a8a05d3767` |

**Registry entry** — `scripts/graph_paths.yaml` gains `quals.igcse-maths-a` with
the 5 store templates (P3: the store set grows as the program earns stores —
concepts/edges/chunk-maps/kinds arrive with K2, relationships with the
ratified-hierarchy lane; no root-form legacy paths ever existed for this qual,
so no `legacy_map` entries). `scripts/check_no_hardcode.py`'s
`registry_consistency` is extended from default-qual-only to **every** registered
qual (the S0 layer of "graph_check extended to the new paths"): 15 stores now
resolve across 2 quals, legacy_map == derived (10), no-hardcode scan 0 bad.

## 2. The one semantics decision: tier dedupe (higher-preferred)

The 4MA1 specification presents content in TWO tier walks (Foundation pp.
17–30, Higher pp. 35–45). 242 canonical rows dedupe to 188 unique
`official_code`s: **54 codes appear in both walks — 53 of them with DIFFERENT
statements per tier** (e.g. `1.3A` Foundation "use decimal notation" vs Higher
"convert recurring decimals into fractions"), 1 with identical text; plus 26
Higher-only and 108 Foundation-only codes.

The store carries **one row per official_code** (matching the chemistry store
shape, the s105 curriculum draft's node count, and the hub manifest's 188),
choosing the **Higher-tier statement wherever the code exists in the Higher
walk** — the operative wording for the commissioned Higher program (the
operator's D4 selection). The 108 Foundation-only statements are carried
verbatim from their Foundation rows — the spec's own applicability rule
declares them "assumed knowledge for Higher Tier papers". Every per-code
choice and both wording variants are in the ledger: **nothing is silently
dropped** (the C26 "never silently fixes" rule applied to tier dedupe). The
same rule selects section titles from the Higher walk (section 4 is
"Geometry and trigonometry" there vs "Geometry" in the Foundation walk —
variant recorded).

**Known cross-layer divergence (recorded, not repaired here):** the s105
curriculum draft (layer-3, landed `4ad1673`) deduped the same 242 rows
first-wins, so its 53 affected draft titles carry the Foundation wording.
That draft is SUGGESTED/provisional scaffolding (confidence 0.95, teacher
review lane); the K1 store is the definitive spec-text source. Any hub/core
title refresh is core-lane work outside this repo's scope guards — flagged
here so the divergence is a known fact, not a surprise.

## 3. Verification battery (all PASS, exit 0)

| Gate | Asserts |
|---|---|
| **G1** `canonical_equality_1to1` | 188 store rows == 188 canonical unique codes; wording whitespace-normalised equal to the chosen canonical row; leading_verb/ordering/scope/applicability(tier+papers+rule)/flags/practical verbatim; global_order contiguous |
| **G2** `topics_subtopics_closure` | 6 topics / 39 subtopics; titles == Higher-walk titles (topics.json numbered rows agree); subtopic.spec_points membership == SP store codes exactly; parents resolve; orderings contiguous; letter == subsection code; parent section agrees with letter |
| **G3** `counts_match_parse_report` | meta counts (188/6/39/0/0) consistent across ALL 5 stores; parse_report 242 rows / 8 flagged preserved; the 242→188 dedupe documented |
| **G4** `schema_provenance_namespace` | every row RULE_DERIVED / confidence 1.0 / version 1 / damage_flags list; provenance complete (tier, source_file, extraction_method, generator, date, pdf_source, pdf_sha1 `b71a6432…`, pdf_page ≥ 1, pdf_oy, canonical_builder); all codes in the `4MA1-*` namespace; foreign-code scan (4CH1/4SD0/WMA/WPH/IAL) zero hits |
| **G5** `tier_dedupe_integrity` | ledger rows == observed dup pairs (54); every ledger row's higher text == the store wording AND provenance.tier_walk == Higher; all 53 reworded rows carry the dedupe note; census 53/1/26/108; section-4 title variant present |
| **G6** `damage_scan_zero` | the C27 S1 damage-class scanner over all 5 stores: 0 hits; 0 md-OCR residue |
| **G7** `empty_by_parse_stores` | practicals/command_words empty with the canonical notes verbatim |
| **G8** `assessment_objectives_verbatim` | 3 statements + 3 unit weightings, every field verbatim incl. pdf pages |
| **G9** `chemistry_graph_check_green` | `graph_check.py` exit 0 — the default qual untouched by the landing |
| **G10** `no_hardcode_registry_green` | `check_no_hardcode.py` exit 0 — 0 bad, 15 stores resolve across 2 quals, legacy_map == derived |

## 4. Not derived for this qual (documented, never silently missing)

`draft_skill_tags` (chemistry's c09-era authoring aid; no canonical source in
the maths parse); `spec_issue` (no issue string asserted by the canonical
parse — `syllabus_version: 2016` per the hub registry and s105 usage);
`practicals` (0 by the parse's `practical:` prefix rule); `command_words` (no
taxonomy table in the source specification); `official_bullets` (canonical
`sub_items` empty on all 242 rows); subtopic titles (the spec numbers content
subsections without titles — canonical `subsection.title` empty on all 242
rows). The derived serving plane (`parsed/_derived/graph/igcse-maths-a/` 4
parse-derived files) is untouched — projection re-pointing to the ratified
stores is K3 work per the spec.

## 5. Scope guards + what K1 arms

Zero bytes changed in `graph/igcse-chemistry/`, `parsed/**` canonical JSON,
SME corpora, or the derived plane; the C25/C26/C27/C28/C29 records untouched;
no core/hub serving behavior changed from this repo. K2 (operator-gated per
batch, chemistry sequence replayed) is now armed: its first prerequisite
remains the notes↔SP name-bridging join recorded at K0. K3 (serving/explorer)
and K4 (extended battery) reuse the C28 machinery. The next operator gates:
K2 batch authoring directive, then per-batch verdicts.
