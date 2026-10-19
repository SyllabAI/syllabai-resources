#!/usr/bin/env python3
"""c34_maths_a_batch02_check.py — T-C34 (K2-C-2) batch-B02 machine battery.

Verifies the batch-B02 authoring (operator gate K2-C-2 of the C31 K2 scope)
against the live repo. Zero-LLM, deterministic; READ-ONLY toward the graph,
the corpora and the parsed canonical plane — it writes only its own report
(graph/reports/C34_BATCH02_CHECK.json).

  G1  commissioning_record   the authorization parses, AUTHORIZED, verbatim
                             directive 'K2-C-2', scope bounds + invariant set
  G2  record_shape           12 CONCEPT + 2 MISCONCEPTION nodes / 10 edges
                             (6 RP + 2 WAP + 2 REMEDIATED_BY) / 8 held / 12
                             command kinds / 3 identity decisions; every slice
                             SP covered; zero promotions (SUGGESTED)
  G3  preverify_gates        c34_maths_a_batch02_preverify.py exit 0
  G4  quote_probe_gates      c34_maths_a_batch02_quote_probe.py exit 0 (every
                             anchor verbatim; the unjoined-corpus negative
                             control holds at second-batch strength)
  G5  review_reproducible    the committed review sheet byte-equals a fresh
                             deterministic build (json twin compared minus
                             generated_utc)
  G6  freeze_integrity       HEAD == the T-C33 landing baseline; git status
                             shows NO tracked modifications and NO untracked
                             paths outside the T-C34 footprint — corpora,
                             canonical parsed bundle, chemistry and maths-a
                             stores byte-identical
  G7  standing_checkers      graph_check.py and check_no_hardcode.py exit 0 on
                             the untouched tree

Usage:
    python3 scripts/c34_maths_a_batch02_check.py
    # emits graph/reports/C34_BATCH02_CHECK.json; exit 0 iff all gates PASS
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
AUTH = HERE / "c34_maths_a_batch02_authorization.yaml"
DECISIONS = HERE / "c34_maths_a_batch02_decisions.yaml"
PASS2 = HERE / "c34_maths_a_batch02_review_pass2.yaml"
SHEET = REPO / "graph/reports/C34_BATCH02_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C34_BATCH02_REVIEW.json"
REPORT = REPO / "graph/reports/C34_BATCH02_CHECK.json"
BASELINE = "f0f4c2d5929a2e06c92e9f740984e8d68325027a"

FOOTPRINT_OK = (
    lambda p: p.startswith("scripts/c34_maths_a_batch02_")
    or p.startswith("graph/reports/C34_")
)


def sha16(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def run(script: Path) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(script)], capture_output=True,
                       text=True, timeout=300)
    return r.returncode, (r.stdout + r.stderr)


gates: list[dict] = []
fails: list[str] = []


def gate(gid: str, name: str, ok: bool, detail: str = "") -> None:
    gates.append({"gate": gid, "name": name,
                  "status": "PASS" if ok else "FAIL", "detail": detail})
    if not ok:
        fails.append(f"{gid} {name}: {detail}")


# --- G1 commissioning record -------------------------------------------------
auth = yaml.safe_load(AUTH.read_text(encoding="utf-8"))
a = auth.get("authorization", {})
m = auth.get("meta", {})
gate("G1", "commissioning_record",
     a.get("decision") == "AUTHORIZED" and a.get("authorized_by") == "operator"
     and a.get("operator_statement_verbatim") == "K2-C-2"
     and a.get("authorized_date") == "2026-10-01"
     and m.get("task") == "T-C34"
     and bool(a.get("scope", {}).get("unlocked"))
     and bool(a.get("scope", {}).get("not_authorized"))
     and len(a.get("invariants", [])) >= 8,
     f"decision={a.get('decision')} verbatim="
     f"{a.get('operator_statement_verbatim')!r} "
     f"invariants={len(a.get('invariants', []))}")

# --- G2 record shape ---------------------------------------------------------
doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
nodes, edges, held = doc["nodes"], doc["edges"], doc["held"]
SLICE = {"4MA1-1.2E", "4MA1-1.2F", "4MA1-1.2G", "4MA1-1.2H", "4MA1-1.2I",
         "4MA1-1.3A", "4MA1-1.3B", "4MA1-1.3C", "4MA1-1.3D", "4MA1-1.3E",
         "4MA1-1.4A", "4MA1-1.4B"}
con = [x for x in nodes if x["family"] == "CONCEPT"]
mis = [x for x in nodes if x["family"] == "MISCONCEPTION"]
node_sps = {sp["code"] for n in nodes for sp in n["spec_points"]}
shape_ok = (len(con) == 12 and len(mis) == 2 and len(edges) == 10
            and len(held) == 8 and len(doc["command_kinds"]) == 12
            and len(doc["identity_decisions"]) == 3
            and node_sps == SLICE
            and all(n["family"] in ("CONCEPT", "MISCONCEPTION") for n in nodes)
            and all(n["validation_status"] == "SUGGESTED" for n in nodes)
            and sum(1 for e in edges
                    if e["relation"] == "REQUIRES_PREREQUISITE") == 6
            and sum(1 for e in edges
                    if e["relation"] == "WRONG_ANSWER_PATTERN") == 2
            and sum(1 for e in edges
                    if e["relation"] == "REMEDIATED_BY") == 2)
p2 = yaml.safe_load(PASS2.read_text(encoding="utf-8"))
gate("G2", "record_shape", shape_ok and len(p2["node_verdicts"]) == 14
     and len(p2["edge_verdicts"]) == 10 and len(p2["held_agreements"]) == 8,
     f"concept={len(con)} misconception={len(mis)} edges={len(edges)} "
     f"held={len(held)}")

# --- G3 preverify ------------------------------------------------------------
rc, out = run(HERE / "c34_maths_a_batch02_preverify.py")
gate("G3", "preverify_gates", rc == 0, out.strip().splitlines()[-1][:220]
     if out.strip() else "no output")

# --- G4 quote probe ----------------------------------------------------------
rc, out = run(HERE / "c34_maths_a_batch02_quote_probe.py")
gate("G4", "quote_probe_gates", rc == 0, out.strip().splitlines()[-2][:220]
     if out.strip() else "no output")

# --- G5 review reproducibility ----------------------------------------------
rc, out = run(HERE / "c34_maths_a_batch02_review_build.py")
sheet_ok = rc == 0
detail = out.strip()[:200]
if sheet_ok:
    committed = SHEET.read_bytes()
    rc2, _ = run(HERE / "c34_maths_a_batch02_review_build.py")
    sheet_ok = rc2 == 0 and SHEET.read_bytes() == committed
    detail = f"byte-stable across rebuilds: {sheet_ok}"
gate("G5", "review_reproducible", sheet_ok, detail)

# --- G6 freeze integrity -----------------------------------------------------
head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                      capture_output=True, text=True).stdout.strip()
st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "-uall"],
                    capture_output=True, text=True).stdout.splitlines()
bad = []
for line in st:
    path = line[3:].strip().strip('"')
    if not FOOTPRINT_OK(path):
        bad.append(line)
gate("G6", "freeze_integrity", head == BASELINE and not bad,
     f"HEAD={head[:12]} baseline={BASELINE[:12]} out-of-footprint={bad[:5]}")

# --- G7 standing checkers ----------------------------------------------------
rc1, o1 = run(REPO / "scripts" / "graph_check.py")
rc2, o2 = run(REPO / "scripts" / "check_no_hardcode.py")
gate("G7", "standing_checkers", rc1 == 0 and rc2 == 0,
     f"graph_check rc={rc1}, check_no_hardcode rc={rc2}")

# ---------------------------------------------------------------------------
ok = not fails
report = {
    "schema": "syllabai.c34-batch02-check/1.0",
    "task": "T-C34",
    "gate": "K2-C-2",
    "batch": "B02",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "baseline": BASELINE,
    "result": "ALL PASS" if ok else "FAIL",
    "gates": gates,
    "artifacts": {
        "authorization": {"path": "scripts/c34_maths_a_batch02_authorization.yaml",
                          "sha256_16": sha16(AUTH)},
        "decisions": {"path": "scripts/c34_maths_a_batch02_decisions.yaml",
                      "sha256_16": sha16(DECISIONS)},
        "pass2": {"path": "scripts/c34_maths_a_batch02_review_pass2.yaml",
                  "sha256_16": sha16(PASS2)},
        "review_sheet": {"path": "graph/reports/C34_BATCH02_REVIEW_SHEET.md",
                         "sha256_16": sha16(SHEET)},
        "review_json": {"path": "graph/reports/C34_BATCH02_REVIEW.json",
                        "sha256_16": sha16(SHEET_JSON)},
    },
}
REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                  encoding="utf-8")
print(f"C34 BATCH02 CHECK: {'ALL PASS' if ok else 'FAIL'} "
      f"({sum(1 for g in gates if g['status'] == 'PASS')}/{len(gates)} gates)")
for g in gates:
    print(f"  [{g['status']}] {g['gate']} {g['name']}"
          + (f" — {g['detail']}" if g["detail"] else ""))
sys.exit(0 if ok else 1)
