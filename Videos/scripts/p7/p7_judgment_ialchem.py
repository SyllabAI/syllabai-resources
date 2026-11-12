#!/usr/bin/env python3
"""P7 judgment addendum: ial-chemistry-17 (33 rows)."""
import json

OUT = '/home/z/my-project/work/p7'

J = {
 0:('rebind',['1.2'],'low',"title 'Calculations Involving the Avogadro Constant' partially names the mole spec 1.2 (mole-unit calculations — partial, disclosed); the 16.15 maths-skills bind is adjacent, trimmed"),
 1:('drop','Infra-Red Spectroscopy (malmesbury): the honest IAL IR-spectroscopy spec was not bound; the 10.17 alcohol-reactions and 15.20 NMR binds are keyword-adjacent'),
 2:('rebind',['10.9'],'medium',"title 'Hydrolysis of Haloalkanes by Nucleophilic Substitution' names the nucleophilic-substitution mechanism spec 10.9 directly; the 15.8 carbonyl bind is nonsense adjacency"),
 3:('rebind',['1.9'],'medium',"title 'Calculating Atom Economy' names the percentage-yield/atom-economy spec 1.9 (verified fragment); the 9.7 catalyst bind is keyword-adjacent"),
 4:('keep',),
 5:('keep',),
 6:('drop','working with gases (mole/gas-volume drills): the honest IAL molar-gas-volume spec was not bound; the 4.3 risk-assessment bind is keyword-adjacent'),
 7:('rebind',['4.18'],'low',"title 'Chlorofluorocarbons and the Ozone Layer' partially names the free-radical-substitution spec 4.18 (CFC ozone-depletion mechanism context — partial, disclosed); the 15.22 Rf-value bind is nonsense"),
 8:('keep',),
 9:('rebind',['5.6'],'medium',"title 'Electrophilic Addition of a Halogen to Alkenes' names the alkene electrophilic-addition mechanism spec 5.6 directly; the 18.5 arene-substitution bind is wrong topic — trimmed"),
 10:('rebind',['10.9'],'low',"title 'The Rate of Hydrolysis of Haloalkanes by Nucleophilic Substitution' partially names the haloalkane-hydrolysis spec 10.9 (rate context — partial, disclosed); the 15.8 carbonyl bind is nonsense"),
 11:('keep',),
 12:('keep',),
 13:('drop','naming unbranched hydrocarbons: the honest IAL nomenclature spec was not bound; the 5.3 E-Z and 5.1 alkene binds are keyword-adjacent'),
 14:('rebind',['8.19'],'low',"title 'Testing for Ammonium Ions' partially names the test-reactions/ionic-equations spec 8.19 (cation tests — partial, disclosed); the 15.23 HPLC bind is nonsense"),
 15:('rebind',['4.12'],'low',"title 'Thermal Cracking and Catalytic Cracking of Alkanes' partially names the alkanes-sources spec 4.12 (alkanes obtained from crude oil by cracking — partial, disclosed); the 4.18 substitution-mechanism bind is the wrong mechanism class — trimmed"),
 16:('keep',),
 17:('keep',),
 18:('rebind',['5.3'],'medium',"title 'Cis-Trans Isomers' names the E-Z/geometric-isomerism spec 5.3 directly (cis-trans = E-Z); the 17.15 square-planar bind is nonsense adjacency"),
 19:('keep',),
 20:('drop','enthalpy cycles involving standard enthalpies: the honest IAL Hess-cycle spec was not bound; the 20.3/16.15 binds are keyword-adjacent'),
 21:('rebind',['8.19'],'low',"title 'Testing for Sulfate Ions' partially names the test-reactions spec 8.19 (anion tests incl. sulfate — partial, disclosed); the 8.15 solubility bind is nonsense"),
 22:('keep',),
 23:('rebind',['5.8'],'low',"title 'Addition Polymers' partially names the polymer-disposal spec 5.8 (addition-polymer environmental context — partial, disclosed); the 19.10 physical-properties bind is adjacent, trimmed"),
 24:('drop','acids, bases and neutralisation (intro): the honest IAL acid-base spec was not bound; the 6.4 standard-enthalpy bind is keyword-adjacent'),
 25:('keep',),
 26:('keep',),
 27:('keep',),
 28:('drop','effect of lone pairs on molecular shape: the honest IAL electron-pair-repulsion spec was not bound; the 5.6/15.8 binds are keyword-adjacent'),
 29:('keep',),
 30:('keep',),
 31:('rebind',['3.15'],'low',"title 'Polar Bonds and Polar Molecules' names the polar-bonds spec 3.15 directly; the 7.6 solvent-choice bind is nonsense adjacency"),
 32:('keep',),
}

adv = json.load(open(f'{OUT}/adjudication-ial-chemistry-17.json'))
n = len(adv['rows'])
assert set(J.keys()) == set(range(n)), f'coverage mismatch ({n} rows)'
json.dump({'course': 'ial-chemistry-17', 'decisions': {str(k): list(v) for k, v in J.items()}},
          open(f'{OUT}/judgment-ial-chemistry-17.json', 'w'), indent=1)
kept = sum(1 for v in J.values() if v[0] in ('keep', 'rebind'))
print(f'ial-chemistry-17: {kept} kept/re-bound, {n - kept} dropped (of {n} pre-pass rows)')
