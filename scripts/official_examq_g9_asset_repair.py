#!/usr/bin/env python3
"""
official_examq_g9_asset_repair.py — the G9 asset-byte repair wave.

DEFECT OF RECORD (found by the G9 rendered check, 2026-10-27): crop assets in
syllabai-resources Official-ExamQuestion were pushed through the git-data API
with UTF-8 TEXT encoding instead of base64 binary — every byte >= 0x80 was
UTF-8-encoded (0x89 -> C2 89), so served PNGs start with C2 89 50 4E 47 and
Chromium (nosniff) refuses to decode them: the learner sees broken figures
corpus-wide while every URL still returns HTTP 200 (the G8 artwork audit's
"exists + 200" probe cannot see this class).

REPAIR: the corruption is a uniform latin1->UTF-8 transform, byte-exactly
reversible (decode('utf-8') -> encode('latin-1') recovers the original PNG;
proof receipt in the wave ledger entry). This tool:

  --census  fetch every unique crop asset rawUrl from the hub official bundles,
            classify valid-PNG / mojibake-PNG / undecodable, write census JSON.
  --fix     re-push every mojibake blob as a base64 binary blob, build one
            tree on a branch, open a PR with the full receipt.

The hub bundles are unaffected (they carry rawUrl references only) — no v2
change is required; the fix is repo-side bytes at the same paths.
"""
import argparse
import base64
import concurrent.futures as cf
import datetime
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
REPO = "SyllabAI/syllabai-resources"
BRANCH = "g9-asset-byte-repair"


def pat():
    return open("/home/z/my-project/.creds/gh.pat").read().strip()


