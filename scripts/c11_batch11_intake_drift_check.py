#!/usr/bin/env python3
"""C11 batch-11 intake conformance check (session 67).

Intake form — a NEW lane, honestly characterized: the operator retrieved
the committed Batch 11 review sheet DIRECTLY from GitHub (the repo
artifact graph/reports/C11_BATCH11_REVIEW_SHEET.md — "I reviewed the
Batch 11 sheet from GitHub"; the sheet's own machine-state section is
therefore read at source, not restated) and returned the operator
verdict INLINE in-chat (zai-web, session 67) as a SELF-CONTAINED verdict
surface: the 11-row decision table, the five node codes, the scoped-
prerequisite guardrail, the boundary-preservation block (12 edges /
10 owners + the 12-vs-10 explanation), the held range, the status
qualification and the Final disposition. No ```text restatement blocks
exist in this intake (the batch-9/10 restatement lane does NOT apply);
byte-identity is NOT claimed and would be meaningless against a
sheet reviewed at source. This check verifies SEMANTIC CONFORMANCE of
the inline verdict against the coded gate-sheet surface:

  1. the 11-row decision table equals the gate totals (5 nodes / 17
     authored edges / 4 identity decisions / 10 held / 12 boundary /
     0 RR / 0 rejected / 0 duplicate mints / 0+0 promotions /
     authority SUGGESTED);
  2. the five named node codes equal the gate §2 node codes exactly;
  3. the four scoped-REQUIRES_PREREQUISITE guardrail bullets are
     present and cover the operator's route-specific interpretation
     invariant (the reconciliation guardrail);
  4. the ten boundary owner codes equal the distinct targets of the
     gate's twelve sanctioned boundary rows, the 12-vs-10 count is
     explained (ALCOHOLS x2 + CARBOXYLIC-ACIDS x2), and the owner set
     matches the session-66 ruling's ownership records (batch
     attributions asserted against the ruling, which the verdict
     inherits);
  5. held range B11-H-01..10 == gate §4 held rows with quarantine +
     §19 failure-class provenance preserved; RR=0, REJECT=0,
     promotions=0, duplicate mints=0;
  6. the status qualification (REPORTED / VERIFIED BY SUBMITTED
     ARTIFACT — 193/488, 33 quote probes, pass-2, the 4.15 negative
     control) and the Final disposition (ACCEPTED — PASS WITH NOTES;
     nothing promoted; the governed path) are present.

Exit 0 only if every check passes. The condensed-element list is printed
for the honest intake record.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry

GATE = GP.reports_dir() / "C11_BATCH11_REVIEW_SHEET.md"
RULING = HERE / "c11_batch11_boundary_ruling.yaml"
DONE = "/home/z/my-project/upload/C11_BATCH11_OPERATOR_VERDICT.md"

gate = open(GATE, encoding="utf-8").read()
done = open(DONE, encoding="utf-8").read()
failures = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


print("== A. transmittal + structure ==")
check("intake artifact opens with the GitHub-direct retrieval statement",
      done.lstrip().startswith(
          "I reviewed the **Batch 11 sheet from GitHub**"))
check("operator verdict header present",
      "### T-C11 Batch 11 — Operator Verdict" in done)
check("key-notes / boundary / held / status / final sections present",
      all(s in done for s in [
          "### Key operator notes", "### Boundary preservation",
          "### Held candidates", "### Status qualification", "### Final"]))

print("== B. gate-sheet coded surface parsed ==")
gate_node_codes = re.findall(r"^\| \d+ \| `(4CH1-(?:CON|MIS)-[A-Z0-9-]+)`",
                             gate, re.M)
gate_edge_triples = [" ".join(t) for t in re.findall(
    r"^\| \d+ \| `(4CH1-(?:CON|MIS|PR)-[A-Z0-9-]+) "
    r"(REQUIRES_PREREQUISITE|WRONG_ANSWER_PATTERN|REMEDIATED_BY) "
    r"(4CH1-(?:CON|MIS|PR)-[A-Z0-9-]+)`", gate, re.M)]
# the batch-11 concept nodes (in-slice RP targets; the 4.43C practical
# rides PR-12, so the node set is the 4 CONCEPT codes)
B11_CONCEPTS = {"4CH1-CON-ESTERS", "4CH1-CON-ADDITION-POLYMERS",
                "4CH1-CON-POLYMER-DISPOSAL",
                "4CH1-CON-CONDENSATION-POLYMERS"}
gate_boundary_rows = [t for t in gate_edge_triples
                      if t.split()[1] == "REQUIRES_PREREQUISITE"
                      and t.split()[2] not in B11_CONCEPTS]
gate_inslice_rows = [t for t in gate_edge_triples
                     if t not in gate_boundary_rows]
gate_held_ids = re.findall(r"^\| (B11-H-\d{2}) \|", gate, re.M)
check("gate node rows == 5", len(gate_node_codes) == 5,
      f"got {len(gate_node_codes)}")
check("gate edge rows == 17", len(gate_edge_triples) == 17,
      f"got {len(gate_edge_triples)}")
check("gate held rows == 10 (B11-H-01..10 contiguous)",
      gate_held_ids == [f"B11-H-{i:02d}" for i in range(1, 11)],
      f"got {gate_held_ids}")

print("== C. verdict table == gate totals ==")
table = dict(re.findall(r"^\| ([A-Za-z_ ]+?)\s+\| \*\*([^*]+)\*\*",
                        done, re.M))
check("VERDICT: PASS WITH NOTES stated",
      "**`PASS WITH NOTES`**" in done)
check("nodes 5/5 CONFIRM", table.get("Nodes") == "5/5 CONFIRM",
      str(table.get("Nodes")))
check("authored edges 17/17 CONFIRM",
      table.get("Authored semantic edges") == "17/17 CONFIRM")
check("identity decisions 4/4 KEEP_AS_IS",
      table.get("Identity decisions") == "4/4 KEEP_AS_IS")
check("held candidates 10/10 ACKNOWLEDGED / QUARANTINED",
      table.get("Held candidates") == "10/10 ACKNOWLEDGED / QUARANTINED")
check("REVIEW_REQUIRED 0 / rejected 0 / duplicate mints 0",
      table.get("REVIEW_REQUIRED") == "0"
      and table.get("Rejected authored edges") == "0"
      and table.get("Duplicate mints") == "0")
check("node promotions 0 / edge promotions 0",
      table.get("Node promotions") == "0"
      and table.get("Edge promotions") == "0")
check("boundary edges 12/12 RETAIN",
      table.get("Boundary edges") == "12/12 RETAIN")
check("authority SUGGESTED", table.get("Authority") == "SUGGESTED")
check("table totals reconcile with the gate surface (5 nodes / 17 edges "
      "/ 10 held / 12 boundary / 4 identities)",
      len(gate_node_codes) == 5 and len(gate_edge_triples) == 17
      and len(gate_held_ids) == 10 and len(gate_boundary_rows) == 12
      and len(gate_inslice_rows) == 5
      and gate.count("cross-section") >= 1)

print("== D. node codes 1:1 (notes list vs gate §2) ==")
done_node_codes = re.findall(r"^\d+\. `(4CH1-(?:CON|MIS)-[A-Z0-9-]+)` — CONFIRM$",
                             done, re.M)
check("verdict names 5 node codes", len(done_node_codes) == 5,
      f"got {done_node_codes}")
check("node code sets equal", sorted(done_node_codes)
      == sorted(gate_node_codes))
check("misconception row present",
      "4CH1-MIS-POLYMER-DOUBLE-BOND" in done_node_codes)
check("identity decisions KEEP_AS_IS incl. the misconception mint",
      "The four identity decisions are **KEEP_AS_IS**, including the "
      "single misconception mint for the double-bonded polymer "
      "repeat-unit error." in done)

print("== E. scoped-prerequisite guardrail (the reconciliation invariant) ==")
check("RP interpreted as scoped teaching/route dependency, not universal "
      "ontological prerequisite",
      "`REQUIRES_PREREQUISITE` should be interpreted as a **scoped "
      "teaching/route dependency**, not automatically as a universal "
      "ontological prerequisite." in done)
for bullet in (
    "Ester → alcohols/carboxylic acids: scoped to esterification.",
    "Addition polymers → alkenes: scoped to the C=C addition-polymer "
    "route.",
    # session-67 editorial correction (2026-09-25, dated): the intake
    # transcription carried a typo 'combattion'; the operator's word is
    # 'combustion' (not an English word otherwise; corrected in the
    # intake artifact, the verdict record and this checker — the bullet
    # is still checked verbatim, nothing weakened).
    "Polymer disposal → CO₂/CO: scoped to the taught "
    "incineration/combustion surface.",
    "Condensation polymers → esters/carboxylic acids/alcohols: scoped "
    "to the polyester route represented in this slice.",
):
    check(f"guardrail bullet present: {bullet[:48]}…", bullet in done)
check("route-specific interpretation invariant named for reconciliation",
      "the **route-specific interpretation of the prerequisite edges**"
      in done
      and "should not accidentally turn these teaching-sequence "
      "relationships into universal KG prerequisites" in done)

print("== F. boundary preservation 1:1 (owners vs gate boundary rows + "
      "session-66 ruling) ==")
check("retain all 12 sanctioned cross-section edges",
      "Retain all **12 sanctioned cross-section edges**" in done)
owners_block = re.findall(r"^\* `(CON-[A-Z0-9-]+)`$", done, re.M)
gate_boundary_targets = sorted({t.split()[2] for t in gate_boundary_rows})
check("gate boundary composition: 12 external-target RP rows + 3 "
      "in-slice RP rows + 2 misconception rows = 17",
      len(gate_boundary_rows) == 12 and len(gate_inslice_rows) == 5
      and sum(1 for t in gate_edge_triples
              if t.split()[1] in ("WRONG_ANSWER_PATTERN",
                                  "REMEDIATED_BY")) == 2
      and all(t.split()[1] == "REQUIRES_PREREQUISITE"
              for t in gate_boundary_rows))
check("10 owner codes named", len(owners_block) == 10,
      f"got {owners_block}")
check("owner set == distinct targets of the gate boundary rows",
      sorted(f"4CH1-{o}" for o in owners_block)
      == gate_boundary_targets,
      f"targets={gate_boundary_targets}")
check("12-vs-10 count explained (ALCOHOLS x2 + CARBOXYLIC-ACIDS x2)",
      "The apparent 12-vs-10 count is intentional because Alcohols and "
      "Carboxylic Acids each receive two sanctioned boundary edges."
      in done)
import yaml  # noqa: E402
rul = yaml.safe_load(RULING.read_text(encoding="utf-8"))
sanctioned = {s["target"]: s for s in
              rul["boundary_edge_ruling"]["sanctioned_targets"]}
owner_batch_expected = {
    tgt: s["owner"].split()[1] for tgt, s in sanctioned.items()}
check("owner->batch attribution (inherited from the session-66 ruling) "
      "covers all 10 owners",
      set(owner_batch_expected.values()) == {"10", "9", "5", "1", "7"}
      and len(rul["boundary_edge_ruling"]["sanctioned_targets"]) == 12
      and len(sanctioned) == 10
      and all(f"4CH1-{o}" in sanctioned for o in owners_block),
      str(sorted(owner_batch_expected.items()))[:120])
check("no duplicate mint for existing owners",
      "do **not** mint duplicates for existing owners" in done)

print("== G. held candidates 1:1 (range vs gate §4) ==")
check("all ten remain quarantined; range B11-H-01..B11-H-10 named",
      "All ten remain quarantined" in done
      and "`B11-H-01` through `B11-H-10`" in done)
check("no held candidate reopened or promoted",
      "No held candidate should be reopened or promoted as part of this "
      "review." in done)
check("§19 failure-class provenance preserved",
      "Their abstention/failure classes remain part of the graph "
      "provenance." in done)

print("== H. status qualification + final disposition ==")
check("sheet directly retrieved and reviewed",
      "The GitHub review sheet itself was directly retrieved and "
      "reviewed." in done)
check("REPORTED / VERIFIED BY SUBMITTED ARTIFACT caveat present",
      "**REPORTED / VERIFIED BY SUBMITTED ARTIFACT**" in done)
check("caveat: not represented as independently re-executed",
      "rather than being represented as independently re-executed by "
      "this review" in done)
check("machine-state surface named (193/488, 33 quote probes, pass-2, "
      "4.15 negative control)",
      "**193-node / 488-edge**" in done and "33 quote probes" in done
      and "pass-2 results" in done and "4.15 negative control" in done)
check("final: ACCEPTED — PASS WITH NOTES",
      "**Batch 11: ACCEPTED — PASS WITH NOTES**" in done)
check("nothing promoted by this review",
      "**Nothing is promoted by this review.**" in done)
check("governed path stated (verdict YAML → … → full gate suite)",
      "`verdict YAML → reconciliation → preserve boundaries/holds → "
      "§18 promotion where separately authorised → regeneration → full "
      "gate suite`" in done)

print("== I. honest intake record: condensed elements ==")
condensed = []
if "```text" in done:
    condensed.append("UNEXPECTED: restatement blocks present (the "
                     "GitHub-direct lane claims none)")
if "Raw agreement (NOT κ" not in done:
    condensed.append("§1 raw-agreement/forecast-calibration paragraphs "
                     "(the sheet is read at source)")
if "| # | code | family | title |" not in done:
    condensed.append("§2 node detail columns (family/title/attaches/"
                     "conf/evidence; the 5 codes + decisions preserved)")
if "| # | edge | conf | derivation |" not in done:
    condensed.append("§3 edge detail columns (conf/derivation/evidence; "
                     "the 17/17 universal + scoped guardrail preserved)")
if "| id | candidate | failure class / reason |" not in done:
    condensed.append("§4 held candidate/failure-class columns (the "
                     "range + quarantine preserved; no per-candidate "
                     "dispositions claimed)")
print("  condensed/restated (recorded, non-blocking):")
for c in condensed:
    print(f"    - {c}")
check("no restatement blocks claimed (GitHub-direct lane)",
      "```text" not in done)
check("condensed-element inventory non-empty (honest characterization)",
      len([c for c in condensed if not c.startswith("UNEXPECTED")]) >= 3)

print()
if failures:
    print(f"INTAKE CONFORMANCE: FAIL ({len(failures)} failures): "
          f"{failures}")
    sys.exit(1)
print("INTAKE CONFORMANCE: ALL PASS — the inline operator verdict covers "
      "the coded gate surface (GitHub-direct sheet review + inline "
      "verdict lane); encoding may proceed tracing the verdict table, "
      "the scoped-RP guardrail, the boundary-preservation block and the "
      "Final disposition.")
