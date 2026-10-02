#!/usr/bin/env python3
"""T-C39 K2 Lane C — §18 GOVERNED APPLY for igcse-maths-a B01..B06 (fail-closed;
the chemistry c11_concept_pilot.py convention instantiated for the consolidated
verdict intake).

Preconditions (all fail-closed):
  * scripts/c39_maths_a_k2c_verdicts.yaml parses; operator_ruling.decided_by ==
    operator; authority SUGGESTED; zero promotions authorized
  * graph/reports/C39_K2C_VERDICT_CHECK.json exists with result == ALL PASS
  * graph/igcse-maths-a/ still carries EXACTLY the 5 K1 stores (pre-apply state)
  * the six decision records parse; per-batch counts equal the REVIEW.json
    totals (nodes, edges, held, command kinds, attachments)

Emits (deterministic; byte-identical re-runs — no wall-clock in the stores):
  graph/igcse-maths-a/concepts.yaml          meta + 82 nodes (71 CONCEPT + 11
                                             MISCONCEPTION) verbatim from the
                                             decision records + version=1 /
                                             created_at=batch generated_date /
                                             damage_flags=[]
  graph/igcse-maths-a/concept_edges.yaml     meta + 84 derived PART_OF edges
                                             (node attachments, node order) +
                                             73 authored semantic edges
                                             (decision order); provenance
                                             blocks built from the batch metas
                                             + the decision edge `derivation`
                                             (verbatim, zero invention); NO
                                             HUMAN_VALIDATED anywhere
  graph/igcse-maths-a/spec_command_kinds.yaml meta + 72 command-kind rows
                                             verbatim
  scripts/graph_paths.yaml                   +3 maths-a store entries
                                             (byte-anchored, fail-closed)
  graph/reports/C39_IGCSE_MATHS_A_K2C_APPLY_RECORD.{json,md}

NEVER touches: the decision records (incl. their held: lists), the 5 K1 maths-a
stores, graph/igcse-chemistry/**, the corpora, the consolidated review copy.
Held candidates are NOT emitted; PART_OF is derived from node attachments only
(C11_ARCHITECTURE.md §18 scope limits).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
GRAPH = REPO / "graph" / QUAL
REPORTS = REPO / "graph/reports"
VERDICTS = HERE / "c39_maths_a_k2c_verdicts.yaml"
VCHECK = REPORTS / "C39_K2C_VERDICT_CHECK.json"
DECISIONS = [HERE / f"c{32+n}_maths_a_batch0{n}_decisions.yaml" for n in range(1, 7)]
REVIEWS = [REPORTS / f"C{32+n}_BATCH0{n}_REVIEW.json" for n in range(1, 7)]
REVIEW_COPY = REPORTS / "C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md"
REGISTRY = HERE / "graph_paths.yaml"
GENERATED = "2026-10-02"  # deterministic store date (the verdict session date)


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def sha256_16(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(doc: dict) -> str:
    return yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100,
                          default_flow_style=False)


# DC-04 (dated correction, P5) — cross-batch namespace disambiguation, applied
# at emission only. B05's 2.1D row-node re-used B03's 1.4C code
# (4MA1-CON-INDEX-LAWS). The decision records themselves assert TWO distinct
# identities: different CORE SPs (1.4C vs 2.1D), different titles ("Index laws
# over integer, fractional and negative powers" vs "Index laws in simple
# cases"), different substances, and B05's own derivation_notes ("the
# laws-of-indices NOTE page is joined to 1.4C (B03's row) and is not citable
# here ... the node authors from the ratified wording alone"). The series'
# mirror-pair convention (B04-ID-01, B05-ID-01, B06-ID-01) rules mirror rows as
# TWO nodes with DISTINCT codes on the store's own row split — B06-ID-01's
# naming precedent puts the row-arm suffix on the second (simple-cases) arm.
# The decision records stay byte-untouched; the B05 instance is emitted under
# its own recorded identity's code and the B05-internal edge endpoints follow.
# Found by c39_maths_a_k2c_apply_check.py P3 (the review §9 "no duplicate
# concept IDs" check working as designed). Fail-closed census asserted below.
DISAMBIGUATION_BY_BATCH = {5: {"4MA1-CON-INDEX-LAWS":
                               "4MA1-CON-INDEX-LAWS-SIMPLE-CASES"}}
DC04 = {
    "id": "DC-04",
    "subject": "cross-batch node-code collision: 4MA1-CON-INDEX-LAWS",
    "finding": "B03 (1.4C) and B05 (2.1D) both minted 4MA1-CON-INDEX-LAWS — "
               "caught by the post-apply P3 uniqueness gate (review §9 'no "
               "duplicate concept IDs were minted'), invisible to the per-batch "
               "preverifies (single-batch scope) and to the consolidated "
               "review's per-batch surface",
    "resolution": "namespace disambiguation at emission per the records' own "
                  "identity assertions: B03's node (1.4C, the full Higher "
                  "laws, two-note substrate) keeps 4MA1-CON-INDEX-LAWS; B05's "
                  "node (2.1D, simple cases, spec-text-only) is emitted as "
                  "4MA1-CON-INDEX-LAWS-SIMPLE-CASES with its 3 B05-internal "
                  "edge endpoints following; zero cross-batch references "
                  "existed (census asserted fail-closed)",
    "basis": "different CORE SPs/titles/substances in the decision records; "
             "B05 derivation_notes ('not citable here; authors from the "
             "ratified wording alone'); the B04/B05/B06-ID-01 mirror-pair "
             "convention (two nodes, distinct codes, per row split); no merge "
             "or split is performed and no decision record is edited",
    "disposition": "records unedited (C31 §7); the emitted store carries both "
                   "nodes under distinct codes; 82 nodes preserved",
}


def main() -> int:
    # ---- preconditions --------------------------------------------------------
    v = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    ruling = (v.get("meta") or {}).get("operator_ruling") or {}
    if ruling.get("decided_by") != "operator":
        die("verdict record is not operator-owned")
    if "SUGGESTED" not in str((v.get("promotion_authorization") or {}).get("authority", "")):
        die("verdict record does not authorize SUGGESTED authority")
    if not VCHECK.exists():
        die("verdict check report missing — run c39_maths_a_k2c_verdict_check.py first")
    vc = json.loads(VCHECK.read_text(encoding="utf-8"))
    if vc.get("result") != "ALL PASS":
        die("verdict check is not ALL PASS")
    k1 = sorted(p.name for p in GRAPH.glob("*.yaml"))
    k1_want = sorted(["specification_points.yaml", "topics.yaml", "practicals.yaml",
                      "assessment_objectives.yaml", "command_words.yaml"])
    k2_want = sorted(k1_want + ["concepts.yaml", "concept_edges.yaml",
                                "spec_command_kinds.yaml"])
    if k1 not in (k1_want, k2_want):
        die(f"pre-apply store state wrong: {k1}")
    for n in range(1, 7):
        arts = json.loads(REVIEWS[n - 1].read_text(encoding="utf-8"))
        if arts.get("stores_grown") != 0:
            die(f"B0{n} stores_grown != 0 in its REVIEW artifact")

    # ---- load decision records + cross-check against the artifacts ------------
    decs = []
    for n, p in enumerate(DECISIONS, start=1):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        arts = json.loads(REVIEWS[n - 1].read_text(encoding="utf-8"))
        t = arts["totals"]
        nodes = d.get("nodes", [])
        edges = d.get("edges", [])
        n_con = sum(1 for x in nodes if x.get("family") == "CONCEPT")
        n_mis = sum(1 for x in nodes if x.get("family") == "MISCONCEPTION")
        att = sum(len(x.get("spec_points") or []) for x in nodes)
        exp_nodes = t.get("nodes", t.get("concept_nodes", 0) + t.get("misconception_nodes", 0))
        if len(nodes) != exp_nodes:
            die(f"B0{n}: {len(nodes)} nodes != artifact {exp_nodes}")
        if n_con != t.get("concept_nodes", n_con) or n_mis != t.get("misconception_nodes", 0):
            die(f"B0{n}: family split {n_con}/{n_mis} != artifact")
        if len(edges) != t["authored_edges"]:
            die(f"B0{n}: {len(edges)} edges != artifact {t['authored_edges']}")
        if len(d.get("held", [])) != t["held"]:
            die(f"B0{n}: held {len(d.get('held', []))} != artifact {t['held']}")
        if len(d.get("command_kinds", [])) != t["command_kinds"]:
            die(f"B0{n}: command kinds != artifact")
        if att != t["node_attachments"]:
            die(f"B0{n}: attachments {att} != artifact {t['node_attachments']}")
        if att != t["derived_partof_at_apply"]:
            die(f"B0{n}: attachments {att} != derived_partof_at_apply")
        decs.append(d)

    # ---- DC-04 census (fail-closed) ---------------------------------------------
    old_code = "4MA1-CON-INDEX-LAWS"
    new_code = DISAMBIGUATION_BY_BATCH[5][old_code]
    b3 = decs[2]
    b5 = decs[4]
    b3_nodes = [x for x in b3["nodes"] if x["code"] == old_code]
    b5_nodes = [x for x in b5["nodes"] if x["code"] == old_code]
    if len(b3_nodes) != 1 or len(b5_nodes) != 1:
        die(f"DC-04 census: expected exactly one {old_code} node in B03 and B05, "
            f"got {len(b3_nodes)}/{len(b5_nodes)}")
    if b3_nodes[0]["spec_points"][0]["code"] != "4MA1-1.4C" or \
            b5_nodes[0]["spec_points"][0]["code"] != "4MA1-2.1D":
        die("DC-04 census: home SPs drifted from 1.4C/2.1D")
    b5_refs = sum(1 for e in b5["edges"]
                  if e["source"] == old_code or e["target"] == old_code)
    if b5_refs != 3:
        die(f"DC-04 census: expected exactly 3 B05 edge endpoint references, "
            f"got {b5_refs}")
    for bn, d in enumerate(decs, start=1):
        if bn in (3, 5):
            continue
        for e in d["edges"]:
            if old_code in (e["source"], e["target"]):
                die(f"DC-04 census: unexpected cross-batch reference in B0{bn}")
        for x in d["nodes"]:
            if x["code"] == old_code:
                die(f"DC-04 census: unexpected node in B0{bn}")

    def dc04(bn: int, code: str) -> str:
        return DISAMBIGUATION_BY_BATCH.get(bn, {}).get(code, code)

    # ---- build the store bodies ------------------------------------------------
    nodes_out = []
    part_of = []
    semantic = []
    cmdk = []
    sp_codes: list[str] = []
    for bn, d in enumerate(decs, start=1):
        bdate = str(d["meta"]["generated_date"])
        bpass = d["meta"]["extraction_pass"]
        bmodel = d["meta"]["model_version"]
        for x in d["nodes"]:
            n = {k: x[k] for k in x}  # verbatim copy, insertion order preserved
            n["code"] = dc04(bn, x["code"])
            n["version"] = 1
            n["created_at"] = bdate
            n["damage_flags"] = []
            nodes_out.append(n)
            for sp in x.get("spec_points") or []:
                if sp["code"] not in sp_codes:
                    sp_codes.append(sp["code"])
                po = {
                    "source": n["code"],
                    "relation": "PART_OF",
                    "target": sp["code"],
                    "role": sp.get("role", "CORE"),
                    "evidence": sp.get("evidence", []),
                    "provenance": dict(x.get("provenance") or {}),
                    "confidence": x.get("confidence", "high"),
                    "validation_status": "SUGGESTED",
                    "version": 1,
                    "created_at": bdate,
                }
                part_of.append(po)
        for e in d["edges"]:
            prov = {
                "tier": "AI_SUGGESTED",
                "model_version": bmodel,
                "extraction_pass": bpass,
                "generated_date": bdate,
                "derivation_method": e["derivation"],
            }
            semantic.append({
                "source": dc04(bn, e["source"]),
                "relation": e["relation"],
                "target": dc04(bn, e["target"]),
                "evidence": e.get("evidence", []),
                "provenance": prov,
                "confidence": e.get("conf", "high"),
                "validation_status": "SUGGESTED",
                "version": 1,
                "created_at": bdate,
            })
        cmdk += [dict(k) for k in d.get("command_kinds", [])]

    # sort spec_points into the ratified global_order walk
    sps = yaml.safe_load((GRAPH / "specification_points.yaml").read_text(encoding="utf-8"))
    go_of = {p["code"]: int(p["global_order"]) for p in sps["specification_points"]
             if p.get("global_order") is not None}
    missing = [c for c in sp_codes if c not in go_of]
    if missing:
        die(f"attachment codes absent from the ratified store: {missing}")
    sp_codes = sorted(set(sp_codes), key=lambda c: go_of[c])
    if [go_of[c] for c in sp_codes] != list(range(1, 73)):
        die("attachment codes != the global_order 1..72 walk")

    n_con = sum(1 for x in nodes_out if x["family"] == "CONCEPT")
    n_mis = sum(1 for x in nodes_out if x["family"] == "MISCONCEPTION")
    counts = {"nodes": len(nodes_out), "concepts": n_con, "misconceptions": n_mis,
              "part_of_edges": len(part_of), "semantic_edges": len(semantic)}
    if counts != {"nodes": 82, "concepts": 71, "misconceptions": 11,
                  "part_of_edges": 84, "semantic_edges": 73}:
        die(f"emitted counts {counts} != the authorized surface")
    if len(cmdk) != 72:
        die(f"command kinds {len(cmdk)} != 72")

    stage = "+".join(str(d["meta"].get("stage") or d["meta"]["extraction_pass"])
                     for d in decs) + "+apply"
    passes = [d["meta"]["extraction_pass"] for d in decs]
    dec_names = ", ".join(p.name for p in DECISIONS)

    common_meta = {
        "task": "T-C39",
        "stage": stage,
        "curriculum_code": "4MA1-2016",
        "phase": 3,
        "scope": ("K2 Lane C batches B01..B06 (global_order 1-72 = 4MA1-1.1A..2.5A "
                  "at the Higher-preferred tier-dedupe store state) — the governed "
                  "§18 apply of the operator's consolidated verdict "
                  "(PASS WITH NOTES, 2026-10-02); zero silent promotion; held "
                  "quarantine preserved (45 candidates stay in the decision "
                  "records, none emitted)"),
        "spec_points": sp_codes,
        "practicals": [],
        "negative_control": ("UNJOINED-CORPUS NEGATIVE CONTROL — every NOTE anchor "
                             "is join-carried through the T-C32 K2-A notes-join "
                             "(202 joins / 111 codes) and pair-backed (node "
                             "attachments at their SP; edge evidence at an endpoint "
                             "SP, the B02 strength); the corpus's unjoined "
                             "neighbours are cited NOWHERE; per-batch uncited-join "
                             "censuses carry dispositions, never padded anchors"),
        "generator": "scripts/c39_maths_a_k2c_apply.py",
        "decision_record": dec_names,
        "extraction_pass": passes,
        "model_version": "GLM (Super Z agent, z.ai)",
        "contract": ("graph/reports/C31_IGCSE_MATHS_A_K2_SCOPE.md §5/§8; promotion "
                     "pathway C11_ARCHITECTURE.md §18; verdict record "
                     "scripts/c39_maths_a_k2c_verdicts.yaml; consolidated operator "
                     "review graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md"),
        "generated": GENERATED,
        "provenance_default": "AI_SUGGESTED",
        "validation_gate": ("operator consolidated review PASS WITH NOTES "
                            "(2026-10-02, zai-web) over the six per-batch review "
                            "sheets; no promotion from generation; HUMAN_VALIDATED "
                            "is operator-only (§18 exact-identity pathway; zero "
                            "promotion entries recorded at this gate)"),
        "edge_vocabulary": ("REQUIRES_PREREQUISITE + WRONG_ANSWER_PATTERN + "
                            "REMEDIATED_BY (the frozen §8A.11 misconception triple "
                            "distinction carried; remediation target = WAP target "
                            "per the B1-E-25 pattern) + derived PART_OF (node "
                            "attachments); V2 projection documented in "
                            "C11_ARCHITECTURE.md §13"),
    }

    def header(title: str) -> str:
        lines = [
            f"# SyllabAI 4MA1 concept graph (K2 Lane C batches B01-B06) — T-C39, graph-as-code"
            f" (KNOWLEDGE_GRAPH_CONTEXT.md §8A.14, C11_ARCHITECTURE.md §10/§18 pattern)",
            f"# Generated by scripts/c39_maths_a_k2c_apply.py from the decision-record registry:",
        ]
        lines += [f"#   {p.name} (extraction_pass {d['meta']['extraction_pass']})"
                  for p, d in zip(DECISIONS, decs)]
        lines += [
            "# DO NOT hand-edit: re-run the script. Provenance tier AI_SUGGESTED; validation gate =",
            "# operator consolidated review PASS WITH NOTES (2026-10-02) — see meta.validation_gate.",
            "# Store date 2026-10-02 (deterministic contract; byte-identical re-runs).",
            f"# {title}",
            "",
        ]
        return "\n".join(lines)

    # ---- write the three stores ------------------------------------------------
    concepts = {"meta": {**common_meta, "counts": counts}, "nodes": nodes_out}
    edges_meta = {**common_meta, "counts": {"edges": len(part_of) + len(semantic),
                                            "part_of_edges": len(part_of),
                                            "semantic_edges": len(semantic)}}
    concept_edges = {"meta": edges_meta, "edges": part_of + semantic}
    cmdk_meta = {**common_meta, "counts": {"spec_points": len(cmdk)}}
    spec_command_kinds = {"meta": cmdk_meta, "command_kinds": cmdk}

    (GRAPH / "concepts.yaml").write_text(
        header("nodes: code/family/[pattern_class]/title/aliases/spec_points/"
               "[evidence/remediation_evidence]/provenance/confidence/"
               "validation_status/version/created_at/damage_flags — verbatim from "
               "the decision records plus version/created_at/damage_flags") +
        dump(concepts), encoding="utf-8")
    (GRAPH / "concept_edges.yaml").write_text(
        header("edges: PART_OF first (the 84 node attachments, node order), then "
               "the 73 authored semantic edges (decision order); provenance built "
               "from the batch metas + the decision `derivation`") +
        dump(concept_edges), encoding="utf-8")
    (GRAPH / "spec_command_kinds.yaml").write_text(
        header("command_kinds: code/verb/guide_class/demanded_substance — verbatim "
               "from the decision records") +
        dump(spec_command_kinds), encoding="utf-8")

    # ---- registry update (byte-anchored, fail-closed) ---------------------------
    reg_txt = REGISTRY.read_text(encoding="utf-8")
    anchor = ("      command_words: graph/{QUAL}/command_words.yaml\n"
              "    reports_dir: graph/reports/                                  # SHARED audit trail (never per-qual)\n")
    insertion = ("      command_words: graph/{QUAL}/command_words.yaml\n"
                 "      concepts: graph/{QUAL}/concepts.yaml\n"
                 "      concept_edges: graph/{QUAL}/concept_edges.yaml\n"
                 "      spec_command_kinds: graph/{QUAL}/spec_command_kinds.yaml\n"
                 "    reports_dir: graph/reports/                                  # SHARED audit trail (never per-qual)\n")
    import yaml as _y
    if insertion in reg_txt:
        pass  # idempotent re-run: registry already carries the maths-a K2 stores
    elif anchor in reg_txt:
        if "      concepts: graph/{QUAL}/concepts.yaml" in reg_txt.split("igcse-chemistry")[1]:
            die("maths-a registry block appears to already carry concepts — aborting")
        reg_new = reg_txt.replace(anchor, insertion, 1)
        reg_check = _y.safe_load(reg_new)
        ma_stores = reg_check["quals"]["igcse-maths-a"]["stores"]
        if sorted(ma_stores.keys()) != sorted(["specification_points", "topics",
                                               "practicals", "assessment_objectives",
                                               "command_words", "concepts",
                                               "concept_edges", "spec_command_kinds"]):
            die(f"post-edit registry maths-a stores wrong: {sorted(ma_stores.keys())}")
        REGISTRY.write_text(reg_new, encoding="utf-8")
    else:
        die("registry anchor not found (maths-a command_words -> reports_dir block)")

    # ---- apply record ------------------------------------------------------------
    stores = {p.name: {"sha256_16": sha256_16(GRAPH / p.name),
                       "bytes": (GRAPH / p.name).stat().st_size}
              for p in sorted(GRAPH.glob("*.yaml"))}
    baseline = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    held_ids = []
    for p in DECISIONS:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        held_ids += [h["id"] for h in d.get("held", [])]
    rec = {
        "schema": "c39-k2c-apply-record/1.0",
        "task": "T-C39",
        "gate": "K2 Lane C §18 governed apply (B01..B06 consolidated)",
        "generated_utc": now,
        "store_generated_date": GENERATED,
        "baseline": baseline,
        "verdict_record": "scripts/c39_maths_a_k2c_verdicts.yaml",
        "verdict_check": "graph/reports/C39_K2C_VERDICT_CHECK.json (ALL PASS)",
        "intake": "graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md",
        "intake_sha256": sha256(REVIEW_COPY),
        "decision_records": [p.name for p in DECISIONS],
        "authorized_surface": {
            "authority": "SUGGESTED (provenance tier AI_SUGGESTED; zero "
                         "HUMAN_VALIDATED; zero §18 promotion entries)",
            "nodes": counts["nodes"], "concepts": n_con, "misconceptions": n_mis,
            "semantic_edges": len(semantic), "part_of_edges": len(part_of),
            "command_kinds": len(cmdk), "held_preserved": len(held_ids),
        },
        "emitted_stores": stores,
        "registry_delta": {"qual": QUAL, "added": ["concepts", "concept_edges",
                                                   "spec_command_kinds"],
                           "maths_a_store_count": 8,
                           "still_absent": ["spec_chunk_mappings (K2-B pending)",
                                            "relationships (ratified-hierarchy lane)"]},
        "dated_corrections": ["DC-01 held 45 (review prose 47 corrected)",
                              "DC-02 PART_OF 84 (batch-record prose 77 corrected; "
                              "machine artifacts govern)",
                              "DC-03 quote probes 490/490 + preverify 192/192 confirmed",
                              DC04],
        "boundary_resolution": {"superseding_map": ["4MA1-1.7C", "4MA1-1.7D",
                                                    "4MA1-2.7B"],
                                "landing_chain": {"B06-H-02": "B05-H-06",
                                                  "B06-H-03": "B04-H-06"},
                                "cross_batch_holds": "all 45 held candidates stay "
                                                     "quarantined in the decision "
                                                     "records; none emitted"},
        "held_ids": held_ids,
        "not_done": ["no HUMAN_VALIDATED anywhere", "no promotions-file entries",
                     "no held-candidate promotion", "no new concept mints beyond "
                     "the 82", "no spec_chunk_mappings (K2-B pending)",
                     "no chemistry writes", "no corpus writes",
                     "decision records unmutated"],
        "post_apply_check": "scripts/c39_maths_a_k2c_apply_check.py",
    }
    (REPORTS / "C39_IGCSE_MATHS_A_K2C_APPLY_RECORD.json").write_text(
        json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md = "\n".join([
        "# C39 — K2 Lane C §18 Governed Apply — igcse-maths-a B01..B06",
        "",
        f"**Generated:** {now}  |  **Baseline:** `{baseline}`  |  "
        f"**Store date (deterministic):** {GENERATED}",
        "",
        "## What this is",
        "",
        "The §18 governed apply authorized by the operator's consolidated review",
        "(PASS WITH NOTES, 2026-10-02, zai-web) over the six authored-to-gate Lane C",
        "packets (B01..B06, global_order 1–72 = 4MA1-1.1A..2.5A). The confirmed",
        "authored surface is materialized at **authority SUGGESTED** (provenance tier",
        "`AI_SUGGESTED`); nothing is HUMAN_VALIDATED; zero promotion entries; all 45",
        "held candidates stay quarantined in the decision records, none emitted.",
        "",
        "## Inputs",
        "",
        "- Verdict record: `scripts/c39_maths_a_k2c_verdicts.yaml` (operator-owned; DC-01..03 dated corrections)",
        "- Verdict check: `graph/reports/C39_K2C_VERDICT_CHECK.json` — ALL PASS 8/8",
        "- Consolidated review: `graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md`",
        f"  (sha256 `{rec['intake_sha256']}`, byte-identical to the operator upload)",
        "- Decision records: " + ", ".join(f"`{p.name}`" for p in DECISIONS),
        "",
        "## Emitted (counts == the authorized verdict surface)",
        "",
        f"- `graph/igcse-maths-a/concepts.yaml` — **{counts['nodes']} nodes** "
        f"({n_con} CONCEPT + {n_mis} MISCONCEPTION), sha256_16 `{stores['concepts.yaml']['sha256_16']}`",
        f"- `graph/igcse-maths-a/concept_edges.yaml` — **{len(part_of)} derived PART_OF + "
        f"{len(semantic)} authored semantic edges** (51 REQUIRES_PREREQUISITE + 11 "
        f"WRONG_ANSWER_PATTERN + 11 REMEDIATED_BY), sha256_16 `{stores['concept_edges.yaml']['sha256_16']}`",
        f"- `graph/igcse-maths-a/spec_command_kinds.yaml` — **{len(cmdk)} rows** "
        f"(56 APPLY_PROCEDURE + 15 UNDERSTAND_RELATION + 1 KNOW_TERM), "
        f"sha256_16 `{stores['spec_command_kinds.yaml']['sha256_16']}`",
        "- `scripts/graph_paths.yaml` — maths-a registry 5 → **8 stores** "
        "(spec_chunk_mappings arrives with K2-B; relationships with the ratified-hierarchy lane)",
        "",
        "## Dated corrections carried (P5)",
        "",
        "- **DC-01** held = **45** (the review's own §2 table and the artifacts; the",
        "  '47' aggregate prose in the review is corrected here)",
        "- **DC-02** derived PART_OF = **84** (the artifacts' "
        "`derived_partof_at_apply` 13/14/14/13/15/15; the C36/C37/C38 record prose",
        "  '77' undercounted B04/B05/B06 attachments — corrected here, records unedited)",
        "- **DC-03** quote probes 490/490 and preverify 192/192 confirmed as stated",
        "",
        "## Governance boundary",
        "",
        "- Zero silent promotion: every emitted row is CONFIRM-authorized by the",
        "  verdict record; the held/quarantine surface (45 ids) is preserved verbatim",
        "  in the decision records and emitted NOWHERE.",
        "- The §18 exact-identity promotion round (HUMAN_VALIDATED,",
        "  `c11_promote.py` pattern) remains a separate operator gate.",
        "- Boundary: superseding map {4MA1-1.7C, 4MA1-1.7D, 4MA1-2.7B}; landing",
        "  re-records B06-H-02 (← B05-H-06) and B06-H-03 (← B04-H-06) stay HELD.",
        "- K2-B (chunk substrate) has not run; K3/K4 (serving/explorer) deferred by",
        "  the playbook; chemistry and the corpora byte-untouched.",
        "",
        "## Post-apply verification",
        "",
        "`scripts/c39_maths_a_k2c_apply_check.py` → `graph/reports/C39_K2C_POST_APPLY_CHECK.json`",
        "(counts, no-held-promoted, uniqueness, endpoint resolution, PART_OF ==",
        "attachments, misconception pairing, anchor byte-verification, negative",
        "controls, registry + standing checkers, determinism re-run).",
        "",
    ])
    (REPORTS / "C39_IGCSE_MATHS_A_K2C_APPLY_RECORD.md").write_text(md + "\n",
                                                                   encoding="utf-8")
    print("c39_maths_a_k2c_apply: APPLIED")
    print(f"  concepts.yaml          {counts['nodes']} nodes ({n_con}+{n_mis}) "
          f"sha256_16 {stores['concepts.yaml']['sha256_16']}")
    print(f"  concept_edges.yaml     {len(part_of)} PART_OF + {len(semantic)} semantic "
          f"sha256_16 {stores['concept_edges.yaml']['sha256_16']}")
    print(f"  spec_command_kinds.yaml {len(cmdk)} rows "
          f"sha256_16 {stores['spec_command_kinds.yaml']['sha256_16']}")
    print(f"  registry: maths-a 5 -> 8 stores; held preserved: {len(held_ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
