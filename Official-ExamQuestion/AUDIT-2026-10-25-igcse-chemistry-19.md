# Honest Audit — Official-ExamQuestion / igcse-chemistry-19

**Audited:** 2026-10-25 · remote `main` (mirror of the chemistry subtree, tree `942bb7a6`, complete, 577 blobs)
**Scope:** 54 official sets (16×4CH1-1C, 16×4CH1-2C, 11×4CH1-1CR, 11×4CH1-2CR) · **2,607 parts · 4,860 marks** · 469 asset PNGs · CROP-REVIEW ledger · SOLUTION-ENRICH ledger · hub bundle `official-papers.json` (v2 `main`)
**Method:** every claim below was checked programmatically against the mirrored corpus; missing-image candidates were verified against the actual QP PDFs (ground truth) where stated.

---

## 1. Verdict (honest, one paragraph)

The corpus is structurally excellent and honestly terrible in exactly one place. Structure, marks, keys and the hub export are essentially perfect: 0 duplicate ids, 0 mark-sum violations, 0 empty fields, all 432 G0–G7 validation gates PASS, all 143 MCQs single-keyed with A–D labels, all 4 MCQ-KEYS adjudications match the corpus, the hub bundle matches the corpus set-for-set (counts, marks, assets), all 424 embedded figure URLs resolve HTTP 200, and the enrichment layer propagates **2,607/2,607 byte-identically** to what learners see. The one weak spot is **artwork**: 3 figures are confirmed missing from the interactive papers (verified against the QP PDFs), 8 parts carry an honest `crop-required` stub instead of an image, and 36 parts across 28 papers still need a human QP-vs-corpus figure review. There are also two cosmetic-but-real text classes: Pearson MS footer lines leaked into 57 `mark_points`, and 16 BEL control characters in question stems (cleaned by the exporter, so never user-facing).

---

## 2. What was checked and what passed

| # | Check | Result |
|---|-------|--------|
| 1 | Inventory: 54/54 topic.json, dirs = `paper_info` (session + code), duplicate question ids | **PASS** (16/16/11/11, 0 dups) |
| 2 | Marks: Σ(part marks) = question `total_marks` for every question; Σ(questions) = paper total (1C/1CR = 110, 2C/2CR = 70); no part ≤ 0 marks | **PASS** (0 violations corpus-wide) |
| 3 | Mark points: Σ(MP marks) = part marks wherever MPs exist (4,161 MPs) | **PASS** (0 mismatches) |
| 4 | MCQ: exactly one `is_correct` per part, labels = A–D, no empty problem/solution (2,607/2,607 populated) | **PASS** (1 anomaly, see §4) |
| 5 | MCQ-KEYS.json (4 adjudicated keys incl. the 2020-01 2CR `1(b)(i)` re-key) vs corpus choices | **PASS** (4/4 match) |
| 6 | Text corruption: control chars, PUA (U+E000–F8FF), mojibake (Ã/â€/U+FFFD) in problem/solution/choices/mark_points | **PASS** (0 in those fields) |
| 7 | Validation gates: all 54 `validation-report.json`, G0–G7 | **PASS** (432/432 gates PASS) |
| 8 | Assets referenced by topic.json exist in the repo tree | **PASS** (355/355, 0 missing files) |
| 9 | Hub `official-papers.json` vs corpus: 54/54 sets, part counts, marks, asset counts, asset-with-path counts | **PASS** (0 diffs) |
| 10 | Enrichment propagation: hub `solutionMd` == SOLUTION-ENRICH.json for every part | **PASS** (2,607/2,607 byte-equal) |
| 11 | Embedded figure URLs (markdown `![]` → raw.githubusercontent) | **PASS** (424 URLs; sampled 12, all HTTP 200) |
| 12 | Solution authoring: corpus solution_md is verbatim MS extraction by design; user-facing solutions come from the enrichment layer via export | **PASS** (verified end-to-end) |

---

## 3. CONFIRMED defects — missing images (the important one)

Three figures verified **real and missing** by opening the QP PDFs and comparing:

| # | Paper / question | What the learner should see | Evidence |
|---|------------------|------------------------------|----------|
| 1 | 2019-06 1C **Q11(b)(i–ii)** | Large apparatus diagram (methane flame → U-tube in ice → limewater flask → pump); both parts answer from it; the stem says "The diagram shows methane burning in air…" | QP p.16 shows the full diagram; corpus question has **zero** assets |
| 2 | 2019-06 1C **Q12(a–c)** | Calorimeter diagram (thermometer + polystyrene cup); stem says "A student uses this apparatus…" | QP p.18 shows the diagram; corpus question has **zero** assets |
| 3 | 2025-06 1C **Q9(a)(i–ii)** | Displayed formula of chloroethene; stem says "This is the displayed formula of chloroethene" | QP p.20 shows the structure; corpus ships a `crop-required` stub with no image |

