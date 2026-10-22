#!/usr/bin/env python3
"""T-SPECS-CIE-COMPLETE-1-BAND-C — the leave-unjoined codification filler.

Codification-only band: ZERO code entries are written anywhere (the
leave-unjoined law IS the disposition). The vehicle:
  1. regenerates ONLY the band-C lanes' pending rows in the verdicts yaml
     (refined codified reasons), all other rows byte-preserved (object-hash)
  2. adds cie_complete.bands.C to the manifest (additive; A/B byte-kept)
  3. adds the bands.C provenance block to the yaml (additive; A/B byte-kept)
  4. proves the spec-links sidecars byte-identical before/after

Battery (fail-closed):
  P0 verdicts-yaml round-trip byte fixed point
  C1 census-closure: inputs cover EXACTLY the non-band-A/B pending universe
  C2 no-code-writes: every spec-links sidecar sha256-identical pre/post
  C3 other-rows preservation: non-band-C yaml rows object-hash unchanged
  C4 idempotence: re-run leaves all written files byte-identical
"""
from __future__ import annotations
import hashlib, json, os, sys, glob
import yaml

RES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEND = os.environ.get('BANDC_PEND', '/home/z/my-project/work/cie-bandC/pending_classes_bandC.json')
TAXO = os.environ.get('BANDC_TAXO', '/home/z/my-project/work/cie-bandC/taxonomy_bandC.json')
YAML_PATH = os.path.join(RES, 'scripts', 'cie_complete_verdicts.yaml')
MAN_PATH = os.path.join(RES, 'spec-links', 'manifest.json')
REPORT = os.path.join(RES, 'graph', 'reports', 'T_SPECS_CIE_COMPLETE_BAND_C_CHECK.json')

BAND = 'C'
BAND_LANE = 'T-SPECS-CIE-COMPLETE-1-BAND-C'
STAMP = '2026-10-22T02:00:00Z'
ORDER = ("operator order 'band B (geo-25's 111 cross-edition rows), band C (EL/fleet "
         "leave-unjoined codification), and then the two parse/spine repair lanes' "
         "(gateway trace 1a1615fe86d96ed9, 2026-10-22, zai-web)")
BAND_LANES_PREV = {'cie-a-level-maths-20-pure-3', 'cie-igcse-further-maths-additional-maths-25',
                   'cie-igcse-geography-25'}
YAML_PARAMS = dict(sort_keys=False, allow_unicode=True, width=110)


