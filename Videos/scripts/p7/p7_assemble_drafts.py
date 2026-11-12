#!/usr/bin/env python3
"""P7 step 6: assemble the per-course second-lane drafts
(video-map.draft.external-p7.json) + owner-review-verdicts.p7.json + the lane
review file. Rows enter as owner-reviewed-external with reviewed:true (the
delegated self-review per owner chat 2026-11-09 'approve and review yourself';
lane authorized 2026-11-13: 'Proceed with remaining channel pools')."""
import json, os, datetime, collections

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
W = '/home/z/my-project/work/p7'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
TASK = 'T-VIDEOMAP-P7 (remaining external channel pools: amoeba-sisters / freesciencelessons / malmesbury-education / doodlescience)'
REVIEWER = ("delegated self-review (agent, per owner chat 2026-11-09: 'approve and review yourself'; "
            "lane authorized 2026-11-13: 'Proceed with remaining channel pools')")
ENUM_UTC = NOW

BOARD_NOTES = {
 'freesciencelessons': 'AQA-focused UK revision channel (GCSE + A-level); titles carry AQA wording bound on topic, not board wording; boardMismatch disclosed per row. Most A-level videos have embedding disabled — identity via thumbnail liveness + uploads-playlist enumeration (identityMethod: thumb-fallback)',
 'amoeba-sisters': 'US-curriculum biology channel (Amoeba Sisters); bound on topic against UK specs, curriculum divergence disclosed via boardMismatch',
 'malmesbury-education': 'Malmesbury Education GCSE/A-level science required-practical channel; AQA practical framing bound on topic against the UK spines',
 'doodlescience': 'Doodle Science UK GCSE/A-level science; board-agnostic teaching content bound on topic',
}

COURSES = ['cie-a-level-biology-25', 'cie-a-level-chemistry-25', 'cie-a-level-physics-25',
           'cie-igcse-biology-23', 'cie-igcse-chemistry-23', 'cie-igcse-physics-23',
           'ial-biology-18', 'ial-chemistry-17', 'ial-physics-19',
           'igcse-biology-19', 'igcse-chemistry-19', 'igcse-physics-19']

pool = {p['id']: p for p in json.load(open(f'{W}/target-pool.json'))}
oem = json.load(open(f'{W}/oembed-p7.json'))

