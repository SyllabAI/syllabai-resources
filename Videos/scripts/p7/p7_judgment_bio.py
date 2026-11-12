#!/usr/bin/env python3
"""P7 step 4: judgment pass (agent) — biology courses.
Every adjudication row must appear exactly once: 'keep' (the deterministic bind
stands), 'drop' (with reason), or 'rebind' (specs, confidence, evidence).
Title assertions applied by the runner. Output: judgment-{course}.json."""
import json, os, sys

OUT = '/home/z/my-project/work/p7'

J = {}

# ============================== cie-igcse-biology-23 (49 rows) ==============================
J['cie-igcse-biology-23'] = {
 0:('drop','Doodle physics-channel video (nuclear radiation): the 18.1.8 mutation-cause half is keyword-adjacent and 17.2.1 mitosis is nonsense adjacency — P6 cross-subject misbind class'),
 1:('keep',),
 2:('rebind',['17.1.8'],'low',"title 'Protein Synthesis' names the protein-synthesis spec 17.1.8 directly; the 12.1.1/6.1.4 binds matched 'synthesi' inside photosynthesis docs — nonsense adjacency"),
 3:('drop','why-study-biology motivational promo; no spec content named'),
 4:('drop','non-specific defence: the binds matched the token non (8.1.2 gas-exchange position / 20.3.2 pollution) — keyword-adjacent garbage; the AQA defence-systems content has no 0610-named spec'),
 5:('drop','metabolism: no 0610 spec names metabolism; the 1.1.1 characteristics bind is keyword-adjacent (MRS GREN respiration != metabolism)'),
 6:('rebind',['4.1.3'],'low',"title 'Required Practical 4: Food Tests' names the food-test chemicals spec 4.1.3 (iodine/Benedict/biuret) directly; the 17.4.13 second bind is a germination experiment — wrong practical"),
 7:('keep',),
 8:('keep',),
 9:('drop','levels-of-organization tour binds trophic-level specs on the token level — keyword-adjacent (biological organisation != trophic levels)'),
 10:('drop','reaction-time practical: no 0610 spec names reaction-time measurement; the 8.4.3 plant-storage bind matched the token time — nonsense adjacency'),
 11:('keep',),
 12:('keep',),
 13:('rebind',['20.4.7'],'low',"title 'Biodiversity' names the conservation-programmes spec 20.4.7; the 20.2.4 deforestation half is adjacent, trimmed"),
 14:('drop','stem cells: no stem-cell spec in 0610; the 8.2.3 bind matched stem inside xylem-stem docs — nonsense adjacency'),
 15:('drop','Eye vs Camera is a Doodle physics-channel video on eye optics (lens/focusing) — the honest target would be the physics lens specs, not the 0610 eye-structure specs; wrong-course route, dropped'),
 16:('drop','fossil evidence for evolution: no 0610 fossil spec; the 19.3.1 bind matched fossil inside carbon-cycle (fossil fuel) docs — keyword-adjacent'),
 17:('keep',),
 18:('keep',),
 19:('keep',),
 20:('rebind',['17.2.4','17.3.2'],'low',"title 'Cell Division - Mitosis and Meiosis' names the mitosis chromosome-separation spec 17.2.4 and the meiosis reduction-division spec 17.3.2; the 12.3.6 bind was a plant-reproduction doc — wrong topic"),
 21:('keep',),
 22:('drop','AQA land-use content (building/quarrying/peat) has no direct 0610 spec; the 20.1.1 food-production bind is keyword-adjacent'),
 23:('keep',),
 24:('rebind',['14.4.3'],'medium',"title 'Negative Feedback' names the homeostatic-control spec 14.4.3 directly; the 20.2.3 second bind matched the token negative — nonsense adjacency"),
 25:('keep',),
 26:('rebind',['4.1.3'],'low',"title 'Food Tests - GCSE Science Required Practical' names the food-test chemicals spec 4.1.3 (iodine/Benedict/biuret) directly; the 17.4.13 second bind is a germination experiment — wrong practical"),
 27:('drop','malmesbury conduction-system-of-the-heart: not 0610 content (cardiac conduction is AQA A-level); the 2.1.6 bind matched the token conduction — keyword-adjacent'),
 28:('keep',),
 29:('keep',),
 30:('drop','competition and interdependence: the honest 0610 target (community interactions) is not named by any bound spec; 19.4.4 is population-growth-rate factors and 20.1.1 is crop production — both keyword-adjacent'),
 31:('drop','gene expression/regulation is A-level content with no 0610 spec; both binds (21.3.3 GM, 16.5.1 testosterone) matched the token expression loosely — nonsense'),
 32:('keep',),
 33:('keep',),
 34:('drop','AQA environmental-change (communities) has no direct 0610 spec; the 6.1.11 limiting-factors bind matched the token environmental — keyword-adjacent'),
 35:('drop','mean/median/mode is generic maths-skills — P6 wholesale reject class; the 14.1.6 reflex bind matched the token mean — nonsense adjacency'),
 36:('keep',),
 37:('keep',),
 38:('rebind',['17.1.8'],'low',"title 'Protein Synthesis and the Lean, Mean Ribosome Machines' names the protein-synthesis spec 17.1.8; the 12.1.1 energy bind is keyword-adjacent"),
 39:('drop','Mega Genetics Review is a survey of many genetics specs; the binds (8.1.2, 20.3.2) matched the token non — nonsense adjacency; P6 survey-reject class'),
 40:('drop','bacteria good/bad survey: the binds (11.1.1 gas exchange via good, 10.1.5) are nonsense adjacency'),
 41:('rebind',['13.1.5'],'medium',"title 'Excretory System and the Nephron' names the nephron structure/function spec 13.1.5 directly (verified: 0610 spine names the nephron); the 16.4.9 placenta bind was keyword-adjacent"),
 42:('drop','cell-membrane content has no 0610-named spec; the 3.2.6 turgor bind matched the token inside — nonsense adjacency'),
 43:('drop','AQA RP2 culturing microorganisms (aseptic technique) has no 0610 spec; the binds matched the token microorganism loosely'),
 44:('rebind',['2.1.6'],'low',"title 'How Cells Become Specialized' names the specialised-cells spec 2.1.6 (ciliated cells, RBCs, etc.); the pre-pass binds (17.2.4, 8.2.3) were token garbage"),
 45:('rebind',['17.3.2','18.1.10'],'low',"title 'Meiosis: The Great Divide' names the meiosis spec 17.3.2 and the genetic-variation-sources spec 18.1.10 (meiosis named in-spec); the 17.2.4 mitosis bind is wrong — this video is meiosis"),
 46:('keep',),
 47:('rebind',['2.1.6'],'low',"title 'Specialized Cells: Significance and Examples' names the specialised-cells spec 2.1.6; the 7.5.3 villi bind matched the token significance — keyword-adjacent"),
 48:('drop','AQA plant-defence responses have no 0610 spec; the binds (10.1.6 active immunity, 10.1.4) matched the token defence — keyword-adjacent'),
}

