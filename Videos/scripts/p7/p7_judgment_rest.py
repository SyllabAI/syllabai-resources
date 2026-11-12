#!/usr/bin/env python3
"""P7 step 4 (cont.): judgment pass (agent) — ial-biology-18 + chemistry + physics."""
import json, sys

OUT = '/home/z/my-project/work/p7'

J = {}

# ============================== ial-biology-18 (99 rows) ==============================
J['ial-biology-18'] = {
 0:('drop','digestive system (amoeba): the 2.16 gene-mutation bind is nonsense adjacency; the honest IAL digestive specs were not bound'),
 1:('rebind',['2.1'],'medium',"title 'Gas Exchange in Bony Fish' names the gas-exchange-surfaces properties spec 2.1 (surface area/thin/diffusion gradient — fish gills context); the 2.16 second bind is garbage"),
 2:('rebind',['4.5'],'low',"title 'The Location and Structure of the Vascular Bundle' names the xylem/phloem structure spec 4.5 partially (verified: similarities/differences of vascular tissues); the 7.12 myogenic bind is nonsense"),
 3:('rebind',['4.5'],'low',"title 'Translocation in the Phloem' names phloem content of spec 4.5 as a genuine partial (the translocation mechanism spec itself did not bind)"),
 4:('drop','enzyme examples/cofactors/inhibitors survey (amoeba): the honest IAL enzyme specs (1.14/1.15) were not bound; 7.2 glycolysis and 1.20 treatment binds are keyword-adjacent'),
 5:('drop','Pacinian corpuscle: the honest IAL receptor spec was not bound; the 6.4 CP13 bind is a misbind magnet (dropped wherever it is not the named practical)'),
 6:('keep',),
 7:('drop','non-Mendelian genetics (amoeba): no honest IAL bind; 6.4 CP13 is keyword-adjacent'),
 8:('drop','biological roles of water: no IAL spec bound honestly; 5.4/5.2 photosynthesis binds are keyword-adjacent'),
 9:('keep',),
 10:('rebind',['3.20'],'low',"title 'Epigenetics' partially names the phenotype-determination spec 3.20 (environment-driven phenotype change — epigenetics adjacent, disclosed); the 6.4 CP13 bind is keyword-adjacent"),
 11:('rebind',['1.9'],'low',"title 'Fetal Haemoglobin (OCR/Edexcel)' partially names the haemoglobin-role spec 1.9 (fetal vs adult Hb binding curves — board-tagged, disclosed); the 2.6 amino-acid bind is nonsense"),
 12:('rebind',['7.19'],'low',"title 'Role of the Liver in Detoxification' partially names the liver urea-production spec 7.19 (deamination/detox context); the 6.4 CP13 bind is keyword-adjacent"),
 13:('drop','plants diversity/structure survey (amoeba): binds (4.19 niche, 4.21 zoos) are survey slices — P6 survey-reject class'),
 14:('drop','protein synthesis 1: the honest IAL protein-synthesis spec was not bound; 5.4/3.18 binds are keyword-adjacent'),
 15:('keep',),
 16:('drop','temporal/spatial summation: the honest IAL synapse spec was not bound; 6.4 CP13 is keyword-adjacent'),
 17:('rebind',['5.16'],'low',"title 'Evidence for Evolution' names the evidence-for-evolution spec 5.16 directly (verified fragment); the 5.23 allele-frequency bind is the mechanism spec, trimmed"),
 18:('drop','tissue fluid/lymph: the honest IAL spec (tissue-fluid formation) was not bound; 2.2 membrane and 7.13 cardiac-output binds are keyword-adjacent'),
 19:('drop','type 1/2 diabetes: the honest IAL blood-glucose spec was not bound; 6.4 CP13 and 5.16 evolution-evidence binds are keyword-adjacent'),
 20:('rebind',['7.14'],'medium',"title 'The Fight or Flight Response' names the adrenaline spec 7.14 directly; the 6.4 CP13 bind is keyword-adjacent"),
 21:('drop','factors affecting genetic biodiversity: the honest IAL spec was not bound; 5.25 scientific-conclusions bind is keyword-adjacent'),
 22:('keep',),
 23:('rebind',['6.5'],'low',"title 'Viruses' partially names the bacteria/virus comparison spec 6.5; the 8.12 CP18 bind is keyword-adjacent"),
 24:('drop','cell cycle (Before the Bell): the honest IAL mitosis/cell-cycle spec was not bound; 5.14 ecology-CP bind is keyword-adjacent'),
 25:('drop','monogenic inheritance: the honest IAL genetic-diagram spec was not bound; 6.4 CP13 and 3.21 binds are keyword-adjacent'),
 26:('keep',),
 27:('keep',),
 28:('rebind',['7.11'],'medium',"title 'Myofibrils, Actin and Myosin' names the muscle-contraction spec 7.11 directly; the 6.4 CP13 bind is keyword-adjacent"),
 29:('rebind',['7.14'],'low',"title 'Adrenaline and Cell Signalling' names the adrenaline spec 7.14; the 6.4 CP13 bind is keyword-adjacent"),
 30:('keep',),
 31:('drop','diagnostic testing of urine: the honest IAL urine-diagnosis spec was not bound; 6.4 CP13 and 4.13 drug-testing binds are keyword-adjacent'),
 32:('keep',),
 33:('keep',),
 34:('keep',),
 35:('rebind',['8.4'],'low',"title 'The Action Potential and the All-or-Nothing...' names the nerve-impulse/action-potential spec 8.4 directly; the 8.8 stimulus-detection bind is adjacent, trimmed"),
 36:('rebind',['7.4'],'low',"title 'Mitochondria' partially names the oxidative-phosphorylation spec 7.4 (mitochondrial function); the 7.3 link-reaction bind is a slice, trimmed"),
 37:('rebind',['2.14'],'low',"title 'Substitution Mutations' partially names the DNA-replication-errors spec 2.14 (base-substitution mutations); the 6.4 CP13 bind is keyword-adjacent"),
 38:('keep',),
 39:('rebind',['8.8'],'low',"title 'Rod Cells and Cone Cells as Light Receptors' partially names the stimulus-detection spec 8.8 (photoreceptors — genuine partial, disclosed); the 6.4 CP13 bind is keyword-adjacent"),
 40:('rebind',['8.3'],'low',"title 'Reflex Actions' names the spinal-reflex spec 8.3 directly; the 6.4 CP13 bind is keyword-adjacent"),
 41:('drop','dihybrid inheritance: the honest IAL dihybrid spec was not bound; 6.4 CP13 and 3.21 (multiple alleles) binds are keyword-adjacent'),
 42:('rebind',['8.14'],'medium',"title 'The Human Brain' names the brain location/functions spec 8.14 directly; the 6.4 CP13 bind is keyword-adjacent"),
 43:('drop','synaptic transmission: the honest IAL synapse spec (8.6) was not bound; the 8.7 drugs bind is adjacent, dropped'),
 44:('rebind',['2.5'],'low',"title 'Diffusion' names the passive-transport spec 2.5 directly; the 2.1 gas-exchange bind is adjacent, trimmed"),
 45:('rebind',['6.1'],'low',"title 'Sampling Techniques used in Biology' partially names the sampling-principles spec 6.1; the 2.17 genetic-screening bind is nonsense"),
 46:('drop','chromatin/histones: no honest IAL bind; 6.4 CP13 and 3.20 binds are keyword-adjacent'),
 47:('keep',),
 48:('keep',),
 49:('drop','bonding in proteins: the honest IAL protein-structure spec was not bound; 2.9 mononucleotide bind is keyword-adjacent'),
 50:('rebind',['2.1'],'medium',"title 'Gas Exchange in Mammals' names the gas-exchange-surfaces properties spec 2.1 (alveoli context); the 2.16 bind is garbage"),
 51:('drop','organisation of the nervous system: the honest IAL spec was not bound; 6.4 CP13 is keyword-adjacent'),
 52:('rebind',['7.19'],'low',"title 'Structure of the Liver' partially names the liver spec 7.19 (urea production in the liver — partial, disclosed); the 6.4 CP13 bind is keyword-adjacent"),
 53:('keep',),
 54:('keep',),
 55:('keep',),
 56:('drop','why plants need specialised transport: the honest IAL spec was not bound; 3.18/5.26 binds are keyword-adjacent'),
 57:('keep',),
 58:('rebind',['7.22'],'low',"title 'Transcription' partially names the gene-switching spec 7.22 (transcription factors — genuine partial, disclosed); the 8.11 phytochrome bind is nonsense"),
 59:('rebind',['7.14'],'low',"title 'The Adrenal Glands' partially names the adrenaline spec 7.14 (the gland secreting it — partial, disclosed); the 6.4/8.14 binds are keyword-adjacent"),
 60:('drop','11 body-systems survey (amoeba): survey reject class; the 5.14 ecology-CP bind is keyword-adjacent'),
 61:('rebind',['3.10'],'low',"title 'Chromosome Numbers During Division: Demystified' partially names the meiosis spec 3.10 (chromosome-number halving); the 3.20 phenotype bind is keyword-adjacent"),
 62:('rebind',['7.19'],'medium',"title 'Deamination and the Ornithine Cycle' names the liver urea-production spec 7.19 directly; the 6.4 CP13 bind is keyword-adjacent"),
 63:('rebind',['7.19'],'low',"title 'Excretion and Waste Products' partially names the urea/excretion spec 7.19; the 7.1 respiration bind is nonsense"),
 64:('rebind',['3.21'],'medium',"title 'Multiple Alleles' names the multiple-alleles phenotype spec 3.21 directly; the 6.4 CP13 bind is keyword-adjacent"),
 65:('keep',),
 66:('rebind',['3.17'],'low',"title 'Stem Cells and Diabetes' names the stem-cell spec 3.17; the 4.6 microscope-CP bind is keyword-adjacent"),
 67:('rebind',['7.4'],'low',"title 'Mitochondria' partially names the oxidative-phosphorylation spec 7.4; the 7.3 bind is a slice, trimmed"),
 68:('keep',),
 69:('drop','tumour suppressor genes: the honest IAL cancer spec was not bound; 3.20/7.12 binds are keyword-adjacent garbage'),
 70:('keep',),
 71:('drop','proto-oncogenes/oncogenes: no honest IAL bind; 6.4 CP13 is keyword-adjacent'),
 72:('drop','skeletal system (amoeba): the binds (7.11/7.10 muscle) are adjacent to skeleton — wrong content, dropped'),
 73:('keep',),
 74:('drop','chromosomes and karyotypes: karyotype content has no IAL spec; the 3.9 locus bind is keyword-adjacent'),
 75:('keep',),
 76:('drop','temperature on enzyme reactions: the honest IAL enzyme spec (1.15) was not bound; 7.1/7.13 binds are keyword-adjacent'),
 77:('keep',),
 78:('drop','11 body-systems survey (older video repeat of 60): survey reject class'),
 79:('drop','genetics vocabulary (Before the Bell): the honest IAL gene/allele spec (2.15) was not bound; 6.4 CP13 is keyword-adjacent'),
 80:('rebind',['7.18'],'low',"title 'Kidney Failure' partially names the kidney structure spec 7.18 (failure/dialysis context — partial, disclosed); the 6.4 CP13 bind is keyword-adjacent"),
 81:('keep',),
 82:('drop','protein synthesis 2: the honest IAL spec was not bound; 5.4/3.18 binds are keyword-adjacent'),
 83:('keep',),
 84:('keep',),
 85:('keep',),
 86:('keep',),
 87:('keep',),
 88:('drop','factors affecting biodiversity: the honest IAL spec was not bound; 5.25 bind is keyword-adjacent'),
 89:('keep',),
 90:('keep',),
 91:('keep',),
 92:('rebind',['7.12'],'low',"title 'Control of the Heart Rate' partially names the cardiac-muscle spec 7.12 (myogenic nature + rate control — partial, disclosed); the 6.4 CP13 bind is keyword-adjacent"),
 93:('rebind',['7.15'],'low',"title 'Respiratory System' partially names the spirometer/ventilation practical spec 7.15 (breathing volumes — partial, disclosed); the 7.6 RQ bind is a different term — trimmed"),
 94:('drop','pancreas endocrine/exocrine: the honest IAL blood-glucose spec was not bound; 6.4/3.2 binds are keyword-adjacent'),
 95:('keep',),
 96:('rebind',['2.4'],'medium',"title 'Osmosis and Water Potential' names the osmosis spec 2.4 directly; the 8.8 bind is nonsense adjacency"),
 97:('keep',),
 98:('drop','protein synthesis (Before the Bell): the honest IAL spec was not bound; 5.4/3.18 binds are keyword-adjacent'),
}