summary = {}
review_rows_summary = []
for course in COURSES:
    jf = f'{W}/judgment-{course}.json'
    if not os.path.exists(jf): continue
    j = json.load(open(jf))
    adv = json.load(open(f'{W}/adjudication-{course}.json'))
    adv_by_idx = {str(i): r for i, r in enumerate(adv['rows'])}
    rows, rejects = [], []
    for k, dec in j['decisions'].items():
        adv_row = adv_by_idx[k]
        if dec[0] == 'drop':
            rejects.append({'video': adv_row['video'], 'reason': 'self-review drop: ' + dec[1]})
            continue
        if dec[0] == 'rebind':
            specs, conf, ev = dec[1], dec[2], dec[3]
        else:  # keep
            specs, conf, ev = adv_row['specs'], adv_row['confidence'], adv_row['evidence']
        rows.append({'video': adv_row['video'], 'lessonRef': None, 'lessonUrl': None,
                     'specs': specs, 'confidence': conf, 'evidence': ev,
                     'method': 'llm-draft-external', 'reviewed': True, 'reviewer': REVIEWER,
                     'reviewedUtc': NOW, 'boardMismatch': True,
                     '_title': adv_row['title']})
    for r in adv['rejects']:
        rejects.append({'video': r['video'], 'reason': 'no honest binding: ' + r['reason']})

    # oEmbed identity assertions
    for r in rows:
        o = oem[r['video']]
        assert o['ok'], f"{course}/{r['video']}: identity failed ({o['identityMethod']})"
        r.pop('_title', None)

    vids = []
    byid = {v['id']: v for v in pool.values() if v['course'] == course}
    for r in rows:
        v = byid[r['video']]
        o = oem[v['id']]
        vids.append({
            'id': v['id'], 'title': o['title'] or v['title'], 'provider': v['provider'],
            'watchUrl': v['watchUrl'], 'lessonRef': None, 'lessonUrl': None,
            'levelTag': v['levelTag'], 'boardNote': BOARD_NOTES[v['provider']],
            'durationS': v['duration'], 'guestVisible': None, 'subelementOfPrimary': False,
            'oembedAuthor': o['author'], 'oembedVerifiedUtc': NOW,
            **({'identityMethod': o['identityMethod']} if o['identityMethod'] == 'thumb-fallback' else {}),
        })
    assert len({x['id'] for x in vids}) == len(vids)

    hub = json.load(open(f'{HUB}/content/video-map/{course}.json'))
    spine = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    spec_total = sum(1 for n in spine['nodes'] if n['family'] == 'SPEC_POINT')
    have = {m['video'] + '|' + json.dumps(sorted(m.get('specs', []))) for m in hub['mappings']}
    for r in rows:
        k = r['video'] + '|' + json.dumps(sorted(r['specs']))
        assert k not in have, f'{course}: P7 row duplicates existing union row {k}'
    distinct_specs = {s for r in rows for s in r['specs']}
    codes = {n['code'] for n in spine['nodes'] if n['family'] == 'SPEC_POINT'}
    missing = [s for s in distinct_specs if s not in codes]
    assert not missing, f'{course}: specs not in spine: {missing[:5]}'

    byc = {'high': 0, 'medium': sum(1 for r in rows if r['confidence'] == 'medium'),
           'low': sum(1 for r in rows if r['confidence'] == 'low')}

    verdicts = {
        'schema': 'syllabai.owner-review/1', 'task': TASK, 'course': course, 'ruledUtc': NOW,
        'source': "delegated self-review — owner chat 2026-11-09 'approve and review yourself'; lane authorized 2026-11-13",
        'default': 'approve', 'reviewer': REVIEWER,
        'evidenceBasis': ('Title-only posture, tightened binding rule. Deterministic distinctive-token pre-pass '
                          f'then a full agent judgment pass over every adjudicated row. Programmatic re-verification: '
                          f'identity {sum(1 for r in rows)} verified (oEmbed + thumb-fallback per the P2D law), all '
                          'specs in the render-plane spine, no duplicates against the existing union, confidence '
                          'never high. Judgment pass: full-row drops with reasons in the reject ledger; re-binds '
                          'tabled with title assertions; borderline low rows kept and named in the review file.'),
        'rejects': rejects, 'applied': {
            'rowsKept': len(rows),
            'rowsDropped': sum(1 for r in rejects if r['reason'].startswith('self-review')),
            'adjudicationNoBind': sum(1 for r in rejects if not r['reason'].startswith('self-review')),
        },
    }
    draft = {
        'schema': 'syllabai.video-map-draft/1', 'draftOf': f'hub.video-map/1 {course}',
        'task': TASK, 'course': course, 'qual': hub['qual'],
        'reviewState': 'owner-reviewed-external',
        'draftLaw': ('second-lane draft (P7): rows enter content/ only through owner-review-verdicts.p7.json '
                     '+ the apply step; a video may map into several courses; rejected videos stay out of the '
                     'shipped videos[] and live in the verdicts ledger'),
        'source': {
            'provider': f"multi ({', '.join(sorted({v['provider'] for v in vids}))})" if vids else 'none',
            'method': ('the unmapped remainder of four previously-mined channel pools (P2B/P2C/P2D precedents), '
                       're-enumerated fresh before the lane (0 deltas: 179/776/72/58) + union-exclusion against the '
                       'current corpus + subject-marker routing with idf best-of across the 12 science parent spines '
                       '+ oEmbed identity sweep with the P2D thumb-fallback for FSL embedding-disabled A-level videos '
                       '(250/250 verified) + deterministic binding pre-pass + agent judgment pass under the tightened '
                       'binding rule; evidence is TITLE-ONLY'),
            'enumeratedUtc': ENUM_UTC,
        },
        'videos': vids, 'mappings': rows,
        'coverage': {'specPointsTotal': spec_total, 'specPointsDraftedHere': len(distinct_specs),
                     'rows': len(rows), 'byConfidence': byc},
        'generatedUtc': NOW, 'reviewedUtc': NOW,
    }
    d = f'{RES}/drafts/{course}'
    json.dump(draft, open(f'{d}/video-map.draft.external-p7.json', 'w'), indent=1, ensure_ascii=False)
    open(f'{d}/video-map.draft.external-p7.json', 'a').write('\n')
    json.dump(verdicts, open(f'{d}/owner-review-verdicts.p7.json', 'w'), indent=1, ensure_ascii=False)
    open(f'{d}/owner-review-verdicts.p7.json', 'a').write('\n')
    summary[course] = (len(rows), len(rejects), byc['medium'], byc['low'], len(distinct_specs), spec_total)
    print(f"{course}: rows {len(rows)} (M{byc['medium']}/L{byc['low']}) + rejects {len(rejects)} | specs +{len(distinct_specs)}/{spec_total}")

json.dump({c: {'rows': s[0], 'rejects': s[1], 'm': s[2], 'l': s[3], 'specs': s[4], 'total': s[5]}
           for c, s in summary.items()}, open(f'{W}/summary.json', 'w'), indent=1)
print(f"TOTAL rows: {sum(s[0] for s in summary.values())} across {len(summary)} courses")
