#!/usr/bin/env python3
"""T-C11 session 44 — encode the OPERATOR VERDICT SET into the operator-owned
verdict record scripts/c11_review_verdicts.yaml.

The operator authorized this exact decision set in the session-44 tasking
(2026-09-12). This script encodes it VERBATIM — no verdict invented, no
evidence reinterpreted, no ID guessed. Fail-closed:

  * refuses if any verdict field is already filled (no double-application);
  * refuses if the template rows do not reconcile 1:1 against the live store
    (31 SUGGESTED semantic edge triples / 29 node codes / 13 held entries
    with 11 HOLD + 2 REJECT / RR edge exactly GAS-VOL-CALC->AVOGADRO-LAW);
  * refuses if the live store is not in the frozen pre-verdict state
    (0 HUMAN_VALIDATED, 0 promotions).

This script WRITES ONLY scripts/c11_review_verdicts.yaml (the sanctioned
operator-owned artifact; the template's own instructions declare hand-edits
the sanctioned pathway and graph/*.yaml never hand-edited). It promotes
nothing, re-authors no decision record, and opens no §16 state.
Application of the verdicts (§18 promotion / §7 re-authoring) is a separate
explicit action for a later session.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
VERDICTS = HERE / "c11_review_verdicts.yaml"
DECISIONS = HERE / "c11_pilot_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"

SESSION = 44
TODAY = "2026-09-12"
DECIDED_BY = "operator"

# ---------------------------------------------------------------------------
# Operator decision set — VERBATIM from the session-44 tasking.
# ---------------------------------------------------------------------------
OD1_NOTE = (
    "Operator ratification (session 44, 2026-09-12): yield concepts must be "
    "split into ACTUAL_YIELD, THEORETICAL_YIELD, PERCENTAGE_YIELD — applied "
    "as the generalized ontology rule for formula-driven / multi-part "
    "specification coverage where the evidence supports distinct concepts. "
    "Maps to the existing store split: 4CH1-CON-YIELD (title 'Yield (actual "
    "yield)') / 4CH1-CON-THEOR-YIELD / 4CH1-CON-PERCENT-YIELD; nodes N-13 / "
    "N-14 / N-15 and the same-anchor operand pair E-09 / E-10 are confirmed "
    "as-is under this ruling (a future merge stays operator-only)."
)
OD2_NOTE = (
    "Operator ratification (session 44, 2026-09-12): incidental terminology "
    "/ table labels are NOT sufficient instructional evidence. A term "
    "appearing only as a table label, heading, isolated vocabulary token, or "
    "incidental terminology does not by itself establish an instructional "
    "relationship. Implicit use may remain REVIEW_REQUIRED / quarantined "
    "unless explicitly supported by substantive instructional content. Do "
    "not manufacture an edge merely because a concept is semantically "
    "related or transitively reachable."
)

# Edge verdicts: id -> (verdict, notes)
EDGE_VERDICTS = {
    **{f"E-{i:02d}": ("CONFIRM", "") for i in range(1, 32)},
    "E-08": ("HOLD", (
        "Operator HOLD (session 44, 2026-09-12): granularity problem. "
        "Evidence supports interpreting/using a balanced equation, but does "
        "not necessarily support the broader EQ-SYMBOL concept as currently "
        "modeled, particularly if that node includes writing/balancing the "
        "equation.")),
    "E-26": ("HOLD", (
        "Operator HOLD (session 44, 2026-09-12): do not promote the "
        "EXPLAINED_BY → AVOGADRO-LAW relationship merely from general "
        "scientific knowledge. The current evidence does not establish that "
        "explanatory relationship strongly enough.")),
    "E-29": ("HOLD", (
        "Operator HOLD (session 44, 2026-09-12): do not promote "
        "REMEDIATED_BY → CONSERVATION-MASS merely because conservation of "
        "mass is conceptually relevant. The source evidence does not "
        "explicitly establish that remediation relationship strongly "
        "enough.")),
}
EDGE_VERDICTS["E-09"] = ("CONFIRM", (
    "Confirmed under ratified OD-1 (yield triple stays split; the "
    "same-anchor operand pair is the expected representation)."))
EDGE_VERDICTS["E-10"] = ("CONFIRM", (
    "Confirmed under ratified OD-1 (yield triple stays split; the "
    "same-anchor operand pair is the expected representation)."))

# Node verdicts: id -> (verdict, notes); default CONFIRM, no note.
NODE_VERDICTS = {f"N-{i:02d}": ("CONFIRM", "") for i in range(1, 30)}
NODE_VERDICTS["N-08"] = ("CONFIRM", (
    "Operator enrichment note (session 44): CONFIRM as an enrichment "
    "concept. It is useful to the concept model but is not itself "
    "necessarily an explicit demanded concept in 4CH1-1.27. (Store role: "
    "ENRICHMENT @ 4CH1-1.27.) Do not convert this enrichment note into a "
    "stronger syllabus-authority claim."))
NODE_VERDICTS["N-27"] = ("CONFIRM", (
    "Operator enrichment note (session 44): CONFIRM as an enrichment "
    "concept because the corpus substantively teaches the idea, while the "
    "exact 1.35C wording does not necessarily explicitly demand the named "
    "law. (Store role: ENRICHMENT @ 4CH1-1.35C.) Do not convert this "
    "enrichment note into a stronger syllabus-authority claim."))
for nid in ("N-13", "N-14", "N-15"):
    NODE_VERDICTS[nid] = ("CONFIRM", (
        "Confirmed under ratified OD-1 (yield triple stays split)."))

ALIAS_POLICY_VERDICT = "RETRIEVAL_EXEMPT"
ALIAS_POLICY_NOTE = (
    "Operator alias policy (session 44, 2026-09-12), recorded explicitly: "
    "(1) Authoritative/evidence-backed aliases may be used where supported "
    "by the source corpus. (2) Retrieval-only synonyms/aliases must NOT be "
    "represented as corpus-evidenced terminology. (3) Unevidenced aliases "
    "must remain clearly marked as retrieval-only / unevidenced. (4) They "
    "must never be used as evidence for a graph relationship. Encoded as "
    "RETRIEVAL_EXEMPT: unevidenced aliases may remain in the store as "
    "retrieval-only entries, clearly marked, never corpus-evidenced "
    "terminology, never edge evidence (dual-track: corpus-evidenced "
    "authoritative track + marked retrieval-only track)."
)
MAX_YIELD_DISPOSITION = "KEEP"
MAX_YIELD_NOTE = (
    "Operator disposition (session 44, 2026-09-12): 'maximum yield' is NOT "
    "present in the relevant source corpus phrase evidence (0 occurrences "
    "in the pilot corpus and the full 112-note corpus — session-43 alias "
    "audit). KEEP only as a retrieval-only synonym/alias, explicitly marked "
    "retrieval-only / unevidenced. Do NOT claim that the corpus teaches or "
    "uses the phrase. Do NOT add it to evidence quotes. Do NOT alter the "
    "source note. Do NOT treat this as data corruption. Data-layer marking "
    "of the alias, if applied later, goes through §7 decision-record "
    "re-authoring and must preserve these constraints."
)
HELD_NOTE = (
    "informational only — all 13 decisions preserved; no reopening, no "
    "promotion. Operator reviewed and confirmed preservation of the "
    "appendix verbatim (session 44, 2026-09-12): HELD-01..HELD-08, "
    "HELD-10..HELD-12 HOLD; HELD-09, HELD-13 REJECT."
)

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_REVIEW_PACKAGE (session 43) — "
    "verdicts recorded by operator decision, session 44 (2026-09-12)."
)
META_INSTRUCTIONS = (
    "Fill verdict per row. Edge/node vocabulary: CONFIRM | REJECT | HOLD | "
    "MERGE | SPLIT. OD vocabulary: RATIFY | RATIFY_WITH_MODIFICATION | "
    "REJECT | DEFER. Alias policy: EVIDENCE_REQUIRED_ALL | "
    "EVIDENCE_REQUIRED_SPECIAL | RETRIEVAL_EXEMPT. Alias disposition: DROP | "
    "RE_EVIDENCE | KEEP | RENAME. Hand-edits HERE are the sanctioned "
    "pathway; graph/*.yaml are never hand-edited. The next session applies "
    "verdicts via the §18 promotion pathway / §7 decision-record "
    "re-authoring. Held appendix: informational only — no reopening, no "
    "promotion of held candidates. The verdicts below were authorized by "
    "the operator in the session-44 tasking (2026-09-12) and encoded "
    "verbatim; they are the operator decisions for this review round. They "
    "are RECORDED, not applied: no semantic edge promoted, no "
    "HUMAN_VALIDATED entry created, live promotion store empty, §16 not "
    "authorized. Changing a recorded verdict requires an explicit operator "
    "decision."
)

# ---------------------------------------------------------------------------
# Fail-closed pre-state assertions
# ---------------------------------------------------------------------------
def die(msg: str):
    print(f"FAIL-CLOSED: {msg}")
    sys.exit(1)


doc = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template missing/empty")

# 1. template must be the untouched session-43 template (no double-fill)
for section in ("od_ratifications", "edge_verdicts", "node_verdicts"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — "
                "refusing to double-apply")
if doc["alias_policy"].get("verdict"):
    die("alias_policy already filled")
if doc["alias_dispositions"][0].get("disposition"):
    die("alias_dispositions already filled")
if doc["held_appendix"].get("acknowledged"):
    die("held_appendix already acknowledged")

# 2. row-shape assertions (exact surface)
assert [r["id"] for r in doc["od_ratifications"]] == ["OD-1", "OD-2"]
assert [r["id"] for r in doc["edge_verdicts"]] == [f"E-{i:02d}" for i in range(1, 32)]
assert [r["id"] for r in doc["node_verdicts"]] == [f"N-{i:02d}" for i in range(1, 30)]
assert len(doc["alias_dispositions"]) == 1
ad = doc["alias_dispositions"][0]
assert ad["node"] == "4CH1-CON-THEOR-YIELD" and ad["alias"] == "maximum yield"

# 3. reconcile against the live store
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml").read_text(encoding="utf-8"))
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))


def triple(e):
    return f"{e['source']} {e['relation']} {e['target']}"


semantic = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
suggested = [e for e in semantic if e["validation_status"] == "SUGGESTED"]
rr = [e for e in semantic if e["validation_status"] == "REVIEW_REQUIRED"]
hv = [e for e in semantic if e["validation_status"] == "HUMAN_VALIDATED"]
tmpl_triples = [r["triple"] for r in doc["edge_verdicts"]]
graph_triples = [triple(e) for e in suggested]

assert len(nodes_doc["nodes"]) == 29, len(nodes_doc["nodes"])
assert len(semantic) == 32 and len(suggested) == 31
assert len(hv) == 0, "live store must have 0 HUMAN_VALIDATED"
assert len(rr) == 1 and triple(rr[0]) == \
    "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW", \
    "RR edge drifted"
assert not promo.get("promotions"), "promotion store must be empty"
if sorted(tmpl_triples) != sorted(graph_triples) or len(set(tmpl_triples)) != 31:
    die("edge triple mismatch between verdict template and live store")
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
graph_codes = [n["code"] for n in nodes_doc["nodes"]]
if sorted(tmpl_codes) != sorted(graph_codes) or len(set(tmpl_codes)) != 29:
    die("node code mismatch between verdict template and live store")
held = dec["held"]
assert len(held) == 13
statuses = {h["id"]: h["status"] for h in held}
expected = {f"HELD-{i:02d}": "held" for i in range(1, 14)}
expected["HELD-09"] = "rejected"
expected["HELD-13"] = "rejected"
assert statuses == expected, "held appendix drifted from 11 HOLD + 2 REJECT"

# 4. the operator's decision set must have exact shape before encoding
assert sum(1 for v, _ in EDGE_VERDICTS.values() if v == "CONFIRM") == 28
assert sum(1 for v, _ in EDGE_VERDICTS.values() if v == "HOLD") == 3
assert {k for k, (v, _) in EDGE_VERDICTS.items() if v == "HOLD"} == \
    {"E-08", "E-26", "E-29"}
assert all(v == "CONFIRM" for v, _ in NODE_VERDICTS.values())

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved; OD rows gain decided_by)
# ---------------------------------------------------------------------------
doc["meta"]["stage"] = "operator-verdicts"
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["instructions"] = META_INSTRUCTIONS

for row in doc["od_ratifications"]:
    row["verdict"] = "RATIFY"
    row["notes"] = OD1_NOTE if row["id"] == "OD-1" else OD2_NOTE
    row["decided_by"] = DECIDED_BY
    # rebuild to keep key order: id, question, verdict, notes, decided_by, decided_date
    ordered = {"id": row["id"], "question": row["question"],
               "verdict": row["verdict"], "notes": row["notes"],
               "decided_by": row["decided_by"], "decided_date": TODAY}
    row.clear()
    row.update(ordered)

for row in doc["edge_verdicts"]:
    v, n = EDGE_VERDICTS[row["id"]]
    row["verdict"] = v
    row["notes"] = n

for row in doc["node_verdicts"]:
    v, n = NODE_VERDICTS[row["id"]]
    row["verdict"] = v
    row["notes"] = n

doc["alias_policy"]["verdict"] = ALIAS_POLICY_VERDICT
doc["alias_policy"]["notes"] = ALIAS_POLICY_NOTE

doc["alias_dispositions"][0]["disposition"] = MAX_YIELD_DISPOSITION
doc["alias_dispositions"][0]["notes"] = MAX_YIELD_NOTE

doc["held_appendix"]["acknowledged"] = True
doc["held_appendix"]["note"] = HELD_NOTE

header = (
    "# T-C11 operator review verdicts — session 43 package, FILLED by "
    "operator decision session 44 (2026-09-12). OPERATOR-OWNED.\n"
    "# Vocabulary and pathway: see the meta.instructions block.\n"
    "# Verdicts are RECORDED, not applied: no promotion, no HUMAN_VALIDATED, "
    "no §16.\n"
)
VERDICTS.write_text(
    header + yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100),
    encoding="utf-8")

# ---------------------------------------------------------------------------
# Post-write verification (re-parse + counts)
# ---------------------------------------------------------------------------
chk = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
ec = {}
for r in chk["edge_verdicts"]:
    ec[r["verdict"]] = ec.get(r["verdict"], 0) + 1
nc = {}
for r in chk["node_verdicts"]:
    nc[r["verdict"]] = nc.get(r["verdict"], 0) + 1

assert [r["verdict"] for r in chk["od_ratifications"]] == ["RATIFY", "RATIFY"]
assert ec == {"CONFIRM": 28, "HOLD": 3}, ec
assert nc == {"CONFIRM": 29}, nc
assert chk["alias_policy"]["verdict"] == "RETRIEVAL_EXEMPT"
assert chk["alias_dispositions"][0]["disposition"] == "KEEP"
assert chk["held_appendix"]["acknowledged"] is True
hold_ids = [r["id"] for r in chk["edge_verdicts"] if r["verdict"] == "HOLD"]
assert hold_ids == ["E-08", "E-26", "E-29"], hold_ids

print("wrote", VERDICTS)
print("OD ratifications: OD-1 RATIFY, OD-2 RATIFY (decided_by operator, "
      f"decided_date {TODAY})")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print(f"HOLD edges: {hold_ids}")
print("alias_policy: RETRIEVAL_EXEMPT; maximum yield: KEEP "
      "(retrieval-only / unevidenced)")
print("held_appendix: acknowledged (13 preserved: 11 HOLD + 2 REJECT)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