Mechanism: the exporter embeds figures as markdown image links (387 parts, 424 links) — these three questions never got a crop, so nothing is embedded. The crop ledger was *honest* about 2 of the 3 (verdict `stub-accepted`), but honesty in the ledger is not an image in front of the learner.

### 3a. The 8 `crop-required` stubs (ledger-known, subset need work)

`CROP-REVIEW.json`: 115 crops reviewed — **107 accepted, 8 stub-accepted**. The 8 ship to the hub as `kind:"crop-required"` (no image, honestly flagged):

- 2021-06 1C 8(b)(iii) — **verified OK as stub**: the QP has no figure (draw-it-yourself dot-and-cross task)
- 2025-06 1C 9(a)(i) — **verified REAL missing** (see §3 #3)
- 6 unverified: 2019-06 1CR 6(c)(ii) p.15 · 2020-11 1CR 7(b)(ii) p.16 · 2021-01 1CR 10(b)(i) p.28 · 2021-11 2C 5(c) p.15 · 2023-01 1CR 5(b)(ii) p.15 · 2026-06 1C 6(b) p.18

### 3b. Review queue: 36 figure-language candidates without any figure

Parts whose problem text uses figure language ("The diagram shows…", "this apparatus…", "displayed formula") where **no part of the question embeds an image** and the text is not a draw-task. Full machine-readable list: `missing-image-candidates.json` (36 parts / 28 papers). Visually verified so far: 3 real (§3), several are false alarms (e.g. "Name a piece of apparatus suitable for measuring 25.0 cm³" needs no figure). **Every one of the 36 needs one human QP page check.** Worst papers: 2024-11 1C (3), 2021-11 2C (2), 2019-06 2C (1 + 2 apparatus).

### 3c. Figures text-extracted as letter soup (related defect)

Where a figure WAS extracted as text instead of cropped, the problem text contains layout debris, e.g.:
- 2022-06 1C 5(a)(iii): "This is the displayed formula of one of the isomers. **H H H H H H C C C C C** H H H H H H…"
- 2022-01 1CR 6(c): "The displayed formula of ocimene is **H H H C H H C H H**…"
- 2020-01 1C 3(a): "The diagram shows two samples of iron, A and B. **iron iron zinc A B** Sample B…"

Learners see atom-letter soup where a structure should be. Same root cause as §3 (crop never made), different symptom.

---

## 4. Minor defects (cosmetic / non-user-facing, but real)

| # | Finding | Count | Detail |
|---|---------|-------|--------|
| 1 | Pearson MS footer leaked into `mark_points` text | **57** (10 papers) | e.g. 2021-01 1CR 1(f): "oxygen and sulfur in either order\n**(Total for Question 1 = 6)**". Worst: 2022-01 1C (10). These render inside the expandable mark scheme UI. |
| 2 | BEL control char `\x07` in question stems / group stems | **16** stems | Numbered method steps ("Step 1 \x07add 25 cm³…"). **Not user-facing** — the exporter strips them and inserts newlines (verified in hub output). Should still be fixed at source. |
| 3 | Ambiguous MCQ from extraction | **1** | 2026-06 1C 1(a): choices A and D are **both** "NH4+", A=False, D=True. The printed options must differ (superscript/charge placement) but extraction flattened them into identical strings. |
| 4 | Orphan asset files (in repo, never referenced) | **58** | Mostly superseded stem/table crops. Harmless; hygiene item. |
| 5 | Corpus-thin solution (verbatim layer) | **1** | 2022-06 2CR 1(a)(i): 3 marks, corpus solution "P neutron\nQ proton\nR electron" (29 chars). **Not user-facing** — the hub serves the authored enriched version. |

Nothing else: 0 control chars in user-facing fields, 0 PUA, 0 mojibake, 0 empty fields, 0 broken links, 0 mark arithmetic errors.

---

## 5. What this audit did NOT check (honest limits)

- Whether every accepted crop is the **right region** of the right page (needs eyes on 355 PNGs; spot-checked 3 via the QP comparison above, all consistent).
- Chemistry correctness of the 2,607 authored solutions beyond the F60 harness they passed at authoring time (wave-22, verifier-clean).
- The `questions.md` derivatives (low value — derived from topic.json).
- Parallel corpora (this audit is igcse-chemistry-19 only; the rule below makes it repeatable for any course).

---

## 6. Recommended fixes, in order

1. **Crop the 3 confirmed missing figures** (2019-06 1C Q11(b) apparatus, Q12 calorimeter; 2025-06 1C 9(a) displayed formula) and re-export. Highest UX value, lowest effort.
2. **Run the 36-part review queue** against QP pages (each = open QP page, yes/no crop needed). Convert the ~12+ real ones into crops; record verdicts in CROP-REVIEW.json.
3. **Fix the ambiguous MCQ** 2026-06 1C 1(a) (restore the A/D distinction, likely superscript charge) — same class as the 2020-01 2CR re-key.
4. **Strip MS footers from mark_points** (57) — one regex pass + re-export; teach the extractor to drop "(Total for Question N = M)" lines permanently.
5. **Fix BEL at source** (16 stems) so the corpus is clean even without the exporter's cleanup.
6. **Delete or reference the 58 orphan crops** (repo hygiene).

---

## 7. Provenance

- Mirror: `oe-audit/mirror/` (raw.githubusercontent CDN, no token) — 115 files + tree listings; scripts `run_audit.py` … `run_audit5.py` in `oe-audit/` are re-runnable end-to-end.
- Ground truth PDFs: `oe-audit/qp/{2019-06,2021-06,2025-06}.pdf` from `SyllabAI/syllabai-pastpapers` (path scheme `past-papers/<spec>/past-papers/<session>/<dir>/qp.pdf`).
- Hub bundle: `oe-audit/hub/official-papers.json` (v2 `main`, 4,106,667 bytes).

---

## 8. Resolution (wave-24, F64/F65 — same day)

Every confirmed defect in §3/§4 closed at source by wave-24 (converter v0.17.0):

| Audit finding | Resolution |
|---|---|
| §3 #1 2019-06 1C Q11(b) apparatus | cropped (`asset_11_stem_apparatus`, p16 raster ink-profile rect, eyeballed) |
| §3 #2 2019-06 1C Q12 calorimeter | cropped (`asset_12_stem_calorimeter`, p18) |
| §3 #3 2025-06 1C 9(a) chloroethene | stub upgraded to a real crop (`asset_9_a_i_diagram`, p20) |
| §3a 8 crop-required stubs | 1 upgraded (above); the 7 remaining are the honest blank-scaffold stubs (§3a list), re-verified in waves 13–15 |
| §3b 36-part review queue | fully dispositioned — 24 figures cropped, 12 dismissed with QP-page evidence (`FIGURE-QUEUE.json`, canary C73 keeps it closed) |
| §3c figure-as-text letter soup | the crops above serve the figures (2020-01 3(a), 2022-06 5(a)(iii), 2022-01 6(c) among them); the flattened label runs stay in the corpus text (G2 verbatim plane) while the served problemMd carries the crop |
| §4 #1 57 MS footers in mark_points | OPEN (not in this wave's scope; exporter strips at serve time — next wave) |
| §4 #2 16 BEL control chars | OPEN (exporter-cleaned; not user-facing — next wave) |
| §4 #3 ambiguous MCQ 2026-06 1C 1(a) | CLOSED at source — converter v0.17.0 F64 span-geometry script restoration; A=NH⁴⁺ is now distinct from D=NH₄⁺ (canary C72 pins it); 55 choice strings restored corpus-wide |
| §4 #4 58 orphan crops | OPEN (repo hygiene; harmless — next wave) |
| §4 #5 thin verbatim solution | not user-facing (hub serves the authored enrichment); no action |

Serving delta of record: 40 parts (26 figure embeds + 14 choice restorations),
G-E1-matched against `scripts/exporter-disclosures/2026-10-25-wave24-g8-fixes.json`.

---

## 9. Resolution (wave-25, F69/F70/F71 — 2026-10-26)

The §4 OPEN classes closed at source one day later (converter v0.18.0). The
re-census at ship time measured each class fresh (census before ship), so the
numbers below supersede this report's §4 estimates where they differ:

| §4 finding | Ship-time census | Resolution |
|---|---|---|
| §4 #1 "57 MS footers in mark_points" | **362 furniture lines in 245 corpus text blocks** (153 parts, 50 slices) — the question-total footer in BOTH printed word orders, the paper-total line, the bare 'Total = N' fragment (2025-06 layouts), and the Pearson copyright block | parse_ms drops every observed shape at source (F69); 50 served mark points cleaned (44 footer tails + 3 footer-only blocks); the 3 footer-only masquerades re-linked through the F47 MS-LINK-OVERRIDES ledger with eyeballed verbatim transcriptions (2021-01 2CR 7(d), 2025-06 2CR 7(c)(ii), 2025-06 1CR 9(d)(ii) — 7(d) had been serving an EMPTY mark-point text); canaries C77/C80/C81/C82. Serving delta: markPoints on exactly 50 parts / 48 slugs, disclosure `scripts/exporter-disclosures/2026-10-26-wave25-sec4-hygiene.json` |
| §4 #2 "16 BEL chars" | 15 strings (6 question stems + 9 group stems; one stem carried 3) | stripped in clean_lines + the page_norm anchor index at source (F70); canary C78 |
| §4 #4 "58 orphan crops" | 57 unreferenced PNGs (one was re-referenced by wave-24's crop wave) | pruned; referenced-asset census = 0 orphans (F71); canary C79 |
