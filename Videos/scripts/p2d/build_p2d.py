#!/usr/bin/env python3
"""Build P2D per-course drafts (CIE A-level trio) + validate everything before writing."""
import json, sys, datetime, urllib.request, urllib.parse, concurrent.futures, os
sys.path.insert(0, "/home/z/my-project/scripts")
from p2d_bindings import BIO, CHEM, PHYS

NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
V2 = "/home/z/my-project/repos/syllabai-v2-fresh"
CH = "/home/z/my-project/work/channels"
RES = "/home/z/my-project/repos/syllabai-resources"

COURSES = {
    "cie-a-level-biology-25": BIO,
    "cie-a-level-chemistry-25": CHEM,
    "cie-a-level-physics-25": PHYS,
}
COURSE_LABEL = {
    "cie-a-level-biology-25": "A Level Biology (9700, Cambridge International A Level 2025+)",
    "cie-a-level-chemistry-25": "A Level Chemistry (9701, Cambridge International A Level 2025+)",
    "cie-a-level-physics-25": "A Level Physics (9702, Cambridge International A Level 2025+)",
}
BOARD_NOTE = {
    "cognito": "Cognito's own channel (channel-only video, not surfaced on cognitoedu.org pages)",
    "freesciencelessons": "AQA-aligned A-level/GCSE channel; AQA<->CIE divergence adjudicated per row (title-only evidence)",
    "doodlescience": "UK Doodle Science channel; A-Level/GCSE physics explainers",
    "amoeba-sisters": "US-curriculum channel; NGSS vocabulary",
    "malmesbury-education": "Malmesbury Education required-practicals channel",
}

durs, titles, prov_of = {}, {}, {}
for name, prov in (("cognito", "cognito"), ("fsl", "freesciencelessons"), ("malmesbury", "malmesbury-education"),
                   ("amoeba", "amoeba-sisters"), ("doodle", "doodlescience")):
    d = json.load(open(f"{CH}/{name}-uploads.json"))
    for v in d["videos"]:
        if v.get("duration"): durs[v["id"]] = v["duration"]
        if v.get("title"):
            titles[v["id"]] = v["title"]; prov_of[v["id"]] = prov
ch_only = {v["id"] for v in json.load(open(f"{CH}/cognito-channel-only.json"))["channelOnly"]}

