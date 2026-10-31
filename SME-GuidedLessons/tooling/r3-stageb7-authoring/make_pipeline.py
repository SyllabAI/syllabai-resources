#!/usr/bin/env python3
"""Parameter-transform: r3-stageb6-pipeline.js -> r3-stageb7-pipeline.js.
Every replacement is occurrence-checked (count must match exactly) — the
S-B5->S-B6 transform's two bugs (interpolated var in P0; wrong untouched bucket)
are guarded by explicit constant blocks here + the pipeline's own gates after.
"""
SRC = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/tooling/r3-stageb6-pipeline.js"
DST = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/tooling/r3-stageb7-pipeline.js"

txt = open(SRC).read()

def rep(old, new, count=1):
    global txt
    n = txt.count(old)
    assert n == count, f"expected {count} occurrence(s), got {n}: {old[:90]!r}"
    txt = txt.replace(old, new)

# ── header docstring (lines 1-40 wholesale) ──────────────────────────────────
head_old = txt[: txt.index('import { createRequire }')]
head_new = '''#!/usr/bin/env node
/**
 * R3-CHECK-TYPES PIPELINE — STAGE B WAVE 7 (S-B7)
 * (operator ignition: "wave 7", hub chat trace 1a18fd512d610f7d, continuing the
 *  stage-B contract of record in R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json, the S-B1 NEXT
 *  ("waves 3..10 to the ~956 total") and the S-B6 promotion receipt merge_order ("stage B wave 7
 *  (next register tranche) remains operator-gated") — gate opened by the operator word above)
 *
 * S-B7 tranche of record: the wave-7 authoring register (9 notes, 19 lessons, 95 MCQs)
 * -> +76 authored written items (38 recall, 19 explain-why, 19 application). FINAL tranche
 * shape read from the register at wave open per the S-B6 NEXT pointer.
 * Schema delta: NONE — the S-B1 union caps (maxItems 45 / check 9 / checkRefs 9) admit this tranche.
 *
 * Stack of record: branch integration/r3-stageb7-20261031 based on the current resources main
 * (wave-open main of record resolved at run time, recorded in input_pins; contains the S-B6
 * merge-of-record 6b70de74 as ancestor — main advanced past it with the unrelated books lanes,
 * disclosed).
 *
 * Inputs (clone /home/z/my-project/syllabai-resources @ integration/r3-stageb7-20261031):
 *   scripts/r3-stageb7/authoring-part{1,2}.json     the 76 authored items (KP-anchored; audit GREEN)
 *   integration/source-0.4/        0.4 generation (D-1 baseline)
 *   integration/source-0.5/        the 71 prior R3 sources (byte-identical re-proof)
 *   integration/hub-import-1.3/    1.3 lesson outputs (D-2 baseline for the tranche)
 *   integration/question-packages/ 1.0 packages (C-9: 32 byte-identical)
 *   integration/hub-import-1.4/ + question-packages-1.1/  the 71 prior-R3 outputs (re-proof)
 *   integration/hub-import-manifest-v13.json + records/INT-3-transform-record-r3-stageb6.json
 *   schema/{guided-lesson.0.5, hub-lesson-import.1.4, sme-question-package.1.1}.json
 *
 * Outputs (namespace-complete):
 *   source-0.5/ x9 (new)           hub-import-1.4/ x9 (new)   question-packages-1.1/ x9 (new)
 *   hub-import-manifest-v14.json   records/INT-3-transform-record-r3-stageb7.json
 *   records/R3-CHECK-TYPES-STAGEB7-PROMOTION-20261031.json
 * + survivors for the hub runner byte-anchors (scripts/r3-survivors/)
 *
 * Gates: A0 authoring inventory, P0 committed==rebuilt x9, D-1 source determinism x9,
 * C-6 ajv (9 sources + 18 tranche outputs + 71 prior-R3 re-proofs + 32 untouched pairs),
 * C-2 preflight vs manifest v13 (224 shas), written-kind invariants x76, MCQ deep conservation x9,
 * C-5 checkRefs closure x9 + x71 prior-R3, D-2 output determinism x9, C-9 package sha
 * conservation x32, G-E stream recompute x112 (32 == v13 anchors; 71 prior-R3 == their anchors
 * exactly; 9 S-B7 rows re-anchored), grand + waves x10 (9 byte-equal vs v13; wave-7 re-anchored).
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */
'''
txt = head_new + txt[txt.index('import { createRequire }'):]

# ── constants block ──────────────────────────────────────────────────────────
rep('const AUTH = "/home/z/my-project/scripts/r3-stageb6";',
    'const AUTH = "/home/z/my-project/scripts/r3-stageb7";')
