#!/usr/bin/env python3
"""T-MG-QB-1 run-001 — bulk-commit the corpus + scripts + governance files via the Git Data API."""
import base64, json, os, sys, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/home/z/my-project/scripts")
import gh_api

WORK = "/home/z/my-project/mg_work"
CORPUS = f"{WORK}/corpus"
BR = "t-mg-qb-1/run-001"
MSG = ("T-MG-QB-1 run-001 — gcse-maths-edexcel per-topic question bank: 133/134 topics, "
       "1,666 questions + per-page solution scans (no paper PDFs per operator decision 2026-11-07); "
       "extractor scripts, manifest, INDEX, receipt, LEDGER wave 25, LICENSE addendum")

SCRIPT_MAP = {
    "scripts/mg/flight_decode.py": "scripts/mg_flight_decode.py",
    "scripts/mg/fetch_catalog.py": "scripts/mg_fetch_catalog.py",
    "scripts/mg/probe_pdf.py": "scripts/mg_probe_pdf.py",
    "scripts/mg/qb_extract.py": "scripts/mg_qb_extract.py",
    "scripts/mg/mg_manifest.py": "scripts/mg_manifest.py",
    "scripts/mg/upload.py": "scripts/mg_upload.py",
}


def build_file_map():
    files = {}
    files["MG-QuestionBank/README.md"] = f"{WORK}/MG-QuestionBank-README.new.md"
    files["LICENSE-DATA.md"] = f"{WORK}/LICENSE.new.md"
    files["LEDGER.md"] = f"{WORK}/LEDGER.new.md"
    for src, dst in SCRIPT_MAP.items():
        p = f"/home/z/my-project/{src}"
        if os.path.exists(p):
            files[dst] = p
    for root, _, fns in os.walk(CORPUS):
        for fn in fns:
            lp = os.path.join(root, fn)
            rp = os.path.relpath(lp, CORPUS)
            files[f"MG-QuestionBank/{rp}"] = lp
    return files


def main():
    files = build_file_map()
    total_bytes = sum(os.path.getsize(p) for p in files.values())
    print(f"files: {len(files)} | {total_bytes/1e6:.1f} MB")

    br = gh_api.get_branch(BR)
    head_sha = br["commit"]["sha"]
    base_tree = br["commit"]["commit"]["tree"]["sha"]
    print(f"branch head {head_sha[:12]} tree {base_tree[:12]}")

    entries_path = f"{WORK}/logs/upload_entries.json"
    done_path = f"{WORK}/logs/upload_blobs_done.json"
    saved_map = None
    if os.path.exists(entries_path):
        saved = json.load(open(entries_path))
        saved_map = {e["path"]: e["sha"] for e in saved}
        if set(saved_map) != set(files):
            saved_map = None
    elif os.path.exists(done_path):
        saved_map = json.load(open(done_path))
        if set(saved_map) != set(files):
            # partial checkpoint: keep only paths still present
            saved_map = {k: v for k, v in saved_map.items() if k in files}
    print(f"checkpoint: {len(saved_map or {})} blobs already created")

    # 1) blobs
    entries = []
    def make_blob(rp, lp):
        if saved_map is not None:
            return {"path": rp, "mode": "100644", "type": "blob", "sha": saved_map[rp]}
        data = open(lp, "rb").read()
        r = gh_api.post(gh_api.api("git/blobs"), {"content": base64.b64encode(data).decode(), "encoding": "base64"})
        return {"path": rp, "mode": "100644", "type": "blob", "sha": r["sha"]}

    done = 0
    remaining = {rp: lp for rp, lp in sorted(files.items()) if rp not in (saved_map or {})}
    print(f"blobs to create: {len(remaining)}")
    with ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(make_blob, rp, lp): rp for rp, lp in remaining.items()}
        for fu in as_completed(futs):
            e = fu.result()
            entries.append(e)
            (saved_map or {}).setdefault(e["path"], e["sha"])
            done += 1
            if done % 300 == 0:
                json.dump(saved_map, open(done_path, "w"))
                print(f"  blobs {done}/{len(remaining)} (checkpointed)", flush=True)
    json.dump(saved_map, open(done_path, "w"))
    entries = sorted(({"path": rp, "mode": "100644", "type": "blob", "sha": sha} for rp, sha in saved_map.items()), key=lambda x: x["path"])
    print(f"blobs ready: {len(entries)}", flush=True)
    json.dump(entries, open(entries_path, "w"))

    # 2) trees in chunks (with bisect on failure)
    tree_sha = base_tree
    CHUNK = 600
    idx = 0
    chunk_no = 0
    while idx < len(entries):
        chunk = entries[idx:idx + CHUNK]
        try:
            r = gh_api.post(gh_api.api("git/trees"), {"base_tree": tree_sha, "tree": chunk})
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:500]
            print(f"  tree chunk {chunk_no} FAILED ({e.code}): {body}")
            if len(chunk) > 1:
                # bisect: push halves individually to find bad entries
                for half in (chunk[:len(chunk)//2], chunk[len(chunk)//2:]):
                    try:
                        r = gh_api.post(gh_api.api("git/trees"), {"base_tree": tree_sha, "tree": half})
                        tree_sha = r["sha"]
                        print(f"    bisect half ok ({len(half)} entries)")
                    except urllib.error.HTTPError as e2:
                        bad = [x["path"] for x in half]
                        print(f"    bisect half FAILED too: {e2.code} {e2.read().decode()[:300]}")
                        print(f"    suspect paths: {bad[:10]}")
                        raise SystemExit(1)
                idx += len(chunk); chunk_no += 1
                continue
            raise
        tree_sha = r["sha"]
        idx += len(chunk); chunk_no += 1
        print(f"  tree chunk {chunk_no}: {len(chunk)} entries -> {tree_sha[:12]}")

    # 3) commit
    c = gh_api.post(gh_api.api("git/commits"), {"message": MSG, "tree": tree_sha, "parents": [head_sha]})
    commit_sha = c["sha"]
    print(f"commit {commit_sha[:12]}")

    # 4) update ref
    gh_api.patch(gh_api.api(f"git/refs/heads/{BR}"), {"sha": commit_sha, "force": False})
    print("ref updated:", BR, "->", commit_sha[:12])


if __name__ == "__main__":
    main()
