#!/usr/bin/env python3
"""T-C11 session 52 — encode the OPERATOR VERDICT SET for §16 batch 3 into
the operator-owned verdict record scripts/c11_batch3_verdicts.yaml.

The operator ruled on the batch-3 gate (review sheet
graph/reports/C11_BATCH3_REVIEW_SHEET.md, session-51 package) with the
practical-review policy below (session-52 tasking, 2026-09-13). This script
encodes the per-row decisions VERBATIM from that policy — no verdict
invented, no evidence reinterpreted, no ID guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses if the template rows do not reconcile 1:1 against the batch-3
    decision record (39 SUGGESTED edge triples / ZERO RR triples / 24 node
    codes / 14 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (79 HUMAN_VALIDATED = 28 pilot + 28 batch-1 + 23 batch-2 §18
    promotions; 0 batch-3 promotions; §16 authorization AUTHORIZED; pilot
    HOLDs + both RR settlements frozen; 91 nodes / 220 edges).

Verdict policy mapping (recorded verbatim in the file's operator_ruling
block):
  * every edge row          -> CONFIRM  (the evidence clearly supports each
    authored relationship: 144/144 quote anchors machine-verified G03/c11.4;
    pass-2 adversarial review 39/39 with zero demotions; the FLAGGED rows
    carry relation-class / first-deployment / family-overlap flags — the
    ordinary-ontology-imperfection class the operator explicitly refuses to
    treat as a blocker)
  * every node row          -> CONFIRM  (no duplicate canonical mint;
    pass-2 verified 24/24)
  * every identity decision -> KEEP_AS_IS (the simplest representation that
    preserves meaningful distinctions and creates no duplicate canonical
    concept; the identity-decision vocabulary has no CONFIRM value)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (14 preserved; a clean
    quarantine is preferable to inventing evidence — no reopening, no
    promotion)

This script WRITES ONLY scripts/c11_batch3_verdicts.yaml (and removes the
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
TEMPLATE = HERE / "c11_batch3_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch3_verdicts.yaml"
DECISIONS = HERE / "c11_batch3_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"

SESSION = 52
TODAY = "2026-09-13"
# Verbatim operative excerpt from the operator's session-52 directive
# ("T-C11 Batch 3 — Operator Verdicts and Promotion", §2 Verdict policy).
OPERATOR_STATEMENT = (
    "Where the evidence clearly supports the authored relationship: "
    "CONFIRM. Where there is genuine evidence insufficiency or an "
    "architectural/semantic problem: HOLD or REJECT, as appropriate. "
    "However, do not turn ordinary ontology imperfection, wording "
    "preferences, enrichment opportunities, or theoretical alternative "
    "interpretations into blockers.")

# ---------------------------------------------------------------------------
# Verdict notes (evidence-grounded context per row; verdicts all per the
# mapping above). Notes cite the operator policy + the pass-2 flag the row
# carries and why it is NOT a blocker under the directive.
# ---------------------------------------------------------------------------
EDGE_NOTES = {
    "B3-E-06": (
        "Operator policy (session 52): CONFIRM as authored — the store's "
        "FIRST RELATED_TO deployment stands on the note's explicit 'C60 is "
        "a simple molecular structure' statement (FP-B3-3; "
        "relation_class_rationale recorded per G08; the alternative "
        "modeling is B3-ID-07 KEEP_AS_IS). A first-class deployment is not "
        "a blocker."),
    "B3-E-14": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "reachable-but-different-information density flag (FP-B3-2; the "
        "§19 reachable-ne-redundant precedent: the edge carries the "
        "COMPOSITION of what is electrolysed) is ordinary ontology "
        "imperfection, not a semantic defect."),
    "B3-E-20": (
        "Operator policy (session 52): CONFIRM as authored — the store's "
        "SECOND COMMONLY_CONFUSED_WITH edge stands on the corpus's explicit "
        "share-vs-transfer difference tip (FP-B3-4; one-directional storage "
        "per the batch-2 convention; MS cross-REJECTs are G07-inadmissible "
        "assessment context only)."),
    "B3-E-26": (
        "Operator policy (session 52): CONFIRM as authored — EXPLAINED_BY "
        "is the stronger evidenced reading for the explicit causal "
        "sentences ('This is because...'; FP-B3-2); the equally-real "
        "prerequisite reading is a theoretical alternative interpretation, "
        "not a blocker; one relation per pair per the ratified discipline."),
    "B3-E-29": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "vocabulary-level operand class (FP-B1-4) + cross-boundary target "
        "was operator-CONFIRMED in batch 2 (B2-E-16); the cross-boundary "
        "target is sanctioned per FN-B2-2, no duplicate mint."),
    "B3-E-30": (
        "Operator policy (session 52): CONFIRM as authored — remediation "
        "target equals the WAP target (the batch-1 B1-E-25 pattern, "
        "operator-CONFIRMED in batches 1-2); kept for "
        "misconception-recommendation queries (node remediation_evidence "
        "also carries the corrective text)."),
    "B3-E-32": (
        "Operator policy (session 52): CONFIRM as authored — remediation "
        "target equals the WAP target (B1-E-25 pattern) + the family "
        "overlap is resolved by B3-ID-06 KEEP_AS_IS (two documented "
        "surfaces, two targets); not a blocker."),
    "B3-E-33": (
        "Operator policy (session 52): CONFIRM as authored — the WAP "
        "evidence is independently documented (COVALENT_MS_P2 Q1(b) "
        "REJECT) with a different target concept (1.50 vs 1.47); the "
        "family-overlap merge question is B3-ID-06 KEEP_AS_IS."),
    "B3-E-34": (
        "Operator policy (session 52): CONFIRM as authored — remediation "
        "target equals the WAP target (the B1-E-25 pattern, "
        "operator-CONFIRMED in batches 1-2)."),
    "B3-E-37": (
        "Operator policy (session 52): CONFIRM as authored — remediation "
        "target equals the MISCONCEPTION_OF target (the B1-E-25 pattern); "
        "kept for misconception-recommendation queries."),
}
NODE_NOTES = {
    "B3-N-01": (
        "Operator policy (session 52): CONFIRM as authored — the term pair "
        "+ migration rule stay one node (FP-B1-1 class; the corpus teaches "
        "them together; the granularity precedent CON-SUBATOMIC-PARTICLES)."),
    "B3-N-02": (
        "Operator policy (session 52): CONFIRM as authored — the 1.58C dual "
        "node attachment stands (B3-ID-05 KEEP_AS_IS: the discharge rules "
        "stay independently assessable; mirrors the spec's describe + "
        "predict wording)."),
    "B3-N-03": (
        "Operator policy (session 52): CONFIRM as authored — the 1.44 "
        "sharing-definition + 1.45 electrostatic-mechanism stay one node "
        "(B3-ID-02 KEEP_AS_IS: definition vs mechanism of one term; the "
        "ratified 1.19/1.20 dual-attachment precedents)."),
    "B3-N-04": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "know/understand dual attachment (1.51+1.55C) stays one node "
        "(B3-ID-01 KEEP_AS_IS: same learnable fact pair at two depths)."),
    "B3-N-05": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "three-allotrope block stays one node (B3-ID-04 KEEP_AS_IS: one "
        "SP, one demand set); the node carries the store's first "
        "RELATED_TO edge (B3-E-06 CONFIRM)."),
    "B3-N-12": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "deduction-rule + named-ion-table block stays one node (FP-B1-1 "
        "class; the corpus teaches them as one block, the deduction rule "
        "introduces the tables)."),
    "B3-N-14": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "know/understand dual attachment (1.43+1.56C) stays one node "
        "(B3-ID-01 KEEP_AS_IS)."),
    "B3-N-18": (
        "Operator policy (session 52): CONFIRM as authored — the "
        "representation-vs-bonding dual attachment (1.52C+1.53C) stays one "
        "node (B3-ID-05 KEEP_AS_IS: the 2-D diagram IS the lattice the "
        "attraction lives in)."),
    "B3-N-20": (
        "Operator policy (session 52): CONFIRM as authored — the structure "
        "node keeps the intermolecular-forces term as its own explanatory "
        "content (B3-ID-03 KEEP_AS_IS); it is also the remediation target "
        "of MIS-COVALENT-BONDS-BROKEN."),
    "B3-M-02": (
        "Operator policy (session 52): CONFIRM as authored — kept separate "
        "from MIS-COVALENT-BONDS-BROKEN for per-concept remediation "
        "targeting (B3-ID-06 KEEP_AS_IS); the WAP evidence is "
        "independently documented."),
    "B3-M-03": (
        "Operator policy (session 52): CONFIRM as authored — the mark-scheme "
        "quote preserves the pinned line-wrap artifact (FP-B3-5, "
        "layout-verified, noted in derivation_notes); the artifact is "
        "explicit, not silent — not a blocker."),
}
ID_NOTES = {
    "B3-ID-01": (
        "Operator policy (session 52): KEEP_AS_IS — the know/understand "
        "dual-attachment pairs (CON-IONIC-CONDUCTION 1.43/1.56C; "
        "CON-COVALENT-CONDUCTION 1.51+1.55C) stay merged as dual "
        "attachments; the simplest representation that preserves the "
        "distinction (same fact pair at two depths; the ratified 1.19/1.20 "
        "precedents). B3-N-04/B3-N-14 confirmed as authored."),
    "B3-ID-02": (
        "Operator policy (session 52): KEEP_AS_IS — CON-COVALENT-BOND keeps "
        "the 1.44 sharing-definition and 1.45 electrostatic-mechanism in "
        "one node (definition vs mechanism of one term; no duplicate "
        "canonical concept arises from the merge). B3-N-03 confirmed as "
        "authored."),
    "B3-ID-03": (
        "Operator policy (session 52): KEEP_AS_IS — CON-SIMPLE-MOLECULAR "
        "stays one node carrying the intermolecular-forces term as its own "
        "explanatory content (the spec names the term; minting a separate "
        "IMF node would be enrichment, not a defect fix). B3-N-20 confirmed "
        "as authored."),
    "B3-ID-04": (
        "Operator policy (session 52): KEEP_AS_IS — the "
        "diamond/graphite/C60 allotrope block stays one node (one SP "
        "4CH1-1.50, one demand set). B3-N-05 confirmed as authored."),
    "B3-ID-05": (
        "Operator policy (session 52): KEEP_AS_IS — CON-METALLIC-BOND keeps "
        "1.52C representation + 1.53C bonding as one node (the 2-D diagram "
        "is the same lattice the attraction lives in), and "
        "CON-AQUEOUS-DISCHARGE stays a separate node on 1.58C (the "
        "discharge rules stay independently assessable). B3-N-02 / B3-N-18 "
        "confirmed as authored."),
    "B3-ID-06": (
        "Operator policy (session 52): KEEP_AS_IS — MIS-GRAPHITE-LAYER-BONDS "
        "stays separate from MIS-COVALENT-BONDS-BROKEN: one bonds-vs-forces "
        "family, two independently documented wrong-answer surfaces and two "
        "different target concepts (1.50 vs 1.47) — per-concept remediation "
        "targeting preserved; no duplicate canonical concept. B3-E-32 / "
        "B3-E-33 / B3-M-02 confirmed as authored."),
    "B3-ID-07": (
        "Operator policy (session 52): KEEP_AS_IS — the "
        "RELATED_TO(DIAMOND-GRAPHITE, SIMPLE-MOLECULAR) edge stands on the "
        "note's explicit 'C60 is a simple molecular structure' statement; "
        "no direct 1.50 attachment on CON-SIMPLE-MOLECULAR replaces it. "
        "B3-E-06 CONFIRM."),
}
HELD_NOTE = (
    "Operator policy (session 52): the 14 held candidates (B3-H-01..14) "
    "stay held — no reopening, no promotion, no rescue attempts. A clean "
    "quarantine is preferable to inventing evidence (the two no-MS "
    "abstentions B3-H-11/B3-H-12 revisit only with new mark-scheme "
    "evidence).")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH3_REVIEW_SHEET (session 51 "
    "package) — verdicts recorded by operator decision, session 52 "
    "(2026-09-13).")
META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "mapping": (
        "The operator authorized moving forward rather than reopening "
        "another prolonged review cycle, delegating the practical per-row "
        "review under the established T-C11 rules ('For each row, make the "
        "best evidence-based decision using the established T-C11 rules.') "
        "and declaring this verdict file the operator authorization for "
        "promotion ('My verdict file is that operator authorization.'). "
        "Applied per row: every edge row CONFIRM (the evidence clearly "
        "supports each authored relationship — 144/144 quote anchors "
        "machine-verified G03/c11.4; pass-2 adversarial review 39/39 with "
        "zero demotions; the FLAGGED rows carry relation-class / "
        "first-deployment / family-overlap flags, the "
        "ordinary-ontology-imperfection class the operator explicitly "
        "refuses to treat as a blocker); every node row CONFIRM (no "
        "duplicate canonical mint; pass-2 verified 24/24); each identity "
        "decision KEEP_AS_IS (the simplest representation that preserves "
        "meaningful distinctions and creates no duplicate canonical "
        "concept — no merge, no split, no boundary re-scope); and the held "
        "appendix stays held (a clean quarantine is preferable to inventing "
        "evidence). This batch authored NO REVIEW_REQUIRED edge, so no RR "
        "settlement row exists. Verdicts recorded session 52; the "
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
    die("scripts/c11_batch3_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch3_verdicts_template.yaml missing — the "
        "session-51 package must be intact")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-3 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-51 surface)
assert [r["id"] for r in doc["edge_verdicts"]] == \
    [f"B3-E-{i:02d}" for i in range(1, 40)]
assert [r["id"] for r in doc["node_verdicts"]] == \
    [f"B3-N-{i:02d}" for i in range(1, 21)] + \
    [f"B3-M-{i:02d}" for i in range(1, 5)]
assert [r["id"] for r in doc["identity_decisions"]] == \
    [f"B3-ID-{i:02d}" for i in range(1, 8)]

# 3. reconcile against the batch-3 decision record + the live store
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml")
                           .read_text(encoding="utf-8"))
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
assert len(b_edges) == 39, len(b_edges)
assert len(b_suggested) == 39 and len(b_rr) == 0
if sorted(tmpl_triples) != sorted(b_suggested) \
        or len(set(tmpl_triples)) != 39:
    die("edge triple mismatch between verdict template and the batch-3 "
        "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
if sorted(tmpl_codes) != sorted(b_codes) or len(set(tmpl_codes)) != 24:
    die("node code mismatch between verdict template and the batch-3 "
        "decision record")
assert len(dec["held"]) == 14, len(dec["held"])

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
if len(hv) != 79 or hv != store_triples:
    die("live HUMAN_VALIDATED set != the 79 pilot+batch-1+batch-2 §18 "
        "promotions (the pre-verdict state must be frozen before recording "
        "batch-3 verdicts)")
if hv & set(b_suggested):
    die("a batch-3 edge is already HUMAN_VALIDATED — pre-verdict state "
        "violated")
if auth.get("authorization", {}).get("decision") != "AUTHORIZED":
    die("§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
if any(p.get("validated_by") != "operator" for p in promo["promotions"]):
    die("existing promotions carry non-operator attribution (anti-forgery)")
assert len(nodes_doc["nodes"]) == 91, len(nodes_doc["nodes"])
assert len(edges_doc["edges"]) == 220, len(edges_doc["edges"])

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
    "# T-C11 §16 batch 3 — OPERATOR verdict record (session-51 package), "
    "FILLED by operator decision session 52 (2026-09-13). OPERATOR-OWNED.\n"
    "# Operator verdict policy (session-52 directive, §2 Verdict policy): "
    "CONFIRM where the evidence\n"
    "# clearly supports the authored relationship; HOLD/REJECT only for "
    "genuine evidence insufficiency or an\n"
    "# architectural/semantic problem; ordinary ontology imperfection, "
    "wording preferences, enrichment opportunities\n"
    "# and theoretical alternative interpretations are NOT blockers — see "
    "meta.operator_ruling for the recorded mapping.\n"
    "# Vocabulary and pathway: see the meta.instructions block. Verdicts are "
    "RECORDED; the application state lives in\n"
    "# scripts/c11_promotions.yaml (§18) and the decision record's §7 "
    "blocks — never here.\n"
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

assert ec == {"CONFIRM": 39}, ec
assert nc == {"CONFIRM": 24}, nc
assert [r["verdict"] for r in chk["identity_decisions"]] == \
    ["KEEP_AS_IS"] * 7
assert "rr_settlement" not in chk
assert chk["held_appendix_acknowledgment"]["acknowledged"] is True
assert chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT
assert not TEMPLATE.exists()

print("wrote", VERDICTS)
print(f"operator verdict policy recorded verbatim "
      f"(decided_by operator, {TODAY})")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 7 x KEEP_AS_IS")
print("RR settlement: none recorded (zero RR edges authored in batch 3)")
print("held_appendix: acknowledged (14 preserved, no reopening)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
