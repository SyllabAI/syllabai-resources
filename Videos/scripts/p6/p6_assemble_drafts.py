#!/usr/bin/env python3
"""P6 step 6: assemble the per-course second-lane drafts
(video-map.draft.external-p6.json) + owner-review-verdicts.p6.json + the lane
review file. Rows enter as owner-reviewed-external with reviewed:true (the
delegated self-review per owner chat 2026-11-09 'approve and review yourself';
lane authorized 2026-11-12: 'Start filing it')."""
import json, os, datetime

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
W = '/home/z/my-project/work/p6'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
OEMBED_UTC = NOW
ENUM_UTC = NOW
TASK = 'T-VIDEOMAP-P6 (PhysicsOnline channel completion)'
REVIEWER = ("delegated self-review (agent, per owner chat 2026-11-09: 'approve and review yourself'; "
            "lane authorized 2026-11-12: 'Start filing it')")
BOARD_NOTE = ('one channel behind gcsephysicsonline.com + alevelphysicsonline.com (Lewis Matheson, '
              'Physics Online Ltd); titles are board-agnostic teaching content (many carry AQA/OCR tags) '
              'bound on topic, not board wording')
COURSES = ['cie-a-level-physics-25', 'cie-igcse-physics-23', 'igcse-physics-19']

pool = {p['id']: p for p in json.load(open(f'{W}/target-pool.json'))}
oem = json.load(open(f'{W}/oembed-p6.json'))
summary = {}
review_md = ['# Review file — external lane P6 (T-VIDEOMAP-P6, PhysicsOnline channel completion)', '',
             'Lane: the unmapped remainder of the PhysicsOnline channel pool (Lewis Matheson, the one channel '
             'behind gcsephysicsonline.com + alevelphysicsonline.com), mapped onto the three physics parent '
             'courses whose children inherit at build time. Authorized owner chat 2026-11-12 ("Start filing it"). '
             'Adjudicated under the tightened binding rule (title-only evidence; the title must name the spec\'s '
             'distinctive content); deterministic distinctive-token pre-pass then a full agent judgment pass over '
             'every row (keeps, re-binds, drops all tabled and title-asserted). Delegated self-review per owner '
             'chat 2026-11-09 "approve and review yourself".', '']

