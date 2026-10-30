#!/usr/bin/env python3
"""SIB-ASSESS-r3-silver — legs 6b/7/8: per-run red-state code counts (all shapes),
pastpapers pinned-file sha256 verification at live tip, resources pinned-file
sha256 verification at tip."""
import json, re, os, glob, hashlib, collections

LIB = "/home/z/my-project/syllabai-resources/SubjectIntelligence/CHEMISTRY_4CH1"
RES = "/home/z/my-project/syllabai-resources"
PP = "/home/z/my-project/syllabai-pastpapers"
OUT = os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-ASSESS-R3")

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()

# ---- L6b: per-run issue-code counts across ALL scoreboard shapes ----
claim = {"SIB-MANI-007": 88, "SIB-MANI-011": 4, "SIB-MANI-012": 7}
per_run = {}
for rn in range(17, 23):
    p = os.path.join(LIB, "runs", f"SIB-CHEMISTRY_4CH1-RUN-{rn:03d}",
                     "post_lifecycle_scoreboard.json")
    j = json.load(open(p))
    codes = collections.Counter()
    if isinstance(j.get("issues"), list):          # RUN-017/020 full-issue shape
        for it in j["issues"]:
            codes[it.get("code", "?")] += 1
    for key in ("issue_counts", "codes_observed"):  # distilled shapes
        if isinstance(j.get(key), dict):
            for k, v in j[key].items():
                codes[k] += int(v)
    per_run[f"RUN-{rn:03d}"] = dict(codes)
l6b_ok = all(c == claim for c in per_run.values())

# ---- L7: pastpapers pinned-file sha256 at live tip ----
pins = {}   # (repo,path) -> set of sha256 across all packs
for pf in glob.glob(os.path.join(LIB, "runs", "*", "evidence", "*", "evidence_pack.json")):
    try:
        j = json.load(open(pf))
    except Exception:
        continue
    for s in j.get("sources", []):
        for f in s.get("files", []):
            pins.setdefault((f.get("repo", "syllabai-resources"), f["path"]),
                            set()).add(f.get("sha256"))
pp_rows, pp_ok, pp_missing = [], 0, []
for (repo, path), shas in sorted(pins.items()):
    if repo != "syllabai-pastpapers":
        continue
    p = os.path.join(PP, path)
    if not os.path.exists(p):
        pp_missing.append(path)
        pp_rows.append({"path": path, "present": False})
        continue
    got = sha256_file(p)
    ok = got in shas
    pp_ok += ok
    pp_rows.append({"path": path, "present": True, "sha_match": ok,
                    "pinned": sorted(x[:12] for x in shas), "at_tip": got[:12]})

# ---- L8: resources pinned-file sha256 at tip (worktree or cat-file) ----
res_rows, res_ok, res_missing = [], 0, []
for (repo, path), shas in sorted(pins.items()):
    if repo != "syllabai-resources":
        continue
    p = os.path.join(RES, path)
    if os.path.exists(p):
        got = sha256_file(p)
    else:
        r = subprocess_run = __import__("subprocess").run(
            ["git", "cat-file", "blob", f"HEAD:{path}"], cwd=RES,
            capture_output=True, timeout=600)
        got = sha256_bytes(r.stdout) if r.returncode == 0 else None
    if got is None:
        res_missing.append(path)
        res_rows.append({"path": path, "present": False})
        continue
    ok = got in shas
    res_ok += ok
    res_rows.append({"path": path, "sha_match": ok,
                     "pinned": sorted(x[:12] for x in shas), "at_tip": got[:12]})

receipt = {
    "L6b_per_run_issue_codes": {"per_run": per_run, "all_match_F4a_claim": l6b_ok,
                                "claim": claim},
    "L7_pastpapers_pins": {"distinct_paths": len([1 for (r, _) in pins if r == "syllabai-pastpapers"]),
                           "present": len(pp_rows) - len(pp_missing),
                           "sha_match": pp_ok, "missing": pp_missing,
                           "mismatches": [r for r in pp_rows if r.get("present") and not r["sha_match"]]},
    "L8_resources_pins": {"distinct_paths": len([1 for (r, _) in pins if r == "syllabai-resources"]),
                          "present": len(res_rows) - len(res_missing),
                          "sha_match": res_ok, "missing": res_missing,
                          "mismatches": [r for r in res_rows if r.get("present") and not r["sha_match"]],
                          "rows": res_rows},
}
json.dump(receipt, open(os.path.join(OUT, "pins_receipt.json"), "w"), indent=1)
print("L6b per-run codes all match F4a claim:", l6b_ok)
print("L7 pastpapers: distinct", receipt["L7_pastpapers_pins"]["distinct_paths"],
      "present", receipt["L7_pastpapers_pins"]["present"],
      "sha_match", pp_ok, "missing", len(pp_missing),
      "mismatch", len(receipt["L7_pastpapers_pins"]["mismatches"]))
print("L8 resources: distinct", receipt["L8_resources_pins"]["distinct_paths"],
      "present", receipt["L8_resources_pins"]["present"],
      "sha_match", res_ok, "missing", len(res_missing),
      "mismatch", len(receipt["L8_resources_pins"]["mismatches"]))
for r in receipt["L8_resources_pins"]["mismatches"][:8]:
    print("  RES-MISMATCH:", r["path"][:80], "pinned", r["pinned"], "tip", r["at_tip"])
for r in receipt["L7_pastpapers_pins"]["mismatches"][:8]:
    print("  PP-MISMATCH:", r["path"][:80], "pinned", r["pinned"], "tip", r["at_tip"])
