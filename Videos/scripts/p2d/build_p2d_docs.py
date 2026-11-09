#!/usr/bin/env python3
"""P2D docs: review-file-external-p2d.md + tracker P2D section + README status row."""
import json, sys, datetime

sys.path.insert(0, "/home/z/my-project/scripts")
from p2d_bindings import BIO, CHEM, PHYS
CH = "/home/z/my-project/work/channels"
RES = "/home/z/my-project/repos/syllabai-resources"

summ = json.load(open(f"{CH}/p2d-summary.json"))
oemb = json.load(open(f"{CH}/candidate-oembed-p2d.json"))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

COURSES = [("cie-a-level-biology-25", BIO, "A Level Biology (9700)"),
           ("cie-a-level-chemistry-25", CHEM, "A Level Chemistry (9701)"),
           ("cie-a-level-physics-25", PHYS, "A Level Physics (9702)")]

GAPS = {
"cie-a-level-biology-25": [
 "enzyme kinetics detail: Vmax/Michaelis-Menten derivation (3.2.2), immobilised-enzyme alginate practical (3.2.4)",
 "protein-interaction chemistry (2.3.3 hydrophobic/ionic/H-bond clauses) — GCSE bonding videos do not carry it",
 "gas-exchange histology clauses (9.1.2/9.1.3/9.1.5/9.1.6 cartilage, ciliated epithelium, goblet cells)",
 "chloride shift (8.2.2) — only the broader CO2-transport video is bound (low)",
 "Calvin-cycle stages (13.1.11/13.1.12) and photophosphorylation detail (13.1.10 partial)",
 "investigative clauses: DCPIP/redox indicators (12.2.13, 13.2.3), respirometer design detail, photosynthesis practicals (13.2.4)",
 "statistics: Spearman/Pearson correlation (18.2.5); conservation bodies/IUCN (18.3.6)",
 "biotech: gene therapy + SCID (19.2.3), GM crops for food security (19.3.1), DELLA proteins (16.3.4), marker genes detail",
 "test crosses (16.2.4) — Punnett videos bound cover monohybrid/dihybrid skills but not the test-cross frame",
],
"cie-a-level-chemistry-25": [
 "Period 3 and its oxides/chlorides (9.2.x, 9.3.x) — no aligned FSL videos exist in the pools",
 "entropy and Gibbs free energy (23.3.x, 23.4.x), lattice energy + Born-Haber cycles (23.1.x, 23.2.x)",
 "electrochemistry: standard electrode potentials, cells, electrolysis calculations (24.1.x detail, 24.2.x)",
 "rate equations: order, rate constants, half-life, initial-rates, Arrhenius (26.1.2-26.1.6)",
 "acid-base detail: Kp (7.1.7/7.1.8), buffers (25.1.5), Ka/pKa definitions (25.1.3), titration curves (7.2.9 partial)",
 "nitrogen chemistry: amines, diazonium, azo compounds (34.x); acyl chlorides (33.3.x); esters (18.2.x, 33.2.x)",
 "transition-metal complex ions, ligand exchange, stereochemistry (28.2.x, 28.3.x detail, 28.4.x, 28.5.x)",
 "carbon-13/proton NMR (37.x); mass-spectrometry working detail (22.2.x partial)",
],
"cie-a-level-physics-25": [
 "kinematics formulas: SUVAT equations, projectile motion (2.1.6-2.1.8) — only graph skills bound",
 "moments/torque equilibrium (4.2.x, 4.3.x detail); work-energy theorem (5.x detail)",
 "DC circuits: e.m.f. vs p.d., internal resistance, potential divider, potentiometer (10.1.3-10.1.5, 10.3.1/10.3.2)",
 "Kirchhoff laws as statements (10.2.1/10.2.2 — only series/parallel applications bound)",
 "capacitors: capacitance, energy, charge/discharge exponentials, smoothing (19.x) — zero aligned videos in pools",
 "quantum: photoelectric effect detail, photon momentum, de Broglie, energy levels in emission spectra (22.x detail)",
 "magnetic fields due to currents, force between conductors, charged particles in B-fields (20.2.x-20.4.x detail)",
 "waves: Doppler, Malus's law, stationary-wave detail, superposition/interference (7.3.x, 7.5.2, 8.x)",
 "oscillations: omega formulas, damping, forced resonance (17.2.3/17.2.4, 17.3.x); ideal-gas derivation (15.3.1c)",
 "E=mc^2 and binding energy (23.1.x detail); applied options: ultrasound/CT (24.x), standard candles/Hubble (25.x partial)",
],
}

