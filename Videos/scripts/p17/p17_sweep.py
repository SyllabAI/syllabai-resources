#!/usr/bin/env python3
"""P17 discovery sweep: targeted YouTube search over the CURRENT corpus residual.

Post-P15/P16 gap profile (gap_profile_p17.json: 3,668 unmapped of 10,814).
Register/paper-code targeted per the spine's own codes — the P15 lesson applied:
the spine's Edexcel IGCSE Geography is 4GE1 (P15 swept 4GE0 and the pool barely
moved), ICT is 4IT1 (not 4IT0), modular maths is 4XM, modular science 4WS/4XS,
modular biology 4WB/4XB, modular chemistry 4WC/4XC.

Dedupe vs (a) all inventoried channels (inventory/channels/*-uploads.json) and
(b) the P15 sweep's 231 harvested channels (work/p15/sweep.json — harvested but
mostly not inventoried; they stay excluded from a P17 proposal).

Cache-resumable: results append to work/p17/sweep.json.

Usage: python3 p17_sweep.py [cluster ...]
"""
import json, os, subprocess, sys, glob

WORK = "/home/z/my-project/work/p17"
RES = "/home/z/my-project/repos/syllabai-resources"
P15 = "/home/z/my-project/work/p15/sweep.json"
os.makedirs(WORK, exist_ok=True)

# gap clusters -> queries (codes verified against the spine curricula at main 2026-11-20)
QUERIES = {
    "edexcel-igcse-geography-4ge1": [
        "Edexcel IGCSE geography A 4GE1", "4GE1 paper 1 walkthrough",
        "IGCSE geography Edexcel coasts rivers revision", "IGCSE geography A fieldwork Edexcel"],
    "ial-chemistry-wch-units": [
        "IAL chemistry unit 3 WCH13", "IAL chemistry unit 4 WCH14 walkthrough",
        "IAL chemistry unit 5 WCH15", "IAL chemistry unit 6 WCH16 revision",
        "WCH11 past paper walkthrough"],
    "cie-igcse-biology-0610": [
        "IGCSE biology 0610 past paper 2023", "CIE IGCSE biology paper 2 multiple choice walkthrough",
        "IGCSE biology 0610 paper 4 extended", "IGCSE biology inheritance genetics 0610"],
    "cie-igcse-em-0680": [
        "IGCSE environmental management 0680 paper 1", "0680 environmental management walkthrough",
        "IGCSE environmental management topic revision"],
    "ial-physics-wph-units": [
        "IAL physics unit 3 WPH13", "IAL physics unit 4 WPH14 walkthrough",
        "IAL physics unit 5 WPH15", "IAL physics unit 6 WPH16",
        "WPH11 past paper walkthrough"],
    "edexcel-igcse-ict-4it1": [
        "Edexcel IGCSE ICT 4IT1", "IGCSE ICT paper 1 walkthrough Edexcel",
        "4IT1 theory revision"],
    "ial-biology-wbi-units": [
        "IAL biology unit 3 WBI13", "IAL biology unit 4 WBI14 walkthrough",
        "IAL biology unit 5 WBI15", "WBI11 past paper walkthrough"],
    "edexcel-igcse-maths-4ma1": [
        "4MA1 paper 1H walkthrough", "4MA1 paper 2H walkthrough",
        "IGCSE maths A foundation 1F walkthrough", "4MA1 higher past paper"],
    "edexcel-igcse-maths-modular-4xm": [
        "Edexcel IGCSE maths modular 4XM1", "IGCSE maths A modular unit 1",
        "IGCSE maths modular higher unit 2"],
    "edexcel-igcse-science-modular-4xs": [
        "Edexcel IGCSE science modular 4XS1", "IGCSE science double award modular unit",
        "4XB1 biology modular", "4XC1 chemistry modular"],
    "cie-igcse-geography-0460": [
        "IGCSE geography 0460 paper 1", "0460 geography paper 2 skills",
        "Cambridge IGCSE geography revision"],
    "cie-igcse-economics-0455": [
        "IGCSE economics 0455 paper 1", "0455 paper 2 structured walkthrough",
        "IGCSE economics revision Cambridge"],
    "cie-a-level-economics-9708": [
        "A level economics 9708 paper 3", "9708 paper 4 data response walkthrough",
        "CIE economics A2 revision"],
    "cie-igcse-accounting-0452": [
        "IGCSE accounting 0452 paper 1", "0452 accounting walkthrough",
        "Cambridge IGCSE accounting revision"],
    "cie-as-general-paper-8021": [
        "AS level general paper 8021", "Cambridge general paper essay writing",
        "8021 comprehension walkthrough"],
    "cie-as-em-8291": [
        "AS environmental management 8291", "Cambridge AS level environmental management"],
    "edexcel-igcse-chemistry-4ch1": [
        "Edexcel IGCSE chemistry 4CH1 paper 1", "4CH1 paper 2 walkthrough",
        "IGCSE chemistry Edexcel revision"],
    "cie-igcse-physics-0625": [
        "IGCSE physics 0625 paper 2 walkthrough", "0625 paper 4 extended",
        "Cambridge IGCSE physics revision"],
    "cie-igcse-chem-0620": [
        "IGCSE chemistry 0620 paper 4 walkthrough", "0620 paper 2 multiple choice"],
    "edexcel-igcse-maths-b-4mb1": [
        "Edexcel IGCSE maths B 4MB1", "IGCSE maths B paper walkthrough"],
    "cie-international-maths-0607": [
        "Cambridge IGCSE international mathematics 0607", "0607 maths paper walkthrough"],
    "cie-igcse-coordinated-0654": [
        "IGCSE coordinated science 0654", "0654 paper 2 walkthrough"],
    "edexcel-igcse-business-4bs1": [
        "Edexcel IGCSE business 4BS1", "IGCSE business studies paper Edexcel"],
    "cie-igcse-lit-0475-unseen": [
        "0475 unseen poetry IGCSE", "IGCSE literature 0475 coursework",
        "Songs of ourselves volume 1 part 4 analysis"],
}


