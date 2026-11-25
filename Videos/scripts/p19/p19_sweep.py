#!/usr/bin/env python3
"""P19 discovery sweep: targeted YouTube search over the POST-P18 corpus residual.

Post-P18 gap profile (gap_profile_p19.json: 2,932 unmapped of 10,814 — the P18
emit moved the residual 3,268 -> 2,932; the anchor-heavy P18 pools moved registry
counts but anchors carry zero spec weight, so the spec-point deficits in the
CONTENT classes remain the target).

All query strings are NEW relative to the P15/P17/P18 sweeps (different phrasing
and angles — a verbatim re-run would only re-harvest the already-sentineled
channels). Register/paper-code targeted per the spine's own codes + the
accumulated corrections of record (4GE1 / 4IT1 / 4XM/4XW/4XS/4XB/4XC / 4MB1 /
4CH1 / 0607 / 0680/8291 / 0455/0452 / 8021 / 0460 / 0450 / 0475-unseen /
WCH-WPH-WBI CONTENT classes / 9609 / 4SD0 / 0654).

Dedupe vs (a) all inventoried channels (inventory/channels/*-uploads.json — now
includes the P17 pools x21 + the P18 pools x21), (b) the P15 sweep's 231
harvested channels, (c) the P17 sweep's 292, and (d) the P18 sweep's 299 —
swept-but-uninventoried channels carry a sentinel: flagged, not hidden
(re-proposable WITH disclosure). Sentinel sources are the COMMITTED sweep caches
(scripts/{p15,p17,p18}/sweep.json) so the dedupe is reproducible in any sandbox.

Cache-resumable: results append to work/p19/sweep.json.

Usage: python3 p19_sweep.py [cluster ...]
"""
import json, os, subprocess, sys, glob

WORK = "/home/z/my-project/work/p19"
RES = "/home/z/my-project/repos/syllabai-resources"
os.makedirs(WORK, exist_ok=True)

