#!/usr/bin/env python3
"""
T-C11 session 48 — c11_verdict_apply_batch1.py: §7 decision-record
re-authoring that applies the operator's session-48 batch-1 verdicts
(scripts/c11_batch1_verdicts.yaml, ruling "CONFIRM all") to the REVIEW-STATE
layer of scripts/c11_batch1_decisions.yaml.

Scope (the §7 sanctioned re-authoring pathway — session-45 precedent):
  * RR edge (CRYSTALLISATION REQUIRES_PREREQUISITE SOLUTION): new
    operator_decision block recording the HOLD_REVIEW_REQUIRED settlement
    (the authored quarantine is confirmed; stays REVIEW_REQUIRED, not
    promotable).
  * B1-N-08 (CON-EVAPORATION-BOILING): enrichment-scoping operator_decision
    CONFIRM block (the pilot N-27 pattern).
  * B1-N-11 (CON-HEATING-CONSTANT-MASS): enrichment-scoping
    operator_decision CONFIRM block (the pilot N-08 pattern).
  * header note recording the session-48 verdict round + application.

The 28 edge CONFIRM verdicts need NO §7 block: they flow through the §18
promotion pathway (c11_diff_review.py approve -> c11_promote.py -> gated
G13 re-run), exactly as the pilot's 28 CONFIRM edges did in session 45.
The 4 KEEP_AS_IS identity decisions need no re-authoring (the authored
representation stands).

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
DEC = HERE / "c11_batch1_decisions.yaml"
VERDICTS = HERE / "c11_batch1_verdicts.yaml"

RR = ("4CH1-CON-CRYSTALLISATION", "REQUIRES_PREREQUISITE",
      "4CH1-CON-SOLUTION")
N08 = "4CH1-CON-EVAPORATION-BOILING"
N11 = "4CH1-CON-HEATING-CONSTANT-MASS"


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def _ends_block(l: str) -> bool:
    s = l.strip()
    return bool(s) and (l.startswith("- ") or l.startswith("#")
                        or not l.startswith(" "))


def find_edge_block(lines: list, src: str, rel: str, tgt: str):
    for i, l in enumerate(lines):
        if (l.rstrip("\n") == f"- source: {src}"
                and lines[i + 1].rstrip("\n") == f"  relation: {rel}"
                and lines[i + 2].rstrip("\n") == f"  target: {tgt}"):
            j = i + 1
            while j < len(lines) and not _ends_block(lines[j]):
                j += 1
            return i, j
    die(f"edge block not found: {src} {rel} {tgt}")


def find_node_block(lines: list, code: str):
    for i, l in enumerate(lines):
        if l.rstrip("\n") == f"- code: {code}":
            j = i + 1
            while j < len(lines) and not _ends_block(lines[j]):
                j += 1
            return i, j
    die(f"node block not found: {code}")


def block_has_od(lines: list, start: int, end: int) -> bool:
    return any(l.rstrip("\n") == "  operator_decision:"
               for l in lines[start:end])


# --- the new operator_decision blocks (session-48 decisions, applied
#     session 48 via §7; review state only — never emitted to graph/*.yaml) ---

OD_RR = """  operator_decision:
    verdict: HOLD_REVIEW_REQUIRED
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_batch1_verdicts.yaml (session 48, row B1-RR-01)'
    reasons:
    - 'Subsumption: the dependency is transitively covered via CRYSTALLISATION -> SATURATED-SOLUTION -> SOLUTION; the load-bearing prerequisite (saturation) is already emitted.'
    - 'Pass-1 self-quarantined the edge to REVIEW_REQUIRED at authoring; pass-2 concordantly HOLD.'
    note: 'Operator RR settlement (session 48, 2026-09-12, ruling "CONFIRM all"): the authored quarantine is confirmed — HOLD_REVIEW_REQUIRED. The edge stays REVIEW_REQUIRED in the graph and is NOT eligible for promotion. Applied session 48 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

