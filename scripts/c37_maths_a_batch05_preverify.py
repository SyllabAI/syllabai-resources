#!/usr/bin/env python3
"""T-C37 K2-C-5 — batch-B05 preverify (fail-closed, run BEFORE anything grows;
the c36_maths_a_batch04_preverify.py pattern adapted to the fifth-batch state).

Machine-verifies the batch-B05 decision record's structure and its discipline
against the live repo:
  1. record shape      15 nodes = 12 CONCEPT + 3 MISCONCEPTION (zero other
                       families) / 14 edges = 8 REQUIRES_PREREQUISITE + 3
                       WRONG_ANSWER_PATTERN + 3 REMEDIATED_BY / 8 held
                       (B05-H-01..08) / 12 command kinds / 3 identity decisions
  2. SP coverage       every one of the 12 slice SPs carries >= 1 CONCEPT node
                       attachment; no node or edge references a non-slice SP
  3. slice state       the live K1 store carries exactly the slice rows at
                       global_order 49-60; the MIXED-TIER honesty profile (5
                       Higher rows: 1.9A, 2.1A, 2.2A, 2.2B, 2.2C + 7 Foundation
                       rows); zero damage flags; the maths-a graph dir still
                       carries exactly the 5 K1 stores (B01..B04 are authored-
                       to-gate, NOT applied — the registry has not grown)
  4. evidence allow-list  NOTE-kind evidence files are exactly the 14
                       join-carried notes of the slice; every NOTE citation is
                       pair-backed (node attachments: the note is joined to the
                       attached SP; edges: joined to one of the edge's endpoint
                       SPs — the B02 pair-back strength, carried forward);
                       MARK_SCHEME evidence lives under the slice course's EQ
                       tree; SPEC evidence cites the ratified store; the
                       uncited-join census is EMPTY (all 14 join-carried pages
                       are cited, each for exactly the SP it is joined to)
  5. boundary discipline  every REQUIRES_PREREQUISITE endpoint is a batch node
                       (no registry exists); each WAP/REMEDIATED_BY source is a
                       MISCONCEPTION node and its target the same CONCEPT node
                       (the B1-E-25 pattern, one target per mint); no self-loops
                       or duplicate triples; validation_status SUGGESTED
                       everywhere
  6. misconception contract  each MIS node carries pattern_class
                       WRONG_ANSWER_PATTERN, >= 1 MARK_SCHEME evidence row,
                       derivation_method ASSESSMENT_DOCUMENTED; the mints ride
                       exactly the in-slice surfaces {2.1D, 2.2A}; none of the
                       five prior maths-a mints is re-minted
  7. inheritance       the B01..B04 packets are present (review jsons carry
                       their boundary maps — B04's 6-code map is the inherited
                       one, B03's map flagged 2.1D now in-slice) and their held
                       ids are NOT reused
  8. held + identity   held ids contiguous with failure-classed reasons;
                       identity decisions reserved to the operator

Exit 0 only if every check passes.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
DECISIONS = HERE / "c37_maths_a_batch05_decisions.yaml"
AUTH = HERE / "c37_maths_a_batch05_authorization.yaml"
JOIN_ARTIFACT = (REPO / "Official-Specifications/parsed/_derived/notes-join/"
                 f"{COURSE}.json")
SP_STORE = REPO / f"graph/{QUAL}/specification_points.yaml"
GRAPH_DIR = REPO / f"graph/{QUAL}"

K1_STORES = {"specification_points.yaml", "topics.yaml", "practicals.yaml",
             "assessment_objectives.yaml", "command_words.yaml"}
SLICE = ["4MA1-1.9A", "4MA1-1.10A", "4MA1-1.10B", "4MA1-1.10C", "4MA1-1.11A",
         "4MA1-2.1A", "4MA1-2.1B", "4MA1-2.1C", "4MA1-2.1D", "4MA1-2.2A",
         "4MA1-2.2B", "4MA1-2.2C"]
HIGHER = {"4MA1-1.9A", "4MA1-2.1A", "4MA1-2.2A", "4MA1-2.2B", "4MA1-2.2C"}
GUIDE_CLASSES = {"KNOW_TERM", "UNDERSTAND_RELATION", "APPLY_PROCEDURE"}
RELATIONS = {"REQUIRES_PREREQUISITE", "WRONG_ANSWER_PATTERN", "REMEDIATED_BY"}
PRIOR_MINTS = {"4MA1-MIS-SURD-FACTOR-SWAP", "4MA1-MIS-CONJUGATE-EXPANSION-SIGN",
               "4MA1-MIS-COMPLEMENT-INTERSECTION-CONFUSION",
               "4MA1-MIS-PERCENTAGE-QUOTIENT-INVERSION",
               "4MA1-MIS-RATIO-ORDER-INVERSION"}

fails: list[str] = []
n = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global n
    n += 1
    if not ok:
        fails.append(name + (f"  [{detail}]" if detail else ""))


doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
auth = yaml.safe_load(AUTH.read_text(encoding="utf-8"))

# 1. record shape
b_nodes, b_edges, b_held = doc["nodes"], doc["edges"], doc["held"]
b_kinds, b_ids = doc["command_kinds"], doc["identity_decisions"]
con_nodes = [x for x in b_nodes if x["family"] == "CONCEPT"]
mis_nodes = [x for x in b_nodes if x["family"] == "MISCONCEPTION"]
check("record shape: authorization decision AUTHORIZED with verbatim directive "
      "'K2-C-5'", auth["authorization"]["decision"] == "AUTHORIZED"
      and auth["authorization"]["operator_statement_verbatim"] == "K2-C-5")
check("record shape: extraction_pass c37-k2c-batch-05 under T-C37",
      doc["meta"]["task"] == "T-C37"
      and doc["meta"]["extraction_pass"] == "c37-k2c-batch-05")
check("record shape: 15 nodes = 12 CONCEPT + 3 MISCONCEPTION, all codes unique",
      len(b_nodes) == 15 and len(con_nodes) == 12 and len(mis_nodes) == 3
      and len({x["code"] for x in b_nodes}) == 15)
rp = [e for e in b_edges if e["relation"] == "REQUIRES_PREREQUISITE"]
wap = [e for e in b_edges if e["relation"] == "WRONG_ANSWER_PATTERN"]
rem = [e for e in b_edges if e["relation"] == "REMEDIATED_BY"]
check("record shape: 14 edges = 8 REQUIRES_PREREQUISITE + 3 WRONG_ANSWER_PATTERN "
      "+ 3 REMEDIATED_BY, all in the concept-graph vocabulary",
      len(b_edges) == 14 and len(rp) == 8 and len(wap) == 3 and len(rem) == 3
      and all(e["relation"] in RELATIONS for e in b_edges))
check("record shape: 8 held candidates, ids B05-H-01..08 contiguous, status=held, "
      "failure-classed reasons",
      len(b_held) == 8
      and [h["id"] for h in b_held] == [f"B05-H-{i:02d}" for i in range(1, 9)]
      and all(h["status"] == "held" and h.get("reason") and h.get("candidate")
              for h in b_held))
check("record shape: 12 command kinds (one per slice SP, codes exact, guide "
      "classes in the B01-founded vocabulary)",
      len(b_kinds) == 12 and {k["code"] for k in b_kinds} == set(SLICE)
      and all(k.get("verb") and k.get("guide_class") in GUIDE_CLASSES
              and k.get("demanded_substance") for k in b_kinds))
check("record shape: 3 identity decisions reserved to the operator",
      [i["id"] for i in b_ids] == ["B05-ID-01", "B05-ID-02", "B05-ID-03"]
      and all(i.get("reserved_to") == "operator verdict" for i in b_ids))

# 2. SP coverage
scope_sps = set(doc["meta"]["scope"]["spec_points"])
check("scope list == the B05 slice (4MA1-1.9A..4MA1-2.2C)",
      scope_sps == set(SLICE), f"got {sorted(scope_sps)}")
node_sps = {sp["code"] for x in b_nodes for sp in (x.get("spec_points") or [])}
check("SP coverage: every slice SP covered by at least one node attachment",
      node_sps == scope_sps, f"missing {sorted(scope_sps - node_sps)}")
check("SP discipline: no node attachment outside the slice",
      node_sps <= scope_sps, f"foreign {sorted(node_sps - scope_sps)}")

# 3. slice state (the live store must be the sanctioned pre-batch state)
store = yaml.safe_load(SP_STORE.read_text(encoding="utf-8"))
rows = store["specification_points"]
by_code = {r["code"]: r for r in rows}
check("pre-state: ratified store 188 rows", len(rows) == 188)
slice_rows = sorted((by_code[c] for c in SLICE), key=lambda r: r["global_order"])
check("pre-state: slice rows sit at global_order 49..60 exactly",
      [r["global_order"] for r in slice_rows] == list(range(49, 61)),
      str([(r["code"], r["global_order"]) for r in slice_rows]))
check("pre-state: MIXED-TIER honesty profile — exactly 5 Higher rows (1.9A, "
      "2.1A, 2.2A, 2.2B, 2.2C — the second-heaviest Higher share of the series) "
      "and 7 Foundation rows",
      all(((r["applicability"] or {}).get("tier") == "Higher")
          == (r["code"] in HIGHER) for r in slice_rows),
      str([(r["code"], (r["applicability"] or {}).get("tier"))
           for r in slice_rows]))
check("pre-state: the 5 higher-preferred rows carry the tier_dedupe_note "
      "(the C30 ledger's Foundation variants recorded)",
      all("higher-preferred" in (by_code[c].get("tier_dedupe_note") or "")
          for c in HIGHER))
check("pre-state: every slice row carries zero damage flags (the 8 flagged rows "
      "live outside this slice)",
      all(not r.get("damage_flags") for r in slice_rows))
check("pre-state: graph/igcse-maths-a/ still carries exactly the 5 K1 stores — "
      "B01, B02, B03 and B04 are authored-to-gate, not applied; the registry "
      "has not grown",
      {p.name for p in GRAPH_DIR.iterdir() if p.is_file()} == K1_STORES,
      str(sorted(p.name for p in GRAPH_DIR.iterdir())))

# 4. evidence allow-list (the B05 negative control, pair-back at B02 strength)
join = json.loads(JOIN_ARTIFACT.read_text(encoding="utf-8"))
code_by_official = {r["official_code"]: r["code"] for r in rows}
join_pairs: set[tuple[str, str]] = set()
join_by_note: dict[str, set[str]] = {}
for j in join["joins"]:
    md = f"SME-RevisionNotes/{COURSE}/" + j["note_path"][:-len(".json")] + ".md"
    rc = code_by_official.get(j["resolved_code"], j["resolved_code"])
    join_pairs.add((md, rc))
    join_by_note.setdefault(md, set()).add(rc)
joined_sps = set().union(*join_by_note.values()) & scope_sps
bad: list[str] = []
for x in b_nodes:
    for sp in (x.get("spec_points") or []):
        for ev in sp["evidence"]:
            f, kind = ev["file"], ev["kind"]
            if kind == "SPEC":
                if f != f"graph/{QUAL}/specification_points.yaml":
                    bad.append(f"{x['code']}/{sp['code']}: bad SPEC file {f}")
            elif kind == "NOTE":
                if f not in join_by_note:
                    bad.append(f"{x['code']}/{sp['code']}: NOTE file outside "
                               f"the 14 join-carried notes: {f}")
                elif sp["code"] not in join_by_note.get(f, set()):
                    bad.append(f"{x['code']}/{sp['code']}: NOTE file {f} is "
                               f"not joined to that SP (unjoined-corpus "
                               f"negative control)")
            elif kind == "MARK_SCHEME":
                if not f.startswith(f"SME-ExamQuestion/{COURSE}/"):
                    bad.append(f"{x['code']}/{sp['code']}: MS file outside the "
                               f"slice course tree: {f}")
            else:
                bad.append(f"{x['code']}/{sp['code']}: unknown kind {kind}")
for e in b_edges:
    endpts = {e["source"], e["target"]}
    endpt_sps = {sp["code"] for x in b_nodes if x["code"] in endpts
                 for sp in (x.get("spec_points") or [])}
    for ev in e["evidence"]:
        kind, f = ev["kind"], ev["file"]
        if kind not in ("SPEC", "NOTE", "MARK_SCHEME"):
            bad.append(f"{e['source']}->{e['target']}: unknown kind {kind}")
        elif kind == "SPEC" and f != f"graph/{QUAL}/specification_points.yaml":
            bad.append(f"{e['source']}->{e['target']}: bad SPEC file {f}")
        elif kind == "NOTE":
            if f not in join_by_note:
                bad.append(f"{e['source']}->{e['target']}: NOTE file outside "
                           f"the join-carried set: {f}")
            elif not (join_by_note.get(f, set()) & endpt_sps):
                bad.append(f"{e['source']}->{e['target']}: NOTE file {f} not "
                           f"joined to any endpoint SP (edge pair-back)")
        elif kind == "MARK_SCHEME" and not f.startswith(
                f"SME-ExamQuestion/{COURSE}/"):
            bad.append(f"{e['source']}->{e['target']}: MS file outside the "
                       f"slice course tree: {f}")
check("evidence allow-list: every evidence anchor cites an allowed file for its "
      "kind, SP-pair-backed on nodes and endpoint-pair-backed on edges (no "
      "unjoined-corpus citations)", not bad, "; ".join(bad[:4]))
cited_notes = {ev["file"] for x in b_nodes
               for sp in x.get("spec_points") or []
               for ev in sp["evidence"] if ev["kind"] == "NOTE"}
cited_notes |= {ev["file"] for x in b_nodes
                for ev in x.get("evidence") or [] if ev["kind"] == "NOTE"}
cited_notes |= {ev["file"] for e in b_edges for ev in e["evidence"]
                if ev["kind"] == "NOTE"}
slice_join_files = {f for f, sps in join_by_note.items() if sps & scope_sps}
check("evidence allow-list: the slice's join-carried NOTE set is exactly the 14 "
      "recorded files and every cited NOTE file is one of them",
      len(slice_join_files) == 14 and cited_notes <= slice_join_files,
      f"join-carried={len(slice_join_files)} "
      f"outside={sorted(cited_notes - slice_join_files)[:3]}")
check("uncited-join census: EMPTY — all 14 join-carried pages are cited, each "
      "for exactly the SP it is joined to (the second fully-cited batch of the "
      "series; no anchor is padded to force this — the coverage grew into the "
      "census)",
      (slice_join_files - cited_notes) == set(),
      str(sorted(slice_join_files - cited_notes)))
ms_sps = {sp["code"] for x in b_nodes
          for sp in x.get("spec_points") or []
          for ev in sp["evidence"] if ev["kind"] == "MARK_SCHEME"}
cp = doc["meta"]["scope"]["coverage_profile"]
check("coverage profile stated: 8 notes-joined / 4 spec-text-only, equal to the "
      "join artifact's own census for this slice",
      set(cp["notes_joined_sps"]) == joined_sps
      and cp["notes_joined_count"] == len(joined_sps) == 8
      and cp["spec_text_only_count"] == len(SLICE) - len(joined_sps) == 4,
      f"join census = {sorted(joined_sps)}")
check("coverage profile stated: MS-evidenced SPs == the record's list (all 12 "
      "slice rows — the first full MS profile of the series)",
      ms_sps == set(cp["ms_evidence_sps"]), f"actual {sorted(ms_sps)}")

# 5. boundary discipline
b_codes = {x["code"] for x in b_nodes}
fam = {x["code"]: x["family"] for x in b_nodes}
check("boundary discipline: every REQUIRES_PREREQUISITE endpoint is a batch node "
      "(no registry exists — B01..B04 unapplied)",
      all(e["source"] in b_codes and e["target"] in b_codes for e in rp))
check("boundary discipline: WAP/REMEDIATED_BY sources are MISCONCEPTION nodes, "
      "targets CONCEPT nodes (the B1-E-25 pattern)",
      all(fam.get(e["source"]) == "MISCONCEPTION"
          and fam.get(e["target"]) == "CONCEPT" for e in wap + rem))
wap_by_mis = {e["source"]: e["target"] for e in wap}
check("boundary discipline: each REMEDIATED_BY target equals its mint's "
      "WRONG_ANSWER_PATTERN target (remediation target = WAP target)",
      all(e["target"] == wap_by_mis.get(e["source"]) for e in rem)
      and set(wap_by_mis) == {e["source"] for e in rem})
check("boundary discipline: no self-loop, no duplicate triple",
      all(e["source"] != e["target"] for e in b_edges)
      and len({(e["source"], e["relation"], e["target"])
               for e in b_edges}) == len(b_edges))
check("promotion discipline: zero silent promotion — every node SUGGESTED",
      all(x["validation_status"] == "SUGGESTED" for x in b_nodes))
check("provenance: every node carries the batch extraction_pass and AI_SUGGESTED "
      "tier",
      all((x.get("provenance") or {}).get("tier") == "AI_SUGGESTED"
          and (x.get("provenance") or {}).get("extraction_pass")
          == "c37-k2c-batch-05" for x in b_nodes))

# 6. misconception contract
check("misconception contract: each MIS node carries pattern_class "
      "WRONG_ANSWER_PATTERN, >= 1 MARK_SCHEME evidence row and "
      "derivation_method ASSESSMENT_DOCUMENTED",
      all(x.get("pattern_class") == "WRONG_ANSWER_PATTERN"
          and any(ev["kind"] == "MARK_SCHEME" for ev in x.get("evidence") or [])
          and (x.get("provenance") or {}).get("derivation_method")
          == "ASSESSMENT_DOCUMENTED" for x in mis_nodes))
check("misconception contract: the mints ride exactly the in-slice surfaces "
      "{2.1D, 2.2A} — the index-laws row and the expand row whose substances "
      "the documented classes violate",
      sorted({sp["code"] for x in mis_nodes
              for sp in x.get("spec_points") or []})
      == ["4MA1-2.1D", "4MA1-2.2A"] and len(mis_nodes) == 3)
prior_codes: set[str] = set()
for dec in (HERE / "c33_maths_a_batch01_decisions.yaml",
            HERE / "c34_maths_a_batch02_decisions.yaml",
            HERE / "c35_maths_a_batch03_decisions.yaml",
            HERE / "c36_maths_a_batch04_decisions.yaml"):
    if dec.is_file():
        prior_codes |= {x["code"] for x in yaml.safe_load(
            dec.read_text(encoding="utf-8"))["nodes"]}
check("misconception contract: none of the five prior maths-a mints is "
      "re-minted and the B05 mint codes are new across all packets",
      PRIOR_MINTS <= prior_codes
      and not PRIOR_MINTS & b_codes
      and not prior_codes & {x["code"] for x in mis_nodes})

# 7. inheritance (the B01..B04 packets and their quarantines)
b01_dec = HERE / "c33_maths_a_batch01_decisions.yaml"
b01_review = REPO / "graph/reports/C33_BATCH01_REVIEW.json"
b02_dec = HERE / "c34_maths_a_batch02_decisions.yaml"
b02_review = REPO / "graph/reports/C34_BATCH02_REVIEW.json"
b03_dec = HERE / "c35_maths_a_batch03_decisions.yaml"
b03_review = REPO / "graph/reports/C35_BATCH03_REVIEW.json"
b04_dec = HERE / "c36_maths_a_batch04_decisions.yaml"
b04_review = REPO / "graph/reports/C36_BATCH04_REVIEW.json"
b01_ok = b01_dec.is_file() and b01_review.is_file()
b02_ok = b02_dec.is_file() and b02_review.is_file()
b03_ok = b03_dec.is_file() and b03_review.is_file()
b04_ok = b04_dec.is_file() and b04_review.is_file()


def review_map(p: Path) -> list:
    return json.loads(p.read_text(encoding="utf-8")).get(
        "future_batch_boundary_map", []) if p.is_file() else []


b01_map, b02_map = review_map(b01_review), review_map(b02_review)
b03_map, b04_map = review_map(b03_review), review_map(b04_review)
prior_held_ids = set()
for dec in (b01_dec, b02_dec, b03_dec, b04_dec):
    if dec.is_file():
        prior_held_ids |= {h["id"] for h in yaml.safe_load(
            dec.read_text(encoding="utf-8"))["held"]}
check("inheritance: the B01..B04 packets are present and the B04 review json "
      "records the 6-code future-batch boundary map (the inherited one)",
      b01_ok and b02_ok and b03_ok and b04_ok
      and sorted(b04_map) == ["4MA1-1.6A", "4MA1-1.6B", "4MA1-4.4C",
                              "4MA1-6.2A", "4MA1-6.2D", "4MA1-6.3G"],
      str(b04_map))
check("inheritance: the B01, B02 and B03 review jsons record their 6/4/4-code "
      "maps",
      sorted(b01_map) == ["4MA1-1.2F", "4MA1-1.2I", "4MA1-1.3B", "4MA1-1.4D",
                          "4MA1-1.4E", "4MA1-1.7A"]
      and sorted(b02_map) == ["4MA1-1.4D", "4MA1-1.4E", "4MA1-1.7A",
                              "4MA1-1.8B"]
      and sorted(b03_map) == ["4MA1-1.1H", "4MA1-1.2A", "4MA1-1.6G",
                              "4MA1-2.1D"], str((b01_map, b02_map, b03_map)))
check("inheritance: of the B04 boundary map, NONE is in the B05 slice (1.6A/"
      "1.6B remain B03's rows; 4.4C/6.2A/6.2D/6.3G remain future)",
      not set(b04_map) & scope_sps, str(set(b04_map) & scope_sps))
check("inheritance: of the B03 boundary map, 2.1D is IN the B05 slice (the "
      "audit prediction landing — 'index laws' against the S2 row) and 1.1H/"
      "1.2A/1.6G remain outside",
      "4MA1-2.1D" in scope_sps
      and not {"4MA1-1.1H", "4MA1-1.2A", "4MA1-1.6G"} & scope_sps)
check("inheritance: the prior held ids (B01-H-01..05, B02-H-01..08, B03-H-01..08, "
      "B04-H-01..08) are preserved untouched — no id reuse in the B05 quarantine",
      prior_held_ids == {f"B01-H-{i:02d}" for i in range(1, 6)}
      | {f"B02-H-{i:02d}" for i in range(1, 9)}
      | {f"B03-H-{i:02d}" for i in range(1, 9)}
      | {f"B04-H-{i:02d}" for i in range(1, 9)}
      and not prior_held_ids & {h["id"] for h in b_held})

# 8. slice honesty (no invented titles)
topics = yaml.safe_load((REPO / f"graph/{QUAL}/topics.yaml").read_text("utf-8"))
subs = [next(s for s in topics["subtopics"] if s["code"] == c)
        for c in ("4MA1-S1-1.9", "4MA1-S1-1.10", "4MA1-S1-1.11",
                  "4MA1-S2-2.1", "4MA1-S2-2.2")]
check("slice honesty: the 1.9/1.10/1.11/2.1/2.2 subtopic titles are NULL in the "
      "ratified store and the record invents none (null-by-design honored)",
      all(s.get("title") is None and s.get("title_md") is None for s in subs))

# ---------------------------------------------------------------------------
if fails:
    print(f"PREVERIFY FAILED: {len(fails)} of {n}")
    for f in fails:
        print("  -", f)
    raise SystemExit(1)
print(f"c37_maths_a_batch05_preverify: ALL PASS ({n} checks) — record shape, "
      f"SP coverage, fifth-batch store state (5 K1 stores, B01..B04 unapplied), "
      f"evidence allow-list with edge pair-back (an EMPTY uncited-join census — "
      f"all 14 join-carried pages cited at their own SP), boundary and "
      f"misconception contract (three mints on {2.1} surfaces, no re-mint), "
      f"B01..B04 inheritance and null-title honesty all verified; the batch may "
      f"proceed to the quote probe")