# ============================== igcse-biology-19 (47 rows) ==============================
J['igcse-biology-19'] = {
 0:('keep',),
 1:('drop','AQA testing-medicines (clinical trials/placebos) is not the 4BI1 content; the 2.6B bind cannot be reconciled with the title content'),
 2:('rebind',['2.1'],'low',"title 'Plant Tissues' names the levels-of-organisation spec 2.1 partially (tissues/organs); the 5.17B micropropagation bind matched the token tissue (tissue culture != plant tissues) — keyword-adjacent"),
 3:('rebind',['3.38'],'medium',"title 'Darwin and Natural Selection' names Darwin's theory spec 3.38 directly; the 3.7 asexual-plant bind is nonsense adjacency"),
 4:('keep',),
 5:('drop','cellular respiration: the honest 4BI1 targets (2.42-2.44 respiration) were not bound; the pre-pass binds (1.4 pathogen, 2.3 organelle functions) are keyword-adjacent garbage'),
 6:('keep',),
 7:('drop','body-tissues (4 US types) binds no 4BI1 spec; 1.4 pathogen and 5.17B micropropagation matched the token tissue — keyword-adjacent'),
 8:('keep',),
 9:('rebind',['4.10'],'low',"title 'Decomposition' names the carbon-cycle spec 4.10 (decomposers named in-spec); the 4.9 bind (10% energy transfer) is a different spec — trimmed"),
 10:('rebind',['3.38'],'medium',"title 'Evolution by Natural Selection' names spec 3.38 directly; the 3.7 bind is nonsense adjacency"),
 11:('rebind',['3.38'],'low',"title 'Natural Selection' names spec 3.38; the 3.7 bind is nonsense adjacency"),
 12:('keep',),
 13:('drop','amoeba playlist-stroll survey; the 2.28 peristalsis bind matched the token food loosely — survey reject class'),
 14:('drop','human-body-systems survey; the binds (3.32 diploid, 1.2 eukaryote) are nonsense adjacency'),
 15:('keep',),
 16:('keep',),
 17:('keep',),
 18:('drop','AQA adaptations (extremophiles) has no direct 4BI1 spec; the 2.61 red-blood-cell bind is a specific-cell slice, not the title content'),
 19:('rebind',['4.10'],'low',"title 'Required Practical 10: Decay' — the decay practical demonstrates decomposer action; bound on the carbon-cycle spec 4.10 as a genuine partial (the AQA rate-of-decay procedure itself has no 4BI1 spec)"),
 20:('drop','communicable/non-communicable disease: the 2.17 bind is the diffusion/osmosis practical — nonsense adjacency'),
 21:('keep',),
 22:('keep',),
 23:('keep',),
 24:('drop','plant hormones (auxin): the honest 4BI1 auxin targets were not bound; the 2.95B/2.94 binds are the human FSH/LH specs — nonsense adjacency'),
 25:('keep',),
 26:('keep',),
 27:('keep',),
 28:('keep',),
 29:('rebind',['2.29'],'low',"title 'The Digestive System' names the digestive-enzymes spec 2.29; the 1.2 eukaryote bind is keyword-adjacent"),
 30:('keep',),
 31:('keep',),
 32:('keep',),
 33:('keep',),
 34:('rebind',['2.29'],'low',"title 'Required Practical 5: Effect of pH on Amylase' — amylase is a digestive enzyme; bound on spec 2.29 as a genuine partial (the pH-procedure itself has no 4BI1 spec); the 5.8 fermenter bind is nonsense adjacency"),
 35:('keep',),
 36:('keep',),
 37:('keep',),
 38:('keep',),
 39:('drop','AQA bacterial-division (binary fission) has no 4BI1 spec; the binds (3.39 antibiotic resistance, 3.30 meiosis) are keyword-adjacent garbage'),
 40:('drop','sizes of cells (orders of magnitude): no 4BI1 spec; both binds are keyword-adjacent'),
 41:('keep',),
 42:('drop','cellular respiration misbind (1.4 pathogen is nonsense adjacency); the honest respiration specs were not bound by the pre-pass'),
 43:('keep',),
 44:('keep',),
 45:('keep',),
 46:('rebind',['2.29'],'low',"title 'Digestive Enzymes' names spec 2.29 directly; the 1.2 bind is keyword-adjacent"),
}

