#!/usr/bin/env python3
"""
T-C11 §16 batch 8 — c11_batch8_review_build.py: renders the batch-8 operator
review gate (the per-batch operator gate required by the §16 authorization)
from the batch-8 decision record + the pass-2 adversarial verdicts, so the
documents cannot drift from the data (the c11_batch7_review_build.py
pattern, batch-8-scoped, session-54 hardening included).

Outputs:
  graph/reports/C11_BATCH8_REVIEW_SHEET.md — the operator review gate
  graph/reports/C11_BATCH8_REVIEW.json     — machine record + agreement stats
  scripts/c11_batch8_verdicts_template.yaml — the OPERATOR-OWNED verdict
      template (empty verdicts; machine pre-triage per row)

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator).

The batch ends HERE: this build promotes nothing, validates nothing as
HUMAN_VALIDATED, and authorizes nothing. The per-batch operator gate is the
operator's action; batch-8 promotion happens only via §18 after verdicts.

Usage: python3 scripts/c11_batch8_review_build.py
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

dec = yaml.safe_load((HERE / "c11_batch8_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_batch8_review_pass2.yaml").read_text(encoding="utf-8"))

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
    "task": "T-C11", "stage": "s16-batch-8-review",
    "batch": 8,
    "generated": M["generated_date"],
    "authorization": "scripts/c11_s16_authorization.yaml (§16 authorized "
                     "2026-09-12; batch 8 commissioned by the operator's "
                     "'Proceed with batch 8' directive, session 61 — Section 2 "
                     "Inorganic Chemistry FOURTH slice (S2-h Chemical Tests); "
                     "under the session-61 cross-slice boundary ruling "
                     "scripts/c11_batch8_boundary_ruling.yaml)",
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_batch8_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges),
              "held": len(held), "command_kinds": len(cks)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-batch8-review-2",
              "verdicts_file": "scripts/c11_batch8_review_pass2.yaml",
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
        "note": "zero pass-2 findings required re-authoring (FP-B8-1..4 and "
                "FN-B8-1..2 are recorded questions/resolutions — the "
                "flame-test family-unity ruling rides B8-ID-01): the record "
                "carries 8 nodes / 10 authored edges at this gate with zero "
                "demotions and zero RR quarantines: the pass-1 authoring "
                "sent 9 candidates to held BEFORE emission and resolved "
                "every remaining doubt on explicit evidence",
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
        "pathway": "record verdicts in scripts/c11_batch8_verdicts.yaml "
                   "(fill the template); a later session encodes + applies "
                   "them via §18 promotion / §7 re-authoring",
        "promotion_now": 0,
        "cross_boundary_edges": 3,
    },
}
(REPORTS / "C11_BATCH8_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- verdict template (OPERATOR-OWNED; empty verdicts + machine pre-triage) ---
E_VOCAB = "CONFIRM | REJECT | HOLD | MERGE | SPLIT"
tpl = ["# T-C11 §16 batch 8 — OPERATOR verdict template (session-61 package).",
       "# OPERATOR-OWNED: fill verdict per row (empty verdict = not decided).",
       "# Hand-edits HERE are the sanctioned pathway; graph/*.yaml are never",
       "# hand-edited. The next session encodes + applies the filled record via",
       "# the §18 promotion pathway / §7 decision-record re-authoring. Verdicts",
       "# are RECORDED, not applied: filling this file promotes nothing.",
       "meta:",
       "  task: T-C11",
       "  stage: s16-batch-8-verdicts",
       "  batch: 8",
       "  session: 61",
       "  file: OPERATOR-OWNED verdict record for C11_BATCH8_REVIEW_SHEET (session 61) — verdicts recorded by operator decision (pending).",
       f"  instructions: 'Fill verdict per row. Edge/node vocabulary: {E_VOCAB}. This batch authored",
       "    NO REVIEW_REQUIRED edge (all doubts were held or resolved on explicit evidence).",
       "    Identity-decision vocabulary: MERGE (fold nodes) | SPLIT (mint finer) | KEEP_AS_IS. The batch-8",
       "    extraction_pass is c11-s16-batch-8 (Section 2 Inorganic Chemistry FOURTH slice, 7 SPs",
       "    4CH1-2.44-2.50: S2-h Chemical Tests; no practicals own any batch-8 SP). Its 9 held",
       "    candidates are informational only (no reopening, no promotion of held candidates — B8-H-07",
       "    holds the documented-but-apparatus-choice flame-test carrier-rod class for operator ruling).",
       "    THREE edges are cross-section boundary edges into the ruled targets",
       "    (CON-ION-CHARGE-RULES — the batch-3 owner, x2; CON-PURE-SUBSTANCE — the batch-1 owner;",
       "    sanctioned by the session-61 cross-slice ruling, no duplicate mint). The next session",
       "    applies verdicts via the §18 promotion pathway / §7 decision-record re-authoring;",
       "    nothing here is HUMAN_VALIDATED.'",
       "edge_verdicts:"]
EDGE_NOTES = {
    "4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES":
        "cross-boundary target (session-61 ruling target 1; the batch-3 "
        "named-ion owner — the 2.48 bullets name the anions with charges, "
        "applied as given)",
    "4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES":
        "cross-boundary target (session-61 ruling target 2 — the second edge "
        "into the batch-3 owner, the batch-5 x2 precedent)",
    "4CH1-CON-WATER-PURITY-TEST REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE":
        "cross-boundary target (session-61 ruling target 3; the batch-1 "
        "pure-substance owner — the impurity effect IS the owner's surface)",
    "4CH1-MIS-GLOWING-SPLINT-HYDROGEN WRONG_ANSWER_PATTERN 4CH1-CON-GAS-TESTS":
        "documented Reject class (the pinned Chemical Tests MS Q4a: glowing "
        "splint / unflamed splint / pop-only)",
    "4CH1-MIS-GLOWING-SPLINT-HYDROGEN REMEDIATED_BY 4CH1-CON-GAS-TESTS":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-HALIDE-TEST-HCL WRONG_ANSWER_PATTERN 4CH1-CON-ANION-TESTS":
        "documented Reject class (the pinned Chemical Tests MS Q4b(i): "
        "hydrochloric acid / HCl rejected as the acidifier)",
    "4CH1-MIS-HALIDE-TEST-HCL REMEDIATED_BY 4CH1-CON-ANION-TESTS":
        "remediation target = WAP target (the B1-E-25 pattern)",
}
i = 0
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    i += 1
    k = ekey(e)
    flag = EDGE_NOTES.get(k, "")
    tpl.append(f"- id: B8-E-{i:02d}")
    tpl.append(f"  triple: {k}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    # session-54 fix: YAML single-quote escaping for embedded apostrophes
    tpl.append(f"  notes: '{flag.replace("'", "''")}'")
tpl.append("node_verdicts:")
NODE_NOTES = {
    "4CH1-CON-FLAME-TEST": "one-node-two-SPs family ruling (B8-ID-01; the "
                           "2.45 procedure + 2.46 colours taught as one "
                           "identification method)",
}
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "CONCEPT":
        continue
    i += 1
    flag = NODE_NOTES.get(n["code"], "")
    tpl.append(f"- id: B8-N-{i:02d}")
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
    if n["code"] == "4CH1-MIS-GLOWING-SPLINT-HYDROGEN":
        note = ("the strongest documented class of the batch (expected answer "
                "+ method + explicit glowing-splint Reject + the unflamed-"
                "splint and pop-only insufficiency notes); the curly-quote "
                "anchor is byte-honest (FP-B8-2)")
    if n["code"] == "4CH1-MIS-HALIDE-TEST-HCL":
        note = "clean Reject-column class with the expected acidifier named and the product identity"
    tpl.append(f"- id: B8-M-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append("  pretriage: LIKELY_SAFE (mark-scheme-documented)")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{note.replace("'", "''")}'")
tpl.append("identity_decisions:")
tpl.append("- id: B8-ID-01")
tpl.append("  question: keep the 2.45/2.46 flame-test family as ONE node (the note teaches the colours INSIDE the technique as one identification method) vs splitting the procedure node from the colours node")
tpl.append("  verdict:")
tpl.append("- id: B8-ID-02")
tpl.append("  question: keep the flame-test / NaOH-cation-test association as a RELATED_TO residual (the two parallel identification techniques; medium confidence) vs dropping the edge entirely (no corpus-documented confusability)")
tpl.append("  verdict:")
tpl.append("- id: B8-ID-03")
tpl.append("  question: mint the MIS-GLOWING-SPLINT-HYDROGEN misconception from the pinned Chemical Tests MS Q4a Reject class (narrow-but-exact; the MIS-CUO-COLOUR/B7-ID-05 precedent) — or rule it exam-trivia")
tpl.append("  verdict:")
tpl.append("- id: B8-ID-04")
tpl.append("  question: mint the MIS-HALIDE-TEST-HCL misconception from the pinned Chemical Tests MS Q4b(i) Reject class (clean single-acid reject with the expected acidifier named) — or rule it exam-trivia")
tpl.append("  verdict:")
tpl.append("held_appendix_acknowledgment:")
tpl.append("  acknowledged:")
tpl.append("  notes: ''")
# re-issue guard (the batch-1..7 pattern): once the verdict round is
# recorded, never re-emit an empty template beside the filled verdict record.
if (HERE / "c11_batch8_verdicts.yaml").exists():
    print("template NOT re-emitted: scripts/c11_batch8_verdicts.yaml exists "
          "(verdict round recorded)")
else:
    (HERE / "c11_batch8_verdicts_template.yaml").write_text(
        "\n".join(tpl) + "\n", encoding="utf-8")
    # fail-closed post-write parseability check (the session-54 hardening)
    _tpl_doc = yaml.safe_load(
        (HERE / "c11_batch8_verdicts_template.yaml")
        .read_text(encoding="utf-8"))
    _require(_tpl_doc is not None and "edge_verdicts" in _tpl_doc,
             "post-write: written template is unparseable or missing edge_verdicts")
    _require(len(_tpl_doc["edge_verdicts"]) == len(edges),
             "post-write: written template edge_verdicts count drifted")
    _require(len(_tpl_doc["node_verdicts"]) == len(nodes),
             "post-write: written template node_verdicts count drifted")
    _require(len(_tpl_doc["identity_decisions"]) == 4,
             "post-write: written template identity_decisions count drifted")

# --- review sheet --------------------------------------------------------------
L = []
A = L.append
A("# T-C11 §16 Batch 8 Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1–2.44–2.50 (Section 2 — Inorganic Chemistry, FOURTH slice: "
  f"h Chemical Tests, 7 SPs; no practicals own any batch-8 SP) · "
  f"generated {M['generated_date']} · "
  f"decision record `scripts/c11_batch8_decisions.yaml` (pass 1: "
  f"`{M['extraction_pass']}`) · adversarial pass 2: "
  f"`scripts/c11_batch8_review_pass2.yaml` · authorization: "
  f"`scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 8 "
  f"commissioned by the operator's 'Proceed with batch 8' directive) · "
  f"boundary ruling: `scripts/c11_batch8_boundary_ruling.yaml` (session 61, "
  f"machine-checked — the 3 sanctioned boundary edges below)")
A("")
A(f"**NOTHING in this batch is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + n_part_of} batch edges are AI_SUGGESTED (SUGGESTED). "
  "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
  "pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
  "regeneration). **Zero batch-8 promotions exist.** This sheet is the "
  "batch's operator gate: record verdicts in "
  "`scripts/c11_batch8_verdicts_template.yaml` (fill + rename to "
  "`c11_batch8_verdicts.yaml`); a later session encodes and applies them.")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Machine state: the full "
  "gate suite is green at the merged 165-node / 384-edge store; every quote "
  "is machine-verified byte-for-byte against its source file (G03/c11.4; "
  "92 quote probes + 87 record anchors pre-verified BEFORE the registry "
  "grew, then re-verified by the generator); the 4.15 negative control is "
  "uncovered. THREE edges are cross-section boundary edges into the ruled "
  "targets (CON-ION-CHARGE-RULES — the batch-3 owner, x2; CON-PURE-SUBSTANCE "
  "— the batch-1 owner; sanctioned per the session-61 cross-slice ruling; no "
  "duplicate concept was minted). The single S2-h family is MS-pinned (the "
  "Chemical Tests MS Q4a and Q4b(i) Reject columns anchor the TWO "
  "misconception mints; pdftotext line-wrap and curly-quote attributions are "
  "recorded in the nodes' derivation_notes). NO pass-2 finding required "
  "re-authoring (FP-B8-1..4 / FN-B8-1..2 are recorded questions and "
  "resolutions).")
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
  "resolved on explicit evidence). **Zero pass-2 findings required "
  "re-authoring; zero demotions.**")
A("")
A(f"Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): "
  f"the batch-8 record is appended by the forecast instrument at this gate "
  f"(see the regenerated C11_BATCH_FORECAST.json). The S2-h family runs in "
  f"the descriptive band the item-14 plan anticipated (nodes/SP "
  f"{len(nodes)/7:.2f}, edges/SP {len(edges)/7:.2f}), with the held "
  "adjacencies (B8-H-01..09 — the naming/mechanism-applied surfaces the "
  "ruling dispositioned) accounting for the gap, not thin coverage: no "
  "S1/S3/batch-5/6/7 identity was re-minted (the 3 existing-owner targets "
  "reached via the 3 sanctioned boundary edges); no batch-8 SP is "
  "practical-typed (the PR lane is empty).")
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
  "operand rule): pass-2 flags the 2.45/2.46 one-family ruling (B8-ID-01), "
  "the flame-vs-NaOH residual-association question (B8-ID-02), and the TWO "
  "single-Reject-column misconception mints (B8-ID-03, B8-ID-04). All are "
  "operator identity decisions (template §identity_decisions). No batch-8 SP "
  "attaches a practical node (none is practical-typed).")
A("")
print("sheet part 1 rendered;", len(L), "lines")

# --- edges + held sections (batch-4/5/6/7 pattern) -----------------------------------
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
A("THREE edges are CROSS-SECTION boundary edges into the ruled targets "
  "(sanctioned per the session-61 cross-slice ruling — no duplicate mint): "
  "the 2.48 anion-identity row and the 2.47 cation-identity row (both into "
  "the batch-3 CON-ION-CHARGE-RULES owner — the batch-5 x2 precedent) and "
  "the 2.50 purity row (into the batch-1 CON-PURE-SUBSTANCE owner). The TWO "
  "gas-test dependencies are IN-SLICE (the NH4+ and carbonate routes "
  "identify their evolved gases via the 2.44 family).")
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
A("Every held candidate cites its §19 failure class; the documented "
  "carrier-rod Reject class is held for operator ruling rather than minted "
  "(B8-H-07 — an apparatus-choice face, not a distinct conceptual error "
  "class). A held record is a valid outcome — the abstention is the system's "
  "honest output.")
A("")
A("## 5. Operator verdict surface")
A("")
A(f"- **{p1_accept} SUGGESTED edges** (B8-E-01..{p1_accept:02d}) — the §18 "
  "promotion surface")
A(f"- **{len(nodes)} nodes** ({sum(1 for n in nodes if n['family']=='CONCEPT')} "
  f"CONCEPT B8-N-01..06 + {sum(1 for n in nodes if n['family']=='MISCONCEPTION')} "
  "MISCONCEPTION B8-M-01..02) — node authority stays SUGGESTED; nodes have "
  "no §18 pathway (node promotion is a separate identity decision, deferred)")
A("- **4 identity decisions** (B8-ID-01..04) — MERGE/SPLIT/KEEP_AS_IS")
A(f"- **{len(held)} held candidates** — acknowledge the quarantine (no "
  "reopening)")
A("- **0 REVIEW_REQUIRED edges** — zero RR settlements needed")
A("")
A("Pathway: fill `scripts/c11_batch8_verdicts_template.yaml` → rename to "
  "`c11_batch8_verdicts.yaml` → a later session encodes + applies via "
  "`c11_verdict_encode_batch8`-style reconciliation + `c11_promote.py` (§18) "
  "+ the gated generator re-run. NOTHING is promoted at this gate.")
A("")

(REPORTS / "C11_BATCH8_REVIEW_SHEET.md").write_text(
    "\n".join(L) + "\n", encoding="utf-8")
print(f"review gate rendered: {REPORTS / 'C11_BATCH8_REVIEW_SHEET.md'} + "
      f"C11_BATCH8_REVIEW.json + the verdict template")