def gh(path, method="GET", body=None, token=None):
    req = urllib.request.Request(
        f"https://api.github.com{path}", method=method,
        headers={"Authorization": f"Bearer {token or pat()}",
                 "Accept": "application/vnd.github+json"},
        data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def classify(raw: bytes):
    if raw.startswith(PNG_MAGIC):
        return "valid", raw
    try:
        fixed = raw.decode("utf-8").encode("latin-1")
    except Exception:
        return "undecodable", raw
    if fixed.startswith(PNG_MAGIC):
        return "mojibake", fixed
    return "undecodable", raw


def unique_asset_urls(bundles_dir: Path):
    urls = {}
    for f in bundles_dir.glob("*/official-papers.json"):
        course = f.parent.name
        for t in json.loads(f.read_text()):
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for a in p.get("assets") or []:
                        if a.get("kind") == "crop" and a.get("rawUrl"):
                            urls.setdefault(a["rawUrl"], {"course": course, "path": a.get("path")})
    return urls


def fetch_bytes(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundles-dir", required=True)
    ap.add_argument("--work-dir", required=True)
    ap.add_argument("--mode", choices=["census", "fix"], required=True)
    ap.add_argument("--limit", type=int, default=0, help="cap assets (0 = all)")
    args = ap.parse_args()

    work = Path(args.work_dir)
    work.mkdir(parents=True, exist_ok=True)
    urls = unique_asset_urls(Path(args.bundles_dir))
    if args.limit:
        urls = dict(list(urls.items())[: args.limit])
    print(f"unique crop assets across lanes: {len(urls)}")

    census_path = work / "asset-byte-census.json"
    if census_path.exists():
        census = json.loads(census_path.read_text())
    else:
        census = {}

    todo = {u: m for u, m in urls.items() if u not in census}
    print(f"to classify: {len(todo)}")

    def probe(item):
        u, meta = item
        try:
            raw = fetch_bytes(u)
            cls, fixed = classify(raw)
            return u, {"course": meta["course"], "path": meta["path"],
                       "served_bytes": len(raw), "class": cls,
                       "fixed_bytes": len(fixed) if cls == "mojibake" else 0,
                       "fixed_sha256": __import__("hashlib").sha256(fixed).hexdigest() if cls == "mojibake" else None}
        except Exception as exc:
            return u, {"course": meta["course"], "path": meta["path"], "class": f"fetch-error: {exc}"}

    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        for i, (u, rec) in enumerate(ex.map(probe, todo.items())):
            census[u] = rec
            if (i + 1) % 50 == 0:
                print(f"  classified {i+1}/{len(todo)}")
    census_path.write_text(json.dumps(census, indent=0))
    from collections import Counter
    counts = Counter(r.get("class", "?") for r in census.values())
    print("census:", dict(counts))
    if args.mode == "census":
        per_lane = {}
        for r in census.values():
            k = (r.get("course"), r.get("class"))
            per_lane[k] = per_lane.get(k, 0) + 1
        for k in sorted(per_lane):
            print("  ", k, per_lane[k])
        return

    # ---- fix mode: push corrected blobs, one tree, one commit, one PR -------
    bad = {u: r for u, r in census.items() if r.get("class") == "mojibake"}
    if not bad:
        print("nothing to fix — all assets valid")
        return
    token = pat()
    print(f"uploading {len(bad)} corrected blobs...")
    blobs = {}

    def upload(item):
        u, rec = item
        fixed = fetch_bytes(u).decode("utf-8").encode("latin-1")
        b = gh(f"/repos/{REPO}/git/blobs", "POST",
               {"content": base64.b64encode(fixed).decode(), "encoding": "base64"}, token=token)
        return u, b["sha"]

    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for i, (u, sha) in enumerate(ex.map(upload, bad.items())):
            blobs[u] = sha
            if (i + 1) % 50 == 0:
                print(f"  blobs {i+1}/{len(bad)}")

    base = gh(f"/repos/{REPO}/git/ref/heads/main")
    base_commit = gh(f"/repos/{REPO}/git/commits/{base['object']['sha']}")
    tree_entries = [{"path": r["path"], "mode": "100644", "type": "blob", "sha": blobs[u]}
                    for u, r in bad.items()]
    print(f"building tree with {len(tree_entries)} entries on base {base_commit['sha'][:10]}")
    tree = gh(f"/repos/{REPO}/git/trees", "POST",
              {"base_tree": base_commit["tree"]["sha"], "tree": tree_entries}, token=token)
    msg = ("G9 asset-byte repair: re-push %d mojibake crop PNGs as binary blobs\n\n"
           "Found by the G9 learner-surface rendered check: crop assets pushed via the\n"
           "git-data API with UTF-8 text encoding instead of base64 binary — every byte\n"
           ">= 0x80 was UTF-8-encoded (89 -> C2 89), so served PNGs start C2 89 50 4E 47\n"
           "and Chromium (nosniff) refuses them: broken figures corpus-wide while every\n"
           "URL still returns HTTP 200.\n\n"
           "Repair: uniform latin1->UTF-8 transform, byte-exactly reversible; every blob\n"
           "re-pushed as base64 after decode-verify (PNG magic). Census + per-blob sha256\n"
           "receipt in the wave ledger (F104)." % len(bad))
    commit = gh(f"/repos/{REPO}/git/commits", "POST",
                {"message": msg, "tree": tree["sha"], "parents": [base_commit["sha"]]}, token=token)
    gh(f"/repos/{REPO}/git/refs", "POST", {"ref": f"refs/heads/{BRANCH}", "sha": commit["sha"]}, token=token)
    body = {
        "receipt_schema": "syllabai.g9-asset-repair-receipt/0.1",
        "defect": "crop PNGs pushed as UTF-8 text blobs (git-data API); served bytes start C2 89 50 4E 47; Chromium nosniff refuses decode -> corpus-wide broken figures at HTTP 200",
        "evidence": "G9 rendered check images-loaded FAIL on physics-2p-2023-06; served asset_2_b_iii_graph.png = 56,770 B mojibake; utf8-decode -> 37,343 B valid PNG (977x572); local corpus copies valid (parity staging)",
        "repaired_assets": len(bad),
        "per_lane": dict(sorted(((k, sum(1 for r in bad.values() if r['course'] == k)) for k in {r['course'] for r in bad.values()}))),
        "fixed_sha256_map": work.name + "/asset-byte-census.json",
        "validator": "official_examq_g9_asset_repair.py",
        "date_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    pr = gh(f"/repos/{REPO}/pulls", "POST", {
        "title": f"G9 asset-byte repair: {len(bad)} mojibake crop PNGs re-pushed as binary (found by the G9 rendered check)",
        "head": BRANCH, "base": "main",
        "body": "```json\n" + json.dumps(body, indent=1) + "\n```\n\n"
                "G9 learner-surface rendered check caught the class the exists+200 probes cannot see: "
                "every non-ASCII byte of the crop PNGs was UTF-8-encoded at push time. The transform is "
                "byte-exactly reversible; each blob here is re-pushed as base64 after decode-verify "
                "(PNG magic). No path/URL changes; hub bundles reference the same rawUrls and need no change.",
    }, token=token)
    print(f"PR opened: {pr['number']} {pr['html_url']}")
    (work / "asset-repair-pr.json").write_text(json.dumps(pr, indent=1))


if __name__ == "__main__":
    main()