# ============================== cie-a-level-chemistry-25 (24 rows) ==============================
J['cie-a-level-chemistry-25'] = {
 0:('drop','FSL practise-questions drill (generic enthalpy calculation practice): the 2.4.1 mole bind is keyword-adjacent — P6 generic-drill reject class'),
 1:('keep',),
 2:('keep',),
 3:('keep',),
 4:('drop','optical isomerism in hydroxynitriles: the honest CIE chirality spec was not bound; the 37.3.2 NMR bind is keyword-adjacent'),
 5:('keep',),
 6:('rebind',['3.4.2'],'low',"title 'Covalent Bonding and Expansion of the Octet' names the expanded-octet spec 3.4.2 (SO2, PCl5 named in-spec — verified); the 3.7.1 ionic-diagram bind is wrong — trimmed"),
 7:('drop','FSL practise-questions drill: keyword-adjacent mole bind — generic-drill reject class'),
 8:('rebind',['7.2.10'],'low',"title 'How to Carry Out a Titration' partially names the indicator-selection spec 7.2.10; the 7.2.9 curves bind is adjacent, trimmed"),
 9:('drop','working with solutions (mole drills): the 22.2.1 mass-spectra bind is nonsense adjacency'),
 10:('rebind',['2.3.4'],'medium',"title 'Determining Water of Crystallisation by Titration' names the hydrated/anhydrous spec 2.3.4 directly; the 7.2.9 curves bind is adjacent, trimmed"),
 11:('rebind',['32.2.5'],'medium',"title 'Bromination of Benzene' names the benzene-bromination conditions spec 32.2.5 directly; the 37.3.2 NMR bind is nonsense adjacency"),
 12:('drop','FSL practise-questions drill: keyword-adjacent — generic-drill reject class'),
 13:('rebind',['2.3.4'],'medium',"title 'Determining Water of Crystallisation by Titration' (part 2) names spec 2.3.4 directly; the 7.2.9 bind is adjacent, trimmed"),
 14:('keep',),
 15:('drop','FSL practise-questions drill: keyword-adjacent — generic-drill reject class'),
 16:('keep',),
 17:('drop','oxidation of aldehydes: the honest CIE spec was not bound; the 37.3.x NMR binds are keyword-adjacent'),
 18:('drop','working with solutions (mole drills): mass-spectra bind is nonsense adjacency'),
 19:('rebind',['2.4.1'],'low',"title 'Calculating Percentage Yield' partially names the mole-calculation spec 2.4.1; the 37.2.2 chromatogram bind is nonsense adjacency"),
 20:('keep',),
 21:('keep',),
 22:('drop','volatility/solubility of alcohols: the honest CIE alcohols spec was not bound; the 11.1.x halogen-volatility binds matched the token volatility — keyword-adjacent'),
 23:('drop','the structure of benzene: the honest CIE delocalised-pi spec was not bound; the 37.3.x NMR binds are keyword-adjacent'),
}

