#!/usr/bin/env python3
"""Generate tooling/r3-stageb8-pipeline.js from the S-B7 pipeline of record.

Every replacement is asserted to occur EXACTLY once (or an exact stated count)
in the S-B7 source, so any drift fails loudly instead of silently mis-emitting.
"""
import re
import sys

SRC = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/tooling/r3-stageb7-pipeline.js"
DST = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/tooling/r3-stageb8-pipeline.js"

src = open(SRC, encoding="utf-8").read()

NEW_HEADER = """/**
 * R3-CHECK-TYPES PIPELINE — STAGE B WAVE 8 (S-B8)
 * (operator ignition: "STAGE-B WAVE 8", hub chat trace 1a1900aa14eb84d5, continuing the
 *  stage-B contract of record in R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json, the S-B1 NEXT
 *  ("waves 3..10 to the ~956 total") and the S-B7 promotion receipt merge_order ("stage B wave 8
 *  (next register tranche) remains operator-gated") — gate opened by the operator word above)
 *
 * S-B8 tranche of record: the wave-8 authoring register (14 notes, 32 lessons, 160 MCQs)
 * -> +128 authored written items (64 recall, 32 explain-why, 32 application). FINAL tranche
 * shape read from the register at wave open per the S-B7 NEXT pointer.
 * Schema delta: NONE — the S-B1 union caps (maxItems 45 / check 9 / checkRefs 9) admit this tranche.
 *
 * Stack of record: branch integration/r3-stageb8-20261031 based on the current resources main
 * (wave-open main of record resolved at run time, recorded in input_pins; contains the S-B7
 * merge-of-record 652ca2d4 as ancestor — main advanced past it with the unrelated T-BOOK-SERVE
 * books lanes, disclosed).
 *
 * Inputs (clone /home/z/my-project/syllabai-resources @ integration/r3-stageb8-20261031):
 *   scripts/r3-stageb8/authoring-part{1,2}.json     the 128 authored items (KP-anchored; audit GREEN)
 *   integration/source-0.4/        0.4 generation (D-1 baseline)
 *   integration/source-0.5/        the 80 prior R3 sources (byte-identical re-proof)
 *   integration/hub-import-1.3/    1.3 lesson outputs (D-2 baseline for the tranche)
 *   integration/question-packages/ 1.0 packages (C-9: 18 byte-identical)
 *   integration/hub-import-1.4/ + question-packages-1.1/  the 80 prior-R3 outputs (re-proof)
 *   integration/hub-import-manifest-v14.json + records/INT-3-transform-record-r3-stageb7.json
 *
 * Outputs (namespace-complete):
 *   source-0.5/ x14 (new)          hub-import-1.4/ x14 (new)   question-packages-1.1/ x14 (new)
 *   hub-import-manifest-v15.json   records/INT-3-transform-record-r3-stageb8.json
 *   records/R3-CHECK-TYPES-STAGEB8-PROMOTION-20261031.json
 * + survivors for the hub runner byte-anchors (scripts/r3-survivors/)
 *
 * Gates: A0 authoring inventory, P0 committed==rebuilt x14, D-1 source determinism x14,
 * C-6 ajv (14 sources + 28 tranche outputs + 80 prior-R3 re-proofs + 18 untouched pairs),
 * C-2 preflight vs manifest v14 (224 shas), written-kind invariants x128, MCQ deep conservation x14,
 * C-5 checkRefs closure x14 + x80 prior-R3, D-2 output determinism x14, C-9 package sha
 * conservation x18, G-E stream recompute x112 (18 == v14 anchors; 80 prior-R3 == their anchors
 * exactly; 14 S-B8 rows re-anchored), grand + waves x10 (9 byte-equal vs v14; wave-8 re-anchored).
 * FAIL-CLOSED: any gate failure aborts before any record is emitted.
 */"""

