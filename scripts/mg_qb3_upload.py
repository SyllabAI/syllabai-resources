#!/usr/bin/env python3
"""T-MG-QB-3 run-001 — bulk-commit the a-level-maths-edexcel lane + scripts +
governance files via the Git Data API (adapted from the T-MG-QB-2 uploader).

Scoped to the NEW lane only (gcse/igcse lanes already live on main)."""
import base64
import json
import os
import sys
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/home/z/my-project/scripts")
import gh_api  # noqa: E402

WORK = "/home/z/my-project/mg_work"
CORPUS = f"{WORK}/corpus/MG-QuestionBank/a-level-maths-edexcel"
RECEIPT = f"{WORK}/corpus/MG-QuestionBank/T-MG-QB-3-run-001-RECEIPT.json"
BR = "t-mg-qb-3/run-001"
BASE_BRANCH = "main"
MSG = ("T-MG-QB-3 run-001 — a-level-maths-edexcel per-chapter question-set bank: 44/44 chapters, "
       "913 questions / 5,323 printed marks + per-page solution scans, zero PDFs stored "
       "(operator decision 2026-11-07); total-line segmentation law (numbers embedded in "
       "display-math; leading anchors unreliable in this lane) with 3 source typos + 1 numbering "
       "gap recorded; 9 question PDFs via site's own naming convention (HEAD-200, discovery "
       "provenance); AS-lane overlap dedup decision; manifest, INDEX, receipt, README coverage "
       "row, LEDGER wave 27")

LOCAL = "/home/z/my-project/scripts/mg_qb3_work"
SCRIPT_MAP = {
    f"{LOCAL}/mg_qb3_catalog.py": "scripts/mg_qb3_catalog.py",
    f"{LOCAL}/mg_qb3_extract.py": "scripts/mg_qb3_extract.py",
    f"{LOCAL}/mg_qb3_manifest.py": "scripts/mg_qb3_manifest.py",
    f"{LOCAL}/mg_qb3_upload.py": "scripts/mg_qb3_upload.py",
    f"{LOCAL}/mg_qb3_gov.py": "scripts/mg_qb3_gov.py",
    "/home/z/my-project/scripts/gh_api.py": "scripts/gh_api.py",
}

EVIDENCE = {
    "scripts/mg_qb3_run001/catalog_log.json": f"{WORK}/logs/qb3_catalog_log.json",
    "scripts/mg_qb3_run001/extract_results.json": f"{WORK}/logs/qb3_extract_results.json",
}


def build_file_map():
    files = {}
    files["MG-QuestionBank/README.md"] = f"{WORK}/QB-README.new.md"
    files["LEDGER.md"] = f"{WORK}/LEDGER.new.md"
    files["MG-QuestionBank/T-MG-QB-3-run-001-RECEIPT.json"] = RECEIPT
    for src, dst in SCRIPT_MAP.items():
        if os.path.exists(src):
            files[dst] = src
        else:
            raise SystemExit(f"missing script {src}")
    for rp, lp in EVIDENCE.items():
        files[rp] = lp
    for root, _, fns in os.walk(CORPUS):
        for fn in fns:
            lp = os.path.join(root, fn)
            rp = os.path.relpath(lp, CORPUS)
            files[f"MG-QuestionBank/a-level-maths-edexcel/{rp}"] = lp
    return files