rep('const SB5_NOTES = ["rn_3B8JxsSjJvR9B4fk","rn_5WvdZNzzhHdjj2Qq","rn_6M5JB7CjvwdDykMS","rn_7Q8M9nVkr2FxCzxd","rn_DGkNCJRcCN4VQ28p","rn_Kd76WccxD9ytSJJC","rn_QzYRzzmwRxk2gKqV","rn_S2fg29M7cqvMj5kT","rn_V9tPMnX6Hq2XnqcP","rn_WJD4ZN4kQfzJNSPV","rn_gBGX339WBpwyCrFF","rn_jXXsc4wt2344BjxX"]; // S-B5, live @ 6fb25fc (PR #243 merged 0e663252)',
    'const SB5_NOTES = ["rn_3B8JxsSjJvR9B4fk","rn_5WvdZNzzhHdjj2Qq","rn_6M5JB7CjvwdDykMS","rn_7Q8M9nVkr2FxCzxd","rn_DGkNCJRcCN4VQ28p","rn_Kd76WccxD9ytSJJC","rn_QzYRzzmwRxk2gKqV","rn_S2fg29M7cqvMj5kT","rn_V9tPMnX6Hq2XnqcP","rn_WJD4ZN4kQfzJNSPV","rn_gBGX339WBpwyCrFF","rn_jXXsc4wt2344BjxX"]; // S-B5, live @ 6fb25fc (PR #243 merged 0e663252)\n'
    'const SB6_NOTES = ["rn_9WM8QhSxmYpGhjqd","rn_BX88twwgffRMgx82","rn_MMkxbt9y3M3XvXrc","rn_ZWrmDYtNGnmFycPM","rn_by5FDNfkqdBCkmXb","rn_dTP52nzhYb96XrJx","rn_nzW5ppBTV3ZnfSYY","rn_p2FmkrXqZSzFngpg","rn_qV5R2cKB59bSKD33","rn_sX8yyBxHn8bS7t46","rn_sf7s7s6bQ2cZv29s","rn_xq9jy75y43kDXkvx"]; // S-B6, live @ 286b5ac (PR #245/#246 merged 6b70de7)')
rep('const PRIOR_R3 = [...PILOTS, ...SB1_NOTES, ...SB2_NOTES, ...SB3_NOTES, ...SB4_NOTES, ...SB5_NOTES]; // the 59 notes already carrying written items (byte-identical this wave)',
    'const PRIOR_R3 = [...PILOTS, ...SB1_NOTES, ...SB2_NOTES, ...SB3_NOTES, ...SB4_NOTES, ...SB5_NOTES, ...SB6_NOTES]; // the 71 notes already carrying written items (byte-identical this wave)')
rep('const REGISTER_W6 = ["rn_9WM8QhSxmYpGhjqd","rn_BX88twwgffRMgx82","rn_MMkxbt9y3M3XvXrc","rn_ZWrmDYtNGnmFycPM","rn_by5FDNfkqdBCkmXb","rn_dTP52nzhYb96XrJx","rn_nzW5ppBTV3ZnfSYY","rn_p2FmkrXqZSzFngpg","rn_qV5R2cKB59bSKD33","rn_sX8yyBxHn8bS7t46","rn_sf7s7s6bQ2cZv29s","rn_xq9jy75y43kDXkvx"]; // wave-6 authoring register order of record',
    'const REGISTER_W7 = ["rn_5g8Dd6y89tkCVJsN","rn_6ZCysv9GnNQmc3w2","rn_T6S7R66N2wSZpWyc","rn_VvsXMdW3TB37JhWF","rn_YWDXCCmjfjkJcs6c","rn_pBp5Z5C2RHTKk7Wn","rn_qb9TBhB6VmnFGjvf","rn_v5JjfpT6grhtq3QW","rn_vVdP57QhDYSVfZgy"]; // wave-7 authoring register order of record (dir listing at wave open)')
rep('const SB5_COMMIT_A = "6fb25fc02d1a7acc71ee2231b547ac85e00705c1";',
    'const SB5_COMMIT_A = "6fb25fc02d1a7acc71ee2231b547ac85e00705c1";\n'
    'const SB6_COMMIT_A = "286b5ac81d43a28e5faa9f9e8ab16b67fbb12c51";')
rep('const OPERATOR_TRACE = "1a18dfb539a4c839"; // "wave 6"',
    'const OPERATOR_TRACE = "1a18fd512d610f7d"; // "wave 7"')
rep('const SB5_IGNITION_TRACE = "1a18d9f731726de1"; // "stage-B wave 5"',
    'const SB5_IGNITION_TRACE = "1a18d9f731726de1"; // "stage-B wave 5"\n'
    'const SB6_IGNITION_TRACE = "1a18dfb539a4c839"; // "wave 6"')
rep('const SB5_MERGE = "0e66325219293c23243c5721dc68199b47a6e71b"; // the S-B5 merge of record (PR #243)',
    'const SB5_MERGE = "0e66325219293c23243c5721dc68199b47a6e71b"; // the S-B5 merge of record (PR #243)\n'
    'const SB6_MERGE = "6b70de744337f41a1cbb9a8ad5ee8e501cd184dc"; // the S-B6 merge-of-record (PR #246, re-merged identical content with the trace-bearing message)')
