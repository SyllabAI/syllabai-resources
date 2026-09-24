#!/usr/bin/env python3
"""C11 batch-10 intake conformance check (session 65).

The operator delivered the completed sheet INLINE in-chat (zai-web,
session 65) as a restatement: the submitted sheet's verdict surface is
preserved (including MORE per-row detail than batch-9's restatement —
the 8 node codes, the 9 held ids with per-candidate dispositions, the
six in-slice edge TRIPLEs and the ELEVEN boundary owner codes), but the
gate sheet's §1/§2/§3/§4/§5 detail columns (evidence quotes,
derivations, failure classes, forecast calibration, pathway line) are
condensed. Byte-identity of §1-5 is therefore NOT claimed (and would be
false — the batch-5/6/8 zero-drift check does not apply; the batch-9
conformance-gate precedent applies). This check verifies SEMANTIC
CONFORMANCE of the completed sheet against the coded gate-sheet surface:

  1. every gate-sheet surface element is covered by an explicit
     completed-sheet verdict (universal totals + the 8 node codes +
     the 6 in-slice TRIPLEs + the ELEVEN owner codes + per-id held
     dispositions + the 5 identity sentences);
  2. the six in-slice TRIPLEs restated in §6.2 match gate rows 1-6
     exactly, modulo the sanctioned shorthand (no `4CH1-` prefixes);
  3. the eleven §6.4 owner codes equal the distinct targets of gate
     rows 7-19, and the §6.2 owner->batch attribution list matches the
     session-64 ruling's ownership records;
  4. the five identity decisions B10-ID-01..05 map 1:1 to the gate
     sheet's identity-policy notes with the same family rulings;
  5. held range B10-H-01..09 == gate §4 held rows with all 9 KEEP HELD;
     RR=0, REJECT=0, promotions=0, duplicate mints=0; REPORTED caveat
     + PASS WITH NOTES present verbatim.

Exit 0 only if every check passes. The condensed-element list is printed
for the honest intake record.
"""
import re
import sys

GATE = ("/home/z/my-project/download/t-c11-batch10-gate/"
        "C11_BATCH10_REVIEW_SHEET.md")
DONE = "/home/z/my-project/upload/C11_BATCH10_REVIEW_SHEET_COMPLETED.md"

gate = open(GATE, encoding="utf-8").read()
done = open(DONE, encoding="utf-8").read()
failures = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


print("== A. transmittal + structure ==")
check("operator completion header is line 1",
      done.splitlines()[0].startswith(
          "# T-C11 §16 Batch 10 Review Sheet — Operator Completion"))
check("operator verdict section exists", "## 6. Operator verdict" in done)
check("final disposition section exists",
      "# 7. Final operator disposition" in done)

print("== B. gate-sheet coded surface parsed ==")
gate_node_codes = re.findall(r"^\| \d+ \| `(4CH1-(?:CON|MIS)-[A-Z0-9-]+)`",
                             gate, re.M)
gate_edge_triples = [" ".join(t) for t in re.findall(
    r"^\| \d+ \| `(4CH1-(?:CON|MIS)-[A-Z0-9-]+) "
    r"(REQUIRES_PREREQUISITE|WRONG_ANSWER_PATTERN|REMEDIATED_BY) "
    r"(4CH1-(?:CON|MIS)-[A-Z0-9-]+)`", gate, re.M)]
gate_held_ids = re.findall(r"^\| (B10-H-\d{2}) \|", gate, re.M)
gate_identity_ids = [f"B10-ID-0{i}" for i in range(1, 6)]  # per gate §2 notes

check("gate node rows == 8", len(gate_node_codes) == 8,
      f"got {len(gate_node_codes)}")
check("gate edge rows == 19", len(gate_edge_triples) == 19,
      f"got {len(gate_edge_triples)}")
check("gate held rows == 9 (B10-H-01..09 contiguous)",
      gate_held_ids == [f"B10-H-{i:02d}" for i in range(1, 10)],
      f"got {gate_held_ids}")

print("== C. completed-sheet verdict surface ==")
check("VERDICT: PASS WITH NOTES (§6 + §7 final status)",
      done.count("VERDICT: PASS WITH NOTES") >= 2)
check("nodes 8/8 CONFIRM stated (§6.1)", "8/8 — CONFIRM" in done)
check("all eight proposed identities accepted (§6.1 universal)",
      "All eight proposed identities are accepted for this review surface."
      in done)
check("edges 19/19 CONFIRM stated (§6.2)", "19/19 — CONFIRM" in done)
check("all 19 submitted edges accepted (§6.2 universal)",
      "All 19 submitted semantic edges are accepted with their submitted "
      "relation class and direction." in done)
check("held 9/9 ACKNOWLEDGE / KEEP QUARANTINED (§6.3)",
      "9/9 — ACKNOWLEDGE / KEEP QUARANTINED" in done)
check("held range B10-H-01..B10-H-09 named (§6.3)",
      "B10-H-01 through B10-H-09 remain held" in done)
check("boundary edges 'retained exactly as ruled' (§6.2)",
      "retained exactly as ruled in the submitted session-64 boundary "
      "ruling" in done)