errs = []
for course, rows in COURSES.items():
    spine = json.load(open(f"{V2}/apps/hub/spines/{course}.json"))
    codes = {n["code"] for n in spine["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT"}
    for vid, prov, specs, conf, ev in rows:
        if vid not in prov_of:
            errs.append(f"{course}: video {vid} not in any uploads pool")
        elif prov_of[vid] != prov:
            errs.append(f"{course}: video {vid} provider mismatch (pools say {prov_of[vid]}, binding says {prov})")
        if prov == "cognito" and vid not in ch_only:
            errs.append(f"{course}: cognito video {vid} is NOT channel-only")
        for s in specs:
            if s not in codes:
                errs.append(f"{course}: spec {s} not in spine (row {vid})")
        if conf not in ("medium", "low"):
            errs.append(f"{course}: bad confidence {conf} (row {vid})")
# duplicate (video,spec) pairs within each course
for course, rows in COURSES.items():
    seen = set()
    for vid, _, specs, _, _ in rows:
        for s in specs:
            if (vid, s) in seen:
                errs.append(f"{course}: duplicate row {vid}|{s}")
            seen.add((vid, s))
print("validation:", errs if errs else "NONE")
if errs:
    sys.exit(1)

all_ids = sorted({r[0] for rows in COURSES.values() for r in rows})
def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    try:
        with urllib.request.urlopen(f"https://www.youtube.com/oembed?url={q}&format=json", timeout=20) as r:
            d = json.loads(r.read())
        return vid, (True, d.get("title"), d.get("author_name"), "oembed")
    except urllib.error.HTTPError as e:
        if e.code == 401:
            return vid, (False, "HTTPError: 401 embedding-disabled", None, "oembed-401")
        return vid, (False, f"HTTPError: {e.code}", None, f"http-{e.code}")
    except Exception as e:
        return vid, (False, f"{type(e).__name__}: {e}", None, "error")
with concurrent.futures.ThreadPoolExecutor(6) as ex:
    res = dict(ex.map(oembed, all_ids))
# fallback identity for oembed-401 (owner disabled embedding; video existence via thumbnail)
for vid, r in list(res.items()):
    if r[3] == "oembed-401":
        try:
            req = urllib.request.Request(f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", method="HEAD")
            with urllib.request.urlopen(req, timeout=20) as t:
                if t.status == 200:
                    res[vid] = (True, titles.get(vid), None, "thumb-fallback")
        except Exception:
            pass
dead = [v for v, r in res.items() if not r[0]]
ok_kind = {}
for v, r in res.items():
    if r[0]: ok_kind[r[3]] = ok_kind.get(r[3], 0) + 1
print(f"oEmbed: {len(all_ids)-len(dead)}/{len(all_ids)} verified {ok_kind}")
if dead:
    print("DEAD:", dead); sys.exit(1)
json.dump({v: {"title": r[1], "author": r[2], "identity": r[3]} for v, r in res.items()},
          open(f"{CH}/candidate-oembed-p2d.json", "w"), ensure_ascii=False, indent=1)

made = {}
for course, rows in COURSES.items():
    spine_total = len({n["code"] for n in json.load(open(f"{V2}/apps/hub/spines/{course}.json"))["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT"})
    videos = {}
    for vid, prov, specs, conf, ev in rows:
        if vid not in videos:
            t = titles.get(vid, "")
            lvl = "a-level" if __import__("re").search(r"a[ -]?level", t, __import__("re").I) else "gcse"
            identity = res[vid][3]
            videos[vid] = {
                "id": vid, "title": res[vid][1], "provider": prov,
                "watchUrl": f"https://www.youtube.com/watch?v={vid}",
                "lessonRef": None, "lessonUrl": None,
                "levelTag": lvl, "boardNote": BOARD_NOTE[prov],
                "durationS": durs.get(vid), "guestVisible": None, "subelementOfPrimary": False,
                "oembedAuthor": res[vid][2] if identity == "oembed" else None,
                "oembedVerifiedUtc": NOW if identity == "oembed" else None,
                "identityMethod": identity,
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
        "task": "T-VIDEOMAP-P2D (CIE A-level external-channels lane)",
        "course": course,
        "qual": "A Level (CIE)",
        "reviewState": "draft-external-sweep",
        "draftLaw": "never enters content/ without owner review; every row reviewed:false; no committed map exists for this course yet (c3/p3 fully guest-gated, channels are the only video source; b3 has 63 Cognito site videos that the P2-method site lane still owes)",
        "source": {
            "provider": "multi (freesciencelessons / doodlescience / cognito channel-only / amoeba-sisters / malmesbury)",
            "method": "yt-dlp flat channel enumeration + oEmbed identity sweep + LLM title-to-spec adjudication; evidence is TITLE-ONLY; AQA<->CIE divergence handled by conservative binding (medium/low only, no high rows). NOTE: freesciencelessons videos with embedding disabled (oEmbed 401) were identity-checked via i.ytimg.com thumbnail liveness + the channel uploads-playlist enumeration instead; identityMethod field records which path each video used",
            "enumeratedUtc": NOW,
        },
        "videos": list(videos.values()),
        "mappings": mappings,
        "coverage": {
            "specPointsTotal": spine_total,
            "specPointsDraftedHere": len(specs_cov),
            "rows": len(mappings),
            "byConfidence": {
                "medium": sum(1 for m in mappings if m["confidence"] == "medium"),
                "low": sum(1 for m in mappings if m["confidence"] == "low"),
            },
        },
        "generatedUtc": NOW,
    }
    path = f"{RES}/Videos/drafts/{course}/video-map.draft.external.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(draft, open(path, "w"), ensure_ascii=False, indent=1)
    made[course] = {"videos": len(videos), "rows": len(mappings), "specs": len(specs_cov),
                    "total": spine_total,
                    "medium": draft["coverage"]["byConfidence"]["medium"],
                    "low": draft["coverage"]["byConfidence"]["low"]}
    print(f"{course}: {len(videos)} videos, {len(mappings)} rows ({draft['coverage']['byConfidence']['medium']}M/{draft['coverage']['byConfidence']['low']}L), {len(specs_cov)}/{spine_total} specs drafted")

json.dump(made, open(f"{CH}/p2d-summary.json", "w"), indent=1)
print("wrote p2d-summary.json")