rep('const WAVE_OPEN_MAIN = "3e918c441d0ceb58e5154e57afec563f29b00161"; // resources main at S-B6 open',
    'const WAVE_OPEN_MAIN = "b57b77f619cd96088399c7da98dc689b69f816b8"; // resources main at S-B7 open')
rep('gate("P0 wave-open main contains the S-B5 merge of record (main advanced past it with unrelated lanes — disclosed)", sb5IsAncestor, RES_MAIN_OPEN_RESOLVED);',
    'gate("P0 wave-open main contains the S-B6 merge of record (main advanced past it with unrelated lanes — disclosed)", sb5IsAncestor, RES_MAIN_OPEN_RESOLVED);')
rep('const sb5IsAncestor = (() => { try { execSync(`git merge-base --is-ancestor ${SB5_MERGE} ${RES_MAIN_OPEN_RESOLVED}`, { cwd: RESROOT }); return true; } catch { return false; } })();',
    'const sb5IsAncestor = (() => { try { execSync(`git merge-base --is-ancestor ${SB6_MERGE} ${RES_MAIN_OPEN_RESOLVED}`, { cwd: RESROOT }); return true; } catch { return false; } })();')
rep('gate("P0 worktree branch == integration/r3-stageb6-20261031", BRANCH_RESOLVED === "integration/r3-stageb6-20261031", BRANCH_RESOLVED);',
    'gate("P0 worktree branch == integration/r3-stageb7-20261031", BRANCH_RESOLVED === "integration/r3-stageb7-20261031", BRANCH_RESOLVED);')
rep('commit A (S-B6 source-0.5 generation)', 'commit A (S-B7 source-0.5 generation)')
rep('process.env.SB6_EMIT_ONLY', 'process.env.SB7_EMIT_ONLY', 3)
rep('const EMIT_ONLY = process.env.SB7_EMIT_ONLY === "1"; // bootstrap: write sources, exit for commit A',
    'const EMIT_ONLY = process.env.SB7_EMIT_ONLY === "1"; // bootstrap: write sources, exit for commit A')  # no-op anchor
rep('if (EMIT_ONLY) { console.log("EMIT-ONLY: 12 source-0.5 files written — commit A, then re-run without SB6_EMIT_ONLY"); process.exit(0); }',
    'if (EMIT_ONLY) { console.log("EMIT-ONLY: 9 source-0.5 files written — commit A, then re-run without SB7_EMIT_ONLY"); process.exit(0); }')

# ── A0 ───────────────────────────────────────────────────────────────────────
rep('for (const part of ["authoring-part1.json", "authoring-part2.json"]) {',
    'for (const part of ["authoring-part1.json", "authoring-part2.json"]) {')  # anchor
rep('gate("A0 tranche == wave-6 register of record (12 notes)", TRANCHE.length === 12, TRANCHE.join(","));',
    'gate("A0 tranche == wave-7 register of record (9 notes)", TRANCHE.length === 9, TRANCHE.join(","));')
rep('gate("A0 tranche set matches the wave-6 authoring register (wave-6/ dir order of record)", JSON.stringify(TRANCHE) === JSON.stringify([...REGISTER_W6].sort()));',
    'gate("A0 tranche set matches the wave-7 authoring register (wave-7/ dir order of record)", JSON.stringify(TRANCHE) === JSON.stringify([...REGISTER_W7].sort()));')
rep('gate("A0 tranche disjoint from the 59 prior-R3 notes", TRANCHE.every((n) => !PRIOR_R3.includes(n)));',
    'gate("A0 tranche disjoint from the 71 prior-R3 notes", TRANCHE.every((n) => !PRIOR_R3.includes(n)));')
rep('gate(`A0 inventory totals (lessons ${lessonTotal}, items ${itemTotal})`, lessonTotal === 24 && itemTotal === 96, `${lessonTotal}/${itemTotal}`);',
    'gate(`A0 inventory totals (lessons ${lessonTotal}, items ${itemTotal})`, lessonTotal === 19 && itemTotal === 76, `${lessonTotal}/${itemTotal}`);')
rep('section("build source-0.5 ×12");', 'section("build source-0.5 ×9");')

# ── C-2 baseline v12 -> v13 ──────────────────────────────────────────────────
rep('section("C-2 preflight vs manifest v11");', 'section("C-2 preflight vs manifest v13");')
rep('const man12 = readJson(path.join(RES, "hub-import-manifest-v12.json"));',
    'const man12 = readJson(path.join(RES, "hub-import-manifest-v13.json"));')
rep('const int3b5 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb5.json"));',
    'const int3b5 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb6.json"));')
rep('gate("C-2 manifest v12 shape", man12.manifest_version === 12 && man12.artifacts.length === 224);',
    'gate("C-2 manifest v13 shape", man12.manifest_version === 13 && man12.artifacts.length === 224);')
