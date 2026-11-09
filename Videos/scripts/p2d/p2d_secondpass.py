#!/usr/bin/env python3
"""P2D second pass: (1) full titles for VERIFY ids, (2) pool grep for second-pass specs,
(3) provider resolution check for DOO vs AMO mislabel in worksheet."""
import json, re

CH = "/home/z/my-project/work/channels"
POOLS = {}
for name in ("cognito", "fsl", "malmesbury", "amoeba", "doodle"):
    PROV = {"cognito": "cognito", "fsl": "freesciencelessons", "malmesbury": "malmesbury-education",
            "amoeba": "amoeba-sisters", "doodle": "doodlescience"}[name]
    d = json.load(open(f"{CH}/{name}-uploads.json"))
    for v in d["videos"]:
        if v.get("title"):
            POOLS[v["id"]] = (PROV, v["title"], v.get("duration"))

VERIFY = ["cnfamzARDrs", "RVesvXbGIC8", "9RTiFuog06s", "oYggmO-W9lQ", "HR9dM7Hg7d4",
          "nwsSl8UiozA", "XH4b0RRqPGQ", "8b_v-FlYIao", "iWWfbWJ-QMw", "UqdEzkhhuBs",
          "A_FwHV2ogRE", "XZ-MhFM3hCM", "WAA08FzArw8", "5r34nGgizDk", "WzSh6ykqn9I",
          "7zcIKkkFg1A", "W1HDDeX4cPM", "VupDd2Z2Fjg", "VHtPeQeRhJw", "8zBLPLiXK-w"]
print("=== VERIFY TITLES ===")
for vid in VERIFY:
    if vid in POOLS:
        print(f"{vid} [{POOLS[vid][0]}] {POOLS[vid][1]}")
    else:
        print(f"{vid} NOT IN POOLS")

SEARCH = {
    # bio
    "Starch": "bio:2.2.7", "Glycogen": "bio:2.2.7", "Monosaccharide": "bio:2.2.1",
    "Glucose": "bio:2.2.1", "Hydrolysis": "bio:2.2.6", "Chromosome": "bio:5.1.1",
    "Mitosis": "bio:5.2.1", "Vaccin": "bio:11.2.6", "Mitochondri": "bio:12.2.9",
    "Respirometer": "bio:12.2.14", "DCPIP": "bio:12.2.13", "Synapse": "bio:15.1.9",
    "Kidney": "bio:14.1.4", "Ultrafiltration": "bio:14.1.6", "Cardiac": "bio:8.3.4",
    "Heart Beat": "bio:8.3.4", "Gene Therapy": "bio:19.2.3", "GM ": "bio:19.3.1",
    "Alveol": "bio:9.1.7", "Ciliated": "bio:9.1.2", "Goblet": "bio:9.1.5",
    "Immobilised": "bio:3.2.4", "Chloroplast": "bio:13.1.1", "Calvin": "bio:13.1.11",
    "Plant and Animal Cells": "bio:1.2.3", "Enzyme Action": "bio:3.1.1",
    "Water Potential": "bio:4.2.x", "Michaelis": "bio:3.2.2", "Colorimeter": "bio:3.1.4",
    "Endocrine": "bio:15.1.x", "Simpson": "bio:18.2.6", "Spearman": "bio:18.2.5",
    "Glycosidic": "bio:2.2.x", "Lipid": "bio:2.2.x", "Triglyceride": "bio:2.2.9",
    # chem
    "Halogenoalkane": "chem:15.1.x/16.1.2", "Acyl Chloride": "chem:33.3.x",
    "Amine": "chem:34.1.x", "Amide": "chem:34.3.x", "Ester": "chem:18.2.x/33.2.1",
    "Nitrile": "chem:19.2.x", "Rate Equation": "chem:26.1.x", "Order of Reaction": "chem:26.1.x",
    "Arrhenius": "chem:26.1.6", "Entropy": "chem:23.3.x", "Gibbs": "chem:23.4.2",
    "Lattice Energy": "chem:23.1/23.2", "Born": "chem:23.1.4", "Electrode Potential": "chem:24.2.x",
    "Electrochemical": "chem:24.2.x", "Buffer": "chem:25.1.5", "Half Life": "chem:26.1.3",
    "Infrared": "chem:22.1.1", "NMR": "chem:37.x", "Electronegativity": "chem:3.1.x",
    "Ionic Bonding": "chem:3.2.2", "Metallic Bonding": "chem:3.3.1", "Period 3": "chem:9.2.x",
    "Halogens": "chem:11.x", "Displacement": "chem:11.2.x", "Haber": "chem:7.1.10",
    "Titration": "chem:7.2.9", "Hybridis": "chem:13.3.x", "Oxides": "chem:9.2.x",
    "Group 17": "chem:11.x", "Group 7": "chem:11.x", "Isotop": "chem:1.2.2",
    "Hydrogenation": "chem:14.1.1", "Dehydration": "chem:14.2.1", "Alcohol": "chem:16.1.x",
    "Carbonyl": "chem:17.x", "Ketone": "chem:17.1.x", "Condensation Polymer": "chem:35.1.x",
    "Polyester": "chem:35.1.1", "Polyamide": "chem:35.1.2", "Partition": "chem:25.2.x",
    "Common Ion": "chem:25.1.10", "Ka ": "chem:25.1.3", "pH ": "chem:25.1.4",
    "Proton NMR": "chem:37.4.1", "Carbon-13": "chem:37.3.1", "m/z": "chem:22.2.x",
    # physics
    "Thermistor": "phys:9.3.8", "e.m.f.": "phys:10.1.3", "EMF": "phys:10.1.3",
    "Internal Resistance": "phys:10.1.5", "Potential Divider": "phys:10.3.1",
    "Photoelectric": "phys:22.2/22.3", "Doppler": "phys:7.3.1", "SUVAT": "phys:2.1.7",
    "Equations of Motion": "phys:2.1.7", "Capacitor": "phys:19.x", "Alternating Current": "phys:21.x",
    "Friction": "phys:3.2.1", "Drag": "phys:3.2.1", "Absolute Zero": "phys:14.2.4",
    "Conduction": "phys:14.1.x", "Neutrino": "phys:11.1.9", "Beta Decay": "phys:11.1.9",
    "Photon": "phys:22.1.x", "Mass Energy": "phys:23.1.1", "Ultrasound": "phys:24.1.3",
    "Stationary Wave": "phys:8.1.2", "Standing Wave": "phys:8.1.2", "Polaris": "phys:7.5.x",
    "Progressive": "phys:7.1.6", "Magnetic Flux": "phys:20.5.1", "Motor Effect": "phys:20.2.x",
    "Circular Motion": "phys:12.x", "Gravitational Field": "phys:13.x", "Electric Field": "phys:18.x",
}
print("\n=== SECOND-PASS GREP (keyword -> pool titles) ===")
for kw, tag in SEARCH.items():
    pat = re.compile(re.escape(kw), re.I)
    hits = [(vid, p, t) for vid, (p, t, _) in POOLS.items() if pat.search(t)]
    # prioritize A-Level / relevant-subject titles
    hits.sort(key=lambda h: (not re.search(r"a[ -]?level", h[2], re.I), h[2]))
    shown = 0
    for vid, p, t in hits:
        # skip wrong-subject noise for compactness
        if re.search(r"psychology", t, re.I) and "Synapse" not in kw:
            continue
        print(f"{tag} | {kw!r} | {vid} [{p}] {t}")
        shown += 1
        if shown >= 4:
            break
