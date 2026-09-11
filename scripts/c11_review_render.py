#!/usr/bin/env python3
"""
T-C11 — c11_review_render.py: renders the pilot human-review sheet and machine
review record from the pass-1 decision record + the pass-2 adversarial verdicts
(so the documents cannot drift from the data).

Outputs:
  graph/reports/C11_PILOT_REVIEW_SHEET.md   — the operator review gate
  graph/reports/C11_PILOT_REVIEW.json       — machine record incl. agreement stats

Agreement statistics are RAW AGREEMENT (pass-2 verdict vs pass-1 emission),
explicitly NOT Cohen's kappa — one human rater exists (the operator); faking a
two-rater kappa would violate the project's honesty constraints (§12).

Usage: python3 scripts/c11_review_render.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"

dec = yaml.safe_load((HERE / "c11_pilot_decisions.yaml").read_text(encoding="utf-8"))
p2 = yaml.safe_load((HERE / "c11_pilot_review_pass2.yaml").read_text(encoding="utf-8"))

M = dec["meta"]
nodes = {n["code"]: n for n in dec["nodes"]}
edges = dec["edges"]
held = dec.get("held", [])


def op_mark(rec):
    """Operator column cell: decision mark if an operator_decision block
    exists on the record, else an open checkbox. Verdicts are operator-side
    review state (REJECT/HOLD/PENDING) — never HUMAN_VALIDATED (that remains
    the promotions-file pathway, §18)."""
    od = rec.get("operator_decision") or {}
    if not od:
        return "☐"
    v = od.get("verdict")
    d = od.get("decided_date") or od.get("presented_date") or ""
    if v == "PENDING":
        return f"PENDING (presented {d})"
    return f"**{v}** (operator, {d})"


def op_blocks():
    """All operator_decision blocks (edges + held candidates) for the sheet's
    decisions section and the machine record."""
    out = []
    for e in edges:
        od = e.get("operator_decision")
        if od:
            out.append({"record": f"{e['source']} {e['relation']} {e['target']}",
                        **od})
    for h in held:
        od = h.get("operator_decision")
        if od:
            out.append({"record": f"{h['id']} (held candidate: {h['candidate']})",
                        **od})
    return out


OP_DECISIONS = op_blocks()


def ekey(e):
    return f"{e['source']} {e['relation']} {e['target']}"


def short_prov(p):
    return (f"{p.get('derivation_method')} · {p.get('upstream','')}")


def quote_line(a):
    q = a["quote"]
    if len(q) > 110:
        q = q[:107] + "..."
    return (f"    - `{a['kind']}` {Path(a['file']).name} — \"{q}\"")


# --- agreement statistics (raw, NOT kappa) ------------------------------------
node_p2 = p2["nodes"]
edge_p2 = p2["edges"]
n_conf = sum(1 for v in node_p2.values()
             if v["verdict"].startswith("CONFIRM"))
e_conf = sum(1 for v in edge_p2.values() if v["verdict"].startswith("CONFIRM"))
e_hold = sum(1 for v in edge_p2.values() if v["verdict"] == "HOLD")
e_rej = sum(1 for v in edge_p2.values() if v["verdict"] == "REJECT")
# pass-1 emission of an edge as SUGGESTED counts as "accept"; REVIEW_REQUIRED
# counts as "uncertain". Pass-2 CONFIRM* = accept, HOLD = uncertain, REJECT.
p1_accept = sum(1 for e in edges if e["validation_status"] == "SUGGESTED")
p1_uncert = sum(1 for e in edges if e["validation_status"] == "REVIEW_REQUIRED")
agree = sum(1 for e in edges
            if (e["validation_status"] == "SUGGESTED"
                and edge_p2[ekey(e)]["verdict"].startswith("CONFIRM")))
uncert_concordant = sum(1 for e in edges
                         if e["validation_status"] == "REVIEW_REQUIRED"
                         and edge_p2[ekey(e)]["verdict"] in ("HOLD", "REJECT"))
asserted = sum(1 for e in edges if e["validation_status"] == "SUGGESTED")
raw_agreement_edges = agree / asserted if asserted else 1.0
open_uncertain = [ekey(e) for e in edges
                  if e["validation_status"] == "REVIEW_REQUIRED"]
raw_agreement_nodes = n_conf / len(nodes)

json_out = {
    "task": "T-C11", "stage": "pilot-review",
    "generated": M["generated_date"],
    "pass1": {"extraction_pass": M["extraction_pass"],
              "decision_record": "scripts/c11_pilot_decisions.yaml",
              "nodes": len(nodes), "authored_edges": len(edges)},
    "pass2": {"reviewer": M["model_version"], "pass": "c11-pilot-review-2",
              "verdicts_file": "scripts/c11_pilot_review_pass2.yaml",
              "nodes_confirm": n_conf, "edges_confirm": e_conf,
              "edges_hold": e_hold, "edges_reject": e_rej},
    "agreement": {
        "metric": "RAW AGREEMENT (pass-2 vs pass-1 emission)",
        "explicitly_not": "Cohen's kappa (single human rater; see architecture §12)",
        "nodes": round(raw_agreement_nodes, 4),
        "edges_asserted": {"confirmed": agree, "total_asserted": asserted,
                            "rate": round(raw_agreement_edges, 4)},
        "edges_uncertain_concordant_nonassertion": uncert_concordant,
        "edges_open_operator_decision": open_uncertain,
    },
    "reviewed_nodes": [{"code": c, "verdict": v["verdict"], "note": v.get("note")}
                       for c, v in node_p2.items()],
    "reviewed_edges": [{"edge": ekey(e), "verdict": edge_p2[ekey(e)]["verdict"],
                        "note": edge_p2[ekey(e)].get("note")}
                       for e in edges],
    "held_review": p2["held_review"],
    "findings": p2["findings"],
    "operator_decisions": OP_DECISIONS,
    "operator_decisions_summary": {
        "decided": sum(1 for d in OP_DECISIONS
                       if d.get("verdict") in ("REJECT", "HOLD", "ACCEPT")),
        "pending": sum(1 for d in OP_DECISIONS
                       if d.get("verdict") == "PENDING"),
        "note": "Operator review verdicts recorded as operator_decision blocks "
                "in the decision record (session 41, 2026-09-11; re-authored "
                "per architecture §8). REJECT of PR-03 -> CON-MOLE applied by "
                "re-authoring: preserved as rejected candidate HELD-13. None of "
                "these is a promotion — HUMAN_VALIDATED remains exclusively the "
                "c11_promotions.yaml pathway.",
    },
    "operator_gate": "Review every §2/§3 row; verdicts are recorded as "
                     "operator_decision blocks (re-authored into the decision "
                     "record); promotion of an exact ratified identity runs "
                     "via scripts/c11_promote.py (§18). Nothing is promoted by "
                     "this document.",
}
(REPORTS / "C11_PILOT_REVIEW.json").write_text(
    json.dumps(json_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# --- review sheet --------------------------------------------------------------
L = []
A = L.append
A("# T-C11 Pilot Review Sheet — Concept / Prerequisite / Misconception Graph")
A("")
A(f"Slice 4CH1-1.25–1.36 · generated {M['generated_date']} · decision record "
  f"`scripts/c11_pilot_decisions.yaml` (pass 1: `{M['extraction_pass']}`) · "
  f"adversarial pass 2: `scripts/c11_pilot_review_pass2.yaml`")
A("")
A(f"**NOTHING in the graph is authoritative.** All {len(nodes)} nodes / "
  f"{len(edges) + sum(len(n['spec_points']) for n in dec['nodes'] if n['family']=='CONCEPT')} "
  "edges are AI_SUGGESTED (SUGGESTED or REVIEW_REQUIRED). HUMAN_VALIDATED is "
  "reachable only by your promotion command — the pathway is BUILT and inert: "
  "`scripts/c11_promote.py` (exact-edge-identity only, architecture §18), "
  "currently **zero promotions recorded**. Operator review verdicts are "
  "recorded as `operator_decision` blocks in the decision record (§8 below).")
A("")
A("How to review: for each row check the quoted evidence actually appears in "
  "the cited file and actually says what the record claims; then rule on the "
  "relation CLASS and direction, not just existence. Verdict vocabulary: "
  "CONFIRM / REJECT / HOLD / MERGE (identity) / SPLIT (identity). Machine "
  "state: `graph_check.py` groups 10–11 + `c11_negative_test.py` are green; "
  "every quote is machine-verified byte-for-byte against its source file.")
A("")
A("## 1. Totals & second-pass agreement")
A("")
A("| | nodes | authored edges | |")
A("|---|---|---|")
A(f"| pass-1 (extraction) | {len(nodes)} | {len(edges)} (+{sum(len(n['spec_points']) for n in dec['nodes'] if n['family']=='CONCEPT')} derived PART_OF) |")
A(f"| pass-2 verdicts | {n_conf} CONFIRM(+note) | {e_conf} CONFIRM(+note) · {e_hold} HOLD · {e_rej} REJECT |")
A("")
A(f"Raw agreement (NOT κ — single human rater, architecture §12): nodes "
  f"{n_conf}/{len(nodes)} = {raw_agreement_nodes:.1%}; edges — of the "
  f"{asserted} edges pass-1 asserted (SUGGESTED), pass-2 confirmed {agree} "
  f"({raw_agreement_edges:.1%}); pass-1 emitted {p1_uncert + 1} edges as "
  "REVIEW_REQUIRED, both concordantly NOT asserted by pass 2 (HOLD/REJECT). "
  "Operator session 41: the first (PR-03 → CON-MOLE) **REJECTED** and "
  "re-authored out of the graph (preserved as HELD-13); the second "
  "(GAS-VOL-CALC → AVOGADRO-LAW) **HOLD** — remains open as REVIEW_REQUIRED. "
  "No pass-2 verdict contradicts a pass-1 assertion.")
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
      f"{n['confidence']} | {evlines} | {v['verdict']} | {op_mark(n)} |")
A("")
A("Identity-policy notes (split-first; merges are operator-only): pass-2 flags "
  "the yield triple (CON-YIELD / CON-THEOR-YIELD / CON-PERCENT-YIELD) and "
  "reminds that all aliases are merge inputs. No pass-2 merge recommendations "
  "beyond §3.1 notes.")
A("")
A(f"## 3. Authored semantic edges ({len(edges)})")
A("")
A("Direction conventions: REQUIRES_PREREQUISITE source=dependent → "
  "target=prerequisite; EXPLAINED_BY explained → explainer; REMEDIATED_BY "
  "misconception → concept.")
A("")
A("### 3.1 REVIEW_REQUIRED (open operator decisions)")
A("")
A("Pass-1 emitted two REVIEW_REQUIRED edges; session 41 settled both — the "
  "first (PR-03 → CON-MOLE) was REJECTED by the operator and re-authored out "
  "of the graph (see HELD-13 in §4), the second remains open under an "
  "operator HOLD. Full decision records in §8.")
A("")
A("| edge | conf | evidence | ambiguity (pass-1) | pass-2 | operator |")
A("|---|---|---|---|---|---|")
for e in edges:
    if e["validation_status"] != "REVIEW_REQUIRED":
        continue
    v = edge_p2[ekey(e)]
    ev = "<br>".join(f"“{a['quote'][:100]}”" for a in e["evidence"])
    amb = (e.get("ambiguity_note") or "")[:220]
    A(f"| `{e['source']}` **{e['relation']}** `{e['target']}` | {e['confidence']} | "
      f"{ev} | {amb} | {v['verdict']}: {(v.get('note') or '')[:200]} | {op_mark(e)} |")
A("")
A(f"### 3.2 SUGGESTED edges ({sum(1 for e in edges if e['validation_status'] == 'SUGGESTED')})")
A("")
A("Two of these are medium-confidence judgments formally gated on operator "
  "review (PENDING — session-41 presentations, §8): MOLAR-GAS-VOL "
  "EXPLAINED_BY AVOGADRO-LAW and MIS-EQ-SUBSCRIPT REMEDIATED_BY "
  "CONSERVATION-MASS. They are NOT promotable until the operator decides.")
A("")
A("| edge | method | conf | evidence (quote) | upstream | pass-2 | operator |")
A("|---|---|---|---|---|---|---|")
for e in edges:
    if e["validation_status"] == "REVIEW_REQUIRED":
        continue
    v = edge_p2[ekey(e)]
    ev = "<br>".join(f"“{a['quote'][:100]}”" for a in e["evidence"])
    up = e["provenance"]["upstream"]
    if len(up) > 90:
        up = up[:87] + "..."
    A(f"| `{e['source']}` **{e['relation']}** `{e['target']}` | "
      f"{e['provenance']['derivation_method']} | {e['confidence']} | {ev} | {up} | "
      f"{v['verdict']} | {op_mark(e)} |")
A("")
A(f"### 3.3 Derived PART_OF edges ({sum(len(n['spec_points']) for n in dec['nodes'] if n['family']=='CONCEPT')})")
A("")
A("Derived deterministically from node attachments (concepts.yaml); each "
  "carries the attachment's evidence anchors and the node's provenance. Not "
  "re-listed here — review them via the §2 node rows. Machine-verified: the "
  "PART_OF set must exactly equal the declared attachments (c11.7).")
A("")
A(f"## 4. Held / rejected candidates ({len(held)}) — the abstention record")
A("")
A("These were considered and NOT drawn. The pilot's success criterion includes "
  "correct abstention; review that each hold reason is right (pass-2 already "
  "did — column below). Overriding a hold = re-authoring the decision record, "
  "never hand-editing the graph. HELD-13 is the operator-REJECTED former "
  "REVIEW_REQUIRED edge (session 41) — permanently non-promotable.")
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
    A(f"| {h['id']} | {h['status']} | {cand} | {r} | {p2v} | {op_mark(h)} |")
A("")
A("## 5. Findings (pass-2, for the pilot report)")
A("")
for f_ in p2["findings"]:
    A(f"- **{f_['id']} ({f_['kind']})** — {f_['detail']}")
A("")
A("## 6. Command-kind tags (guide §8)")
A("")
A("| SP | verb | guide class | demanded substance | operator |")
A("|---|---|---|---|---|")
for c in sorted(dec["command_kinds"], key=lambda x: x["code"]):
    A(f"| {c['code']} | {c['verb']} | {c['guide_class']} | "
      f"{c['demanded_substance']} | ☐ |")
A("")
A("## 7. Negative control (4CH1-4.15)")
A("")
A("Zero concepts, zero edges, zero coverage for 4.15. The premise "
  "(“All these fuels contain carbon, hydrogen and small quantities of "
  "sulfur”, Definition-of-combustion note, mapped 4.11–4.13) and the stated "
  "consequence (“The sulfur dioxide produced from the combustion of fossil "
  "fuels dissolves in rainwater”, Nitrogen-Oxides-&-Sulfur-Dioxide note, "
  "mapped 4.14/4.16) were both present — the machine rules (attachment rule "
  "§2 + anchor admissibility §11 + negative test class 11) make the "
  "premise+consequence edge structurally impossible. Remediation is a corpus "
  "decision (new note / student-book OCR), never a graph-side inference. "
  "Operator: acknowledge ☐")
A("")
A("## 8. Operator decisions recorded (session 41, 2026-09-11)")
A("")
A("Verdicts are operator-side review decisions, recorded as "
  "`operator_decision` blocks in `scripts/c11_pilot_decisions.yaml` "
  "(re-authored per architecture §8; never emitted into the graph; never "
  "HUMAN_VALIDATED — promotion remains exclusively `c11_promote.py` + "
  "`c11_promotions.yaml`, §18). Reasons are verbatim from the operator.")
A("")
A("| record | verdict | decided/presented | reasons / note |")
A("|---|---|---|---|")
for d in OP_DECISIONS:
    reasons = d.get("reasons")
    if reasons:
        txt = " · ".join(reasons)
    else:
        txt = (d.get("note") or "")[:300]
    when = (d.get("decided_by") or "presented") + ", " \
        + (d.get("decided_date") or d.get("presented_date") or "")
    A(f"| `{d['record']}` | **{d['verdict']}** | {when} | {txt} |")
A("")
A("Open after this round: the two PENDING medium-confidence judgments (§3.2) "
  "and the per-row verdicts on the remaining SUGGESTED edges and nodes. "
  "Ontology ruling OD-1 (yield triple stays split) is recorded in "
  "`C11_ARCHITECTURE.md` §20.")
A("")
A("## 9. After review")
A("")
A("1. Record further verdicts — they are re-authored into the decision record "
  "as `operator_decision` blocks (REJECT/HOLD/PENDING; merges/splits remain "
  "operator-only identity decisions).")
A("2. Promote exact ratified edge identities via `scripts/c11_promote.py` "
  "(--edge 'SOURCE RELATION TARGET'); a staged batch command can be derived "
  "mechanically from your confirms (c10_promote pattern).")
A("3. Expansion to the full 4CH1 graph requires the §16 criteria (all gates "
  "green + this review recorded + scoped expansion plan) and explicit "
  "operator authorization — see `C11_S16_GATE_REPORT.md`.")
A("")
A("---")
A(f"Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, "
  f"`graph/spec_command_kinds.yaml` (generated, gated) · "
  f"`C11_PILOT_REVIEW.json` (this sheet's machine record) · contract: "
  f"`C11_ARCHITECTURE.md`")

(REPORTS / "C11_PILOT_REVIEW_SHEET.md").write_text("\n".join(L) + "\n",
                                                   encoding="utf-8")
print(f"wrote {REPORTS / 'C11_PILOT_REVIEW_SHEET.md'}")
print(f"wrote {REPORTS / 'C11_PILOT_REVIEW.json'}")
print(f"raw agreement (NOT kappa): nodes {raw_agreement_nodes:.1%}; edges "
      f"{agree}/{asserted} asserted confirmed; {uncert_concordant} uncertain edges "
      f"concordantly non-asserted (open: {open_uncertain})")
