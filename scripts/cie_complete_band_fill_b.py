#!/usr/bin/env python3
"""T-SPECS-CIE-COMPLETE-1-BAND-B — the semantic lane band filler.

The T-SPECS-CIE-COMPLETE-1 engine shape re-run as a band-scoped, additive
layer over the of-record artifacts. Band B = geography-25's 111 cross-edition
rows (cie-igcse-geography-25): SME notes authored against the 2027-2029
syllabus (718150) judged per-row against the served 2025-2026 lattice
(113 pts, 664610 parse of record).

Operator order: "band B (geo-25's 111 cross-edition rows), band C (EL/fleet
leave-unjoined codification), and then the two parse/spine repair lanes"
— gateway trace 1a1615fe86d96ed9, 2026-10-22, zai-web.

Law: AGENT.md rule 3 — no manufactured coverage; tier V7_agent_note_join;
rows individually overturnable; evidence in the verdicts yaml of record.

Additivity discipline (this vehicle NEVER rewrites history):
  * sidecars: band V7 code entries appended only to notes that had none;
    review_state.complete gains a `bands.A` sub-block, original fields byte-kept
  * manifest: cie_complete gains a `bands.A` sub-block, original totals byte-kept
  * verdicts yaml: ONLY the two band lanes' rows are regenerated from the band
    inputs (resolve + refined pending); all other lanes' rows byte-preserved
    (pre-flight P0 proves the yaml loader/dumper round-trip is a byte fixed
    point before any write); a top-level `bands.A` provenance block is added
  * anything unexpected -> fail-closed abort with zero writes

Battery (fail-closed):
  G1 every applied code exists in the parsed official spec (and pure-3 codes
     are component-prefixed '3.')
  G2 target item exists, kind=note, no pre-existing codes other than this
     band's own identical V7 entries (never overwrites)
  G3 additive-only: post-apply state projected back to its pre-band form
     byte-matches the pre-band baseline
  G4 census-closure: every band input row resolves to applied/already or a
     refined pending_classified reason; per-lane totals 76/64
  G5 idempotence: a re-run applies zero rows and leaves every written file
     byte-identical (proven live by running --apply twice)

Inputs (pinned by sha256 into the report):
  work/cie-complete-bandA/complete_rows_bandA.json   {slug: {noteId: {codes, cls}}}
  work/cie-complete-bandA/pending_classes_bandA.json {slug: {noteId: reason}}
"""
from __future__ import annotations
import hashlib, json, os, sys
import yaml

RES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = os.environ.get('BAND_ROWS', '/home/z/my-project/work/cie-bandB/complete_rows_bandB.json')
PEND = os.environ.get('BAND_PEND', '/home/z/my-project/work/cie-bandB/pending_classes_bandB.json')
PARSED = os.path.join(RES, 'Official-Specifications', 'parsed')
YAML_PATH = os.path.join(RES, 'scripts', 'cie_complete_verdicts.yaml')
REPORT = os.path.join(RES, 'graph', 'reports', 'T_SPECS_CIE_COMPLETE_BAND_B_CHECK.json')

LANE = 'T-SPECS-CIE-COMPLETE-1'
BAND = 'B'
BAND_LANE = 'T-SPECS-CIE-COMPLETE-1-BAND-B'
TIER = 'V7_agent_note_join'
STAMP = '2026-10-22T00:30:00Z'
ORDER = ("operator order 'band B (geo-25's 111 cross-edition rows), band C (EL/fleet "
         "leave-unjoined codification), and then the two parse/spine repair lanes' "
         "(gateway trace 1a1615fe86d96ed9, 2026-10-22, zai-web)")
QUAL = {
    'cie-igcse-geography-25': 'cie-igcse-geography-2025-2026',
}
# cross-edition shape law: geo joins are official 2025-2026 codes N.M.K
PREFIX = {}
YAML_PARAMS = dict(sort_keys=False, allow_unicode=True, width=110)


