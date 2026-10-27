#!/usr/bin/env python3
"""
T-C11 session 50 — c11_verdict_apply_batch2.py: §7 decision-record
re-authoring that applies the operator's session-50 batch-2 verdicts
(scripts/c11_batch2_verdicts.yaml, ruling "CONFIRM all") to the REVIEW-STATE
layer of scripts/c11_batch2_decisions.yaml.

Scope (the §7 sanctioned re-authoring pathway — session-45/48 precedent):
  * B2-N-08 (4CH1-CON-METALLOID): enrichment-scoping operator_decision
    CONFIRM block (the pilot N-08/N-27 + batch-1 B1-N-08/B1-N-11 pattern).
  * header note recording the session-50 verdict round + application.

The 23 edge CONFIRM verdicts need NO §7 block: they flow through the §18
promotion pathway (c11_diff_review.py approve -> c11_promote.py -> gated
G13 re-run), exactly as the pilot's 28 and batch-1's 28 CONFIRM edges did
in sessions 45 and 48. The 4 KEEP_AS_IS identity decisions need no
re-authoring (the authored representation stands — in particular B2-ID-01
means NO Ar-boundary re-scope). This batch authored NO REVIEW_REQUIRED
edge, so no RR settlement block arises.

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
DEC = HERE / "c11_batch2_decisions.yaml"
VERDICTS = HERE / "c11_batch2_verdicts.yaml"

N08 = "4CH1-CON-METALLOID"


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def _ends_block(l: str) -> bool:
    s = l.strip()
    return bool(s) and (l.startswith("- ") or l.startswith("#")
                        or not l.startswith(" "))


def find_node_block(lines: list, code: str):
    for i, l in enumerate(lines):
        if l.rstrip("\n") == f"- code: {code}":
            j = i + 1
            while j < len(lines) and not _ends_block(lines[j]):
                j += 1
            return i, j
    die(f"node block not found: {code}")


# --- the new operator_decision block (session-50 decision, applied
#     session 50 via §7; review state only — never emitted to graph/*.yaml) ---

OD_N08 = """  operator_decision:
    verdict: CONFIRM
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_batch2_verdicts.yaml (session 50, row B2-N-08)'
    reasons:
    - 'CONFIRM as an enrichment concept: the 1.21 wording demands a binary metal/non-metal identification, while the mapped note names and teaches the boundary class (semi-metal / metalloid) as an examiner tip.'
    note: 'Operator enrichment scoping (session 50, 2026-09-12, ruling "CONFIRM all"): the node keeps its ENRICHMENT role @ 4CH1-1.21 (the pilot N-08/N-27 and batch-1 B1-N-08/B1-N-11 leaf pattern; no authored edges). Do NOT convert this enrichment note into a stronger syllabus-authority claim. Node confirmation is review state only (nodes have no §18 promotion pathway) and this block is never emitted into graph/*.yaml. Applied session 50 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

HEADER_NOTE = """
#
# OPERATOR DECISIONS (session 50, applied session 50, 2026-09-12): the
# operator's batch-2 verdicts live in scripts/c11_batch2_verdicts.yaml
# (operator-owned; ruling verbatim "CONFIRM all"): 23 edge CONFIRM /
# 0 HOLD / 0 REJECT; 14 node CONFIRM; 4 identity decisions KEEP_AS_IS;
# no RR settlement (this batch authored no REVIEW_REQUIRED edge); the
# held appendix (10) acknowledged. Session 50 applied them: the 23
# confirmed edges flow through the §18 pathway (scripts/c11_promotions.yaml
# — the ONLY HUMAN_VALIDATED source; never this record); the B2-N-08
# enrichment scoping is recorded below as an operator_decision block.
# Node CONFIRMs are review state only (no §18 node pathway). These blocks
# are never emitted into graph/*.yaml and can never carry HUMAN_VALIDATED.
""".splitlines(keepends=True)

HEADER_ANCHOR = "# earlier-record identity.\n"


