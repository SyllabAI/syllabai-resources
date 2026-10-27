#!/usr/bin/env python3
"""
T-C11 session 52 — c11_verdict_apply_batch3.py: §7 decision-record
re-authoring that applies the operator's session-52 batch-3 verdicts
(scripts/c11_batch3_verdicts.yaml, the practical-review policy) to the
REVIEW-STATE layer of scripts/c11_batch3_decisions.yaml.

Scope (the §7 sanctioned re-authoring pathway — session-45/48/50 precedent):
  * header note recording the session-52 verdict round + application.
  * NOTHING ELSE: this batch authored no REVIEW_REQUIRED edge (no RR
    settlement block), carries no ENRICHMENT-scoped node (no enrichment
    operator_decision block), and every identity decision is KEEP_AS_IS
    (no MERGE/SPLIT re-authoring). The node CONFIRM verdicts are recorded
    in the operator-owned verdict file itself — review state only.

The 39 edge CONFIRM verdicts need NO §7 block: they flow through the §18
promotion pathway (c11_diff_review.py approve -> c11_promote.py -> gated
G13 re-run), exactly as the pilot's 28, batch-1's 28 and batch-2's 23
CONFIRM edges did in sessions 45/48/50.

What this script NEVER does:
  * never sets validation_status (blocks are review state only, §7; they are
    not in EDGE_KEYS/NODE_KEYS and never reach graph/*.yaml);
  * never promotes anything (§18 promotions live in
    scripts/c11_promotions.yaml, written only by scripts/c11_promote.py);
  * never touches evidence quotes, provenance, confidence, held candidates.

Fail-closed: every edit is anchored on byte-exact pre-state text; any drift,
duplication or missing anchor aborts BEFORE the file is written.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DEC = HERE / "c11_batch3_decisions.yaml"
VERDICTS = HERE / "c11_batch3_verdicts.yaml"

HEADER_NOTE = """
#
# OPERATOR DECISIONS (session 52, applied session 52, 2026-09-13): the
# operator's batch-3 verdicts live in scripts/c11_batch3_verdicts.yaml
# (operator-owned; the session-52 practical-review policy: CONFIRM where
# the evidence clearly supports the authored relationship; HOLD/REJECT only
# for genuine evidence insufficiency or an architectural/semantic problem;
# ordinary ontology imperfection, wording preferences, enrichment
# opportunities and theoretical alternative interpretations are NOT
# blockers; the verdict file is the operator authorization for promotion):
# 39 edge CONFIRM / 0 HOLD / 0 REJECT; 24 node CONFIRM; 7 identity
# decisions KEEP_AS_IS; no RR settlement (this batch authored no
# REVIEW_REQUIRED edge); the held appendix (14) acknowledged — a clean
# quarantine, no rescue attempts. Session 52 applied them: the 39
# confirmed edges flow through the §18 pathway
# (scripts/c11_promotions.yaml — the ONLY HUMAN_VALIDATED source; never
# this record). This batch needs NO operator_decision blocks: no RR
# settlement, no ENRICHMENT-scoped node, and every identity decision is
# KEEP_AS_IS (the authored representation stands — no merge, no split, no
# boundary re-scope). Node CONFIRMs are review state only (no §18 node
# pathway), recorded in the verdict file. This note is never emitted into
# graph/*.yaml and can never carry HUMAN_VALIDATED.
""".splitlines(keepends=True)

HEADER_ANCHOR = "# re-uses an earlier-record identity.\n"


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    text = DEC.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    # ---- pre-state assertions (fail closed BEFORE any edit) --------------
    if not VERDICTS.exists():
        die("pre-state: scripts/c11_batch3_verdicts.yaml missing — encode "
            "the verdicts first (c11_verdict_encode_batch3.py)")
    vd = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    r = vd["meta"].get("operator_ruling") or {}
    if r.get("session") != 52 or r.get("decided_by") != "operator":
        die("pre-state: verdict record does not carry the expected operator "
            "ruling (session 52)")
    if any(x["verdict"] != "CONFIRM" for x in vd["edge_verdicts"]):
        die("pre-state: an edge verdict is not CONFIRM (unexpected shape)")
    if any(x["verdict"] != "CONFIRM" for x in vd["node_verdicts"]):
        die("pre-state: a node verdict is not CONFIRM (unexpected shape)")
    if any(x["verdict"] != "KEEP_AS_IS"
           for x in vd["identity_decisions"]):
        die("pre-state: an identity decision is not KEEP_AS_IS (a "
            "MERGE/SPLIT would require §7 re-authoring this script does "
            "not implement)")

    if "operator_decision:" in text:
        die("pre-state: an operator_decision block already exists in the "
            "batch-3 decision record (double-apply?)")
    if "OPERATOR DECISIONS (session 52" in text:
        die("pre-state: the session-52 header note already exists "
            "(double-apply?)")

    dec = yaml.safe_load(text)
    if len(dec["edges"]) != 39 or len(dec["nodes"]) != 24 \
            or len(dec.get("held", [])) != 14:
        die("pre-state: unexpected batch-3 record shape (39/24/14 "
            "expected)")
    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec["edges"] + dec["nodes"]):
        die("pre-state: HUMAN_VALIDATED in the decision record "
            "(anti-forgery)")
    if any(e["validation_status"] == "REVIEW_REQUIRED"
           for e in dec["edges"]):
        die("pre-state: batch-3 authored an RR edge (record shape drift)")
    if any(sp.get("role") == "ENRICHMENT"
           for n in dec["nodes"] for sp in n.get("spec_points", [])):
        die("pre-state: an ENRICHMENT node exists in batch 3 (would need "
            "an enrichment operator_decision block)")

    # ---- edit (anchored, single insertion) --------------------------------
    if text.count(HEADER_ANCHOR) != 1:
        die("edit 1: header anchor not unique")
    idx = next(i for i, l in enumerate(lines) if l == HEADER_ANCHOR)
    lines = lines[:idx + 1] + HEADER_NOTE + lines[idx + 1:]

    # ---- post-state validation -------------------------------------------
    new_text = "".join(lines)
    dec2 = yaml.safe_load(new_text)
    if len(dec2["edges"]) != 39 or len(dec2["nodes"]) != 24 \
            or len(dec2.get("held", [])) != 14:
        die("post-state: store shape changed (39/24/14 expected)")
    if new_text.count("operator_decision:") != 0:
        die("post-state: operator_decision block appeared (none is "
            "sanctioned for batch 3 — header note only)")
    if "OPERATOR DECISIONS (session 52" not in new_text:
        die("post-state: the session-52 header note is missing")

    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec2["edges"] + dec2["nodes"]):
        die("post-state: HUMAN_VALIDATED leaked into the decision record")

    # authored fields untouched: every record must still carry the exact
    # same non-review fields as before (comments are the only permitted
    # addition — the YAML payload must be byte-equal post-reparse)
    eb = {(x["source"], x["relation"], x["target"]): x for x in dec["edges"]}
    ea = {(x["source"], x["relation"], x["target"]): x
          for x in dec2["edges"]}
    if set(eb) != set(ea) or any(eb[k] != ea[k] for k in eb):
        die("post-state: authored-edge fields drifted")
    nb = {n["code"]: n for n in dec["nodes"]}
    na = {n["code"]: n for n in dec2["nodes"]}
    if set(nb) != set(na) or any(nb[c] != na[c] for c in nb):
        die("post-state: node fields drifted")

    DEC.write_text(new_text, encoding="utf-8")
    print("APPLIED (§7 re-authoring, session 52):")
    print("  header: session-52 operator-decisions note (review state only)")
    print("  (no RR settlement block — batch 3 authored zero RR edges;")
    print("   no enrichment operator_decision block — no ENRICHMENT nodes;")
    print("   no MERGE/SPLIT re-authoring — all 7 identity decisions")
    print("   KEEP_AS_IS)")
    print("next: §18 promotion of the 39 CONFIRM edges "
          "(c11_diff_review.py export + approve -> c11_promote.py)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
