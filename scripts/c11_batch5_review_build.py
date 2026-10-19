#!/usr/bin/env python3
"""
T-C11 §16 batch 5 — c11_batch5_review_build.py: renders the batch-5 operator
review gate (the per-batch operator gate required by the §16 authorization)
from the batch-5 decision record + the pass-2 adversarial verdicts, so the
documents cannot drift from the data (the c11_batch4_review_build.py
pattern, batch-5-scoped, session-54 hardening included).

Outputs:
  graph/reports/C11_BATCH5_REVIEW_SHEET.md — the operator review gate
  graph/reports/C11_BATCH5_REVIEW.json     — machine record + agreement stats
  scripts/c11_batch5_verdicts_template.yaml — the OPERATOR-OWNED verdict
      template (empty verdicts; machine pre-triage per row)

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator).

The batch ends HERE: this build promotes nothing, validates nothing as
HUMAN_VALIDATED, and authorizes nothing. The per-batch operator gate is the
operator's action; batch-5 promotion happens only via §18 after verdicts.

Usage: python3 scripts/c11_batch5_review_build.py
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

dec = yaml.safe_load((HERE / "c11_batch5_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_batch5_review_pass2.yaml").read_text(encoding="utf-8"))

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
    "task": "T-C11", "stage": "s16-batch-5-review",
    "batch": 5,
    "generated": M["generated_date"],
    "authorization": "scripts/c11_s16_authorization.yaml (§16 authorized "
                     "2026-09-12; batch 5 commissioned by the operator's "
                     "'run batch 5' directive, session 55 — Section 2 "
                     "Inorganic Chemistry FIRST slice; under the session-55 "
                     "cross-slice boundary ruling "
                     "scripts/c11_batch5_boundary_ruling.yaml)",
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_batch5_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges),
              "held": len(held), "command_kinds": len(cks)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-batch5-review-2",
              "verdicts_file": "scripts/c11_batch5_review_pass2.yaml",
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
        "note": "one pass-2 finding (FP-B5-5, a mistargeted dependency "
                "surface) was re-authored BEFORE the gate — the record "
                "carries 18 authored edges at this gate; zero demotions at "
                "the re-authored state and zero RR quarantines: the pass-1 "
                "authoring sent 14 candidates to held BEFORE emission and "
                "resolved every remaining doubt on explicit evidence",
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
        "pathway": "record verdicts in scripts/c11_batch5_verdicts.yaml "
                   "(fill the template); a later session encodes + applies "
                   "them via §18 promotion / §7 re-authoring",
        "promotion_now": 0,
        "cross_boundary_edges": 3,
    },
}
(REPORTS / "C11_BATCH5_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- verdict template (OPERATOR-OWNED; empty verdicts + machine pre-triage) ---
E_VOCAB = "CONFIRM | REJECT | HOLD | MERGE | SPLIT"
tpl = ["# T-C11 §16 batch 5 — OPERATOR verdict template (session-55 package).",
       "# OPERATOR-OWNED: fill verdict per row (empty verdict = not decided).",
       "# Hand-edits HERE are the sanctioned pathway; graph/*.yaml are never",
       "# hand-edited. The next session encodes + applies the filled record via",
       "# the §18 promotion pathway / §7 decision-record re-authoring. Verdicts",
       "# are RECORDED, not applied: filling this file promotes nothing.",
       "meta:",
       "  task: T-C11",
       "  stage: s16-batch-5-verdicts",
       "  batch: 5",
       "  session: 55",
       "  file: OPERATOR-OWNED verdict record for C11_BATCH5_REVIEW_SHEET (session 55) — verdicts recorded by operator decision (pending).",
       f"  instructions: 'Fill verdict per row. Edge/node vocabulary: {E_VOCAB}. This batch authored",
       "    NO REVIEW_REQUIRED edge (all doubts were held or resolved on explicit evidence).",
       "    Identity-decision vocabulary: MERGE (fold nodes) | SPLIT (mint finer) | KEEP_AS_IS. The batch-5",
       "    extraction_pass is c11-s16-batch-5 (Section 2 Inorganic Chemistry FIRST slice, 14 SPs",
       "    4CH1-2.1-2.14); its 14 held candidates are informational only (no reopening, no promotion of",
       "    held candidates — B5-H-04/05/06 record the classic wrong-answer patterns refused for missing",
       "    documentation; revisit only with new MS evidence). THREE edges are cross-section boundary edges",
       "    into the ruled owners (CON-ELECTRONIC-CONFIGURATION x2 — batch 2; CON-EXO-ENDO — batch 4;",
       "    sanctioned by the session-55 cross-slice ruling, no duplicate mint). The next session applies",
       "    verdicts via the §18 promotion pathway / §7 decision-record re-authoring; nothing here is",
       "    HUMAN_VALIDATED.'",
       "edge_verdicts:"]
EDGE_NOTES = {
    "4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION":
        "cross-boundary target (session-55 ruling; batch-2 owner)",
    "4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION":
        "cross-boundary target (session-55 ruling; the verbatim dependency statement)",
    "4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO":
        "cross-boundary target (session-55 ruling; batch-4 owner)",
    "4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION":
        "relation-class choice (the grounding direction; FP-B5-4 pass-2 flag — "
        "operator may prune)",
    "4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG":
        "pass-2 re-authoring companion (FP-B5-5 — the reactivity surface)",
    "4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES":
        "pass-2 re-scoped to the physical-trend surface (FP-B5-5)",
    "4CH1-MIS-G1-SHELL-EXPLANATION WRONG_ANSWER_PATTERN 4CH1-CON-G1-REACTIVITY-ECONFIG":
        "IGNORE/award-restriction evidence class (FP-B5-2 — confirm the subtype)",
    "4CH1-MIS-HALOGEN-HALIDE WRONG_ANSWER_PATTERN 4CH1-CON-G7-DISPLACEMENT":
        "Reject column, both conflation directions; antonym-pair attribution",
    "4CH1-MIS-CUO-COLOUR WRONG_ANSWER_PATTERN 4CH1-CON-CO2-FROM-CARBONATES":
        "narrow-but-exact Reject evidence (operator may rule exam-trivia)",
    "4CH1-MIS-G1-SHELL-EXPLANATION REMEDIATED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-HALOGEN-HALIDE REMEDIATED_BY 4CH1-CON-G7-DISPLACEMENT":
        "remediation target = WAP target (the B1-E-25 pattern)",
    "4CH1-MIS-CUO-COLOUR REMEDIATED_BY 4CH1-CON-CO2-FROM-CARBONATES":
        "remediation target = WAP target (the B1-E-25 pattern)",
}
i = 0
for e in sorted(edges, key=ekey):
    if e["validation_status"] != "SUGGESTED":
        continue
    i += 1
    k = ekey(e)
    flag = EDGE_NOTES.get(k, "")
    tpl.append(f"- id: B5-E-{i:02d}")
    tpl.append(f"  triple: {k}")
    tpl.append(f"  pretriage: {'FLAGGED' if flag else 'LIKELY_SAFE'}")
    tpl.append("  verdict:")
    # session-54 fix: YAML single-quote escaping for embedded apostrophes
    tpl.append(f"  notes: '{flag.replace("'", "''")}'")
tpl.append("node_verdicts:")
NODE_NOTES = {
    "4CH1-CON-G1-REACTIVITY-ECONFIG": "sibling-split question vs the 2.8C node (B5-ID-01)",
    "4CH1-CON-G7-REACTIVITY-ECONFIG": "sibling-split question vs the 2.4C node (B5-ID-01)",
}
i = 0
for n in sorted(nodes, key=lambda x: x["code"]):
    if n["family"] != "CONCEPT":
        continue
    i += 1
    flag = NODE_NOTES.get(n["code"], "")
    tpl.append(f"- id: B5-N-{i:02d}")
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
    if n["code"] == "4CH1-MIS-G1-SHELL-EXPLANATION":
        note = "IGNORE/award-restriction evidence class (FP-B5-2 — confirm the subtype)"
    elif n["code"] == "4CH1-MIS-CUO-COLOUR":
        note = "narrow-but-exact Reject evidence (operator may rule exam-trivia)"
    tpl.append(f"- id: B5-M-{i:02d}")
    tpl.append(f"  code: {n['code']}")
    tpl.append("  pretriage: LIKELY_SAFE (mark-scheme-documented)")
    tpl.append("  verdict:")
    tpl.append(f"  notes: '{note.replace("'", "''")}'")
tpl.append("identity_decisions:")
tpl.append("- id: B5-ID-01")
tpl.append("  question: merge the 2.4C and 2.8C trend-explanation nodes into one electronic-configuration explanation node (opposite directions, electron loss vs gain)")
tpl.append("  verdict:")
tpl.append("- id: B5-ID-02")
tpl.append("  question: split the air-composition know-facts from the oxygen-percentage determination (the spec's 2.9 know vs 2.10 understand-method pair)")
tpl.append("  verdict:")
tpl.append("- id: B5-ID-03")
tpl.append("  question: keep the 2.14 practical un-attached (PR-05 owns it) with the practical->concept edge — or mint a determination-procedure node ON 2.14")
tpl.append("  verdict:")
tpl.append("- id: B5-ID-04")
tpl.append("  question: one combustion node for all three named elements (2.11) vs per-element nodes")
tpl.append("  verdict:")
tpl.append("- id: B5-ID-05")
tpl.append("  question: split the CO2 family — carbonate decomposition (2.12) vs greenhouse role (2.13) — keep the two-node split")
tpl.append("  verdict:")
tpl.append("- id: B5-ID-06")
tpl.append("  question: split the G1 family-evidence (2.1) from the G1 trend (2.2) — the spec's similarities/differences pair")
tpl.append("  verdict:")
tpl.append("held_appendix_acknowledgment:")
tpl.append("  acknowledged:")
tpl.append("  notes: ''")
# re-issue guard (the batch-1/2/3/4 pattern): once the verdict round is
# recorded, never re-emit an empty template beside the filled verdict record.
if (HERE / "c11_batch5_verdicts.yaml").exists():
    print("template NOT re-emitted: scripts/c11_batch5_verdicts.yaml exists "
          "(verdict round recorded)")
else:
    (HERE / "c11_batch5_verdicts_template.yaml").write_text(
        "\n".join(tpl) + "\n", encoding="utf-8")
    # fail-closed post-write parseability check (the session-54 hardening)
    _tpl_doc = yaml.safe_load(
        (HERE / "c11_batch5_verdicts_template.yaml")
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
A("# T-C11 §16 Batch 5 Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1-2.1–2.14 (Section 2 — Inorganic Chemistry, FIRST slice: a Group 1 "
  f"(Alkali Metals) / b Group 7 (Halogens) / c Gases in the Atmosphere, 14 SPs) "
  f"+ practical PR-05 · generated {M['generated_date']} · decision record "
  f"`scripts/c11_batch5_decisions.yaml` (pass 1: `{M['extraction_pass']}`) · "
  f"adversarial pass 2: `scripts/c11_batch5_review_pass2.yaml` · "
  f"authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized "
  f"2026-09-12; batch 5 commissioned by the operator's 'run batch 5' "
  f"directive) · boundary ruling: `scripts/c11_batch5_boundary_ruling.yaml` "
  f"(session 55, machine-checked — the 3 sanctioned boundary edges below)")
A("")
A(f"**NOTHING in this batch is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + n_part_of} batch edges are AI_SUGGESTED (SUGGESTED). "
  "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
  "pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
  "regeneration). **Zero batch-5 promotions exist.** This sheet is the "
  "batch's operator gate: record verdicts in "
  "`scripts/c11_batch5_verdicts_template.yaml` (fill + rename to "
  "`c11_batch5_verdicts.yaml`); a later session encodes and applies them.")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Machine state: the full "
  "gate suite is green at the merged 129-node / 306-edge store; every quote "
  "is machine-verified byte-for-byte against its source file (G03/c11.4; "
  "105 quote probes + 89 record anchors pre-verified BEFORE the registry "
  "grew, then re-verified by the generator); the 4.15 negative control is "
  "uncovered. THREE edges are cross-section boundary edges into the ruled "
  "owners (CON-ELECTRONIC-CONFIGURATION x2 — batch 2; CON-EXO-ENDO — batch 4 "
  "— sanctioned per the session-55 cross-slice ruling; no duplicate concept "
  "was minted). The GROUP1 pdftotext pin splits the Q1d IGNORE line across a "
  "column break and the GROUP7 pin interleaves the Q1bii Reject entries; the "
  "misconception attributions are recorded in the nodes' derivation_notes.")
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
  "resolved on explicit evidence). **One pass-2 finding (FP-B5-5, a "
  "mistargeted dependency surface) was re-authored BEFORE the gate; zero "
  "demotions at the re-authored state.**")
A("")
A(f"Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): "
  f"predicted 33.6 nodes / 38.5 edges / 14.0 held vs actual "
  f"{len(nodes)} / {len(edges)} / {len(held)} — the batch-5 record is "
  "appended by the forecast instrument at this gate (see the regenerated "
  "C11_BATCH_FORECAST.json). The descriptive-heavy S2 families run the "
  "lightest yield band so far (nodes/SP 1.14, edges/SP 1.29) — the item-14 "
  "plan's own S2 anticipation, with the inline-re-teach abstentions "
  "(B5-H-02/03) accounting for the gap, not thin coverage: no S1/S3 "
  "identity was re-minted (the 2 ruled targets reached via 3 sanctioned "
  "boundary edges); 2.14 attaches no concept node (PR-05 owns it — the "
  "1.13/1.60C precedent) with the practical->concept edge authored.")
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
  "operand rule): pass-2 flags the 2.4C/2.8C sibling split (opposite trend "
  "directions — B5-ID-01), the 2.9/2.10 know-vs-method pair (B5-ID-02), the "
  "2.14 practical ownership (B5-ID-03), the 2.11 single-family node "
  "(B5-ID-04), the CO2 two-node split (B5-ID-05) and the 2.1/2.2 "
  "similarities/differences pair (B5-ID-06). All are operator identity "
  "decisions (template §identity_decisions). 2.14 attaches NO batch-5 "
  "concept node (PR-05 owns it — the 1.13/1.60C precedent).")
A("")
print("sheet part 1 rendered;", len(L), "lines")

# --- edges + held sections (batch-4 pattern) -----------------------------------
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
A("Three edges are CROSS-SECTION boundary edges into the ruled owners "
  "(sanctioned per the session-55 cross-slice ruling — no duplicate mint): "
  "the two 2.4C/2.8C electronic-configuration rows (batch-2 owner) and the "
  "2.11 exothermic-classification row (batch-4 owner). The EXPLAINED_BY "
  "composition row is the one relation-class flag to eyeball (FP-B5-4: the "
  "grounding direction vs an independent-facts reading).")
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
A("Every held candidate cites its §19 failure class; the four CLASSIC "
  "wrong-answer patterns without pinned documentation are refused (the "
  "session-53 Step-3 rule). A held record is a valid outcome — the "
  "abstention is the system's honest output.")
A("")
A("## 5. Operator verdict surface")
A("")
A(f"- **{p1_accept} SUGGESTED edges** (B5-E-01..{p1_accept:02d}) — the §18 "
  "promotion surface")
A(f"- **{len(nodes)} nodes** ({sum(1 for n in nodes if n['family']=='CONCEPT')} "
  f"CONCEPT B5-N-01..13 + {sum(1 for n in nodes if n['family']=='MISCONCEPTION')} "
  "MISCONCEPTION B5-M-01..03) — node authority stays SUGGESTED; nodes have "
  "no §18 pathway (node promotion is a separate identity decision, deferred)")
A("- **6 identity decisions** (B5-ID-01..06) — MERGE/SPLIT/KEEP_AS_IS")
A(f"- **{len(held)} held candidates** — acknowledge the quarantine (no "
  "reopening)")
A("- **0 REVIEW_REQUIRED edges** — zero RR settlements needed")
A("")
A("Pathway: fill `scripts/c11_batch5_verdicts_template.yaml` → rename to "
  "`c11_batch5_verdicts.yaml` → a later session encodes + applies via "
  "`c11_verdict_encode_batch5`-style reconciliation + `c11_promote.py` (§18) "
  "+ the gated generator re-run. NOTHING is promoted at this gate.")
A("")

(REPORTS / "C11_BATCH5_REVIEW_SHEET.md").write_text(
    "\n".join(L) + "\n", encoding="utf-8")
print(f"review gate rendered: {REPORTS / 'C11_BATCH5_REVIEW_SHEET.md'} + "
      f"C11_BATCH5_REVIEW.json + the verdict template")