NEW_CONSTANTS = """const PILOTS = ["rn_2MpXPtNXvn8pQm3r", "rn_8T5GfPn2q7sY2YCh"]; // stage A, already live
const SB1_NOTES = ["rn_2d6Yb8GwGfRRd6pZ","rn_4SgDJv8rKxpQQSBh","rn_HZM2WRjPPT8Srcxt","rn_JCfdFrHsCkrmMbFj","rn_TM4QVMgXVxs4vbfY","rn_fQSYvKRMDBj3s2Bx","rn_jNJ4gTmcHqdFqsNh","rn_kJg2gwF77vdFZZ2H","rn_wTtM2fQVVjntRm64","rn_xT8XsdJtDX5gNFXj"]; // S-B1, live @ 78ad6a20
const SB2_NOTES = ["rn_2VnK66PqbvFKdKYt","rn_S7GPh8BBPBbmhYKm","rn_cTk2cs2h2BKQ3y3B","rn_QVmDs8X4szpds3cP","rn_TWGVV6RXN3Ktqb9h","rn_RvgxXR36425BFMcx","rn_YBWYstSRgM2QPzQq","rn_R3ptwxGTTvdBFvyP","rn_TsfqyK9BYMtN2Bfd","rn_kb2VkFMdBTbmG33t","rn_vzGMZxqQtWYVWB7h","rn_b3XCzdtfQddbJjVf"]; // S-B2, live @ 96c261a (PR #237 merged e679c919)
const SB3_NOTES = ["rn_Syxyh4Fct8KFg8NQ","rn_mBqgkpZ3hbSBmWCC","rn_N4HX8tqbdhTQcHyS","rn_VyXFNyxZHZGkxqTG","rn_vXPcH3vS8wv7BFkK","rn_pWzTTBv3B4yGFfj3","rn_yj4y972FxCWnDnSg","rn_Hkwmd9GSp3gdxxR5","rn_4tzwS4GZjPybwtkS","rn_T55t3HNsgyZcXZtN","rn_mbcBZkygY4YpG2bf","rn_8Nv33F4dD3kkZnY6"]; // S-B3, live @ da18433 (PR #240 merged 163cb2f)
const SB4_NOTES = ["rn_3YZNCXSQQqXTT6HR","rn_FCnWFz9MhgsqnZGM","rn_GkJG52NCN98ShGRm","rn_Hp2nK8XpN2SmjdQc","rn_J7ZcTWyRxRgWQ45R","rn_KpvF2TWr5fYHk2Jz","rn_MVnFKDMVkswzpmpw","rn_jVwPmjqHbqQkXcjG","rn_kdRjZHjHcpVZsD3h","rn_rHKCkt3PTXDBpmJG","rn_vfmJxw4VQgXKzXF3"]; // S-B4, live @ fa1f302 (PR #242 merged e76925db)
const SB5_NOTES = ["rn_3B8JxsSjJvR9B4fk","rn_5WvdZNzzhHdjj2Qq","rn_6M5JB7CjvwdDykMS","rn_7Q8M9nVkr2FxCzxd","rn_DGkNCJRcCN4VQ28p","rn_Kd76WccxD9ytSJJC","rn_QzYRzzmwRxk2gKqV","rn_S2fg29M7cqvMj5kT","rn_V9tPMnX6Hq2XnqcP","rn_WJD4ZN4kQfzJNSPV","rn_gBGX339WBpwyCrFF","rn_jXXsc4wt2344BjxX"]; // S-B5, live @ 6fb25fc (PR #243 merged 0e663252)
const SB6_NOTES = ["rn_9WM8QhSxmYpGhjqd","rn_BX88twwgffRMgx82","rn_MMkxbt9y3M3XvXrc","rn_ZWrmDYtNGnmFycPM","rn_by5FDNfkqdBCkmXb","rn_dTP52nzhYb96XrJx","rn_nzW5ppBTV3ZnfSYY","rn_p2FmkrXqZSzFngpg","rn_qV5R2cKB59bSKD33","rn_sX8yyBxHn8bS7t46","rn_sf7s7s6bQ2cZv29s","rn_xq9jy75y43kDXkvx"]; // S-B6, live @ 286b5ac (PR #245/#246 merged 6b70de7)
const SB7_NOTES = ["rn_5g8Dd6y89tkCVJsN","rn_6ZCysv9GnNQmc3w2","rn_T6S7R66N2wSZpWyc","rn_VvsXMdW3TB37JhWF","rn_YWDXCCmjfjkJcs6c","rn_pBp5Z5C2RHTKk7Wn","rn_qb9TBhB6VmnFGjvf","rn_v5JjfpT6grhtq3QW","rn_vVdP57QhDYSVfZgy"]; // S-B7, live @ a8889009 (PR #248 merged 652ca2d4)
const PRIOR_R3 = [...PILOTS, ...SB1_NOTES, ...SB2_NOTES, ...SB3_NOTES, ...SB4_NOTES, ...SB5_NOTES, ...SB6_NOTES, ...SB7_NOTES]; // the 80 notes already carrying written items (byte-identical this wave)
const REGISTER_W8 = ["rn_3wZh9qRT7qFJn9QW","rn_6478QfpYNQDjZSvt","rn_DRQXrcSrmgQ7jcbZ","rn_H6ZVkxvdNgYDvfFb","rn_HNXFQt7vM32g6PMv","rn_KTZjJ7sPdDt4tkTH","rn_XJ8qXfzZJJFKXHnF","rn_Zh6Pw56rjdMkPCD4","rn_dgVRCKCwn4rTGxGZ","rn_t68QRDhwR6r5gxYX","rn_tvwj4VZ6yFscPJfD","rn_w25KHshCMNQWwftj","rn_x5m8QBWxtKvxQ9sx","rn_y85XYRv5QfgZFQxv"]; // wave-8 authoring register order of record (dir listing at wave open)
const STAGE_A_COMMIT = "80afdb8e02b628754f0e522d257e54d046ba5b0f";
const SB1_COMMIT_A = "78ad6a2073c669231bb40bd7266674a257c6003e";
const SB2_COMMIT_A = "96c261a"; // resolved below
const SB3_COMMIT_A = "da18433ed9e8351a2e8ce1282b8eaf5c362442d4";
const SB4_COMMIT_A = "fa1f302050ba38b6b2e97760e88d32567d2b0c90";
const SB5_COMMIT_A = "6fb25fc02d1a7acc71ee2231b547ac85e00705c1";
const SB6_COMMIT_A = "286b5ac81d43a28e5faa9f9e8ab16b67fbb12c51";
const SB7_COMMIT_A = "a8889009338bc5ce09edfed1d610d8cc9c9457b4";
const SOURCE_PIN_V6 = "71922d1510ee9e00400667670b40f36e1ae5d456"; // source-0.4 (the 18 untouched lessons)
const OPERATOR_TRACE = "1a1900aa14eb84d5"; // "STAGE-B WAVE 8"
const SB5_IGNITION_TRACE = "1a18d9f731726de1"; // "stage-B wave 5"
const SB6_IGNITION_TRACE = "1a18dfb539a4c839"; // "wave 6"
const SB7_IGNITION_TRACE = "1a18fd512d610f7d"; // "wave 7"
const STAGE_A_TRACE = "1a18a0218b7f44fd";
const QUEUE_TRACE = "1a189fd011119961";
const SB_GATE_TRACE = "1a18bc1ca2cf48e5"; // "stage B proceed"
const SB2_EXECUTE_TRACE = "1a18c3fc617d21b9"; // "wave 2 proceed"
const SB3_IGNITION_TRACE = "1a18c9f53d7b8dd1"; // "wave 3 proceed"
const SB4_IGNITION_TRACE = "1a18d09c1263e991"; // "stage-B wave 4 proceed"
const ADAPTER = "guided-lesson-0.5--hub-lesson-import-1.4";
const SB5_MERGE = "0e66325219293c23243c5721dc68199b47a6e71b"; // the S-B5 merge of record (PR #243)
const SB6_MERGE = "6b70de744337f41a1cbb9a8ad5ee8e501cd184dc"; // the S-B6 merge-of-record (PR #246, re-merged identical content with the trace-bearing message)
const SB7_MERGE = "652ca2d4e7709647cfd68040a56d817ae985fc5e"; // the S-B7 merge-of-record (PR #248)
const WAVE_OPEN_MAIN = "7819d8a4aed0aefd53a9709f737d73159868432c"; // resources main at S-B8 open"""