OD_N08 = """  operator_decision:
    verdict: CONFIRM
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_batch1_verdicts.yaml (session 48, row B1-N-08)'
    reasons:
    - 'CONFIRM as an enrichment concept: the corpus substantively teaches the boiling-vs-evaporation distinction, while the 1.2 wording names the interconversions without demanding it.'
    note: 'Operator enrichment scoping (session 48, 2026-09-12, ruling "CONFIRM all"): the node keeps its ENRICHMENT role @ 4CH1-1.2 (the pilot N-27 pattern). Do NOT convert this enrichment note into a stronger syllabus-authority claim. Node confirmation is review state only (nodes have no §18 promotion pathway) and this block is never emitted into graph/*.yaml. Applied session 48 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

OD_N11 = """  operator_decision:
    verdict: CONFIRM
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_batch1_verdicts.yaml (session 48, row B1-N-11)'
    reasons:
    - 'CONFIRM as an enrichment concept: a named technique taught as a method step + examiner tip, not demanded by the 1.7C wording.'
    note: 'Operator enrichment scoping (session 48, 2026-09-12, ruling "CONFIRM all"): the node keeps its ENRICHMENT role @ 4CH1-1.7C (the pilot N-08 leaf pattern; no authored edges). Do NOT convert this enrichment note into a stronger syllabus-authority claim. Node confirmation is review state only (nodes have no §18 promotion pathway) and this block is never emitted into graph/*.yaml. Applied session 48 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

HEADER_NOTE = """
#
# OPERATOR DECISIONS (session 48, applied session 48, 2026-09-12): the
# operator's batch-1 verdicts live in scripts/c11_batch1_verdicts.yaml
# (operator-owned; ruling verbatim "CONFIRM all"): 28 edge CONFIRM /
# 0 HOLD / 0 REJECT; 24 node CONFIRM; 4 identity decisions KEEP_AS_IS;
# RR settlement HOLD_REVIEW_REQUIRED; held appendix acknowledged. Session
# 48 applied them: the 28 confirmed edges flow through the §18 pathway
# (scripts/c11_promotions.yaml — the ONLY HUMAN_VALIDATED source; never
# this record); the RR settlement and the B1-N-08/B1-N-11 enrichment
# scoping are recorded below as operator_decision blocks. Node CONFIRMs
# are review state only (no §18 node pathway). These blocks are never
# emitted into graph/*.yaml and can never carry HUMAN_VALIDATED.
""".splitlines(keepends=True)

HEADER_ANCHOR = "# node attaches to 4.15; no batch-1 edge re-uses a pilot identity.\n"


