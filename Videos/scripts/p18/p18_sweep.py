#!/usr/bin/env python3
"""P18 discovery sweep: targeted YouTube search over the POST-P17 corpus residual.

Post-P17 gap profile (gap_profile_p18.json: 3,268 unmapped of 10,814 — the P17
emit moved the residual 3,668 -> 3,268; the anchor-heavy P17 pools moved registry
counts but anchors carry zero spec weight, so the spec-point deficits in the
CONTENT classes remain the target).

Register/paper-code targeted per the spine's own codes + the accumulated
corrections of record (4GE1 not 4GE0, 4IT1 not 4IT0, modular 4XM/4XW/4XS/4XB/
4XC/4WS, 4MB1, 4CH1, 0607, 0680/8291, 0455/0452, 8021, 0460, 0475-unseen,
IAL WCH/WPH/WBI CONTENT classes — the P17 IAL pools were paper-walkthrough
registers; this sweep targets the topic/revision register for the unit tails).

Dedupe vs (a) all inventoried channels (inventory/channels/*-uploads.json — now
includes the P17 pools x21), (b) the P15 sweep's 231 harvested channels, and
(c) the P17 sweep's 292 harvested channels — swept-but-uninventoried channels
carry a sentinel: flagged, not hidden (re-proposable WITH disclosure).

Cache-resumable: results append to work/p18/sweep.json.

Usage: python3 p18_sweep.py [cluster ...]
"""
import json, os, subprocess, sys, glob

WORK = "/home/z/my-project/work/p18"
RES = "/home/z/my-project/repos/syllabai-resources"
P15 = "/home/z/my-project/work/p15/sweep.json"
P17 = "/home/z/my-project/work/p17/sweep.json"
os.makedirs(WORK, exist_ok=True)

# gap clusters -> queries (codes verified against the spine curricula at main cb0f9c3f)
QUERIES = {
    "edexcel-igcse-geography-4ge1": [
        "Edexcel IGCSE geography A 4GE1 revision", "4GE1 paper 1 walkthrough",
        "IGCSE geography A Edexcel coasts topic", "4GE1 fieldwork paper"],
    "ial-chemistry-content-wch": [
        "IAL chemistry WCH11 topic 1 bonding revision", "WCH12 unit 2 chemistry IAL topic",
        "IAL chemistry WCH13 organic content", "WCH14 WCH15 WCH16 chemistry unit revision"],
    "cie-igcse-em-0680": [
        "IGCSE environmental management 0680 revision topic", "0680 atmosphere hydrosphere lithosphere",
        "IGCSE EM 0680 case study walkthrough"],
    "edexcel-igcse-ict-4it1": [
        "4IT1 digital world revision", "Edexcel IGCSE ICT paper 1 walkthrough digital world",
        "4IT1 paper 2 applied ICT walkthrough"],
    "ial-biology-content-wbi": [
        "IAL biology WBI11 topic revision", "WBI12 unit 2 biology IAL content",
        "IAL biology WBI13 WBI14 topic walkthrough"],
    "ial-physics-content-wph": [
        "IAL physics WPH11 topic revision", "WPH12 unit 2 physics IAL waves",
        "IAL physics WPH13 WPH14 content walkthrough", "IAL physics unit 5 WPH15 thermodynamics revision"],
    "4ma1-higher-content": [
        "IGCSE maths A higher 4MA1 full topic revision", "4MA1 vectors calculus trigonometry revision",
        "Edexcel IGCSE higher maths grade 9 topic walkthrough"],
    "4ma1-foundation-content": [
        "4MA1 foundation revision topics", "IGCSE maths A foundation 1F walkthrough",
        "Edexcel foundation maths IGCSE number algebra revision"],
    "cie-igcse-geography-0460": [
        "Cambridge IGCSE geography 0460 revision", "0460 population settlement topic",
        "0460 paper 2 geography skills walkthrough"],
    "cie-igcse-economics-0455": [
        "Cambridge IGCSE economics 0455 revision topic", "0455 paper 2 structured walkthrough",
        "IGCSE economics 0455 demand supply revision"],
    "cie-igcse-accounting-0452": [
        "Cambridge IGCSE accounting 0452 revision", "0452 accounting paper 1 walkthrough",
        "IGCSE accounting partnership accounts revision"],
    "cie-as-general-paper-8021": [
        "AS level general paper 8021 essay revision", "8021 comprehension walkthrough",
        "Cambridge general paper content revision"],
    "cie-a-level-economics-9708-tail": [
        "CIE A2 economics 9708 paper 4 revision", "9708 A2 topic content walkthrough",
        "A level economics 9708 theory revision"],
    "cie-igcse-chemistry-0620-tail": [
        "Cambridge IGCSE chemistry 0620 topic revision", "0620 paper 6 alternative to practical",
        "IGCSE chemistry 0620 organic electrolysis revision"],
    "cie-igcse-physics-0625-tail": [
        "Cambridge IGCSE physics 0625 topic revision", "0625 paper 6 alternative to practical",
        "IGCSE physics 0625 paper 4 walkthrough"],
    "cie-international-maths-0607": [
        "Cambridge 0607 international mathematics investigation", "0607 maths revision topic",
        "IGCSE international maths 0607 paper 4"],
    "edexcel-modular-tails": [
        "Edexcel IGCSE maths modular 4XM1 unit 2 revision", "IGCSE science modular 4XS1 4XB1 4XC1 unit",
        "4XW1 modular double award unit walkthrough"],
    "edexcel-igcse-maths-b-4mb1": [
        "Edexcel IGCSE maths B 4MB1 revision", "4MB1 paper walkthrough topic"],
    "edexcel-double-award-17-tails": [
        "Edexcel IGCSE science double award revision topic", "4SD0 double award biology chemistry physics revision"],
    "cie-igcse-business-0450": [
        "Cambridge IGCSE business 0450 revision topic", "0450 business paper 2 case study walkthrough"],
    "cie-igcse-further-maths": [
        "Cambridge IGCSE further pure mathematics revision", "4PM0 IGCSE further maths topic walkthrough"],
    "cie-as-em-8291": [
        "AS environmental management 8291 revision", "Cambridge AS level EM content walkthrough"],
    "lit-0475-unseen-spine": [
        "0475 unseen poetry prose analysis", "IGCSE literature 0475 set text essay walkthrough",
        "songs of ourselves volume 1 part 4 analysis"],
    "cie-igcse-biology-0610-tail": [
        "Cambridge IGCSE biology 0610 topic revision", "0610 paper 6 alternative to practical"],
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
    for prior_path, tag in ((P15, "p15-swept-uninventoried"), (P17, "p17-swept-uninventoried")):
        if os.path.exists(prior_path):
            prior = json.load(open(prior_path))
            for cid in prior.get("channels", {}):
                # swept-but-uninventoried channels carry a sentinel: flagged, not
                # hidden — a corrected-code cluster hitting one hard is re-proposable
                # WITH the disclosure (nothing silently dropped).
                ucs.setdefault(cid, tag)
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
    resurf = {k: v for k, v in sweep["channels"].items()
              if (v.get("knownAs") or "").endswith("-swept-uninventoried")}
    if resurf:
        top = sorted(resurf.items(), key=lambda kv: -sum(kv[1]["clusters"].values()))[:10]
        print("swept-uninventoried resurfacing (top 10):")
        for cid, v in top:
            print(f"  {sum(v['clusters'].values()):3d}  {v.get('knownAs')[:4]}  {v['channel'][:36]:36s} {cid}")
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
