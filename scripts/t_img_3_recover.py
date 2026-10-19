#!/usr/bin/env python3
"""
T-IMG-3 — recover the 5 asset-failed SME ExamQuestion images in the OLD
lanes (the last 5 unresolved image refs corpus-wide in SME-ExamQuestion),
following the T-IMG-2 style: locate the original asset on the live source,
recover it, and document the recovery with dated HTML comments in the md.

Failures being repaired (recorded at scrape time in the lane manifests):

  ial-maths-20-mechanics-1 / dynamics-and-statics /
  resolving-forces-inclined-planes-and-friction (4 images)
    The SME CMS stores these CDN filenames with a literal mojibake 'Gamma'
    (U+0393, UTF-8 CE 93) inside "Newton-Gamma-COs-Laws" (the CMS-side
    mangling of "Newton's Laws"). The Sep-17 scraper passed the raw decoded
    URL to urllib, whose ascii codec refused the non-ASCII char -> "GET
    failed after 3 tries ... 'ascii'". The objects themselves are healthy:
    fetching with the Gamma percent-encoded (%CE%93), exactly as a browser
    does, returns valid PNGs (verified 200 + PNG magic on 2026-09-20).

  igcse-chemistry-modular-24-unit-2 / principles-of-chemistry /
  covalent-bonding (1 image, 011-img.png, 3 refs)
    An ExamQuest (doublestruck) mark-scheme tick glyph hosted at
    ds-content.doublestruck.eu (S3). Proven dead at origin on 2026-09-20:
    S3 AccessDenied via urllib, curl/HTTP2, headless Chromium direct nav,
    AND an in-page Image() probe inside the live SME page session (cookies
    + referrer); sibling AG_CHM folder probes all 403; no archive captures
    retrievable. The live SME page itself renders this tick broken today.
    NOT fabricated (T-IMG-2 honesty rule); refs carry a figure-unrecoverable
    comment and the manifest record is annotated with the evidence.
"""
from __future__ import annotations

import hashlib
import json
import struct
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path("/home/z/my-project/download/syllabai-resources")
EQ = REPO / "SME-ExamQuestion"
MECH = EQ / "ial-maths-20-mechanics-1"
CHEM = EQ / "igcse-chemistry-modular-24-unit-2"
TOPIC_ASSETS = MECH / "dynamics-and-statics" / \
    "resolving-forces-inclined-planes-and-friction" / "assets"
COVAL_MS = CHEM / "principles-of-chemistry" / "covalent-bonding" / \
    "mark-schemes.md"
MECH_MS = MECH / "dynamics-and-statics" / \
    "resolving-forces-inclined-planes-and-friction" / "mark-schemes.md"
REPORT = REPO / "scripts" / "t_img_3_recover_report.json"
DATE = "2026-09-20"

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# name -> (upload dir, filename as served by the SME CDN)
MECH_TARGETS = {
    "025-img.png": ("2021/11",
                    "MA_Q6_3.3-Further-Forces-Newton\u0393COs-Laws"
                    "_Easy_Edexcel_A_Level_Maths_Mechanics.png"),
    "067-img.png": ("2021/12",
                    "MI_Q10_3.3-Further-Forces-Newton\u0393COs-Laws"
                    "_Hard_Edexcel_A_Level_Maths_Mechanics.png"),
    "069-img.png": ("2021/03",
                    "MI_Q10a_3.3-Further-Forces-Newton\u0393COs-Laws"
                    "_Medium_Edexcel_A_Level_Maths_Mechanics.png"),
    "070-img.png": ("2021/03",
                    "MI_Q10b_3.3-Further-Forces-Newton\u0393COs-Laws"
                    "_Medium_Edexcel_A_Level_Maths_Mechanics.png"),
}

TICK_URL = ("https://ds-content.doublestruck.eu/AG_CHM/Q11WY2F02_files_Q/"
            "tick.png?ser=1652356153063")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "*/*",
        "Accept-Language": "en-GB,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def png_dims(data: bytes) -> tuple[int, int]:
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise RuntimeError("not a PNG/IHDR payload")
    w, h = struct.unpack(">II", data[16:24])
    return w, h


def recover_mech() -> list[dict]:
    out = []
    for name, (ym, fname) in MECH_TARGETS.items():
        served = f"https://cdn.savemyexams.com/uploads/{ym}/{fname}"
        fetched = served.replace("\u0393", "%CE%93")
        data = fetch(fetched)
        if data[:4] != b"\x89PNG":
            raise RuntimeError(f"{name}: not a PNG payload")
        if len(data) < 64:
            raise RuntimeError(f"{name}: suspiciously small ({len(data)} B)")
        w, h = png_dims(data)
        target = TOPIC_ASSETS / name
        target.write_bytes(data)
        out.append({
            "name": name,
            "lane": "ial-maths-20-mechanics-1",
            "target": str(target.relative_to(REPO)),
            "source_url_served": served,
            "fetched_url": fetched,
            "bytes": len(data),
            "dimensions": f"{w}x{h}",
            "sha256": hashlib.sha256(data).hexdigest(),
            "recovered": DATE,
        })
        print(f"recovered {name}: {w}x{h}, {len(data)} B")
        time.sleep(0.3)
    return out


