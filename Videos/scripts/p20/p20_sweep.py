#!/usr/bin/env python3
"""P20 discovery sweep: targeted YouTube search over the POST-P19 corpus residual.

Post-P19 gap profile (gap_profile_p20.json: 2,660 unmapped of 10,814 — the P19
emit moved the residual 2,932 -> 2,660; the anchor-heavy P19 registers carry zero
spec weight, so the CONTENT-class deficits remain the target: 4GE1 183, WCH 164,
4IT1 109, WBI 107, WPH 102, 4MA1-H 100, lit-21 unseen 96, 4MA1-F 95, 0452 71,
GP-21 70, 8291 64, the modular ladders, the combined-23 trio, 0460 48+37, the
0607 content class, the 9700/9708/9709/9701/9618/9609 A-level families).

All query strings are NEW relative to the P15/P17/P18/P19 sweeps — machine-checked
against the four committed caches below — so the deduped channels are sentinel
resurfacing, not re-harvest. Register/topic-class targeted per the spine's own
codes + the accumulated corrections of record (the P19 honest calls: the ginger
"4MA1 x159" family was CIE 0580, so 4MA1 queries carry Edexcel-specific tokens).

Dedupe vs (a) all inventoried channels (inventory/channels/*-uploads.json — now
includes the P19 pools x25), (b) the P15 sweep's 231 harvested channels, (c) the
P17 sweep's 292, (d) the P18 sweep's 299, and (e) the P19 sweep's 389 —
swept-but-uninventoried channels carry a sentinel: flagged, not hidden
(re-proposable WITH disclosure). Sentinel sources are the COMMITTED sweep caches
(scripts/{p15,p17,p18,p19}/sweep.json) so the dedupe is reproducible in any sandbox.

Cache-resumable: results append to work/p20/sweep.json.

Usage: python3 p20_sweep.py [cluster ...]
"""
import json, os, subprocess, sys, glob

WORK = "/home/z/my-project/work/p20"
RES = "/home/z/my-project/repos/syllabai-resources"
os.makedirs(WORK, exist_ok=True)