# legacy pools of record excluded by title (inventory files carry no channelId):
# Amoeba Sisters / Cognito / Doodle Science / Freesciencelessons / Malmesbury
# + Exam Essentials (P2F pool of record — the P15 exclusion of record)
EXCLUSIONS = {
    "UC4qJbWvplEpYsKdc5X1hd9w": "p2f-pool-of-record-excluded",
}
LEGACY_TITLES = {
    "amoeba sisters", "cognito", "doodle science", "freesciencelessons",
    "malmesbury education", "exam essentials",
}


def _norm(t):
    import re as _re
    return _re.sub(r"[^a-z0-9]", "", (t or "").lower())


def known_ucs():
    """UC -> name map PLUS title -> name map for legacy inventories w/o channelId."""
    ucs, titles = {}, {}
    for f in glob.glob(RES + "/Videos/inventory/channels/*-uploads.json"):
        name = os.path.basename(f).replace("-uploads.json", "")
        d = json.load(open(f))
        cid = d.get("channelId")
        t = d.get("channelTitle") or d.get("channel") or ""
        if isinstance(t, str) and t.startswith("http"):
            t = t.rstrip("/").rsplit("@", 1)[-1].replace("/videos", "").replace("-", " ")
        if cid:
            ucs[cid] = name
        if _norm(t):
            titles[_norm(t)] = name
    if os.path.exists(P15):
        p15 = json.load(open(P15))
        for cid, v in p15.get("channels", {}).items():
            # P15 swept-but-uninventoried channels carry a sentinel: flagged, not
            # hidden — a corrected-code cluster hitting one hard is re-proposable
            # WITH the p15-swept disclosure (nothing silently dropped).
            ucs.setdefault(cid, "p15-swept-uninventoried")
    return ucs, titles


def known_as(cid, name, ucs, titles):
    if cid in EXCLUSIONS:
        return EXCLUSIONS[cid]
    if cid in ucs:
        return ucs[cid]
    n = _norm(name)
    for lt in LEGACY_TITLES:
        if n and (n == _norm(lt) or n.startswith(_norm(lt))):
            return titles.get(_norm(lt), lt + " (legacy pool of record)")
    return None


