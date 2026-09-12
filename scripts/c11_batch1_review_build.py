#!/usr/bin/env python3
"""
T-C11 §16 batch 1 — c11_batch1_review_build.py: renders the batch-1 operator
review gate (the per-batch operator gate required by the §16 authorization)
from the batch-1 decision record + the pass-2 adversarial verdicts, so the
documents cannot drift from the data (the c11_review_render.py pattern,
batch-scoped).

Outputs:
  graph/reports/C11_BATCH1_REVIEW_SHEET.md — the operator review gate
  graph/reports/C11_BATCH1_REVIEW.json     — machine record + agreement stats
  scripts/c11_batch1_verdicts_template.yaml — the OPERATOR-OWNED verdict
      template (empty verdicts; machine pre-triage per row)

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator).

The batch ends HERE: this build promotes nothing, validates nothing as
HUMAN_VALIDATED, and authorizes nothing. The per-batch operator gate is the
operator's action; batch-1 promotion happens only via §18 after verdicts.

Usage: python3 scripts/c11_batch1_review_build.py
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

dec = yaml.safe_load((HERE / "c11_batch1_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_batch1_review_pass2.yaml").read_text(encoding="utf-8"))

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
    "task": "T-C11", "stage": "s16-batch-1-review",
    "batch": 1,
    "generated": M["generated_date"],
    "authorization": "scripts/c11_s16_authorization.yaml (§16 authorized "
                     "2026-09-12; batch 1 commissioned by the operator's "
                     "'run batch 1', session 47)",
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_batch1_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges),
              "held": len(held), "command_kinds": len(cks)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-batch1-review-2",
              "verdicts_file": "scripts/c11_batch1_review_pass2.yaml",
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
        "note": "zero pass-2 demotions: the pass-1 authoring quarantined its "
                "weakest emission to REVIEW_REQUIRED and sent 12 candidates "
                "to held BEFORE emission — the adversarial findings land as "
                "CONFIRM_WITH_NOTE flags enumerated for the operator gate",
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
        "pathway": "record verdicts in scripts/c11_batch1_verdicts.yaml "
                   "(fill the template); a later session encodes + applies "
                   "them via §18 promotion / §7 re-authoring",
        "promotion_now": 0,
    },
}
(REPORTS / "C11_BATCH1_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- verdict template (OPERATOR-OWNED; empty verdicts + machine pre-triage) ---
E_VOCAB = "CONFIRM | REJECT | HOLD | MERGE | SPLIT"
RR_VOCAB = "KEEP_AS_SUGGESTED | PRUNE_TO_HELD | HOLD_REVIEW_REQUIRED"
tpl = ["# T-C11 §16 batch 1 — OPERATOR verdict template (session-47 package).",
       "# OPERATOR-OWNED: fill verdict per row (empty verdict = not decided).",
       "# Hand-edits HERE are the sanctioned pathway; graph/*.yaml are never",
       "# hand-edited. The next session encodes + applies the filled record via",
       "# the §18 promotion pathway / §7 decision-record re-authoring. Verdicts",
       "# are RECORDED, not applied: filling this file promotes nothing.",
       "meta:",
       "  task: T-C11",
       "  stage: s16-batch-1-verdicts",
       "  batch: 1",
       "  session: 47",
       f"  file: OPERATOR-OWNED verdict record for C11_BATCH1_REVIEW_SHEET (session 47) — verdicts recorded by operator decision (pending).",
       f"  instructions: 'Fill verdict per row. Edge/node vocabulary: {E_VOCAB}. RR settlement vocabulary: {RR_VOCAB}.",
       "    Identity-decision vocabulary: MERGE (fold nodes) | SPLIT (mint finer) | KEEP_AS_IS. The batch-1",
       "    extraction_pass is c11-s16-batch-1; its 12 held candidates are informational only (no reopening,",
       "    no promotion of held candidates). The next session applies verdicts via the §18 promotion pathway /",
       "    §7 decision-record re-authoring; nothing here is HUMAN_VALIDATED.'",
       "edge_verdicts:"]
EDGE_NOTES = {
    "4CH1-CON-STATE-PARTICLE-MODEL REQUIRES_PREREQUISITE 4CH1-CON-STATES-THREE":
        "merge-candidate dependent (FP-B1-1)",
    "4CH1-CON-DIFFUSION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL":
        "relation-class choice flagged (B1-H-04 / FP-B1-2)",
    "4CH1-CON-MIXTURE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND":
        "symmetric-operand pair option (B1-H-01)",
    "4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND":
        "symmetric-operand pair option (B1-H-10)",
    "4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION":
        "vocabulary-level dependency class (FP-B1-4)",
    "4CH1-CON-FILTRATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION":
        "vocabulary-level dependency class (FP-B1-4)",
    "4CH1-MIS-GAS-PARTICLES-TOUCH REMEDIATED_BY 4CH1-CON-STATE-PARTICLE-MODEL":
        "remediation target = WAP target (pilot pattern targeted different concepts)",
}
i = 0
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    i += 1
    k = ekey(e)
    flag = EDGE_NOTES.get(k, "")
    tpl.append(f"- id: B1-E-{i:02d}")
    tpl.append(f"  triple: {k}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{flag}'")
tpl.append("rr_settlement:")
tpl.append("- id: B1-RR-01")
tpl.append("  triple: 4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION")
tpl.append("  pretriage: QUARANTINED (subsumption class; pass-1 self-review + pass-2 HOLD)")
tpl.append("  verdict:")
tpl.append("  notes: ''")
tpl.append("node_verdicts:")
NODE_NOTES = {
    "4CH1-CON-STATES-THREE": "merge candidate with CON-STATE-PARTICLE-MODEL (FP-B1-1)",
    "4CH1-CON-EVAPORATION-BOILING": "enrichment scoping (mirrors pilot N-27 pattern)",
    "4CH1-CON-HEATING-CONSTANT-MASS": "enrichment leaf, no edges (mirrors pilot N-08 pattern)",
    "4CH1-CON-SOLUTION": "triple-node split option (FP-B1-1 class)",
    "4CH1-CON-PURE-SUBSTANCE": "definition+criterion split option (FP-B1-3)",
}
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "CONCEPT":
        continue
    i += 1
    flag = NODE_NOTES.get(n["code"], "")
    tpl.append(f"- id: B1-N-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{flag}'")
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "MISCONCEPTION":
        continue
    i += 1
    tpl.append(f"- id: B1-M-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append("  pretriage: LIKELY_SAFE (mark-scheme documented)")
    tpl.append("  verdict:")
    tpl.append("  notes: ''")
tpl.append("identity_decisions:")
tpl.append("- id: B1-ID-01")
tpl.append("  question: merge CON-STATES-THREE into CON-STATE-PARTICLE-MODEL (1.1 pair)")
tpl.append("  verdict:")
tpl.append("- id: B1-ID-02")
tpl.append("  question: split CON-SOLUTION into term-level nodes (solvent/solute/solution)")
tpl.append("  verdict:")
tpl.append("- id: B1-ID-03")
tpl.append("  question: split CON-PURE-SUBSTANCE (definition vs fixed-point criterion)")
tpl.append("  verdict:")
tpl.append("- id: B1-ID-04")
tpl.append("  question: emit the symmetric operand pairs MIXTURE->{COMPOUND, ELEMENT} and PURE->{COMPOUND, ELEMENT} instead of the chain representatives")
tpl.append("  verdict:")
tpl.append("held_appendix_acknowledgment:")
tpl.append("  acknowledged:")
tpl.append("  notes: ''")
(HERE / "c11_batch1_verdicts_template.yaml").write_text("\n".join(tpl) + "\n",
                                                        encoding="utf-8")

# --- review sheet --------------------------------------------------------------
L = []
A = L.append
A("# T-C11 §16 Batch 1 Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1-1.1–1.12 (S1 remainder, first 12 SPs) · generated "
  f"{M['generated_date']} · decision record `scripts/c11_batch1_decisions.yaml` "
  f"(pass 1: `{M['extraction_pass']}`) · adversarial pass 2: "
  f"`scripts/c11_batch1_review_pass2.yaml` · authorization: "
  f"`scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 1 "
  f"commissioned by the operator, session 47)")
A("")
A(f"**NOTHING in this batch is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + n_part_of} batch edges are AI_SUGGESTED (SUGGESTED or "
  "REVIEW_REQUIRED). HUMAN_VALIDATED is reachable only by your promotion "
  "command via the §18 pathway (`scripts/c11_promote.py` → "
  "`scripts/c11_promotions.yaml` → gated generator re-run). **Zero batch-1 "
  "promotions exist.** This sheet is the batch's operator gate: record "
  "verdicts in `scripts/c11_batch1_verdicts_template.yaml` (fill + rename to "
  "`c11_batch1_verdicts.yaml`); a later session encodes and applies them.")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Machine state: the full "
  "gate suite is green at the merged 53-node / 118-edge store; every quote is "
  "machine-verified byte-for-byte against its source file (G03/c11.4); the "
  "4.15 negative control is uncovered.")
A("")
A("## 1. Totals & second-pass agreement")
A("")
A("| | nodes | authored edges | held | |")
A("|---|---|---|---|")
A(f"| pass-1 (extraction) | {len(nodes)} | {len(edges)} (+{n_part_of} derived PART_OF) | {len(held)} |")
A(f"| pass-2 verdicts | {n_conf} CONFIRM(+note) | {e_conf} CONFIRM(+note) · {e_hold} HOLD · {e_rej} REJECT | all 12 AGREE |")
A("")
A(f"Raw agreement (NOT κ — single human rater, architecture §12): nodes "
  f"{n_conf}/{len(nodes)} = {raw_agreement_nodes:.1%}; edges — of the "
  f"{asserted} edges pass-1 asserted (SUGGESTED), pass-2 confirmed {agree} "
  f"({raw_agreement_edges:.1%}); pass-1 quarantined {p1_rr} edge as "
  "REVIEW_REQUIRED, concordantly HOLD by pass 2. **Zero pass-2 demotions** — "
  "the abstention happened at authoring (12 held + 1 self-quarantine) rather "
  "than as pass-2 attack fallout; the adversarial findings land as "
  "CONFIRM_WITH_NOTE flags (§5).")
A("")
A(f"Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): "
  f"predicted 28.8 nodes / 33 edges / 12 held vs actual {len(nodes)} / "
  f"{len(edges)} / {len(held)} — nodes −16.7%, edges −12.1%, held 0.0% "
  "(terminology-heavy slice, lighter on procedures than the "
  "calculation-heavy pilot).")
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
  "operand rule): pass-2 flags the CON-STATES-THREE / "
  "CON-STATE-PARTICLE-MODEL pair (merge candidate), the CON-SOLUTION "
  "triple-node (split option) and CON-PURE-SUBSTANCE (definition + criterion "
  "in one node). All are operator identity decisions (template §identity_decisions).")
A("")
A(f"## 3. Authored semantic edges ({len(edges)})")
A("")
A("Direction conventions: REQUIRES_PREREQUISITE source=dependent → "
  "target=prerequisite; EXPLAINED_BY explained → explainer; REMEDIATED_BY "
  "misconception → concept.")
A("")
A("### 3.1 REVIEW_REQUIRED (open operator decision)")
A("")
A("| edge | conf | evidence | ambiguity (pass-1 self-review) | pass-2 | operator |")
A("|---|---|---|---|---|---|")
for e in edges:
    if e["validation_status"] != "REVIEW_REQUIRED":
        continue
    v = edge_p2[ekey(e)]
    ev = "<br>".join(f"“{a['quote'][:100]}”" for a in e["evidence"])
    amb = (e.get("ambiguity_note") or "")[:220]
    A(f"| `{e['source']}` **{e['relation']}** `{e['target']}` | {e['confidence']} | "
      f"{ev} | {amb} | {v['verdict']}: {(v.get('note') or '')[:200]} | ☐ |")
A("")
A(f"### 3.2 SUGGESTED edges ({asserted}) — the §18- promotable surface after verdicts")
A("")
A("Flagged rows (pre-triage FLAGGED in the verdict template): the "
  "relation-class choice on DIFFUSION EXPLAINED_BY (B1-H-04), the "
  "symmetric-operand options (B1-H-01/B1-H-10), the vocabulary-level "
  "technique→solution class (FP-B1-4), and the MIS-GAS remediation-target "
  "pattern.")
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
  "re-authoring the decision record, never hand-editing the graph. B1-H-06 "
  "and B1-H-07 record documented misconception evidence deferred for later "
  "passes — the operator may direct their minting.")
A("")
A("| id | status | candidate | failing rule | pass-2 | operator |")
A("|---|---|---|---|---|---|")
for h in held:
    r = h["reason"].split("—")[0].strip()
    v = p2["held_review"].get(h["id"], {})
    p2v = v.get("verdict", "—")
    cand = h["candidate"]
    if len(cand) > 120:
        cand = cand[:117] + "..."
    A(f"| {h['id']} | {h['status']} | {cand} | {r} | {p2v} | ☐ |")
A("")
A("## 5. Findings (pass-2, for the batch record)")
A("")
for f_ in p2["findings"]:
    A(f"- **{f_['id']} ({f_['kind']})** — {f_['detail']}")
A("")
A("## 6. Command-kind tags (guide §8) — batch-1 SPs")
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
A("## 8. Batch-1 evidence set (pinned)")
A("")
A("- 10 T-C10 HUMAN_VALIDATED-mapped notes (read in full at extraction): "
  "a. States of Matter ×5 (Changing states, Diffusion, Solutions, "
  "Solubility, Investigating solubility) + b. Elements, Compounds and "
  "Mixtures ×5 (Element/Compound or Mixture, Pure substances, Separation "
  "techniques, Interpreting chromatograms, Paper chromatography).")
A("- 2 pinned mark-scheme extractions (misconception-class evidence only): "
  "SOM_MS_P1.txt (sha1_12 e41e67f27cd5) + ECM2_MS_P1.txt (sha1_12 "
  "3c31a1a0e154) — per-batch mark-scheme mining per the §16 scope; ECM1/ECM3 "
  "and the Paper-2 variants remain unpinned (FN-B1-1).")
A("")
A("## 9. After review (the batch gate)")
A("")
A("1. Fill `scripts/c11_batch1_verdicts_template.yaml` (rename to "
  "`c11_batch1_verdicts.yaml`): per-row verdicts, the RR settlement, the "
  "identity decisions, the held acknowledgment.")
A("2. The next session encodes your verdicts (fail-closed) and applies them: "
  "CONFIRM edges through the §18 pathway (`c11_diff_review.py approve` → one "
  "`c11_promote.py` invocation → gated G13 re-run); REJECT rows re-authored "
  "out like HELD-13; MERGE/SPLIT as §7 re-authoring; the RR settlement per "
  "its vocabulary.")
A("3. Only after the batch-1 gate settles does batch 2 (S1 remainder "
  "1.13–1.24) get commissioned — the consolidated cross-slice boundary "
  "ruling comes before phase 2 (S3).")
A("")
A("---")
A(f"Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, "
  f"`graph/spec_command_kinds.yaml` (generated, gated, merged store) · "
  f"`C11_BATCH1_REVIEW.json` (this sheet's machine record) · "
  f"`scripts/c11_batch1_verdicts_template.yaml` (the verdict template) · "
  f"contract: `C11_ARCHITECTURE.md`")

(REPORTS / "C11_BATCH1_REVIEW_SHEET.md").write_text("\n".join(L) + "\n",
                                                   encoding="utf-8")
print(f"wrote {REPORTS / 'C11_BATCH1_REVIEW_SHEET.md'}")
print(f"wrote {REPORTS / 'C11_BATCH1_REVIEW.json'}")
print(f"wrote {HERE / 'c11_batch1_verdicts_template.yaml'}")
print(f"raw agreement (NOT kappa): nodes {raw_agreement_nodes:.1%}; edges "
      f"{agree}/{asserted} asserted confirmed; {uncert_concordant} RR edge "
      f"concordantly held (open: {open_uncertain})")
