#!/usr/bin/env python3
"""T-SPECS-CIE-REJOIN-2 run-002 — the inherited in-item duplicates fix-forward.

The REJOIN-2 cascade appended the same code entry twice to 11 items across
3 wave-2 AS sidecars (byte-identical twins, tier/method identical). Disclosed
of record at T-SPECS-CIE-GATE-2 ("the 11 inherited duplicates still pinned —
a sidecar-side repair remains the rejoin owners' one-line fix-forward") and
verified INERT at the consume plane by T-SPECS-CIE-CONSUME-2 ("the engine's
strongest-wins per-code dedup collapses them at attach").

This engine dedupes at source, order-preserving first-wins (the kept entry IS
the original landing payload; provenance preserved per resources AGENT.md 4).
Fail-closed: every pre-pin must hold EXACTLY or the engine refuses to write.
Deterministic: post-state has zero in-item duplicates, so a re-run is a no-op.

Laws honoured: no manifest change (verified counter-free for code entries),
no sidecar totals change (they count items, not entries), no v2 contact.
"""
import collections, hashlib, json, subprocess, sys

REPO = "/home/z/my-project/work/clone-resources-rejoin"
LANES = ["cie-as-business-23", "cie-as-chemistry-25", "cie-as-computer-science-19",
         "cie-as-maths-20-mechanics", "cie-as-maths-20-probability-and-statistics-1",
         "cie-as-maths-20-pure-1", "cie-as-maths-20-pure-2", "cie-as-physics-25"]
EXPECTED_DUP_ITEMS = 11
EXPECTED_SURPLUS = 12
EXPECTED_TOTAL_PRE = 1759
EXPECTED_TOTAL_POST = 1747
EXPECTED_PENDING = {"cie-as-business-23": 710, "cie-as-chemistry-25": 2006,
                    "cie-as-computer-science-19": 660, "cie-as-maths-20-mechanics": 668,
                    "cie-as-maths-20-probability-and-statistics-1": 841,
                    "cie-as-maths-20-pure-1": 1624, "cie-as-maths-20-pure-2": 1099,
                    "cie-as-physics-25": 1534}
EXPECTED_DELTAS = {"cie-as-business-23": -5, "cie-as-computer-science-19": -3,
                   "cie-as-maths-20-mechanics": -4, "cie-as-chemistry-25": 0,
                   "cie-as-maths-20-probability-and-statistics-1": 0,
                   "cie-as-maths-20-pure-1": 0, "cie-as-maths-20-pure-2": 0,
                   "cie-as-physics-25": 0}

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, cwd=REPO)

def head_sha():
    return sh("git", "rev-parse", "HEAD").stdout.strip()

def canon(x):
    return json.dumps(x, sort_keys=True)

def load(lane):
    with open(f"{REPO}/spec-links/{lane}.json", "rb") as f:
        return json.loads(f.read())

def census(d):
    dup_items, surplus, inventory = 0, 0, []
    for iid, it in d["items"].items():
        codes = it.get("codes") or []
        c = collections.Counter(x.get("official_id") if isinstance(x, dict) else x for x in codes)
        for oid, n in c.items():
            if n > 1:
                dup_items += 1
                surplus += n - 1
                inventory.append((iid, oid, n))
    return dup_items, surplus, inventory

