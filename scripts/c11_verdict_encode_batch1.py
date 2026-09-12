#!/usr/bin/env python3
"""T-C11 session 48 — encode the OPERATOR VERDICT SET for §16 batch 1 into
the operator-owned verdict record scripts/c11_batch1_verdicts.yaml.

The operator ruled on the batch-1 gate (review sheet
graph/reports/C11_BATCH1_REVIEW_SHEET.md, session-47 package) with the
verbatim ruling "CONFIRM all" (session-48 tasking, 2026-09-12). This script
encodes it VERBATIM — no verdict invented, no evidence reinterpreted, no ID
guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses if the template rows do not reconcile 1:1 against the batch-1
    decision record (28 SUGGESTED edge triples / 1 RR triple / 24 node
    codes / 12 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (28 pilot HUMAN_VALIDATED = the pilot §18 promotions; 0 batch-1
    promotions; §16 authorization AUTHORIZED; pilot HOLDs + RR frozen).

Ruling mapping (recorded verbatim in the file's operator_ruling block):
  * every edge row          -> CONFIRM
  * every node row          -> CONFIRM (B1-N-08/B1-N-11 keep ENRICHMENT
    scoping; never silently syllabus-authority)
  * every identity decision -> KEEP_AS_IS (confirm the authored
    representation — no merge, no split, no symmetric-pair re-emission;
    the identity-decision vocabulary has no CONFIRM value)
  * the RR settlement       -> HOLD_REVIEW_REQUIRED (confirm the authored
    quarantine: pass-1 self-quarantine + pass-2 concordant HOLD — the
    fail-closed direction; the RR vocabulary has no CONFIRM value)
  * held appendix           -> acknowledged (no reopening, no promotion)

This script WRITES ONLY scripts/c11_batch1_verdicts.yaml (and removes the
now-renamed template, per the sheet's gate pathway). It promotes nothing
and re-authors no decision record; application (§18 promotion / §7
re-authoring) is the separate sanctioned step in this same session.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
TEMPLATE = HERE / "c11_batch1_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch1_verdicts.yaml"
DECISIONS = HERE / "c11_batch1_decisions.yaml"
PILOT_DECISIONS = HERE / "c11_pilot_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"

SESSION = 48
TODAY = "2026-09-12"
OPERATOR_STATEMENT = "CONFIRM all"  # verbatim, session-48 tasking

# ---------------------------------------------------------------------------
# Ruling notes (factual context per flagged row; verdicts all per the mapping)
# ---------------------------------------------------------------------------
EDGE_NOTES = {
    "B1-E-07": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "the causal evidence class stands (EXPLAINED_BY; the prerequisite "
        "reading stays parked in held B1-H-04: one relation per pair)."),
    "B1-E-10": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "vocabulary-level solution link kept (FP-B1-4; filtration's only "
        "solution link, not transitively subsumed)."),
    "B1-E-12": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "chain representative kept (ID-04 KEEP_AS_IS; B1-H-01 stays held)."),
    "B1-E-13": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "chain representative kept (ID-04 KEEP_AS_IS; B1-H-10 stays held)."),
    "B1-E-17": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "vocabulary-level solution link kept (FP-B1-4; simple distillation's "
        "only solution link, not transitively subsumed)."),
    "B1-E-22": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "the edge depends on ID-01 KEEP_AS_IS (states classification and "
        "particle model stay separate nodes)."),
    "B1-E-25": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "remediation target equals the WAP target; kept for "
        "misconception-recommendation queries (node remediation_evidence "
        "also carries the corrective text)."),
}
NODE_NOTES = {
    "B1-N-08": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as "
        "ENRICHMENT-scoped (mirrors the pilot N-27 pattern). Do not convert "
        "this enrichment scoping into a stronger syllabus-authority claim."),
    "B1-N-11": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as "
        "ENRICHMENT-scoped (mirrors the pilot N-08 pattern; leaf node, no "
        "authored edges). Do not convert this enrichment scoping into a "
        "stronger syllabus-authority claim."),
    "B1-N-13": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "definition + fixed melting/boiling criterion stay one node "
        "(ID-03 KEEP_AS_IS)."),
    "B1-N-19": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "the solute/solvent/solution triple stays one node "
        "(ID-02 KEEP_AS_IS)."),
    "B1-N-22": (
        "Operator ruling 'CONFIRM all' (session 48): CONFIRM as authored — "
        "separate from CON-STATE-PARTICLE-MODEL (ID-01 KEEP_AS_IS)."),
}
ID_NOTES = {
    "B1-ID-01": (
        "Operator ruling 'CONFIRM all' (session 48): KEEP_AS_IS — the "
        "states-classification and particle-model nodes stay separate; "
        "B1-E-22 / B1-N-22 confirmed as authored."),
    "B1-ID-02": (
        "Operator ruling 'CONFIRM all' (session 48): KEEP_AS_IS — the "
        "solution triple stays one node; B1-N-19 confirmed as authored."),
    "B1-ID-03": (
        "Operator ruling 'CONFIRM all' (session 48): KEEP_AS_IS — the "
        "definition and the fixed-point criterion stay one node; B1-N-13 "
        "confirmed as authored."),
    "B1-ID-04": (
        "Operator ruling 'CONFIRM all' (session 48): KEEP_AS_IS — the chain "
        "representatives stay; the symmetric operand pairs stay held "
        "(B1-H-01 / B1-H-10); B1-E-12 / B1-E-13 confirmed as authored."),
}
RR_NOTE = (
    "Operator ruling 'CONFIRM all' (session 48): HOLD_REVIEW_REQUIRED — the "
    "authored quarantine is confirmed (subsumption via CRYSTALLISATION -> "
    "SATURATED-SOLUTION -> SOLUTION; pass-1 self-quarantine + pass-2 "
    "concordant HOLD). The edge stays REVIEW_REQUIRED and is not promotable.")
HELD_NOTE = (
    "Operator ruling 'CONFIRM all' (session 48): the 12 held candidates "
    "(B1-H-01..12) stay held — no reopening, no promotion.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH1_REVIEW_SHEET (session 47 "
    "package) — verdicts recorded by operator decision, session 48 "
    "(2026-09-12).")
META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "mapping": (
        "The ruling confirms the authored batch-1 package as presented on "
        "the session-47 review sheet: every edge row CONFIRM, every node "
        "row CONFIRM (B1-N-08/B1-N-11 keep their ENRICHMENT scoping), each "
        "identity decision KEEP_AS_IS (the authored representation "
        "confirmed as-is — no merge, no split, no symmetric-pair "
        "re-emission), the RR settlement confirms the authored quarantine "
        "(HOLD_REVIEW_REQUIRED — stays REVIEW_REQUIRED, not promotable), "
        "and the held appendix stays held. Verdicts recorded session 48; "
        "the application state lives in scripts/c11_promotions.yaml (the "
        "§18 pathway is the only HUMAN_VALIDATED source) and in the §7 "
        "decision-record re-authoring — this file never carries promotion "
        "payload or promoted status. Changing a recorded verdict requires "
        "an explicit operator decision."),
}


def die(msg: str):
    print(f"FAIL-CLOSED: {msg}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Load + pre-state assertions
# ---------------------------------------------------------------------------
if VERDICTS.exists():
    die("scripts/c11_batch1_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch1_verdicts_template.yaml missing — the "
        "session-47 package must be intact")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
for row in doc["rr_settlement"]:
    if row.get("verdict"):
        die(f"rr_settlement {row['id']} already has a verdict — refusing")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-47 surface)
assert [r["id"] for r in doc["edge_verdicts"]] == \
    [f"B1-E-{i:02d}" for i in range(1, 29)]
assert [r["id"] for r in doc["node_verdicts"]] == \
    [f"B1-N-{i:02d}" for i in range(1, 23)] + ["B1-M-01", "B1-M-02"]
assert [r["id"] for r in doc["identity_decisions"]] == \
    [f"B1-ID-{i:02d}" for i in range(1, 5)]
assert [r["id"] for r in doc["rr_settlement"]] == ["B1-RR-01"]

# 3. reconcile against the batch-1 decision record + the live store
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml").read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
auth = yaml.safe_load(S16_AUTH.read_text(encoding="utf-8"))


def triple(e):
    return f"{e['source']} {e['relation']} {e['target']}"


b_edges = dec["edges"]
b_suggested = [triple(e) for e in b_edges
               if e["validation_status"] == "SUGGESTED"]
b_rr = [triple(e) for e in b_edges
        if e["validation_status"] == "REVIEW_REQUIRED"]
tmpl_triples = [r["triple"] for r in doc["edge_verdicts"]]
assert len(b_edges) == 29, len(b_edges)
assert len(b_suggested) == 28 and len(b_rr) == 1
if sorted(tmpl_triples) != sorted(b_suggested) \
        or len(set(tmpl_triples)) != 28:
    die("edge triple mismatch between verdict template and the batch-1 "
        "decision record")
if doc["rr_settlement"][0]["triple"] != b_rr[0]:
    die("RR triple mismatch between verdict template and the batch-1 "
        "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
if sorted(tmpl_codes) != sorted(b_codes) or len(set(tmpl_codes)) != 24:
    die("node code mismatch between verdict template and the batch-1 "
        "decision record")
assert len(dec["held"]) == 12, len(dec["held"])

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
if len(hv) != 28 or hv != store_triples:
    die("live HUMAN_VALIDATED set != the 28 pilot §18 promotions (pilot "
        "state must be frozen before recording batch-1 verdicts)")
if hv & set(b_suggested):
    die("a batch-1 edge is already HUMAN_VALIDATED — pre-verdict state "
        "violated")
rr_live = {triple(e) for e in sem
           if e["validation_status"] == "REVIEW_REQUIRED"}
if b_rr[0] not in rr_live:
    die("the batch-1 RR edge is not REVIEW_REQUIRED in the live store")
if auth.get("authorization", {}).get("decision") != "AUTHORIZED":
    die("§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
if any(p.get("validated_by") != "operator" for p in promo["promotions"]):
    die("pilot promotions carry non-operator attribution (anti-forgery)")
assert len(nodes_doc["nodes"]) == 53, len(nodes_doc["nodes"])

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

for row in doc["edge_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = EDGE_NOTES.get(row["id"], "")
for row in doc["rr_settlement"]:
    row["verdict"] = "HOLD_REVIEW_REQUIRED"
    row["notes"] = RR_NOTE
for row in doc["node_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = NODE_NOTES.get(row["id"], "")
for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = ID_NOTES[row["id"]]
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 1 — OPERATOR verdict record (session-47 package), "
    "FILLED by operator decision session 48 (2026-09-12). OPERATOR-OWNED.\n"
    "# Ruling verbatim: \"CONFIRM all\" — see meta.operator_ruling for the "
    "recorded mapping.\n"
    "# Vocabulary and pathway: see the meta.instructions block. Verdicts are "
    "RECORDED; the application state lives in scripts/c11_promotions.yaml "
    "(§18) and the decision record's §7 blocks — never here.\n"
)
VERDICTS.write_text(
    header + yaml.safe_dump(doc, sort_keys=False, allow_unicode=True,
                            width=100),
    encoding="utf-8")
TEMPLATE.unlink()  # the sheet's gate pathway: fill + RENAME

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

assert ec == {"CONFIRM": 28}, ec
assert nc == {"CONFIRM": 24}, nc
assert [r["verdict"] for r in chk["identity_decisions"]] == \
    ["KEEP_AS_IS"] * 4
assert chk["rr_settlement"][0]["verdict"] == "HOLD_REVIEW_REQUIRED"
assert chk["held_appendix_acknowledgment"]["acknowledged"] is True
assert chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT
assert not TEMPLATE.exists()

print("wrote", VERDICTS)
print(f"operator ruling (verbatim): {OPERATOR_STATEMENT!r} "
      f"(decided_by operator, {TODAY})")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 4 x KEEP_AS_IS")
print("RR settlement B1-RR-01: HOLD_REVIEW_REQUIRED (quarantine confirmed)")
print("held_appendix: acknowledged (12 preserved, no reopening)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