rep('gate("C-2 224 local bytes == manifest v11 shas (checkout == pinned generations)", shaOk === 112, `${shaOk}/112 notes (224 artifacts)`);',
    'gate("C-2 224 local bytes == manifest v13 shas (checkout == pinned generations)", shaOk === 112, `${shaOk}/112 notes (224 artifacts)`);')
rep('section("transform (declared deltas on the 1.3 / 1.0 bytes)");',
    'section("transform (declared deltas on the 1.3 / 1.0 bytes)");')  # anchor

# ── untouched bucket 41 -> 32 ────────────────────────────────────────────────
rep('gate("C-6 41 untouched lessons+packages vs union schemas", untouchedOk === 41, `${untouchedOk}/41`);',
    'gate("C-6 32 untouched lessons+packages vs union schemas", untouchedOk === 32, `${untouchedOk}/32`);')
rep('gate("C-9 41 package shas == manifest v12 (byte conservation)", pkgShaOk === 41, `${pkgShaOk}/41`);',
    'gate("C-9 32 package shas == manifest v13 (byte conservation)", pkgShaOk === 32, `${pkgShaOk}/32`);')

# ── G-E ──────────────────────────────────────────────────────────────────────
rep('row.r3_delta = { written_items: 4 * src5[n].lessons.length, mcq_unchanged: true, wave: "S-B6" };',
    'row.r3_delta = { written_items: 4 * src5[n].lessons.length, mcq_unchanged: true, wave: "S-B7" };')
rep('gate("G-E 41 non-R3 stream anchors == S-B5 (v12) generation exactly (figures-2.2 + stage-A + S-B1 + S-B2 + S-B3 + S-B4 + S-B5)", nonTrancheStreamOk === 41, `${nonTrancheStreamOk}/41`);',
    'gate("G-E 32 non-R3 stream anchors == S-B6 (v13) generation exactly (figures-2.2 + stage-A + S-B1 + S-B2 + S-B3 + S-B4 + S-B5 + S-B6)", nonTrancheStreamOk === 32, `${nonTrancheStreamOk}/32`);')
rep('gate("G-E 59 prior-R3 streams == their anchors exactly (bytes unchanged)", priorStreamOk === 59, `${priorStreamOk}/59`);',
    'gate("G-E 71 prior-R3 streams == their anchors exactly (bytes unchanged)", priorStreamOk === 71, `${priorStreamOk}/71`);')
rep('gate("G-E 12 S-B6 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 12);',
    'gate("G-E 9 S-B7 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 9);')
rep('gate("G-E the 12 re-anchored rows carry authoring wave 6 of record", rows.filter((r) => TRANCHE.includes(r.noteId)).every((r) => r.wave === 6));',
    'gate("G-E the 9 re-anchored rows carry authoring wave 7 of record", rows.filter((r) => TRANCHE.includes(r.noteId)).every((r) => r.wave === 7));')

# ── cross-checks vs v13 ──────────────────────────────────────────────────────
rep('gate("cross-check: manifest v12 grand == v12 record", man12.conservation.authored_stream_sha256 === int3b5.grand_stream.sha256);',
    'gate("cross-check: manifest v13 grand == v13 record", man12.conservation.authored_stream_sha256 === int3b5.grand_stream.sha256);')
rep('gate("cross-check: wave subtotals preserved for the 9 untouched waves (1,2,3,4,5,7,8,9,10)", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-7","wave-8","wave-9","wave-10"].every((w) => waveOut[w] === man12.conservation.wave_stream_sha256[w]));',
    'gate("cross-check: wave subtotals preserved for the 9 untouched waves (1,2,3,4,5,6,8,9,10)", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-6","wave-8","wave-9","wave-10"].every((w) => waveOut[w] === man12.conservation.wave_stream_sha256[w]));')
rep('gate("cross-check: wave-6 re-anchored", waveOut["wave-6"] !== man12.conservation.wave_stream_sha256["wave-6"]);',
    'gate("cross-check: wave-7 re-anchored", waveOut["wave-7"] !== man12.conservation.wave_stream_sha256["wave-7"]);')

# ── manifest v14 ─────────────────────────────────────────────────────────────
rep('section("manifest v13");', 'section("manifest v14");')
rep('  checks: 1787,', '  checks: 1863,')
rep('  checks_written: 592,\n  checks_mcq: 1195,\n  written_recall: 296,\n  written_explain_why: 148,\n  written_application: 148,',
    '  checks_written: 668,\n  checks_mcq: 1195,\n  written_recall: 334,\n  written_explain_why: 167,\n  written_application: 167,')
rep('gate("manifest v13 lists 224", artifacts.length === 224);', 'gate("manifest v14 lists 224", artifacts.length === 224);')
rep('gate("manifest v13: exactly 24 re-issued vs v12", artifacts.filter((a) => !man12.artifacts.some((b) => b.path === a.path)).length === 24);',
    'gate("manifest v14: exactly 18 re-issued vs v13", artifacts.filter((a) => !man12.artifacts.some((b) => b.path === a.path)).length === 18);')