def main():
    files = build_file_map()
    total_bytes = sum(os.path.getsize(p) for p in files.values())
    print(f"files: {len(files)} | {total_bytes/1e6:.1f} MB")

    # 0) ensure branch exists at current main
    main_sha = gh_api.get_branch(BASE_BRANCH)["commit"]["sha"]
    try:
        br = gh_api.get_branch(BR)
        print(f"branch exists at {br['commit']['sha'][:12]}")
    except urllib.error.HTTPError:
        gh_api.post("git/refs", {"ref": f"refs/heads/{BR}", "sha": main_sha})
        br = gh_api.get_branch(BR)
        print(f"branch created from main {main_sha[:12]}")
    head_sha = br["commit"]["sha"]
    base_tree = br["commit"]["commit"]["tree"]["sha"]

    entries_path = f"{WORK}/logs/qb3_upload_entries.json"
    done_path = f"{WORK}/logs/qb3_upload_blobs_done.json"
    saved_map = None
    if os.path.exists(entries_path):
        saved = json.load(open(entries_path))
        saved_map = {e["path"]: e["sha"] for e in saved}
        if set(saved_map) != set(files):
            saved_map = None
    elif os.path.exists(done_path):
        saved_map = json.load(open(done_path)) or None
        if saved_map is not None and set(saved_map) != set(files):
            saved_map = {k: v for k, v in saved_map.items() if k in files}
    if saved_map is None:
        saved_map = {}
    print(f"checkpoint: {len(saved_map)} blobs already created")

    # 1) blobs
    def make_blob(rp, lp):
        sha = saved_map.get(rp)
        if sha:
            return {"path": rp, "mode": "100644", "type": "blob", "sha": sha}
        data = open(lp, "rb").read()
        r = gh_api.post("git/blobs", {"content": base64.b64encode(data).decode(), "encoding": "base64"})
        return {"path": rp, "mode": "100644", "type": "blob", "sha": r["sha"]}

    remaining = {rp: lp for rp, lp in sorted(files.items()) if rp not in saved_map}
    print(f"blobs to create: {len(remaining)}")
    done = 0
    with ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(make_blob, rp, lp): rp for rp, lp in remaining.items()}
        for fu in as_completed(futs):
            e = fu.result()
            saved_map[e["path"]] = e["sha"]
            done += 1
            if done % 400 == 0:
                json.dump(saved_map, open(done_path, "w"))
                print(f"  blobs {done}/{len(remaining)} (checkpointed)", flush=True)
    json.dump(saved_map, open(done_path, "w"))
    entries = sorted(({"path": rp, "mode": "100644", "type": "blob", "sha": sha}
                      for rp, sha in saved_map.items()), key=lambda x: x["path"])
    print(f"blobs ready: {len(entries)}", flush=True)
    json.dump(entries, open(entries_path, "w"))

    # 2) trees in chunks (bisect on failure)
    tree_sha = base_tree
    CHUNK = 600
    idx = 0
    chunk_no = 0
    while idx < len(entries):
        chunk = entries[idx:idx + CHUNK]
        try:
            r = gh_api.post("git/trees", {"base_tree": tree_sha, "tree": chunk})
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:500]
            print(f"  tree chunk {chunk_no} FAILED ({e.code}): {body}")
            if len(chunk) > 1:
                for half in (chunk[:len(chunk)//2], chunk[len(chunk)//2:]):
                    try:
                        r = gh_api.post("git/trees", {"base_tree": tree_sha, "tree": half})
                        tree_sha = r["sha"]
                        print(f"    bisect half ok ({len(half)} entries)")
                    except urllib.error.HTTPError as e2:
                        print(f"    bisect half FAILED too: {e2.code} {e2.read().decode()[:300]}")
                        raise SystemExit(1)
                idx += len(chunk); chunk_no += 1
                continue
            raise
        tree_sha = r["sha"]
        idx += len(chunk); chunk_no += 1
        print(f"  tree chunk {chunk_no}: {len(chunk)} entries -> {tree_sha[:12]}")

    # 3) commit
    c = gh_api.post("git/commits", {"message": MSG, "tree": tree_sha, "parents": [head_sha]})
    commit_sha = c["sha"]
    print(f"commit {commit_sha[:12]}")

    # 4) update ref
    gh_api.patch(f"git/refs/heads/{BR}", {"sha": commit_sha, "force": False})
    print("ref updated:", BR, "->", commit_sha[:12])


if __name__ == "__main__":
    main()
