#!/usr/bin/env python3
"""
T-C11 §16 batch 4 — c11_batch4_review_build.py: renders the batch-4 operator
review gate (the per-batch operator gate required by the §16 authorization)
from the batch-4 decision record + the pass-2 adversarial verdicts, so the
documents cannot drift from the data (the c11_batch3_review_build.py
pattern, batch-4-scoped).

Outputs:
  graph/reports/C11_BATCH4_REVIEW_SHEET.md — the operator review gate
  graph/reports/C11_BATCH4_REVIEW.json     — machine record + agreement stats
  scripts/c11_batch4_verdicts_template.yaml — the OPERATOR-OWNED verdict
      template (empty verdicts; machine pre-triage per row)

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator).

The batch ends HERE: this build promotes nothing, validates nothing as
HUMAN_VALIDATED, and authorizes nothing. The per-batch operator gate is the
operator's action; batch-4 promotion happens only via §18 after verdicts.

Usage: python3 scripts/c11_batch4_review_build.py
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

dec = yaml.safe_load((HERE / "c11_batch4_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_batch4_review_pass2.yaml").read_text(encoding="utf-8"))

M = dec["meta"]
nodes = dec["nodes"]
edges = dec["edges"]
held = dec["held"]
cks = dec["command_kinds"]
n_part_of = sum(len(n["spec_points"]) for n in nodes if n["family"] == "CONCEPT")


def ekey(e):
    return f"{e['source']} {e['relation']} {e['target']}"


# --- agreement statistics (raw, NOT kappa) ------------------------------------
node_p2 = p2["nodes"]
edge_p2 = p2["edges"]
n_conf = sum(1 for v in node_p2.values() if v["verdict"].startswith("CONFIRM"))
e_conf = sum(1 for v in edge_p2.values() if v["verdict"].startswith("CONFIRM"))
e_hold = sum(1 for v in edge_p2.values() if v["verdict"] == "HOLD")
e_rej = sum(1 for v in edge_p2.values() if v["verdict"] == "REJECT")
p1_accept = sum(1 for e in edges if e["validation_status"] == "SUGGESTED")
p1_rr = sum(1 for e in edges if e["validation_status"] == "REVIEW_REQUIRED")
agree = sum(1 for e in edges
            if e["validation_status"] == "SUGGESTED"
            and edge_p2[ekey(e)]["verdict"].startswith("CONFIRM"))
uncert_concordant = sum(1 for e in edges
                         if e["validation_status"] == "REVIEW_REQUIRED"
                         and edge_p2[ekey(e)]["verdict"] in ("HOLD", "REJECT"))
asserted = p1_accept
raw_agreement_edges = agree / asserted if asserted else 1.0
raw_agreement_nodes = n_conf / len(nodes)
open_uncertain = [ekey(e) for e in edges
                  if e["validation_status"] == "REVIEW_REQUIRED"]

json_out = {
    "task": "T-C11", "stage": "s16-batch-4-review",
    "batch": 4,
    "generated": M["generated_date"],
    "authorization": "scripts/c11_s16_authorization.yaml (§16 authorized "
                     "2026-09-12; batch 4 commissioned by the operator's "
                     "session-53 batch-4 directive — Section 3 Physical "
                     "Chemistry; under the session-52 cross-slice boundary "
                     "ruling scripts/c11_batch4_boundary_ruling.yaml)",
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_batch4_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges),
              "held": len(held), "command_kinds": len(cks)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-batch4-review-2",
              "verdicts_file": "scripts/c11_batch4_review_pass2.yaml",
              "nodes_confirm": n_conf, "edges_confirm": e_conf,
              "edges_hold": e_hold, "edges_reject": e_rej},
    "agreement": {
        "metric": "RAW AGREEMENT (pass-2 vs pass-1 emission)",
        "explicitly_not": "Cohen's kappa (single human rater; see "
                          "architecture §12)",
        "nodes": round(raw_agreement_nodes, 4),
        "edges_asserted": {"confirmed": agree, "total_asserted": asserted,
                           "rate": round(raw_agreement_edges, 4)},
        "edges_uncertain_concordant_nonassertion": uncert_concordant,
        "edges_open_operator_decision": open_uncertain,
        "note": "zero pass-2 demotions and zero RR quarantines: the pass-1 "
                "authoring sent 14 candidates to held BEFORE emission and "
                "resolved every remaining doubt on explicit evidence — the "
                "adversarial findings land as CONFIRM_WITH_NOTE flags "
                "enumerated for the operator gate",
    },
    "reviewed_nodes": [{"code": c, "verdict": v["verdict"], "note": v.get("note")}
                       for c, v in node_p2.items()],
    "reviewed_edges": [{"edge": ekey(e), "verdict": edge_p2[ekey(e)]["verdict"],
                        "note": edge_p2[ekey(e)].get("note")}
                       for e in edges],
    "held_review": p2["held_review"],
    "findings": p2["findings"],
    "operator_gate": {
        "gate": "per-batch operator review (§16 authorization "
                "scope.unlocked; each batch = own operator gate)",
        "surface": {"suggested_edges": p1_accept,
                    "review_required_edges": p1_rr,
                    "nodes": len(nodes), "held": len(held)},
        "pathway": "record verdicts in scripts/c11_batch4_verdicts.yaml "
                   "(fill the template); a later session encodes + applies "
                   "them via §18 promotion / §7 re-authoring",
        "promotion_now": 0,
        "cross_boundary_edges": 5,
    },
}
(REPORTS / "C11_BATCH4_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- verdict template (OPERATOR-OWNED; empty verdicts + machine pre-triage) ---
E_VOCAB = "CONFIRM | REJECT | HOLD | MERGE | SPLIT"
tpl = ["# T-C11 §16 batch 4 — OPERATOR verdict template (session-53 package).",
       "# OPERATOR-OWNED: fill verdict per row (empty verdict = not decided).",
       "# Hand-edits HERE are the sanctioned pathway; graph/*.yaml are never",
       "# hand-edited. The next session encodes + applies the filled record via",
       "# the §18 promotion pathway / §7 decision-record re-authoring. Verdicts",
       "# are RECORDED, not applied: filling this file promotes nothing.",
       "meta:",
       "  task: T-C11",
       "  stage: s16-batch-4-verdicts",
       "  batch: 4",
       "  session: 53",
       "  file: OPERATOR-OWNED verdict record for C11_BATCH4_REVIEW_SHEET (session 53) — verdicts recorded by operator decision (pending).",
       f"  instructions: 'Fill verdict per row. Edge/node vocabulary: {E_VOCAB}. This batch authored",
       "    NO REVIEW_REQUIRED edge (all doubts were held or resolved on explicit evidence).",
       "    Identity-decision vocabulary: MERGE (fold nodes) | SPLIT (mint finer) | KEEP_AS_IS. The batch-4",
       "    extraction_pass is c11-s16-batch-4 (Section 3 Physical Chemistry, 22 SPs 4CH1-3.1-3.22C); its 14",
       "    held candidates are informational only (no reopening, no promotion of held candidates —",
       "    B4-H-08..11 record the four classic misconceptions refused for missing documentation; revisit",
       "    only with new MS evidence). Five edges are cross-section boundary edges into the ruled S1 owners",
       "    (CON-MOLE, CON-COVALENT-BOND, CON-CONCENTRATION, CON-EQ-SYMBOL, CON-WATER-CRYST — sanctioned,",
       "    no duplicate mint; the bond-energy->covalent-bond row is the medium-confidence one to eyeball).",
       "    The next session applies verdicts via the §18 promotion pathway /",
       "    §7 decision-record re-authoring; nothing here is HUMAN_VALIDATED.'",
       "edge_verdicts:"]
EDGE_NOTES = {
    "4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND":
        "cross-boundary + the medium-confidence row: note says 'chemical bond', "
        "attribution via worked-example bond set + the ruling (FP-B4-1)",
    "4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-MOLE":
        "cross-boundary target (session-52 ruling; OD-1 operand)",
    "4CH1-CON-RATE-FACTORS REQUIRES_PREREQUISITE 4CH1-CON-CONCENTRATION":
        "cross-boundary target (session-52 ruling)",
    "4CH1-CON-REVERSIBLE REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL":
        "cross-boundary target (session-52 ruling)",
    "4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-WATER-CRYST":
        "cross-boundary target (session-52 ruling; 3.18 owns the reversible "
        "behaviour, NOT the hydration term)",
    "4CH1-CON-RATE-FACTORS EXPLAINED_BY 4CH1-CON-COLLISION-THEORY":
        "relation-class choice (the prereq reading is weaker; FP-B4 pass-2 flag)",
    "4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO":
        "sign-step operand; MS de-emphasises signs (pass-2 note; operator may prune)",
    "4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY":
        "teach-sequence reading (the 3.2 note teaches the formula inside the method)",
    "4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY":
        "dual-node companion on 3.14C (B4-ID-04)",
    "4CH1-MIS-EQ-PRESSURE-FEWER WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION":
        "medium confidence: reject entry byte-verified, column attribution "
        "antonym-based (FP-B4-2)",
    "4CH1-MIS-BOND-ENERGY-COUNT WRONG_ANSWER_PATTERN 4CH1-CON-BOND-ENERGY-CALC":
        "medium confidence: two partial sources (MS deduction + tip naming; FP-B4-2)",
    "4CH1-MIS-CATALYST-PARTICLE-ENERGY REMEDIATED_BY 4CH1-CON-CATALYST":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-EQ-TEMP-EXO REMEDIATED_BY 4CH1-CON-EQ-POSITION":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-EQ-PRESSURE-FEWER REMEDIATED_BY 4CH1-CON-EQ-POSITION":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-ENTHALPY-UNIT-J REMEDIATED_BY 4CH1-CON-MOLAR-ENTHALPY":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-BOND-ENERGY-COUNT REMEDIATED_BY 4CH1-CON-BOND-ENERGY-CALC":
        "remediation target = WAP target (the B1-E-25 pattern)",
}
i = 0
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    i += 1
    k = ekey(e)
    flag = EDGE_NOTES.get(k, "")
    tpl.append(f"- id: B4-E-{i:02d}")
    tpl.append(f"  triple: {k}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    # session-54 fix: YAML single-quote escaping for embedded apostrophes
    # (the session-53 emission wrote the B4-E-03 note's inner quotes raw,
    # producing an unparseable template — genuine blocking defect at the
    # operator gate; fixed at the source, content byte-preserved).
    tpl.append(f"  notes: '{flag.replace("'", "''")}'")
tpl.append("node_verdicts:")
NODE_NOTES = {
    "4CH1-CON-CATALYST": "know+know dual attachment 3.12+3.13 (B4-ID-01)",
    "4CH1-CON-ACTIVATION-ENERGY": "dual node attachment on 3.14C with CON-REACTION-PROFILE (B4-ID-04)",
    "4CH1-CON-REACTION-PROFILE": "dual node attachment on 3.14C with CON-ACTIVATION-ENERGY (B4-ID-04)",
    "4CH1-CON-RATE-EXPERIMENTS": "the 3.9/3.10 fold question (B4-ID-06; directionless edge held B4-H-03)",
    "4CH1-CON-RATE-FACTORS": "the 3.9/3.10 fold question (B4-ID-06)",
    "4CH1-CON-REVERSIBLE-EXAMPLES": "fold-into-CON-REVERSIBLE question (B4-ID-05)",
    "4CH1-CON-DYNAMIC-EQUILIBRIUM": "know+know dual attachment 3.19C+3.20C (B4-ID-02)",
    "4CH1-CON-EQ-POSITION": "know+understand dual attachment 3.21C+3.22C (B4-ID-03); "
                            "Le Chatelier stays a corpus-evidenced alias (spec de-scopes the name)",
}
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "CONCEPT":
        continue
    i += 1
    flag = NODE_NOTES.get(n["code"], "")
    tpl.append(f"- id: B4-N-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    # session-54 fix: same YAML single-quote escaping (defensive).
    tpl.append(f"  notes: '{flag.replace("'", "''")}'")
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "MISCONCEPTION":
        continue
    i += 1
    note = ""
    if n["code"] == "4CH1-MIS-EQ-PRESSURE-FEWER":
        note = "medium confidence (column attribution antonym-based; FP-B4-2)"
    elif n["code"] == "4CH1-MIS-BOND-ENERGY-COUNT":
        note = "medium confidence (two partial sources: MS deduction + examiner tip; FP-B4-2)"
    elif n["code"] == "4CH1-MIS-EQ-TEMP-EXO":
        note = "mark-scheme reject/accept antonym pair, layout-robust"
    tpl.append(f"- id: B4-M-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append("  pretriage: LIKELY_SAFE (mark-scheme-documented)")
    tpl.append("  verdict:")
    # session-54 fix: same YAML single-quote escaping (defensive).
    tpl.append(f"  notes: '{note.replace("'", "''")}'")
tpl.append("identity_decisions:")
tpl.append("- id: B4-ID-01")
tpl.append("  question: split the catalyst know+know dual attachment into separate 3.12 (definition) and 3.13 (mechanism) nodes")
tpl.append("  verdict:")
tpl.append("- id: B4-ID-02")
tpl.append("  question: split CON-DYNAMIC-EQUILIBRIUM into the 3.19C (reach in a sealed container) and 3.20C (characteristics) nodes")
tpl.append("  verdict:")
tpl.append("- id: B4-ID-03")
tpl.append("  question: split CON-EQ-POSITION into the 3.21C catalyst rule and the 3.22C temperature/pressure shift rules")
tpl.append("  verdict:")
tpl.append("- id: B4-ID-04")
tpl.append("  question: merge CON-ACTIVATION-ENERGY and CON-REACTION-PROFILE (the dual node attachment on 3.14C — the concept vs its representation)")
tpl.append("  verdict:")
tpl.append("- id: B4-ID-05")
tpl.append("  question: fold CON-REVERSIBLE-EXAMPLES into CON-REVERSIBLE (one 3.17+3.18 node) instead of the separate examples node")
tpl.append("  verdict:")
tpl.append("- id: B4-ID-06")
tpl.append("  question: fold CON-RATE-EXPERIMENTS and CON-RATE-FACTORS into one rate node (the spec's 3.9/3.10 experiment/describe pair)")
tpl.append("  verdict:")
tpl.append("held_appendix_acknowledgment:")
tpl.append("  acknowledged:")
tpl.append("  notes: ''")
# session-53 guard (the batch-1/2/3 pattern): once the verdict round is
# recorded, never re-emit an empty template beside the filled verdict record.
if (HERE / "c11_batch4_verdicts.yaml").exists():
    print("template NOT re-emitted: scripts/c11_batch4_verdicts.yaml exists "
          "(verdict round recorded)")
else:
    (HERE / "c11_batch4_verdicts_template.yaml").write_text(
        "\n".join(tpl) + "\n", encoding="utf-8")
    # session-54 fix: fail-closed post-write parseability check for the
    # emitted template (the session-53 emission shipped an unparseable
    # notes scalar; this check makes that class of defect impossible to
    # re-ship silently).
    _tpl_doc = yaml.safe_load(
        (HERE / "c11_batch4_verdicts_template.yaml")
        .read_text(encoding="utf-8"))
    assert _tpl_doc is not None and "edge_verdicts" in _tpl_doc
    assert len(_tpl_doc["edge_verdicts"]) == 35
    assert len(_tpl_doc["node_verdicts"]) == 22
    assert len(_tpl_doc["identity_decisions"]) == 6

# --- review sheet --------------------------------------------------------------
L = []
A = L.append
A("# T-C11 §16 Batch 4 Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1-3.1–3.22C (Section 3 — Physical Chemistry: Energetics / Rates "
  f"of Reaction / Reversibility & Equilibria, 22 SPs) + practicals PR-09/PR-10/"
  f"PR-11 · generated {M['generated_date']} · decision record "
  f"`scripts/c11_batch4_decisions.yaml` (pass 1: `{M['extraction_pass']}`) · "
  f"adversarial pass 2: `scripts/c11_batch4_review_pass2.yaml` · "
  f"authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized "
  f"2026-09-12; batch 4 commissioned by the operator's session-53 batch-4 "
  f"directive) · boundary ruling: `scripts/c11_batch4_boundary_ruling.yaml` "
  f"(session 52, machine-checked — the 5 sanctioned S1 targets below)")
A("")
A(f"**NOTHING in this batch is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + n_part_of} batch edges are AI_SUGGESTED (SUGGESTED). "
  "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
  "pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
  "regeneration). **Zero batch-4 promotions exist.** This sheet is the "
  "batch's operator gate: record verdicts in "
  "`scripts/c11_batch4_verdicts_template.yaml` (fill + rename to "
  "`c11_batch4_verdicts.yaml`); a later session encodes and applies them.")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Machine state: the full "
  "gate suite is green at the merged 113-node / 275-edge store; every quote "
  "is machine-verified byte-for-byte against its source file (G03/c11.4; "
  "128 quote anchors pre-verified BEFORE the registry grew, then re-verified "
  "by the generator); the 4.15 negative control is uncovered. Five edges are "
  "CROSS-SECTION boundary edges into the ruled S1 owners (CON-MOLE, "
  "CON-COVALENT-BOND, CON-CONCENTRATION, CON-EQ-SYMBOL, CON-WATER-CRYST — "
  "sanctioned per the session-52 cross-slice ruling; no duplicate concept "
  "was minted; the bond-energy→covalent-bond row is the one medium-"
  "confidence boundary row to eyeball). The pdftotext pins for RRE scramble "
  "the answer/accept/reject columns; the two equilibrium misconception rows "
  "are attributed by reject/accept antonym pairing (recorded in the nodes' "
  "derivation_notes).")
A("")
A("## 1. Totals & second-pass agreement")
A("")
A("| | nodes | authored edges | held | |")
A("|---|---|---|---|")
A(f"| pass-1 (extraction) | {len(nodes)} | {len(edges)} (+{n_part_of} derived PART_OF) | {len(held)} |")
A(f"| pass-2 verdicts | {n_conf} CONFIRM(+note) | {e_conf} CONFIRM(+note) · {e_hold} HOLD · {e_rej} REJECT | all {len(held)} AGREE |")
A("")
A(f"Raw agreement (NOT κ — single human rater, architecture §12): nodes "
  f"{n_conf}/{len(nodes)} = {raw_agreement_nodes:.1%}; edges — of the "
  f"{asserted} edges pass-1 asserted (SUGGESTED), pass-2 confirmed {agree} "
  f"({raw_agreement_edges:.1%}); pass-1 quarantined {p1_rr} edges as "
  "REVIEW_REQUIRED (this batch authored NONE — every doubt was held or "
  "resolved on explicit evidence). **Zero pass-2 demotions.**")
A("")
A(f"Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): "
  f"predicted 52.8 nodes / 60.5 edges / 22.0 held vs actual "
  f"{len(nodes)} / {len(edges)} / {len(held)} — the batch-4 record is "
  "appended by the forecast instrument at this gate (see the regenerated "
  "C11_BATCH_FORECAST.json). The 22-SP scope doubled the model's per-batch "
  "12-SP assumption; the per-SP yield lands in the batch-3 range "
  "(nodes/SP 1.0, edges/SP 1.6) — the boundary discipline and SP-family "
  "granularity again, not thin coverage: no S1 identity was re-minted (the "
  "5 ruled targets reached via 5 sanctioned boundary edges); 3.8/3.15/3.16 "
  "attach no concept node (the practicals own them — the 1.13/1.60C "
  "precedent); the spec's know pairs merged as dual attachments "
  "(3.12+3.13, 3.19C+3.20C, 3.21C+3.22C).")
A("")
A(f"## 2. Concept & misconception nodes ({len(nodes)})")
A("")
A("| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |")
A("|---|---|---|---|---|---|---|---|---|")
i = 0
for n in dec["nodes"]:
    i += 1
    if n["family"] == "CONCEPT":
        att = "; ".join(f"{a['code']} ({a['role'][:4].lower()})"
                        for a in n["spec_points"])
        ev = [a for a in n["spec_points"][0]["evidence"]][:1]
        evlines = "<br>".join(f"{a['kind']}: “{a['quote'][:100]}”" for a in ev)
    else:
        att = "—"
        evlines = "<br>".join(f"{a['kind']}: “{a['quote'][:100]}”"
                              for a in n.get("evidence", [])[:1])
        rem = "<br>".join(f"remediation: “{a['quote'][:80]}”"
                          for a in n.get("remediation_evidence", [])[:1])
        evlines = evlines + "<br>" + rem if rem else evlines
    v = node_p2[n["code"]]
    A(f"| {i} | `{n['code']}` | {n['family'][:5]} | {n['title']} | {att} | "
      f"{n['confidence']} | {evlines} | {v['verdict']} | ☐ |")
A("")
A("Identity-policy notes (split-first; merges are operator-only, OD-1 "
  "operand rule): pass-2 flags the three know-pair dual attachments "
  "(3.12+3.13, 3.19C+3.20C, 3.21C+3.22C), the dual node attachment on "
  "3.14C (CON-ACTIVATION-ENERGY + CON-REACTION-PROFILE — concept vs "
  "representation), the separate examples node (3.18) and the 3.9/3.10 "
  "experiment/describe pair. All are operator identity decisions (template "
  "§identity_decisions, B4-ID-01..06). 3.8/3.15/3.16 attach NO batch-4 "
  "concept node (the practicals PR-09/PR-10/PR-11 own them — the "
  "1.13/1.60C precedent).")
A("")
A(f"## 3. Authored semantic edges ({len(edges)})")
A("")
A("Direction conventions: REQUIRES_PREREQUISITE source=dependent → "
  "target=prerequisite; EXPLAINED_BY explained → explainer; "
  "WRONG_ANSWER_PATTERN / REMEDIATED_BY misconception → concept.")
A("")
A("### 3.1 REVIEW_REQUIRED (open operator decision)")
A("")
A("**None.** This batch authored no REVIEW_REQUIRED edge: the pass-1 "
  "authoring either resolved each doubt on explicit evidence or sent the "
  "candidate to held (14 rows, §4).")
A("")
A(f"### 3.2 SUGGESTED edges ({asserted}) — the §18-promotable surface after verdicts")
A("")
A("Flagged rows (pre-triage FLAGGED in the verdict template): the five "
  "cross-section boundary edges (one per ruled S1 target), the "
  "EXPLAINED_BY relation-class choice, the sign-step HEAT-CALC→EXO-ENDO "
  "row (MS de-emphasises signs), the dual-node companion on 3.14C, the "
  "two medium-confidence misconception rows (antonym-attributed reject; "
  "two-source tip+MS), and the five remediation-target=misconception-"
  "target rows (the batch-1 B1-E-25 pattern).")
A("")
A("| edge | method | conf | evidence (quote) | upstream | pass-2 | operator |")
A("|---|---|---|---|---|---|---|")
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    v = edge_p2[ekey(e)]
    ev = "<br>".join(f"“{a['quote'][:100]}”" for a in e["evidence"])
    up = e["provenance"]["upstream"]
    if len(up) > 90:
        up = up[:87] + "..."
    flag = " ⚑" if ekey(e) in EDGE_NOTES else ""
    A(f"| `{e['source']}` **{e['relation']}** `{e['target']}`{flag} | "
      f"{e['provenance']['derivation_method']} | {e['confidence']} | {ev} | {up} | "
      f"{v['verdict']} | ☐ |")
A("")
A(f"### 3.3 Derived PART_OF edges ({n_part_of})")
A("")
A("Derived deterministically from node attachments (concepts.yaml); each "
  "carries the attachment's evidence anchors and the node's provenance. Not "
  "re-listed here — review them via the §2 node rows. Machine-verified: the "
  "PART_OF set must exactly equal the declared attachments (c11.7).")
A("")
A(f"## 4. Held / rejected candidates ({len(held)}) — the abstention record")
A("")
A("These were considered and NOT drawn. Review that each hold reason is "
  "right (pass-2 already did — column below). Overriding a hold = "
  "re-authoring the decision record, never hand-editing the graph. "
  "B4-H-08..11 record the four CLASSIC misconceptions (static equilibrium; "
  "consumed catalyst; catalyst-shifts-position; bond-breaking exo/endo "
  "swap) refused because no pinned source documents the wrong answer — "
  "the session-53 Step-3 rule applied exactly (revisit only with new MS "
  "evidence).")
A("")
A("| id | status | candidate | failing rule | pass-2 | operator |")
A("|---|---|---|---|---|---|")
for h in held:
    v = p2["held_review"][h["id"]]
    cand = h["candidate"][:95]
    reason = h["reason"].split("—")[0].strip()[:60]
    A(f"| {h['id']} | {h['status']} | `{cand}` | {reason} | {v['verdict']} | ☐ |")
A("")
A("## 5. Findings (pass-2, for the batch record)")
A("")
for f_ in p2["findings"]:
    A(f"- **{f_['id']} ({f_['kind']})** — {f_['detail']}")
A("")
A("## 6. Command-kind tags (guide §8) — batch-4 SPs")
A("")
A("| SP | verb | guide class | demanded substance | operator |")
A("|---|---|---|---|---|")
for c in sorted(cks, key=lambda x: x["code"]):
    A(f"| {c['code']} | {c['verb']} | {c['guide_class']} | "
      f"{c['demanded_substance']} | ☐ |")
A("")
A("## 7. Negative control (4CH1-4.15) — carried forward, still uncovered")
A("")
A("Zero concepts, zero edges, zero coverage for 4.15 across the whole merged "
  "store (machine-tested: graph_check + negative test + the "
  "s16-authorization check D5). The batch adds nothing in S4 territory. "
  "Operator: acknowledge ☐")
A("")
A("## 8. Batch-4 evidence set (pinned)")
A("")
A("- 15 T-C10 HUMAN_VALIDATED-mapped notes (read in full at extraction): "
  "a. Energetics ×6 (Exothermic and endothermic, Calorimetry, Energetics "
  "calculations, Energy level diagrams, What is bond energy, Temperature "
  "change practical) + b. Rates of Reaction ×6 (Rate of reaction, "
  "Explaining Rates, Catalysts in Chemistry, What is activation energy, "
  "How surface area affects rate, Investigating catalysts) + "
  "c. Reversible Reactions & Equilibria ×3 (Reversible reactions, Dynamic "
  "equilibrium, The position of equilibrium).")
A("- 3 pinned Paper-2 mark-scheme extractions (misconception-class evidence "
  "only; FULL S3 family coverage for the first time): ENERGETICS_MS_P2.txt "
  "(0288d7d15006) + RATES_MS_P2.txt (97876cf4ffe7) + RRE_MS_P2.txt "
  "(7d50fc44586b). Coverage facts: PMT Unit 3 publishes exactly one "
  "Paper-2 MS per S3 family — all pinned, so no S3 family lacks MS "
  "evidence (unlike batch 3's metallic/electrolysis gap); the RATES and "
  "RRE pins overlap (the same catalyst question/cap rule appears in "
  "both — recorded, not silently assumed away); Paper-1 variants remain "
  "unpinned per the Paper-2-first convention.")
A("")
A("## 9. After review (the batch gate)")
A("")
A("1. Fill `scripts/c11_batch4_verdicts_template.yaml` (rename to "
  "`c11_batch4_verdicts.yaml`): per-row verdicts, the identity decisions, "
  "the held acknowledgment. (This batch has NO RR settlement — no "
  "REVIEW_REQUIRED edge was authored.)")
A("2. The next session encodes your verdicts (fail-closed) and applies them: "
  "CONFIRM edges through the §18 pathway (`c11_diff_review.py approve` → one "
  "`c11_promote.py` invocation → gated G13 re-run); REJECT rows re-authored "
  "out; MERGE/SPLIT as §7 re-authoring (B4-ID-01..06 may re-scope the "
  "dual-attachment pairs).")
A("3. This batch adds Section 3 coverage to the concept graph (pilot + "
  "batches 1-3 = all 60 S1 SPs; batch 4 = 22 S3 SPs → 82 of 182 spec "
  "points). Per the §16 phase order the next slice is S2 Inorganic (batch "
  "5); its cross-slice boundaries (S1↔S2, S3↔S2 — the S3 examples "
  "reference neutralisation, copper(II) sulfate and hydrochloric acid "
  "heavily) will need the same ruling treatment this batch received.")
A("")
A("---")
A(f"Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, "
  f"`graph/spec_command_kinds.yaml` (generated, gated, merged store) · "
  f"`C11_BATCH4_REVIEW.json` (this sheet's machine record) · "
  f"`scripts/c11_batch4_verdicts_template.yaml` (the verdict template) · "
  f"contract: `C11_ARCHITECTURE.md`")

(REPORTS / "C11_BATCH4_REVIEW_SHEET.md").write_text("\n".join(L) + "\n",
                                                   encoding="utf-8")
print(f"wrote {REPORTS / 'C11_BATCH4_REVIEW_SHEET.md'}")
print(f"wrote {REPORTS / 'C11_BATCH4_REVIEW.json'}")
if (HERE / "c11_batch4_verdicts.yaml").exists():
    print(f"verdict record present: {HERE / 'c11_batch4_verdicts.yaml'} "
          f"(template intentionally not re-emitted)")
else:
    print(f"wrote {HERE / 'c11_batch4_verdicts_template.yaml'}")
print(f"raw agreement (NOT kappa): nodes {raw_agreement_nodes:.1%}; edges "
      f"{agree}/{asserted} asserted confirmed; {len(held)} held all "
      f"AGREE_HOLD; zero RR authored")