rep('  manifest_version: 13,', '  manifest_version: 14,')
rep('  supersedes: "hub-import-manifest-v12.json (41 hub-lesson-import-1.3 lessons + 41 sme-question-package/1.0 packages + the 118 already-live R3 re-issues byte-identical re-pins; exactly 24 re-issued artifacts: 12 hub-lesson-import-1.4 lessons (checkRefs delta) + 12 sme-question-package/1.1 packages (+96 written items) — the R3 stage-B wave 6 tranche: the wave-6 authoring register)",',
    '  supersedes: "hub-import-manifest-v13.json (32 hub-lesson-import-1.3 lessons + 32 sme-question-package/1.0 packages + the 142 already-live R3 re-issues byte-identical re-pins; exactly 18 re-issued artifacts: 9 hub-lesson-import-1.4 lessons (checkRefs delta) + 9 sme-question-package/1.1 packages (+76 written items) — the R3 stage-B wave 7 tranche: the wave-7 authoring register)",')
rep('wave: `R3-MIXED-CHECK-TYPES stage B wave 6 (S-B6) — operator ignition trace ${OPERATOR_TRACE} ("wave 6") on the stage-B contract of record (S-B1 NEXT: "waves 3..10 to the ~956 total"; S-B5 promotion receipt merge_order: "stage B wave 6 (next register tranche) remains operator-gated")`,',
    'wave: `R3-MIXED-CHECK-TYPES stage B wave 7 (S-B7) — operator ignition trace ${OPERATOR_TRACE} ("wave 7") on the stage-B contract of record (S-B1 NEXT: "waves 3..10 to the ~956 total"; S-B6 promotion receipt merge_order: "stage B wave 7 (next register tranche) remains operator-gated")`,')
rep('derivation: "96 authored written items (48 recall, 24 explain-why, 24 application), each spec-anchored to its lesson\'s keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 24 wave-6 lessons in the SME kind order [recall, recall, explain-why, application]",',
    'derivation: "76 authored written items (38 recall, 19 explain-why, 19 application), each spec-anchored to its lesson\'s keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 19 wave-7 lessons in the SME kind order [recall, recall, explain-why, application]",')
rep('cumulative R3 generation = 71 notes / 148 lessons / 592 written items",',
    'cumulative R3 generation = 80 notes / 167 lessons / 668 written items",')
rep('const int3b6 = {\n  stage: "INT-3",\n  title: "transform record — R3 mixed check types STAGE B WAVE 6 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",',
    'const int3b6 = {\n  stage: "INT-3",\n  title: "transform record — R3 mixed check types STAGE B WAVE 7 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",')
rep('prior_record: "records/INT-3-transform-record-r3-stageb5.json (stage-B wave 5 — superseded by this record for the 71-note R3 generation; anchors for the 41 non-R3 notes carried unchanged)",',
    'prior_record: "records/INT-3-transform-record-r3-stageb6.json (stage-B wave 6 — superseded by this record for the 80-note R3 generation; anchors for the 32 non-R3 notes carried unchanged)",')
rep('note: "resources main at S-B6 open (contains the S-B5 merge 0e663252 of record; main advanced past it with the unrelated lanes before this wave opened — disclosed)",',
    'note: "resources main at S-B7 open (contains the S-B6 merge-of-record 6b70de74; main advanced past it with the unrelated lanes before this wave opened — disclosed)",')
rep('note: "71 files: 2 stage-A pilots (80afdb8e) + 10 S-B1 notes (78ad6a20) + 12 S-B2 notes (96c261a…, PR #237) + 12 S-B3 notes (da18433…, PR #240) + 11 S-B4 notes (fa1f302…, PR #242) + 12 S-B5 notes (6fb25fc…, PR #243) + 12 S-B6 notes (this generation commit)" },',
    'note: "80 files: 2 stage-A pilots (80afdb8e) + 10 S-B1 notes (78ad6a20) + 12 S-B2 notes (96c261a…, PR #237) + 12 S-B3 notes (da18433…, PR #240) + 11 S-B4 notes (fa1f302…, PR #242) + 12 S-B5 notes (6fb25fc…, PR #243) + 12 S-B6 notes (286b5ac…, PR #245/#246) + 9 S-B7 notes (this generation commit)" },')
rep('"kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 41 non-R3 per-note streams equal the S-B5 (v12) anchors exactly; the 59 prior-R3 streams equal their own anchors exactly (bytes unchanged); the 12 S-B6 notes add the 96 written items\' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",',
    '"kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 32 non-R3 per-note streams equal the S-B6 (v13) anchors exactly; the 71 prior-R3 streams equal their own anchors exactly (bytes unchanged); the 9 S-B7 notes add the 76 written items\' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",')