lines = []
lines.append("# Review file — P2D CIE A-level external-channels lane (T-VIDEOMAP-P2D)\n")
lines.append(f"**All rows `reviewed: false` — nothing enters `content/` without your ruling.** Same law as P2/P2B/P2C. Generated {NOW}.\n")
lines.append("Bundles: **3 per-course drafts, "
             f"{sum(s['rows'] for s in summ.values())} mapping rows over "
             f"{sum(s['videos'] for s in summ.values())} distinct video slots** (identity **264/264**: "
             "104 oEmbed + 160 thumbnail-fallback).\n")
lines.append("**Why this lane exists:** the P2C tracker deferred the CIE A-level trio — \"AQA<->CIE A-level divergence "
             "too sharp for title-only binding; needs a dedicated lane — and c3/p3 have NO site videos so channels "
             "are unavoidable there\". This is that dedicated lane, run more conservatively than P2C: bind only where "
             "the candidate title names the spec's distinctive content; everything else left honestly unmapped.\n")
lines.append("**Evidence posture:** channel flat-playlist enumeration + oEmbed identity. NEW FINDING vs P2C: "
             "freesciencelessons has disabled embedding on most of its A-level videos (oEmbed returns 401 "
             "Unauthorized where its GCSE videos still verify). For those 160 videos identity was confirmed by "
             "i.ytimg.com thumbnail liveness (bogus ids 404; these 200) + the first-party yt-dlp uploads-playlist "
             "enumeration (titles/durations come from the channel itself). Each draft video records `identityMethod`: "
             "`oembed` or `thumb-fallback`. **No high rows anywhere** — title-only evidence cannot earn high.\n")
lines.append("**Board note:** FSL is AQA-aligned; every FSL row carries `boardMismatch:true` for you to weigh. "
             "Cognito rows are channel-only videos (its site pages own the rest). Doodle Science contributes "
             "A-Level Physics explainers (a channel P2B excluded as GCSE-only — its A-Level Physics playlist "
             "changes that for this lane). Amoeba Sisters (US) and Malmesbury (required practicals) are low-yield "
             "but occasionally exact.\n")

for course, rows, label in COURSES:
    s = summ[course]
    lines.append(f"\n---\n\n## {label} — {s['total']} specs, {s['specs']} drafted ({round(100*s['specs']/s['total'])}%)\n")
    lines.append(f"Rows: {s['rows']} ({s['medium']} medium / {s['low']} low) · videos: {s['videos']} · "
                 f"draft: `Videos/drafts/{course}/video-map.draft.external.json`\n")
    for conf, header in (("medium", "MEDIUM"), ("low", "LOW")):
        lines.append(f"\n**{header}**\n")
        for vid, prov, specs, c, ev in rows:
            if c != conf:
                continue
            t = oemb[vid]["title"]
            dur = ""
            lines.append(f"- [ ] **{t}** — video `{vid}` ({prov}) → specs `{', '.join(specs)}`\n"
                         f"      evidence: {ev}\n"
                         f"      source: https://www.youtube.com/watch?v={vid}\n")
    lines.append(f"\n**Notable honest gaps** (no defensible title-only candidate; left unmapped):\n")
    for g in GAPS[course]:
        lines.append(f"- {g}\n")