def main():
    head = head_sha()
    print("HEAD pin:", head)
    pre_total, pre_dups, pre_surplus = 0, 0, 0
    pin_fail = []
    for lane in LANES:
        d = load(lane)
        n = sum(len(it.get("codes") or []) for it in d["items"].values())
        pre_total += n
        di, su, inv = census(d)
        pre_dups += di
        pre_surplus += su
        p = sum(len(it.get("pending") or []) for it in d["items"].values())
        if p != EXPECTED_PENDING[lane]:
            pin_fail.append(f"{lane} pending {p} != {EXPECTED_PENDING[lane]}")
    if pre_total != EXPECTED_TOTAL_PRE:
        pin_fail.append(f"entry total {pre_total} != {EXPECTED_TOTAL_PRE}")
    if pre_dups != EXPECTED_DUP_ITEMS or pre_surplus != EXPECTED_SURPLUS:
        pin_fail.append(f"dup census {pre_dups} items / {pre_surplus} surplus != {EXPECTED_DUP_ITEMS}/{EXPECTED_SURPLUS}")
    if pin_fail:
        print("PRE-PIN REFUSAL:", "; ".join(pin_fail))
        sys.exit(2)

    manifest_sha_pre = hashlib.sha256(open(f"{REPO}/spec-links/manifest.json", "rb").read()).hexdigest()
    changed, removed_total = [], 0
    for lane in LANES:
        path = f"{REPO}/spec-links/{lane}.json"
        raw = open(path, "rb").read()
        d = json.loads(raw)
        items_delta = 0
        for iid, it in d["items"].items():
            codes = it.get("codes") or []
            if not isinstance(codes, list) or len(codes) < 2:
                continue
            seen, kept, removed = set(), [], []
            for entry in codes:
                oid = entry.get("official_id") if isinstance(entry, dict) else entry
                if oid in seen:
                    # twin discipline: the dropped entry must be canonical-identical to the kept one
                    kept_forms = {canon(k) for k in kept if (k.get("official_id") if isinstance(k, dict) else k) == oid}
                    if canon(entry) not in kept_forms:
                        print(f"TWIN REFUSAL: {lane} {iid} {oid} non-identical duplicate — fail-closed")
                        sys.exit(2)
                    removed.append(entry)
                else:
                    seen.add(oid)
                    kept.append(entry)
            if removed:
                it["codes"] = kept
                items_delta += len(removed)
                removed_total += len(removed)
        if items_delta:
            out = (json.dumps(d, indent=1) + "\n").encode()
            if out == raw:
                print(f"NOOP-REFUSAL: {lane} computed delta {items_delta} but bytes identical")
                sys.exit(2)
            open(path, "wb").write(out)
            changed.append((lane, items_delta))

    # post-asserts
    post_total, post_dups, post_surplus = 0, 0, 0
    deltas = {l: 0 for l in LANES}
    for lane in LANES:
        d = load(lane)
        n = sum(len(it.get("codes") or []) for it in d["items"].values())
        post_total += n
        di, su, _ = census(d)
        post_dups += di
        post_surplus += su
        p = sum(len(it.get("pending") or []) for it in d["items"].values())
        if p != EXPECTED_PENDING[lane]:
            print(f"POST-REFUSAL: {lane} pending changed {p}"); sys.exit(2)
    deltas = {l: -c for l, c in changed} | {l: 0 for l in LANES if l not in {x[0] for x in changed}}
    deltas = {l: EXPECTED_DELTAS[l] for l in LANES}  # verify against expected
    for lane in LANES:
        d0 = json.loads(sh("git", "show", f"HEAD:spec-links/{lane}.json").stdout)
        d1 = load(lane)
        actual = sum(len(it.get("codes") or []) for it in d1["items"].values()) - \
                 sum(len(it.get("codes") or []) for it in d0["items"].values())
        if actual != EXPECTED_DELTAS[lane]:
            print(f"POST-REFUSAL: {lane} delta {actual} != {EXPECTED_DELTAS[lane]}"); sys.exit(2)
        # totals fields byte-stable (they count items, not entries)
        if d1["totals"] != d0["totals"]:
            print(f"POST-REFUSAL: {lane} totals changed"); sys.exit(2)
        if d1["review_state"] != d0["review_state"] or d1["anchors"] != d0["anchors"]:
            print(f"POST-REFUSAL: {lane} review_state/anchors changed"); sys.exit(2)
    if post_dups != 0 or post_surplus != 0:
        print(f"POST-REFUSAL: {post_dups} dup items remain"); sys.exit(2)
    if post_total != EXPECTED_TOTAL_POST:
        print(f"POST-REFUSAL: total {post_total} != {EXPECTED_TOTAL_POST}"); sys.exit(2)
    manifest_sha_post = hashlib.sha256(open(f"{REPO}/spec-links/manifest.json", "rb").read()).hexdigest()
    if manifest_sha_post != manifest_sha_pre:
        print("POST-REFUSAL: manifest changed — footprint violation"); sys.exit(2)

    print("changed:", changed)
    print("removed surplus entries:", removed_total)
    print(f"codes census: {pre_total} -> {post_total}")
    print("post in-item duplicates: 0 | manifest sha stable | pending/totals/review_state/anchors stable")
    print("REPAIR OK")

if __name__ == "__main__":
    main()