def main() -> int:
    text = DEC.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    # ---- pre-state assertions (fail closed BEFORE any edit) --------------
    if not VERDICTS.exists():
        die("pre-state: scripts/c11_batch1_verdicts.yaml missing — encode "
            "the verdicts first (c11_verdict_encode_batch1.py)")
    vd = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    if vd["meta"]["operator_ruling"]["statement"] != "CONFIRM all":
        die("pre-state: verdict record does not carry the expected operator "
            "ruling")
    rr_row = next(r for r in vd["rr_settlement"] if r["id"] == "B1-RR-01")
    if rr_row["verdict"] != "HOLD_REVIEW_REQUIRED":
        die("pre-state: RR settlement is not HOLD_REVIEW_REQUIRED")
    for row in vd["node_verdicts"]:
        if row["id"] == "B1-N-08" and row["verdict"] != "CONFIRM":
            die("pre-state: B1-N-08 verdict is not CONFIRM")
        if row["id"] == "B1-N-11" and row["verdict"] != "CONFIRM":
            die("pre-state: B1-N-11 verdict is not CONFIRM")

    if "operator_decision:" in text:
        die("pre-state: an operator_decision block already exists in the "
            "batch-1 decision record (double-apply?)")

    dec = yaml.safe_load(text)
    if len(dec["edges"]) != 29 or len(dec["nodes"]) != 24 \
            or len(dec.get("held", [])) != 12:
        die("pre-state: unexpected batch-1 record shape (29/24/12 expected)")
    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec["edges"] + dec["nodes"]):
        die("pre-state: HUMAN_VALIDATED in the decision record "
            "(anti-forgery)")

    s, e = find_edge_block(lines, *RR)
    if not any(l.rstrip("\n") == "  validation_status: REVIEW_REQUIRED"
               for l in lines[s:e]):
        die("pre-state: the RR edge is not REVIEW_REQUIRED")
    for code in (N08, N11):
        s, e = find_node_block(lines, code)
        if not any(l.rstrip("\n") == "  validation_status: SUGGESTED"
                   for l in lines[s:e]):
            die(f"pre-state: node {code} is not SUGGESTED")
        if not any(l.rstrip("\n") == "    role: ENRICHMENT"
                   for l in lines[s:e]):
            die(f"pre-state: node {code} does not carry the ENRICHMENT role")

    # ---- edits (bottom-up so line indexes stay valid) --------------------
    # 1. RR settlement block
    s, e = find_edge_block(lines, *RR)
    lines = lines[:e] + OD_RR + lines[e:]

    # 2. B1-N-11 enrichment block
    s, e = find_node_block(lines, N11)
    lines = lines[:e] + OD_N11 + lines[e:]

    # 3. B1-N-08 enrichment block
    s, e = find_node_block(lines, N08)
    lines = lines[:e] + OD_N08 + lines[e:]

    # 4. header note
    if text.count(HEADER_ANCHOR) != 1:
        die("edit 4: header anchor not unique")
    idx = next(i for i, l in enumerate(lines) if l == HEADER_ANCHOR)
    lines = lines[:idx + 1] + HEADER_NOTE + lines[idx + 1:]

    # ---- post-state validation -------------------------------------------
    new_text = "".join(lines)
    dec2 = yaml.safe_load(new_text)
    if len(dec2["edges"]) != 29 or len(dec2["nodes"]) != 24 \
            or len(dec2.get("held", [])) != 12:
        die("post-state: store shape changed (29/24/12 expected)")
    if new_text.count("  operator_decision:") != 3:
        die("post-state: expected exactly 3 operator_decision blocks, "
            f"found {new_text.count('  operator_decision:')}")

    def edge_od(src, rel, tgt):
        return next(e_["operator_decision"] for e_ in dec2["edges"]
                    if (e_["source"], e_["relation"], e_["target"])
                    == (src, rel, tgt))

    def node_od(code):
        return next(n["operator_decision"] for n in dec2["nodes"]
                    if n["code"] == code)

    checks = [
        (edge_od(*RR)["verdict"] == "HOLD_REVIEW_REQUIRED",
         "RR settlement HOLD_REVIEW_REQUIRED"),
        (edge_od(*RR)["decided_by"] == "operator"
         and edge_od(*RR)["decided_date"] == "2026-09-12",
         "RR settlement attribution"),
        (node_od(N08)["verdict"] == "CONFIRM", "B1-N-08 CONFIRM enrichment"),
        (node_od(N11)["verdict"] == "CONFIRM", "B1-N-11 CONFIRM enrichment"),
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
    key = lambda e: (e["source"], e["relation"], e["target"])
    strip = lambda e: {k: v for k, v in e.items() if k != "operator_decision"}
    before = {key(e): strip(e) for e in dec["edges"]}
    after = {key(e): strip(e) for e in dec2["edges"]}
    if before != after:
        die("post-state: authored-edge non-review fields drifted")
    nb = {n["code"]: {k: v for k, v in n.items() if k != "operator_decision"}
          for n in dec["nodes"]}
    na = {n["code"]: {k: v for k, v in n.items() if k != "operator_decision"}
          for n in dec2["nodes"]}
    if nb != na:
        die("post-state: node non-review fields drifted")

    DEC.write_text(new_text, encoding="utf-8")
    print("APPLIED (§7 re-authoring, session 48):")
    print("  RR     operator_decision HOLD_REVIEW_REQUIRED (settlement, "
          "B1-RR-01)")
    print("  B1-N-08 operator_decision CONFIRM (enrichment scoping)")
    print("  B1-N-11 operator_decision CONFIRM (enrichment scoping)")
    print("  header: session-48 operator-decisions note")
    print("next: §18 promotion of the 28 CONFIRM edges "
          "(c11_diff_review.py export + approve -> c11_promote.py)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