REPS = [
    # header + constants blocks
    ("REGEX_HEADER", None),
    (
        'const AUTH = "/home/z/my-project/scripts/r3-stageb7";',
        'const AUTH = "/home/z/my-project/scripts/r3-stageb8";',
    ),
    # P0 ancestry gate
    (
        'const sb5IsAncestor = (() => { try { execSync(`git merge-base --is-ancestor ${SB6_MERGE} ${RES_MAIN_OPEN_RESOLVED}`, { cwd: RESROOT }); return true; } catch { return false; } })();',
        'const sb5IsAncestor = (() => { try { execSync(`git merge-base --is-ancestor ${SB7_MERGE} ${RES_MAIN_OPEN_RESOLVED}`, { cwd: RESROOT }); return true; } catch { return false; } })();',
    ),
    (
        'gate("P0 wave-open main contains the S-B6 merge of record (main advanced past it with unrelated lanes — disclosed)", sb5IsAncestor, RES_MAIN_OPEN_RESOLVED);',
        'gate("P0 wave-open main contains the S-B7 merge of record (main advanced past it with the unrelated T-BOOK-SERVE books lanes — disclosed)", sb5IsAncestor, RES_MAIN_OPEN_RESOLVED);',
    ),
    (
        'gate("P0 worktree branch == integration/r3-stageb7-20261031", BRANCH_RESOLVED === "integration/r3-stageb7-20261031", BRANCH_RESOLVED);',
        'gate("P0 worktree branch == integration/r3-stageb8-20261031", BRANCH_RESOLVED === "integration/r3-stageb8-20261031", BRANCH_RESOLVED);',
    ),
    ("commit A (S-B7 source-0.5 generation)", "commit A (S-B8 source-0.5 generation)"),
    ("process.env.SB7_EMIT_ONLY", "process.env.SB8_EMIT_ONLY"),  # x3 (asserted below)
    # A0 gates
    (
        'gate("A0 tranche == wave-7 register of record (9 notes)", TRANCHE.length === 9, TRANCHE.join(","));',
        'gate("A0 tranche == wave-8 register of record (14 notes)", TRANCHE.length === 14, TRANCHE.join(","));',
    ),
    (
        'gate("A0 tranche set matches the wave-7 authoring register (wave-7/ dir order of record)", JSON.stringify(TRANCHE) === JSON.stringify([...REGISTER_W7].sort()));',
        'gate("A0 tranche set matches the wave-8 authoring register (wave-8/ dir order of record)", JSON.stringify(TRANCHE) === JSON.stringify([...REGISTER_W8].sort()));',
    ),
    (
        'gate("A0 tranche disjoint from the 71 prior-R3 notes", TRANCHE.every((n) => !PRIOR_R3.includes(n)));',
        'gate("A0 tranche disjoint from the 80 prior-R3 notes", TRANCHE.every((n) => !PRIOR_R3.includes(n)));',
    ),
    ("lessonTotal === 19 && itemTotal === 76", "lessonTotal === 32 && itemTotal === 128"),
    ('section("build source-0.5 ×9")', 'section("build source-0.5 ×14")'),
    ('console.log("EMIT-ONLY: 9 source-0.5 files written — commit A, then re-run without SB7_EMIT_ONLY")',
     'console.log("EMIT-ONLY: 14 source-0.5 files written — commit A, then re-run without SB8_EMIT_ONLY")'),
    ("// ── D-1 source determinism ×12 ─", "// ── D-1 source determinism ×14 ─"),
    ("// ── C-2 preflight: manifest v11 upstream fidelity (112+112 local bytes) ───────",
     "// ── C-2 preflight: manifest v14 upstream fidelity (224 local bytes) ───────────"),
    ('section("C-2 preflight vs manifest v13")', 'section("C-2 preflight vs manifest v14")'),
    ('const man12 = readJson(path.join(RES, "hub-import-manifest-v13.json"));',
     'const man12 = readJson(path.join(RES, "hub-import-manifest-v14.json"));'),
    ('const int3b5 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb6.json"));',
     'const int3b5 = readJson(path.join(RES, "records/INT-3-transform-record-r3-stageb7.json"));'),
    ('gate("C-2 manifest v13 shape", man12.manifest_version === 13 && man12.artifacts.length === 224);',
     'gate("C-2 manifest v14 shape", man12.manifest_version === 14 && man12.artifacts.length === 224);'),
    ('gate("C-2 224 local bytes == manifest v13 shas (checkout == pinned generations)"',
     'gate("C-2 224 local bytes == manifest v14 shas (checkout == pinned generations)"'),
    ("// prior-R3 re-proof under the union schemas + C-5 (byte-identical to the S-B1/S-B2/S-B3/S-B4/S-B5 generations)",
     "// prior-R3 re-proof under the union schemas + C-5 (byte-identical to the S-B1..S-B7 generations)"),
    ("// 41 untouched: ajv under the UNION schemas + package sha conservation (C-9)",
     "// 18 untouched: ajv under the UNION schemas + package sha conservation (C-9)"),
    ('gate("C-6 32 untouched lessons+packages vs union schemas", untouchedOk === 32, `${untouchedOk}/32`);',
     'gate("C-6 18 untouched lessons+packages vs union schemas", untouchedOk === 18, `${untouchedOk}/18`);'),
    ('gate("C-9 32 package shas == manifest v13 (byte conservation)", pkgShaOk === 32, `${pkgShaOk}/32`);',
     'gate("C-9 18 package shas == manifest v14 (byte conservation)", pkgShaOk === 18, `${pkgShaOk}/18`);'),
    ('wave: "S-B7" };\n  } else if (PRIOR_R3.includes(n)) {', 'wave: "S-B8" };\n  } else if (PRIOR_R3.includes(n)) {'),
    ('gate("G-E 32 non-R3 stream anchors == S-B6 (v13) generation exactly (figures-2.2 + stage-A + S-B1 + S-B2 + S-B3 + S-B4 + S-B5 + S-B6)", nonTrancheStreamOk === 32, `${nonTrancheStreamOk}/32`);',
     'gate("G-E 18 non-R3 stream anchors == S-B7 (v14) generation exactly (figures-2.2 + stage-A + S-B1 + S-B2 + S-B3 + S-B4 + S-B5 + S-B6 + S-B7)", nonTrancheStreamOk === 18, `${nonTrancheStreamOk}/18`);'),
    ('gate("G-E 71 prior-R3 streams == their anchors exactly (bytes unchanged)", priorStreamOk === 71, `${priorStreamOk}/71`);',
     'gate("G-E 80 prior-R3 streams == their anchors exactly (bytes unchanged)", priorStreamOk === 80, `${priorStreamOk}/80`);'),
    ('gate("G-E 9 S-B7 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 9);',
     'gate("G-E 14 S-B8 rows re-anchored", rows.filter((r) => TRANCHE.includes(r.noteId)).length === 14);'),
    ('gate("G-E the 9 re-anchored rows carry authoring wave 7 of record", rows.filter((r) => TRANCHE.includes(r.noteId)).every((r) => r.wave === 7));',
     'gate("G-E the 14 re-anchored rows carry authoring wave 8 of record", rows.filter((r) => TRANCHE.includes(r.noteId)).every((r) => r.wave === 8));'),
    ('gate("cross-check: manifest v13 grand == v13 record"',
     'gate("cross-check: manifest v14 grand == v14 record"'),
    ('gate("cross-check: wave subtotals preserved for the 9 untouched waves (1,2,3,4,5,6,8,9,10)", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-6","wave-8","wave-9","wave-10"].every((w) => waveOut[w] === man12.conservation.wave_stream_sha256[w]));',
     'gate("cross-check: wave subtotals preserved for the 9 untouched waves (1,2,3,4,5,6,7,9,10)", ["wave-1","wave-2","wave-3","wave-4","wave-5","wave-6","wave-7","wave-9","wave-10"].every((w) => waveOut[w] === man12.conservation.wave_stream_sha256[w]));'),
    ('gate("cross-check: wave-7 re-anchored", waveOut["wave-7"] !== man12.conservation.wave_stream_sha256["wave-7"]);',
     'gate("cross-check: wave-8 re-anchored", waveOut["wave-8"] !== man12.conservation.wave_stream_sha256["wave-8"]);'),
    ('section("manifest v14")', 'section("manifest v15")'),
    # manifest counts
    ("  checks: 1863,", "  checks: 1991,"),
    ("  checks_written: 668,", "  checks_written: 796,"),
    ("  written_recall: 334,", "  written_recall: 398,"),
    ("  written_explain_why: 167,", "  written_explain_why: 199,"),
    ("  written_application: 167,", "  written_application: 199,"),
    ('gate("manifest v14 lists 224", artifacts.length === 224);',
     'gate("manifest v15 lists 224", artifacts.length === 224);'),
    ('gate("manifest v14: exactly 18 re-issued vs v13", artifacts.filter((a) => !man12.artifacts.some((b) => b.path === a.path)).length === 18);',
     'gate("manifest v15: exactly 28 re-issued vs v14", artifacts.filter((a) => !man12.artifacts.some((b) => b.path === a.path)).length === 28);'),
    # manifest texts
    ('  supersedes: "hub-import-manifest-v13.json (32 hub-lesson-import-1.3 lessons + 32 sme-question-package/1.0 packages + the 142 already-live R3 re-issues byte-identical re-pins; exactly 18 re-issued artifacts: 9 hub-lesson-import-1.4 lessons (checkRefs delta) + 9 sme-question-package/1.1 packages (+76 written items) — the R3 stage-B wave 7 tranche: the wave-7 authoring register)",',
     '  supersedes: "hub-import-manifest-v14.json (18 hub-lesson-import-1.3 lessons + 18 sme-question-package/1.0 packages + the 188 already-live R3 re-issues byte-identical re-pins; exactly 28 re-issued artifacts: 14 hub-lesson-import-1.4 lessons (checkRefs delta) + 14 sme-question-package/1.1 packages (+128 written items) — the R3 stage-B wave 8 tranche: the wave-8 authoring register)",'),
    ('    wave: `R3-MIXED-CHECK-TYPES stage B wave 7 (S-B7) — operator ignition trace ${OPERATOR_TRACE} ("wave 7") on the stage-B contract of record (S-B1 NEXT: "waves 3..10 to the ~956 total"; S-B6 promotion receipt merge_order: "stage B wave 7 (next register tranche) remains operator-gated")`,',
     '    wave: `R3-MIXED-CHECK-TYPES stage B wave 8 (S-B8) — operator ignition trace ${OPERATOR_TRACE} ("STAGE-B WAVE 8") on the stage-B contract of record (S-B1 NEXT: "waves 3..10 to the ~956 total"; S-B7 promotion receipt merge_order: "stage B wave 8 (next register tranche) remains operator-gated")`,'),
    ('    derivation: "76 authored written items (38 recall, 19 explain-why, 19 application), each spec-anchored to its lesson\'s keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 19 wave-7 lessons in the SME kind order [recall, recall, explain-why, application]",',
     '    derivation: "128 authored written items (64 recall, 32 explain-why, 32 application), each spec-anchored to its lesson\'s keyPoints (KP-index provenance in the authoring parts of record), carrying modelAnswer + generous synonym/inflection-bearing keywords; appended after the 5 MCQs of each of the 32 wave-8 lessons in the SME kind order [recall, recall, explain-why, application]",'),
    ('    declared_revision: "the SEVENTH package-channel delta since INT-0: 12 further packages re-issued under sme-question-package/1.1 (union schema — the 41 untouched 1.0 packages validate unchanged); 12 further lessons re-issued under hub/lesson-import/1.4 (checkRefs 5->9); kind/modelAnswer/keywords are §7-declared stream tokens on written items; cumulative R3 generation = 80 notes / 167 lessons / 668 written items",',
     '    declared_revision: "the EIGHTH package-channel delta since INT-0: 14 further packages re-issued under sme-question-package/1.1 (union schema — the 18 untouched 1.0 packages validate unchanged); 14 further lessons re-issued under hub/lesson-import/1.4 (checkRefs 5->9); kind/modelAnswer/keywords are §7-declared stream tokens on written items; cumulative R3 generation = 94 notes / 199 lessons / 796 written items",'),
    ("  manifest_version: 14,", "  manifest_version: 15,"),
    # INT-3 record
    ('  title: "transform record — R3 mixed check types STAGE B WAVE 7 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",',
     '  title: "transform record — R3 mixed check types STAGE B WAVE 8 generation (adapter guided-lesson-0.5--hub-lesson-import-1.4)",'),
    ('  prior_record: "records/INT-3-transform-record-r3-stageb6.json (stage-B wave 6 — superseded by this record for the 80-note R3 generation; anchors for the 32 non-R3 notes carried unchanged)",',
     '  prior_record: "records/INT-3-transform-record-r3-stageb7.json (stage-B wave 7 — superseded by this record for the 94-note R3 generation; anchors for the 18 non-R3 notes carried unchanged)",'),
    ('    note: "resources main at S-B7 open (contains the S-B6 merge-of-record 6b70de74; main advanced past it with the unrelated lanes before this wave opened — disclosed)",',
     '    note: "resources main at S-B8 open (contains the S-B7 merge-of-record 652ca2d4; main advanced past it with the unrelated T-BOOK-SERVE books lanes before this wave opened — disclosed)",'),
    ('note: "80 files: 2 stage-A pilots (80afdb8e) + 10 S-B1 notes (78ad6a20) + 12 S-B2 notes (96c261a…, PR #237) + 12 S-B3 notes (da18433…, PR #240) + 11 S-B4 notes (fa1f302…, PR #242) + 12 S-B5 notes (6fb25fc…, PR #243) + 12 S-B6 notes (286b5ac…, PR #245/#246) + 9 S-B7 notes (this generation commit)" },',
     'note: "94 files: 2 stage-A pilots (80afdb8e) + 10 S-B1 notes (78ad6a20) + 12 S-B2 notes (96c261a…, PR #237) + 12 S-B3 notes (da18433…, PR #240) + 11 S-B4 notes (fa1f302…, PR #242) + 12 S-B5 notes (6fb25fc…, PR #243) + 12 S-B6 notes (286b5ac…, PR #245/#246) + 9 S-B7 notes (a8889009…, PR #248) + 14 S-B8 notes (this generation commit)" },'),
    ('    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 32 non-R3 per-note streams equal the S-B6 (v13) anchors exactly; the 71 prior-R3 streams equal their own anchors exactly (bytes unchanged); the 9 S-B7 notes add the 76 written items\' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",',
     '    "kind/modelAnswer/keywords on written items ARE §7 stream tokens (the walk extends by those fields on kind!=mcq; old packages carry no kind so the walk is byte-neutral for them): the 18 non-R3 per-note streams equal the S-B7 (v14) anchors exactly; the 80 prior-R3 streams equal their own anchors exactly (bytes unchanged); the 14 S-B8 notes add the 128 written items\' tokens (stem, misconceptionClass, modelAnswer, keywords — written kinds carry no options). Grand + wave subtotals recomputed over all 112 in the v6 note order.",'),
    ('    "one declared 0.4->0.5 shape normalization, first exercised by this wave: lesson-level figureIds == [] is the 0.4 encoding of \'the lesson claims no figures\', and the guided-lesson/0.5 schema requires the key ABSENT in that case (schema description: \'Absent when the lesson claims no figures\') — so the 0.5 build deletes empty figureIds arrays and the D-1 gate normalizes the 0.4 side by the same rule before its byte-compare. Exactly 1 lesson of record is affected across the whole corpus: rn_vVdP57QhDYSVfZgy L2 (the other 2 empty-figureIds 0.4 lessons sit in notes that have never entered the R3 generation). Claimed figures carry through unchanged; schema FILES untouched (delta NONE).",',
     '    "one declared 0.4->0.5 shape normalization (first exercised at wave 7): lesson-level figureIds == [] is the 0.4 encoding of \'the lesson claims no figures\', and the guided-lesson/0.5 schema requires the key ABSENT in that case (schema description: \'Absent when the lesson claims no figures\') — so the 0.5 build deletes empty figureIds arrays and the D-1 gate normalizes the 0.4 side by the same rule before its byte-compare. Exactly 1 lesson of record is affected by this wave: rn_HNXFQt7vM32g6PMv L2 (rn_vVdP57QhDYSVfZgy L2 was normalized the same way at wave 7). Claimed figures carry through unchanged; schema FILES untouched (delta NONE).",'),
    ("""    sb7_notes: TRANCHE,
    cumulative_r3_notes: 80,
    cumulative_r3_lessons: 167,
    cumulative_written_items: 668,
    kinds_cumulative: { recall: 334, "explain-why": 167, application: 167 },
    sb7_wave: { notes: 9, lessons: 19, written_items: 76, kinds: { recall: 38, "explain-why": 19, application: 19 } },
    mcqs_conserved: 1195,
    packages_untouched: 32,
    lessons_untouched: 32,
    authored_chars_delta_vs_v12: grandChars - int3b5.grand_stream.chars,""",
     """    sb7_notes: SB7_NOTES,
    sb8_notes: TRANCHE,
    cumulative_r3_notes: 94,
    cumulative_r3_lessons: 199,
    cumulative_written_items: 796,
    kinds_cumulative: { recall: 398, "explain-why": 199, application: 199 },
    sb8_wave: { notes: 14, lessons: 32, written_items: 128, kinds: { recall: 64, "explain-why": 32, application: 32 } },
    mcqs_conserved: 1195,
    packages_untouched: 18,
    lessons_untouched: 18,
    authored_chars_delta_vs_v14: grandChars - int3b5.grand_stream.chars,"""),
    ('  sb7_authoring_register: {', '  sb8_authoring_register: {'),
    ('    basis: "stage-B plan of record: \'tranche order mirrors the authoring register\' + the S-B6 NEXT (\'per the wave-7/ bucket: 19 guided-lesson files in the authoring dir — final tranche size to be read from the register at wave open\') — S-B7 = the wave-7 register notes (9 notes / 19 lessons / 95 checks per source-0.4; wave-field proven: all 9 rows carry wave==7 in the INT-3 record)",',
     '    basis: "stage-B plan of record: \'tranche order mirrors the authoring register\' + the S-B7 NEXT (\'stage B wave 8 (next register tranche) remains operator-gated per the ledger convention\') — S-B8 = the wave-8 register notes (14 notes / 32 lessons / 160 checks per source-0.4; wave-field proven: all 14 rows carry wave==8 in the INT-3 record)",'),
    # emit paths
    ('const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb7.json"), int3b6);',
     'const int3Buf = emit(path.join(RES, "records/INT-3-transform-record-r3-stageb8.json"), int3b6);'),
    ('const man13Buf = emit(path.join(RES, "hub-import-manifest-v14.json"), man13);',
     'const man13Buf = emit(path.join(RES, "hub-import-manifest-v15.json"), man13);'),
    # promotion receipt
    ('  wave: "R3-MIXED-CHECK-TYPES (stage B wave 7 — the wave-7 authoring register, 9 notes / 19 lessons / 76 written items)",',
     '  wave: "R3-MIXED-CHECK-TYPES (stage B wave 8 — the wave-8 authoring register, 14 notes / 32 lessons / 128 written items)",'),
    ('  operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, SB_GATE_TRACE, SB2_EXECUTE_TRACE, SB3_IGNITION_TRACE, SB4_IGNITION_TRACE, SB5_IGNITION_TRACE, SB6_IGNITION_TRACE, OPERATOR_TRACE],',
     '  operator_traces: [QUEUE_TRACE, STAGE_A_TRACE, SB_GATE_TRACE, SB2_EXECUTE_TRACE, SB3_IGNITION_TRACE, SB4_IGNITION_TRACE, SB5_IGNITION_TRACE, SB6_IGNITION_TRACE, SB7_IGNITION_TRACE, OPERATOR_TRACE],'),
    ('  branch: "integration/r3-stageb7-20261031",',
     '  branch: "integration/r3-stageb8-20261031",'),
    ('  contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups + the S-B1 NEXT of record (\'waves 3..10 to the ~956 total\') + the S-B6 promotion receipt merge_order (\'stage B wave 7 (next register tranche) remains operator-gated per the ledger convention\') — gate opened by operator trace 1a18fd512d610f7d (\'wave 7\')",',
     '  contract_of_record: "R3-MIXED-CHECK-TYPES-STAGE-A-20261030.json followups + the S-B1 NEXT of record (\'waves 3..10 to the ~956 total\') + the S-B7 promotion receipt merge_order (\'stage B wave 8 (next register tranche) remains operator-gated per the ledger convention\') — gate opened by operator trace 1a1900aa14eb84d5 (\'STAGE-B WAVE 8\')",'),
    ('    note: "S-B7 is based on the current resources main (wave-open main of record resolved at run time, recorded in input_pins): the S-B6 generation (PR #245 + merge-of-record #246, merge 6b70de74) is an ancestor of main, and main advanced past it with the unrelated lanes before this wave opened — disclosed, zero overlap with the stage-B namespaces. The S-B1 merge-order convention (resources PR merges first; the hub chain follows) holds for this wave.",\n    sb6_merge_commit: SB6_MERGE,',
     '    note: "S-B8 is based on the current resources main (wave-open main of record resolved at run time, recorded in input_pins): the S-B7 generation (PR #248, merge 652ca2d4) is an ancestor of main, and main advanced past it with the unrelated T-BOOK-SERVE books lanes before this wave opened — disclosed, zero overlap with the stage-B namespaces. The S-B1 merge-order convention (resources PR merges first; the hub chain follows) holds for this wave.",\n    sb7_merge_commit: SB7_MERGE,'),
    ('    A: { sha: commitA, parent: commitAParent, note: "S-B7 source-0.5 generation — 9 authored guided-lesson/0.5 notes (76 written items) added to the namespace (80 files total)" },',
     '    A: { sha: commitA, parent: commitAParent, note: "S-B8 source-0.5 generation — 14 authored guided-lesson/0.5 notes (128 written items) added to the namespace (94 files total)" },'),
    ('    C: { sha: "(namespace-complete — outputs + manifest v14 + records + pipeline)", note: "hub-import-1.4/ ×9 + question-packages-1.1/ ×9 + hub-import-manifest-v14.json + records/INT-3-transform-record-r3-stageb7.json + records/R3-CHECK-TYPES-STAGEB7-PROMOTION-20261031.json + tooling/r3-stageb7-pipeline.js + tooling/r3-stageb7-authoring/ — schema delta NONE (the S-B1 union caps already admit this tranche)" },',
     '    C: { sha: "(namespace-complete — outputs + manifest v15 + records + pipeline)", note: "hub-import-1.4/ ×14 + question-packages-1.1/ ×14 + hub-import-manifest-v15.json + records/INT-3-transform-record-r3-stageb8.json + records/R3-CHECK-TYPES-STAGEB8-PROMOTION-20261031.json + tooling/r3-stageb8-pipeline.js + tooling/r3-stageb8-authoring/ — schema delta NONE (the S-B1 union caps already admit this tranche)" },'),
    ('  artifact_pin: `${SOURCE_PIN_V6} (32 untouched lessons) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${SB1_COMMIT_A} (10 S-B1 notes) | ${SB2_A_FULL} (12 S-B2 notes) | ${SB3_COMMIT_A} (12 S-B3 notes) | ${SB4_COMMIT_A} (11 S-B4 notes) | ${SB5_COMMIT_A} (12 S-B5 notes) | ${SB6_COMMIT_A} (12 S-B6 notes) | ${commitA} (9 new source-0.5 lessons — commit A of this wave)`,',
     '  artifact_pin: `${SOURCE_PIN_V6} (18 untouched lessons) | ${STAGE_A_COMMIT} (2 stage-A pilots) | ${SB1_COMMIT_A} (10 S-B1 notes) | ${SB2_A_FULL} (12 S-B2 notes) | ${SB3_COMMIT_A} (12 S-B3 notes) | ${SB4_COMMIT_A} (11 S-B4 notes) | ${SB5_COMMIT_A} (12 S-B5 notes) | ${SB6_COMMIT_A} (12 S-B6 notes) | ${SB7_COMMIT_A} (9 S-B7 notes) | ${commitA} (14 new source-0.5 lessons — commit A of this wave)`,'),
    ('  pkg_pin: `(32 untouched keep INT-0 4d857c47…; 2 pilots keep ${STAGE_A_COMMIT.slice(0, 8)}; 10 S-B1 keep 78ad6a20; 12 S-B2 keep ${SB2_A_FULL.slice(0, 8)}; 12 S-B3 keep ${SB3_COMMIT_A.slice(0, 8)}; 11 S-B4 keep ${SB4_COMMIT_A.slice(0, 8)}; 12 S-B5 keep ${SB5_COMMIT_A.slice(0, 8)}; 12 S-B6 keep ${SB6_COMMIT_A.slice(0, 8)}; ${commitA} for the 9 new — the EIGHTH package-channel re-pin since INT-0)`,',
     '  pkg_pin: `(18 untouched keep INT-0 4d857c47…; 2 pilots keep ${STAGE_A_COMMIT.slice(0, 8)}; 10 S-B1 keep 78ad6a20; 12 S-B2 keep ${SB2_A_FULL.slice(0, 8)}; 12 S-B3 keep ${SB3_COMMIT_A.slice(0, 8)}; 11 S-B4 keep ${SB4_COMMIT_A.slice(0, 8)}; 12 S-B5 keep ${SB5_COMMIT_A.slice(0, 8)}; 12 S-B6 keep ${SB6_COMMIT_A.slice(0, 8)}; 9 S-B7 keep ${SB7_COMMIT_A.slice(0, 8)}; ${commitA} for the 14 new — the NINTH package-channel re-pin since INT-0)`,'),
    ('  manifest: "hub-import-manifest-v13.json",', '  manifest: "hub-import-manifest-v14.json",'),
    ('  int_record: "INT-3-transform-record-r3-stageb6.json",', '  int_record: "INT-3-transform-record-r3-stageb7.json",'),
    ('  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb7-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb7-authoring/authoring-part2.json", "(lane mirrors: scripts/r3-stageb7/authoring-part{1,2}.json; audit: scripts/r3-stageb7/audit_authoring.py)"],',
     '  authoring_parts: ["SME-GuidedLessons/tooling/r3-stageb8-authoring/authoring-part1.json", "SME-GuidedLessons/tooling/r3-stageb8-authoring/authoring-part2.json", "(lane mirrors: scripts/r3-stageb8/authoring-part{1,2}.json; audit: scripts/r3-stageb8/audit_authoring.py)"],'),
    ('  counts_census: { notes: 112, lessons: 239, checks: 1863, checks_mcq: 1195, checks_written: 668, written_recall: 334, written_explain_why: 167, written_application: 167, sb7_notes: TRANCHE, sb7_written: 76, distractors: 3565 },',
     '  counts_census: { notes: 112, lessons: 239, checks: 1991, checks_mcq: 1195, checks_written: 796, written_recall: 398, written_explain_why: 199, written_application: 199, sb8_notes: TRANCHE, sb8_written: 128, distractors: 3565 },'),
    ('  schema_delta: "NONE — the S-B1 union minors already admit this tranche (sme-question-package/1.1 questions maxItems 45; guided-lesson/0.5 check maxItems 9; hub/lesson-import/1.4 checkRefs 9). S-B7 is a pure data wave under unchanged schemas (ajv re-proof ×224 artifacts + ×9 sources in this run).",',
     '  schema_delta: "NONE — the S-B1 union minors already admit this tranche (sme-question-package/1.1 questions maxItems 45; guided-lesson/0.5 check maxItems 9; hub/lesson-import/1.4 checkRefs 9). S-B8 is a pure data wave under unchanged schemas (ajv re-proof ×224 artifacts + ×14 sources in this run).",'),
    ('    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 32 non-R3 streams == S-B6 (v13) anchors exactly; 71 prior-R3 streams == their own anchors exactly",',
     '    law: "written stems + misconceptionClass + modelAnswer + keywords are §7 stream tokens on kind!=mcq (feed-safe extension: no kind field -> walk unchanged); 18 non-R3 streams == S-B7 (v14) anchors exactly; 80 prior-R3 streams == their own anchors exactly",'),
    ('    mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×9 (+76 count); 32 package shas byte-identical ×32; 71 prior-R3 packages byte-identical ×71",',
     '    mcq_conservation: "tranche package MCQs deep-equal the 1.0 bytes ×14 (+128 count); 18 package shas byte-identical ×18; 80 prior-R3 packages byte-identical ×80",'),
    ('    "resources PR (this branch; a clean descendant of main at wave open) merges to main FIRST; the hub PR (runner FEED r3-stageb7-v14 + re-issued artifacts + re-issued guided-import.json) merges only after; stage B wave 8 (next register tranche) remains operator-gated",',
     '    "resources PR (this branch; a clean descendant of main at wave open) merges to main FIRST; the hub PR (runner FEED r3-stageb8-v15 + re-issued artifacts + re-issued guided-import.json) merges only after; stage B wave 9 (next register tranche) remains operator-gated",'),
    ('    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (9 untouched waves byte-equal to v13 — declared preserved, including wave-9/10 whose buckets carry the already-live stage-A pilots byte-unchanged; wave-7 re-anchored by its 9 S-B7 notes)",',
     '    "wave receipt + recalibration: grand stream recomputed over all 112 notes; wave subtotals ×10 recomputed (9 untouched waves byte-equal to v14 — declared preserved, including wave-9/10 whose buckets carry the already-live stage-A pilots byte-unchanged; wave-8 re-anchored by its 14 S-B8 notes)",'),
    ('emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB7-PROMOTION-20261031.json"), receipt);',
     'emit(path.join(RES, "records/R3-CHECK-TYPES-STAGEB8-PROMOTION-20261031.json"), receipt);'),
    ('fs.copyFileSync(path.join(RES, "hub-import-manifest-v14.json"), path.join(SURV, "hub-import-manifest-v14.json"));',
     'fs.copyFileSync(path.join(RES, "hub-import-manifest-v15.json"), path.join(SURV, "hub-import-manifest-v15.json"));'),
    ('fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb7.json"), path.join(SURV, "INT-3-transform-record-r3-stageb7.json"));',
     'fs.copyFileSync(path.join(RES, "records/INT-3-transform-record-r3-stageb8.json"), path.join(SURV, "INT-3-transform-record-r3-stageb8.json"));'),
    ('console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (v12: ${int3b5.grand_stream.chars} → delta +${grandChars - int3b5.grand_stream.chars})`);',
     'console.log(`  grand stream: ${grandChars} chars ${grandSha.slice(0, 16)}… (v14: ${int3b5.grand_stream.chars} → delta +${grandChars - int3b5.grand_stream.chars})`);'),
    ('console.log(`  census: checks 1787 → 1863 (written 592 → 668: recall 334 / explain-why 167 / application 167; MCQ 1,195 conserved)`);',
     'console.log(`  census: checks 1863 → 1991 (written 668 → 796: recall 398 / explain-why 199 / application 199; MCQ 1,195 conserved)`);'),
]