# ============================== cie-a-level-biology-25 (55 rows) ==============================
J['cie-a-level-biology-25'] = {
 0:('keep',),
 1:('keep',),
 2:('drop','homeobox genes/body plans: verified ABSENT from the CIE 9700 spine (AQA-specific content); both binds (1.2.1 organelles, 9.1.4 trachea) are keyword-adjacent garbage'),
 3:('keep',),
 4:('drop','channel birthday-celebration promo — sewage'),
 5:('drop','potometer content: verified NO potometer spec in the CIE 9700 spine; the 7.2.8 phloem-mass-flow bind matched the token mass (mass potometer) — nonsense adjacency'),
 6:('drop','characteristics-of-life survey; the binds (10.1.4, 18.2.2) are keyword-adjacent'),
 7:('keep',),
 8:('rebind',['7.2.2'],'low',"title 'Movement of Water Through the Roots of a Plant' names the water-transport-pathway spec 7.2.2 (apoplast/symplast, Casparian strip — verified in spine); the 12.2.12 rice bind and 7.1.2 distribution bind were adjacent, replaced"),
 9:('keep',),
 10:('keep',),
 11:('drop','cofactors/coenzymes: verified ABSENT from the CIE 9700 spine; the binds (12.2.4 link reaction, 2.3.6 haemoglobin) matched coenzyme-in-NAD docs — keyword-adjacent'),
 12:('rebind',['1.1.3'],'low',"title 'Microscope Drawings' partially names the magnification-calculation spec 1.1.3; the 7.2.5 plant-section-drawing bind is a different context — trimmed"),
 13:('drop','endosymbiotic theory: not CIE 9700 content; the 17.3.1 evolution-theory bind is keyword-adjacent'),
 14:('keep',),
 15:('drop','angiosperm reproduction is not a CIE 9700 topic; the binds (5.1.2 mitosis, 18.3.4 assisted reproduction) are keyword-adjacent garbage'),
 16:('rebind',['14.1.10'],'low',"title 'The Regulation of Blood Glucose Concentration' names the blood-glucose negative-feedback spec 14.1.10 directly (verified in spine); the 14.2.1 stomata bind matched the token regulation — nonsense adjacency"),
 17:('keep',),
 18:('keep',),
 19:('drop','general lab safety: no spec; the 2.3.1 bind is nonsense adjacency'),
 20:('drop','AQA oestrogen-breast-cancer content is absent from the CIE spine; the 19.2.2 genetic-screening bind matched the token breast loosely — keyword-adjacent'),
 21:('keep',),
 22:('keep',),
 23:('keep',),
 24:('keep',),
 25:('keep',),
 26:('keep',),
 27:('drop','end-product inhibition: no CIE spec names it; the 5.1.1a bind is a cell-cycle doc fragment — keyword-adjacent'),
 28:('drop','AQA benign/malignant tumours framing; the 5.1.1a cell-cycle bind cannot be reconciled with the title content (spine names telomeres/stem cells, not tumours)'),
 29:('keep',),
 30:('rebind',['2.2.7'],'low',"title 'Starch Part 2: Amylopectin' names the polysaccharide-structure spec 2.2.7 (starch/amylopectin); the 2.1.1 Benedict bind is wrong (starch is non-reducing — iodine, not Benedict's)"),
 31:('drop','AQA sources-of-medicines content has no CIE spec; the binds are keyword-adjacent'),
 32:('keep',),
 33:('keep',),
 34:('rebind',['15.1.12'],'medium',"title 'Muscle Tissues and Sliding Filament Model' names the sliding-filament spec 15.1.12 directly; the 4.1.1 fluid-mosaic bind is nonsense adjacency"),
 35:('keep',),
 36:('keep',),
 37:('drop','AQA kidney dialysis content is absent from the CIE spine (verified); the 14.1.4 kidney-structure bind is adjacent, the 4.2.2 practical bind is nonsense'),
 38:('rebind',['16.3.2'],'low',"title 'Gene Regulation and the Operon' names the lac-operon spec 16.3.2 (verified: spine names the lac operon); the 14.2.1 stomata bind is nonsense adjacency"),
 39:('drop','plant structure/diversity survey; the 18.2.6 Simpson-index bind is keyword-adjacent'),
 40:('rebind',['8.3.4'],'low',"title 'Initiation and Coordination of the Action of the Heart' names the heartbeat-initiation spec 8.3.4 (sinoatrial/AV nodes, Purkyne tissue — verified in spine); the 14.1.9 cell-signalling bind was adjacent, replaced"),
 41:('drop','insect gas exchange (tracheal system): verified ABSENT from the CIE 9700 spine; the 19.3.1 genetic-engineering bind matched the token insects loosely — keyword-adjacent'),
 42:('keep',),
 43:('keep',),
 44:('rebind',['6.1.4'],'low',"title 'DNA Replication' names the semi-conservative-replication spec 6.1.4 (verified in spine); the 15.1.1 endocrine bind is nonsense adjacency"),
 45:('keep',),
 46:('keep',),
 47:('rebind',['6.2.7'],'low',"title 'Frame Shift Mutations' — frame shifts result from the substitution/deletion/insertion named by the gene-mutation spec 6.2.7 (verified in spine; the word 'frameshift' itself is not in the spine, disclosed); the 18.2.4/8.2.6 binds are nonsense adjacency"),
 48:('keep',),
 49:('drop','German-language lesson (malmesbury non-science leak past the sewage regex): no biology content; the 7.1.3 bind is nonsense adjacency'),
 50:('keep',),
 51:('keep',),
 52:('drop','biotechnology (PCR/gel electrophoresis US framing): the honest CIE targets (19.x gene technology) were not bound; the 15.2.3 gibberellin bind is nonsense adjacency'),
 53:('keep',),
 54:('rebind',['5.1.2','16.1.4'],'low',"title 'Mitosis vs. Meiosis: Side by Side Comparison' names the mitosis spec 5.1.2 and the meiosis chromosome-behaviour spec 16.1.4 (both verified in spine); the 2.1.2 Benedict bind is nonsense adjacency"),
}

def main():
    only = sys.argv[1:] or list(J.keys())
    for course in only:
        if course not in J:
            print(f'no judgment table for {course}'); continue
        adv = json.load(open(f'{OUT}/adjudication-{course}.json'))
        n = len(adv['rows'])
        idx = set(J[course].keys())
        assert idx == set(range(n)), f'{course}: table covers {sorted(idx)[:3]}.. but {n} rows'
        out = {'course': course, 'decisions': {str(k): list(v) for k, v in J[course].items()}}
        json.dump(out, open(f'{OUT}/judgment-{course}.json', 'w'), indent=1)
        kept = sum(1 for v in J[course].values() if v[0] in ('keep', 'rebind'))
        print(f'{course}: {kept} kept/re-bound, {n - kept} dropped (of {n} pre-pass rows)')

if __name__ == '__main__':
    main()
