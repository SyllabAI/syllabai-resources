#!/usr/bin/env python3
"""c42_r0_blast_radius_census.py — T-C42 R0: the EQ blast-radius census.

Read-only. Enumerates, for the 45 defective id->code mappings named by the
C40 fill (and re-verified by the C42 scope battery G2):
  1. per-id EQ part references declared by the resolution file, cross-checked
     against the EQ corpus tree via git grep (no checkout needed);
  2. which surfaces in THIS repo consume those tags:
       - spec-links/ per-course JSONs (built by build_learner_spec_links.py)
       - the s104 question-package tooling (consumption check by source grep)
       - the C32 notes-join / C40 chunk substrate (the triggering surfaces)
       - maths-a kg export artifacts (existence check)
  3. external consumers (core/hub/RAG serving): recorded as NOT audited here.

Writes exactly one file: graph/reports/C42_R0_BLAST_RADIUS_CENSUS.json.
Exit 0 iff the census completes (it asserts nothing beyond shape).
"""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R0_BLAST_RADIUS_CENSUS.json"
COURSE = "igcse-maths-a-18-higher"


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"git show failed for {path}")
    return r.stdout


def git_grep_all_ids(tree_path: str) -> Counter:
    """persistent cat-file batch over the course's JSON files (the sparse-cone
    fast channel, the c32/c40 convention — git grep walks the asset blobs and
    is prohibitively slow); returns id -> total occurrence count."""
    ls = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "HEAD", "--name-only",
                         tree_path], capture_output=True, text=True, check=True).stdout.split()
    jsons = [f for f in ls if f.endswith(".json")]
    proc = subprocess.Popen(["git", "-C", str(REPO), "cat-file", "--batch"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    assert proc.stdin and proc.stdout
    counts: Counter = Counter()
    import re
    id_re = re.compile(r"spcpt_[A-Za-z0-9]+")
    for f in jsons:
        proc.stdin.write(f"HEAD:{f}\n".encode())
        proc.stdin.flush()
        header = proc.stdout.readline().decode().split()
        if len(header) < 3 or header[1] != "blob":
            continue
        size = int(header[2])
        blob = proc.stdout.read(size + 1)[:-1]  # blob + trailing newline
        for m in id_re.findall(blob.decode("utf-8", "replace")):
            counts[m] += 1
    proc.stdin.close()
    proc.wait(timeout=30)
    return counts


def main() -> int:
    verdicts = yaml.safe_load((REPO / "scripts/c40_maths_a_substrate_review_verdicts.yaml").read_text())["verdicts"]
    join = json.loads((REPO / "Official-Specifications/parsed/_derived/notes-join/"
                       "igcse-maths-a-18-higher.json").read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}
    res = json.loads(git_show(f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"))
    by_id = {r["id"]: r for r in res["resolved"]}

    nl = [x for x in verdicts.values()
          if x["verdict"] == "REJECT" and x.get("root") == "note-level"]
    pairs = sorted(set((x["note_path"], x["spec_code"]) for x in nl))

    eq_dir = f"SME-ExamQuestion/{COURSE}"
    id_occurrences = git_grep_all_ids(eq_dir)
    rows = []
    for np_, wrong in pairs:
        aid = jrows[np_]["anchor_id"]
        rr = by_id[aid]
        rows.append({
            "anchor_id": aid,
            "sme_name": rr["sme_name"],
            "wrong_code": f"4MA1-{rr['resolved_code']}",
            "wrong_code_wording": rr["official_wording"],
            "referenced_by_parts_declared": rr.get("referenced_by_parts", 0),
            "eq_corpus_id_occurrences": id_occurrences.get(aid, 0),
        })

    # spec-links surface
    sl_files = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "HEAD", "--name-only",
                               "spec-links/"], capture_output=True, text=True).stdout.split()
    sl_maths = [f for f in sl_files if "maths-a" in f]
    sl_hits = {}
    sl_wrong_code_hits = {}
    for f in sl_maths:
        blob = git_show(f).decode("utf-8", "replace")
        ids_hit = sum(1 for r in rows if r["anchor_id"] in blob)
        codes_hit = sum(1 for r in rows if r["wrong_code"] in blob)
        sl_hits[f] = ids_hit
        sl_wrong_code_hits[f] = codes_hit

    # s104 consumption check (source-level, recorded verbatim)
    s104 = (REPO / "scripts/s104_build_question_package.py").read_text()
    s104_consumes = any(t in s104 for t in ("spec_point_resolution", "spcpt_", "spec_point_ids"))

    # maths-a kg export existence
    kg_maths = sorted(p.name for p in (REPO / "graph/igcse-maths-a").glob("*kg*"))

    census = {
        "schema": "syllabai.c42-r0-blast-radius-census/1.0",
        "task": "T-C42 / R0",
        "stage": "eq-blast-radius-census",
        "defective_joins": len(rows),
        "sum_referenced_by_parts_declared": sum(r["referenced_by_parts_declared"] for r in rows),
        "ids_with_parts": sum(1 for r in rows if r["referenced_by_parts_declared"] > 0),
        "per_id": rows,
        "spec_links": {
            "files_for_maths_a": sl_maths,
            "anchor_id_hits_per_file": sl_hits,
            "wrong_code_hits_per_file": sl_wrong_code_hits,
        },
        "s104_question_package": {
            "consumes_resolution_or_spcpt_ids": s104_consumes,
            "note": "source-level check of scripts/s104_build_question_package.py; "
                    "the layer-3 maths-a package did not read the resolution substrate",
        },
        "kg_export_maths_a": {"artifacts": kg_maths,
                              "note": "no maths-a kg export exists; the 49-course kg fork predates subject #2"},
        "triggering_surfaces": ["C32 notes-join (Official-Specifications/parsed/_derived/notes-join/)",
                                "C40 chunk substrate (graph/igcse-maths-a/spec_chunk_mappings.yaml)"],
        "not_audited_here": ["syllabai-core / hub RAG serving", "any external downstream of the EQ corpus"],
        "read_only": True,
    }
    OUT.write_text(json.dumps(census, indent=1, ensure_ascii=False) + "\n")

    print(f"defective joins: {len(rows)}  |  declared part refs: {census['sum_referenced_by_parts_declared']}"
          f"  |  ids with parts: {census['ids_with_parts']}")
    print("spec-links maths-a files:", sl_maths, "| id hits:", sl_hits, "| wrong-code hits:", sl_wrong_code_hits)
    print("s104 consumes resolution:", s104_consumes, "| maths-a kg artifacts:", kg_maths or "none")
    print("census ->", OUT.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