rep('    sb5_notes: SB5_NOTES,\n    sb6_notes: TRANCHE,\n    cumulative_r3_notes: 71,\n    cumulative_r3_lessons: 148,\n    cumulative_written_items: 592,\n    kinds_cumulative: { recall: 296, "explain-why": 148, application: 148 },\n    sb6_wave: { notes: 12, lessons: 24, written_items: 96, kinds: { recall: 48, "explain-why": 24, application: 24 } },\n    mcqs_conserved: 1195,\n    packages_untouched: 41,\n    lessons_untouched: 41,',
    '    sb5_notes: SB5_NOTES,\n    sb6_notes: SB6_NOTES,\n    sb7_notes: TRANCHE,\n    cumulative_r3_notes: 80,\n    cumulative_r3_lessons: 167,\n    cumulative_written_items: 668,\n    kinds_cumulative: { recall: 334, "explain-why": 167, application: 167 },\n    sb7_wave: { notes: 9, lessons: 19, written_items: 76, kinds: { recall: 38, "explain-why": 19, application: 19 } },\n    mcqs_conserved: 1195,\n    packages_untouched: 32,\n    lessons_untouched: 32,')
rep('  sb6_authoring_register: {\n    basis: "stage-B plan of record: \'tranche order mirrors the authoring register\' — S-B6 = the wave-6 register notes (12 notes / 24 lessons / 120 checks per source-0.4; wave-field proven: all 12 rows carry wave==6 in the INT-3 record)",',
    '  sb7_authoring_register: {\n    basis: "stage-B plan of record: \'tranche order mirrors the authoring register\' + the S-B6 NEXT (\'per the wave-7/ bucket: 19 guided-lesson files in the authoring dir — final tranche size to be read from the register at wave open\') — S-B7 = the wave-7 register notes (9 notes / 19 lessons / 95 checks per source-0.4; wave-field proven: all 9 rows carry wave==7 in the INT-3 record)",')
rep('anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson\'s keyPoints by KP index; stems verified non-duplicative against ALL 1,195 of-record MCQ stems + 496 of-record written stems + intra-tranche x96 (token-Jaccard >= 0.6: 1 collision caught at authoring and re-pointed to a distinct form — 0 flags on the final pass); the wave\'s self-grading audit (model answer grades correct under its own keyword law): 96/96 pass pre-commit; numeric-claim clusters recomputed in code (the brass 70+30=100 and stainless 20+10=30 compositions, the steel ordering 0.25<0.5<=1.4 with range width 0.9, the burette concordance chain 15.00-14.90=0.10<=0.1 with mean 14.95 and the 0.05x2=0.1 precision span, the pH scale midpoint (0+14)/2=7 with band placements 12 in [11,14] and 4 in [4,6] plus 13>7 and 5<7 and 1<5, the H+ + OH- -> H2O atom census, the 2-electron Mg/Cu and Fe/Cu half-equation censuses with charge balance, the 3-electron Al3+ cathode census, the C+O2->CO2 anode-wear census, the Cu(NO3)2 and Ca(OH)2 charge balances, the Zn+CuO oxygen-transfer census, the displacement chain M>N>X, the 1+1 ion censuses for HCl/NaOH ionisation)",',
    'anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson\'s keyPoints by KP index; stems verified non-duplicative against ALL 1,195 of-record MCQ stems + 592 of-record written stems + intra-tranche x76 (token-Jaccard >= 0.6: 0 flags on the final pass — 6 keyword-hygiene re-points and 1 chlorine-MCQ stem re-point applied at authoring); the wave\'s self-grading audit (model answer grades correct under its own keyword law): 76/76 pass pre-commit; zero-keyword miss probe scores 0 hits on all 76 items; numeric-claim clusters recomputed in code (the burette difference identity final-starting=added on a worked sample, the CuSO4.5H2O hydrate census 5 waters / 10 H atoms, the alkali pH band 11 > 7, the NH4+ + OH- -> NH3 + H2O atom-and-charge census, the impurity laws 102 > 100 boiling raised and -3 < 0 melting depressed, the 25 cm3 / 0.5 mol dm-3 measured volume pinned in the KP of record, the AgNO3 + NaCl -> AgCl + NaNO3 atom census, the Ca(OH)2 limewater census, the five-further-drops slight-excess count)",')

# ── INT-3 emit + manifest emit paths ─────────────────────────────────────────
rep('const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb6.json"), int3b6);\nconst man13Buf = emit(path.join(RES, "hub-import-manifest-v13.json"), man13);',
    'const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb7.json"), int3b6);\nconst man13Buf = emit(path.join(RES, "hub-import-manifest-v14.json"), man13);')

# ── promotion receipt ────────────────────────────────────────────────────────
rep('wave: "R3-MIXED-CHECK-TYPES (stage B wave 6 — the wave-6 authoring register, 12 notes / 24 lessons / 96 written items)",',
    'wave: "R3-MIXED-CHECK-TYPES (stage B wave 7 — the wave-7 authoring register, 9 notes / 19 lessons / 76 written items)",')
