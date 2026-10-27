#!/usr/bin/env python3
"""Corrective commit for the G9 asset repair: move the 31 misplaced root
assets/ blobs to their true slice paths (fresh blobs, collision-safe) and
delete the stray root files added by 4a10484a99."""
import base64, json, urllib.request, concurrent.futures as cf

REPO = "SyllabAI/syllabai-resources"
TOK = open("/home/z/my-project/.creds/gh.pat").read().strip()

def gh(path, method="GET", body=None):
    req = urllib.request.Request(f"https://api.github.com{path}", method=method,
        headers={"Authorization": f"Bearer {TOK}", "Accept": "application/vnd.github+json"},
        data=json.dumps(body).encode() if body else None)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"gh {method} {path} -> {e.code}: {e.read().decode()[:500]}") from None

census = json.load(open("/home/z/my-project/g8/asset-repair/asset-byte-census.json"))
bad = {u: r for u, r in census.items() if r.get("class") == "mojibake"}
# full target path from the rawUrl
def full_path(u):
    return u.split("raw.githubusercontent.com/SyllabAI/syllabai-resources/main/")[1]

targets = {full_path(u): r for u, r in bad.items()}
print(f"targets: {len(targets)}")

# pre-existing root files (not mine to touch)
root = gh(f"/repos/{REPO}/contents/assets")
root_names = {x["name"] for x in root}
mine = {p.rsplit("/", 1)[1] for p in targets}
strays = [f"assets/{n}" for n in (root_names & mine)]
pre_existing = root_names - mine
print(f"strays to delete: {len(strays)}; pre-existing root files kept: {sorted(pre_existing)}")

def upload(item):
    full, rec = item
    u = [k for k, v in bad.items() if v is rec][0]
    fixed = urllib.request.urlopen(u, timeout=60).read().decode("utf-8").encode("latin-1")
    assert fixed.startswith(b"\x89PNG"), full
    b = gh(f"/repos/{REPO}/git/blobs", "POST", {"content": base64.b64encode(fixed).decode(), "encoding": "base64"})
    return full, b["sha"]

entries = []
stray_names = set()
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    for full, sha in ex.map(upload, list(targets.items())):
        entries.append({"path": full, "mode": "100644", "type": "blob", "sha": sha})
        stray_names.add(f"assets/{full.rsplit('/', 1)[1]}")  # dedupe: two slices share a name
for s in sorted(stray_names):
    entries.append({"path": s, "mode": "100644", "type": "blob", "sha": None})  # delete stray
print(f"tree entries: {len(entries)}")

ref = gh(f"/repos/{REPO}/git/ref/heads/main")
c = gh(f"/repos/{REPO}/git/commits/{ref['object']['sha']}")
tree = gh(f"/repos/{REPO}/git/trees", "POST", {"base_tree": c["tree"]["sha"], "tree": entries})
nc = gh(f"/repos/{REPO}/git/commits", "POST", {
    "message": "G9 asset repair correction: move the 31 re-pushed PNGs to their slice paths; delete the stray root assets/\n\n"
               "4a10484a99 uploaded the corrected blobs with census-relative paths (assets/<name>.png), which\n"
               "created a stray repo-root assets/ dir (two name collisions collapsed distinct slices' files)\n"
               "instead of updating the slice paths of record. This commit re-uploads every corrected blob\n"
               "(decode-verified PNG magic) at the FULL paths referenced by the hub bundles and removes the\n"
               "31 stray root files (pre-existing root assets/ files untouched).",
    "tree": tree["sha"], "parents": [c["sha"]]})
branch = gh(f"/repos/{REPO}/git/refs", "POST", {"ref": "refs/heads/g9-asset-repair-correction", "sha": nc["sha"]})
pr = gh(f"/repos/{REPO}/pulls", "POST", {
    "title": "G9 asset repair correction: slice paths of record for the 31 re-pushed PNGs; stray root assets/ removed",
    "head": "g9-asset-repair-correction", "base": "main",
    "body": ("Follows #187. The repair blobs were uploaded with census-relative paths and landed at a "
             "repo-root `assets/` dir (wrong; 2 filename collisions). This PR re-uploads all 31 corrected "
             "blobs (decode-verified PNG magic) at the full paths the hub bundles reference and deletes the "
             "31 stray root files. Pre-existing root `assets/` files are untouched. No content changes vs "
             "#187's intended bytes; path placement only.")})
print(f"correction PR: {pr['number']} {pr['html_url']}")
