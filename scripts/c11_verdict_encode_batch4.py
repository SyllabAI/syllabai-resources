#!/usr/bin/env python3
"""T-C11 session 54 — encode the OPERATOR VERDICT SET for §16 batch 4 into
the operator-owned verdict record scripts/c11_batch4_verdicts.yaml.

The operator ruled on the batch-4 gate (review sheet
graph/reports/C11_BATCH4_REVIEW_SHEET.md, session-53 package) with the
practical verdict policy of the session-54 tasking (2026-09-13), including
the two special-attention directives: FP-B4-1 (the bond-energy ->
covalent-bond boundary row — the evidence was actually inspected) and
FP-B4-2 (the two medium-confidence misconception rows — the mark-scheme
evidence was actually inspected). This script encodes the per-row decisions
from that policy — no verdict invented, no evidence reinterpreted, no ID
guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses if the template rows do not reconcile 1:1 against the batch-4
    decision record (35 SUGGESTED edge triples / ZERO RR triples / 22 node
    codes [17 CONCEPT + 5 MISCONCEPTION] / 14 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (118 HUMAN_VALIDATED = 28 pilot + 28 batch-1 + 23 batch-2 + 39 batch-3
    §18 promotions; 0 batch-4 promotions; §16 authorization AUTHORIZED;
    pilot HOLDs + both RR settlements frozen; 113 nodes / 275 edges).

Verdict policy mapping (recorded verbatim in the file's operator_ruling
block):
  * every edge row          -> CONFIRM  (the existing evidence substantively
    supports each authored relationship and the modeling choice is
    reasonable: 128/128 quote anchors machine-verified G03/c11.4; pass-2
    adversarial review 35/35 with zero demotions; the FLAGGED rows carry
    boundary-evidence-asymmetry / relation-class / medium-confidence
    flags — the normal-ontology-ambiguity class the operator explicitly
    refuses to treat as a blocker)
  * every node row          -> CONFIRM  (no duplicate canonical mint; the
    five cross-section boundary edges reuse the ruled S1 owners; pass-2
    verified 22/22)
  * every identity decision -> KEEP_AS_IS (prefer the existing canonical
    concept; avoid unnecessary splitting or merging; do not redesign the
    S3 ontology — the identity-decision vocabulary has no CONFIRM value)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (14 preserved; a held record is
    a valid outcome — no rescue merely to increase graph coverage)

This script WRITES ONLY scripts/c11_batch4_verdicts.yaml (and removes the
now-renamed template, per the sheet's gate pathway). It promotes nothing
and re-authors no decision record; application (§18 promotion) is the
separate sanctioned step in this same session per the operator's §6
directive ("apply the accepted Batch-4 decisions immediately").
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
TEMPLATE = HERE / "c11_batch4_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch4_verdicts.yaml"
DECISIONS = HERE / "c11_batch4_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"

SESSION = 54
TODAY = "2026-09-13"
# Verbatim operative excerpt from the operator's session-54 directive
# ("T-C11 Batch 4 — Operator Verdicts and Promotion", §2 Practical verdict
# policy).
OPERATOR_STATEMENT = (
    "Use CONFIRM when the existing evidence substantively supports the "
    "relationship/node and the modeling choice is reasonable. Use HOLD "
    "when evidence is insufficient or the relationship is plausible but "
    "not adequately demonstrated by the supplied corpus. Use REJECT when "
    "the evidence does not support the relationship or the "
    "relationship/classification is materially wrong. Do not turn normal "
    "ontology ambiguity into a blocking issue. This is an iterative graph. "
    "We are no longer trying to achieve theoretical perfection before the "
    "system can proceed.")

# ---------------------------------------------------------------------------
# Verdict notes (evidence-grounded context per row; verdicts all per the
# mapping above). Notes cite the operator policy + the pass-2 flag the row
# carries and why it is NOT a blocker under the directive.
# ---------------------------------------------------------------------------
EDGE_NOTES = {
    # FP-B4-1 — the operator's special-attention row, evidence inspected.
    "B4-E-03": (
        "Operator policy (session 54, §3 special attention): CONFIRM as "
        "authored — the FP-B4-1 evidence was actually inspected: the "
        "note's own dependency statement ('To do this it is necessary to "
        "know the bonds present in both the reactants and products'), the "
        "all-covalent worked-example bond set (H-H, Cl-Cl, H-Cl, H-Br, "
        "Br-Br — the 1.44/1.46 diatomic set), and the examiner tip's "
        "displayed-formula-first strategy (the S1 covalent-bond "
        "representation) substantively support the prerequisite; the "
        "session-52 boundary ruling sanctions exactly this target "
        "(batch-3 CON-COVALENT-BOND, no duplicate mint); the note's "
        "'chemical bond' wording caveat is honestly recorded in "
        "derivation_notes with confidence medium — normal ontology "
        "wording, not a blocker."),
    # The other four sanctioned cross-section boundary edges.
    "B4-E-13": (
        "Operator policy (session 54): CONFIRM as authored — OD-1 operand "
        "rule (Delta-H = Q/n uses n), the note's per-mole statement, "
        "session-52 sanctioned target CON-MOLE (pilot), no duplicate "
        "mint."),
    "B4-E-15": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "concentration rate-factor uses the S1 concept without "
        "re-teaching; session-52 sanctioned target CON-CONCENTRATION "
        "(pilot), no duplicate mint."),
    "B4-E-18": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "reversible-notation statement is the S1 eq-symbol usage; "
        "session-52 sanctioned target CON-EQ-SYMBOL (pilot), no "
        "duplicate mint."),
    "B4-E-20": (
        "Operator policy (session 54): CONFIRM as authored — 3.18 owns "
        "the reversible behaviour of the hydrated-copper(II)-sulfate "
        "example, NOT the hydration term (session-52 ruling recorded "
        "exactly this ownership split); sanctioned target CON-WATER-CRYST "
        "(pilot), no duplicate mint."),
    # Relation-class / teach-sequence flagged rows.
    "B4-E-10": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "teach-sequence reading (the 3.2 note teaches the formula inside "
        "the method; the spec's own order 3.2 -> 3.3) matches the "
        "established EXPLICIT_TEACH_SEQUENCE pattern (MOLAR-ENTHALPY -> "
        "HEAT-CALC, operator-CONFIRMED in batch 3); normal ontology "
        "reading, not a blocker."),
    "B4-E-11": (
        "Operator policy (session 54): CONFIRM as authored — the sign "
        "step is the note's own teaching and the spec 3.3 demand "
        "('Exothermic reactions have a negative enthalpy change' — "
        "quote-verified); the MS 'Ignore sign' leniency is a marking "
        "fact, not a modeling defect; the dependency is real and "
        "note-evidenced."),
    "B4-E-14": (
        "Operator policy (session 54): CONFIRM as authored — "
        "EXPLAINED_BY stands on the note's own causal sentence ('We can "
        "use collision theory to explain why these factors influence the "
        "reaction rate'); the weaker prerequisite reading is a "
        "theoretical alternative interpretation, not a blocker; one "
        "relation per pair per the ratified discipline."),
    "B4-E-16": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "profile's peak IS the activation energy ('The initial increase "
        "in energy, from the reactants to the peak of the curve, "
        "represents the activation energy' — quote-verified); the "
        "dual-node companion shape on 3.14C is B4-ID-04 KEEP_AS_IS (the "
        "B3-ID-05 1.58C precedent)."),
    # FP-B4-2 — the two medium-confidence misconception rows, evidence
    # inspected.
    "B4-E-22": (
        "Operator policy (session 54, §3 special attention): CONFIRM as "
        "authored — the FP-B4-2 evidence was actually inspected: the "
        "pinned ENERGETICS Paper-2 MS carries the per-mistake deduction "
        "rule twice on the bond-sum rows ('Deduct 1 mark for each "
        "mistake' on (4 x C-H) + (2 x O=O) and (2 x C=O) + (4 x H-O)), "
        "and the note's examiner tip names the exact mistake class "
        "('Don't forget to take into account the balancing numbers when "
        "working out how many of each type of bond is being "
        "broken/formed'). Two partial sources together document the "
        "wrong-answer pattern with assessment consequences; the honest "
        "medium confidence records the derivation, not a defect."),
    "B4-E-28": (
        "Operator policy (session 54, §3 special attention): CONFIRM as "
        "authored — the FP-B4-2 evidence was actually inspected: the "
        "pinned RRE Paper-2 MS REJECT column carries the byte-verified "
        "entry 'shifts to the side with fewer (gas) moles/molecules'; a "
        "Reject-column entry is by definition a recorded wrong answer "
        "students give; the antonym-pairing attribution (three reject "
        "entries -> three sub-questions) is sound and recorded in "
        "derivation_notes; the remediation quotes are note-verified. The "
        "honest medium confidence records the column attribution method, "
        "not a defect."),
    # The remediation-target=WAP-target rows (the B1-E-25 pattern).
    "B4-E-21": (
        "Operator policy (session 54): CONFIRM as authored — remediation "
        "target equals the WAP target (the batch-1 B1-E-25 pattern, "
        "operator-CONFIRMED in batches 1-3); kept for "
        "misconception-recommendation queries (node remediation_evidence "
        "also carries the corrective text)."),
    "B4-E-23": (
        "Operator policy (session 54): CONFIRM as authored — remediation "
        "target equals the WAP target (the B1-E-25 pattern); the "
        "corrective text ('The alternative pathway has a lower "
        "activation energy') is note-verified."),
    "B4-E-25": (
        "Operator policy (session 54): CONFIRM as authored — remediation "
        "target equals the WAP target (the B1-E-25 pattern); the J-to-kJ "
        "conversion rule is note-verified."),
    "B4-E-27": (
        "Operator policy (session 54): CONFIRM as authored — remediation "
        "target equals the WAP target (the B1-E-25 pattern); both "
        "directions of the molecule-count rule are note-verified."),
    "B4-E-29": (
        "Operator policy (session 54): CONFIRM as authored — remediation "
        "target equals the WAP target (the B1-E-25 pattern); the "
        "endothermic-direction shift rule is note-verified."),
}
NODE_NOTES = {
    # The identity-flagged concept nodes (their fold/split questions are
    # the ID rows below — all KEEP_AS_IS).
    "B4-N-01": (
        "Operator policy (session 54): CONFIRM as authored — the dual "
        "node attachment on 3.14C stands (B4-ID-04 KEEP_AS_IS: concept "
        "vs representation, the B3-ID-05 1.58C precedent; both "
        "independently assessable)."),
    "B4-N-05": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "know+know dual attachment (3.12 definition + 3.13 mechanism) "
        "stays one node (B4-ID-01 KEEP_AS_IS: the ratified 1.19/1.20 + "
        "B3-ID-01 know-pair precedents; one note teaches both)."),
    "B4-N-07": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "know+know dual attachment (3.19C sealed-container reach + 3.20C "
        "characteristics) stays one node (B4-ID-02 KEEP_AS_IS; one note "
        "teaches both)."),
    "B4-N-09": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "know+understand dual attachment (3.21C catalyst rule + 3.22C "
        "temperature/pressure shifts) stays one node (B4-ID-03 "
        "KEEP_AS_IS; Le Chatelier stays a corpus-evidenced alias while "
        "the spec de-scopes the name — FN-B4-3 records the gap "
        "explicitly)."),
    "B4-N-13": (
        "Operator policy (session 54): CONFIRM as authored — the 3.9 "
        "experiments node stays separate (B4-ID-06 KEEP_AS_IS: distinct "
        "spec demands — describe the experiments vs describe the "
        "factors; two notes cover them)."),
    "B4-N-14": (
        "Operator policy (session 54): CONFIRM as authored — the 3.10 "
        "factors node stays separate (B4-ID-06 KEEP_AS_IS); its "
        "EXPLAINED_BY edge (B4-E-14 CONFIRM) carries the 3.11 causal "
        "link; the directionless experiments-vs-factors edge stays held "
        "(B4-H-03)."),
    "B4-N-15": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "representation node on 3.14C stays separate from the concept "
        "node (B4-ID-04 KEEP_AS_IS; the dual-node attachment precedent)."),
    "B4-N-17": (
        "Operator policy (session 54): CONFIRM as authored — the named-"
        "examples node (3.18) stays separate from the concept/notation "
        "node (3.17) (B4-ID-05 KEEP_AS_IS: distinct spec demands, "
        "distinct learning surfaces)."),
    # The two medium-confidence misconception nodes (FP-B4-2).
    "B4-M-01": (
        "Operator policy (session 54, §3 special attention): CONFIRM as "
        "authored — the mark-scheme evidence really establishes the "
        "misconception as a documented wrong-answer pattern: the "
        "ENERGETICS Paper-2 MS per-mistake deduction rule (twice, on the "
        "bond-sum rows) + the examiner tip naming the mistake class "
        "(ignoring balancing numbers in bond counting); honest medium "
        "confidence recorded, not a defect."),
    "B4-M-04": (
        "Operator policy (session 54, §3 special attention): CONFIRM as "
        "authored — the mark-scheme evidence really establishes the "
        "misconception as a documented wrong-answer pattern: the RRE "
        "Paper-2 MS REJECT entry 'shifts to the side with fewer (gas) "
        "moles/molecules' (byte-verified) records that students give "
        "this wrong answer; the antonym-pairing column attribution is "
        "recorded in derivation_notes; honest medium confidence "
        "recorded, not a defect."),
    "B4-M-05": (
        "Operator policy (session 54): CONFIRM as authored — the "
        "reject/accept antonym pair ('moves in the exothermic direction' "
        "rejected for the endothermic-direction answer) is "
        "layout-robust; the corrective rule is note-verified."),
}
ID_NOTES = {
    "B4-ID-01": (
        "Operator policy (session 54, §4): KEEP_AS_IS — the catalyst "
        "know+know dual attachment (3.12 definition + 3.13 mechanism) "
        "stays one node: the ratified 1.19/1.20 + B3-ID-01 know-pair "
        "precedents; the simplest representation that preserves the "
        "distinction without a duplicate canonical concept. B4-N-05 "
        "confirmed as authored."),
    "B4-ID-02": (
        "Operator policy (session 54, §4): KEEP_AS_IS — "
        "CON-DYNAMIC-EQUILIBRIUM keeps the 3.19C sealed-container reach "
        "and 3.20C characteristics as one node (same know-pair "
        "precedents; one note teaches both). B4-N-07 confirmed as "
        "authored."),
    "B4-ID-03": (
        "Operator policy (session 54, §4): KEEP_AS_IS — CON-EQ-POSITION "
        "keeps the 3.21C catalyst rule and 3.22C temperature/pressure "
        "shift rules as one node (know+understand dual attachment, the "
        "ratified precedent; one note covers both). B4-N-09 confirmed as "
        "authored."),
    "B4-ID-04": (
        "Operator policy (session 54, §4): KEEP_AS_IS — "
        "CON-ACTIVATION-ENERGY (the concept) and CON-REACTION-PROFILE "
        "(the representation) stay separate nodes on 3.14C: concept vs "
        "representation is a meaningful distinction, independently "
        "assessable (the B3-ID-05 1.58C dual-node precedent). No merge: "
        "merging would fold a draw-skill into a definition. B4-N-01 / "
        "B4-N-15 confirmed as authored."),
    "B4-ID-05": (
        "Operator policy (session 54, §4): KEEP_AS_IS — "
        "CON-REVERSIBLE-EXAMPLES stays a separate 3.18 node (the named "
        "reversible reactions are a distinct describe demand with "
        "distinct learning surfaces); no fold into CON-REVERSIBLE. "
        "B4-N-17 confirmed as authored."),
    "B4-ID-06": (
        "Operator policy (session 54, §4): KEEP_AS_IS — "
        "CON-RATE-EXPERIMENTS (3.9) and CON-RATE-FACTORS (3.10) stay "
        "separate nodes: distinct spec demands (describe the experiments "
        "vs describe the factors), two notes; the directionless "
        "prerequisite between them stays held (B4-H-03). No fold. B4-N-13 "
        "/ B4-N-14 confirmed as authored."),
}
HELD_NOTE = (
    "Operator policy (session 54, §5): the 14 held candidates "
    "(B4-H-01..14) stay held — quarantined, no reopening, no rescue. A "
    "held record is a valid outcome; held candidates are not rescued "
    "merely to increase graph coverage. The four CLASSIC misconceptions "
    "(B4-H-08..11 — static equilibrium, consumed catalyst, "
    "catalyst-shifts-position, bond-breaking exo/endo swap) revisit only "
    "with new mark-scheme evidence documenting the wrong answers; the "
    "unaudited sixth boundary edge (B4-H-14) stays outside the "
    "five-target session-52 ruling.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH4_REVIEW_SHEET (session-53 "
    "package) — verdicts recorded by operator decision, session 54 "
    "(2026-09-13).")
META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "mapping": (
        "The operator ruled verdicts and immediate promotion in one "
        "session ('Once the verdict file is complete and validated: apply "
        "the accepted Batch-4 decisions immediately through the existing "
        "operator-only promotion mechanism. Do not create another "
        "approval cycle... The operator verdict file itself is the "
        "authorization.'). Special attention was paid as directed "
        "(§3): FP-B4-1 — the bond-energy -> covalent-bond boundary row's "
        "evidence was actually inspected (the note's own "
        "'necessary to know the bonds present' dependency statement, the "
        "all-covalent worked-example bond set, the displayed-formula "
        "examiner tip, and the authoritative session-52 boundary ruling "
        "sanctioning exactly this target) — the existing evidence is "
        "sufficient for the authored relationship and relation class; "
        "FP-B4-2 — both medium-confidence misconception rows' "
        "mark-scheme evidence was actually inspected (the ENERGETICS MS "
        "per-mistake deduction rule on the bond-sum rows + the tip "
        "naming the mistake class; the RRE MS byte-verified REJECT entry "
        "'shifts to the side with fewer (gas) moles/molecules' with the "
        "antonym-pairing attribution recorded) — both really are "
        "documented wrong-answer patterns. Applied per row: every edge "
        "row CONFIRM (the existing evidence substantively supports each "
        "authored relationship and the modeling choice is reasonable — "
        "128/128 quote anchors machine-verified G03/c11.4; pass-2 "
        "adversarial review 35/35 with zero demotions; the FLAGGED rows "
        "carry boundary-evidence-asymmetry / relation-class / "
        "medium-confidence flags, the normal-ontology-ambiguity class "
        "the operator explicitly refuses to treat as a blocker); every "
        "node row CONFIRM (no duplicate canonical mint; the five "
        "cross-section boundary edges reuse the ruled S1 owners; pass-2 "
        "verified 22/22); each identity decision KEEP_AS_IS (prefer the "
        "existing canonical concept; avoid unnecessary splitting or "
        "merging; do not redesign the S3 ontology — no merge, no split, "
        "no boundary re-scope); and the held appendix stays quarantined "
        "(a held record is a valid outcome — no rescue merely to "
        "increase graph coverage). This batch authored NO "
        "REVIEW_REQUIRED edge, so no RR settlement row exists. Verdicts "
        "recorded session 54; the application state lives in "
        "scripts/c11_promotions.yaml (the §18 pathway is the only "
        "HUMAN_VALIDATED source) — this file never carries promotion "
        "payload or promoted status. Changing a recorded verdict "
        "requires an explicit operator decision."),
}


def die(msg: str):
    print(f"FAIL-CLOSED: {msg}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Load + pre-state assertions
# ---------------------------------------------------------------------------
if VERDICTS.exists():
    die("scripts/c11_batch4_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch4_verdicts_template.yaml missing — the "
        "session-53 package must be intact")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-4 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-53 surface)
assert [r["id"] for r in doc["edge_verdicts"]] == \
    [f"B4-E-{i:02d}" for i in range(1, 36)]
assert [r["id"] for r in doc["node_verdicts"]] == \
    [f"B4-N-{i:02d}" for i in range(1, 18)] + \
    [f"B4-M-{i:02d}" for i in range(1, 6)]
assert [r["id"] for r in doc["identity_decisions"]] == \
    [f"B4-ID-{i:02d}" for i in range(1, 7)]

# 3. reconcile against the batch-4 decision record + the live store
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
assert len(b_edges) == 35, len(b_edges)
assert len(b_suggested) == 35 and len(b_rr) == 0
if sorted(tmpl_triples) != sorted(b_suggested) \
        or len(set(tmpl_triples)) != 35:
    die("edge triple mismatch between verdict template and the batch-4 "
        "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
if sorted(tmpl_codes) != sorted(b_codes) or len(set(tmpl_codes)) != 22:
    die("node code mismatch between verdict template and the batch-4 "
        "decision record")
assert len(dec["held"]) == 14, len(dec["held"])

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
if len(hv) != 118 or hv != store_triples:
    die("live HUMAN_VALIDATED set != the 118 pilot+batch-1+batch-2+batch-3 "
        "§18 promotions (the pre-verdict state must be frozen before "
        "recording batch-4 verdicts)")
if hv & set(b_suggested):
    die("a batch-4 edge is already HUMAN_VALIDATED — pre-verdict state "
        "violated")
if auth.get("authorization", {}).get("decision") != "AUTHORIZED":
    die("§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
if any(p.get("validated_by") != "operator" for p in promo["promotions"]):
    die("existing promotions carry non-operator attribution (anti-forgery)")
assert len(nodes_doc["nodes"]) == 113, len(nodes_doc["nodes"])
assert len(edges_doc["edges"]) == 275, len(edges_doc["edges"])

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
    "# T-C11 §16 batch 4 — OPERATOR verdict record (session-53 package), "
    "FILLED by operator decision session 54 (2026-09-13). OPERATOR-OWNED.\n"
    "# Operator verdict policy (session-54 directive, §2 Practical verdict "
    "policy): CONFIRM when\n"
    "# the existing evidence substantively supports the relationship/node "
    "and the modeling choice\n"
    "# is reasonable; HOLD/REJECT only for genuine evidence insufficiency "
    "or a materially wrong\n"
    "# relationship/classification; normal ontology ambiguity is NOT a "
    "blocker — see\n"
    "# meta.operator_ruling for the recorded mapping (incl. the §3 "
    "special-attention rulings on\n"
    "# FP-B4-1 and FP-B4-2, evidence inspected).\n"
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

assert ec == {"CONFIRM": 35}, ec
assert nc == {"CONFIRM": 22}, nc
assert [r["verdict"] for r in chk["identity_decisions"]] == \
    ["KEEP_AS_IS"] * 6
assert "rr_settlement" not in chk
assert chk["held_appendix_acknowledgment"]["acknowledged"] is True
assert chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT
assert not TEMPLATE.exists()

print("wrote", VERDICTS)
print(f"operator verdict policy recorded verbatim "
      f"(decided_by operator, {TODAY})")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 6 x KEEP_AS_IS")
print("RR settlement: none recorded (zero RR edges authored in batch 4)")
print("held_appendix: acknowledged (14 preserved, quarantined)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
