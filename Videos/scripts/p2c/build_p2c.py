#!/usr/bin/env python3
"""Build P2C per-course draft JSONs + validate everything before writing."""
import json, sys, datetime, urllib.request, urllib.parse, concurrent.futures
sys.path.insert(0, "/home/z/my-project/scripts")
from p2c_bindings import CHEM, PHYS, MATHS, CIE_BIO, CIE_CHEM, CIE_PHYS

NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
V2 = "/home/z/my-project/repos/syllabai-v2"
CH = "/home/z/my-project/work/channels"

COURSES = {
    "igcse-chemistry-19": CHEM,
    "igcse-physics-19": PHYS,
    "igcse-maths-a-18-higher": MATHS,
    "cie-igcse-biology-23": CIE_BIO,
    "cie-igcse-chemistry-23": CIE_CHEM,
    "cie-igcse-physics-23": CIE_PHYS,
}
COURSE_LABEL = {
    "igcse-chemistry-19": "IGCSE Chemistry (4CH1, Edexcel International GCSE)",
    "igcse-physics-19": "IGCSE Physics (4PH1, Edexcel International GCSE)",
    "igcse-maths-a-18-higher": "IGCSE Maths A (4MA1 Higher, Edexcel International GCSE)",
    "cie-igcse-biology-23": "IGCSE Biology (0610, Cambridge IGCSE 2023+)",
    "cie-igcse-chemistry-23": "IGCSE Chemistry (0620, Cambridge IGCSE 2023+)",
    "cie-igcse-physics-23": "IGCSE Physics (0625, Cambridge IGCSE 2023+)",
}

# load pools for durations/titles + channel-only guard
durs, titles = {}, {}
for name in ("cognito", "fsl", "malmesbury", "amoeba", "doodle"):
    d = json.load(open(f"{CH}/{name}-uploads.json"))
    for v in d["videos"]:
        if v.get("duration"): durs[v["id"]] = v["duration"]
        if v.get("title"): titles[v["id"]] = v["title"]
ch_only = {v["id"] for v in json.load(open(f"{CH}/cognito-channel-only.json"))["channelOnly"]}

errs = []
for course, rows in COURSES.items():
    spine = json.load(open(f"{V2}/apps/hub/spines/{course}.json"))
    codes = {n["code"] for n in spine["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT"}
    for vid, prov, specs, conf, ev in rows:
        if prov == "cognito" and vid not in ch_only:
            errs.append(f"{course}: cognito video {vid} is NOT channel-only (already on a site page)")
        for s in specs:
            if s not in codes:
                errs.append(f"{course}: spec {s} not in spine (row {vid})")
        if conf not in ("medium", "low"):
            errs.append(f"{course}: bad confidence {conf}")
print("validation:", errs if errs else "NONE")
if errs:
    sys.exit(1)

# oEmbed verify all distinct ids
all_ids = sorted({r[0] for rows in COURSES.values() for r in rows})
def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    try:
        with urllib.request.urlopen(f"https://www.youtube.com/oembed?url={q}&format=json", timeout=20) as r:
            d = json.loads(r.read())
        return vid, (True, d.get("title"), d.get("author_name"))
    except Exception as e:
        return vid, (False, f"{type(e).__name__}: {e}", None)
with concurrent.futures.ThreadPoolExecutor(6) as ex:
    res = dict(ex.map(oembed, all_ids))
dead = [v for v, r in res.items() if not r[0]]
print(f"oEmbed: {len(all_ids)-len(dead)}/{len(all_ids)} verified")
if dead:
    print("DEAD:", dead); sys.exit(1)
json.dump({v: {"title": r[1], "author": r[2]} for v, r in res.items()},
          open(f"{CH}/candidate-oembed-p2c.json", "w"), ensure_ascii=False, indent=1)

# write per-course drafts
made = {}
for course, rows in COURSES.items():
    videos = {}
    for vid, prov, specs, conf, ev in rows:
        if vid not in videos:
            videos[vid] = {
                "id": vid, "title": res[vid][1], "provider": prov,
                "watchUrl": f"https://www.youtube.com/watch?v={vid}",
                "lessonRef": None, "lessonUrl": None,
                "levelTag": "ks3" if (titles.get(vid) or "").startswith("KS3") else "gcse",
                "boardNote": "Cognito's own channel (channel-only video, not surfaced on cognitoedu.org pages)" if prov == "cognito"
                             else "AQA-aligned GCSE channel; content generic GCSE-level" if prov == "freesciencelessons"
                             else "US-curriculum channel; NGSS vocabulary" if prov == "amoeba-sisters"
                             else "UK GCSE physics doodle channel" if prov == "doodlescience"
                             else "Malmesbury Education required-practicals channel",
                "durationS": durs.get(vid), "guestVisible": None, "subelementOfPrimary": False,
                "oembedAuthor": res[vid][2], "oembedVerifiedUtc": NOW,
            }
    mappings = [{
        "video": vid, "lessonRef": None, "lessonUrl": None, "specs": specs,
        "confidence": conf, "evidence": ev, "method": "llm-draft-external",
        "reviewed": False, "reviewer": None, "reviewedUtc": None, "boardMismatch": True,
    } for vid, prov, specs, conf, ev in rows]
    specs_cov = sorted({s for _, _, sp, _, _ in rows for s in sp})
    draft = {
        "schema": "syllabai.video-map-draft/1",
        "draftOf": f"hub.video-map/1 {course}",
        "task": "T-VIDEOMAP-P2C (all-subjects external-channels sweep)",
        "course": course,
        "qual": "IGCSE",
        "reviewState": "draft-external-sweep",
        "draftLaw": "never enters content/ without owner review; every row reviewed:false; note: NO committed map exists for this course yet — these channel rows are a supplement and the P2-method site-inventory alignment remains the primary follow-up pass",
        "source": {
            "provider": "multi (freesciencelessons / doodlescience / amoeba-sisters / cognito channel-only)",
            "method": "yt-dlp flat channel enumeration + oEmbed identity sweep + LLM title-to-spec adjudication; evidence is TITLE-ONLY",
            "enumeratedUtc": NOW,
        },
        "videos": list(videos.values()),
        "mappings": mappings,
        "coverage": {
            "specPointsTotal": len({n["code"] for n in json.load(open(f"{V2}/apps/hub/spines/{course}.json"))["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT"}),
            "specPointsDraftedHere": len(specs_cov),
            "rows": len(mappings),
            "byConfidence": {
                "medium": sum(1 for m in mappings if m["confidence"] == "medium"),
                "low": sum(1 for m in mappings if m["confidence"] == "low"),
            },
        },
        "generatedUtc": NOW,
    }
    path = f"/home/z/my-project/repos/syllabai-resources/Videos/drafts/{course}/video-map.draft.external.json"
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(draft, open(path, "w"), ensure_ascii=False, indent=1)
    made[course] = (len(videos), len(mappings), len(specs_cov))
    print(f"{course}: {len(videos)} videos, {len(mappings)} rows, {len(specs_cov)} specs drafted")

json.dump(made, open(f"{CH}/p2c-summary.json", "w"), indent=1)
