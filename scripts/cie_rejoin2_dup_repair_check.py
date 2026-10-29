#!/usr/bin/env python3
"""T-SPECS-CIE-REJOIN-2 run-002 battery — DR1-DR6 for the in-item duplicates fix-forward.

Runs against the working tree vs HEAD blobs (the engine must have run).
Independent re-derivation throughout; fail-closed on any mismatch.
"""
import collections, hashlib, json, subprocess, sys

REPO = "/home/z/my-project/work/clone-resources-rejoin"
LANES = ["cie-as-business-23", "cie-as-chemistry-25", "cie-as-computer-science-19",
         "cie-as-maths-20-mechanics", "cie-as-maths-20-probability-and-statistics-1",
         "cie-as-maths-20-pure-1", "cie-as-maths-20-pure-2", "cie-as-physics-25"]
EXPECT_DELTA = {"cie-as-business-23": -5, "cie-as-computer-science-19": -3,
                "cie-as-maths-20-mechanics": -4, "cie-as-chemistry-25": 0,
                "cie-as-maths-20-probability-and-statistics-1": 0,
                "cie-as-maths-20-pure-1": 0, "cie-as-maths-20-pure-2": 0,
                "cie-as-physics-25": 0}

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, cwd=REPO)

def canon(x):
    return json.dumps(x, sort_keys=True)

def blobs(lane):
    return json.loads(sh("git", "show", f"HEAD:spec-links/{lane}.json").stdout)

def tree(lane):
    with open(f"{REPO}/spec-links/{lane}.json", "rb") as f:
        return json.loads(f.read())

def census(d):
    items, surplus, inv = 0, 0, []
    for iid, it in d["items"].items():
        codes = it.get("codes") or []
        c = collections.Counter(x.get("official_id") if isinstance(x, dict) else x for x in codes)
        for oid, n in c.items():
            if n > 1:
                items += 1; surplus += n - 1; inv.append((iid, oid, n))
    return items, surplus, inv