rep('operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, SB_GATE_TRACE, SB2_EXECUTE_TRACE, SB3_IGNITION_TRACE, SB4_IGNITION_TRACE, SB5_IGNITION_TRACE, OPERATOR_TRACE],',
    'operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, SB_GATE_TRACE, SB2_EXECUTE_TRACE, SB3_IGNITION_TRACE, SB4_IGNITION_TRACE, SB5_IGNITION_TRACE, SB6_IGNITION_TRACE, OPERATOR_TRACE],')
rep('branch: "integration/r3-stageb6-20261031",', 'branch: "integration/r3-stageb7-20261031",')
rep('contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups + the S-B1 NEXT of record (\'waves 3..10 to the ~956 total\') + the S-B5 promotion receipt merge_order (\'stage B wave 6 (next register tranche) remains operator-gated per the ledger convention\') — gate opened by operator trace 1a18dfb539a4c839 (\'wave 6\')",',
    'contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups + the S-B1 NEXT of record (\'waves 3..10 to the ~956 total\') + the S-B6 promotion receipt merge_order (\'stage B wave 7 (next register tranche) remains operator-gated per the ledger convention\') — gate opened by operator trace 1a18fd512d610f7d (\'wave 7\')",')
rep('note: "S-B6 is based on the current resources main (wave-open main of record resolved at run time, recorded in input_pins): the S-B5 generation (PR #243, merge 0e663252) is an ancestor of main, and main advanced past it with the unrelated lanes before this wave opened — disclosed, zero overlap with the stage-B namespaces. The S-B1 merge-order convention (resources PR merges first; the hub chain follows) holds for this wave.",\n    sb5_merge_commit: SB5_MERGE,',
    'note: "S-B7 is based on the current resources main (wave-open main of record resolved at run time, recorded in input_pins): the S-B6 generation (PR #245 + merge-of-record #246, merge 6b70de74) is an ancestor of main, and main advanced past it with the unrelated lanes before this wave opened — disclosed, zero overlap with the stage-B namespaces. The S-B1 merge-order convention (resources PR merges first; the hub chain follows) holds for this wave.",\n    sb6_merge_commit: SB6_MERGE,')
rep('A: { sha: commitA, parent: commitAParent, note: "S-B6 source-0.5 generation — 12 authored guided-lesson/0.5 notes (96 written items) added to the namespace (71 files total)" },',
    'A: { sha: commitA, parent: commitAParent, note: "S-B7 source-0.5 generation — 9 authored guided-lesson/0.5 notes (76 written items) added to the namespace (80 files total)" },')
rep('C: { sha: "(namespace-complete — outputs + manifest v13 + records + pipeline)", note: "hub-import-1.4/ ×12 + question-packages-1.1/ ×12 + hub-import-manifest-v13.json + records/INT-3-transform-record-r3-stageb6.json + records/R3-CHECK-TYPES-STAGEB6-PROMOTION-20261031.json + tooling/r3-stageb6-pipeline.js + tooling/r3-stageb6-authoring/ — schema delta NONE (the S-B1 union caps already admit this tranche)" },',
    'C: { sha: "(namespace-complete — outputs + manifest v14 + records + pipeline)", note: "hub-import-1.4/ ×9 + question-packages-1.1/ ×9 + hub-import-manifest-v14.json + records/INT-3-transform-record-r3-stageb7.json + records/R3-CHECK-TYPES-STAGEB7-PROMOTION-20261031.json + tooling/r3-stageb7-pipeline.js + tooling/r3-stageb7-authoring/ — schema delta NONE (the S-B1 union caps already admit this tranche)" },')
rep('artifact_pin: `${SOURCE_PIN_V6} (41 untouched lessons) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${SB1_COMMIT_A} (10 S-B1 notes) | ${SB2_A_FULL} (12 S-B2 notes) | ${SB3_COMMIT_A} (12 S-B3 notes) | ${SB4_COMMIT_A} (11 S-B4 notes) | ${SB5_COMMIT_A} (12 S-B5 notes) | ${commitA} (12 new source-0.5 lessons — commit A of this wave)`,',
    'artifact_pin: `${SOURCE_PIN_V6} (32 untouched lessons) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${SB1_COMMIT_A} (10 S-B1 notes) | ${SB2_A_FULL} (12 S-B2 notes) | ${SB3_COMMIT_A} (12 S-B3 notes) | ${SB4_COMMIT_A} (11 S-B4 notes) | ${SB5_COMMIT_A} (12 S-B5 notes) | ${SB6_COMMIT_A} (12 S-B6 notes) | ${commitA} (9 new source-0.5 lessons — commit A of this wave)`,')