lines.append("\n---\n\n## Validation gates (all green before write)\n")
lines.append("- spec codes resolved against the real CIE spines (`apps/hub/spines/cie-a-level-*.json`) — gate caught "
             "2 wrong guesses (17.2.1/17.2.2 -> real codes 17.1.4/17.1.5) and one reduction-spec misfile (now 16.1.1(d))\n"
             "- cognito channel-only guard: gate rejected 6 Cognito rows that are already surfaced on cognitoedu.org "
             "(site lane owns them) — removed\n"
             "- provider cross-check against the uploads pools; confidence whitelist medium/low; no (video,spec) dupes per course\n"
             "- identity 264/264 (104 oEmbed + 160 thumb-fallback after FSL 401s)\n")
lines.append("\n## Review protocol\n")
lines.append("1. Walk the checkboxes per course; strike anything where the title-only case does not convince you.\n"
             "2. Verdicts land in `owner-review-verdicts.json` (same format as igcse-biology-19) before any flag flip.\n"
             "3. c3/p3 have no site videos: if you approve rows here, the hub video lane for chemistry/physics A-level "
             "starts existing at all. b3 (biology) still owes its P2-method site-alignment pass — these rows are a "
             "supplement, not a substitute.\n")

open(f"{RES}/Videos/drafts/review-file-external-p2d.md", "w").write("".join(lines))
print("review file written:", len("".join(lines)), "chars")

# tracker append
tr = open(f"{RES}/Videos/trackers/P2-ALIGNMENT-TRACKER.md").read()
p2d = f"""
## P2D — CIE A-level external-channels lane (2026-11-09, T-VIDEOMAP-P2D)

The dedicated lane P2C deferred. Same title-only evidence posture, tightened binding rule (title must name the
spec's distinctive content), no high rows, every row `reviewed:false` + `boardMismatch:true`.

**P2D drafts:**

| Course | Specs | Rows (M/L) | Distinct specs drafted |
| --- | --- | --- | --- |
| cie-a-level-biology-25 | 257 | 139 (104/35) | 145 (56%) |
| cie-a-level-chemistry-25 | 356 | 103 (75/28) | 127 (36%) |
| cie-a-level-physics-25 | 303 | 61 (46/15) | 76 (25%) |

Identity: **264/264** — 104 oEmbed + 160 thumbnail-fallback. NEW: freesciencelessons disabled embedding on most
A-level videos (oEmbed 401); identity for those = i.ytimg.com thumbnail liveness + yt-dlp uploads-playlist
enumeration (`identityMethod` field per video). Doodle Science's A-Level Physics playlist (excluded in P2B as
"GCSE-only") is a real source here — 20 physics rows.

Validation gates: spine-code resolution caught 3 pre-commit errors (17.2.x guesses -> 17.1.4/17.1.5; reduction
misfile -> 16.1.1(d)); cognito channel-only guard rejected 6 site-gated rows (removed); no (video,spec) dupes.

Still honest-empty after this lane: Period 3 chemistry, entropy/Gibbs/lattice/Born-Haber, electrode potentials,
NMR, rate equations, buffers, capacitors, photoelectric detail, Doppler, SUVAT, most A2 options (bio: gene
therapy/GM food/stats; full lists in `Videos/drafts/review-file-external-p2d.md`).

Review file: `Videos/drafts/review-file-external-p2d.md`. Branch: `videos/p2d-cie-alevel` (off videos/p2c-all-subjects).
"""
open(f"{RES}/Videos/trackers/P2-ALIGNMENT-TRACKER.md", "a").write(p2d)
print("tracker appended")

# README status row
rd = open(f"{RES}/Videos/README.md").read()
anchor = "| P2C — all-subjects"
if anchor not in rd:
    # find the status table's last P2 row generically
    import re
    m = list(re.finditer(r"^\| P2C .*$',", rd, re.M)) or list(re.finditer(r"^\| P2C .*\|\s*$", rd, re.M))
    if m:
        last = m[-1]
        rd = rd[:last.end()] + f"\n| P2D — CIE A-level trio | 🟡 draft pushed, review open | `videos/p2d-cie-alevel` (303 rows M/L only, reviewed:false) |" + rd[last.end():]
        open(f"{RES}/Videos/README.md", "w").write(rd)
        print("README updated")
    else:
        print("README anchor NOT found — inspect manually")
else:
    print("README already has P2D row")