def main() -> int:
    text = DEC.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    # ---- pre-state assertions (fail closed BEFORE any edit) --------------
    if not VERDICTS.exists():
        die("pre-state: scripts/c11_batch2_verdicts.yaml missing — encode "
            "the verdicts first (c11_verdict_encode_batch2.py)")
    vd = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    if vd["meta"]["operator_ruling"]["statement"] != "CONFIRM all":
        die("pre-state: verdict record does not carry the expected operator "
            "ruling")
    n08_row = next(r for r in vd["node_verdicts"] if r["id"] == "B2-N-08")
    if n08_row["verdict"] != "CONFIRM":
        die("pre-state: B2-N-08 verdict is not CONFIRM")
    if any(r["verdict"] != "CONFIRM" for r in vd["edge_verdicts"]):
        die("pre-state: an edge verdict is not CONFIRM (unexpected shape)")

    if "operator_decision:" in text:
        die("pre-state: an operator_decision block already exists in the "
            "batch-2 decision record (double-apply?)")

    dec = yaml.safe_load(text)
    if len(dec["edges"]) != 23 or len(dec["nodes"]) != 14 \
            or len(dec.get("held", [])) != 10:
        die("pre-state: unexpected batch-2 record shape (23/14/10 expected)")
    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec["edges"] + dec["nodes"]):
        die("pre-state: HUMAN_VALIDATED in the decision record "
            "(anti-forgery)")
    if any(e["validation_status"] == "REVIEW_REQUIRED"
           for e in dec["edges"]):
        die("pre-state: batch-2 authored an RR edge (record shape drift)")

    s, e = find_node_block(lines, N08)
    if not any(l.rstrip("\n") == "  validation_status: SUGGESTED"
               for l in lines[s:e]):
        die("pre-state: node CON-METALLOID is not SUGGESTED")
    if not any(l.rstrip("\n") == "    role: ENRICHMENT"
               for l in lines[s:e]):
        die("pre-state: node CON-METALLOID does not carry the ENRICHMENT "
            "role")

    # ---- edits (bottom-up so line indexes stay valid) --------------------
    # 1. B2-N-08 enrichment block
    s, e = find_node_block(lines, N08)
    lines = lines[:e] + OD_N08 + lines[e:]

    # 2. header note
    if text.count(HEADER_ANCHOR) != 1:
        die("edit 2: header anchor not unique")
    idx = next(i for i, l in enumerate(lines) if l == HEADER_ANCHOR)
    lines = lines[:idx + 1] + HEADER_NOTE + lines[idx + 1:]

    # ---- post-state validation -------------------------------------------
    new_text = "".join(lines)
    dec2 = yaml.safe_load(new_text)
    if len(dec2["edges"]) != 23 or len(dec2["nodes"]) != 14 \
            or len(dec2.get("held", [])) != 10:
        die("post-state: store shape changed (23/14/10 expected)")
    if new_text.count("  operator_decision:") != 1:
        die("post-state: expected exactly 1 operator_decision block, "
            f"found {new_text.count('  operator_decision:')}")

    def node_od(code):
        return next(n["operator_decision"] for n in dec2["nodes"]
                    if n["code"] == code)

    checks = [
        (node_od(N08)["verdict"] == "CONFIRM", "B2-N-08 CONFIRM enrichment"),
        (node_od(N08)["decided_by"] == "operator"
         and node_od(N08)["decided_date"] == "2026-09-12",
         "B2-N-08 attribution"),
        ("ENRICHMENT" in node_od(N08).get("note", ""),
         "B2-N-08 enrichment scoping preserved"),
    ]
    for ok, name in checks:
        if not ok:
            die(f"post-state: {name} failed")

    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec2["edges"] + dec2["nodes"]):
        die("post-state: HUMAN_VALIDATED leaked into the decision record")

    # authored fields untouched: every record must still carry the exact
    # same non-review fields as before (operator_decision is the only
    # permitted addition)
    eb = {(x["source"], x["relation"], x["target"]): x for x in dec["edges"]}
    ea = {(x["source"], x["relation"], x["target"]): x
          for x in dec2["edges"]}
    if set(eb) != set(ea) or any(eb[k] != ea[k] for k in eb):
        die("post-state: authored-edge fields drifted")
    nb = {n["code"]: n for n in dec["nodes"]}
    na = {n["code"]: {k: v for k, v in n.items() if k != "operator_decision"}
          for n in dec2["nodes"]}
    if any(nb[c] != na[c] for c in nb):
        die("post-state: node non-review fields drifted")

    DEC.write_text(new_text, encoding="utf-8")
    print("APPLIED (§7 re-authoring, session 50):")
    print("  B2-N-08 operator_decision CONFIRM (enrichment scoping)")
    print("  header: session-50 operator-decisions note")
    print("  (no RR settlement block — batch 2 authored zero RR edges; "
          "the 4 KEEP_AS_IS identity decisions needed no re-authoring)")
    print("next: §18 promotion of the 23 CONFIRM edges "
          "(c11_diff_review.py export + approve -> c11_promote.py)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