# anchor_law body swap (long line) — matched by unique prefix/suffix
ANCHOR_OLD_PREFIX = '    anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson\'s keyPoints by KP index; stems verified non-duplicative against ALL 1,195 of-record MCQ stems + 592 of-record written stems + intra-tranche x76'
ANCHOR_NEW = ('    anchor_law: "each written item anchored (authoring-time provenance, stripped from emitted bytes) to one of its lesson\'s keyPoints by KP index; stems verified non-duplicative against ALL 1,195 of-record MCQ stems + 668 of-record written stems + intra-tranche x128 '
              '(token-Jaccard >= 0.6: 0 flags on the final pass — 7 keyword-hygiene re-points and 6 stem re-points applied at authoring); '
              'the wave\'s self-grading audit (model answer grades correct under its own keyword law): 128/128 pass pre-commit; zero-keyword miss probe scores 0 hits on all 128 items; '
              'numeric-claim clusters recomputed in code (the 850 vs 900 bond-balance exothermic census and the 1350 vs 1200 endothermic census, the 10-degrees-Celsius doubling rule, '
              'Q = 100 g x 4.18 J/g/degC x 8 degC = 3344 J with the /1000 kilojoule conversion, the 20-degrees-Celsius combustion stop point, the 21 -> 17 degrees-Celsius endothermic cooling fall, '
              'the -6/+2/-9 sign classification, the 2 g - 0.2 g catalyst remainder, the 5 cm3 portions and the 25 cm3 neutralisation peak, the 4.18 J/g/degC SHC and the manganese(IV) oxide peroxide catalyst pinned in their KPs of record)",')