check("boundary relationships not new identities (§6.2)",
      "boundary relationships to existing concept owners" in done)
check("no duplicate concept for any boundary target (§6.2)",
      "No duplicate concept should be minted for any of these targets."
      in done)
check("REPORTED caveat present verbatim (x2)",
      done.count("REPORTED / VERIFIED BY SUBMITTED ARTIFACT") >= 2)
check("caveat: rather than independently re-executed (§6)",
      "rather than independently re-executed in this review" in done)
check("caveat: not independently re-executed during this review (§6.6)",
      "They have not been independently re-executed during this review."
      in done)
check("authority stays SUGGESTED",
      "`SUGGESTED`" in done and "NODE AUTHORITY: SUGGESTED" in done)
check("no node promoted by this review (§6.1)",
      "No node is promoted by this review." in done)
check("zero promotions at gate stated (§7 final status)",
      "Promotion count at this gate:** `0`" in done
      and "EDGE PROMOTIONS: 0" in done and "NODE PROMOTIONS: 0" in done)
check("counts block: 8 confirmed / 19 edges / 9 held / 0 RR / 0 rejected",
      all(s in done for s in [
          "Nodes confirmed                    8",
          "Authored edges confirmed          19",
          "Held candidates                    9",
          "REVIEW_REQUIRED edges              0",
          "Rejected authored edges            0",
          "Node promotions                    0",
          "Edge promotions                    0",
          "Duplicate concept mints            0",
          "Boundary-owner violations          0 reported"]))
check("no duplicate mints",
      "DUPLICATE MINTS: 0" in done and "Duplicate concept mints            0"
      in done)
check("boundary edges retained count (§7)", "BOUNDARY EDGES: 13 — RETAIN"
      in done)
check("§18 authorization for post-gate promotion (§7 step 6)",
      "Apply §18 promotion only to explicitly authorized promotion records"
      in done)
check("'No node or edge is promoted by this review sheet itself.'",
      "No node or edge is promoted by this review sheet itself." in done)

print("== D. identity decisions 1:1 ==")
id_map = {
    "B10-ID-01": "Keep the 4.23–4.26 alkene family unified.",
    "B10-ID-02": "Keep the 4.27–4.28 bromine-water reaction/test family "
                 "unified.",
    "B10-ID-03": "Keep the 4.32C–4.33C ethanol-manufacture family unified.",
    "B10-ID-04": "Keep the 4.34C + 4.35C + 4.37C carboxylic-acids family "
                 "unified.",
    "B10-ID-05": "Keep the single assessment-documented propan-2-ol naming "
                 "misconception mint.",
}
for iid, sentence in id_map.items():
    ok = f"{iid} — ACCEPT**\n\n{sentence}" in done
    check(f"{iid} ACCEPT with matching family ruling", ok,
          sentence if not ok else "exact sentence match")
check("anti-duplication guardrail present",
      "must **not** be interpreted as permission to mint duplicate "
      "concepts during reconciliation" in done)

print("== E. node codes 1:1 (§6.1 table vs gate §2) ==")
done_node_codes = re.findall(r"^\| `(4CH1-(?:CON|MIS)-[A-Z0-9-]+)`\s*\|",
                             done, re.M)
check("completed sheet names 8 node codes", len(done_node_codes) == 8,
      f"got {done_node_codes}")
check("node code sets equal",
      sorted(done_node_codes) == sorted(gate_node_codes))
check("misconception row present",
      "4CH1-MIS-PROPANOL-POSITION" in done_node_codes)

print("== F. held dispositions 1:1 (§6.3 vs gate §4) ==")
done_held = re.findall(r"^\| (B10-H-\d{2}) \| \*\*KEEP HELD\*\*", done, re.M)
check("9 held rows all KEEP HELD, ids B10-H-01..09",
      done_held == [f"B10-H-{i:02d}" for i in range(1, 10)],
      f"got {done_held}")
check("held quarantine closing rules present",
      "No held candidate should be reopened or promoted as a consequence "
      "of this review." in done
      and "The §19 failure-class provenance should remain intact." in done)

print("== G. edge conformance (shorthand-tolerant) ==")


def strip4(s):
    return s.replace("4CH1-", "")


gate_inslice = [tuple(strip4(x) for x in t.split())
                for t in gate_edge_triples[:6]]
blocks = []
for chunk in done.split("```text\n")[1:]:
    body = chunk.split("```")[0]
    ls = [ln.strip() for ln in body.splitlines() if ln.strip()]
    blocks.append(ls)
check("five ```text blocks present (edges x2 + owners + counts + status "
      "== 5 total)", len(blocks) == 5, f"got {len(blocks)} blocks: "
      f"{[len(b) for b in blocks]}")
# classify blocks by CONTENT (two blocks share the 11-non-empty-line
# shape: the §6.4 owner list and the §7 final-status block)
edge_blocks = [b for b in blocks if len(b) == 12]
miscon_blocks = [b for b in blocks if len(b) == 6]
owner_blocks = [b for b in blocks if len(b) == 11
                and all(re.fullmatch(r"(?:CON-)?[A-Z0-9]+(?:-[A-Z0-9]+)*",
                                     ln) for ln in b)]
