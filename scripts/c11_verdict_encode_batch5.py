#!/usr/bin/env python3
"""T-C11 session 56 — encode the OPERATOR VERDICT SET for §16 batch 5 into
the operator-owned verdict record scripts/c11_batch5_verdicts.yaml.

The operator ruled on the batch-5 gate (review sheet
graph/reports/C11_BATCH5_REVIEW_SHEET.md, session-55 package) with the
completed review sheet section 6 ("Completed operator verdict", delivered
to the verdict session as C11_BATCH5_REVIEW_SHEET_COMPLETED.md, 2026-09-22):
all 16 node verdicts + all 18 edge verdicts accepted with the pass-2
statuses retained, the six identity decisions KEEP_AS_IS, the 14 held
candidates acknowledged/quarantined, zero RR, and the final directive
"PASS — proceed to encoding/reconciliation and the separately governed
promotion step." This script encodes the per-row decisions from that
completed sheet — no verdict invented, no evidence reinterpreted, no ID
guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses if the template rows do not reconcile 1:1 against the batch-5
    decision record (18 SUGGESTED edge triples / ZERO RR triples / 16 node
    codes [13 CONCEPT + 3 MISCONCEPTION] / 14 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (153 HUMAN_VALIDATED = 28 pilot + 28 batch-1 + 23 batch-2 + 39 batch-3
    + 35 batch-4 §18 promotions; 0 batch-5 promotions; §16 authorization
    AUTHORIZED; pilot HOLDs + both RR settlements frozen; 129 nodes /
    306 edges).

Encoding rules (recorded verbatim in the file's operator_ruling.mapping):
  * every edge row          -> CONFIRM  (B5-E-01 carries the operator's
    CONFIRM_WITH_NOTE qualification in notes — the verdict-record
    vocabulary CONFIRM|REJECT|HOLD|MERGE|SPLIT has no WITH_NOTE value, the
    batch-1..4 precedent is that qualifications ride in notes)
  * every node row          -> CONFIRM  (the four pass-2 CONFIRM_WITH_NOTE
    rows — G1/G7-REACTIVITY-ECONFIG, MIS-HALOGEN-HALIDE, MIS-CUO-COLOUR —
    carry the retained pass-2 qualification in notes)
  * every identity decision -> KEEP_AS_IS (the operator's §6 rationale
    table, verbatim)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (14 preserved, quarantined)

IDENTITY-SAFETY NOTE (the sheet-vs-template numbering hazard): the review
sheet's section-2/6 rows number nodes in table order (B5-N-01 =
G1-FAMILY-EVIDENCE) while the template numbers them alphabetically by code
(B5-N-01 = AIR-COMPOSITION). Verdicts and notes here are therefore keyed
by TRIPLE (edges) and CODE (nodes), never by row id, and each template
row's id<->code/triple correspondence is asserted against the decision
record before anything is written.

This script WRITES ONLY scripts/c11_batch5_verdicts.yaml (and removes the
now-renamed template, per the sheet's gate pathway). It promotes nothing
and re-authors no decision record; application (§18 promotion) is the
separate sanctioned step in this same session per the operator's §6
directive ("proceed to encoding/reconciliation and the separately governed
promotion step").
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry (session-56: post-C28 layout)

GRAPH = GP.qual_dir()          # the qual's ratified store dir
TEMPLATE = HERE / "c11_batch5_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch5_verdicts.yaml"
DECISIONS = HERE / "c11_batch5_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"

SESSION = 56
TODAY = "2026-09-22"
# Verbatim operative text from the operator's completed review sheet §6
# ("Final operator gate" + "Operator verdict", C11_BATCH5_REVIEW_SHEET_
# COMPLETED.md, 2026-09-22).
OPERATOR_STATEMENT = (
    "Final operator gate: Nodes 16/16 confirmed; Authored edges 18/18 "
    "confirmed; Identity decisions 6/6 KEEP_AS_IS; Held candidates 14/14 "
    "acknowledged and quarantined; REVIEW_REQUIRED edges 0; REJECTED "
    "authored edges 0; Batch-5 promotions 0; Authority status SUGGESTED "
    "until the §18 promotion pathway is executed. Operator verdict: PASS — "
    "proceed to encoding/reconciliation and the separately governed "
    "promotion step. This verdict does not itself perform promotion. The "
    "next mechanical step remains the existing pathway: encode the "
    "verdicts -> run the §18 promotion process -> regenerate -> rerun the "
    "gate suite.")

# ---------------------------------------------------------------------------
# Verdict notes (evidence-grounded context per row; verdicts all CONFIRM per
# the mapping above — the operator's §6 CONFIRM_WITH_NOTE qualifications ride
# in notes). Keyed by TRIPLE (edges) / CODE (nodes).
# ---------------------------------------------------------------------------
EDGE_NOTES = {
    # The one relation-class qualification row (operator §6 explicitly noted).
    "4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION": (
        "Operator §6 (session 56): CONFIRM_WITH_NOTE retained — retain the "
        "edge as a grounding/teaching relation; do not reinterpret it as a "
        "claim that the composition concept is independently caused by the "
        "percentage-determination method. Pass-2 (FP-B5-4): the derivation "
        "chain (method -> calculation -> 19.7% -> 'approximately 20%') is "
        "fully in ONE source, which satisfies the EXPLAINED_BY contract; "
        "the grounding direction is defensible and evidenced."),
    # The three sanctioned cross-section boundary edges (session-55 ruling).
    "4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO": (
        "Operator §6: CONFIRM — a sanctioned cross-section boundary edge "
        "(session-55 ruling; batch-4 owner CON-EXO-ENDO, no duplicate "
        "mint); the operator's directive: the boundary edges 'remain "
        "CONFIRM and must continue to reference the existing owners.'"),
    "4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION": (
        "Operator §6: CONFIRM — a sanctioned cross-section boundary edge "
        "(session-55 ruling; batch-2 owner CON-ELECTRONIC-CONFIGURATION, "
        "no duplicate mint); the boundary edges 'remain CONFIRM and must "
        "continue to reference the existing owners.'"),
    "4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION": (
        "Operator §6: CONFIRM — a sanctioned cross-section boundary edge "
        "(session-55 ruling; batch-2 owner CON-ELECTRONIC-CONFIGURATION; "
        "the note's verbatim dependency statement 'We can use electronic "
        "configuration to explain the trends in chemical reactivity down "
        "Group 7'); the boundary edges 'remain CONFIRM and must continue "
        "to reference the existing owners.'"),
    # The FP-B5-5 re-authoring companion rows (re-scoped pre-gate).
    "4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES": (
        "Operator §6: CONFIRM as re-authored (FP-B5-5) — scoped to the "
        "physical-trend surface ('The melting and boiling points of the "
        "halogens increase as you go down the group'); the reactivity "
        "dependency rides its own edge (B5-E-10)."),
    "4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG": (
        "Operator §6: CONFIRM as authored — the FP-B5-5 companion row: the "
        "reactivity surface of the prediction demand ('The halogens "
        "decrease in reactivity moving down the group, but they still form "
        "halide salts') depends on the 2.8C trend-explanation node."),
    # The misconception evidence rows.
    "4CH1-MIS-CUO-COLOUR REMEDIATED_BY 4CH1-CON-CO2-FROM-CARBONATES": (
        "Operator §6: CONFIRM as authored — remediation target equals the "
        "WAP target (the B1-E-25 pattern, operator-CONFIRMED in batches "
        "1-4); the corrective text ('Copper(II) carbonate is a green "
        "powder and slowly darkens as black copper(II) oxide is produced') "
        "is note-verified."),
    "4CH1-MIS-CUO-COLOUR WRONG_ANSWER_PATTERN 4CH1-CON-CO2-FROM-CARBONATES": (
        "Operator §6: CONFIRM as authored — the GASES Q1c Reject column "
        "('REJECT all other colours' + 'IGNORE brown' against the expected "
        "'black') is clean documentation; narrow (one observation answer) "
        "but the evidence is exact."),
    "4CH1-MIS-G1-SHELL-EXPLANATION REMEDIATED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG": (
        "Operator §6: CONFIRM as authored — remediation target equals the "
        "WAP target (the B1-E-25 pattern); the corrective outer-electron "
        "distance/attraction text is note-verified."),
    "4CH1-MIS-G1-SHELL-EXPLANATION WRONG_ANSWER_PATTERN 4CH1-CON-G1-REACTIVITY-ECONFIG": (
        "Operator §6: CONFIRM as authored — the GROUP1 Q1d/Q3d "
        "IGNORE/award-restriction evidence class (FP-B5-2 subtype "
        "confirmed by the operator's acceptance): 'IGNORE references to "
        "more shells / larger atomic radius' is a documented "
        "wrong-answer pattern with an award restriction."),
    "4CH1-MIS-HALOGEN-HALIDE REMEDIATED_BY 4CH1-CON-G7-DISPLACEMENT": (
        "Operator §6: CONFIRM as authored — remediation target equals the "
        "WAP target (the B1-E-25 pattern); the displacement definition is "
        "note-verified."),
    "4CH1-MIS-HALOGEN-HALIDE WRONG_ANSWER_PATTERN 4CH1-CON-G7-DISPLACEMENT": (
        "Operator §6: CONFIRM as authored — the GROUP7 Q1bii Reject column "
        "documents BOTH conflation directions (same reactivity / different "
        "reactivity) — double-documented; the pdftotext column interleaving "
        "is handled by the antonym-pairing attribution recorded in "
        "derivation_notes (the batch-4 RRE convention)."),
    # The 2.14 practical-ownership edge (B5-ID-03 KEEP_AS_IS).
    "4CH1-PR-05 REQUIRES_PREREQUISITE 4CH1-CON-O2-PERCENT-DETERMINATION": (
        "Operator §6: CONFIRM as authored — PR-05 owns 2.14 (the "
        "1.13/1.60C precedent; B5-ID-03 KEEP_AS_IS); the practical->concept "
        "dependency ('To determine the percentage of oxygen in air using "
        "the oxidation of iron') is note-verified."),
}
NODE_NOTES = {
    # The two pass-2 CONFIRM_WITH_NOTE concept rows (sibling-split B5-ID-01).
    "4CH1-CON-G1-REACTIVITY-ECONFIG": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2: "
        "SEPARATE from the 2.8C sibling node (B5-ID-01): electron LOSS vs "
        "electron GAIN, opposite trend directions, distinct SPs — the "
        "split is defensible under the minting rule (distinct taught "
        "substance); a MERGE would corrupt the opposite-direction "
        "structure the spec itself demands. Attack result: keep."),
    "4CH1-CON-G7-REACTIVITY-ECONFIG": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2: same "
        "B5-ID-01 sibling question as the 2.4C node; the note states the "
        "electronic-configuration dependency VERBATIM ('We can use "
        "electronic configuration to explain the trends') — the strongest "
        "boundary-edge anchor in the batch."),
    # The two pass-2 CONFIRM_WITH_NOTE misconception rows.
    "4CH1-MIS-CUO-COLOUR": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2: the "
        "Q1c Reject column ('REJECT all other colours' + 'IGNORE brown' "
        "against the expected 'black') is clean documentation; the pattern "
        "is narrow (one observation answer) but the evidence is exact — "
        "the mint is defensible because the wrong colour is the CuCO3 "
        "decomposition's most assessable surface."),
    "4CH1-MIS-HALOGEN-HALIDE": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2: the "
        "Q1bii Reject column rejects BOTH conflation directions (same "
        "reactivity / different reactivity) — double-documented; the "
        "pdftotext column interleaving is handled by antonym-pairing "
        "attribution recorded in the node's derivation_notes (the batch-4 "
        "RRE convention)."),
}
ID_NOTES = {
    "B5-ID-01": (
        "Operator §6: KEEP_AS_IS — keep 2.4C and 2.8C as distinct sibling "
        "concepts because they encode opposite Group-trend directions and "
        "therefore have distinct operands/meanings."),
    "B5-ID-02": (
        "Operator §6: KEEP_AS_IS — keep 2.9 air composition and 2.10 "
        "oxygen-percentage determination separate: one is "
        "knowledge/composition; the other is a determination method."),
    "B5-ID-03": (
        "Operator §6: KEEP_AS_IS — keep 2.14 under the existing PR-05 "
        "practical ownership rather than minting a duplicate batch-5 "
        "concept."),
    "B5-ID-04": (
        "Operator §6: KEEP_AS_IS — keep the 2.11 combustion concept as one "
        "family node; the source evidence does not justify splitting the "
        "combustion-of-elements family into separate concept identities."),
    "B5-ID-05": (
        "Operator §6: KEEP_AS_IS — keep the two CO2 concepts separate: "
        "thermal decomposition of carbonates and greenhouse/climate-change "
        "significance represent different educational operands."),
    "B5-ID-06": (
        "Operator §6: KEEP_AS_IS — keep 2.1 family evidence and 2.2 "
        "trend/differences separate: similarities establish family "
        "evidence, while differences support the reactivity trend."),
}
HELD_NOTE = (
    "Operator §6: all 14 held candidates (B5-H-01..14) are ACKNOWLEDGED / "
    "KEEP QUARANTINED — no held candidate is reopened, promoted, or "
    "converted into an authored edge/node by this review; the abstention "
    "reasons remain part of the evidence record. The three CLASSIC "
    "wrong-answer patterns refused for missing documentation (B5-H-04/05/06) "
    "revisit only with new mark-scheme evidence (the session-53 Step-3 "
    "rule). A held record is a valid outcome — the abstention is the "
    "system's honest output.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH5_REVIEW_SHEET (session-55 "
    "package) — verdicts recorded by operator decision, session 56 "
    "(2026-09-22), from the completed review sheet §6 "
    "(C11_BATCH5_REVIEW_SHEET_COMPLETED.md).")
META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "mapping": (
        "The operator reviewed the session-55 gate package (review sheet "
        "graph/reports/C11_BATCH5_REVIEW_SHEET.md §1-5 byte-identical in "
        "the completed copy — verified before encoding) and returned the "
        "completed sheet §6 'Completed operator verdict': all 16 pass-2 "
        "node verdicts accepted with the statuses retained (13 CONCEPT "
        "rows CONFIRM — the 2.4C and 2.8C reactivity-econfig rows as "
        "CONFIRM_WITH_NOTE; 3 MISCONCEPTION rows CONFIRM — the "
        "halogen/halide and CuO-colour rows as CONFIRM_WITH_NOTE); all 18 "
        "authored semantic edges CONFIRM except the explicitly noted "
        "relation-class qualification B5-E-01 (AIR-COMPOSITION "
        "EXPLAINED_BY O2-PERCENT-DETERMINATION) — CONFIRM_WITH_NOTE: "
        "'Retain the edge as a grounding/teaching relation; do not "
        "reinterpret it as a claim that the composition concept is "
        "independently caused by the percentage-determination method'; "
        "'the three sanctioned cross-section boundary edges remain CONFIRM "
        "and must continue to reference the existing owners. No duplicate "
        "concept is to be minted'; the six identity decisions resolved "
        "KEEP_AS_IS each with a recorded rationale (the 2.4C/2.8C opposite-"
        "direction siblings, the 2.9/2.10 know-vs-method pair, the 2.14 "
        "PR-05 practical ownership, the 2.11 single family node, the two "
        "CO2 operands, the 2.1/2.2 similarities/differences pair); the 14 "
        "held candidates 'ACKNOWLEDGED / KEEP QUARANTINED' — none reopened, "
        "promoted, or converted; zero RR rows (the batch authored none); "
        "zero REJECTED authored edges; final directive: 'Operator verdict: "
        "PASS — proceed to encoding/reconciliation and the separately "
        "governed promotion step.' The operator verdict file itself is the "
        "authorization (the session-54 precedent). ENCODING RULES: the "
        "verdict-record vocabulary (CONFIRM|REJECT|HOLD|MERGE|SPLIT) has "
        "no WITH_NOTE value, so the operator's five CONFIRM_WITH_NOTE "
        "statuses are recorded as CONFIRM with the qualification carried "
        "verbatim in the row's notes (the batch-1..4 precedent that "
        "qualifications ride in notes); node verdicts are keyed by CODE "
        "and edge verdicts by TRIPLE — never by row id — because the "
        "sheet's §2/§6 node numbering (table order) differs from the "
        "template's alphabetical-by-code numbering, and each template "
        "row's id<->code correspondence was asserted against the decision "
        "record before encoding; node authority is NOT changed by these "
        "confirmations (nodes have no §18 pathway — node promotion remains "
        "a separate identity decision, deferred); PART_OF is derived and "
        "outside §18; the application state lives in "
        "scripts/c11_promotions.yaml (the §18 pathway is the only "
        "HUMAN_VALIDATED source) — this file never carries promotion "
        "payload or promoted status. Changing a recorded verdict requires "
        "an explicit operator decision."),
}


def die(msg: str):
    print(f"FAIL-CLOSED: {msg}")
    sys.exit(1)


def _require(cond: bool, msg: str) -> None:
    """Fail-closed gate that survives `python -O` (assert is stripped
    under -O, which would turn this gate fail-open — MD-33)."""
    if not cond:
        raise RuntimeError(msg)


# ---------------------------------------------------------------------------
# Load + pre-state assertions
# ---------------------------------------------------------------------------
if VERDICTS.exists():
    die("scripts/c11_batch5_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch5_verdicts_template.yaml missing — the "
        "session-55 package must be intact")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-5 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-55 surface)
assert [r["id"] for r in doc["edge_verdicts"]] == \
    [f"B5-E-{i:02d}" for i in range(1, 19)]
assert [r["id"] for r in doc["node_verdicts"]] == \
    [f"B5-N-{i:02d}" for i in range(1, 14)] + \
    [f"B5-M-{i:02d}" for i in range(1, 4)]
assert [r["id"] for r in doc["identity_decisions"]] == \
    [f"B5-ID-{i:02d}" for i in range(1, 7)]

# 3. reconcile against the batch-5 decision record + the live store
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
_require(len(b_edges) == 18, f"batch-5 decision record carries "
         f"{len(b_edges)} edges, expected 18")
_require(len(b_suggested) == 18 and len(b_rr) == 0,
         "batch-5 edges must be 18 SUGGESTED / 0 RR at the pre-verdict state")
_require(sorted(tmpl_triples) == sorted(b_suggested)
         and len(set(tmpl_triples)) == 18,
         "edge triple mismatch between verdict template and the batch-5 "
         "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
_require(sorted(tmpl_codes) == sorted(b_codes) and len(set(tmpl_codes)) == 16,
         "node code mismatch between verdict template and the batch-5 "
         "decision record")
_require(len(dec["held"]) == 14, f"batch-5 held count "
         f"{len(dec['held'])}, expected 14")
# every note key must hit a real row (no stale keys)
for k in EDGE_NOTES:
    _require(k in set(tmpl_triples), f"EDGE_NOTES key not in template: {k}")
for k in NODE_NOTES:
    _require(k in set(tmpl_codes), f"NODE_NOTES key not in template: {k}")

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
_require(len(hv) == 153 and hv == store_triples,
         "live HUMAN_VALIDATED set != the 153 pilot+batch-1+batch-2+batch-3"
         "+batch-4 §18 promotions (the pre-verdict state must be frozen "
         "before recording batch-5 verdicts)")
_require(not (hv & set(b_suggested)),
         "a batch-5 edge is already HUMAN_VALIDATED — pre-verdict state "
         "violated")
_require(auth.get("authorization", {}).get("decision") == "AUTHORIZED",
         "§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
_require(all(p.get("validated_by") == "operator"
             for p in promo["promotions"]),
         "existing promotions carry non-operator attribution (anti-forgery)")
_require(len(nodes_doc["nodes"]) == 129, f"store nodes "
         f"{len(nodes_doc['nodes'])}, expected 129")
_require(len(edges_doc["edges"]) == 306, f"store edges "
         f"{len(edges_doc['edges'])}, expected 306")

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

for row in doc["edge_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = EDGE_NOTES.get(row["triple"], "")
for row in doc["node_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = NODE_NOTES.get(row["code"], "")
for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = ID_NOTES[row["id"]]
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 5 — OPERATOR verdict record (session-55 package), "
    "FILLED by operator decision session 56 (2026-09-22). OPERATOR-OWNED.\n"
    "# Operator verdict (completed review sheet §6, "
    "C11_BATCH5_REVIEW_SHEET_COMPLETED.md): all 16 node verdicts and all 18\n"
    "# edge verdicts accepted with the pass-2 statuses retained (the five\n"
    "# CONFIRM_WITH_NOTE qualifications recorded in notes per the vocabulary "
    "rule); the six identity\n"
    "# decisions KEEP_AS_IS; the 14 held candidates acknowledged and "
    "quarantined; zero RR; zero REJECT.\n"
    "# Vocabulary and pathway: see the meta.instructions block. Verdicts are "
    "RECORDED; the application state lives in\n"
    "# scripts/c11_promotions.yaml (§18) — never here.\n"
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

_require(ec == {"CONFIRM": 18},
         f"post-write: edge verdict counts drifted: {ec}")
_require(nc == {"CONFIRM": 16},
         f"post-write: node verdict counts drifted: {nc}")
_require([r["verdict"] for r in chk["identity_decisions"]]
         == ["KEEP_AS_IS"] * 6,
         "post-write: identity decisions drifted")
_require("rr_settlement" not in chk,
         "post-write: unexpected rr_settlement present")
_require(chk["held_appendix_acknowledgment"]["acknowledged"] is True,
         "post-write: held appendix acknowledgment missing")
_require(chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT,
         "post-write: operator ruling text drifted")
_require(chk["edge_verdicts"][0]["notes"].startswith(
    "Operator §6 (session 56): CONFIRM_WITH_NOTE retained"),
    "post-write: the B5-E-01 qualification note drifted")
_require(not TEMPLATE.exists(),
         "post-write: verdict template was not consumed")

print("wrote", VERDICTS)
print("operator verdict recorded verbatim from the completed review sheet "
      f"§6 (decided_by operator, {TODAY})")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 6 x KEEP_AS_IS")
print("RR settlement: none recorded (zero RR edges authored in batch 5)")
print("held_appendix: acknowledged (14 preserved, quarantined)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
