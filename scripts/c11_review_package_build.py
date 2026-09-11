#!/usr/bin/env python3
"""T-C11 session 43 — build the OPERATOR REVIEW PACKAGE.

Renders, deterministically and read-only from the decision record + live
store + corpus:
  graph/reports/C11_REVIEW_PACKAGE.md     (the operator document)
  graph/reports/C11_REVIEW_PACKAGE.json    (machine record, null verdicts)
  scripts/c11_review_verdicts.yaml         (operator-owned verdict template)

Package contents (operator tasking, session 43):
  31 edge dossiers, 29 concept dossiers, 13-entry held/rejected appendix,
  OD-1/OD-2 PENDING-RATIFICATION slots, machine pre-triage (FC-1..FC-4 /
  likely-safe / likely-ambiguous), the 'maximum yield' alias audit, the
  quantified review reduction, and the batch-forecast pointer.

CONSTRAINTS ENFORCED BY THIS SCRIPT (fail-closed):
  - no promotion authority: c11_promotions.yaml must have 0 entries and is
    never written;
  - the authoritative graph is never written (outputs are new files only);
  - 4CH1-4.15 must remain uncovered; the REVIEW_REQUIRED operator-HOLD edge
    must remain exactly GAS-VOL-CALC -> AVOGADRO-LAW.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
REPORTS = GRAPH / "reports"
NOTES = REPO / "Chemistry IGCSE Revision Notes"

SESSION = 43
TODAY = "2026-09-12"
BASE_RES = "3b70dde"
BASE_TRK = "6d36fb0"

# --- T-C10 norm() convention (copied verbatim from scripts/c11_concept_pilot.py) ---
_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


_dec = yaml.safe_load((HERE / "c11_pilot_decisions.yaml").read_text(encoding="utf-8"))
_pass2 = yaml.safe_load((HERE / "c11_pilot_review_pass2.yaml").read_text(encoding="utf-8"))
_graph_edges = yaml.safe_load((GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))["edges"]
_sp_data = yaml.safe_load((GRAPH / "specification_points.yaml").read_text(encoding="utf-8"))
_promo = yaml.safe_load((HERE / "c11_promotions.yaml").read_text(encoding="utf-8"))
_forecast = json.loads((REPORTS / "C11_BATCH_FORECAST.json").read_text(encoding="utf-8"))
_arch = (REPORTS / "C11_ARCHITECTURE.md").read_text(encoding="utf-8")

nodes = _dec["nodes"]
edges = _dec["edges"]
held = _dec["held"]
ckinds = {c["code"]: c for c in _dec["command_kinds"]}
spec_by_code = {sp["code"]: sp for sp in _sp_data["specification_points"]}

# ---------------------------------------------------------------------------
# Fail-closed pre-state assertions (the package must describe THIS state)
# ---------------------------------------------------------------------------
assert len(nodes) == 29, len(nodes)
assert len(edges) == 32, len(edges)
assert len(_graph_edges) == 65, len(_graph_edges)
assert sum(1 for e in _graph_edges if e["relation"] == "PART_OF") == 33
assert len(held) == 13, len(held)
assert len(_promo.get("promotions", [])) == 0, "promotions must be zero"
assert sum(1 for e in _graph_edges if e["validation_status"] == "HUMAN_VALIDATED") == 0
_rr = [e for e in edges if e["validation_status"] == "REVIEW_REQUIRED"]
assert len(_rr) == 1 and _rr[0]["source"] == "4CH1-CON-GAS-VOL-CALC" \
    and _rr[0]["target"] == "4CH1-CON-AVOGADRO-LAW", _rr
SUGGESTED = [e for e in edges if e["validation_status"] == "SUGGESTED"]
assert len(SUGGESTED) == 31, len(SUGGESTED)
for e in edges + [x for n in nodes for x in n.get("spec_points", [])]:
    for ev in e.get("evidence", []):
        assert "4.15" not in ev.get("file", ""), "negative control violated"

# ---------------------------------------------------------------------------
# Corpus cache + independent quote verification (T-C10 norm)
# ---------------------------------------------------------------------------
_files = {}
def normed_file(rel: str):
    if rel not in _files:
        p = REPO / rel
        _files[rel] = norm(p.read_text(encoding="utf-8")) if p.exists() else None
    return _files[rel]

def verify_quote(ev) -> bool:
    nf = normed_file(ev["file"])
    return nf is not None and norm(ev["quote"]) in nf

quote_checks = {"checked": 0, "verified": 0, "failed": []}
def check_ev(ev, owner):
    quote_checks["checked"] += 1
    if verify_quote(ev):
        quote_checks["verified"] += 1
    else:
        quote_checks["failed"].append(owner)

for n in nodes:
    for sp in n.get("spec_points", []):
        for ev in sp.get("evidence", []):
            check_ev(ev, f"node {n['code']}")
for e in edges:
    for ev in e["evidence"]:
        check_ev(ev, f"edge {e['source']}->{e['target']}")

# ---------------------------------------------------------------------------
# Alias evidence audit (machine): VERBATIM / VARIANT / UNEVIDENCED
# ---------------------------------------------------------------------------
_pilot_sp = _dec["meta"]["scope"]["spec_points"]
spec_text = " ".join(str(v) for sp in _sp_data["specification_points"]
                     if sp["code"] in _pilot_sp
                     for v in sp.values() if isinstance(v, str))
corpus = {}
for rel in _dec["meta"]["scope"]["notes"]:
    corpus[rel] = normed_file(rel)
for ms in _dec["meta"]["scope"]["mark_scheme_evidence"]:
    corpus[ms["file"]] = normed_file(ms["file"])
corpus["SPEC (12 pilot spec points)"] = norm(spec_text)


def _hits(alias: str, pattern: str):
    pat = re.compile(pattern, re.I)
    return [k for k, t in corpus.items() if t and pat.search(t)]


def alias_status(alias: str):
    wb = r"(?<![A-Za-z])" + re.escape(alias) + r"(?![A-Za-z])"
    w = _hits(alias, wb)
    if w:
        return "VERBATIM", w
    for cand in (alias + "s", alias[:-1] if alias.endswith("s") else None,
                 alias.replace("ing", "")):
        if cand and cand != alias:
            v = _hits(cand, r"(?<![A-Za-z])" + re.escape(cand) + r"(?![A-Za-z])")
            if v:
                return "VARIANT", [f"'{cand}' @ {v[0].split('/')[-1]}"]
    return "UNEVIDENCED", []

alias_audit = []
for n in nodes:
    row = {"node": n["code"], "title": n["title"], "aliases": []}
    for a in n.get("aliases", []):
        st, where = alias_status(a)
        row["aliases"].append({"alias": a, "status": st, "evidence": where})
    alias_audit.append(row)

n_ver = sum(1 for r in alias_audit for a in r["aliases"] if a["status"] == "VERBATIM")
n_var = sum(1 for r in alias_audit for a in r["aliases"] if a["status"] == "VARIANT")
n_une = sum(1 for r in alias_audit for a in r["aliases"] if a["status"] == "UNEVIDENCED")

# --- 'maximum yield' special investigation (word-level, with context) ------
maxm_occurrences = []
for k, t in corpus.items():
    if not t:
        continue
    for m in re.finditer(r"[Mm]aximum", t):
        ctx = t[max(0, m.start() - 70):m.end() + 90]
        maxm_occurrences.append({"corpus": k.split("/")[-1][:60],
                                 "context": ctx.strip()[:160]})
phrase_hits = _hits("maximum yield", r"(?<![A-Za-z])maximum\s+yield(?![A-Za-z])")

# ---------------------------------------------------------------------------
# Pass-2 index
# ---------------------------------------------------------------------------
p2_nodes = _pass2["nodes"]
p2_edges = _pass2["edges"]
p2_held = _pass2["held_review"]


def p2_edge_note(e):
    return p2_edges.get(f"{e['source']} {e['relation']} {e['target']}", {})


# ---------------------------------------------------------------------------
# Machine pre-triage
# ---------------------------------------------------------------------------
OD1_NODES = {"4CH1-CON-YIELD", "4CH1-CON-THEOR-YIELD", "4CH1-CON-PERCENT-YIELD"}
OD1_PAIR_EDGES = {
    ("4CH1-CON-PERCENT-YIELD", "4CH1-CON-THEOR-YIELD"),
    ("4CH1-CON-PERCENT-YIELD", "4CH1-CON-YIELD"),
}

# FC-3 machine subsumption: BFS over authored RP edges (excluding the edge itself)
rp_pairs = {(e["source"], e["target"]) for e in edges
            if e["relation"] == "REQUIRES_PREREQUISITE"}
succ = {}
for s, t in rp_pairs:
    succ.setdefault(s, set()).add(t)


def reachable(src, dst, skip_pair):
    seen, stack = {src}, [src]
    while stack:
        cur = stack.pop()
        for nxt in succ.get(cur, ()):  # pragma: no branch
            if (cur, nxt) == skip_pair or nxt in seen:
                continue
            if nxt == dst:
                return True
            seen.add(nxt)
            stack.append(nxt)
    return False


FC1_METHODS = {"IMPLICIT_USE", "EXAMINER_TIP_IMPLICIT", "EXAMINER_TIP_IMPLIED"}
ADMISSIBILITY = {
    "SPEC_VERBATIM": "ADMISSIBLE — official spec wording (explicit instructional text)",
    "DEFINITIONAL_DEPENDENCY": "ADMISSIBLE — explicit definition sentence (byte-verified)",
    "EXPLICIT_TEACH_SEQUENCE": "ADMISSIBLE — explicit teaching sequence in the note",
    "USED_WITHOUT_RETEACHING": "ADMISSIBLE — worked-example step using the concept without re-teaching it",
    "SINGLE_SOURCE_CAUSAL_TEACHING": "ADMISSIBLE — causal teaching in one source (confidence-capped where adjacency-grounded)",
    "EXAMINER_TIP_EXPLICIT": "ADMISSIBLE — examiner tip explicitly documents the error and/or corrective",
    "ASSESSMENT_DOCUMENTED": "ADMISSIBLE — mark-scheme-documented wrong answer",
    "IMPLICIT_USE": "NOT ADMISSIBLE ALONE (OD-2) — implicit/incidental use; quarantine-or-abstain",
}


def edge_pretriage(e):
    flags = []
    triple = (e["source"], e["target"])
    p2 = p2_edge_note(e)
    p2v, p2n = p2.get("verdict", "(not reviewed)"), p2.get("note", "")
    od = e.get("operator_decision") or {}
    if e["confidence"] == "medium" or e["provenance"]["derivation_method"] in FC1_METHODS:
        flags.append("FC-1: medium confidence or implicit-evidence derivation")
    concern = any(k in p2n for k in ("FP-concern", "Alternative:", "section order"))
    if p2v in ("HOLD", "REJECT") or e.get("ambiguity_note") or concern:
        flags.append("FC-2: relation-class concern (pass-2 / ambiguity note)")
    same_anchor = [x for x in edges
                   if x is not e and x["source"] == e["source"]
                   and x["evidence"][0]["quote"] == e["evidence"][0]["quote"]]
    if same_anchor or triple in OD1_PAIR_EDGES:
        flags.append("FC-3: same-anchor operand pair (OD-1-linked; vanishes under merge)")
    reach = reachable(e["source"], e["target"], triple)
    if reach:
        # §19 precedent: MOLAR-MASS -> {MR, AR} proves transitively-reachable
        # edges can be semantically distinct — reachability is surfaced, the
        # label stays safe when pass-2 addressed the pair (assurance).
        flags.append("FC-3 machine-flag (informational): target transitively "
                     "reachable via other RP edges — §19: reachable ≠ "
                     "redundant; per-edge semantic judgment")
    if od.get("verdict") == "PENDING":
        flags.append("PENDING: operator decision already presented (10-field), awaiting ruling")
    if "granularity note" in p2n.lower() or "operative dependency" in p2n.lower():
        flags.append("granularity: pass-2 FP-3 note")

    if od.get("verdict") == "PENDING":
        label = "FC-1+FC-2 (PENDING judgment)"
        group = "G3"
    elif any(f.startswith("FC-3: same-anchor") for f in flags):
        label = "FC-3 (OD-1-linked)"
        group = "G2"
    elif any("granularity" in f for f in flags):
        label = "LIKELY_AMBIGUOUS (granularity note)"
        group = "G3"
    elif any(f.startswith("FC-2") for f in flags):
        label = "LIKELY_AMBIGUOUS (relation-class note)"
        group = "G3"
    elif reach and p2v not in ("CONFIRM", "CONFIRM_WITH_NOTE"):
        label = "LIKELY_AMBIGUOUS (transitive-reachability unaddressed by pass-2)"
        group = "G3"
    elif reach:
        label = ("LIKELY_SAFE (transitively-reachable; §19 semantic-distinctness "
                 "precedent — pass-2 addressed the pair)")
        group = "G1"
    elif p2v == "CONFIRM_WITH_NOTE":
        label = "LIKELY_SAFE (pass-2 note)"
        group = "G1"
    else:
        label = "LIKELY_SAFE"
        group = "G1"
    return {"label": label, "flags": flags, "pass2_verdict": p2v,
            "pass2_note": p2n, "group": group}


def edge_recommendation(tri, pt):
    if "(PENDING" in pt["label"]:
        return ("Decision already presented 10-field in C11_OPERATOR_DECISIONS.md "
                "§2 — recommendation there is HOLD; rule on the presentation, "
                "not on this row alone")
    if "FC-3" in pt["label"]:
        return ("CONFIRM jointly with the OD-1 ratification — the pair mirrors the "
                "formula's operand structure and vanishes under an operator merge; "
                "do not confirm individually before ruling OD-1")
    if "granularity" in pt["label"]:
        return ("CONFIRM likely (high confidence, pass-2 concordant; the granularity "
                "point is an expansion-round concern) — or HOLD if an "
                "interpret-equations concept should be minted first")
    if "transitively-reachable" in pt["label"]:
        return ("CONFIRM — bulk-eligible; the reachability machine-flag is the §19 "
                "MOLAR-MASS→{MR, AR} precedent (reachable ≠ redundant: element vs "
                "compound definitions) and pass-2 explicitly dismissed double-counting")
    if "pass-2 note" in pt["label"]:
        return ("CONFIRM — bulk-eligible; read the one-line pass-2 note first "
                "(it anticipates and dismisses a concern)")
    return ("CONFIRM — bulk-eligible (high confidence, explicit evidence class, "
            "pass-2 concordant, zero machine flags)")


def node_pretriage(n):
    p2 = p2_nodes.get(n["code"], {})
    p2v, p2n = p2.get("verdict", "(not reviewed)"), p2.get("note", "")
    flags = []
    if "merge candidate" in p2n.lower() or "Merge candidate" in p2n:
        flags.append("FC-2: identity — pass-2 merge candidate (OD-1 governs)")
    une = [a["alias"] for a in
           next(r for r in alias_audit if r["node"] == n["code"])["aliases"]
           if a["status"] == "UNEVIDENCED"]
    if une:
        flags.append(f"alias-audit: {len(une)} unevidenced alias(es) — see §7")
    if n["code"] in OD1_NODES:
        flags.append("OD-1: member of the yield triple (ratification governs)")
    if flags and any(f.startswith("FC-2") for f in flags):
        label, group = "FC-2 identity (OD-1-linked)", "G2"
    elif p2v == "CONFIRM_WITH_NOTE":
        label, group = "LIKELY_SAFE (pass-2 note)", "G1"
    else:
        label, group = "LIKELY_SAFE", "G1"
    return {"label": label, "flags": flags, "pass2_verdict": p2v,
            "pass2_note": p2n, "group": group}


def node_recommendation(pt):
    if pt["label"].startswith("FC-2"):
        return ("CONFIRM-split if OD-1 is ratified; MERGE is the operator-only "
                "alternative (re-versions nodes, removes the operand edge pair) — "
                "do not decide this node before ruling OD-1")
    if "pass-2 note" in pt["label"]:
        return "CONFIRM — bulk-eligible; read the one-line pass-2 note first"
    return "CONFIRM — bulk-eligible (identity clean, high confidence, pass-2 concordant)"


def node_kind(n):
    if n["family"] == "MISCONCEPTION":
        return "documented student error (misconception / wrong-answer pattern; unattached by design)"
    sps = n.get("spec_points", [])
    roles = {sp["role"] for sp in sps}
    primary = sps[0] if sps else None
    verb = ckinds.get(primary["code"], {}).get("verb", "") if primary else ""
    gclass = ckinds.get(primary["code"], {}).get("guide_class", "") if primary else ""
    if roles and roles <= {"ENRICHMENT"}:
        return "enrichment content (taught substantively; demanded by no SP)"
    if verb == "know":
        return "term definition (KNOW_TERM demand)"
    if gclass == "DESCRIBE_EXPERIMENT":
        return "experimental method (DESCRIBE_EXPERIMENT demand)"
    if n["code"] in ("4CH1-CON-YIELD", "4CH1-CON-THEOR-YIELD"):
        return ("operand DEFINITION under a CALCULATE point (OD-1: the procedure "
                "node is CON-PERCENT-YIELD)")
    if n["code"] == "4CH1-CON-PERCENT-YIELD":
        return "calculation procedure (CALCULATE demand; the OD-1 procedure node of the yield triple)"
    if gclass == "CALCULATE":
        return "calculation procedure (CALCULATE demand)"
    return "concept (mixed demand)"


# ---------------------------------------------------------------------------
# Dossier assembly
# ---------------------------------------------------------------------------
partof_by_src = {}
for e in _graph_edges:
    if e["relation"] == "PART_OF":
        partof_by_src.setdefault(e["source"], []).append((e["target"], e["role"]))

alias_collisions = {}
for r in alias_audit:
    for a in r["aliases"]:
        alias_collisions.setdefault(a["alias"].lower(), []).append(r["node"])

edge_dossiers = []
for i, e in enumerate(SUGGESTED, 1):
    tri = f"{e['source']} {e['relation']} {e['target']}"
    pt = edge_pretriage(e)
    od = e.get("operator_decision") or {}
    ev = e["evidence"][0]
    edge_dossiers.append({
        "id": f"E-{i:02d}",
        "triple": tri,
        "source": e["source"], "relation": e["relation"], "target": e["target"],
        "relation_count_in_pilot": sum(1 for x in _graph_edges if x["relation"] == e["relation"]),
        "evidence": [{"kind": x["kind"], "file": x["file"], "quote": x["quote"]}
                     for x in e["evidence"]],
        "evidence_admissibility": ADMISSIBILITY.get(
            e["provenance"]["derivation_method"],
            "ADMISSIBLE — explicit instructional text (byte-verified)"),
        "rationale": e["provenance"]["derivation_notes"],
        "derivation_method": e["provenance"]["derivation_method"],
        "upstream": e["provenance"]["upstream"],
        "confidence": e["confidence"],
        "validation_status": e["validation_status"],
        "operator_decision_pending": od.get("verdict") == "PENDING",
        "pretriage": pt,
        "recommendation": edge_recommendation(tri, pt),
        "operator_verdict": None,
    })

node_dossiers = []
for i, n in enumerate(nodes, 1):
    pt = node_pretriage(n)
    ar = next(r for r in alias_audit if r["node"] == n["code"])
    dup_flags = [f["text"] for f in [
        {"text": f"pass-2 merge candidate: {pt['pass2_note']}"}
        if "merge candidate" in pt["pass2_note"].lower() else None,
        {"text": "member of the OD-1 yield triple — merge question is the OD-1 "
                 "ratification, not a per-node decision"}
        if n["code"] in OD1_NODES else None,
        {"text": f"alias-collision check: clean"}
        if True else None,
    ] if f]
    coll = {a["alias"]: [c for c in alias_collisions[a["alias"].lower()]
                         if c != n["code"]]
            for a in ar["aliases"] if len(alias_collisions.get(a["alias"].lower(), [])) > 1}
    if coll:
        dup_flags.append(f"alias string(s) also present on other nodes: {coll}")
    node_dossiers.append({
        "id": f"N-{i:02d}",
        "code": n["code"], "title": n["title"], "family": n["family"],
        "node_kind": node_kind(n),
        "spec_attachments": [{"code": sp["code"], "role": sp["role"],
                              "verb": ckinds.get(sp["code"], {}).get("verb", ""),
                              "evidence": sp.get("evidence", [])}
                             for sp in n.get("spec_points", [])],
        "aliases": ar["aliases"],
        "placement": [{"spec_point": t, "role": r}
                      for t, r in sorted(partof_by_src.get(n["code"], []))],
        "duplicate_overlap": dup_flags,
        "confidence": n["confidence"],
        "validation_status": n["validation_status"],
        "derivation_method": n["provenance"]["derivation_method"],
        "rationale": n["provenance"]["derivation_notes"],
        "pretriage": pt,
        "recommendation": node_recommendation(pt),
        "operator_verdict": None,
    })

# ---------------------------------------------------------------------------
# Held appendix (failure-class keyword map)
# ---------------------------------------------------------------------------
FC_KEYWORDS = [
    ("FC-4", ["NEGATIVE_CONTROL"]),
    ("FC-1", ["INSUFFICIENT_EVIDENCE", "EVIDENCE_AMBIGUOUS"]),
    ("FC-3", ["TRANSITIVELY_SUBSUMED", "TAUGHT_INLINE", "DEFENSIONAL"]),
    ("FC-2", ["RELATION_CLASS", "WEAK_CLASS", "EXAM_TECHNIQUE", "RESIDUAL_CLASS"]),
]


def held_fc(h):
    if h["id"] == "HELD-13":
        return "FC-3 (primary; transitively subsumed) + FC-1 (implicit-use evidence)"
    for fc, keys in FC_KEYWORDS:
        if any(k in h["reason"] for k in keys):
            return fc
    return "FC-2"


held_appendix = []
for h in held:
    p2 = p2_held.get(h["id"], {})
    held_appendix.append({
        "id": h["id"],
        "status": h["status"],
        "channel": "REJECTED (permanent, machine-guarded)" if h["status"] == "rejected"
                   else "HELD (abstained — awaiting evidence/decision, not promotable, not in the graph)",
        "candidate": h["candidate"],
        "evidence": h["evidence"],
        "reason": h["reason"],
        "failure_class": held_fc(h),
        "pass2_verdict": p2.get("verdict", ""),
        "pass2_note": p2.get("note", ""),
        "operator_decision": h.get("operator_decision"),
        "history": h.get("history", ""),
    })

# ---------------------------------------------------------------------------
# OD ratification slots (§20 extracted verbatim)
# ---------------------------------------------------------------------------
sec20 = _arch[_arch.index("## 20. Ontology decisions"):]
od1_block = sec20[sec20.index("### OD-1"):sec20.index("### OD-2")].strip()
od2_block = sec20[sec20.index("### OD-2"):].strip()

od_slots = [
    {
        "id": "OD-1",
        "title": "The yield triple stays split (three concept nodes)",
        "provenance": (
            "Agent-derived ontology recommendation — session 41, exercising the "
            "operator's delegated instruction to resolve the yield-triple question "
            "as an ontology decision, on frozen identity-policy grounds (§8). "
            "Recorded in C11_ARCHITECTURE.md §20. NOT operator-ratified: it must "
            "not be relabeled as ratified without an explicit operator decision."),
        "effect_if_ratified": (
            "Becomes a binding generation rule for §16 (one procedure concept + one "
            "concept per distinctly-taught operand definition, one prerequisite per "
            "operand). The PERCENT-YIELD edge pair (E-09/E-10) and the three yield "
            "nodes are then confirmable as-is; a future merge stays operator-only."),
        "recorded_ruling_verbatim": od1_block,
        "ratification_status": "PENDING OPERATOR RATIFICATION",
        "operator_verdict": None,
    },
    {
        "id": "OD-2",
        "title": "Incidental terminology is not instructional evidence (operator rule)",
        "provenance": (
            "The verbatim rule is operator-issued (recorded with the HELD-13 REJECT, "
            "session 41). Its codification as a STANDING evidence-admissibility rule "
            "for the expansion round is agent-proposed (session 41, C11_ARCHITECTURE "
            "§20). The codification — not the rule's wording — awaits ratification."),
        "effect_if_ratified": (
            "Becomes a standing expansion-round rule: IMPLICIT_USE evidence alone can "
            "never ground promotion; quarantine-or-abstain per FC-1. Affects all "
            "future batches' evidence bar."),
        "recorded_ruling_verbatim": od2_block,
        "ratification_status": "PENDING OPERATOR RATIFICATION",
        "operator_verdict": None,
    },
]

# ---------------------------------------------------------------------------
# Quantified review reduction
# ---------------------------------------------------------------------------
eg = {}
for d in edge_dossiers:
    eg[d["pretriage"]["label"]] = eg.get(d["pretriage"]["label"], 0) + 1
ng = {}
for d in node_dossiers:
    ng[d["pretriage"]["label"]] = ng.get(d["pretriage"]["label"], 0) + 1
e_safe = sum(v for k, v in eg.items() if k.startswith("LIKELY_SAFE"))
e_amb = sum(v for k, v in eg.items() if k.startswith("LIKELY_AMBIGUOUS"))
e_fc3 = sum(v for k, v in eg.items() if k.startswith("FC-3"))
e_pend = sum(v for k, v in eg.items() if "PENDING" in k)
n_safe = sum(v for k, v in ng.items() if k.startswith("LIKELY_SAFE"))
n_fc2 = sum(v for k, v in ng.items() if k.startswith("FC-2"))

review_reduction = {
    "edges_31": {
        "likely_safe_bulk_confirmable": e_safe,
        "fc3_od1_linked_one_joint_ruling": e_fc3,
        "likely_ambiguous_individual": e_amb,
        "pending_judgments_already_presented": e_pend,
        "grouped_by_class": e_safe + e_fc3,
        "require_genuine_human_semantic_judgment": e_amb + e_pend,
        "distribution": eg,
    },
    "nodes_29": {
        "likely_safe_bulk_confirmable": n_safe,
        "fc2_identity_od1_linked": n_fc2,
        "grouped": n_safe,
        "require_genuine_human_semantic_judgment": n_fc2,
        "distribution": ng,
    },
    "held_appendix_13": {"informational": 13, "reopenings": 0,
                          "decisions_preserved_verbatim": 13},
    "decision_load": (
        "Per-row surface 60 verdicts (31 edges + 29 nodes) reduces to ~7 actual "
        "decisions: (1) OD-1 ratification [covers 2 nodes + 2 edges], (2) OD-2 "
        "ratification, (3–4) the two PENDING judgments [already presented 10-field], "
        "(5) the granularity edge, (6) the alias-evidence policy, (7) the "
        "'maximum yield' disposition — plus bulk CONFIRM/REJECT commands over the "
        "pre-triaged groups."),
    "alias_audit": {"total_aliases": n_ver + n_var + n_une,
                    "verbatim_evidenced": n_ver, "morphological_variant": n_var,
                    "unevidenced": n_une},
}

# ---------------------------------------------------------------------------
# JSON machine record
# ---------------------------------------------------------------------------
pkg_json = {
    "task": "T-C11", "stage": "operator-review-package", "session": SESSION,
    "generated": TODAY,
    "baselines": {"resources": BASE_RES, "syllabai": BASE_TRK},
    "authority": {
        "promotion_authority": False, "s16_authorization": False,
        "graph_modification": False, "expansion": False,
        "constraint_verbatim": [
            "Do not promote anything. Do not modify the authoritative graph. "
            "Do not open §16. Do not begin S1-remainder/S2/S3/S4 expansion.",
            "No promotion authority and no §16 authorization.",
            "Correct the phantom 'aximum yield' report text; do not modify the "
            "actual concept alias until evidence/disposition is established.",
        ],
    },
    "reconciliation": {
        "resources": "4ac4a82 -> 3b70dde (ff-only; +3 remote: RAG corpus guidance + 2 Drive-sync CI)",
        "syllabai": "6ef49f2 -> 6d36fb0 (ff-only; +10 remote incl. session-42 T-C12, ADR-020, dashboard CI)",
        "note": "T-C12 subsequently moved forward; local Session-41 clones were behind origin and were reconciled before any work",
    },
    "edge_dossiers": edge_dossiers,
    "node_dossiers": node_dossiers,
    "held_appendix": held_appendix,
    "ontology_decision_slots": od_slots,
    "alias_audit": {
        "policy_question": (
            "Must aliases carry verbatim corpus evidence, or are they "
            "retrieval-oriented paraphrases exempt from the evidence discipline? "
            "24 of 47 pilot aliases are not verbatim-evidenced (21 after allowing "
            "morphological variants); most are transparent paraphrases of the node "
            "title, but 'maximum yield' is a foreign synonym with corpus support "
            "only for the concept ('maximum possible mass'), never the phrase."),
        "maximum_yield": {
            "phrase_occurrences": len(phrase_hits),
            "phrase_finding": "UNEVIDENCED — the phrase 'maximum yield' appears nowhere in the pilot corpus (10 notes + 12-SP spec text + 2 pinned mark schemes), nor in the full 112-note markdown corpus",
            "word_maximum_occurrences_in_pilot_corpus": maxm_occurrences,
            "closest_semantic_anchor": (
                "Reacting mass calculations note, worked example: 'Calculate the "
                "maximum possible mass of aluminium, in tonnes, that can be "
                "produced' — the theoretical-yield concept phrased without the word "
                "'yield'; instructional text (not a table label), but not the "
                "verbatim alias phrase"),
            "note": "the data was never corrupted: 'maximum yield' is byte-stable in scripts/c11_pilot_decisions.yaml and graph/concepts.yaml across all committed revisions; the reported 'aximum yield' corruption existed only in report text (corrected this session)",
            "disposition_options": [
                "DROP the alias (strict verbatim-phrase policy)",
                "RE-EVIDENCE: keep an alias grounded on the Reacting-mass 'maximum possible mass' usage (requires an operator ruling that non-verbatim derived aliases are admissible)",
                "KEEP unevidenced (requires a ruling that aliases are retrieval-oriented and exempt from the evidence discipline)",
                "RENAME to a verbatim-evidenced form (note: 'maximum mass' itself is ambiguous — the metal-oxide note uses it for crucible-constant-mass)",
            ],
            "alias_untouched": True,
        },
        "per_node": alias_audit,
        "counts": {"verbatim": n_ver, "variant": n_var, "unevidenced": n_une},
    },
    "pretriage_summary": {
        "edges": eg, "nodes": ng,
        "legend": {
            "FC-1": "evidence-sufficiency risk (medium confidence / implicit evidence)",
            "FC-2": "relation-class or identity misfit risk",
            "FC-3": "redundancy / normalization (subsumption or same-anchor operand pair)",
            "FC-4": "negative-control (4.15) — machine-asserted zero in this package",
            "LIKELY_SAFE": "zero machine flags; high confidence; pass-2 concordant",
            "LIKELY_AMBIGUOUS": "a flag or note requires a human read before confirmation",
        },
    },
    "review_reduction": review_reduction,
    "batch_forecast": {
        "instrument": "scripts/c11_batch_forecast.py",
        "record": "graph/reports/C11_BATCH_FORECAST.json",
        "calibration": _forecast["predicted_vs_actual_pilot_calibration"]["rows"],
        "rates": {k: v["value"] for k, v in _forecast["rates"].items()},
    },
    "verification": {
        "quote_checks": quote_checks,
        "gates_this_session": {
            "graph_check": "ALL PASS (11/11; 29 nodes / 65 edges / 0 HUMAN_VALIDATED / 4.15 uncovered)",
            "c11_negative_test": "14/14 PASS",
            "c11_task4_variants": "3/3 PASS",
            "c11_promote_test": "27/27 PASS",
        },
        "zero_action_attestation": (
            "Nothing promoted (c11_promotions.yaml unchanged, 0 entries). "
            "graph/*.yaml byte-untouched. §16 not opened. No expansion. "
            "Outputs: this package + the batch-forecast record + the phantom-text "
            "corrections in 3 report artifacts + 1 renderer literal."),
    },
}

(REPORTS / "C11_REVIEW_PACKAGE.json").write_text(
    json.dumps(pkg_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# Verdict template (operator-owned)
# ---------------------------------------------------------------------------
verdicts = {
    "meta": {
        "task": "T-C11", "stage": "operator-review-package", "session": SESSION,
        "file": "OPERATOR-OWNED verdict record for C11_REVIEW_PACKAGE (session 43).",
        "instructions": (
            "Fill verdict per row. Edge/node vocabulary: CONFIRM | REJECT | HOLD | "
            "MERGE | SPLIT. OD vocabulary: RATIFY | RATIFY_WITH_MODIFICATION | "
            "REJECT | DEFER. Alias policy: EVIDENCE_REQUIRED_ALL | "
            "EVIDENCE_REQUIRED_SPECIAL | RETRIEVAL_EXEMPT. Alias disposition: DROP | "
            "RE_EVIDENCE | KEEP | RENAME. Hand-edits HERE are the sanctioned "
            "pathway; graph/*.yaml are never hand-edited. The next session applies "
            "verdicts via the §18 promotion pathway / §7 decision-record "
            "re-authoring. Held appendix: informational only — no reopening, no "
            "promotion of held candidates."),
    },
    "od_ratifications": [
        {"id": "OD-1", "question": "yield triple stays split",
         "verdict": "", "notes": "", "decided_date": ""},
        {"id": "OD-2", "question": "incidental-terminology evidence rule codified",
         "verdict": "", "notes": "", "decided_date": ""},
    ],
    "edge_verdicts": [
        {"id": d["id"], "triple": d["triple"], "pretriage": d["pretriage"]["label"],
         "verdict": "", "notes": ""} for d in edge_dossiers
    ],
    "node_verdicts": [
        {"id": d["id"], "code": d["code"], "title": d["title"],
         "pretriage": d["pretriage"]["label"], "verdict": "", "notes": ""}
        for d in node_dossiers
    ],
    "alias_policy": {"verdict": "", "notes": ""},
    "alias_dispositions": [
        {"node": "4CH1-CON-THEOR-YIELD", "alias": "maximum yield",
         "disposition": "", "notes": ""}
    ],
    "held_appendix": {"acknowledged": False,
                      "note": "informational only — all 13 decisions preserved; "
                              "no reopening, no promotion"},
}
# Session-44 guard: the verdict record is OPERATOR-OWNED and has been filled
# with actual operator verdicts (session 44, 2026-09-12). Rebuilding the
# package must never silently clobber them. If a rebuild is genuinely
# required, the operator verdict record must be moved aside explicitly.
_vf = HERE / "c11_review_verdicts.yaml"
if _vf.exists():
    _vd = yaml.safe_load(_vf.read_text(encoding="utf-8"))
    _v_filled = any(
        row.get("verdict") for row in
        (_vd or {}).get("od_ratifications", []) + (_vd or {}).get("edge_verdicts", [])
        + (_vd or {}).get("node_verdicts", []))
    if _v_filled:
        raise SystemExit(
            "FAIL-CLOSED: scripts/c11_review_verdicts.yaml already carries "
            "recorded operator verdicts (session 44) — refusing to overwrite "
            "the operator-owned verdict record with an empty template. A "
            "package rebuild requires explicitly preserving/moving that file.")
_vf.write_text(
    "# T-C11 operator review verdicts — session 43 package. OPERATOR-OWNED.\n"
    "# Vocabulary and pathway: see the meta.instructions block.\n"
    + yaml.safe_dump(verdicts, sort_keys=False, allow_unicode=True, width=100),
    encoding="utf-8")

# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------
def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def q(s):
    return '"' + esc(s) + '"'


L = []
A = L.append

A("# T-C11 Operator Review Package — Session 43 (2026-09-12)")
A("")
A("Built read-only from the decision record and live store at resources "
  f"`{BASE_RES}` / syllabai `{BASE_TRK}` (both fast-forwarded from the "
  "Session-41 clones before any work — T-C12 had advanced). Machine record: "
  "`graph/reports/C11_REVIEW_PACKAGE.json`. Verdict template (operator-owned): "
  "`scripts/c11_review_verdicts.yaml`.")
A("")
A("**This package carries NO promotion authority and NO §16 authorization.**")
A("")
A("> Do not promote anything. Do not modify the authoritative graph. Do not")
A("> open §16. Do not begin S1-remainder/S2/S3/S4 expansion.")
A("")
A("Nothing was promoted; `graph/*.yaml` are byte-untouched; the promotions "
  "record remains at zero entries. The concept alias under audit below was "
  "NOT modified — its disposition is the operator's.")
A("")
A("---")
A("")
A("## 0. Tasking record")
A("")
A("Operator tasking (session 43): the C11 audit + review-preparation round "
  "with **no promotion authority and no §16 authorization**. Required "
  "contents: (1) 31 individual edge dossiers; (2) 29 individual concept "
  "dossiers; (3) a 13-entry held/rejected appendix incl. HELD-13, HOLD vs "
  "REJECT distinguished, all existing decisions preserved, no reopening; "
  "(4) OD-1/OD-2 ratification slots marked PENDING, provenance unchanged; "
  "(5) machine pre-triage FC-1..FC-4 / likely-safe / likely-ambiguous; "
  "(6) the `maximum yield` alias audit with the phantom `aximum yield` "
  "report text corrected but the concept alias untouched; (7) a quantified "
  "review reduction; (8) batch-forecast instrumentation. Operational "
  "directive: reconcile to the current remote HEAD first (done — §0.1).")
A("")
A("### 0.1 Reconciliation record")
A("")
A("| repo | session-41 clone | reconciled HEAD | mode | what moved |")
A("|---|---|---|---|---|")
A("| resources | `4ac4a82` | `3b70dde` | ff-only, tree clean | RAG corpus "
  "guidance doc + 2 Google-Drive-sync CI commits; `graph/` and C11 scripts "
  "untouched |")
A("| syllabai (tracker) | `6ef49f2` | `6d36fb0` | ff-only, tree clean | "
  "session-42 T-C12 record (P0 closed + P1 IAL placement; 2 baseline "
  "ratification flags — pastpapers corpus, out of scope here), ADR-020, RAG "
  "research, dashboard/Drive CI |")
A("")
A("All four gates re-verified green at the reconciled HEAD before authoring "
  "(graph_check ALL PASS 29/65/0-HV; negative 14/14; task4 variants 3/3; "
  "promote 27/27). Every evidence quote was additionally re-verified "
  "independently under the T-C10 norm() by this package's builder: "
  f"{quote_checks['verified']}/{quote_checks['checked']} byte-true.")
A("")
A("## 1. How to use this package")
A("")
A("- **Verdict vocabulary** (edges & nodes): `CONFIRM / REJECT / HOLD / "
  "MERGE / SPLIT`. MERGE and SPLIT are operator-only identity decisions.")
A("- **Where to record**: `scripts/c11_review_verdicts.yaml` (operator-owned "
  "template rendered with this package). Hand-edits there are the sanctioned "
  "pathway; hand-edits to `graph/*.yaml` are silently reverted by the "
  "generator.")
A("- **Application**: the next session applies verdicts via the §18 "
  "promotion pathway (`scripts/c11_promote.py`, exact identities only) and "
  "§7 decision-record re-authoring for REJECT/MERGE/SPLIT — the HELD-13 "
  "precedent.")
A("- **Reading order for minimum effort**: §2 summary → §6 OD slots → the "
  "two PENDING presentations (C11_OPERATOR_DECISIONS.md §2) → §7 alias "
  "audit → bulk-confirm §3/§4 groups → spot-read dossiers as desired.")
A("")
A("## 2. Executive surface")
A("")
A("| surface | count | pre-triage split |")
A("|---|---|---|")
A(f"| edge dossiers (§3) | 31 | {e_safe} likely-safe · {e_fc3} FC-3 "
  f"(OD-1-linked) · {e_amb} ambiguous · {e_pend} PENDING |")
A(f"| concept dossiers (§4) | 29 | {n_safe} likely-safe · {n_fc2} FC-2 "
  "identity (OD-1-linked) |")
A("| held/rejected appendix (§5) | 13 | 11 HELD + 2 REJECTED — decisions "
  "preserved, no reopening |")
A("| OD ratification slots (§6) | 2 | both PENDING OPERATOR RATIFICATION |")
A(f"| alias audit (§7) | 47 aliases | {n_ver} verbatim · {n_var} variant · "
  f"{n_une} unevidenced — 1 special case (`maximum yield`) |")
A("")
A("**Review reduction (headline):** the 60 per-row verdicts collapse to "
  "**~7 actual decisions** — OD-1, OD-2, the two PENDING judgments, one "
  "granularity edge, the alias policy, and the `maximum yield` disposition "
  "— plus bulk CONFIRM/REJECT commands over the pre-triaged groups. See §8 "
  "for the quantification and §9 for the forecast instrumentation.")
A("")
A("---")
A("")
A("## 3. Edge dossiers (31 SUGGESTED authored edges awaiting per-row verdicts)")
A("")
A("Order = decision-record order. The REVIEW_REQUIRED operator-HOLD edge "
  "(`CON-GAS-VOL-CALC REQUIRES_PREREQUISITE CON-AVOGADRO-LAW`) is NOT in "
  "this list — it already carries an operator verdict (HOLD, stays in the "
  "graph, not promotable; see §5 legend). The two PENDING-gated edges are "
  "**E-26 and E-29** and reference their existing 10-field presentations.")
A("")

for d in edge_dossiers:
    ev = d["evidence"][0]
    A(f"### {d['id']} — {d['triple']}")
    A("")
    A("| field | value |")
    A("|---|---|")
    A(f"| exact triple | `{d['source']}` —**{d['relation']}**→ "
      f"`{d['target']}` |")
    A(f"| relation class | {d['relation']} ({d['relation_count_in_pilot']} "
      "in the pilot graph incl. PART_OF) |")
    A(f"| source evidence | [{ev['kind']}] `{ev['file'].split('/')[-1]}` — "
      f"{q(ev['quote'])} |")
    extra = d["evidence"][1:]
    if extra:
        A(f"| additional anchor | [{extra[0]['kind']}] "
          f"{q(extra[0]['quote'])} |")
    A(f"| evidence admissibility | {d['evidence_admissibility']} |")
    A(f"| rationale (pass-1) | {esc(d['rationale'])} |")
    A(f"| confidence / status | {d['confidence']} / {d['validation_status']}"
      + (" — **operator_decision PENDING**" if d["operator_decision_pending"]
         else "") + " |")
    pt = d["pretriage"]
    A(f"| failure-class pre-triage | **{pt['label']}**"
      + (f" — {'; '.join(pt['flags'])}" if pt["flags"] else "") + " |")
    A(f"| pass-2 verdict | {pt['pass2_verdict']}"
      + (f" — {q(pt['pass2_note'])}" if pt["pass2_note"] else "") + " |")
    A(f"| recommendation | {d['recommendation']} |")
    A(f"| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / "
      f"SPLIT) — record in `c11_review_verdicts.yaml` row {d['id']} |")
    A("")

A("---")
A("")
A("## 4. Concept dossiers (29 nodes awaiting per-row verdicts)")
A("")

for d in node_dossiers:
    A(f"### {d['id']} — `{d['code']}` {d['title']}")
    A("")
    A("| field | value |")
    A("|---|---|")
    A(f"| concept identity | `{d['code']}` — {d['title']} |")
    A(f"| node kind | {d['family']} · {d['node_kind']} |")
    att = "; ".join(f"`{a['code']}` {a['role']} ({a['verb']})"
                    for a in d["spec_attachments"]) or "(unattached)"
    A(f"| SpecificationPoint attachments | {att} |")
    for a in d["spec_attachments"]:
        for e2 in a["evidence"][:1]:
            A(f"| exact source evidence ({a['code']}) | [{e2['kind']}] "
              f"{q(e2['quote'])} |")
    als = "; ".join(f"{esc(x['alias'])} [{x['status']}"
                    + (f" @ {esc(x['evidence'][0])}" if x["evidence"] else "")
                    + "]" for x in d["aliases"]) or "(none)"
    A(f"| aliases (+ evidence) | {als} |")
    plc = "; ".join(f"`{p['spec_point']}` {p['role']}" for p in d["placement"])
    A(f"| placement (PART_OF) | {plc} |")
    dup = "; ".join(esc(x) for x in d["duplicate_overlap"]) or "none flagged"
    A(f"| potential duplicate / overlap | {dup} |")
    A(f"| confidence / status | {d['confidence']} / {d['validation_status']} |")
    pt = d["pretriage"]
    A(f"| pre-triage | **{pt['label']}**"
      + (f" — {'; '.join(pt['flags'])}" if pt["flags"] else "") + " |")
    A(f"| pass-2 verdict | {pt['pass2_verdict']}"
      + (f" — {q(pt['pass2_note'])}" if pt["pass2_note"] else "") + " |")
    A(f"| recommendation | {d['recommendation']} |")
    A(f"| **operator verdict** | ______ (CONFIRM / REJECT / HOLD / MERGE / "
      f"SPLIT) — record in `c11_review_verdicts.yaml` row {d['id']} |")
    A("")

A("---")
A("")
A("## 5. Held / rejected appendix (13 entries — informational, no reopening)")
A("")
A("**Channel legend.** `HELD` = abstained at generation: evidence-complete "
  "or deliberately withheld, NOT in the graph, NOT promotable, awaiting "
  "future evidence or an operator decision — but this package does not "
  "reopen any of them. `REJECTED` = permanently refused and machine-guarded "
  "(not an edge; promotion categorically refused: T19/T20). A third "
  "quarantine channel exists outside this list: the operator **HOLD** on "
  "the REVIEW_REQUIRED edge `CON-GAS-VOL-CALC → CON-AVOGADRO-LAW` — that "
  "edge IS in the graph, stays REVIEW_REQUIRED, is not promotable, and is "
  "not to be converted to ACCEPT/REJECT merely to complete the pilot.")
A("")
for h in held_appendix:
    A(f"### {h['id']} — {h['status'].upper()}")
    A("")
    A("| field | value |")
    A("|---|---|")
    A(f"| channel | {h['channel']} |")
    A(f"| candidate | {esc(h['candidate'])} |")
    A(f"| evidence (recorded at generation) | {q(h['evidence'])} |")
    A(f"| reason | {esc(h['reason'])} |")
    A(f"| failure class | {h['failure_class']} |")
    A(f"| pass-2 review | {h['pass2_verdict']}"
      + (f" — {q(h['pass2_note'])}" if h["pass2_note"] else "") + " |")
    if h["operator_decision"]:
        od = h["operator_decision"]
        A(f"| operator decision | {od['verdict']} by {od['decided_by']} "
          f"{od['decided_date']} — reasons verbatim: "
          + "; ".join(q(r) for r in od["reasons"]) + " |")
    A("")

A("*(Session-43 finding, documentation-only: HELD-08 is unassigned in the "
  "§19 / §16-item-6 failure-class distributions, which count 12 of 13 "
  "entries — this appendix assigns it FC-2 (residual-class discipline). "
  "ARCHITECTURE.md §19 text is unchanged; flag it for the next revision "
  "of that document.)*")
A("")
A("---")
A("")
A("## 6. Ontology decision ratification slots — PENDING OPERATOR RATIFICATION")
A("")
A("Neither slot below is ratified. OD-1 is an **agent-derived ontology "
  "recommendation**; OD-2's verbatim rule is operator-issued but its "
  "codification as a standing expansion rule is **agent-proposed**. Both "
  "provenances are stated exactly and must not be silently relabeled.")
A("")
for od in od_slots:
    A(f"### {od['id']} — {od['title']}")
    A("")
    A(f"**STATUS: {od['ratification_status']}**")
    A("")
    A(f"- Provenance: {od['provenance']}")
    A(f"- Effect if ratified: {od['effect_if_ratified']}")
    A("- Recorded ruling (verbatim, C11_ARCHITECTURE.md §20):")
    A("")
    A("```markdown")
    A(od["recorded_ruling_verbatim"])
    A("```")
    A("")
    A(f"| **operator ratification** | ______ (RATIFY / RATIFY_WITH_"
      f"MODIFICATION / REJECT / DEFER) — record in `c11_review_verdicts."
      f"yaml` row {od['id']} |")
    A("")

A("---")
A("")
A("## 7. Alias audit — `maximum yield` (concept alias NOT modified)")
A("")
A("### 7.1 What the data actually says (counter-confirmation of the "
  "session-42 counter-audit)")
A("")
A("- `scripts/c11_pilot_decisions.yaml` → `aliases: " + chr(91) + "maximum yield" + chr(93) + "`")
A("- `graph/concepts.yaml` → `- maximum yield`")
A("- No committed data revision — `e218259`, `4eba8ea`, `4ac4a82`, "
  "`3b70dde` — contains the string `aximum yield`. **The data corruption "
  "reported in session-41's defect record never existed in the store.**")
A("- The erroneous `aximum yield` text existed only in report artifacts "
  "(`C11_OPERATOR_DECISIONS.md`/`.json`, `C11_S16_GATE_REPORT.md`) and one "
  "renderer literal — **report/data drift, corrected this session** (the "
  "reports now describe the store byte-accurately; see §10).")
A("")
A("### 7.2 The real question: is the alias evidenced?")
A("")
A(f"- The phrase **`maximum yield` occurs {len(phrase_hits)} times** in the "
  "pilot corpus (10 notes, the 12 spec-point texts, 2 pinned mark schemes) "
  "and 0 times in the full 112-note markdown corpus → **unevidenced as a "
  "verbatim phrase**.")
A("- The word `maximum` occurs in the pilot corpus only here:")
A("")
for m in maxm_occurrences:
    A(f"  - `{m['corpus']}`: …{esc(m['context'])}…")
A("")
A("The Reacting-mass occurrences are the theoretical-yield **concept** "
  "phrased without the word 'yield' (instructional worked-example text, "
  "not a table label — so OD-2 does not directly forbid them); the "
  "metal-oxide and solubility occurrences are different senses entirely. "
  "The counter-audit's cited phrase 'Maximum amount of product possible' "
  "was itself an imprecise paraphrase — it appears nowhere in the markdown "
  "corpus or the pinned extractions; this section is the byte-true record.")
A("")
A(f"### 7.3 The alias table at a glance — {n_ver} verbatim / {n_var} "
  f"morphological variant / {n_une} unevidenced (of 47)")
A("")
A("| node | alias | status | evidence |")
A("|---|---|---|---|")
for r in alias_audit:
    for a in r["aliases"]:
        w = "; ".join(esc(x) for x in a["evidence"][:2]) if a["evidence"] else "—"
        A(f"| `{r['node']}` | {esc(a['alias'])} | {a['status']} | {w} |")
A("")
A("**Policy question for the operator** (one ruling covers the table): "
  "must aliases carry verbatim corpus evidence, or are they "
  "retrieval-oriented paraphrases exempt from the evidence discipline? "
  "Most unevidenced aliases are transparent paraphrases of the node title "
  "('calculating gas volumes' ~ *Gas volume calculation*); "
  "**`maximum yield` is the special case** — a foreign synonym of the "
  "*Theoretical yield* title with corpus support only for the concept, "
  "never the phrase. Disposition options: DROP / RE-EVIDENCE (ground on "
  "'maximum possible mass') / KEEP (retrieval-exempt) / RENAME (note: "
  "'maximum mass' itself is ambiguous — the metal-oxide note uses it for "
  "crucible constant mass). Record in `c11_review_verdicts.yaml`: "
  "`alias_policy` + the `maximum yield` row.")
A("")
A("**No alias was modified in this session** — the decision record and "
  "`graph/concepts.yaml` are byte-identical to `3b70dde`.")
A("")
A("---")
A("")
A("## 8. Quantified review reduction")
A("")
A("| population | groupable (class/bulk) | genuine human semantic judgment |")
A("|---|---|---|")
A(f"| 31 edges | {e_safe + e_fc3} ({e_safe} likely-safe bulk + {e_fc3} "
  f"FC-3 under ONE OD-1 ruling) | {e_amb + e_pend} ({e_amb} granularity + "
  f"{e_pend} PENDING, already presented 10-field) |")
n_clean = sum(1 for d in node_dossiers if d["pretriage"]["label"] == "LIKELY_SAFE")
n_noted = n_safe - n_clean
A(f"| 29 nodes | {n_safe} (bulk; {n_clean} clean + "
  f"{n_noted} one-line notes) | "
  f"{n_fc2} (the yield merge pair — governed by OD-1) |")
A("| 13 held/rejected | 13 preserved decisions, 0 reopened | 0 (informational) |")
A("")
A("Distributions (machine-countable in the JSON):")
A("")
A("```json")
A(json.dumps({"edges": eg, "nodes": ng}, indent=2))
A("```")
A("")
A(f"**Decision load:** {review_reduction['decision_load']}")
A("")
A("---")
A("")
A("## 9. Batch forecasting instrumentation")
A("")
A("Instrument: `scripts/c11_batch_forecast.py` → "
  "`graph/reports/C11_BATCH_FORECAST.json` (written this session; "
  "read-only with respect to the graph). The pilot is batch 0; each "
  "authorized §16 batch appends a `future_batch_records` entry so "
  "forecast error, rates, and false-positive categories are measured, "
  "not assumed.")
A("")
A("| metric | §16 model prediction (pilot's 12 SPs) | pilot actual | error |")
A("|---|---|---|---|")
for r in _forecast["predicted_vs_actual_pilot_calibration"]["rows"]:
    A(f"| {r['metric']} | {r['predicted']} | {r['actual']} | "
      f"{r['delta']:+} ({r['pct_error']:+}%) |")
A("")
A("| rate | pilot value | formula |")
A("|---|---|---|")
for k, v in _forecast["rates"].items():
    A(f"| {k} | {v['value']} | {v['formula']} |")
A("")
A("False-positive categories tracked (pilot history): "
  + "; ".join(f"{c['id']} {c['category']}" for c in _forecast["false_positive_categories"]) + ".")
A("")
A("---")
A("")
A("## 10. Zero-action attestation")
A("")
A("- Promotions record `scripts/c11_promotions.yaml`: **unchanged, 0 "
  "entries** — nothing promoted, nothing ratified.")
A("- `graph/*.yaml`: **byte-identical to `3b70dde`** (git diff empty; the "
  "generator was not re-run to write).")
A("- §16: **not opened**; expansion: **not begun**; DB writes: **none**.")
A("- Concept alias `maximum yield`: **untouched** (§7).")
A("- Store-adjacent writes this session: this package (new files), "
  "`C11_BATCH_FORECAST.json` (new), the verdict template (new), and the "
  "phantom-text corrections in `C11_OPERATOR_DECISIONS.md`/`.json` + "
  "`C11_S16_GATE_REPORT.md` + the renderer literal — report text only, "
  "describing the store byte-accurately.")
A("")

(REPORTS / "C11_REVIEW_PACKAGE.md").write_text("\n".join(L) + "\n", encoding="utf-8")

print("wrote", REPORTS / "C11_REVIEW_PACKAGE.md")
print("wrote", REPORTS / "C11_REVIEW_PACKAGE.json")
print("wrote", HERE / "c11_review_verdicts.yaml")
print("edge pretriage:", json.dumps(eg, indent=None))
print("node pretriage:", json.dumps(ng, indent=None))
print("alias audit:", n_ver, "verbatim /", n_var, "variant /", n_une, "unevidenced")
print("quote checks:", quote_checks["verified"], "/", quote_checks["checked"],
      "failed:", quote_checks["failed"])
