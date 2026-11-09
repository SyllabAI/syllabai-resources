#!/usr/bin/env python3
"""oEmbed identity sweep for external-channel candidate videos."""
import json, urllib.request, urllib.parse, concurrent.futures, sys

CANDS = [
    # (id, provider, my_subject_tag)
    ("Lomr_t5Pdjs", "freesciencelessons", "gcse"),
    ("vWZWPlFmua4", "freesciencelessons", "gcse"),
    ("QekStThHD2M", "freesciencelessons", "gcse"),
    ("hNq-y2Kg5CE", "freesciencelessons", "gcse"),
    ("nrbJl3R4YJU", "freesciencelessons", "gcse"),
    ("u59Eg1uNr5g", "freesciencelessons", "gcse"),
    ("DbLVB_EDnRs", "freesciencelessons", "gcse"),
    ("kmRh_yRbAR4", "freesciencelessons", "gcse"),
    ("iXswGsfeHJg", "freesciencelessons", "gcse"),
    ("yLHz2Ea10Mg", "freesciencelessons", "gcse"),
    ("1Z405uGDZGo", "freesciencelessons", "gcse"),
    ("9yTDokLRZs0", "freesciencelessons", "gcse"),
    ("gu9T91GJXDo", "freesciencelessons", "gcse"),
    ("RhMOCxXcDrQ", "malmesbury-education", "gcse"),
    ("sI2Dp5fNdDY", "malmesbury-education", "gcse"),
    ("1Dx7LDwINLU", "amoeba-sisters", "us-intro"),
    ("ALFE2tNIY5c", "amoeba-sisters", "us-intro"),
    ("NHqEthRCqQ4", "amoeba-sisters", "us-intro"),
    ("QMBGMUgAqCs", "amoeba-sisters", "us-intro"),
    ("YbdkbCU20_M", "amoeba-sisters", "us-intro"),
    ("YJHGfbW55l0", "amoeba-sisters", "us-intro"),
    ("CDw4WPng2iE", "amoeba-sisters", "us-intro"),
    ("RNLceVI8jcc", "amoeba-sisters", "us-intro"),
    ("DGpPHrLF-5M", "amoeba-sisters", "us-intro"),
    ("UrTchvRUMW0", "cognito", "ks3"),
    ("als-gv_D7bc", "cognito", "ks3"),
    ("BIf0sIKQm_E", "cognito", "ks3"),
]

def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    u = f"https://www.youtube.com/oembed?url={q}&format=json"
    try:
        with urllib.request.urlopen(u, timeout=20) as r:
            d = json.loads(r.read())
        return vid, {"ok": True, "title": d.get("title"), "author": d.get("author_name"),
                     "authorUrl": d.get("author_url"), "thumb": d.get("thumbnail_url")}
    except Exception as e:
        return vid, {"ok": False, "err": f"{type(e).__name__}: {e}"}

with concurrent.futures.ThreadPoolExecutor(6) as ex:
    res = dict(ex.map(lambda c: oembed(c[0]), CANDS))

out = {}
for vid, prov, tag in CANDS:
    o = res[vid]
    out[vid] = {"provider": prov, "levelTag": tag, **o}
    status = "OK " if o["ok"] else "DEAD"
    print(f"{status} {vid} [{prov}] {o.get('author','?')!r} :: {(o.get('title') or o.get('err'))[:90]}")

json.dump(out, open("/home/z/my-project/work/channels/candidate-oembed.json", "w"), ensure_ascii=False, indent=1)
n_ok = sum(1 for v in out.values() if v["ok"])
print(f"\nverified {n_ok}/{len(out)}")
sys.exit(0 if n_ok == len(out) else 1)
