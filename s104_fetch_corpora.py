#!/usr/bin/env python3
"""Session 104: fetch the full SME EQ + RevisionNotes igcse-chemistry-19 corpora
from github.com/SyllabAI/syllabai-resources (repo too big to clone) via raw fetches.

Outputs to /home/z/my-project/work/sme-igcse-corpus/
  eq/   <- SME-ExamQuestion/igcse-chemistry-19   (topic.json per topic + spec files)
  rn/   <- SME-RevisionNotes/igcse-chemistry-19  (page .json/.md + index files)
"""
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = "SyllabAI/syllabai-resources"
BRANCH = "main"
BASE = Path("/home/z/my-project/work/sme-igcse-corpus")
TOKEN = None

def get_token():
    global TOKEN
    if TOKEN:
        return TOKEN
    url = subprocess.run(["git", "-C", "/home/z/my-project/work/syllabai-resources",
                          "config", "--get", "remote.origin.url"],
                         capture_output=True, text=True).stdout.strip()
    TOKEN = re.search(r"x-access-token:([^@]+)@", url).group(1)
    return TOKEN

def api(path):
    """GitHub API listing (directory contents)."""
    tok = get_token()
    for attempt in range(4):
        r = subprocess.run(["curl", "-s", "-H", f"Authorization: token {tok}",
                            f"https://api.github.com/repos/{REPO}/contents/{path}"],
                           capture_output=True, text=True)
        try:
            d = json.loads(r.stdout)
        except json.JSONDecodeError:
            d = None
        if isinstance(d, list):
            return d
        if isinstance(d, dict) and d.get("message", "").startswith("API rate limit"):
            time.sleep(20)
            continue
        break
    print(f"  !! API listing failed for {path}", file=sys.stderr)
    return None

def raw(path, dest):
    """Fetch a raw file."""
    tok = get_token()
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{path}"
    r = subprocess.run(["curl", "-s", "-L", "-H", f"Authorization: token {tok}",
                        "-w", "%{http_code}", url, "-o", str(dest)],
                       capture_output=True, text=True)
    code = r.stdout.strip() if r.stdout else "000"
    if code != "200":
        print(f"  !! HTTP {code} for {path}", file=sys.stderr)
        return False
    return True

def walk_dir(rel, dest, exts=None, max_files=2000):
    """Recursively fetch a remote directory."""
    n = 0
    listing = api(rel)
    if listing is None:
        return 0
    for entry in listing:
        if n >= max_files:
            break
        name, etype = entry["name"], entry["type"]
        if etype == "dir":
            n += walk_dir(f"{rel}/{name}", dest / name, exts, max_files - n)
        elif exts is None or any(name.endswith(e) for e in exts):
            if raw(f"{rel}/{name}", dest / name):
                n += 1
    return n

def main():
    BASE.mkdir(parents=True, exist_ok=True)

    # ---- EQ course root files ----
    eq_root = "SME-ExamQuestion/igcse-chemistry-19"
    eq = BASE / "eq"
    eq.mkdir(exist_ok=True)
    for f in ["manifest.json", "spec_point_index.json", "spec_point_resolution.json",
              "spec_point_map.json", "VALIDATION.md", "README.md"]:
        ok = raw(f"{eq_root}/{f}", eq / f)
        print(f"eq/{f}: {'ok' if ok else 'MISSING'}")

    # topic.json files via manifest topics[] (avoids walking assets/)
    man = json.load(open(eq / "manifest.json"))
    n_topics = 0
    for t in man.get("topics", []):
        sec, top = t["section_slug"], t.get("topic_slug") or t.get("slug")
        if not top:
            continue
        ok = raw(f"{eq_root}/{sec}/{top}/topic.json",
                 eq / "sections" / sec / top / "topic.json")
        n_topics += 1 if ok else 0
    print(f"eq topic.json fetched: {n_topics}/{len(man.get('topics', []))}")

    # ---- RN course ----
    rn_root = "SME-RevisionNotes/igcse-chemistry-19"
    rn = BASE / "rn"
    # root listing first to discover structure
    root_ls = api(rn_root)
    if root_ls is None:
        print("RN root listing failed — trying common file names")
    else:
        print("RN root:", [(e["type"], e["name"]) for e in root_ls][:20])
    # fetch root files (manifest/index) then walk .json only (skip .md for now)
    for entry in (root_ls or []):
        if entry["type"] == "file" and entry["name"].endswith(".json"):
            raw(f"{rn_root}/{entry['name']}", rn / entry["name"])
            print(f"rn/{entry['name']}: ok")
    n = walk_dir(rn_root, rn, exts=[".json"])
    print(f"rn .json files fetched: {n}")

if __name__ == "__main__":
    main()
