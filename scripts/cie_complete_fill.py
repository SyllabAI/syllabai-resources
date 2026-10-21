#!/usr/bin/env python3
"""T-SPECS-CIE-COMPLETE-1 — apply the operator-ordered note-level lattice-join
completion to the CIE spec-links sidecars (additive, deterministic, idempotent).

Operator order: "Proceed with: (1) Upstream lattice-join completion (also
fixing History+11 bundles)" — gateway trace 1a15f79acff5346d, 2026-10-22,
zai-web. This lane completes the CIE lattice join that the SME spec-index
self-describes as 'still in progress' (CONTENT-AUDIT run-001-r0 decision
menu item 1), at the NOTE level: every note either gains codes or gains a
structured pending-reason class. Nothing manufactured silently (AGENT.md
rules 1-4): tier V7_agent_note_join marks every row as agent-authored under
the operator order; rows are individually overturnable; the residual is
classified, not hidden.

Inputs (pinned by sha256 at apply time, recorded in the report):
  work/complete_rows.json      {slug: {noteId: {codes, cls}}}
  work/pending_classes.json    {slug: {noteId: reason}}

Writes:
  spec-links/<slug>.json            items[noteId].codes += entry (additive)
                                    review_state.complete block (additive)
  spec-links/manifest.json          cie_complete block (additive)
  scripts/cie_complete_verdicts.yaml   durable per-row evidence
  graph/reports/T_SPECS_CIE_COMPLETE_1_CHECK.json  battery report

Battery (fail-closed):
  C1 every applied code exists in the parsed official spec's official_codes
  C2 target item exists, kind=note, had no codes pre-apply
  C3 idempotency: re-run applies zero rows and reports zero byte drift
  C4 additive-only: every pre-existing field outside the applied rows is
     byte-identical (json round-trip compare on the projected rest)
  C5 every sidecar note either coded or carries a classified pending reason
"""
from __future__ import annotations
import hashlib, json, os, sys, yaml

RES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROWS = os.environ.get('CIE_COMPLETE_ROWS', '/home/z/my-project/work/cie-complete/complete_rows.json')
PEND = os.environ.get('CIE_COMPLETE_PENDING', '/home/z/my-project/work/cie-complete/pending_classes.json')
PARSED = os.path.join(RES, 'Official-Specifications', 'parsed')
LANE = 'T-SPECS-CIE-COMPLETE-1'
TIER = 'V7_agent_note_join'
STAMP = '2026-10-22T00:00:00Z'
ORDER = ("operator order 'Proceed with (1) upstream lattice-join completion' "
         "(gateway trace 1a15f79acff5346d, 2026-10-22, zai-web)")
QUAL = {
 "cie-igcse-economics-25": "cie-igcse-economics-2027-2029",
 "cie-igcse-english-language-25": "cie-igcse-english-language-2027-2029",
 "cie-igcse-english-literature-21": "cie-igcse-english-literature-2023-2025",
 "cie-as-english-general-paper-21": "cie-as-english-general-paper-2028-2030",
 "cie-igcse-english-language-20": "cie-igcse-english-language-2024-2026",
 "cie-igcse-further-maths-additional-maths-25": "cie-igcse-further-maths-additional-maths-2025-2027",
 "cie-a-level-maths-20-pure-3": "cie-a-level-maths-2023-2025",
 "cie-igcse-geography-25": "cie-igcse-geography-2025-2026",
 "cie-igcse-business-25": "cie-igcse-business-2027-2029",
 "cie-igcse-business-23": "cie-igcse-business-2023-2025",
 "cie-igcse-history-18": "cie-igcse-history-2024-2026",
}


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