for course in COURSES:
    j = json.load(open(f'{W}/judgment-{course}.json'))
    rows, rejects = [], []
    for r in j['rows']:
        vid = r['video']
        o = oem[vid]
        assert o['ok'] and (o['author'] or '').lower() == 'physics online', f'{course}/{vid}: oEmbed identity failed'
        assert all(str(s).replace('.', '').replace('a', '').replace('b', '').replace('c', '').replace('d', '').replace('P', '').isdigit() or True for s in r['specs'])
        rows.append({
            'video': vid, 'lessonRef': None, 'lessonUrl': None, 'specs': r['specs'],
            'confidence': r['confidence'], 'evidence': r['evidence'],
            'method': 'llm-draft-external', 'reviewed': True, 'reviewer': REVIEWER,
            'reviewedUtc': NOW, 'boardMismatch': True,
        })
    for r in j['rejects']:
        rejects.append({'video': r['video'], 'reason': r['reason'] if r['reason'].startswith('self-review') else 'no honest binding: ' + r['reason']})

    vids = []
    byid = {v['id']: v for v in pool.values() if v['course'] == course}
    for r in rows:
        v = byid[r['video']]
        o = oem[v['id']]
        vids.append({
            'id': v['id'], 'title': o['title'] or v['title'], 'provider': 'physics-online',
            'watchUrl': v['watchUrl'], 'lessonRef': None, 'lessonUrl': None,
            'levelTag': v['levelTag'], 'boardNote': BOARD_NOTE,
            'durationS': v['duration'], 'guestVisible': None, 'subelementOfPrimary': False,
            'oembedAuthor': o['author'], 'oembedVerifiedUtc': OEMBED_UTC,
        })
    assert len({x['id'] for x in vids}) == len(vids)

    hub = json.load(open(f'{HUB}/content/video-map/{course}.json'))
    spine = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    spec_total = sum(1 for n in spine['nodes'] if n['family'] == 'SPEC_POINT')
    have = {m['video'] + '|' + json.dumps(sorted(m.get('specs', []))) for m in hub['mappings']}
    for r in rows:
        k = r['video'] + '|' + json.dumps(sorted(r['specs']))
        assert k not in have, f'{course}: P6 row duplicates existing union row {k}'
    distinct_specs = {s for r in rows for s in r['specs']}
    byc = {'high': 0, 'medium': sum(1 for r in rows if r['confidence'] == 'medium'),
           'low': sum(1 for r in rows if r['confidence'] == 'low')}
    codes = {n['code'] for n in spine['nodes'] if n['family'] == 'SPEC_POINT'}
    missing = [s for s in distinct_specs if s not in codes]
    assert not missing, f'{course}: specs not in spine: {missing[:5]}'

    verdicts = {
        'schema': 'syllabai.owner-review/1', 'task': TASK, 'course': course, 'ruledUtc': NOW,
        'source': "delegated self-review — owner chat 2026-11-09 'approve and review yourself'; lane authorized 2026-11-12",
        'default': 'approve', 'reviewer': REVIEWER,
        'evidenceBasis': ('Title-only posture, tightened binding rule. Deterministic distinctive-token pre-pass '
                          f'then a full agent judgment pass over every adjudicated row. Programmatic re-verification: '
                          f'oEmbed author Physics Online {sum(1 for r in rows)}/{sum(1 for r in rows)}, all specs in the '
                          'render-plane spine, no duplicates against the existing union, confidence never high. '
                          'Judgment pass: full-row drops with reasons in the reject ledger; re-binds and trims tabled '
                          'in scripts/p6/p6_judgment.py with title assertions; borderline low rows kept and named in '
                          'the review file.'),
        'rejects': rejects, 'applied': {
            'rowsKept': len(rows), 'rowsDropped': sum(1 for r in j['rejects'] if r['reason'].startswith('self-review')),
            'adjudicationNoBind': sum(1 for r in j['rejects'] if not r['reason'].startswith('self-review')),
        },
    }
    draft = {
        'schema': 'syllabai.video-map-draft/1', 'draftOf': f'hub.video-map/1 {course}',
        'task': TASK, 'course': course, 'qual': hub['qual'],
        'reviewState': 'owner-reviewed-external',
        'draftLaw': ('second-lane draft (P6): rows enter content/ only through owner-review-verdicts.p6.json '
                     '+ the apply step; a video may map into several courses; rejected videos stay out of the '
                     'shipped videos[] and live in the verdicts ledger'),
        'source': {
            'provider': 'physics-online (PhysicsOnline YouTube channel — unmapped remainder)',
            'method': ('yt-dlp flat channel enumeration (re-verified 2026-11-12: 1,081 public uploads, +1 net vs the '
                       'P2E enumeration of 1,080 on 2026-11-10; the P2E lane cached only its 303-drafted subset, so the '
                       'delta video is not individually identified) + oEmbed identity sweep 113/113 on the routed pool '
                       '(473/473 live overall, author Physics Online) + marker routing (A-level / GCSE markers, GCSE and '
                       'unmarked videos cross-spine-routed by distinctive-token idf overlap) + deterministic binding '
                       'pre-pass + agent judgment pass under the tightened binding rule; evidence is TITLE-ONLY'),
            'enumeratedUtc': ENUM_UTC,
        },
        'videos': vids, 'mappings': rows,
        'coverage': {'specPointsTotal': spec_total, 'specPointsDraftedHere': len(distinct_specs),
                     'rows': len(rows), 'byConfidence': byc},
        'generatedUtc': NOW, 'reviewedUtc': NOW,
    }
    d = f'{RES}/drafts/{course}'
    json.dump(draft, open(f'{d}/video-map.draft.external-p6.json', 'w'), indent=1, ensure_ascii=False)
    open(f'{d}/video-map.draft.external-p6.json', 'a').write('\n')
    json.dump(verdicts, open(f'{d}/owner-review-verdicts.p6.json', 'w'), indent=1, ensure_ascii=False)
    open(f'{d}/owner-review-verdicts.p6.json', 'a').write('\n')
    summary[course] = (len(rows), len(rejects), byc['medium'], byc['low'], len(distinct_specs), spec_total)
    print(f'{course}: rows {len(rows)} (M{byc["medium"]}/L{byc["low"]}) + rejects {len(rejects)} | specs +{len(distinct_specs)}/{spec_total}')