rep('pkg_pin: `(41 untouched keep INT-0 4d857c47…; 2 pilots keep ${STAGE_A_COMMIT.slice(0, 8)}; 10 S-B1 keep 78ad6a20; 12 S-B2 keep ${SB2_A_FULL.slice(0, 8)}; 12 S-B3 keep ${SB3_COMMIT_A.slice(0, 8)}; 11 S-B4 keep ${SB4_COMMIT_A.slice(0, 8)}; 12 S-B5 keep ${SB5_COMMIT_A.slice(0, 8)}; ${commitA} for the 12 new — the SEVENTH package-channel re-pin since INT-0)`,',
    'pkg_pin: `(32 untouched keep INT-0 4d857c47…; 2 pilots keep ${STAGE_A_COMMIT.slice(0, 8)}; 10 S-B1 keep 78ad6a20; 12 S-B2 keep ${SB2_A_FULL.slice(0, 8)}; 12 S-B3 keep ${SB3_COMMIT_A.slice(0, 8)}; 11 S-B4 keep ${SB4_COMMIT_A.slice(0, 8)}; 12 S-B5 keep ${SB5_COMMIT_A.slice(0, 8)}; 12 S-B6 keep ${SB6_COMMIT_A.slice(0, 8)}; ${commitA} for the 9 new — the EIGHTH package-channel re-pin since INT-0)`,')
rep('manifest: "hub-import-manifest-v12.json",\n  int_record: "INT-3-transform-record-r3-stageb5.json",\n  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb6-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb6-authoring/authoring-part2.json", "(lane mirrors: scripts/r3-stageb6/authoring-part{1,2}.json; audit: scripts/r3-stageb6/audit_authoring.py)"],',
    'manifest: "hub-import-manifest-v13.json",\n  int_record: "INT-3-transform-record-r3-stageb6.json",\n  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb7-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb7-authoring/authoring-part2.json", "(lane mirrors: scripts/r3-stageb7/authoring-part{1,2}.json; audit: scripts/r3-stageb7/audit_authoring.py)"],')
rep('counts_census: { notes: 112, lessons: 239, checks: 1787, checks_mcq: 1195, checks_written: 592, written_recall: 296, written_explain_why: 148, written_application: 148, sb6_notes: TRANCHE, sb6_written: 96, distractors: 3565 },',
    'counts_census: { notes: 112, lessons: 239, checks: 1863, checks_mcq: 1195, checks_written: 668, written_recall: 334, written_explain_why: 167, written_application: 167, sb7_notes: TRANCHE, sb7_written: 76, distractors: 3565 },')
rep('S-B6 is a pure data wave under unchanged schemas (ajv re-proof ×224 artifacts + ×12 sources in this run).",',
    'S-B7 is a pure data wave under unchanged schemas (ajv re-proof ×224 artifacts + ×9 sources in this run).",')
rep('law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 41 non-R3 streams == S-B5 (v12) anchors exactly; 59 prior-R3 streams == their own anchors exactly",',
    'law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 32 non-R3 streams == S-B6 (v13) anchors exactly; 71 prior-R3 streams == their own anchors exactly",')
rep('mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×12 (+96 count); 41 package shas byte-identical ×41; 59 prior-R3 packages byte-identical ×59",',
    'mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×9 (+76 count); 32 package shas byte-identical ×32; 71 prior-R3 packages byte-identical ×71",')
rep('"resources PR (this branch; a clean descendant of main at wave open) merges to main FIRST; the hub PR (runner FEED r3-stageb6-v13 + re-issued artifacts + re-issued guided-import.json) merges only after; stage B wave 7 (next register tranche) remains operator-gated",',
    '"resources PR (this branch; a clean descendant of main at wave open) merges to main FIRST; the hub PR (runner FEED r3-stageb7-v14 + re-issued artifacts + re-issued guided-import.json) merges only after; stage B wave 8 (next register tranche) remains operator-gated",')
rep('recalibration_note:\n    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (9 untouched waves byte-equal to v12 — declared preserved, including wave-9/10 whose buckets carry the already-live stage-A pilots byte-unchanged; wave-6 re-anchored by its 12 S-B6 notes)",',
    'recalibration_note:\n    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (9 untouched waves byte-equal to v13 — declared preserved, including wave-9/10 whose buckets carry the already-live stage-A pilots byte-unchanged; wave-7 re-anchored by its 9 S-B7 notes)",')
rep('emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB6-PROMOTION-20261031.json"), receipt);',
    'emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB7-PROMOTION-20261031.json"), receipt);')
rep('fs.copyFileSync(path.join(RES, "hub-import-manifest-v13.json"), path.join(SURV, "hub-import-manifest-v13.json"));\nfs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb6.json"), path.join(SURV, "INT-3-transform-record-r3-stageb6.json"));',
    'fs.copyFileSync(path.join(RES, "hub-import-manifest-v14.json"), path.join(SURV, "hub-import-manifest-v14.json"));\nfs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb7.json"), path.join(SURV, "INT-3-transform-record-r3-stageb7.json"));')
rep('console.log(`  census: checks 1691 → 1787 (written 496 → 592; MCQ 1,195 conserved)`);',
    'console.log(`  census: checks 1787 → 1863 (written 592 → 668: recall 334 / explain-why 167 / application 167; MCQ 1,195 conserved)`);')

open(DST, "w").write(txt)
print(f"OK — wrote {DST} ({len(txt)} bytes); all occurrence-checked replacements passed")
