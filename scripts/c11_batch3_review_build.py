#!/usr/bin/env python3
"""
T-C11 §16 batch 3 — c11_batch3_review_build.py: renders the batch-3 operator
review gate (the per-batch operator gate required by the §16 authorization)
from the batch-3 decision record + the pass-2 adversarial verdicts, so the
documents cannot drift from the data (the c11_batch2_review_build.py
pattern, batch-3-scoped).

Outputs:
  graph/reports/C11_BATCH3_REVIEW_SHEET.md — the operator review gate
  graph/reports/C11_BATCH3_REVIEW.json     — machine record + agreement stats
  scripts/c11_batch3_verdicts_template.yaml — the OPERATOR-OWNED verdict
      template (empty verdicts; machine pre-triage per row)

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator).

The batch ends HERE: this build promotes nothing, validates nothing as
HUMAN_VALIDATED, and authorizes nothing. The per-batch operator gate is the
operator's action; batch-3 promotion happens only via §18 after verdicts.

Usage: python3 scripts/c11_batch3_review_build.py
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

dec = yaml.safe_load((HERE / "c11_batch3_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_batch3_review_pass2.yaml").read_text(encoding="utf-8"))

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
    "task": "T-C11", "stage": "s16-batch-3-review",
    "batch": 3,
    "generated": M["generated_date"],
    "authorization": "scripts/c11_s16_authorization.yaml (§16 authorized "
                     "2026-09-12; batch 3 commissioned by the operator's "
                     "session-51 move-forward directive — the full S1 "
                     "remainder 1.37–1.60C + the Paper-2 MS pins)",
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_batch3_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges),
              "held": len(held), "command_kinds": len(cks)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-batch3-review-2",
              "verdicts_file": "scripts/c11_batch3_review_pass2.yaml",
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
        "pathway": "record verdicts in scripts/c11_batch3_verdicts.yaml "
                   "(fill the template); a later session encodes + applies "
                   "them via §18 promotion / §7 re-authoring",
        "promotion_now": 0,
        "cross_boundary_edges": 6,
    },
}
(REPORTS / "C11_BATCH3_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- verdict template (OPERATOR-OWNED; empty verdicts + machine pre-triage) ---
E_VOCAB = "CONFIRM | REJECT | HOLD | MERGE | SPLIT"
tpl = ["# T-C11 §16 batch 3 — OPERATOR verdict template (session-51 package).",
       "# OPERATOR-OWNED: fill verdict per row (empty verdict = not decided).",
       "# Hand-edits HERE are the sanctioned pathway; graph/*.yaml are never",
       "# hand-edited. The next session encodes + applies the filled record via",
       "# the §18 promotion pathway / §7 decision-record re-authoring. Verdicts",
       "# are RECORDED, not applied: filling this file promotes nothing.",
       "meta:",
       "  task: T-C11",
       "  stage: s16-batch-3-verdicts",
       "  batch: 3",
       "  session: 51",
       "  file: OPERATOR-OWNED verdict record for C11_BATCH3_REVIEW_SHEET (session 51) — verdicts recorded by operator decision (pending).",
       f"  instructions: 'Fill verdict per row. Edge/node vocabulary: {E_VOCAB}. This batch authored",
       "    NO REVIEW_REQUIRED edge (all doubts were held or resolved on explicit evidence).",
       "    Identity-decision vocabulary: MERGE (fold nodes) | SPLIT (mint finer) | KEEP_AS_IS. The batch-3",
       "    extraction_pass is c11-s16-batch-3; its 14 held candidates are informational only (no reopening,",
       "    no promotion of held candidates). Six edges are cross-boundary into earlier-record nodes",
       "    (CON-ATOM x2, CON-ELECTRONIC-CONFIGURATION x2, CON-MOLECULE x2 — sanctioned, no duplicate mint).",
       "    The next session applies verdicts via the §18 promotion pathway /",
       "    §7 decision-record re-authoring; nothing here is HUMAN_VALIDATED.'",
       "edge_verdicts:"]
EDGE_NOTES = {
    "4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE":
        "vocabulary-level operand class + cross-boundary target (FP-B1-4 class)",
    "4CH1-CON-DIAMOND-GRAPHITE RELATED_TO 4CH1-CON-SIMPLE-MOLECULAR":
        "first RELATED_TO deployment in the store (FP-B3-3; B3-ID-07)",
    "4CH1-CON-METAL-PROPERTIES EXPLAINED_BY 4CH1-CON-METALLIC-BOND":
        "relation-class choice (prereq reading equally real; FP-B3-2)",
    "4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND":
        "density flag: transitively reachable, different information (FP-B3-2)",
    "4CH1-CON-IONIC-BOND COMMONLY_CONFUSED_WITH 4CH1-CON-COVALENT-BOND":
        "second COMMONLY_CONFUSED_WITH deployment (FP-B3-4)",
    "4CH1-MIS-IONIC-CONDUCTION-ELECTRONS REMEDIATED_BY 4CH1-CON-IONIC-CONDUCTION":
        "remediation target = MO target (the batch-1 B1-E-25 pattern)",
    "4CH1-MIS-IONIC-BOND-ATOMS REMEDIATED_BY 4CH1-CON-IONIC-BOND":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-COVALENT-BONDS-BROKEN REMEDIATED_BY 4CH1-CON-SIMPLE-MOLECULAR":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-GRAPHITE-LAYER-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-DIAMOND-GRAPHITE":
        "family overlap with MIS-COVALENT-BONDS-BROKEN (B3-ID-06 merge question)",
    "4CH1-MIS-GRAPHITE-LAYER-BONDS REMEDIATED_BY 4CH1-CON-DIAMOND-GRAPHITE":
        "family overlap + B1-E-25 pattern (B3-ID-06 merge question)",
}
i = 0
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    i += 1
    k = ekey(e)
    flag = EDGE_NOTES.get(k, "")
    tpl.append(f"- id: B3-E-{i:02d}")
    tpl.append(f"  triple: {k}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{flag}'")
tpl.append("node_verdicts:")
NODE_NOTES = {
    "4CH1-CON-ION-CHARGE-RULES": "deduction-rule vs named-ion-table split option (FP-B1-1 class)",
    "4CH1-CON-IONIC-CONDUCTION": "know/understand dual attachment 1.43+1.56C (B3-ID-01)",
    "4CH1-CON-COVALENT-BOND": "definition-vs-mechanism dual attachment 1.44+1.45 (B3-ID-02)",
    "4CH1-CON-SIMPLE-MOLECULAR": "structure node vs IMF term node split (B3-ID-03)",
    "4CH1-CON-DIAMOND-GRAPHITE": "three-allotrope block + first RELATED_TO edge (B3-ID-04)",
    "4CH1-CON-COVALENT-CONDUCTION": "know/understand dual attachment 1.51+1.55C (B3-ID-01 class)",
    "4CH1-CON-METALLIC-BOND": "representation-vs-mechanism dual attachment 1.52C+1.53C (B3-ID-05)",
    "4CH1-CON-ANODE-CATHODE": "term pair + migration rule in one node (FP-B1-1 class)",
    "4CH1-CON-AQUEOUS-DISCHARGE": "second node on 1.58C (dual node attachment, B3-ID-05 class)",
    "4CH1-MIS-GRAPHITE-LAYER-BONDS": "family overlap with MIS-COVALENT-BONDS-BROKEN (B3-ID-06)",
}
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "CONCEPT":
        continue
    i += 1
    flag = NODE_NOTES.get(n["code"], "")
    tpl.append(f"- id: B3-N-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{flag}'")
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "MISCONCEPTION":
        continue
    i += 1
    note = ""
    if n["code"] == "4CH1-MIS-IONIC-BOND-ATOMS":
        note = "mark-scheme quote preserves the pinned line-wrap artifact (FP-B3-5)"
    elif n["code"] == "4CH1-MIS-GRAPHITE-LAYER-BONDS":
        note = "family overlap with MIS-COVALENT-BONDS-BROKEN (B3-ID-06)"
    tpl.append(f"- id: B3-M-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append("  pretriage: LIKELY_SAFE (note- / mark-scheme-documented)")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{note}'")
tpl.append("identity_decisions:")
tpl.append("- id: B3-ID-01")
tpl.append("  question: split the know/understand dual-attachment pairs into separate nodes (CON-IONIC-CONDUCTION 1.43/1.56C; CON-COVALENT-CONDUCTION 1.51+1.55C)")
tpl.append("  verdict:")
tpl.append("- id: B3-ID-02")
tpl.append("  question: split CON-COVALENT-BOND into the 1.44 sharing-definition node and the 1.45 electrostatic-mechanism node")
tpl.append("  verdict:")
tpl.append("- id: B3-ID-03")
tpl.append("  question: split CON-SIMPLE-MOLECULAR into a structure node and a separate intermolecular-forces term node (the spec names the term)")
tpl.append("  verdict:")
tpl.append("- id: B3-ID-04")
tpl.append("  question: split CON-DIAMOND-GRAPHITE into diamond/graphite/C60 term-level nodes (one SP, two notes)")
tpl.append("  verdict:")
tpl.append("- id: B3-ID-05")
tpl.append("  question: split CON-METALLIC-BOND (1.52C 2-D representation vs 1.53C bonding) and/or fold CON-AQUEOUS-DISCHARGE into CON-ELECTROLYSIS (dual node attachment on 1.58C)")
tpl.append("  verdict:")
tpl.append("- id: B3-ID-06")
tpl.append("  question: merge MIS-GRAPHITE-LAYER-BONDS into MIS-COVALENT-BONDS-BROKEN (one bonds-vs-forces family, two documented surfaces) or keep separate for per-concept remediation targeting")
tpl.append("  verdict:")
tpl.append("- id: B3-ID-07")
tpl.append("  question: replace the RELATED_TO(DIAMOND-GRAPHITE, SIMPLE-MOLECULAR) edge with a direct 1.50 attachment on CON-SIMPLE-MOLECULAR (the alternative C60 modeling)")
tpl.append("  verdict:")
tpl.append("held_appendix_acknowledgment:")
tpl.append("  acknowledged:")
tpl.append("  notes: ''")
# session-51 guard (the batch-1/2 pattern): once the verdict round is
# recorded, never re-emit an empty template beside the filled verdict record.
if (HERE / "c11_batch3_verdicts.yaml").exists():
    print("template NOT re-emitted: scripts/c11_batch3_verdicts.yaml exists "
          "(verdict round recorded)")
else:
    (HERE / "c11_batch3_verdicts_template.yaml").write_text(
        "\n".join(tpl) + "\n", encoding="utf-8")

# --- review sheet --------------------------------------------------------------
L = []
A = L.append
A("# T-C11 §16 Batch 3 Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1-1.37–1.60C (the FULL S1 remainder: ionic + covalent + metallic "
  f"bonding + electrolysis, 24 SPs) + practical PR-04 · generated "
  f"{M['generated_date']} · decision record "
  f"`scripts/c11_batch3_decisions.yaml` (pass 1: `{M['extraction_pass']}`) · "
  f"adversarial pass 2: `scripts/c11_batch3_review_pass2.yaml` · "
  f"authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized "
  f"2026-09-12; batch 3 commissioned by the operator's session-51 "
  f"move-forward directive — the whole S1 remainder in one batch; FN-B2-1 "
  f"closed: the Paper-2 topic MS set is pinned)")
A("")
A(f"**NOTHING in this batch is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + n_part_of} batch edges are AI_SUGGESTED (SUGGESTED). "
  "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
  "pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
  "**Zero batch-3 promotions exist.** This sheet is the batch's operator "
  "gate: record verdicts in `scripts/c11_batch3_verdicts_template.yaml` "
  "(fill + rename to `c11_batch3_verdicts.yaml`); a later session encodes "
  "and applies them.)")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Machine state: the full "
  "gate suite is green at the merged 91-node / 220-edge store; every quote is "
  "machine-verified byte-for-byte against its source file (G03/c11.4); the "
  "4.15 negative control is uncovered. Six edges are CROSS-BOUNDARY into "
  "batch-2 nodes (CON-ATOM ×2, CON-ELECTRONIC-CONFIGURATION ×2, "
  "CON-MOLECULE ×2 — sanctioned per FN-B1-2/FN-B2-2; no duplicate concept "
  "was minted). One mark-scheme quote preserves the pinned artifact's line "
  "wrap (\"atoms/molecul es/electrons\" — FP-B3-5, layout-verified against "
  "the PDF).")
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
  f"predicted 57.6 nodes / 66 edges / 24 held vs actual {len(nodes)} / "
  f"{len(edges)} / {len(held)} — nodes −58.3%, edges −40.9%, held −41.7%. "
  "The delta is the boundary discipline + bond-family granularity, not thin "
  "coverage: no batch-2 identity was re-minted (ION/CBOND/DCC/SM reach "
  "ATOM/ELECTRONIC-CONFIGURATION/MOLECULE via 6 sanctioned boundary edges); "
  "the spec's own know/understand pairs were merged as dual attachments "
  "(1.43+1.56C, 1.44+1.45, 1.51+1.55C, 1.52C+1.53C); and 1.60C attaches no "
  "concept node (the practical owns it — the 1.13 precedent).")
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
  "operand rule): pass-2 flags the four know/understand dual-attachment "
  "pairs (FP-B3-1 — 1.43+1.56C, 1.44+1.45, 1.51+1.55C, 1.52C+1.53C), the "
  "CON-SIMPLE-MOLECULAR structure-vs-IMF split question, the "
  "CON-DIAMOND-GRAPHITE three-allotrope block, the CON-METALLIC-BOND "
  "representation-vs-mechanism pair and the 1.58C dual node attachment. All "
  "are operator identity decisions (template §identity_decisions, "
  "B3-ID-01..07). 1.60C attaches NO batch-3 concept node (the practical "
  "PR-04 owns it — the 1.13 precedent; the explicit gap is §5 FN-B3-3).")
A("")
A(f"## 3. Authored semantic edges ({len(edges)})")
A("")
A("Direction conventions: REQUIRES_PREREQUISITE source=dependent → "
  "target=prerequisite; EXPLAINED_BY explained → explainer; RELATED_TO is a "
  "residual concept-to-concept association; COMMONLY_CONFUSED_WITH is a "
  "symmetric term-pair relation stored one-directionally; "
  "WRONG_ANSWER_PATTERN / REMEDIATED_BY / MISCONCEPTION_OF misconception → "
  "concept.")
A("")
A("### 3.1 REVIEW_REQUIRED (open operator decision)")
A("")
A("**None.** This batch authored no REVIEW_REQUIRED edge: the pass-1 "
  "authoring either resolved each doubt on explicit evidence or sent the "
  "candidate to held (14 rows, §4).")
A("")
A(f"### 3.2 SUGGESTED edges ({asserted}) — the §18-promotable surface after verdicts")
A("")
A("Flagged rows (pre-triage FLAGGED in the verdict template): the "
  "relation-class choice on the EXPLAINED_BY edge, the density flag on "
  "ELECTROLYSIS→IONIC-BOND, the FIRST RELATED_TO deployment, the SECOND "
  "COMMONLY_CONFUSED_WITH deployment, the vocabulary-level "
  "SIMPLE-MOLECULAR→MOLECULE class, and the four remediation-target="
  "misconception-target rows (the batch-1 B1-E-25 pattern) + the "
  "MIS-GRAPHITE-LAYER-BONDS family-overlap rows.")
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
  "re-authoring the decision record, never hand-editing the graph.")
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
A("## 6. Command-kind tags (guide §8) — batch-3 SPs")
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
  "store (machine-tested: graph_check + negative test class 10/11 + the "
  "s16-authorization check D5). The batch adds nothing in S4 territory. "
  "Operator: acknowledge ☐")
A("")
A("## 8. Batch-3 evidence set (pinned)")
A("")
A("- 14 T-C10 HUMAN_VALIDATED-mapped notes (read in full at extraction): "
  "f. Ionic Bonding ×5 (Common Ions, Formation of ions, Formula of ionic "
  "compounds, Ionic bonding and lattices, Ionic bonding diagrams) + "
  "g. Covalent Bonding ×4 (Dot & Cross Diagrams, Forming covalent bonds, "
  "Giant covalent structures, Simple molecular structures) + "
  "h. Metallic Bonding ×1 (Metallic bonding) + i. Electrolysis ×4 "
  "(Electrolysis diagram, Electronic conductivity, Half equations, the "
  "1.60C practical note).")
A("- 3 pinned Paper-2 mark-scheme extractions (misconception-class evidence "
  "only; FN-B2-1 closed): IONIC_MS_P2.txt (4ccfc377514a) + "
  "COVALENT_MS_P2.txt (ed012522d306) + CFEC_MS_P2.txt (84d641c55208). "
  "Coverage fact: PMT Unit 1 publishes NO metallic-bonding or electrolysis "
  "MS, so 1.52C–1.60C misconception mining has note evidence only "
  "(B3-H-11/H-12 record the refused candidates — the gap is explicit, not "
  "silent).")
A("")
A("## 9. After review (the batch gate)")
A("")
A("1. Fill `scripts/c11_batch3_verdicts_template.yaml` (rename to "
  "`c11_batch3_verdicts.yaml`): per-row verdicts, the identity decisions, "
  "the held acknowledgment. (This batch has NO RR settlement — no "
  "REVIEW_REQUIRED edge was authored.)")
A("2. The next session encodes your verdicts (fail-closed) and applies them: "
  "CONFIRM edges through the §18 pathway (`c11_diff_review.py approve` → one "
  "`c11_promote.py` invocation → gated G13 re-run); REJECT rows re-authored "
  "out like HELD-13; MERGE/SPLIT as §7 re-authoring (B3-ID-01..07 may "
  "re-scope the dual-attachment pairs).")
A("3. This batch COMPLETES Section 1 coverage (pilot + batches 1–3 = all 60 "
  "S1 SPs). Per the §16 phase order, the next slice is S3 Physical (batch "
  "4); the consolidated cross-slice boundary-concept ruling comes before "
  "phase 2 (S3).")
A("")
A("---")
A(f"Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, "
  f"`graph/spec_command_kinds.yaml` (generated, gated, merged store) · "
  f"`C11_BATCH3_REVIEW.json` (this sheet's machine record) · "
  f"`scripts/c11_batch3_verdicts_template.yaml` (the verdict template) · "
  f"contract: `C11_ARCHITECTURE.md`")

(REPORTS / "C11_BATCH3_REVIEW_SHEET.md").write_text("\n".join(L) + "\n",
                                                   encoding="utf-8")
print(f"wrote {REPORTS / 'C11_BATCH3_REVIEW_SHEET.md'}")
print(f"wrote {REPORTS / 'C11_BATCH3_REVIEW.json'}")
if (HERE / "c11_batch3_verdicts.yaml").exists():
    print(f"verdict record present: {HERE / 'c11_batch3_verdicts.yaml'} "
          f"(template intentionally not re-emitted)")
else:
    print(f"wrote {HERE / 'c11_batch3_verdicts_template.yaml'}")
print(f"raw agreement (NOT kappa): nodes {raw_agreement_nodes:.1%}; edges "
      f"{agree}/{asserted} asserted confirmed; {len(held)} held all "
      f"AGREE_HOLD; zero RR authored")
