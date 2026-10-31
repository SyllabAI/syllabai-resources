#!/usr/bin/env python3
"""T-ZNOTES-2 integrate pass: fix leaf-json provenance, update course
manifests, rebuild the global manifest, verify consistency.

Run AFTER zn_resync_images.py in the same working tree.
"""
import json
import os
import sys
import time
from datetime import datetime, timezone

TASK = "T-ZNOTES-2"


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--resolved", required=True, help="json ledger of resolved failures")
    ap.add_argument("--report2", required=True, help="final resync report (unresolved list)")
    a = ap.parse_args()
    resolved = json.load(open(a.resolved))
    report2 = json.load(open(a.report2))
    zn = os.path.join(a.root, "ZNotes")

    by_asset = {}
    for e in resolved:
        by_asset[e["asset"]] = e

    per_course = {}
    for e in resolved:
        per_course.setdefault(e["course"], []).append(e)

    # ---- 1. restore leaf-json provenance ----
    fixed_json = 0
    for course, entries in per_course.items():
        cdir = os.path.join(zn, course)
        notes = os.path.join(cdir, "notes")
        for dirpath, _, fns in os.walk(notes):
            for fn in fns:
                if not fn.endswith(".json"):
                    continue
                p = os.path.join(dirpath, fn)
                j = json.load(open(p, encoding="utf-8"))
                imgs = j.get("images") or []
                hit = False
                for im in imgs:
                    ou = im.get("orig_url") or ""
                    if ou.startswith("../../../assets/"):
                        asset = ou.rsplit("/", 1)[-1]
                        e = by_asset.get(asset)
                        if not e:
                            print(f"!! no ledger entry for asset {asset} in {p}")
                            continue
                        im["orig_url"] = e["url"]
                        im["file"] = e["asset"]
                        im["resourced_via"] = {"strategy": e["strategy"],
                                               "recovered_url": e["recovered_url"],
                                               "task": TASK}
                        hit = True
                if hit:
                    json.dump(j, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
                    fixed_json += 1
    print(f"leaf jsons fixed: {fixed_json}")

    # ---- 2. course manifests ----
    unresolved_by_course = {}
    for e in report2["unresolved"]:
        unresolved_by_course.setdefault(e["course"], []).append(e)

    for course, entries in per_course.items():
        cdir = os.path.join(zn, course)
        p = os.path.join(cdir, "manifest.json")
        man = json.load(open(p, encoding="utf-8"))
        cnt = man["counts"]
        n = len(entries)
        cnt["images"] = cnt.get("images", 0) + n
        cnt["image_failures"] = cnt.get("image_failures", 0) - n
        cnt["assets_bytes"] = cnt.get("assets_bytes", 0) + sum(e["bytes"] for e in entries)
        fails = man.get("failures") or {}
        orig_fails = fails.get("images") or []
        res_urls = {e["url"] for e in entries}
        fails["images"] = [f for f in orig_fails if f["url"] not in res_urls]
        fails["images_resolved"] = [{
            "orig_url": e["url"], "orig_error": e["orig_error"],
            "recovered_url": e["recovered_url"], "strategy": e["strategy"],
            "asset": e["asset"], "bytes": e["bytes"],
        } for e in entries]
        man["failures"] = fails
        man["resynced_utc"] = now_utc()
        man["resync_task"] = TASK
        json.dump(man, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        print(f"manifest {course}: +{n} images, failures {len(orig_fails)} -> {len(fails['images'])}")

    # ---- 3. global manifest rebuild (mirrors zn_fetch.build_global_manifest) ----
    courses = {}
    tot = {"modules": 0, "chapters": 0, "cards": 0, "images": 0,
           "image_failures": 0, "fetch_failures": 0, "markdown_chars": 0,
           "assets_bytes": 0}
    for slug in sorted(os.listdir(zn)):
        p = os.path.join(zn, slug, "manifest.json")
        if not os.path.isfile(p):
            continue
        man = json.load(open(p, encoding="utf-8"))
        cnt = man["counts"]
        courses[slug] = {"course_slug": slug, "notes_base": man["notes_base"],
                         "subject": man.get("subject"), "code": man.get("code"),
                         "board": man.get("board"), "level": man.get("level"),
                         "wip": man.get("wip", False), "counts": cnt}
        for k in tot:
            tot[k] += cnt.get(k, 0)
    out = {
        "schema": "syllabai.znotes-revision-notes/1.0",
        "generated_utc": now_utc(),
        "task": TASK,
        "source": {"site": "https://znotes.org", "api": "https://api.znotes.org",
                   "boards": ["caie", "edexcel"]},
        "totals": tot,
        "scraped_courses": len(courses),
        "courses": courses,
    }
    with open(os.path.join(zn, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"global manifest rebuilt: {len(courses)} courses, images {tot['images']}, "
          f"image_failures {tot['image_failures']}, assets {tot['assets_bytes']/1e6:.1f} MB")

    # ---- 4. verification ----
    print("\n=== verification ===")
    bad_json = 0
    missing_assets = 0
    stale_md = 0
    resolved_urls = {e["url"] for e in resolved}
    for course, entries in per_course.items():
        cdir = os.path.join(zn, course)
        for dirpath, _, fns in os.walk(os.path.join(cdir, "notes")):
            for fn in fns:
                p = os.path.join(dirpath, fn)
                if fn.endswith(".json"):
                    j = json.load(open(p, encoding="utf-8"))
                    for im in (j.get("images") or []):
                        if (im.get("orig_url") or "").startswith("../../../assets/"):
                            bad_json += 1
                else:
                    txt = open(p, encoding="utf-8").read()
                    for e in entries:
                        if e["url"] in txt:
                            stale_md += 1
                            print(f"  stale md ref: {p}")
                    import re
                    for m in re.finditer(r"\.\./\.\./\.\./assets/([A-Za-z0-9._-]+)", txt):
                        if not os.path.isfile(os.path.join(cdir, "assets", m.group(1))):
                            missing_assets += 1
                            print(f"  missing asset: {m.group(1)} referenced in {p}")
    print(f"json orig_url still local: {bad_json}")
    print(f"resolved urls still in md: {stale_md}")
    print(f"missing asset files: {missing_assets}")
    # asset bytes cross-check
    size_mismatch = 0
    for e in resolved:
        p = os.path.join(zn, e["course"], "assets", e["asset"])
        actual = os.path.getsize(p) if os.path.isfile(p) else -1
        if actual != e["bytes"]:
            size_mismatch += 1
            print(f"  size mismatch {e['asset']}: ledger {e['bytes']} vs disk {actual}")
    print(f"asset size mismatches: {size_mismatch}")
    ok = not (bad_json or missing_assets or stale_md or size_mismatch)
    print("VERIFICATION:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
