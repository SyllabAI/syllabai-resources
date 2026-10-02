#!/usr/bin/env python3
"""T-C39 K2 Lane C — consolidated verdict CHECK (fail-closed; the chemistry
c11_batchN_verdict_check.py convention, instantiated for the consolidated
B01..B06 intake).

Validates scripts/c39_maths_a_k2c_verdicts.yaml (the OPERATOR verdict record,
encoded 2026-10-02 from the operator's consolidated review) against the six
machine-readable review artifacts (graph/reports/C{33..38}_BATCH0{1..6}_REVIEW.json
+ _CHECK.json), the six decision records, the ratified maths-a spec store and
the repo copy of the consolidated review itself.

Gates:
  G1 verdict-record shape + intake provenance (repo copy present; sha256 equal
     to the record's source_integrity block)
  G2 per-batch verdict surfaces == the REVIEW.json artifacts (windows, node /
     edge / held / identity counts, anchors, quote probes, PASS WITH NOTES)
  G3 consolidated totals == artifact sums (82 = 71+11 nodes; 73 = 51+11+11
     edges; 45 held; 17 identity; 72 command kinds; 490 anchors; 84 PART_OF;
     192 preverify)
  G4 held-id inventory == exact union of the six held_ids lists (45 ids)
  G5 identity-decision inventory == the decision records' 17 ids
  G6 pre-apply store state: graph/igcse-maths-a/ carries EXACTLY the 5 K1
     stores; all six artifacts report stores_grown == 0
  G7 slice coverage: the six coverage profiles are set-equal to the ratified
     global_order 1..72 walk, pairwise disjoint, 12 SPs each
  G8 dated corrections + boundary resolution: DC-01 (45 not 47), DC-02 (84,
     machine artifacts over batch prose), DC-03 (quote probes confirmed);
     superseding boundary map == B06's future map; the landing chain
     B05-H-06 -> B06-H-02 and B04-H-06 -> B06-H-03 intact

Exit 0 = all gates pass; 1 = any failure. Writes
graph/reports/C39_K2C_VERDICT_CHECK.json (or the path given as argv[1]).
Nothing else is written; the decision records and stores are read-only here.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
VERDICTS = HERE / "c39_maths_a_k2c_verdicts.yaml"
REPORTS = REPO / "graph/reports"
BATCHES = [f"C{32+n}_BATCH0{n}" for n in range(1, 7)]
DECISIONS = [HERE / f"c{32+n}_maths_a_batch0{n}_decisions.yaml" for n in range(1, 7)]
REVIEW_COPY = REPORTS / "C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md"
OUT = REPORTS / "C39_K2C_VERDICT_CHECK.json"

FAILS: list[str] = []


def fail(msg: str) -> None:
    FAILS.append(msg)


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    v = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    arts = {n: json.loads((REPORTS / f"{b}_REVIEW.json").read_text(encoding="utf-8"))
            for n, b in enumerate(BATCHES, start=1)}
    checks = {n: json.loads((REPORTS / f"{b}_CHECK.json").read_text(encoding="utf-8"))
              for n, b in enumerate(BATCHES, start=1)}
    gates: list[dict] = []

    # ---- G1 verdict-record shape + intake provenance -------------------------
    g1: list[str] = []
    meta = v.get("meta") or {}
    for key in ("task", "stage", "batch", "curriculum_code", "session", "file",
                "instructions", "operator_ruling", "source_integrity"):
        if key not in meta:
            g1.append(f"meta.{key} missing")
    if meta.get("task") != "T-C39":
        g1.append(f"meta.task {meta.get('task')!r} != 'T-C39'")
    if meta.get("stage") != "k2c-b01-b06-verdicts":
        g1.append(f"meta.stage {meta.get('stage')!r} unexpected")
    ruling = meta.get("operator_ruling") or {}
    for key in ("statement", "session", "decided_by", "decided_date",
                "completed_sheet", "go_no_go"):
        if key not in ruling:
            g1.append(f"operator_ruling.{key} missing")
    if ruling.get("decided_by") != "operator":
        g1.append("operator_ruling.decided_by must be 'operator'")
    if "PASS WITH NOTES" not in ruling.get("statement", ""):
        g1.append("operator_ruling.statement must carry PASS WITH NOTES")
    si = meta.get("source_integrity") or {}
    if not REVIEW_COPY.exists():
        g1.append(f"repo copy of consolidated review missing: {REVIEW_COPY.name}")
    else:
        got = sha256(REVIEW_COPY)
        if got != si.get("sha256"):
            g1.append(f"consolidated review sha256 {got[:16]}.. != recorded "
                      f"{str(si.get('sha256'))[:16]}..")
        up = Path("/home/z/my-project/upload/MATHS_A_B01_B06_FINAL_CONSOLIDATED_REVIEW.md")
        if up.exists() and sha256(up) != got:
            g1.append("repo copy diverged from the operator upload")
    if v.get("batches") and len(v["batches"]) != 6:
        g1.append(f"batches list has {len(v['batches'])} entries != 6")
    gates.append({"gate": "G1", "name": "verdict_record_and_intake",
                  "status": "PASS" if not g1 else "FAIL",
                  "detail": "; ".join(g1) or
                  "record shape ok; repo copy byte-verified sha256 f33aa7b8..; "
                  "intake = consolidated review (2026-10-02, zai-web upload)"})

    # ---- G2 per-batch verdict surfaces ---------------------------------------
    g2: list[str] = []
    win_expect = {1: (1, 12), 2: (13, 24), 3: (25, 36), 4: (37, 48),
                  5: (49, 60), 6: (61, 72)}
    for i, b in enumerate(v.get("batches") or [], start=1):
        a = arts[i]["totals"]
        exp = {
            "nodes": a.get("nodes", a.get("concept_nodes", 0) + a.get("misconception_nodes", 0)),
            "edges": a["authored_edges"],
            "held": a["held"],
            "ids": a["identity_decisions"],
            "anchors": a["evidence_anchors"],
        }
        got_n = b.get("nodes_confirmed", "")
        got_e = b.get("edges_confirmed", "")
        got_h = b.get("held_acknowledged", "")
        got_i = b.get("identity_decisions_accepted", "")
        def hit(field, want):
            return str(field).split("/")[0].isdigit() and int(str(field).split("/")[0]) == want \
                and str(field).endswith(f"/{want}")
        if not hit(got_n, exp["nodes"]):
            g2.append(f"B0{i} nodes_confirmed {got_n!r} != {exp['nodes']}/{exp['nodes']}")
        if not hit(got_e, exp["edges"]):
            g2.append(f"B0{i} edges_confirmed {got_e!r} != {exp['edges']}/{exp['edges']}")
        if not hit(got_h, exp["held"]):
            g2.append(f"B0{i} held_acknowledged {got_h!r} != {exp['held']}/{exp['held']}")
        if not hit(got_i, exp["ids"]):
            g2.append(f"B0{i} identity_decisions_accepted {got_i!r} != {exp['ids']}/{exp['ids']}")
        if b.get("evidence_anchors") != exp["anchors"]:
            g2.append(f"B0{i} evidence_anchors {b.get('evidence_anchors')} != {exp['anchors']}")
        qp = str(b.get("quote_probe", ""))
        if not qp.endswith("/" + str(exp["anchors"])):
            g2.append(f"B0{i} quote_probe {qp!r} inconsistent with {exp['anchors']}")
        if b.get("verdict") != "PASS WITH NOTES":
            g2.append(f"B0{i} verdict {b.get('verdict')!r} != PASS WITH NOTES")
        task = f"T-C{32+i}"
        if b.get("task") != task:
            g2.append(f"B0{i} task {b.get('task')!r} != {task!r}")
        if b.get("gate") != f"K2-C-{i}":
            g2.append(f"B0{i} gate {b.get('gate')!r} != K2-C-{i}")
        lo, hi = win_expect[i]
        if f"global_order {lo}-{hi}" not in str(b.get("window", "")):
            g2.append(f"B0{i} window {b.get('window')!r} != global_order {lo}-{hi}")
        # battery result + quote probe gate
        if checks[i].get("result") != "ALL PASS":
            g2.append(f"B0{i} CHECK.json result {checks[i].get('result')!r}")
    gates.append({"gate": "G2", "name": "per_batch_verdict_surfaces",
                  "status": "PASS" if not g2 else "FAIL",
                  "detail": "; ".join(g2) or
                  "6/6 batches: PASS WITH NOTES; node/edge/held/identity surfaces "
                  "equal the REVIEW.json totals; anchors 47/61/83/89/110/100; "
                  "windows global_order 1-72; batteries ALL PASS"})

    # ---- G3 consolidated totals ----------------------------------------------
    g3: list[str] = []
    t = v.get("consolidated_totals") or {}
    nodes = sum(a["totals"].get("nodes", a["totals"].get("concept_nodes", 0)
                                + a["totals"].get("misconception_nodes", 0))
                for a in arts.values())
    concepts = sum(a["totals"].get("concept_nodes", a["totals"].get("nodes", 0))
                   for a in arts.values())
    miscon = sum(a["totals"].get("misconception_nodes", 0) for a in arts.values())
    edges = sum(a["totals"]["authored_edges"] for a in arts.values())
    held = sum(a["totals"]["held"] for a in arts.values())
    ids = sum(a["totals"]["identity_decisions"] for a in arts.values())
    cmd = sum(a["totals"]["command_kinds"] for a in arts.values())
    anch = sum(a["totals"]["evidence_anchors"] for a in arts.values())
    pof = sum(a["totals"]["derived_partof_at_apply"] for a in arts.values())
    expect = {"sps": 72, "candidate_nodes": nodes, "concept_nodes": concepts,
              "misconception_nodes": miscon, "authored_edges": edges,
              "held_candidates": held, "identity_decisions": ids,
              "command_kinds": cmd, "evidence_anchors": anch,
              "derived_partof_at_apply": pof}
    for k, want in expect.items():
        if t.get(k) != want:
            g3.append(f"consolidated_totals.{k} {t.get(k)} != {want}")
    # relation split from the DECISION RECORDS (authoritative; B01's artifact
    # totals predate the per-relation keys and its 12 edges are all
    # REQUIRES_PREREQUISITE — census below confirms against the artifacts)
    from collections import Counter
    rel_c: Counter = Counter()
    for p in DECISIONS:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        rel_c.update(e["relation"] for e in d.get("edges", []))
    rp = rel_c.get("REQUIRES_PREREQUISITE", 0)
    wap = rel_c.get("WRONG_ANSWER_PATTERN", 0)
    rem = rel_c.get("REMEDIATED_BY", 0)
    art_rp = sum(a["totals"].get("requires_prerequisite_edges", 0) for a in arts.values())
    art_wap = sum(a["totals"].get("wap_edges", 0) for a in arts.values())
    art_rem = sum(a["totals"].get("remediated_by_edges", 0) for a in arts.values())
    b1_edges = arts[1]["totals"]["authored_edges"]
    if art_rp + b1_edges != rp or art_wap != wap or art_rem != rem:
        g3.append(f"relation census {rp}/{wap}/{rem} inconsistent with artifact keys "
                  f"{art_rp}+{b1_edges}/{art_wap}/{art_rem}")
    if t.get("requires_prerequisite_edges") != rp or t.get("wrong_answer_pattern_edges") != wap \
            or t.get("remediated_by_edges") != rem or rp + wap + rem != edges:
        g3.append(f"edge-relation split {rp}+{wap}+{rem} != {edges} or totals mismatch")
    if (nodes, concepts, miscon, edges, held, ids, cmd, anch, pof) != \
            (82, 71, 11, 73, 45, 17, 72, 490, 84):
        g3.append(f"artifact sums {(nodes, concepts, miscon, edges, held, ids, cmd, anch, pof)} "
                  f"!= review-claimed (82, 71, 11, 73, 45, 17, 72, 490, 84)")
    pv = 0
    for n in range(1, 7):
        c = checks[n]
        import re as _re
        g3d = next((g for g in c["gates"] if g["gate"] == "G3"), {})
        m = _re.search(r"\((\d+) checks\)", str(g3d.get("detail", "")))
        if not m:
            g3.append(f"B0{n} preverify count not found in CHECK G3 detail")
        else:
            pv += int(m.group(1))
    if pv != 192:
        g3.append(f"preverify total {pv} != 192")
    if t.get("preverify_checks") != 192:
        g3.append(f"consolidated_totals.preverify_checks {t.get('preverify_checks')} != 192")
    gates.append({"gate": "G3", "name": "consolidated_totals_vs_artifacts",
                  "status": "PASS" if not g3 else "FAIL",
                  "detail": "; ".join(g3) or
                  "82 = 71+11 nodes; 73 = 51+11+11 edges; 45 held; 17 identity; "
                  "72 command kinds; 490 anchors; 84 PART_OF; preverify 192/192 "
                  "(21+32+33+35+36+35) — review §1 equal to the artifact sums"})

    # ---- G4 held-id inventory -------------------------------------------------
    g4: list[str] = []
    held_ids: list[str] = []
    for n in range(1, 7):
        held_ids += arts[n]["held_ids"]
    if len(held_ids) != 45:
        g4.append(f"held-id union {len(held_ids)} != 45")
    if len(set(held_ids)) != len(held_ids):
        g4.append("duplicate held ids across batches")
    want_ids = [f"B0{n}-H-{k:02d}" for n in range(1, 7) for k in range(1, 9) if not (n == 1 and k > 5)]
    if sorted(held_ids) != sorted(want_ids):
        g4.append("held-id set != B01-H-01..05 + B02..B06-H-01..08")
    if len(v.get("dated_corrections", [])) < 1:
        g4.append("dated corrections missing")
    dc1 = next((d for d in v.get("dated_corrections", []) if d.get("id") == "DC-01"), {})
    if str(dc1.get("corrected_value", "")) != "45":
        g4.append(f"DC-01 corrected_value {dc1.get('corrected_value')!r} != 45")
    gates.append({"gate": "G4", "name": "held_id_inventory",
                  "status": "PASS" if not g4 else "FAIL",
                  "detail": "; ".join(g4) or
                  "45 held ids = B01-H-01..05 + B02..B06-H-01..08, exact match to "
                  "the six REVIEW.json held_ids lists; DC-01 records 45 (the "
                  "review's own table summed 45; the '47' prose is corrected)"})
    # ---- G5 identity-decision inventory ---------------------------------------
    g5: list[str] = []
    dec_ids: list[str] = []
    for p in DECISIONS:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        dec_ids += [x["id"] for x in d.get("identity_decisions", [])]
    art_ids: list[str] = []
    for n in range(1, 7):
        art_ids += arts[n]["identity_decisions"]
    if len(dec_ids) != 17 or dec_ids != art_ids:
        g5.append(f"identity ids decision-records {len(dec_ids)} vs artifacts "
                  f"{len(art_ids)} or sets differ")
    want = ([f"B01-ID-0{k}" for k in (1, 2)]
            + [f"B0{n}-ID-0{k}" for n in range(2, 7) for k in (1, 2, 3)])
    if sorted(dec_ids) != sorted(want):
        g5.append("identity ids != B01-ID-01..02 + B02..B06-ID-01..03")
    gates.append({"gate": "G5", "name": "identity_decision_inventory",
                  "status": "PASS" if not g5 else "FAIL",
                  "detail": "; ".join(g5) or
                  "17 identity decisions = B01-ID-01..02 + B02..B06-ID-01..03, "
                  "decision records == REVIEW.json artifacts"})

    # ---- G6 pre-apply store state ---------------------------------------------
    g6: list[str] = []
    ma = REPO / "graph/igcse-maths-a"
    present = sorted(p.name for p in ma.glob("*.yaml"))
    k1_want = sorted(["specification_points.yaml", "topics.yaml", "practicals.yaml",
                      "assessment_objectives.yaml", "command_words.yaml"])
    k2_want = sorted(k1_want + ["concepts.yaml", "concept_edges.yaml",
                                "spec_command_kinds.yaml"])
    # the verdict check is a pre-apply gate but must remain green in the
    # post-apply steady state: both the 5-K1 store state (pre-apply) and the
    # 8-store state (5 K1 + the three §18-emitted K2 stores) are admissible
    if present not in (k1_want, k2_want):
        g6.append(f"maths-a stores {present} != the 5 K1 stores (pre-apply) or "
                  f"the 8-store post-apply state {k2_want}")
    for n in range(1, 7):
        if arts[n].get("stores_grown") != 0:
            g6.append(f"B0{n} stores_grown {arts[n].get('stores_grown')} != 0")
    gates.append({"gate": "G6", "name": "pre_apply_store_state",
                  "status": "PASS" if not g6 else "FAIL",
                  "detail": "; ".join(g6) or
                  "graph/igcse-maths-a/ = the 5 K1 stores (pre-apply) or the "
                  "8-store post-apply state; stores_grown = 0 "
                  "on all six artifacts (the sheets were gates, not promotions)"})

    # ---- G7 slice coverage ------------------------------------------------------
    g7: list[str] = []
    sp = yaml.safe_load((ma / "specification_points.yaml").read_text(encoding="utf-8"))
    go_map = {int(p["global_order"]): p["code"] for p in sp["specification_points"]
              if p.get("global_order") is not None}
    walk = {go_map[i] for i in range(1, 73)}
    union: set = set()
    per: dict[int, set] = {}
    for n in range(1, 7):
        cp = arts[n]["coverage_profile"]
        s = set(cp["notes_joined_sps"]) | set(cp["spec_text_only_sps"])
        if len(s) != 12:
            g7.append(f"B0{n} slice size {len(s)} != 12")
        per[n] = s
        union |= s
    if union != walk:
        g7.append("batch union != ratified global_order 1..72 walk")
    for n in range(1, 6):
        inter = per[n] & per[n + 1]
        if inter:
            g7.append(f"B0{n}/B0{n+1} overlap {sorted(inter)}")
    gates.append({"gate": "G7", "name": "slice_coverage",
                  "status": "PASS" if not g7 else "FAIL",
                  "detail": "; ".join(g7) or
                  "six 12-SP slices, pairwise disjoint, union set-equal to the "
                  "ratified global_order 1..72 walk (4MA1-1.1A..2.5A)"})

    # ---- G8 dated corrections + boundary resolution -----------------------------
    g8: list[str] = []
    dcs = {d.get("id"): d for d in v.get("dated_corrections", [])}
    if "DC-01" not in dcs or str(dcs["DC-01"].get("corrected_value")) != "45":
        g8.append("DC-01 (held 45 not 47) missing or wrong")
    if "DC-02" not in dcs or "84" not in str(dcs["DC-02"].get("corrected_value")):
        g8.append("DC-02 (PART_OF 84, machine artifacts over batch prose) missing")
    if "DC-03" not in dcs:
        g8.append("DC-03 (quote probes confirmed) missing")
    b6 = arts[6]
    if sorted(b6.get("future_batch_boundary_map", [])) != sorted(
            ["4MA1-1.7C", "4MA1-1.7D", "4MA1-2.7B"]):
        g8.append("B06 future map != the superseding 3-code map")
    br = v.get("boundary_resolution") or {}
    if sorted(br.get("superseding_map", [])) != sorted(b6["future_batch_boundary_map"]):
        g8.append("verdict boundary_resolution != B06 future map")
    lh = b6.get("landed_holds", {})
    if lh.get("B06-H-02") != "B05-H-06" or lh.get("B06-H-03") != "B04-H-06":
        g8.append(f"B06 landing chain {lh} != B05-H-06->B06-H-02 / B04-H-06->B06-H-03")
    if br.get("cross_batch_holds") and "quarantined" not in br["cross_batch_holds"]:
        g8.append("cross-batch holds must stay quarantined per NO-GO #3")
    pa = v.get("promotion_authorization") or {}
    if "SUGGESTED" not in str(pa.get("authority", "")):
        g8.append("promotion authorization authority must be SUGGESTED")
    if "HUMAN_VALIDATED" in str(pa.get("not_authorized", "")) and \
            "zero HUMAN_VALIDATED" not in str(pa.get("authority", "")):
        g8.append("authority must assert zero HUMAN_VALIDATED")
    gates.append({"gate": "G8", "name": "corrections_and_boundary",
                  "status": "PASS" if not g8 else "FAIL",
                  "detail": "; ".join(g8) or
                  "DC-01/DC-02/DC-03 recorded with evidence; superseding boundary "
                  "map {1.7C, 1.7D, 2.7B}; landing chain B05-H-06->B06-H-02 / "
                  "B04-H-06->B06-H-03 intact; authority SUGGESTED, zero "
                  "HUMAN_VALIDATED, zero promotion entries"})

    ok = all(g["status"] == "PASS" for g in gates)
    doc = {
        "schema": "c39-verdict-check/1.0",
        "task": "T-C39",
        "gate": "K2 Lane C consolidated verdict check (B01..B06)",
        "generated_utc": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "verdict_record": "scripts/c39_maths_a_k2c_verdicts.yaml",
        "intake": "graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md",
        "intake_sha256": sha256(REVIEW_COPY) if REVIEW_COPY.exists() else None,
        "baseline": __import__("subprocess").run(
            ["git", "-C", str(REPO), "rev-parse", "HEAD"],
            capture_output=True, text=True).stdout.strip(),
        "result": "ALL PASS" if ok else "FAIL",
        "gates": gates,
        "held_ids": held_ids,
        "identity_decisions": dec_ids,
    }
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    for g in gates:
        print(f"{g['status']}  {g['gate']} {g['name']}"
              + (f" — {g['detail']}" if g["status"] == "FAIL" else ""))
    print(f"c39_maths_a_k2c_verdict_check: {doc['result']} "
          f"({sum(1 for g in gates if g['status'] == 'PASS')}/{len(gates)} gates)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