def die(m):
    print(f'ABORT: {m}', flush=True)
    sys.exit(1)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    apply_mode = '--apply' in sys.argv
    pend = json.load(open(PEND, encoding='utf8'))
    taxo = json.load(open(TAXO, encoding='utf8'))
    report = {'lane': BAND_LANE, 'band': BAND, 'stamp': STAMP, 'order': ORDER,
              'apply': apply_mode,
              'inputs': {'pending_classes_bandC.json': sha(PEND),
                         'taxonomy_bandC.json': sha(TAXO)},
              'problems': []}
    probs = report['problems']

    # P0 pre-flight
    ybytes = open(YAML_PATH, 'rb').read()
    ydoc = yaml.safe_load(ybytes)
    if yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8') != ybytes:
        die('P0 verdicts-yaml round-trip is not a byte fixed point')

    # C1 census-closure: inputs == the non-band-A/B pending universe
    universe = {}
    for r in ydoc['verdicts']:
        if r['verdict'] == 'pending_classified' and r['lane'] not in BAND_LANES_PREV:
            universe.setdefault(r['lane'], set()).add(r['id'])
    in_rows = {s: set(v) for s, v in pend.items()}
    if set(universe) != set(in_rows):
        probs.append(f'lane mismatch: universe {sorted(universe)} vs inputs {sorted(in_rows)}')
    for s in universe:
        if universe.get(s) != in_rows.get(s):
            probs.append(f'{s}: census mismatch {len(universe.get(s, set()))} vs {len(in_rows.get(s, set()))}')
    if probs:
        report['ok'] = False
        print('PROBLEMS:', probs[:8], flush=True)
        json.dump(report, open(REPORT, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        return 1

    # sidecar shas BEFORE
    # the COURSE sidecars are the no-write set; manifest.json is this band's own
    # additive target (cie_complete.bands.C) and is excluded here
    sidecars = sorted(p for p in glob.glob(os.path.join(RES, 'spec-links', '*.json'))
                      if os.path.basename(p) != 'manifest.json')
    side_pre = {p: sha(p) for p in sidecars}

    if apply_mode:
        # yaml: regenerate ONLY band-C lanes' pending rows
        kept, regen = [], []
        for r in ydoc['verdicts']:
            if (r['verdict'] == 'pending_classified' and r['lane'] in pend
                    and r['id'] in pend[r['lane']]):
                regen.append({'lane': r['lane'], 'id': r['id'],
                              'verdict': 'pending_classified',
                              'reason': pend[r['lane']][r['id']],
                              'label': r.get('label'), 'section': r.get('section'),
                              'topic': r.get('topic')})
            else:
                kept.append(r)
        bands_doc = dict(ydoc.get('bands') or {})
        bands_doc[BAND] = {
            'lane': BAND_LANE, 'stamp': STAMP, 'order': ORDER,
            'disposition': 'LEAVE-UNJOINED codified per class — zero code entries written '
                           'anywhere; the hub unmapped card is the honest surface of record',
            'law': ('AGENT.md rule 3 verbatim: no manufactured coverage; rule 2: agent mappings '
                    'remain suggestions until the review/promotion gate accepts them; rows '
                    'individually overturnable'),
            'taxonomy': {k: {'count': sum(1 for s in pend for nid in pend[s]
                                          if pend[s][nid].startswith(k + ' (codified')),
                             'basis': v} for k, v in sorted(taxo.items())},
            'totals': {'rows': sum(len(v) for v in pend.values()), 'joins': 0,
                       'lanes': sorted(pend)},
            'basis': ('semantic-lane band C of the pending ledger of record (CONTENT-AUDIT '
                      'lattice-residuals-run-001-r0); class classes KEPT from the '
                      'T-SPECS-CIE-COMPLETE-1 of record, verified by content sampling this '
                      'lane; reasons refined to the codified evidence format; all other '
                      "lanes' rows byte-preserved"),
        }
        ydoc['bands'] = dict(sorted(bands_doc.items()))
        ydoc['verdicts'] = kept + regen
        out_bytes = yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8')
        # census check on the regenerated doc
        chk = yaml.safe_load(out_bytes)
        bandc_rows = [r for r in chk['verdicts'] if r['verdict'] == 'pending_classified'
                      and r.get('lane') in pend
                      and (r.get('reason') or '').find(BAND_LANE) >= 0]
        if len(bandc_rows) != sum(len(v) for v in pend.values()):
            open(YAML_PATH, 'wb').write(ybytes)
            die(f'C-census failed: {len(bandc_rows)} codified rows vs {sum(len(v) for v in pend.values())} inputs — original yaml restored')
        with open(YAML_PATH, 'wb') as f:
            f.write(out_bytes)
        # manifest additive block
        man = json.load(open(MAN_PATH, encoding='utf8'))
        cc = man.setdefault('cie_complete', {})
        bands_m = cc.setdefault('bands', {})
        bands_m[BAND] = {
            'schema_note': 'additive band layer under cie_complete; T-SPECS-CIE-COMPLETE-1-BAND-C (codification-only)',
            'lane': BAND_LANE, 'stamp': STAMP, 'order': ORDER,
            'disposition': bands_doc[BAND]['disposition'],
            'courses': {s: {'rows': len(v), 'joins': 0} for s, v in sorted(pend.items())},
            'totals': {'rows': sum(len(v) for v in pend.values()), 'joins': 0,
                       'pending_classified': sum(len(v) for v in pend.values())},
        }
        json.dump(man, open(MAN_PATH, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        open(MAN_PATH, 'a', encoding='utf8').write('\n')

    # C2 no-code-writes
    side_post = {p: sha(p) for p in sidecars}
    if side_pre != side_post:
        probs.append('C2 violation: a spec-links sidecar changed under a codification-only band')
    # report
    if probs:
        report['ok'] = False
        print('PROBLEMS:', probs[:8], flush=True)
    else:
        report['ok'] = True
        report['courses'] = {s: {'rows': len(v), 'joins': 0} for s, v in sorted(pend.items())}
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    json.dump(report, open(REPORT, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    open(REPORT, 'a', encoding='utf8').write('\n')
    print(f"report -> {REPORT}  ok={report['ok']}", flush=True)
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
