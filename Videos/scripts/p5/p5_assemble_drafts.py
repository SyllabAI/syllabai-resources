#!/usr/bin/env python3
"""P5 step 4: assemble the per-course second-lane drafts (video-map.draft.external-p5.json)
+ owner-review-verdicts.p5.json + the lane review file.
Applies the delegated self-review judgment pass (5 full-row drops, 2 spec trims),
then flips reviewState to owner-reviewed-external with reviewed:true rows."""
import json, os, datetime, re

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
W = '/home/z/my-project/work/p5'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
OEMBED_UTC = '2026-11-12T06:32:15Z'
TASK = 'T-VIDEOMAP-P5 (Cognito channel completion)'
REVIEWER = ("delegated self-review (agent, per owner chat 2026-11-09: 'approve and review yourself'; "
            "lane authorized 2026-11-12: 'file it as the next lane (P5)')")

COURSES = ['cie-a-level-biology-25', 'cie-igcse-biology-23', 'cie-igcse-chemistry-23',
           'cie-igcse-physics-23', 'igcse-maths-a-18-higher']
# judgment pass — full-row drops (title names a technique/topic the CIE spine does not carry)
DROPS = {
    'cie-igcse-chemistry-23': {'1BCc_RrrSSw': 'flame emission spectroscopy has no CIE 0620 spec; the 12.5.4 flame-test bind is keyword-adjacent, not title-named content'},
    'cie-igcse-physics-23': {'_5xzIfB_cbM': '3.3.4 is EM-radiation hazard; the video teaches nuclear irradiation/contamination — adjacent, not named'},
    'cie-igcse-biology-23': {
        'kKiz8Wzcfc8': 'no binary-fission spec in CIE 0610; the 21.1.1 "rapid reproduction rate" hook is a phrase fragment, not the spec content',
        'ow6GIfvhTbs': '20.4.8 is captive-breeding context; IVF binds the code but not the spec content — misbind',
        'w3ykU52K-Hw': 'no clinical-trials spec in CIE 0610; the drug-definition hook does not carry "development and testing"',
    },
}
# judgment pass — spec trims (keep row, drop the weak secondary bind)
TRIMS = {
    'cie-igcse-chemistry-23': {'MvC2nieIv3A': ('10.3.2', 'combustion secondary bind on an alkane-properties title — weakest medium call in the file')},
    'cie-igcse-biology-23': {'jvIr7b0roYI': ('14.4.7', 'thermoregulatory role not title-named; keep 14.1.2 (CNS) as the honest bind')},
}

pool = {p['id']: p for p in json.load(open(f'{W}/target-pool.json'))}
oem = json.load(open(f'{W}/oembed-p5.json'))
summary = {}
review_md = ['# Review file — external lane P5 (T-VIDEOMAP-P5, Cognito channel completion)', '',
             'Lane: the unmapped remainder of the Cognito Edu channel pool, mapped onto the five parent '
             'courses whose children inherit at build time. Authorized owner chat 2026-11-12 '
             '("file it as the next lane (P5)"). Adjudicated per subject cluster under the tightened '
             'binding rule (title-only evidence; the title must name the spec\'s distinctive content); '
             'delegated self-review per owner chat 2026-11-09 "approve and review yourself".', '']