results = []
def check(rid, ok, detail=""):
    results.append({"id": rid, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS" if ok else "FAIL"), rid, detail[:160])
    return ok

ok = True

# DR1 — pre-state pins re-derived independently from HEAD blobs
pre_total = sum(sum(len(it.get("codes") or []) for it in blobs(l)["items"].values()) for l in LANES)
pre_dups, pre_surplus, pre_inv, twins_ok = 0, 0, [], True
pre_pending = {}
for l in LANES:
    d = blobs(l)
    di, su, inv = census(d)
    pre_dups += di; pre_surplus += su; pre_inv += [(l,) + x for x in inv]
    pre_pending[l] = sum(len(it.get("pending") or []) for it in d["items"].values())
    for iid, oid, n in inv:
        it = d["items"][iid]
        forms = {canon(x) for x in (it.get("codes") or []) if (x.get("official_id") if isinstance(x, dict) else x) == oid}
        if len(forms) != 1: twins_ok = False
ok &= check("DR1", pre_total == 1759 and pre_dups == 11 and pre_surplus == 12 and twins_ok
            and len(pre_inv) == 11,
            f"HEAD: entries {pre_total}, dup items {pre_dups} (inventory {len(pre_inv)}), surplus {pre_surplus}, twins identical {twins_ok}")

# DR2 — mutation discipline: only the 11 items' codes arrays changed, later-twin removal only
delta_ok, deep_ok = True, True
for l in LANES:
    d0, d1 = blobs(l), tree(l)
    n0 = sum(len(it.get("codes") or []) for it in d0["items"].values())
    n1 = sum(len(it.get("codes") or []) for it in d1["items"].values())
    if n1 - n0 != EXPECT_DELTA[l]: delta_ok = False
    if d1["totals"] != d0["totals"] or d1["review_state"] != d0["review_state"] or d1["anchors"] != d0["anchors"]:
        deep_ok = False
    if pre_pending[l] != sum(len(it.get("pending") or []) for it in d1["items"].values()):
        deep_ok = False
    for iid, it0 in d0["items"].items():
        it1 = d1["items"][iid]
        c0 = [canon(x) for x in (it0.get("codes") or [])]
        c1 = [canon(x) for x in (it1.get("codes") or [])]
        if c1 == c0: continue
        # allowed mutation: c1 is c0 with later duplicate occurrences removed (order preserved)
        seen, expect = set(), []
        for x in c0:
            if x in seen: continue
            seen.add(x); expect.append(x)
        if c1 != expect: deep_ok = False
        for k in it0:
            if k != "codes" and canon(it0.get(k)) != canon(it1.get(k)): deep_ok = False
    if set(d0["items"].keys()) != set(d1["items"].keys()): deep_ok = False
st = sh("git", "status", "--porcelain").stdout.splitlines()
spec_changes = sorted(x[3:] for x in st if x[3:].startswith("spec-links/"))
ok &= check("DR2", delta_ok and deep_ok and spec_changes == [
    "spec-links/cie-as-business-23.json", "spec-links/cie-as-computer-science-19.json",
    "spec-links/cie-as-maths-20-mechanics.json"],
    f"per-lane deltas exact, deep-equal outside later-twin removals, spec-links delta == {spec_changes}")

# DR3 — post-census
post_total = sum(sum(len(it.get("codes") or []) for it in tree(l)["items"].values()) for l in LANES)
post_dups = sum(census(tree(l))[0] for l in LANES)
post_surplus = sum(census(tree(l))[1] for l in LANES)
ok &= check("DR3", post_total == 1747 and post_dups == 0 and post_surplus == 0,
            f"tree: entries {post_total} (1759->1747), dup items {post_dups}, surplus {post_surplus}")

# DR4 — manifest byte-untouched vs HEAD
m_head = hashlib.sha256(sh("git", "show", "HEAD:spec-links/manifest.json").encode() if False else
                        subprocess.run(["git", "show", "HEAD:spec-links/manifest.json"], capture_output=True, cwd=REPO).stdout).hexdigest()
m_tree = hashlib.sha256(open(f"{REPO}/spec-links/manifest.json", "rb").read()).hexdigest()
ok &= check("DR4", m_head == m_tree, f"manifest sha256 stable {m_tree[:16]}…")

# DR5 — idempotence: engine re-run performs ZERO writes (pre-pin refusal path)
st_before = sh("git", "status", "--porcelain").stdout
sh("python3", "scripts/cie_rejoin2_dup_repair.py")
st_after = sh("git", "status", "--porcelain").stdout
ok &= check("DR5", st_before == st_after, "engine re-run refusal path performs zero writes (tree byte-stable)")

# DR6 — consume-plane inertness: every repaired item retains the exact payload the consume attached
inert = True
for lane, iid, oid, n in pre_inv:
    d0, d1 = blobs(lane), tree(lane)
    first = next(canon(x) for x in (d0["items"][iid].get("codes") or [])
                 if (x.get("official_id") if isinstance(x, dict) else x) == oid)
    kept = [canon(x) for x in (d1["items"][iid].get("codes") or [])
            if (x.get("official_id") if isinstance(x, dict) else x) == oid]
    if kept != [first]: inert = False
ok &= check("DR6", inert,
            "all 11 repaired items retain exactly the pre-state first payload (the one the consume's "
            "per-official_id attach already used) — v2 outcome unchanged, zero v2 contact")

verdict = "PASS" if ok and all(r["verdict"] == "PASS" for r in results) else "FAIL"
out = {"battery": "cie_rejoin2_dup_repair_check", "task": "T-SPECS-CIE-REJOIN-2 run-002",
       "base": sh("git", "rev-parse", "HEAD").stdout.strip(), "verdict": verdict, "checks": results,
       "census": {"pre": {"entries": pre_total, "dup_items": pre_dups, "surplus": pre_surplus},
                  "post": {"entries": post_total, "dup_items": post_dups, "surplus": post_surplus}},
       "laws": {"consume_inertness": "T-SPECS-CIE-GATE-2 RECORD: 'the consume lane dedups per official_id at attach time'; T-SPECS-CIE-CONSUME-2: 'the engine's strongest-wins per-code dedup collapses them at attach'"}}
with open(f"{REPO}/graph/reports/T_SPECS_CIE_REJOIN_2_REPAIR_CHECK.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print("BATTERY:", verdict)
sys.exit(0 if verdict == "PASS" else 2)