def patch_mech_md() -> None:
    text = MECH_MS.read_text(encoding="utf-8")
    for name, (ym, fname) in MECH_TARGETS.items():
        old = f"![](assets/{name})"
        comment = (f"<!-- figure recovered {DATE} from "
                   f"https://cdn.savemyexams.com/uploads/{ym}/{fname} "
                   f"(SME CMS stores the filename with a mojibake "
                   f"U+0393; fetched with it percent-encoded as %CE%93 "
                   f"— the scrape-time failure was the raw non-ASCII "
                   f"URL hitting the ascii codec) -->")
        n = text.count(old)
        if n != 1:
            raise RuntimeError(f"{name}: expected 1 ref, found {n}")
        text = text.replace(old, old + comment)
    MECH_MS.write_text(text, encoding="utf-8")
    print("mechanics mark-schemes.md: 4 recovery comments written")


def patch_chem_md() -> None:
    text = COVAL_MS.read_text(encoding="utf-8")
    old = "![](assets/011-img.png)"
    comment = (f"<!-- figure unrecoverable {DATE}: origin object dead "
               f"(S3 AccessDenied for all client classes incl. an "
               f"in-page probe inside the live SME page session; "
               f"sibling ExamQuest folders 403; no archive capture) "
               f"— evidence: scripts/t_img_3_recover_report.json -->")
    n = text.count(old)
    if n != 3:
        raise RuntimeError(f"011-img.png: expected 3 refs, found {n}")
    text = text.replace(old, old + comment)
    COVAL_MS.write_text(text, encoding="utf-8")
    print("covalent-bonding mark-schemes.md: 3 unrecoverable comments written")


def patch_manifests() -> dict:
    # mechanics: resolve the 4 failures
    mp = MECH / "manifest.json"
    m = json.loads(mp.read_text(encoding="utf-8"))
    trec = next(t for t in m["topics"]
                if t["topic_slug"] ==
                "resolving-forces-inclined-planes-and-friction")
    if len(trec["asset_failures"]) != 4:
        raise RuntimeError("mechanics: expected 4 recorded failures")
    trec["asset_failures"] = []
    trec["assets"] += 4
    if m["totals"]["asset_failures"] != 4:
        raise RuntimeError("mechanics: totals.asset_failures != 4")
    m["totals"]["asset_failures"] = 0
    m["totals"]["assets"] += 4
    mp.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n",
                  encoding="utf-8")
    # chemistry: keep the failure recorded, annotate with the evidence
    cp = CHEM / "manifest.json"
    c = json.loads(cp.read_text(encoding="utf-8"))
    ct = next(t for t in c["topics"] if t.get("asset_failures"))
    entry = ct["asset_failures"][0]
    if entry["name"] != "011-img.png":
        raise RuntimeError("chem: unexpected failure record")
    entry["error"] += ("; re-verified 2026-09-20 (T-IMG-3): object dead at "
                       "origin - S3 AccessDenied via urllib/curl/HTTP2 and "
                       "an in-page Image() probe inside the live SME page "
                       "session; sibling AG_CHM folders 403; no archive "
                       "capture retrievable; marked figure-unrecoverable in "
                       "mark-schemes.md (T-IMG-2 honesty rule: not "
                       "fabricated)")
    cp.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n",
                  encoding="utf-8")
    return {"mechanics": mp.relative_to(REPO).as_posix(),
            "chem": cp.relative_to(REPO).as_posix()}


def patch_registry() -> None:
    rp = EQ / "manifest.json"
    reg = json.loads(rp.read_text(encoding="utf-8"))
    c = next(x for x in reg["courses"]
             if x["slug"] == "ial-maths-20-mechanics-1")
    if c["totals"]["assets"] != 679 or c["totals"]["asset_failures"] != 4:
        raise RuntimeError("registry: unexpected mechanics totals")
    c["totals"]["assets"] = 683
    c["totals"]["asset_failures"] = 0
    rp.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n",
                  encoding="utf-8")
    print("registry: mechanics-1 totals -> assets 683, failures 0")


def main() -> int:
    recovered = recover_mech()
    patch_mech_md()
    patch_chem_md()
    manifests = patch_manifests()
    patch_registry()
    report = {
        "task": "T-IMG-3",
        "title": "recover the 5 asset-failed SME ExamQuestion images "
                 "(old lanes), T-IMG-2 style",
        "date": DATE,
        "recovered": recovered,
        "unrecoverable": [{
            "name": "011-img.png",
            "lane": "igcse-chemistry-modular-24-unit-2",
            "target": "SME-ExamQuestion/igcse-chemistry-modular-24-unit-2/"
                      "principles-of-chemistry/covalent-bonding/assets/"
                      "011-img.png",
            "refs": 3,
            "role": "ExamQuest mark-scheme tick glyph",
            "source_url": TICK_URL,
            "evidence": [
                "S3 AccessDenied (server: AmazonS3) via urllib with browser "
                "headers, with and without Referer",
                "S3 AccessDenied via curl --http2 with full browser headers",
                "S3 AccessDenied via headless Chromium direct navigation",
                "in-page Image() probe inside the live SME page session "
                "(cookies + referrer): load ERROR",
                "bounded sibling-folder probes "
                "(Q11WY2F01/F03/F04, Q11WY1F02, Q11WY3F02, Q12WY2F02, "
                "Q10WY2F02, Q11WY2F00): all 403",
                "web.archive.org: CDX lists no capture; replay unreachable "
                "from the work environment",
                "the live SME page itself renders this tick broken today "
                "(only ds-content URL on the page; no local sibling copy in "
                "the corpus)",
            ],
            "disposition": "not fabricated (T-IMG-2 honesty rule); "
                           "figure-unrecoverable comments written at the 3 "
                           "refs; manifest record annotated",
        }],
        "manifest_updates": manifests,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"report written: {REPORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