# ============================== igcse-chemistry-19 (12 rows) ==============================
J['igcse-chemistry-19'] = {
 0:('keep',),
 1:('keep',),
 2:('keep',),
 3:('rebind',['4CH1-1.27'],'low',"title 'Using Moles to Balance Equations' partially names the mole spec 4CH1-1.27; the 4CH1-4.18 cracking bind is nonsense adjacency"),
 4:('rebind',['4CH1-1.29'],'medium',"title 'Reacting Masses 2' names the reacting-masses spec 4CH1-1.29 directly; the 4CH1-4.32C ethanol bind is nonsense adjacency"),
 5:('rebind',['4CH1-1.27'],'low',"title 'Calculating Moles of a Compound' partially names the mole spec 4CH1-1.27; the 4CH1-3.22C equilibrium bind is nonsense adjacency"),
 6:('keep',),
 7:('keep',),
 8:('rebind',['4CH1-2.23C'],'low',"title 'Alternative Methods of Extracting Metals' names the extraction-methods spec 4CH1-2.23C directly; the 4CH1-3.13 catalyst bind is nonsense adjacency"),
 9:('keep',),
 10:('keep',),
 11:('drop','making salts practical: the honest 4CH1 salt-preparation spec was not bound; the 4CH1-3.6C bond-breaking bind is keyword-adjacent'),
}