# 1) header
m = re.search(r"/\*\*.*?\*/", src, flags=re.S)
assert m and m.start() == src.index("/**"), "header anchor not at top"
src = src[: m.start()] + NEW_HEADER + src[m.end():]

# 2) constants block: from 'const PILOTS' through the WAVE_OPEN_MAIN line
c_start = src.index('const PILOTS = ["rn_2MpXPtNXvn8pQm3r"')
c_end_marker = 'const WAVE_OPEN_MAIN = "b57b77f619cd96088399c7da98dc689b69f816b8"; // resources main at S-B7 open'
c_end = src.index(c_end_marker) + len(c_end_marker)
src = src[:c_start] + NEW_CONSTANTS + src[c_end:]

# 3) anchor_law line
a_start = src.index(ANCHOR_OLD_PREFIX)
a_end = src.index('",', a_start) + 2
src = src[:a_start] + ANCHOR_NEW + src[a_end:]

# 4) plain replacements with occurrence assertions
EXPECT = {
    "process.env.SB7_EMIT_ONLY": 3,
    "SB7_EMIT_ONLY": 1,  # after the 3 above are replaced, 1 remains (console line)
}
for old, new in REPS:
    if old == "REGEX_HEADER":
        continue
    n = src.count(old)
    want = EXPECT.get(old, 1)
    if n != want:
        print(f"COUNT MISMATCH ({n}x, want {want}): {old[:110]}")
        sys.exit(1)
    src = src.replace(old, new)

# verify env-var rename count
assert src.count("SB7_EMIT_ONLY") == 0, "stale SB7_EMIT_ONLY remains"
assert src.count("SB8_EMIT_ONLY") == 4, f"SB8_EMIT_ONLY count {src.count('SB8_EMIT_ONLY')}"

open(DST, "w", encoding="utf-8").write(src)
print(f"written {DST} ({len(src)} chars)")
print("all replacements unique — OK")