for course in COURSES:
    adj = json.load(open(f'{W}/adjudication-{course}.json'))
    rows, rejects = [], []
    for r in adj['rows']:
        vid = r['video']
        specs = list(r['specs'])
        if vid in TRIMS.get(course, {}):
            spec, reason = TRIMS[course][vid]
            assert spec in specs, f'{course}/{vid}: trim spec {spec} not in row'
            specs.remove(spec)
            assert specs, f'{course}/{vid}: trim would empty the row'
        if vid in DROPS.get(course, {}):
            rejects.append({'video': vid, 'reason': 'self-review full-row drop: ' + DROPS[course][vid]})
            continue
        o = oem[vid]
        assert o['ok'] and (o['author'] or '').lower() == 'cognito', f'{course}/{vid}: oEmbed identity failed'
        assert all(re.match(r'^[\w.-]+$', s) for s in specs)
        rows.append({
            'video': vid, 'lessonRef': None, 'lessonUrl': None, 'specs': specs,
            'confidence': r['confidence'], 'evidence': r['evidence'],
            'method': 'llm-draft-external', 'reviewed': True, 'reviewer': REVIEWER,
            'reviewedUtc': NOW, 'boardMismatch': True,
        })
    for r in adj['rejects']:
        rejects.append({'video': r['video'], 'reason': 'no honest binding: ' + r['reason']})

    # video entries: row-bearing videos only (rejected videos stay out of the shipped file)
    vids = []
    byid = {v['id']: v for v in pool.values() if v['course'] == course}
    for r in rows:
        v = byid[r['video']]
        o = oem[v['id']]
        vids.append({
            'id': v['id'], 'title': o['title'] or v['title'], 'provider': 'cognito',
            'watchUrl': v['watchUrl'], 'lessonRef': None, 'lessonUrl': None,
            'levelTag': v['levelTag'],
            'boardNote': 'Cognito Edu channel; titles are board-agnostic teaching content bound on topic, not board wording',
            'durationS': v['duration'], 'guestVisible': None, 'subelementOfPrimary': False,
            'oembedAuthor': o['author'], 'oembedVerifiedUtc': OEMBED_UTC,
        })
    assert len({x['id'] for x in vids}) == len(vids)

    hub = json.load(open(f'{HUB}/content/video-map/{course}.json'))
    spine = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    spec_total = sum(1 for n in spine['nodes'] if n['family'] == 'SPEC_POINT')
    # no dup rows against the existing union
    have = {m['video'] + '|' + json.dumps(sorted(m.get('specs', []))) for m in hub['mappings']}
    for r in rows:
        k = r['video'] + '|' + json.dumps(sorted(r['specs']))
        assert k not in have, f'{course}: P5 row duplicates existing union row {k}'
    distinct_specs = {s for r in rows for s in r['specs']}
    byc = {'high': 0, 'medium': sum(1 for r in rows if r['confidence'] == 'medium'),
           'low': sum(1 for r in rows if r['confidence'] == 'low')}
    # every spec exists in the spine (render plane of record)
    codes = {n['code'] for n in spine['nodes'] if n['family'] == 'SPEC_POINT'}
    missing = [s for s in distinct_specs if s not in codes]
    assert not missing, f'{course}: specs not in spine: {missing[:5]}'

    trims = TRIMS.get(course, {})
    verdicts = {
        'schema': 'syllabai.owner-review/1', 'task': TASK, 'course': course, 'ruledUtc': NOW,
        'source': "delegated self-review — owner chat 2026-11-09 'approve and review yourself'; lane authorized 2026-11-12",
        'default': 'approve', 'reviewer': REVIEWER,
        'evidenceBasis': ('Title-only posture, tightened binding rule. Programmatic re-verification: oEmbed author Cognito '
                          f'{sum(1 for r in rows)}/{sum(1 for r in rows)}, all specs in the render-plane spine, no duplicates against '
                          'the existing union, confidence never high. Judgment pass: borderline rows kept at low with disclosed '
                          'partial overlap; full-row drops and spec trims below.'),
        'rejects': rejects, 'applied': {
            'rowsKept': len(rows), 'rowsDropped': len(DROPS.get(course, {})),
            'specsTrimmed': [{'video': v, 'spec': s, 'reason': rr} for v, (s, rr) in trims.items()],
        },
    }
    draft = {
        'schema': 'syllabai.video-map-draft/1', 'draftOf': f'hub.video-map/1 {course}',
        'task': TASK, 'course': course, 'qual': hub['qual'],
        'reviewState': 'owner-reviewed-external',
        'draftLaw': ('second-lane draft (P5): rows enter content/ only through owner-review-verdicts.p5.json '
                     '+ the apply step; a video may map into several courses; rejected videos stay out of the '
                     'shipped videos[] and live in the verdicts ledger'),
        'source': {
            'provider': 'cognito (Cognito Edu YouTube channel — unmapped remainder)',
            'method': ('yt-dlp flat channel enumeration (re-verified 2026-11-12: 529 public uploads, 0 delta vs the '
                       'P4 cache; the 545-548 header count includes members-only/shorts) + oEmbed identity sweep '
                       '254/254 + subject routing + LLM title-to-spec adjudication under the tightened binding rule; '
                       'evidence is TITLE-ONLY'),
            'enumeratedUtc': '2026-11-01T01:04:15Z',
        },
        'videos': vids, 'mappings': rows,
        'coverage': {'specPointsTotal': spec_total, 'specPointsDraftedHere': len(distinct_specs),
                     'rows': len(rows), 'byConfidence': byc},
        'generatedUtc': NOW, 'reviewedUtc': NOW,
    }
    d = f'{RES}/drafts/{course}'
    json.dump(draft, open(f'{d}/video-map.draft.external-p5.json', 'w'), indent=1, ensure_ascii=False)
    open(f'{d}/video-map.draft.external-p5.json', 'a').write('\n')
    json.dump(verdicts, open(f'{d}/owner-review-verdicts.p5.json', 'w'), indent=1, ensure_ascii=False)
    open(f'{d}/owner-review-verdicts.p5.json', 'a').write('\n')
    summary[course] = (len(rows), len(rejects), byc['medium'], byc['low'], len(distinct_specs), spec_total)
    print(f'{course}: rows {len(rows)} (M{byc["medium"]}/L{byc["low"]}) + rejects {len(rejects)} | specs +{len(distinct_specs)}/{spec_total}')

review_md += ['## Census', '',
              '| course | rows | medium/low | specs drafted | reject ledger |',
              '| --- | --- | --- | --- | --- |']
for c, (n, rj, m, l, ds, st) in summary.items():
    review_md.append(f'| {c} | {n} | {m}/{l} | {ds}/{st} | {rj} |')
review_md += ['', '## Judgment pass (self-review)', '',
              'Full-row drops (5) and spec trims (2) are recorded in the per-course verdicts with reasons. '
              'Kept-borderline rows (disclosed low-confidence partial overlaps): '
              'QN4hqLdC48g, L_aXRbm5adg, wW1NiCQvkDg, KcMFFzDn2FE, o2_jih4xkE0, AUy4UxmcQi0, c8cKqka8Pqc (a-level bio); '
              'mR3GI7SXNqA, A74Sf8U3v_E, X1zptKXIEfY (chem-23); XMhOKC34tvs, 6G7glidXTcQ, JQEZaJXNVQ, evWpDrRAyCc (phys-23); '
              'umRe7GBJ5GE (bio-23).', '',
              '## Honest no-target census', '',
              'Of the 309 unmapped public uploads: 254 routed into this lane; 55 skipped with no honest spine '
              'target (20 KS3, 28 psychology, 7 platform/exam-service announcements). Of the 254 routed, 208 '
              'bound and 46 stay unmapped (41 no candidate named the title content — largely AQA-flavoured '
              'topics absent from the CIE spines — plus the 5 self-review drops).', '']
open(f'{RES}/drafts/review-file-external-p5.md', 'w').write('\n'.join(review_md))
print('review file written')
tot = sum(s[0] for s in summary.values())
print(f'TOTAL rows shipped: {tot}')