# ============================== cie-igcse-chemistry-23 (22 rows) ==============================
J['cie-igcse-chemistry-23'] = {
 0:('keep',),
 1:('rebind',['12.4.3'],'low',"title 'Purity and Formulations' names the purity-assessment spec 12.4.3; the 3.3.8 yield bind is keyword-adjacent"),
 2:('drop','using tangents to determine rate: generic graph/maths skill — P6 wholesale reject class; both binds are keyword-adjacent'),
 3:('keep',),
 4:('keep',),
 5:('keep',),
 6:('keep',),
 7:('drop','bond energy calculations: the honest 0620 bond-energy spec was not bound; 3.3.4/3.2.3 binds are keyword-adjacent'),
 8:('drop','Dalton atomic model: the honest 0620 atomic-structure spec was not bound; the formula-deduction binds are keyword-adjacent'),
 9:('drop','Doodle physics-channel video (life cycle of stars): cross-subject misroute — the binds matched generic substance tokens; no honest 0620 chemistry bind'),
 10:('keep',),
 11:('keep',),
 12:('drop','nuclear model of atomic structure: honest target unbound; the formula-deduction binds are keyword-adjacent'),
 13:('keep',),
 14:('drop','acids reacting with metals 2: the reacting-mass binds are keyword-adjacent; the reaction content itself is not named by the bound specs'),
 15:('keep',),
 16:('rebind',['10.1.7'],'low',"title 'Waste Water Treatment' names the domestic-water-treatment spec 10.1.7 directly; the 10.3.2 noble-gases bind is nonsense adjacency"),
 17:('keep',),
 18:('keep',),
 19:('keep',),
 20:('drop','titration calculations 1: the honest 0620 concentration-calc spec was not bound; 3.3.4 gas-volume/3.2.3 reacting-mass binds are keyword-adjacent'),
 21:('drop','titration calculations 2: as above — honest target unbound, binds keyword-adjacent'),
}

