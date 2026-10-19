#!/usr/bin/env python3
"""T-C33 K2-C-1 — batch-B01 preverify (fail-closed, run BEFORE anything grows;
the c11_batch11_preverify.py pattern adapted to the first-batch state).

Machine-verifies the batch-B01 decision record's structure and its discipline
against the live repo:
  1. record shape      11 nodes (all CONCEPT, zero MISCONCEPTION) / 12 edges
                       (all REQUIRES_PREREQUISITE) / 5 held (B01-H-01..05) /
                       12 command kinds / 2 identity decisions
  2. SP coverage       every one of the 12 slice SPs carries >= 1 node
                       attachment; no node or edge references a non-slice SP
  3. slice state       the live K1 store carries exactly the slice rows at
                       global_order 1-12, all Foundation-applicability, zero
                       damage flags; the maths-a graph dir carries exactly the
                       5 K1 stores (no concepts/edges/kinds store exists yet —
                       the registry has not grown)
  4. evidence allow-list  NOTE-kind evidence files are exactly the 4
                       join-carried notes of the slice and each note evidence
                       row cites a note joined to the SAME SP it attaches to
                       (the unjoined-corpus negative control); MARK_SCHEME
                       evidence lives under the slice's EQ topic tree; SPEC
                       evidence cites the ratified store
  5. boundary discipline  every edge endpoint is a batch node (first batch —
                       no existing registry to reach into); no self-loops or
                       duplicate triples; every relation is in the concept-graph
                       vocabulary; validation_status SUGGESTED everywhere
                       (zero silent promotion)
  6. held + identity   held ids contiguous, status=held, reasons carry failure
                       classes; identity decisions reserved to the operator

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
DECISIONS = HERE / "c33_maths_a_batch01_decisions.yaml"
AUTH = HERE / "c33_maths_a_batch01_authorization.yaml"
JOIN_ARTIFACT = (REPO / "Official-Specifications/parsed/_derived/notes-join/"
                 f"{COURSE}.json")
SP_STORE = REPO / f"graph/{QUAL}/specification_points.yaml"
GRAPH_DIR = REPO / f"graph/{QUAL}"

K1_STORES = {"specification_points.yaml", "topics.yaml", "practicals.yaml",
             "assessment_objectives.yaml", "command_words.yaml"}
NOTE_FILES = {
    f"SME-RevisionNotes/{COURSE}/notes/1-numbers-and-the-number-system/"
    "number-toolkit/order-of-operations-bidmas-bodmas.md": "4MA1-1.1F",
    f"SME-RevisionNotes/{COURSE}/notes/1-numbers-and-the-number-system/"
    "prime-factors-hcf-and-lcm/types-of-number.md": "4MA1-1.1G",
    f"SME-RevisionNotes/{COURSE}/notes/2-equations-formulae-and-identities/"
    "algebraic-fractions/algebraic-fractions.md": "4MA1-1.2A",
    f"SME-RevisionNotes/{COURSE}/notes/1-numbers-and-the-number-system/"
    "fractions/mixed-numbers-and-improper-fractions.md": "4MA1-1.2B",
}
SLICE = [f"4MA1-1.1{c}" for c in "ABCDEFGH"] + \
        [f"4MA1-1.2{c}" for c in "ABCD"]
GUIDE_CLASSES = {"KNOW_TERM", "UNDERSTAND_RELATION", "APPLY_PROCEDURE"}
RELATIONS = {"REQUIRES_PREREQUISITE", "WRONG_ANSWER_PATTERN", "REMEDIATED_BY"}

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
check("record shape: authorization decision AUTHORIZED with verbatim directive "
      "'K2-C-1'", auth["authorization"]["decision"] == "AUTHORIZED"
      and auth["authorization"]["operator_statement_verbatim"] == "K2-C-1")
check("record shape: extraction_pass c33-k2c-batch-01 under T-C33",
      doc["meta"]["task"] == "T-C33"
      and doc["meta"]["extraction_pass"] == "c33-k2c-batch-01")
check("record shape: 11 nodes, all CONCEPT (zero misconception mints)",
      len(b_nodes) == 11 and len({x["code"] for x in b_nodes}) == 11
      and all(x["family"] == "CONCEPT" for x in b_nodes))
check("record shape: 12 authored edges, all REQUIRES_PREREQUISITE "
      "(first batch — no misconception pairing, no boundary class)",
      len(b_edges) == 12
      and all(e["relation"] in RELATIONS for e in b_edges)
      and {e["relation"] for e in b_edges} == {"REQUIRES_PREREQUISITE"})
check("record shape: 5 held candidates, ids B01-H-01..05 contiguous, "
      "status=held, failure-classed reasons",
      len(b_held) == 5
      and [h["id"] for h in b_held] == [f"B01-H-{i:02d}" for i in range(1, 6)]
      and all(h["status"] == "held" and h.get("reason") and h.get("candidate")
              for h in b_held))
check("record shape: 12 command kinds (one per slice SP, codes exact)",
      len(b_kinds) == 12 and {k["code"] for k in b_kinds} == set(SLICE)
      and all(k.get("verb") and k.get("guide_class") in GUIDE_CLASSES
              and k.get("demanded_substance") for k in b_kinds))
check("record shape: 2 identity decisions reserved to the operator",
      [i["id"] for i in b_ids] == ["B01-ID-01", "B01-ID-02"]
      and all(i.get("reserved_to") == "operator verdict" for i in b_ids))

# 2. SP coverage
scope_sps = set(doc["meta"]["scope"]["spec_points"])
check("scope list == the B01 slice (4MA1-1.1A..4MA1-1.2D)",
      scope_sps == set(SLICE), f"got {sorted(scope_sps)}")
node_sps = {sp["code"] for x in b_nodes for sp in (x.get("spec_points") or [])}
check("SP coverage: every slice SP covered by at least one node attachment",
      node_sps == scope_sps,
      f"missing {sorted(scope_sps - node_sps)}")
check("SP discipline: no node attachment outside the slice",
      node_sps <= scope_sps, f"foreign {sorted(node_sps - scope_sps)}")

# 3. slice state (the live store must be the sanctioned pre-batch state)
store = yaml.safe_load(SP_STORE.read_text(encoding="utf-8"))
rows = store["specification_points"]
by_code = {r["code"]: r for r in rows}
check("pre-state: ratified store 188 rows", len(rows) == 188)
slice_rows = sorted((by_code[c] for c in SLICE), key=lambda r: r["global_order"])
check("pre-state: slice rows sit at global_order 1..12 exactly",
      [r["global_order"] for r in slice_rows] == list(range(1, 13)))
check("pre-state: every slice row is Foundation-applicability with zero "
      "damage flags (the 8 flagged rows live outside this slice)",
      all((r["applicability"] or {}).get("tier") == "Foundation"
          and not r.get("damage_flags") for r in slice_rows))
check("pre-state: graph/igcse-maths-a/ carries exactly the 5 K1 stores — "
      "the registry has not grown (no concepts/edges/chunk-maps/kinds yet)",
      {p.name for p in GRAPH_DIR.iterdir() if p.is_file()} == K1_STORES,
      str(sorted(p.name for p in GRAPH_DIR.iterdir())))

# 4. evidence allow-list (the B01 negative control)
join = json.loads(JOIN_ARTIFACT.read_text(encoding="utf-8"))
code_by_official = {r["official_code"]: r["code"] for r in rows}
join_by_note = {}
for j in join["joins"]:
    md = j["note_path"][:-len(".json")] + ".md"
    rc = code_by_official.get(j["resolved_code"], j["resolved_code"])
    join_by_note.setdefault(f"SME-RevisionNotes/{COURSE}/{md}",
                            set()).add(rc)
bad: list[str] = []
for x in b_nodes:
    for sp in (x.get("spec_points") or []):
        for ev in sp["evidence"]:
            f, kind = ev["file"], ev["kind"]
            if kind == "SPEC":
                if f != f"graph/{QUAL}/specification_points.yaml":
                    bad.append(f"{x['code']}/{sp['code']}: bad SPEC file {f}")
            elif kind == "NOTE":
                if f not in NOTE_FILES:
                    bad.append(f"{x['code']}/{sp['code']}: NOTE file outside "
                               f"the 4 join-carried notes: {f}")
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
    for ev in e["evidence"]:
        if ev["kind"] not in ("SPEC", "NOTE", "MARK_SCHEME"):
            bad.append(f"{e['source']}->{e['target']}: unknown kind")
check("evidence allow-list: every evidence anchor cites an allowed file for "
      "its kind and SP (no unjoined-corpus citations)",
      not bad, "; ".join(bad[:4]))
note_files_cited = {ev["file"] for x in b_nodes
                    for sp in x.get("spec_points") or []
                    for ev in sp["evidence"] if ev["kind"] == "NOTE"}
check("evidence allow-list: the cited NOTE set is exactly the 4 join-carried "
      "notes (each used for its joined SP)",
      note_files_cited == set(NOTE_FILES), str(sorted(note_files_cited)))

# 5. boundary discipline
b_codes = {x["code"] for x in b_nodes}
check("boundary discipline: every edge endpoint is a batch node (first batch "
      "— no existing registry, no cross-batch targets)",
      all(e["source"] in b_codes and e["target"] in b_codes for e in b_edges))
check("boundary discipline: no self-loop, no duplicate triple",
      all(e["source"] != e["target"] for e in b_edges)
      and len({(e["source"], e["relation"], e["target"])
               for e in b_edges}) == len(b_edges))
check("promotion discipline: zero silent promotion — every node SUGGESTED",
      all(x["validation_status"] == "SUGGESTED" for x in b_nodes))
check("provenance: every node carries the batch extraction_pass and "
      "AI_SUGGESTED tier",
      all((x.get("provenance") or {}).get("tier") == "AI_SUGGESTED"
          and (x.get("provenance") or {}).get("extraction_pass")
          == "c33-k2c-batch-01" for x in b_nodes))

# 6. coverage profile stated on the record
cp = doc["meta"]["scope"]["coverage_profile"]
joined_in_slice = set().union(*join_by_note.values()) & scope_sps
check("coverage profile stated: 4 notes-joined / 8 spec-text-only, equal to "
      "the join artifact's own census for this slice",
      set(cp["notes_joined_sps"]) == joined_in_slice
      and cp["notes_joined_count"] == len(joined_in_slice) == 4
      and cp["spec_text_only_count"] == len(SLICE) - len(joined_in_slice) == 8,
      f"join census = {sorted(joined_in_slice)}")

# ---------------------------------------------------------------------------
if fails:
    print(f"PREVERIFY FAILED: {len(fails)} of {n}")
    for f in fails:
        print("  -", f)
    raise SystemExit(1)
print(f"c33_maths_a_batch01_preverify: ALL PASS ({n} checks) — record shape, "
      f"SP coverage, first-batch store state, evidence allow-list (the "
      f"unjoined-corpus negative control), boundary and promotion discipline "
      f"all verified; the batch may proceed to the quote probe")
