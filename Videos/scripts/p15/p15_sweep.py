#!/usr/bin/env python3
"""P15 discovery sweep: targeted YouTube search over the corpus gap registers.

Per gap cluster, run ytsearch queries and harvest (channelId, channel, title)
rows. Aggregates per-channel hit counts per cluster, dedupes against the known
channel set (all prior lane inventories + P14 pools), ranks candidates by
register density. Cache-resumable: results append to work/p15/sweep.json.

Usage: python3 p15_sweep.py [cluster ...]
"""
import json, os, re, subprocess, sys, glob

WORK = "/home/z/my-project/work/p15"
RES = "/home/z/my-project/repos/syllabai-resources"
os.makedirs(WORK, exist_ok=True)

# gap clusters -> queries (register + paper-code targeted; ANCHOR-GRANULARITY spine only)
QUERIES = {
    "cie-igcse-biology-0610": [
        "IGCSE biology 0610 past paper", "CIE IGCSE biology paper 2 walkthrough",
        "IGCSE biology 0610 paper 4", "IGCSE biology paper 6 alternative to practical",
        "CIE IGCSE biology revision topic"],
    "cie-igcse-coordinated-0654": [
        "coordinated science double award IGCSE", "0654 coordinated science biology",
        "IGCSE double award science paper"],
    "edexcel-igcse-geography-4ge0": [
        "Edexcel IGCSE geography 4GE0", "Edexcel IGCSE geography paper 1",
        "Edexcel IGCSE geography revision"],
    "ial-physics-wph": [
        "Edexcel IAL physics unit 1 WPH11", "IAL physics unit 2 walkthrough",
        "Edexcel international A level physics past paper"],
    "ial-biology-wbi": [
        "Edexcel IAL biology unit 1", "IAL biology unit 2 walkthrough",
        "Edexcel international A level biology past paper"],
    "ial-chemistry-wch": [
        "Edexcel IAL chemistry unit 2", "WCH12 walkthrough",
        "IAL chemistry unit 4 past paper"],
    "cie-igcse-accounting-0452": [
        "Cambridge IGCSE accounting 0452", "IGCSE accounting past paper walkthrough",
        "IGCSE accounting 0452 paper 1"],
    "cie-igcse-economics-0455": [
        "Cambridge IGCSE economics 0455", "IGCSE economics paper 2 walkthrough",
        "IGCSE economics 0455 revision"],
    "cie-igcse-em-0680": [
        "Cambridge IGCSE environmental management 0680", "IGCSE environmental management paper"],
    "cie-igcse-ict-0417": [
        "Cambridge IGCSE ICT 0417", "IGCSE ICT paper 2 walkthrough"],
    "edexcel-igcse-ict-4it0": [
        "Edexcel IGCSE ICT 4IT0", "Edexcel IGCSE ICT paper"],
    "cie-igcse-geography-0460": [
        "Cambridge IGCSE geography 0460", "IGCSE geography paper 2 walkthrough"],
    "cie-igcse-physics-0625": [
        "Cambridge IGCSE physics 0625 past paper", "IGCSE physics 0625 paper 4",
        "CIE IGCSE physics revision topic"],
    "cie-igcse-chemistry-0620": [
        "Cambridge IGCSE chemistry 0620 past paper", "IGCSE chemistry 0620 paper 4"],
    "edexcel-igcse-maths-4ma1": [
        "Edexcel IGCSE maths 4MA1 higher walkthrough", "IGCSE maths A paper 1H",
        "Edexcel IGCSE maths modular unit"],
    "cie-a-level-business-9609": [
        "Cambridge A level business 9609", "A level business 9609 paper 1 walkthrough"],
    "cie-a-level-economics-9708": [
        "Cambridge A level economics 9708 paper", "A level economics 9708 paper 4 walkthrough"],
    "cie-as-gp-8021": [
        "AS general paper 8021", "Cambridge general paper essay"],
    "cie-as-em-8291": [
        "AS environmental management 8291", "Cambridge AS environmental management"],
    "cie-igcse-addmaths-0606": [
        "CIE additional mathematics 0606", "add maths 0606 paper 1 walkthrough"],
    "cie-igcse-fle-0500": [
        "IGCSE first language english 0500", "0500 paper 2 directed writing"],
    "edexcel-igcse-chemistry-4ch0": [
        "Edexcel IGCSE chemistry 4CH0", "Edexcel IGCSE chemistry paper 1C walkthrough"],
    "cie-igcse-lit-0475": [
        "IGCSE literature english 0475", "Songs of ourselves analysis"],
    "cie-igcse-combined-0653": [
        "Cambridge combined science 0653 IGCSE"],
}

def known_ucs():
    ucs = {}
    for f in glob.glob(RES + "/Videos/inventory/channels/*-uploads.json"):
        d = json.load(open(f))
        cid = d.get("channelId")
        if cid:
            ucs[cid] = os.path.basename(f).replace("-uploads.json", "")
    return ucs

def search(q, n=15):
    try:
        p = subprocess.run(["yt-dlp", "--flat-playlist", "--no-warnings", "-i",
                            "--print", "%(channel_id)s\\t%(channel)s\\t%(title)s",
                            f"ytsearch{n}:{q}"],
                           capture_output=True, text=True, timeout=150)
    except subprocess.TimeoutExpired:
        return []
    rows = []
    for l in (p.stdout or "").splitlines():
        if "\\t" in l:
            parts = l.split("\\t", 2)
        elif "\t" in l:
            parts = l.split("\t", 2)
        else:
            continue
        if len(parts) == 3 and parts[0].startswith("UC"):
            rows.append({"channelId": parts[0], "channel": parts[1], "title": parts[2]})
    return rows

def main():
    sweep_path = os.path.join(WORK, "sweep.json")
    sweep = json.load(open(sweep_path)) if os.path.exists(sweep_path) else {"queries": {}, "channels": {}}
    known = known_ucs()
    clusters = sys.argv[1:] or list(QUERIES)
    for cl in clusters:
        for q in QUERIES[cl]:
            if f"{cl}::{q}" in sweep["queries"]:
                continue
            rows = search(q)
            sweep["queries"][f"{cl}::{q}"] = {"n": len(rows), "rows": rows}
            print(f"[{cl}] {q!r} -> {len(rows)} hits", flush=True)
            for r in rows:
                c = sweep["channels"].setdefault(r["channelId"], {
                    "channel": r["channel"], "clusters": {}, "titles": [], "knownAs": known.get(r["channelId"])})
                c["clusters"][cl] = c["clusters"].get(cl, 0) + 1
                if len(c["titles"]) < 4:
                    c["titles"].append(r["title"])
            json.dump(sweep, open(sweep_path, "w"))

    # report
    print("\n=== per-channel cluster density (new channels only, >=2 cluster hits) ===")
    newc = {k: v for k, v in sweep["channels"].items() if not v.get("knownAs")}
    ranked = sorted(newc.items(), key=lambda kv: -sum(kv[1]["clusters"].values()))
    for cid, v in ranked[:40]:
        tot = sum(v["clusters"].values())
        print(f"{tot:3d}  {v['channel'][:40]:40s} {cid}  {dict(sorted(v['clusters'].items(), key=lambda x:-x[1]))}")
    print(f"\nknown channels seen in sweep (deduped): {sum(1 for v in sweep['channels'].values() if v.get('knownAs'))}")
    print(f"total distinct channels: {len(sweep['channels'])} (new: {len(newc)})")
    json.dump(sweep, open(sweep_path, "w"))

if __name__ == "__main__":
    main()
