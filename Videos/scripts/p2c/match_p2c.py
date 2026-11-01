#!/usr/bin/env python3
"""P2C: per-course channel->spec candidate matcher (title-only evidence posture).
Outputs top-3 candidates per spec for LLM adjudication."""
import json, re, sys, collections

CH = "/home/z/my-project/work/channels"
V2 = "/home/z/my-project/repos/syllabai-v2"

def load_pools():
    pools = []
    for name, prov in (("cognito", "cognito"), ("fsl", "freesciencelessons"),
                        ("malmesbury", "malmesbury-education"), ("doodle", "doodlescience"),
                        ("amoeba", "amoeba-sisters")):
        d = json.load(open(f"{CH}/{name}-uploads.json"))
        for v in d["videos"]:
            if v.get("title"):
                pools.append({"id": v["id"], "title": v["title"], "duration": v.get("duration"), "provider": prov})
    return pools

POOLS = load_pools()
by_id = {p["id"]: p for p in POOLS}

STOP = set("""a an the of and or to in on for with as by from that this these those it its their
understand understand how why what which who when describe explain use used using including include
practical investigate investigation lesson course gcse igcse a-level ks3 revision science biology chemistry physics maths
is are be been being can could should would may might will shall must do does did have has had
they them then than there here where also more most some any all both each other another into onto upon about
not no yes if but so because however therefore thus hence while whilst during before after between among within without
""".split())

def toks(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]

def spec_tokens(stmt):
    # drop leading command words but keep content
    return toks(stmt)

def score(title, spec_toks, spec_code):
    tt = set(toks(title))
    s = 0.0
    hits = []
    for w in spec_toks:
        if w in tt:
            s += 2.0 if len(w) > 5 else 1.2
            hits.append(w)
    # distinctive-term boost: long spec words are the meat
    for w in spec_toks:
        if len(w) >= 8 and w in tt:
            s += 1.5
    # code fragment in title (e.g. '4.11') rarely useful; ignore
    return s, hits

def run(course, pool_filter=None, topn=3, min_score=3.0):
    spine = json.load(open(f"{V2}/apps/hub/spines/{course}.json"))
    pts = [n for n in spine["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT"]
    pools = [p for p in POOLS if (pool_filter is None or pool_filter(p))]
    out = []
    for p in pts:
        st = spec_tokens(p["title"])
        ranked = []
        seen = set()
        for cand in pools:
            s, hits = score(cand["title"], st, p["code"])
            if s >= min_score and cand["id"] not in seen:
                ranked.append((s, cand, hits))
                seen.add(cand["id"])
        ranked.sort(key=lambda x: -x[0])
        out.append({"code": p["code"], "title": p["title"], "top": [
            {"id": c["id"], "title": c["title"], "provider": c["provider"], "score": round(s, 1), "hits": hits[:8]}
            for s, c, hits in ranked[:topn]
        ]})
    json.dump(out, open(f"{CH}/match-{course}.json", "w"), ensure_ascii=False, indent=1)
    n_with = sum(1 for o in out if o["top"])
    print(f"{course}: {len(pts)} specs, {n_with} with >=1 candidate")
    return out

if __name__ == "__main__":
    # external-only pool: Cognito channel-only videos (not on any crawled site page) + all non-Cognito channels
    ch_only = {v["id"] for v in json.load(open(f"{CH}/cognito-channel-only.json"))["channelOnly"]}
    ext = lambda p: p["provider"] != "cognito" or p["id"] in ch_only
    for course in sys.argv[1:]:
        run(course, pool_filter=ext)