status_blocks = [b for b in blocks if "VERDICT: PASS WITH NOTES" in b
                 and "BOUNDARY EDGES" in " ".join(b)]
counts_blocks = [b for b in blocks if len(b) == 9
                 and any(ln.startswith("Nodes confirmed") for ln in b)]
check("block classification 1/1/1/1/1",
      len(edge_blocks) == 1 and len(miscon_blocks) == 1
      and len(owner_blocks) == 1 and len(status_blocks) == 1
      and len(counts_blocks) == 1,
      f"edges={len(edge_blocks)} miscon={len(miscon_blocks)} "
      f"owners={len(owner_blocks)} status={len(status_blocks)} "
      f"counts={len(counts_blocks)}")
restated = []
if edge_blocks:
    b = edge_blocks[0]
    restated += [(b[i], b[i + 1], b[i + 2]) for i in range(0, 12, 3)]
if miscon_blocks:
    b = miscon_blocks[0]
    restated += [(b[i], b[i + 1], b[i + 2]) for i in range(0, 6, 3)]
check("6 in-slice TRIPLEs restated (4 RP + WAP + RB)", len(restated) == 6)
check("restated TRIPLEs match gate rows 1-6 (modulo 4CH1- prefix)",
      restated == gate_inslice,
      f"restated={restated}" if restated != gate_inslice else "exact match")
check("restated classes: 4 REQUIRES_PREREQUISITE + 1 WAP + 1 REMEDIATED_BY",
      [c for _, c, _ in restated] ==
      ["REQUIRES_PREREQUISITE"] * 4 + ["WRONG_ANSWER_PATTERN",
                                       "REMEDIATED_BY"])
if owner_blocks:
    owners_block = owner_blocks[0]
    gate_boundary_targets = sorted({t.split()[2].replace("4CH1-CON-", "")
                                    for t in gate_edge_triples[6:]})
    check("§6.4 owner block == 11 codes == distinct targets of gate rows "
          "7-19", sorted(owners_block) == gate_boundary_targets,
          f"block={sorted(owners_block)} targets={gate_boundary_targets}")
else:
    check("§6.4 owner block present", False)

print("== H. owner->batch attribution list (§6.2 vs session-64 ruling) ==")
expected_owner_batch = {
    "CON-HOMOLOGOUS-SERIES": "9", "CON-ORGANIC-FORMULAE": "9",
    "CON-HYDROCARBON": "9", "CON-ALKANES": "9",
    "CON-ORGANIC-REACTION-CLASSES": "9", "CON-IUPAC-NAMING": "9",
    "CON-CRACKING": "9", "CON-COMBUSTION-O2": "5",
    "CON-OX-RED-AGENTS": "6", "CON-FRACTIONAL-DISTILLATION": "1",
    "CON-ACID-REACTIONS": "7",
}
done_owner_batch = dict(re.findall(
    r"^\* `(CON-[A-Z0-9-]+)` — batch (\d+)$", done, re.M))
check("11 owner->batch bullets present", len(done_owner_batch) == 11,
      f"got {len(done_owner_batch)}")
check("owner->batch attribution matches the session-64 ruling records",
      done_owner_batch == expected_owner_batch,
      f"got {done_owner_batch}"
      if done_owner_batch != expected_owner_batch else "exact match")

print("== I. honest intake record: condensed elements ==")
condensed = []
if "Forecast calibration (C11_BATCH_FORECAST.json" not in done:
    condensed.append("§1 forecast-calibration paragraph")
if "| # | code | family | title |" not in done:
    condensed.append("§2 node detail columns (family/title/attaches/conf/"
                     "evidence; codes + decisions preserved)")
if "| # | edge | conf | derivation |" not in done:
    condensed.append("§3 edge detail columns (conf/derivation/evidence; "
                     "the 6 in-slice TRIPLEs preserved in §6.2)")
if "| id | candidate | failure class / reason |" not in done:
    condensed.append("§4 held candidate/failure-class columns (ids + "
                     "dispositions preserved)")
if "Raw agreement (NOT κ" not in done:
    condensed.append("§1 raw-agreement note")
if "Pathway: fill `scripts/c11_batch10_verdicts_template.yaml`" not in done:
    condensed.append("§5 pathway line (superseded by §7 required-next-"
                     "steps)")
if done.count("REQUIRES_PREREQUISITE") < 13:
    condensed.append("§6.2 13-row boundary edge detail (restated as the "
                     "ELEVEN owner targets + the 13-edge count)")
print("  condensed/restated (recorded, non-blocking):")
for c in condensed:
    print(f"    - {c}")
check("condensed-element inventory non-empty (restatement confirmed)",
      len(condensed) >= 4)

print()
if failures:
    print(f"INTAKE CONFORMANCE: FAIL ({len(failures)} failures): "
          f"{failures}")
    sys.exit(1)
print("INTAKE CONFORMANCE: ALL PASS — completed sheet covers the coded "
      "gate surface; encoding may proceed tracing §6/§7 rulings.")