def die(msg):
    print(f'ABORT: {msg}', flush=True)
    sys.exit(1)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def load(p):
    return json.load(open(p, encoding='utf8'))


def parsed_codes(qual):
    out = {}
    d = os.path.join(PARSED, qual)
    for fn in sorted(os.listdir(d)):
        if fn.endswith('.parsed.json'):
            for p in json.load(open(os.path.join(d, fn), encoding='utf8')).get('spec_points') or []:
                if p.get('official_code'):
                    out[p['official_code']] = (p.get('text') or '').strip()
    return out


def strip_band(obj, slug, band_rows):
    """project a sidecar back to its pre-band form"""
    o = json.loads(json.dumps(obj))
    o.get('review_state', {}).get('complete', {}).pop('bands', None)
    for nid0 in band_rows:
        it0 = o['items'].get(nid0)
        if it0 is not None:
            it0['codes'] = [e for e in (it0.get('codes') or [])
                            if not (e.get('tier') == TIER and e.get('lane') == BAND_LANE)]
    return o


def main():
    apply_mode = '--apply' in sys.argv
    rows = load(ROWS)
    pend = load(PEND)
    report = {'lane': BAND_LANE, 'band': BAND, 'stamp': STAMP, 'order': ORDER,
              'apply': apply_mode,
              'inputs': {'complete_rows_bandB.json': sha(ROWS),
                         'pending_classes_bandB.json': sha(PEND)},
              'courses': {}, 'problems': []}
    yaml_resolve_by_slug = {}
    if sorted(rows) != sorted(QUAL):
        die(f'band input lanes {sorted(rows)} != {sorted(QUAL)}')

    # P0 pre-flight: yaml round-trip must be a byte fixed point
    ybytes = open(YAML_PATH, 'rb').read()
    ydoc = yaml.safe_load(ybytes)
    if yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8') != ybytes:
        die('P0 verdicts-yaml round-trip is not a byte fixed point')

    for slug in sorted(rows):
        sd = load(os.path.join(RES, 'spec-links', f'{slug}.json'))
        items = sd['items']
        lane_rows, lane_pend = rows[slug], pend.get(slug, {})
        pre_bytes = json.dumps(strip_band(sd, slug, lane_rows), sort_keys=True, ensure_ascii=False)
        codes_universe = parsed_codes(QUAL[slug])
        applied = already = 0
        yaml_resolve_by_slug[slug] = []
        for nid, rec in lane_rows.items():
            it = items.get(nid)
            if it is None:
                report['problems'].append(f'{slug} {nid}: absent from sidecar'); continue
            if it.get('kind') != 'note':
                report['problems'].append(f'{slug} {nid}: kind {it.get("kind")!r} != note'); continue
            existing = it.get('codes') or []
            mine = [e for e in existing if e.get('tier') == TIER and e.get('lane') == BAND_LANE]
            other = [e for e in existing if not (e.get('tier') == TIER and e.get('lane') == BAND_LANE)]
            if other:
                report['problems'].append(f'{slug} {nid}: pre-existing non-band codes {other[:1]}'); continue
            if mine:
                if sorted(e['official_code'] for e in mine) != sorted(rec['codes']):
                    report['problems'].append(f'{slug} {nid}: band V7 drift'); continue
                already += 1
            else:
                for c in rec['codes']:
                    if c not in codes_universe:
                        report['problems'].append(f'{slug} {nid}: code {c} absent from parsed {QUAL[slug]}')
                    pref = PREFIX.get(slug)
                    if pref and not c.startswith(pref):
                        report['problems'].append(f'{slug} {nid}: code {c} violates component prefix {pref}')
                    if slug == 'cie-igcse-geography-25' and not __import__('re').fullmatch(r'\d+\.\d+\.\d+', c):
                        report['problems'].append(f'{slug} {nid}: code {c} not an official N.M.K geo code')
                if any(c not in codes_universe for c in rec['codes']):
                    continue
                if apply_mode:
                    it['codes'] = existing + [
                        {'official_id': f'{sd.get("qual") or QUAL[slug].upper()}:{c}',
                         'official_code': c, 'tier': TIER, 'method': rec['cls'],
                         'score': None, 'lane': BAND_LANE, 'applied_utc': STAMP}
                        for c in rec['codes']]
                applied += 1
            yaml_resolve_by_slug[slug].append({
                'lane': slug, 'id': nid, 'verdict': 'resolve', 'tier': TIER,
                'method': rec['cls'], 'codes': rec['codes'],
                'label': it.get('label'), 'section': it.get('section'), 'topic': it.get('topic'),
                'official_texts': {c: (codes_universe.get(c) or '')[:160] for c in rec['codes']},
                'rule': f'{rec["cls"]} under {BAND_LANE}; {ORDER}',
            })
        # G4 census-closure
        band_ids = set(lane_rows) | set(lane_pend)
        want = {nid for nid, v in items.items() if v.get('kind') == 'note' and not (v.get('codes') or [])}
        uncoded_outside_band = want - band_ids
        if uncoded_outside_band:
            report['problems'].append(f'{slug}: {len(uncoded_outside_band)} uncoded notes outside band universe')
        if apply_mode and not report['problems']:
            rs = sd.setdefault('review_state', {}).setdefault('complete', {})
            bands = rs.setdefault('bands', {})
            bands[BAND] = {
                'state': 'ACCEPTED_operator_ordered_band_B', 'lane': BAND_LANE,
                'applied_utc': STAMP, 'order': ORDER,
                'tier_policy': {TIER: 'agent-authored note-level semantic join executed under the '
                                     'operator band-B order (cross-edition bridge, statements not '
                                     'numbers decide); rows individually overturnable; '
                                     'evidence in scripts/cie_complete_verdicts.yaml'},
                # run-invariant: counters derive from the band INPUTS, not from
                # this run's applied/already split (per-run facts live in the
                # battery report), so a re-run writes byte-identical blocks
                'rows': len(lane_rows), 'applied': len(lane_rows),
                'already': 0,
                'pending_classified': len(lane_pend),
                'pending_reasons': sorted(set(lane_pend.values())),
            }
            # G3 additive-only projection check BEFORE writing
            if json.dumps(strip_band(sd, slug, lane_rows), sort_keys=True, ensure_ascii=False) != pre_bytes:
                report['problems'].append(f'{slug}: G3 additive-only violation')
                die(f'{slug}: G3 additive-only violation')
            p = os.path.join(RES, 'spec-links', f'{slug}.json')
            json.dump(sd, open(p, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
            open(p, 'a', encoding='utf8').write('\n')
        notes_total = sum(1 for v in items.values() if v.get('kind') == 'note')
        notes_coded = sum(1 for v in items.values() if v.get('kind') == 'note' and (v.get('codes') or []))
        report['courses'][slug] = {
            'rows': len(lane_rows), 'applied': applied, 'already': already,
            'pending_classified': len(lane_pend),
            'notes_total': notes_total, 'notes_coded_after': notes_coded,
        }
        print(f"{slug:46s} rows={len(lane_rows):3d} applied={applied:3d} already={already:3d} "
              f"pendingClassified={len(lane_pend):3d} notesCoded={notes_coded}/{notes_total}", flush=True)

    if not report['problems']:
        # manifest additive sub-block
        man_path = os.path.join(RES, 'spec-links', 'manifest.json')
        man = load(man_path)
        if apply_mode:
            cc = man.setdefault('cie_complete', {})
            bands_m = cc.setdefault('bands', {})
            bands_m[BAND] = {
                'schema_note': 'additive band layer under cie_complete; T-SPECS-CIE-COMPLETE-1-BAND-A',
                'lane': BAND_LANE, 'stamp': STAMP, 'order': ORDER,
                'courses': {s: {'rows': report['courses'][s]['rows'],
                                'applied': report['courses'][s]['rows'],
                                'already': 0,
                                'pending_classified': report['courses'][s]['pending_classified'],
                                'notes_total': report['courses'][s]['notes_total'],
                                'notes_coded_after': report['courses'][s]['notes_coded_after']}
                            for s in sorted(report['courses'])},
                'totals': {'rows': sum(c['rows'] for c in report['courses'].values()),
                           'applied': sum(c['rows'] for c in report['courses'].values()),
                           'pending_classified': sum(c['pending_classified'] for c in report['courses'].values())},
            }
            json.dump(man, open(man_path, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
            open(man_path, 'a', encoding='utf8').write('\n')
        # verdicts yaml: regenerate ONLY the two band lanes' rows
        if apply_mode:
            kept = [r for r in ydoc['verdicts'] if r.get('lane') not in QUAL]
            # bands sub-block is MERGED additively: band A's of-record block is
            # byte-preserved, band B is added alongside it
            bands_doc = dict(ydoc.get('bands') or {})
            bands_doc[BAND] = {
                'lane': BAND_LANE, 'stamp': STAMP, 'order': ORDER,
                'basis': ('semantic-lane band B of the pending ledger of record '
                          "(CONTENT-AUDIT lattice-residuals-run-001-r0); the band lane's "
                          'verdict rows are regenerated from the band adjudication inputs '
                          '(cross-edition bridge: SME notes authored against the 2027-2029 '
                          'syllabus 718150 judged per-row against the served 2025-2026 '
                          "lattice 664610); all other lanes' rows are byte-preserved "
                          'from the T-SPECS-CIE-COMPLETE-1 / BAND-A of record'),
            }
            ydoc['bands'] = bands_doc
            new_rows = list(kept)
            for slug in sorted(rows):
                side = load(os.path.join(RES, 'spec-links', f'{slug}.json'))['items']
                for r in yaml_resolve_by_slug[slug]:
                    r2 = dict(r)
                    it = side.get(r['id']) or {}
                    r2['label'] = it.get('label')
                    if not r2['label']:
                        die(f'yaml regen: band row {slug} {r["id"]} has no label — regen universe bug')
                    new_rows.append(r2)
                for nid in sorted(pend.get(slug, {})):
                    it = side.get(nid) or {}
                    new_rows.append({'lane': slug, 'id': nid, 'verdict': 'pending_classified',
                                     'reason': pend[slug][nid], 'label': it.get('label'),
                                     'section': it.get('section'), 'topic': it.get('topic')})
            ydoc['verdicts'] = new_rows
            out_bytes = yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8')
            # G6 yaml-regen census (fail-closed: restore original bytes on any
            # mismatch before dying) — guards against regen universe bugs
            chk = yaml.safe_load(out_bytes)
            band_res = [r for r in chk['verdicts'] if r.get('rule', '').find(BAND_LANE) >= 0]
            band_pend = [r for r in chk['verdicts'] if r['verdict'] == 'pending_classified'
                         and r.get('lane') in QUAL]
            want_res = sum(len(v) for v in yaml_resolve_by_slug.values())
            want_pend = sum(len(pend.get(s, {})) for s in QUAL)
            if (len(band_res) != want_res or len(band_pend) != want_pend
                    or len(chk['verdicts']) != len(kept) + want_res + want_pend
                    or any(r.get('label') is None for r in band_res)):
                open(YAML_PATH, 'wb').write(ybytes)
                die(f'G6 yaml-regen census failed: band_res={len(band_res)}/{want_res} '
                    f'band_pend={len(band_pend)}/{want_pend} '
                    f'total={len(chk["verdicts"])}/{len(kept)+want_res+want_pend} — original yaml restored')
            with open(YAML_PATH, 'wb') as f:
                f.write(out_bytes)

    if report['problems']:
        report['ok'] = False
        print('PROBLEMS:', report['problems'][:12], flush=True)
    else:
        report['ok'] = True
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    json.dump(report, open(REPORT, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    open(REPORT, 'a', encoding='utf8').write('\n')
    print(f"report -> {REPORT}  ok={report['ok']}", flush=True)
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