def search(q, n=15):
    try:
        p = subprocess.run(["yt-dlp", "--flat-playlist", "--no-warnings", "-i",
                            "--print", "%(channel_id)s\t%(channel)s\t%(title)s",
                            f"ytsearch{n}:{q}"],
                           capture_output=True, text=True, timeout=150)
    except subprocess.TimeoutExpired:
        return []
    rows = []
    for l in (p.stdout or "").splitlines():
        if "\t" in l:
            parts = l.split("\t", 2)
        else:
            continue
        if len(parts) == 3 and parts[0].startswith("UC"):
            rows.append({"channelId": parts[0], "channel": parts[1], "title": parts[2]})
    return rows


def main():
    sweep_path = os.path.join(WORK, "sweep.json")
    sweep = json.load(open(sweep_path)) if os.path.exists(sweep_path) else {"queries": {}, "channels": {}}
    ucs, titles = known_ucs()
    # reclassification pass: refresh knownAs on cached entries under the fixed dedupe
    refreshed = 0
    for cid, v in sweep["channels"].items():
        ka = known_as(cid, v.get("channel", ""), ucs, titles)
        if ka != v.get("knownAs"):
            v["knownAs"] = ka
            refreshed += 1
    if refreshed:
        json.dump(sweep, open(sweep_path, "w"))
        print(f"knownAs refreshed on {refreshed} cached entries")
    clusters = sys.argv[1:] or list(QUERIES)
    done = 0
    for cl in clusters:
        for q in QUERIES[cl]:
            if f"{cl}::{q}" in sweep["queries"]:
                continue
            rows = search(q)
            sweep["queries"][f"{cl}::{q}"] = {"n": len(rows), "rows": rows}
            done += 1
            print(f"[{cl}] {q!r} -> {len(rows)} hits", flush=True)
            for r in rows:
                c = sweep["channels"].setdefault(r["channelId"], {
                    "channel": r["channel"], "clusters": {}, "titles": [],
                    "knownAs": known_as(r["channelId"], r["channel"], ucs, titles)})
                c["clusters"][cl] = c["clusters"].get(cl, 0) + 1
                if len(c["titles"]) < 4:
                    c["titles"].append(r["title"])
            json.dump(sweep, open(sweep_path, "w"))
    if done == 0:
        print("all queries already cached")
    # report
    print("\n=== per-channel cluster density (truly new channels, ranked) ===")
    newc = {k: v for k, v in sweep["channels"].items() if v.get("knownAs") is None}
    p15res = {k: v for k, v in sweep["channels"].items() if v.get("knownAs") == "p15-swept-uninventoried"}
    if p15res:
        top = sorted(p15res.items(), key=lambda kv: -sum(kv[1]["clusters"].values()))[:10]
        print("p15-swept-uninventoried resurfacing (top 10):")
        for cid, v in top:
            print(f"  {sum(v['clusters'].values()):3d}  {v['channel'][:40]:40s} {cid}")
    excl = {k: v for k, v in sweep["channels"].items() if (v.get("knownAs") or "").startswith("p2f")}
    if excl:
        print(f"excluded-of-record still surfacing: {[(v['channel'], sum(v['clusters'].values())) for v in excl.values()]}")
    ranked = sorted(newc.items(), key=lambda kv: -sum(kv[1]["clusters"].values()))
    for cid, v in ranked[:40]:
        tot = sum(v["clusters"].values())
        print(f"{tot:3d}  {v['channel'][:40]:40s} {cid}  {dict(sorted(v['clusters'].items(), key=lambda x: -x[1]))}")
    print(f"\nknown channels seen (deduped): {sum(1 for v in sweep['channels'].values() if v.get('knownAs'))}")
    print(f"total distinct channels: {len(sweep['channels'])} (new: {len(newc)})")
    json.dump(sweep, open(sweep_path, "w"))


if __name__ == "__main__":
    main()