# gap clusters -> queries (codes verified against the spine curricula; each
# string is NEW vs the P15/P17/P18/P19 sweep query caches)
QUERIES = {
    "4ge1-case-classes": [
        "Edexcel IGCSE geography 4GE1 case study series",
        "international GCSE geography tectonics hazards topic class Edexcel",
        "4GE1 geography economic activity globalisation topic class"],
    "4ge1-pearson-angles": [
        "Pearson Edexcel international GCSE geography A revision",
        "Edexcel international GCSE geography river processes class",
        "IGCSE geography Edexcel urban fieldwork human geography class"],
    "wch-unit-classes": [
        "IAL chemistry formulas equations moles class WCH11",
        "WCH12 organic chemistry names reactions revision IAL",
        "IAL chemistry enthalpy entropy rates WCH14 topic class"],
    "wch-analysis-classes": [
        "IAL chemistry spectroscopy chromatography WCH15 analysis",
        "Edexcel IAL chemistry exam paper debrief walkthrough",
        "IAL chemistry unit 3 organic trends WCH13 class"],
    "wbi-unit-classes": [
        "IAL biology membranes transport WBI11 class",
        "WBI12 cardiovascular plant transport revision IAL biology",
        "IAL biology photosynthesis respiration WBI14 revision"],
    "wbi-higher-classes": [
        "IAL biology genetics evolution WBI15 topic class",
        "Edexcel IAL biology unit 6 lab debrief WBI16",
        "IAL biology immune system vaccination walkthrough"],
    "wph-classes": [
        "IAL physics fluids viscosity Stokes class WPH",
        "WPH11 waves optics class Edexcel IAL",
        "IAL physics capacitors magnetic fields WPH13 class"],
    "4it1-skills-classes": [
        "Edexcel international GCSE ICT spreadsheet database exam skills",
        "4IT1 online world email safety skills revision",
        "ICT Edexcel IGCSE web design html unit class"],
    "lit-unseen-craft": [
        "unseen poetry essay structure IGCSE literature",
        "IGCSE English literature analysis unseen prose technique",
        "Cambridge literature paper unseen poetry prose lesson"],
    "4ma1-topic-classes": [
        "Edexcel IGCSE maths A set language probability class",
        "4MA1 higher sequences surds indices revision",
        "IGCSE maths A differentiation kinematics higher walkthrough"],
    "4ma1-foundation-classes": [
        "4MA1 foundation decimals angles measures topic class",
        "IGCSE maths A foundation ratio proportion class",
        "Edexcel IGCSE maths A foundation statistics class"],
    "4mb1-more": [
        "IGCSE maths B set functions graphs class",
        "4MB1 calculus differentiation integration class",
        "Edexcel maths B matrices networks walkthrough"],
    "gp-8021-craft": [
        "general paper AS level essay plan examples CIE 8021",
        "8021 general paper reading comprehension answers",
        "general paper global perspective topics class AS"],
    "8291-topic-classes": [
        "8291 environmental management lithosphere soil revision",
        "AS environmental management energy industry 8291 class",
        "Cambridge 8291 atmosphere global climate walkthrough"],
    "0460-topic-classes": [
        "0460 IGCSE geography earthquake volcano case class",
        "Cambridge IGCSE geography rivers landforms walkthrough",
        "IGCSE geography 0460 industry tourism theme class"],
    "0460-urban-classes": [
        "0460 population structure settlement services revision",
        "IGCSE geography Cambridge 0460 exam skills paper class",
        "Cambridge IGCSE geography weather climate class"],
    "0607-content-classes": [
        "0607 international maths number algebra topic class",
        "Cambridge 0607 maths geometry measurement revision",
        "international maths probability statistics 0607 class"],
    "combined-0653-classes": [
        "0653 combined science biology topic class IGCSE",
        "combined science chemistry reactions revision Cambridge 0653",
        "IGCSE combined science physics electricity waves class"],
    "modular-maths-classes": [
        "modular maths 4XM1 unit 1 number class",
        "IGCSE maths modular higher unit 2 geometry walkthrough",
        "modular maths foundation unit 3 number revision class"],
    "modular-science-classes": [
        "modular science biology unit 2 responses class Edexcel",
        "modular science chemistry unit 1 states class",
        "IGCSE modular physics unit 2 electricity class"],
    "modular-da-classes": [
        "double award modular biology unit 1 class Edexcel",
        "double award modular chemistry unit 2 walkthrough",
        "double award modular physics unit 3 class"],
    "4sd0-classes": [
        "4SD0 biology movement energy class Edexcel",
        "double award chemistry 4SD0 bonding acids class",
        "4SD0 physics astrophysics forces class walkthrough"],
    "0620-topic-classes": [
        "IGCSE chemistry mole stoichiometry walkthrough 0620",
        "0620 chemistry metals reactivity series class",
        "Cambridge IGCSE chemistry acids bases salts walkthrough"],
    "9700-alevel-bio": [
        "CIE A level biology 9700 energy respiration class",
        "9700 A level biology genetics inheritance walkthrough",
        "A level biology Cambridge 9700 paper 2 debrief"],
    "9708-alevel-econ": [
        "9708 economics basic economic ideas class CIE",
        "A level economics Cambridge price mechanism walkthrough",
        "9708 economics government macro intervention class"],
    "9709-pure-maths": [
        "9709 pure mathematics functions quadratics class",
        "CIE A level maths circular measure trigonometry class",
        "9709 pure maths paper 2 integration walkthrough"],
    "0625-physics-classes": [
        "IGCSE physics forces motion class 0625",
        "Cambridge IGCSE physics light sound waves walkthrough",
        "0625 electromagnetism motors transformers class"],
    "9701-alevel-chem": [
        "9701 chemistry atomic structure bonding class",
        "CIE A level chemistry reaction kinetics equilibria walkthrough",
        "9701 chemistry analysis spectroscopy class"],
    "9618-alevel-cs": [
        "9618 computer science data representation class",
        "CIE A level computer science programming pseudocode class",
        "9618 networks internet security walkthrough"],
    "9609-business-classes": [
        "9609 business human resource management class CIE",
        "A level business 9609 operations methods class",
        "9609 business paper 3 case study walkthrough"],
    "0606-add-maths": [
        "0606 additional maths functions quadratics class",
        "Cambridge additional mathematics differentiation integration class",
        "0606 add maths vectors relative velocity walkthrough"],
    "0452-0455-classes": [
        "0452 accounting incomplete records manufacturing class",
        "IGCSE accounting payroll co-operative class walkthrough",
        "0455 economics inflation unemployment class IGCSE"],
    "9706-alevel-acc": [
        "9706 A level accounting costing class",
        "CIE A level accounting financial statements walkthrough",
        "9706 prepayment accruals adjustment class"],
    "0455-econ-more": [
        "IGCSE economics firm costs revenues class 0455",
        "0455 economics trade globalisation revision Cambridge",
        "Cambridge IGCSE economics population workforce class"],
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


def prior_query_strings():
    """All query strings from the four committed sweep caches (the all-new law)."""
    prior = set()
    for tag in ("p15", "p17", "p18", "p19"):
        path = os.path.join(RES, "Videos", "scripts", tag, "sweep.json")
        d = json.load(open(path))
        for k in d["queries"]:
            q = k.split("::", 1)[1].strip().lower()
            prior.add(q)
    return prior


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
            (RES + "/Videos/scripts/p18/sweep.json", "p18-swept-uninventoried"),
            (RES + "/Videos/scripts/p19/sweep.json", "p19-swept-uninventoried")):
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
    # ALL-NEW law: every P20 query string must be new vs the P15/P17/P18/P19 caches
    prior = prior_query_strings()
    coll = [q for qs in QUERIES.values() for q in qs if q.strip().lower() in prior]
    if coll:
        print("ALL-NEW LAW VIOLATION — these strings exist in a prior cache:")
        for q in coll:
            print("  !", q)
        sys.exit(1)
    nq = sum(len(v) for v in QUERIES.values())
    print(f"all-new law PASS: {nq} queries, 0 collisions vs {len(prior)} prior strings")

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
    for cid, v in ranked[:45]:
        tot = sum(v["clusters"].values())
        print(f"{tot:3d}  {v['channel'][:40]:40s} {cid}  {dict(sorted(v['clusters'].items(), key=lambda x: -x[1]))}")
    print(f"\nknown channels seen (deduped): {sum(1 for v in sweep['channels'].values() if v.get('knownAs'))}")
    print(f"total distinct channels: {len(sweep['channels'])} (new: {len(newc)})")
    json.dump(sweep, open(sweep_path, "w"))


if __name__ == "__main__":
    main()