# gap clusters -> queries (codes verified against the spine curricula; each
# string is NEW vs the P15/P17/P18 sweep query caches)
QUERIES = {
    "4ge1-geography-a-deep": [
        "Edexcel IGCSE Geography A 4GE1 paper 2 human fieldwork walkthrough",
        "4GE1 geography fieldwork enquiry question technique",
        "International GCSE Geography A physical world coasts revision"],
    "4ge1-topic-classes": [
        "IGCSE Geography coastal landscapes Edexcel revision topic",
        "Edexcel International GCSE geography urban economic topics",
        "4GE1 grade 9 geography exam technique"],
    "wch-unit-tails": [
        "WCH11 topic 2a ionic bonding IAL chemistry",
        "WCH12 topic 4 organic chemistry IAL unit",
        "IAL chemistry WCH13 lab skills analysis walkthrough"],
    "wch-higher-units": [
        "WCH14 rates equilibria energetics revision IAL",
        "WCH15 transition metals nitrogen organic IAL",
        "IAL chemistry unit 6 WCH16 practical revision"],
    "4it1-digital-world": [
        "Edexcel IGCSE ICT digital world online services revision",
        "4IT1 paper 1 digital design mock walkthrough",
        "Edexcel International GCSE ICT topic list living digital"],
    "wbi-content-tail": [
        "WBI11 topic 1 lifestyle health IAL biology",
        "IAL biology WBI12 development plants insects unit",
        "WBI13 WBI14 energy reproduction revision IAL"],
    "wph-content-tail": [
        "WPH11 mechanics materials waves IAL physics",
        "IAL physics WPH12 DC electricity thermal unit",
        "WPH13 further mechanics fields particles revision"],
    "wph-higher-units": [
        "WPH14 further mechanics fields and particles IAL",
        "IAL physics unit 5 thermodynamics radiation nuclear decay",
        "IAL physics unit 6 experimental methods WPH16"],
    "4ma1-h-angles": [
        "4MA1 paper 2H walkthrough higher tier",
        "IGCSE maths A harder topics grade 9 vectors proof",
        "Edexcel IGCSE maths A calculus differentiation revision"],
    "4ma1-f-angles": [
        "4MA1 foundation paper 1F walkthrough",
        "IGCSE maths foundation number percentages ratio revision",
        "Edexcel IGCSE foundation maths algebra graphs topic"],
    "lit-21-unseen-angles": [
        "IGCSE literature unseen poetry technique Cambridge",
        "unseen prose analysis passage questions IGCSE",
        "CIE 0475 literature paper 1 unseen walkthrough"],
    "em-0680-angles": [
        "IGCSE environmental management 0680 lithosphere walkthrough",
        "0680 climate oceans case studies revision",
        "IGCSE EM energy resources pollution topic class"],
    "0455-econ-angles": [
        "IGCSE economics 0455 price elasticity walkthrough",
        "Cambridge IGCSE economics paper 1 multiple choice solution",
        "0455 market failure government intervention revision"],
    "0452-accounting-angles": [
        "IGCSE accounting 0452 depreciation provision revision",
        "Cambridge IGCSE accounting partnership dissolution walkthrough",
        "0452 paper 2 financial statements walkthrough"],
    "8021-gp-angles": [
        "CIE AS general paper 8021 essay walkthrough",
        "general paper comprehension note making AS level",
        "8021 global issues topic revision environment"],
    "8291-em-angles": [
        "8291 environmental management AS topic revision",
        "AS environmental management 8291 paper 2 walkthrough",
        "Cambridge AS EM atmosphere hydrosphere lithosphere"],
    "0654-coordinated": [
        "0654 co-ordinated science physics revision IGCSE",
        "coordinated science IGCSE chemistry biology walkthrough",
        "0654 paper 4 extended walkthrough"],
    "0620-chem-angles": [
        "IGCSE chemistry 0620 organic chemistry crude oil revision",
        "0620 electrolysis redox topic walkthrough",
        "Cambridge IGCSE chemistry paper 4 extended solution"],
    "modular-4xm-angles": [
        "Edexcel modular maths higher unit 2 4XM1 revision",
        "IGCSE maths modular foundation unit tests walkthrough",
        "4XM1 unit 3 algebra and graphs"],
    "modular-science-4xs": [
        "4XS1 modular science biology unit revision",
        "4XB1 4XC1 modular science unit walkthrough",
        "Edexcel IGCSE science modular physics unit 4XW1"],
    "0625-physics-angles": [
        "IGCSE physics 0625 moments momentum revision",
        "Cambridge IGCSE physics paper 4 extended walkthrough",
        "0625 thermal physics circuits topic class"],
    "0460-geo-angles": [
        "IGCSE geography 0460 population migration revision",
        "Cambridge IGCSE geography paper 2 skills walkthrough",
        "0460 rivers coasts geomorphic processes topic"],
    "9609-business-angles": [
        "CIE A level business 9609 paper 1 walkthrough",
        "9609 business unit 1 enterprise revision",
        "A level business Cambridge marketing operations revision"],
    "4mb1-angles": [
        "IGCSE maths B 4MB1 sets functions revision",
        "Edexcel IGCSE maths B paper 2 walkthrough",
        "4MB1 algebra calculus geometry topic class"],
    "0607-intl-maths-angles": [
        "0607 international maths paper 4 investigation walkthrough",
        "Cambridge international mathematics functions graphs revision",
        "0607 paper 6 project modelling walkthrough"],
    "4sd0-double-award": [
        "Edexcel IGCSE double award science 4SD0 biology revision",
        "4SD0 chemistry physics topic walkthrough",
        "IGCSE double award science paper walkthrough Edexcel"],
    "0417-ict-angles": [
        "IGCSE ICT 0417 paper 2 problem solving walkthrough",
        "Cambridge IGCSE ICT theory revision hardware software",
        "0417 databases spreadsheets practical revision"],
    "0610-bio-angles": [
        "IGCSE biology 0610 inheritance genetics revision",
        "Cambridge IGCSE biology paper 4 extended walkthrough",
        "0610 coordination homeostasis topic class"],
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
    # committed sweep caches of record as sentinels (deterministic, any sandbox)
    for prior_path, tag in (
            (RES + "/Videos/scripts/p15/sweep.json", "p15-swept-uninventoried"),
            (RES + "/Videos/scripts/p17/sweep.json", "p17-swept-uninventoried"),
            (RES + "/Videos/scripts/p18/sweep.json", "p18-swept-uninventoried")):
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