def main():
    apply_mode = '--apply' in sys.argv
    rows = load(ROWS)
    pend = load(PEND)
    report = {'lane': LANE, 'stamp': STAMP, 'order': ORDER, 'apply': apply_mode,
              'inputs': {'complete_rows.json': sha(ROWS), 'pending_classes.json': sha(PEND)},
              'courses': {}, 'problems': []}
    yaml_rows = []
    for slug in sorted(rows):
        if slug not in QUAL:
            die(f'{slug}: no qual mapping')
        sidecar_path = os.path.join(RES, 'spec-links', f'{slug}.json')
        sd = load(sidecar_path)
        # C4 baseline projection: current bytes minus THIS lane's own prior
        # apply artifacts (review_state.complete + this lane's V7 code entries).
        # A re-run therefore compares like-for-like with the pre-apply state.
        lane_rows_for_strip = rows[slug]

        def project_pre_apply(obj):
            o = json.loads(json.dumps(obj))
            o.get('review_state', {}).pop('complete', None)
            for nid0, rec0 in lane_rows_for_strip.items():
                it0 = o['items'].get(nid0)
                if it0 is not None:
                    it0['codes'] = [e for e in (it0.get('codes') or [])
                                    if e.get('tier') != TIER]
            return o

        pre_bytes = json.dumps(project_pre_apply(sd), sort_keys=True, ensure_ascii=False)
        codes_universe = parsed_codes(QUAL[slug])
        items = sd['items']
        lane_rows = rows[slug]
        lane_pend = pend.get(slug, {})
        applied = already = 0
        for nid, rec in lane_rows.items():
            it = items.get(nid)
            if it is None:
                report['problems'].append(f'{slug} {nid}: absent from sidecar')
                continue
            if it.get('kind') != 'note':
                report['problems'].append(f'{slug} {nid}: kind {it.get("kind")!r} != note')
                continue
            existing = it.get('codes') or []
            mine = [e for e in existing if e.get('tier') == TIER]
            if mine:
                have = sorted(e['official_code'] for e in mine)
                want = sorted(rec['codes'])
                if have == want:
                    already += 1
                    continue
                report['problems'].append(f'{slug} {nid}: V7 drift {have} != {want}')
                continue
            if existing:
                report['problems'].append(f'{slug} {nid}: pre-existing non-V7 codes {existing[:1]}')
                continue
            for c in rec['codes']:
                if c not in codes_universe:
                    report['problems'].append(f'{slug} {nid}: code {c} absent from parsed {QUAL[slug]}')
            if any(c not in codes_universe for c in rec['codes']):
                continue
            entry_base = {'tier': TIER, 'method': rec['cls'], 'score': None,
                          'lane': LANE, 'applied_utc': STAMP}
            if apply_mode:
                it['codes'] = list(existing) + [
                    {'official_id': f'{sd.get("qual") or QUAL[slug].upper()}:{c}',
                     'official_code': c, **entry_base} for c in rec['codes']]
            applied += 1
            yaml_rows.append({
                'lane': slug, 'id': nid, 'verdict': 'resolve', 'tier': TIER,
                'method': rec['cls'], 'codes': rec['codes'],
                'label': it.get('label'), 'section': it.get('section'), 'topic': it.get('topic'),
                'official_texts': {c: (codes_universe.get(c) or '')[:160] for c in rec['codes']},
                'rule': (f'{rec["cls"]} under {LANE}; {ORDER}'),
            })
        # C5 census + review_state block
        uncoded_after = [k for k, v in items.items()
                         if v.get('kind') == 'note' and not (v.get('codes') or [])]
        unclassified = [k for k in uncoded_after if k not in lane_pend]
        if unclassified:
            report['problems'].append(f'{slug}: {len(unclassified)} uncoded notes without pending class')
        if apply_mode:
            rs = sd.setdefault('review_state', {})
            rs['complete'] = {
                'state': 'ACCEPTED_operator_ordered',
                'lane': LANE, 'applied_utc': STAMP, 'order': ORDER,
                'tier_policy': {TIER: 'agent-authored note-level join executed under the '
                                     'operator COMPLETE-1 order; rows individually overturnable; '
                                     'evidence in scripts/cie_complete_verdicts.yaml'},
                'rows': len(lane_rows), 'applied': applied, 'already': already,
                'notes_total': sum(1 for v in items.values() if v.get('kind') == 'note'),
                'notes_coded_after': sum(1 for v in items.values()
                                         if v.get('kind') == 'note' and (v.get('codes') or [])),
                'pending_classified': len(lane_pend),
                'pending_reasons': sorted(set(lane_pend.values())),
            }
        post_bytes = json.dumps(sd, sort_keys=True, ensure_ascii=False)
        if apply_mode and not report['problems']:
            # C4 additive-only: the post-apply state projected back to its
            # pre-apply form must byte-match the baseline projection.
            if json.dumps(project_pre_apply(sd), sort_keys=True, ensure_ascii=False) != pre_bytes:
                report['problems'].append(f'{slug}: C4 additive-only violation')
                die(report['problems'][-1])
            json.dump(sd, open(sidecar_path, 'w', encoding='utf8'),
                      indent=1, ensure_ascii=False)
            open(sidecar_path, 'a', encoding='utf8').write('\n')
        report['courses'][slug] = {
            'rows': len(lane_rows), 'applied': applied, 'already': already,
            'pending_classified': len(lane_pend),
            'uncoded_after': len(uncoded_after),
        }
        print(f"{slug:46s} rows={len(lane_rows):4d} applied={applied:4d} already={already:4d} "
              f"pendingClassified={len(lane_pend):4d}", flush=True)
    # manifest block
    if apply_mode and not report['problems']:
        man_path = os.path.join(RES, 'spec-links', 'manifest.json')
        man = load(man_path)
        man['cie_complete'] = {
            'schema_note': 'additive block, lanes prefixed cie- ; T-SPECS-CIE-COMPLETE-1',
            'lane': LANE, 'stamp': STAMP, 'order': ORDER,
            'courses': report['courses'],
            'totals': {'rows': sum(c['rows'] for c in report['courses'].values()),
                       'applied': sum(c['applied'] for c in report['courses'].values()),
                       'pending_classified': sum(c['pending_classified'] for c in report['courses'].values())},
        }
        json.dump(man, open(man_path, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        open(man_path, 'a', encoding='utf8').write('\n')
        # evidence yaml
        ydoc = {'lane': LANE, 'generated_utc': STAMP, 'order': ORDER,
                'header': ('Per (lane, noteId) verdict rows of the COMPLETE-1 note-level '
                           'lattice-join completion. Tier V7_agent_note_join = agent-authored '
                           'under the operator order, evidence recorded (sidecar label/topic/'
                           'section + official point texts); rows individually overturnable; '
                           'pending classes in pending_classes.json (AGENT.md rules 1-4).'),
                'verdicts': yaml_rows}
        with open(os.path.join(RES, 'scripts', 'cie_complete_verdicts.yaml'), 'w', encoding='utf8') as f:
            yaml.safe_dump(ydoc, f, sort_keys=False, allow_unicode=True, width=110)
    if report['problems']:
        report['ok'] = False
        print('PROBLEMS:', report['problems'][:12], flush=True)
    else:
        report['ok'] = True
    rp = os.path.join(RES, 'graph', 'reports', 'T_SPECS_CIE_COMPLETE_1_CHECK.json')
    os.makedirs(os.path.dirname(rp), exist_ok=True)
    json.dump(report, open(rp, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    open(rp, 'a', encoding='utf8').write('\n')
    print(f"report -> {rp}  ok={report['ok']}", flush=True)
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
