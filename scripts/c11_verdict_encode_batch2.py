#!/usr/bin/env python3
"""T-C11 session 50 — encode the OPERATOR VERDICT SET for §16 batch 2 into
the operator-owned verdict record scripts/c11_batch2_verdicts.yaml.

The operator ruled on the batch-2 gate (review sheet
graph/reports/C11_BATCH2_REVIEW_SHEET.md, session-49 package) with the
verbatim ruling "CONFIRM all" (session-50 tasking, 2026-09-12). This script
encodes it VERBATIM — no verdict invented, no evidence reinterpreted, no ID
guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses if the template rows do not reconcile 1:1 against the batch-2
    decision record (23 SUGGESTED edge triples / ZERO RR triples / 14 node
    codes / 10 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (56 HUMAN_VALIDATED = the 28 pilot + 28 batch-1 §18 promotions; 0
    batch-2 promotions; §16 authorization AUTHORIZED; pilot HOLDs + both
    RR settlements frozen).

Ruling mapping (recorded verbatim in the file's operator_ruling block):
  * every edge row          -> CONFIRM
  * every node row          -> CONFIRM (B2-N-08 keeps its ENRICHMENT
    scoping; never silently syllabus-authority)
  * every identity decision -> KEEP_AS_IS (confirm the authored
    representation — no merge, no split, no boundary re-scope; the
    identity-decision vocabulary has no CONFIRM value)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (no reopening, no promotion)

This script WRITES ONLY scripts/c11_batch2_verdicts.yaml (and removes the
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
TEMPLATE = HERE / "c11_batch2_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch2_verdicts.yaml"
DECISIONS = HERE / "c11_batch2_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"

SESSION = 50
TODAY = "2026-09-12"
OPERATOR_STATEMENT = "CONFIRM all"  # verbatim, session-50 tasking

# ---------------------------------------------------------------------------
# Ruling notes (factual context per flagged row; verdicts all per the mapping)
# ---------------------------------------------------------------------------
EDGE_NOTES = {
    "B2-E-01": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the USED_WITHOUT_RETEACHING relation class stands (FP-B2-2); the "
        "Ar TERM stays with the pilot's CON-AR (B2-ID-01 KEEP_AS_IS); the "
        "cross-boundary source is sanctioned per FN-B1-2 (no duplicate "
        "mint)."),
    "B2-E-02": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the store's FIRST COMMONLY_CONFUSED_WITH deployment stands on the "
        "explicit corpus confusability statement + assessed confusion "
        "family (FP-B2-3; relation_class_rationale recorded per G08)."),
    "B2-E-06": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the causal evidence class stands (EXPLAINED_BY; the prerequisite "
        "reading stays parked in held B2-H-05: one relation per pair)."),
    "B2-E-09": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the pair keeps both edges in their distinct classes (the "
        "confusability link is B2-E-02 COMMONLY_CONFUSED_WITH; density flag "
        "acknowledged, different relation class)."),
    "B2-E-13": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the causal evidence class stands (EXPLAINED_BY; the prerequisite "
        "reading stays parked in held B2-H-06: one relation per pair)."),
    "B2-E-16": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "vocabulary-level element link kept (FP-B1-4 class; the "
        "cross-boundary target is sanctioned per FN-B1-2, no duplicate "
        "mint)."),
    "B2-E-18": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "remediation target equals the WAP target (the batch-1 B1-E-25 "
        "pattern); kept for misconception-recommendation queries (node "
        "remediation_evidence also carries the corrective text)."),
    "B2-E-20": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "remediation target equals the WAP target + cross-boundary target "
        "(the batch-1 B1-E-25 pattern; CON-AR owned by the pilot; kept for "
        "misconception-recommendation queries)."),
}
NODE_NOTES = {
    "B2-N-02": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the node carries the store's first CCW edge (FP-B2-3; B2-E-02 "
        "confirmed)."),
    "B2-N-05": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the CON-ISOTOPES/CON-AR boundary split stands (FP-B2-1; B2-ID-01 "
        "KEEP_AS_IS: the Ar TERM stays with the pilot's CON-AR, the "
        "1.26/1.28 owner)."),
    "B2-N-07": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the 1.20 property-based + 1.21 position-based classification "
        "stays one node (B2-ID-04 KEEP_AS_IS; the B1-N-13/ID-03 pattern)."),
    "B2-N-08": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as "
        "ENRICHMENT-scoped (mirrors the pilot N-08/N-27 and batch-1 "
        "B1-N-08/B1-N-11 patterns; leaf node, no authored edges). Do not "
        "convert this enrichment scoping into a stronger "
        "syllabus-authority claim."),
    "B2-N-11": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "arrangement + group + period stay one node (B2-ID-03 KEEP_AS_IS)."),
    "B2-N-12": (
        "Operator ruling 'CONFIRM all' (session 50): CONFIRM as authored — "
        "the proton/neutron/electron particle triple stays one node "
        "(B2-ID-02 KEEP_AS_IS)."),
}
ID_NOTES = {
    "B2-ID-01": (
        "Operator ruling 'CONFIRM all' (session 50): KEEP_AS_IS — the "
        "CON-ISOTOPES/CON-AR boundary split stands; the Ar TERM stays with "
        "the pilot's CON-AR (the 1.26/1.28 owner); no §7 re-scope. B2-E-01 "
        "/ B2-N-05 confirmed as authored."),
    "B2-ID-02": (
        "Operator ruling 'CONFIRM all' (session 50): KEEP_AS_IS — the "
        "proton/neutron/electron particle triple stays one node; B2-N-12 "
        "confirmed as authored."),
    "B2-ID-03": (
        "Operator ruling 'CONFIRM all' (session 50): KEEP_AS_IS — "
        "arrangement + group + period stay one node; B2-N-11 confirmed as "
        "authored."),
    "B2-ID-04": (
        "Operator ruling 'CONFIRM all' (session 50): KEEP_AS_IS — the "
        "1.20 property-based and 1.21 position-based classification stays "
        "one node; B2-N-07 confirmed as authored."),
}
HELD_NOTE = (
    "Operator ruling 'CONFIRM all' (session 50): the 10 held candidates "
    "(B2-H-01..10) stay held — no reopening, no promotion.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH2_REVIEW_SHEET (session 49 "
    "package) — verdicts recorded by operator decision, session 50 "
    "(2026-09-12).")
META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "mapping": (
        "The ruling confirms the authored batch-2 package as presented on "
        "the session-49 review sheet: every edge row CONFIRM, every node "
        "row CONFIRM (B2-N-08 keeps its ENRICHMENT scoping), each identity "
        "decision KEEP_AS_IS (the authored representation confirmed as-is "
        "— no merge, no split, no boundary re-scope), and the held "
        "appendix stays held. This batch authored NO REVIEW_REQUIRED edge, "
        "so no RR settlement row exists. Verdicts recorded session 50; the "
        "application state lives in scripts/c11_promotions.yaml (the §18 "
        "pathway is the only HUMAN_VALIDATED source) and in the §7 "
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
    die("scripts/c11_batch2_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch2_verdicts_template.yaml missing — the "
        "session-49 package must be intact")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-2 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-49 surface)
assert [r["id"] for r in doc["edge_verdicts"]] == \
    [f"B2-E-{i:02d}" for i in range(1, 24)]
assert [r["id"] for r in doc["node_verdicts"]] == \
    [f"B2-N-{i:02d}" for i in range(1, 13)] + ["B2-M-01", "B2-M-02"]
assert [r["id"] for r in doc["identity_decisions"]] == \
    [f"B2-ID-{i:02d}" for i in range(1, 5)]

# 3. reconcile against the batch-2 decision record + the live store
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
assert len(b_edges) == 23, len(b_edges)
assert len(b_suggested) == 23 and len(b_rr) == 0
if sorted(tmpl_triples) != sorted(b_suggested) \
        or len(set(tmpl_triples)) != 23:
    die("edge triple mismatch between verdict template and the batch-2 "
        "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
if sorted(tmpl_codes) != sorted(b_codes) or len(set(tmpl_codes)) != 14:
    die("node code mismatch between verdict template and the batch-2 "
        "decision record")
assert len(dec["held"]) == 10, len(dec["held"])

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
if len(hv) != 56 or hv != store_triples:
    die("live HUMAN_VALIDATED set != the 56 pilot+batch-1 §18 promotions "
        "(the pre-verdict state must be frozen before recording batch-2 "
        "verdicts)")
if hv & set(b_suggested):
    die("a batch-2 edge is already HUMAN_VALIDATED — pre-verdict state "
        "violated")
if auth.get("authorization", {}).get("decision") != "AUTHORIZED":
    die("§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
if any(p.get("validated_by") != "operator" for p in promo["promotions"]):
    die("existing promotions carry non-operator attribution (anti-forgery)")
assert len(nodes_doc["nodes"]) == 67, len(nodes_doc["nodes"])
assert len(edges_doc["edges"]) == 156, len(edges_doc["edges"])

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

for row in doc["edge_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = EDGE_NOTES.get(row["id"], "")
for row in doc["node_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = NODE_NOTES.get(row["id"], "")
for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = ID_NOTES[row["id"]]
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 2 — OPERATOR verdict record (session-49 package), "
    "FILLED by operator decision session 50 (2026-09-12). OPERATOR-OWNED.\n"
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

assert ec == {"CONFIRM": 23}, ec
assert nc == {"CONFIRM": 14}, nc
assert [r["verdict"] for r in chk["identity_decisions"]] == \
    ["KEEP_AS_IS"] * 4
assert "rr_settlement" not in chk
assert chk["held_appendix_acknowledgment"]["acknowledged"] is True
assert chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT
assert not TEMPLATE.exists()

print("wrote", VERDICTS)
print(f"operator ruling (verbatim): {OPERATOR_STATEMENT!r} "
      f"(decided_by operator, {TODAY})")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 4 x KEEP_AS_IS")
print("RR settlement: none recorded (zero RR edges authored in batch 2)")
print("held_appendix: acknowledged (10 preserved, no reopening)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