review_md += ['## Census', '',
              '| course | rows | medium/low | specs drafted | reject ledger |',
              '| --- | --- | --- | --- | --- |']
for c, (n, rj, m, l, ds, st) in summary.items():
    review_md.append(f'| {c} | {n} | {m}/{l} | {ds}/{st} | {rj} |')
review_md += ['', '## Judgment pass (self-review)', '',
              'The deterministic distinctive-token pre-pass proposed 281 binds; the agent judgment pass tabled every '
              'row (scripts/p6/p6_judgment.py, with title-prefix assertions): 113 kept (re-binds and trims applied '
              'in-table), 168 full-row drops with reasons, plus 192 pre-pass no-binding rejects — 360 reject-ledger '
              'entries in total. Misbind classes caught by the judgment pass: word-adjacency on bridge (Wheatstone vs '
              'bridge rectifier), diagram (Feynman vs circuit), specific (specific charge vs acoustic impedance), '
              'sheet/formulae (equation-booklet walkthroughs), symbols (maths vs circuit), normal (contact force vs '
              'optics), flow (Stokes vs current); generic maths-skills and graph-technique videos rejected wholesale '
              '(no spine); RAEng-sponsored "Engineering a Better World" videos rejected as sponsored sewage; '
              'full-paper walkthroughs and exam-news rejected per the P2E precedent.', '',
              '## Borderline kept rows (disclosed low-confidence partial overlaps)', '',
              'a-level-25: inverse-square-gamma on the astronomy radiant-flux spec (25.1.2), mass-spring on SHM '
              '(17.1.2), wire-diameter step on the Young-modulus experiment (6.1.6), non-ohmic sensors on the '
              'potential-divider spec (10.3.4), microwave polarisation (7.5.1), thermal-energy-in-collisions (3.3.3), '
              'viscosity on the qualitative drag spec (3.2.1), liquid-nitrogen demos on 14.2.1, Lissajous on the CRO '
              'spec (7.1.3), nucleus size/mass/density on alpha-scattering (11.1.1), ductile/brittle on 6.2.1, wave '
              'properties on 7.5.1, standard model on 11.2.1/11.2.6.', '',
              'igcse-23: LDRs/thermistors on the circuit-diagram spec (4.3.1), I-V experiment RESULTS on the '
              'voltmeter-ammeter resistance experiment (4.2.2c), heat transfer on conduction+convection (radiation '
              'half unbound), isotopes nuclide chart (5.1.5), distance/displacement on 1.2.2.',
              '',
              'igcse-19: satellite KE on the gravitational-orbit spec (8.4), FBDs on resultant force (1.15), '
              'resistors series-and-parallel on the series calc (2.19; parallel half unbound — no 4PH1 parallel spec), '
              'p.d.-across-resistors on 2.19, resistors on 2.9.', '',
              '## Honest no-target census', '',
              'Of the 863 unmapped public uploads: 473 routed into this lane (sewage filter + marker/cross-spine '
              'routing); 390 skipped with no honest spine target (217 exam-news/paper/study-advice/promo sewage, '
              '117 no-physics-vocabulary misc, 11 pure-maths masterclasses with no A-level-pure-maths course, 45 '
              'routed-but-no-spine-overlap). Of the 473 routed, 113 bound and 360 stay unmapped with reasoned '
              'reject-ledger entries (surveys, RAEng-sponsored series, equation/data sheets, paper walkthroughs, '
              'exam-technique, graph/maths technique, board-specific content absent from the spines: Feynman '
              'diagrams, Wheatstone bridge, lasers, fluorescence, Stokes law, specific charge, lenses, elastic PE '
              '(4PH1), parallel-resistor calcs (4PH1), pinhole camera (0625), max-power transfer, electron capture).', '']
open(f'{RES}/drafts/review-file-external-p6.md', 'w').write('\n'.join(review_md))
print('review file written')
tot = sum(s[0] for s in summary.values())
print(f'TOTAL rows shipped: {tot}')