# ============================== igcse-physics-19 (21 rows) ==============================
J['igcse-physics-19'] = {
 0:('keep',),
 1:('rebind',['2.2'],'low',"title 'Electrical Appliances' partially names the home-safety spec 2.2 (insulation/double insulation of appliances); the 6.18P transformer bind is nonsense adjacency"),
 2:('keep',),
 3:('keep',),
 4:('keep',),
 5:('keep',),
 6:('keep',),
 7:('keep',),
 8:('keep',),
 9:('keep',),
 10:('keep',),
 11:('keep',),
 12:('rebind',['4.5'],'low',"title 'Electromagnetic Devices' partially names the everyday-magnetic-applications spec 4.5 (electromagnets); the 2.2 bind is nonsense adjacency"),
 13:('drop',"Newton's FIRST law: the honest 4PH1 inertia spec was not bound; the 1.29P Newton's-THIRD-law bind is a misbind and 1.23 is Hooke's law — nonsense adjacency"),
 14:('rebind',['1.23'],'medium',"title \"Hooke's Law\" names the Hooke's-law spec 1.23 directly; the 3.15 reflection bind is nonsense adjacency"),
 15:('keep',),
 16:('keep',),
 17:('drop','energy transfer by appliances (E=Pt content): the honest 4PH1 power/energy spec was not bound; the 2.2 insulation bind is keyword-adjacent'),
 18:('keep',),
 19:('keep',),
 20:('keep',),
}

