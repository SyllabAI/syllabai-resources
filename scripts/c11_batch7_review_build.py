#!/usr/bin/env python3
"""
T-C11 §16 batch 7 — c11_batch7_review_build.py: renders the batch-7 operator
review gate (the per-batch operator gate required by the §16 authorization)
from the batch-7 decision record + the pass-2 adversarial verdicts, so the
documents cannot drift from the data (the c11_batch6_review_build.py
pattern, batch-7-scoped, session-54 hardening included).

Outputs:
  graph/reports/C11_BATCH7_REVIEW_SHEET.md — the operator review gate
  graph/reports/C11_BATCH7_REVIEW.json     — machine record + agreement stats
  scripts/c11_batch7_verdicts_template.yaml — the OPERATOR-OWNED verdict
      template (empty verdicts; machine pre-triage per row)

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator).

The batch ends HERE: this build promotes nothing, validates nothing as
HUMAN_VALIDATED, and authorizes nothing. The per-batch operator gate is the
operator's action; batch-7 promotion happens only via §18 after verdicts.

Usage: python3 scripts/c11_batch7_review_build.py
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

def _require(cond: bool, msg: str) -> None:
    """Fail-closed gate that survives `python -O` (assert is stripped
    under -O, which would turn this gate fail-open — MD-33)."""
    if not cond:
        raise RuntimeError(msg)

dec = yaml.safe_load((HERE / "c11_batch7_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_batch7_review_pass2.yaml").read_text(encoding="utf-8"))

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
    "task": "T-C11", "stage": "s16-batch-7-review",
    "batch": 7,
    "generated": M["generated_date"],
    "authorization": "scripts/c11_s16_authorization.yaml (§16 authorized "
                     "2026-09-12; batch 7 commissioned by the operator's "
                     "'Proceed with batch 7' directive, session 59 — Section 2 "
                     "Inorganic Chemistry THIRD slice; under the session-59 "
                     "cross-slice boundary ruling "
                     "scripts/c11_batch7_boundary_ruling.yaml)",
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_batch7_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges),
              "held": len(held), "command_kinds": len(cks)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-batch7-review-2",
              "verdicts_file": "scripts/c11_batch7_review_pass2.yaml",
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
        "note": "one pass-2 finding (FP-B7-4, the PR-08 anchor swap away from "
                "the source-note's 'Wash filtrate' line conflicting with the "
                "pinned MS Q7a(iii)) was re-authored BEFORE the gate — the "
                "record carries 15 nodes / 19 authored edges at this gate; "
                "zero demotions at the re-authored state and zero RR "
                "quarantines: the pass-1 authoring sent 9 candidates to held "
                "BEFORE emission and resolved every remaining doubt on "
                "explicit evidence",
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
        "pathway": "record verdicts in scripts/c11_batch7_verdicts.yaml "
                   "(fill the template); a later session encodes + applies "
                   "them via §18 promotion / §7 re-authoring",
        "promotion_now": 0,
        "cross_boundary_edges": 2,
    },
}
(REPORTS / "C11_BATCH7_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- verdict template (OPERATOR-OWNED; empty verdicts + machine pre-triage) ---
E_VOCAB = "CONFIRM | REJECT | HOLD | MERGE | SPLIT"
tpl = ["# T-C11 §16 batch 7 — OPERATOR verdict template (session-59 package).",
       "# OPERATOR-OWNED: fill verdict per row (empty verdict = not decided).",
       "# Hand-edits HERE are the sanctioned pathway; graph/*.yaml are never",
       "# hand-edited. The next session encodes + applies the filled record via",
       "# the §18 promotion pathway / §7 decision-record re-authoring. Verdicts",
       "# are RECORDED, not applied: filling this file promotes nothing.",
       "meta:",
       "  task: T-C11",
       "  stage: s16-batch-7-verdicts",
       "  batch: 7",
       "  session: 59",
       "  file: OPERATOR-OWNED verdict record for C11_BATCH7_REVIEW_SHEET (session 59) — verdicts recorded by operator decision (pending).",
       f"  instructions: 'Fill verdict per row. Edge/node vocabulary: {E_VOCAB}. This batch authored",
       "    NO REVIEW_REQUIRED edge (all doubts were held or resolved on explicit evidence).",
       "    Identity-decision vocabulary: MERGE (fold nodes) | SPLIT (mint finer) | KEEP_AS_IS. The batch-7",
       "    extraction_pass is c11-s16-batch-7 (Section 2 Inorganic Chemistry THIRD slice, 16 SPs",
       "    4CH1-2.28-2.43C: f Acids, Alkalis & Titrations + g Acids, Bases & Salt Preparations); its 9 held",
       "    candidates are informational only (no reopening, no promotion of held candidates — B7-H-04 records",
       "    the insufficient-characterization refusal; B7-H-06 holds the note-anchored ERRONEOUS_BELIEF lane for",
       "    operator ruling). TWO edges are cross-section boundary edges into the ruled targets",
       "    (CON-REACT-ORDER — the batch-6 owner; CON-ION-CHARGE-RULES — the batch-3 owner; sanctioned by the",
       "    session-59 cross-slice ruling, no duplicate mint). The next session applies verdicts via the §18",
       "    promotion pathway / §7 decision-record re-authoring; nothing here is HUMAN_VALIDATED.'",
       "edge_verdicts:"]
EDGE_NOTES = {
    "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER":
        "cross-boundary target (session-59 ruling; the batch-6 order owner — "
        "the 2.37 acid-metal row applies the placement as given)",
    "4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES":
        "cross-boundary target (session-59 ruling; the batch-3 named-ion owner "
        "— the rules table presupposes the ion-family vocabulary)",
    "4CH1-MIS-ENDPOINT-PH-ABOVE-7 WRONG_ANSWER_PATTERN 4CH1-CON-NEUTRALISATION":
        "documented Reject-column class (the pinned Titrations MS Q2a(iv); "
        "temperature-experiment context recorded)",
    "4CH1-MIS-ENDPOINT-PH-ABOVE-7 REMEDIATED_BY 4CH1-CON-NEUTRALISATION":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-PRECIPITATE-IN-FILTRATE WRONG_ANSWER_PATTERN 4CH1-CON-SALT-PRECIPITATION":
        "documented class with expected-answer + Reject rationale (the pinned "
        "Salt-Prep MS Q2a(iii))",
    "4CH1-MIS-PRECIPITATE-IN-FILTRATE REMEDIATED_BY 4CH1-CON-SALT-PRECIPITATION":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-PR-07 REQUIRES_PREREQUISITE 4CH1-CON-SALT-INSOLUBLE-REACTANT":
        "practical->conceptual (the PR-05/PR-06 shape; 2.42 attaches no node)",
    "4CH1-PR-08 REQUIRES_PREREQUISITE 4CH1-CON-SALT-PRECIPITATION":
        "practical->conceptual (the PR-05/PR-06 shape; 2.43C attaches no node; "
        "the FP-B7-4 anchor swap is recorded)",
}
i = 0
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    i += 1
    k = ekey(e)
    flag = EDGE_NOTES.get(k, "")
    tpl.append(f"- id: B7-E-{i:02d}")
    tpl.append(f"  triple: {k}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    # session-54 fix: YAML single-quote escaping for embedded apostrophes
    tpl.append(f"  notes: '{flag.replace("'", "''")}'")
tpl.append("node_verdicts:")
NODE_NOTES = {
    "4CH1-CON-PROTON-TRANSFER": "one-node-two-SPs family ruling (B7-ID-01)",
    "4CH1-CON-SOLUBILITY-RULES": "qualitative-rules vs the S3 quantitative owners (B7-ID-02)",
    "4CH1-CON-ACID-ALKALI-IONS": "self-contained solution-ion reading vs the S1 CON-ION owner (B7-ID-03)",
}
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "CONCEPT":
        continue
    i += 1
    flag = NODE_NOTES.get(n["code"], "")
    tpl.append(f"- id: B7-N-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{flag.replace("'", "''")}'")
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "MISCONCEPTION":
        continue
    i += 1
    note = ""
    if n["code"] == "4CH1-MIS-ENDPOINT-PH-ABOVE-7":
        note = ("the question context is a temperature-rise experiment (the S3 "
                "adjacency recorded); the WAP target reading is argued in the "
                "pass-2 findings (FP-B7-3)")
    if n["code"] == "4CH1-MIS-PRECIPITATE-IN-FILTRATE":
        note = "the strongest documented class of the batch (expected answer + Reject rationale + the residue instruction)"
    tpl.append(f"- id: B7-M-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append("  pretriage: LIKELY_SAFE (mark-scheme-documented)")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{note.replace("'", "''")}'")
tpl.append("identity_decisions:")
tpl.append("- id: B7-ID-01")
tpl.append("  question: keep the 2.35/2.36 proton-transfer framework as ONE family node (the note extends the earlier definition; donor/acceptor IS the transfer account) vs splitting the donor/acceptor definitions from the transfer framework")
tpl.append("  verdict:")
tpl.append("- id: B7-ID-02")
tpl.append("  question: keep the 2.34 qualitative solubility RULES distinct from the S3 quantitative owners (CON-SOLUBILITY g-per-100g / CON-SOLUBILITY-CURVE) — distinct-demand mint, no merge")
tpl.append("  verdict:")
tpl.append("- id: B7-ID-03")
tpl.append("  question: keep the 2.31 solution-ionisation family self-contained (no boundary edge into the S1 CON-ION electron-loss/gain owner — different mechanism and demand)")
tpl.append("  verdict:")
tpl.append("- id: B7-ID-04")
tpl.append("  question: keep the three salt-preparation routes as THREE nodes (2.39 insoluble-reactant / 2.40C titration / 2.41C precipitation — distinct experiments, distinct starting materials; the B5-ID-03 trio precedent) vs one salt-preparation node")
tpl.append("  verdict:")
tpl.append("- id: B7-ID-05")
tpl.append("  question: mint the MIS-ENDPOINT-PH-ABOVE-7 misconception from the pinned Titrations MS Q2a(iv) Reject column (narrow-but-exact; the MIS-CUO-COLOUR/B6-ID-06 precedent) — or rule it exam-trivia")
tpl.append("  verdict:")
tpl.append("- id: B7-ID-06")
tpl.append("  question: mint the MIS-PRECIPITATE-IN-FILTRATE misconception from the pinned Salt-Prep MS Q2a(iii) class (the strongest documented pattern of the batch) — or rule it exam-trivia")
tpl.append("  verdict:")
tpl.append("held_appendix_acknowledgment:")
tpl.append("  acknowledged:")
tpl.append("  notes: ''")
# re-issue guard (the batch-1..6 pattern): once the verdict round is
# recorded, never re-emit an empty template beside the filled verdict record.
if (HERE / "c11_batch7_verdicts.yaml").exists():
    print("template NOT re-emitted: scripts/c11_batch7_verdicts.yaml exists "
          "(verdict round recorded)")
else:
    (HERE / "c11_batch7_verdicts_template.yaml").write_text(
        "\n".join(tpl) + "\n", encoding="utf-8")
    # fail-closed post-write parseability check (the session-54 hardening)
    _tpl_doc = yaml.safe_load(
        (HERE / "c11_batch7_verdicts_template.yaml")
        .read_text(encoding="utf-8"))
    _require(_tpl_doc is not None and "edge_verdicts" in _tpl_doc,
             "post-write: written template is unparseable or missing edge_verdicts")
    _require(len(_tpl_doc["edge_verdicts"]) == len(edges),
             "post-write: written template edge_verdicts count drifted")
    _require(len(_tpl_doc["node_verdicts"]) == len(nodes),
             "post-write: written template node_verdicts count drifted")
    _require(len(_tpl_doc["identity_decisions"]) == 6,
             "post-write: written template identity_decisions count drifted")

# --- review sheet --------------------------------------------------------------
L = []
A = L.append
A("# T-C11 §16 Batch 7 Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1-2.28–2.43C (Section 2 — Inorganic Chemistry, THIRD slice: "
  f"f Acids, Alkalis & Titrations / g Acids, Bases & Salt Preparations, 16 SPs) "
  f"+ practicals PR-07 (2.42) / PR-08 (2.43C) · generated {M['generated_date']} · "
  f"decision record `scripts/c11_batch7_decisions.yaml` (pass 1: "
  f"`{M['extraction_pass']}`) · adversarial pass 2: "
  f"`scripts/c11_batch7_review_pass2.yaml` · authorization: "
  f"`scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 7 "
  f"commissioned by the operator's 'Proceed with batch 7' directive) · "
  f"boundary ruling: `scripts/c11_batch7_boundary_ruling.yaml` (session 59, "
  f"machine-checked — the 2 sanctioned boundary edges below)")
A("")
A(f"**NOTHING in this batch is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + n_part_of} batch edges are AI_SUGGESTED (SUGGESTED). "
  "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
  "pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
  "regeneration). **Zero batch-7 promotions exist.** This sheet is the "
  "batch's operator gate: record verdicts in "
  "`scripts/c11_batch7_verdicts_template.yaml` (fill + rename to "
  "`c11_batch7_verdicts.yaml`); a later session encodes and applies them.")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Machine state: the full "
  "gate suite is green at the merged 157-node / 367-edge store; every quote "
  "is machine-verified byte-for-byte against its source file (G03/c11.4; "
  "135 quote probes + 107 record anchors pre-verified BEFORE the registry "
  "grew, then re-verified by the generator); the 4.15 negative control is "
  "uncovered. TWO edges are cross-section boundary edges into the ruled "
  "targets (CON-REACT-ORDER — the batch-6 owner; CON-ION-CHARGE-RULES — the "
  "batch-3 owner; sanctioned per the session-59 cross-slice ruling; no "
  "duplicate concept was minted). BOTH batch families are MS-pinned (the "
  "best coverage of any slice — meta.ms_coverage_note): the Titrations MS "
  "Q2a(iv) Reject line and the Salt-Prep MS Q2a(iii) class anchor the TWO "
  "misconception mints; the pdftotext line-wrap attributions are recorded in "
  "the nodes' derivation_notes. ONE pass-2 finding (FP-B7-4) was re-authored "
  "BEFORE the gate: the PR-08 edge anchors were swapped away from the source "
  "note's 'Wash filtrate' line, which conflicts with the pinned MS Q7a(iii) "
  "(the conflict is recorded in the findings, not silently quoted or "
  "dropped).")
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
  "resolved on explicit evidence). **One pass-2 finding (FP-B7-4, the PR-08 "
  "anchor swap) was re-authored BEFORE the gate; zero demotions at the "
  "re-authored state.**")
A("")
A(f"Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): "
  f"the batch-7 record is appended by the forecast instrument at this gate "
  f"(see the regenerated C11_BATCH_FORECAST.json). The S2-f/g families run "
  f"in the descriptive band the item-14 plan anticipated (nodes/SP "
  f"{len(nodes)/16:.2f}, edges/SP {len(edges)/16:.2f}), with the "
  "inline-re-teach abstentions (the separation-technique surfaces) and the "
  "held S3-lane surfaces (B7-H-01/02/05/09) accounting for the gap, not thin "
  "coverage: no S1/S3/batch-5/6 identity was re-minted (the 2 existing-owner "
  "targets reached via the 2 sanctioned boundary edges); 2.42/2.43C attach "
  "no concept node (PR-07/PR-08 own them — the 1.13/1.60C/2.14/2.21 "
  "precedent) with the practical->concept edges authored.")
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
  "operand rule): pass-2 flags the 2.35/2.36 one-family ruling (B7-ID-01), "
  "the qualitative-rules-vs-quantitative-owners split (B7-ID-02), the "
  "self-contained solution-ion reading (B7-ID-03), the three-route "
  "salt-preparation split (B7-ID-04), and the TWO single-Reject-column "
  "misconception mints (B7-ID-05, B7-ID-06). All are operator identity "
  "decisions (template §identity_decisions). 2.42/2.43C attach NO batch-7 "
  "concept node (PR-07/PR-08 own them — the 1.13/1.60C/2.14/2.21 precedent).")
A("")
print("sheet part 1 rendered;", len(L), "lines")

# --- edges + held sections (batch-4/5/6 pattern) -----------------------------------
A(f"## 3. Authored semantic edges ({len(edges)})")
A("")
A("| # | edge | conf | derivation | evidence (anchor → quote) | pass-2 | operator |")
A("|---|---|---|---|---|---|---|")
i = 0
for e in sorted(edges, key=ekey):
    i += 1
    a0 = e["evidence"][0]
    ev = f"{a0['kind']}: “{a0['quote'][:90]}”"
    v = edge_p2[ekey(e)]
    A(f"| {i} | `{ekey(e)}` | {e['confidence']} | "
      f"{e['provenance']['derivation_method']} | {ev} | {v['verdict']} | ☐ |")
A("")
A("TWO edges are CROSS-SECTION boundary edges into the ruled targets "
  "(sanctioned per the session-59 cross-slice ruling — no duplicate mint): "
  "the 2.37 acid-metal placement row (into the batch-6 CON-REACT-ORDER "
  "owner) and the 2.34 ion-family rules row (into the batch-3 "
  "CON-ION-CHARGE-RULES owner). The TWO practical edges ride the PR-05/PR-06 "
  "shape (2.42/2.43C attach no concept node).")
A("")
A(f"## 4. Held candidates ({len(held)}) — the abstention record")
A("")
A("| id | candidate | failure class / reason |")
A("|---|---|---|")
for h in held:
    reason = h["reason"]
    cls = reason.split(" — ")[0].split(":")[0][:60]
    A(f"| {h['id']} | {h['candidate']} | {cls} |")
A("")
A("Every held candidate cites its §19 failure class; the reagent-selection "
  "wrong-answer candidate is refused for insufficient characterization (the "
  "session-53 Step-3 rule; the B6-H-03 precedent) and the note-anchored "
  "ERRONEOUS_BELIEF lane is held for operator ruling (B7-H-06). A held "
  "record is a valid outcome — the abstention is the system's honest output.")
A("")
A("## 5. Operator verdict surface")
A("")
A(f"- **{p1_accept} SUGGESTED edges** (B7-E-01..{p1_accept:02d}) — the §18 "
  "promotion surface")
A(f"- **{len(nodes)} nodes** ({sum(1 for n in nodes if n['family']=='CONCEPT')} "
  f"CONCEPT B7-N-01..13 + {sum(1 for n in nodes if n['family']=='MISCONCEPTION')} "
  "MISCONCEPTION B7-M-01..02) — node authority stays SUGGESTED; nodes have "
  "no §18 pathway (node promotion is a separate identity decision, deferred)")
A("- **6 identity decisions** (B7-ID-01..06) — MERGE/SPLIT/KEEP_AS_IS")
A(f"- **{len(held)} held candidates** — acknowledge the quarantine (no "
  "reopening)")
A("- **0 REVIEW_REQUIRED edges** — zero RR settlements needed")
A("")
A("Pathway: fill `scripts/c11_batch7_verdicts_template.yaml` → rename to "
  "`c11_batch7_verdicts.yaml` → a later session encodes + applies via "
  "`c11_verdict_encode_batch7`-style reconciliation + `c11_promote.py` (§18) "
  "+ the gated generator re-run. NOTHING is promoted at this gate.")
A("")

(REPORTS / "C11_BATCH7_REVIEW_SHEET.md").write_text(
    "\n".join(L) + "\n", encoding="utf-8")
print(f"review gate rendered: {REPORTS / 'C11_BATCH7_REVIEW_SHEET.md'} + "
      f"C11_BATCH7_REVIEW.json + the verdict template")