# ============================== cie-igcse-physics-23 (23 rows) ==============================
J['cie-igcse-physics-23'] = {
 0:('keep',),
 1:('drop','hazards of radiation (Doodle): the 4.4.1 bind matched the token hazards on an ELECTRICAL-hazards spec — keyword-adjacent; the honest radiation-hazard spec was not bound'),
 2:('keep',),
 3:('rebind',['3.2.1b'],'low',"title 'Converging Lenses' names the thin-converging/diverging-lens-action spec 3.2.1b; the 3.2.9 optical-fibre bind is nonsense adjacency"),
 4:('keep',),
 5:('keep',),
 6:('drop','correcting vision: the eye-vision-lens content has no clear 0625-23 spine spec; the 3.3.3 EM-region bind is keyword-adjacent'),
 7:('keep',),
 8:('rebind',['2.2.5'],'low',"title 'Cooling of Buildings' partially names the evaporation-causes-cooling spec 2.2.5 (cooling context — partial, disclosed); the 5.2.2 greenhouse bind is nonsense adjacency"),
 9:('rebind',['3.2.1b'],'low',"title 'Convex Lenses' names the thin-lens-action spec 3.2.1b; the 3.2.9/3.2.5 binds are adjacent, trimmed"),
 10:('keep',),
 11:('rebind',['1.5.11'],'medium',"title \"Newton's Second Law of Motion (F=ma)\" names the F=ma spec 1.5.11 directly; the 6.2.10 Hubble bind is nonsense adjacency"),
 12:('rebind',['2.3.3'],'low',"title 'Black Body Radiation' partially names the surface-colour emission/absorption spec 2.3.3 (black surfaces — genuine partial, disclosed); the 3.3.4 EM-harm bind is nonsense adjacency"),
 13:('keep',),
 14:('keep',),
 15:('keep',),
 16:('keep',),
 17:('drop','the UK energy mix: the honest 0625 energy-resources spec was not bound; the 1.4.4 density/float bind is nonsense adjacency'),
 18:('keep',),
 19:('keep',),
 20:('drop','heating and cooling graphs: the honest 0625 state-change-graph spec was not bound; the 2.2.5 evaporation bind names a different phenomenon'),
 21:('rebind',['3.2.1b'],'low',"title 'Concave Lenses' names the thin-diverging-lens half of spec 3.2.1b; the 3.2.9/3.2.5 binds are adjacent, trimmed"),
 22:('keep',),
}

# ============================== cie-a-level-physics-25 (2 rows) ==============================
J['cie-a-level-physics-25'] = {
 0:('keep',),
 1:('keep',),
}

# ============================== ial-physics-19 (1 row) ==============================
J['ial-physics-19'] = {
 0:('rebind',['107'],'medium',"title 'Motor Effect F=BIL - Physics A-level Practical' names the F=BIl(sin theta) force-on-conductor spec 107 directly; the 62 photoelectric bind is nonsense adjacency"),
}

def main():
    for course in sys.argv[1:]:
        if course not in J:
            print(f'no judgment table for {course}'); continue
        adv = json.load(open(f'{OUT}/adjudication-{course}.json'))
        n = len(adv['rows'])
        assert set(J[course].keys()) == set(range(n)), f'{course}: table coverage mismatch ({n} rows)'
        json.dump({'course': course, 'decisions': {str(k): list(v) for k, v in J[course].items()}},
                  open(f'{OUT}/judgment-{course}.json', 'w'), indent=1)
        kept = sum(1 for v in J[course].values() if v[0] in ('keep', 'rebind'))
        print(f'{course}: {kept} kept/re-bound, {n - kept} dropped (of {n} pre-pass rows)')

if __name__ == '__main__':
    main()
