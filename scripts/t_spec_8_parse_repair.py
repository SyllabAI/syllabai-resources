#!/usr/bin/env python3
"""T-SPEC-8 — parse repairs for the flagged parse-gap pendings.

Scope (from the T-SPEC-6/7 verdict records and report parse_notes):

1. ial-maths   The spec's Appendix 7: Notation walk (pages 93-98) was emitted
               with scope 'D1' (last-seen unit), producing 119 bogus D1-*
               rows; three of its codes (3.4, 4.2, 4.4) shadowed the real D1
               unit-content rows, whose texts were lost. Also, the two-column
               unit-content layout interleaved right-column Guidance text into
               the flagged statements D1-2.1 and S2-4.6, and S2-4.6 carried
               assessment-copy sub_items.
               Repair: drop the 119 notation rows, restore the three real D1
               rows and re-extract the two interleaved statements from the
               PDF left column (verbatim, span provenance).

2. igcse-geography   The heading_bullets strategy never matched the content
               walks (Key ideas | Detailed content two-column tables): every
               topic's detailed content statements (lettered a) b) c) plus
               full-width case-study lines) are missing from the parse.
               Repair: extract topics 1-9 content walks from the PDF and
               append them as synthesised-id statements continuing the
               document counter (existing ids are never renumbered).

3. igcse-accounting   Same heading_bullets miss: the content walks for
               Topics 1-5 (bold N subsections, lettered statements, bullet
               sub-items) are missing; the parse retained only bullet
               fragments after false 'Topic N:' matches on overview pages
               (S4.069-S4.072 ratio fragments survive because lanes reference
               them - they are kept, never renumbered).
               Repair: extract Topics 1-5 content walks and append.

4. igcse-maths-a / igcse-maths-a-modular: NO parse change. The Higher
   content-walk statements flagged by T-SPEC-7 are present in both parses
   (verified verbatim); the T-SPEC-7 evidence packs omitted the H-scope
   statements from the per-lane pools. Corrected by the T-SPEC-8 verdict
   round (scripts/t_spec_8_verdicts.yaml + t_spec_8_apply.py), not here.

Every extracted row carries page + oy provenance and flag
't-spec-8-parse-repair'. Existing ids are never altered or renumbered.
Report: graph/reports/T_SPEC_8_PARSE_REPAIR.json (full audit trail).
"""
import json
import re
import sys
import datetime
from pathlib import Path

import pymupdf

BASE = Path('/home/z/my-project/download/syllabai-resources')
SPEC = BASE / 'Official-Specifications'
PARSED = SPEC / 'parsed'
EQ = BASE / 'SME-ExamQuestion'
LINKS = BASE / 'spec-links'
REPORTS = BASE / 'graph' / 'reports'

sys.path.insert(0, str(BASE / 'scripts'))
from spec_parser import page_spans, strip_running_text, visual_lines  # noqa: E402

FLAG = 't-spec-8-parse-repair'
TOPIC_RE = re.compile(r'^Topic (\d+): (.+)$')
REPORT = {
    'schema': 'syllabai.t-spec-8-parse-repair/1.0',
    'generated_utc': datetime.datetime.now(datetime.timezone.utc)
                              .strftime('%Y-%m-%dT%H:%M:%SZ'),
    'parser': 'spec-parser-1.0 + t-spec-8 repair',
    'ial_maths': {'removed': [], 'patched': []},
    'igcse_geography': {'added': [], 'subsections_added': 0},
    'igcse_accounting': {'added': [], 'subsections_added': 0},
    'igcse_maths_a': {'change': 'none - H-walk statements verified present; '
                                'corrected via T-SPEC-8 verdict round'},
}


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def clean_punct(s):
    """Join artifact: no space before closing punctuation, none after '('."""
    s = re.sub(r'\s+([.,;:)])', r'\1', s)
    s = re.sub(r'\(\s+', '(', s)
    return norm(s)


def load_v1(qual, stem):
    return json.loads((PARSED / qual / f'{stem}.parsed.json').read_text())


def save_v1(qual, stem, doc):
    (PARSED / qual / f'{stem}.parsed.json').write_text(
        json.dumps(doc, indent=1, ensure_ascii=False) + '\n')


def synth_id(qual_prefix, topic_number, counter):
    return f'{qual_prefix}:S{topic_number}.{counter:03d}'


def max_synth_counter(rows):
    mx = 0
    for sp in rows:
        m = re.match(r'^S[A-Z0-9]*\.(\d+)$', sp['id'].rsplit(':', 1)[-1])
        if not m:
            m = re.match(r'^SX\.(\d+)$', sp['id'].rsplit(':', 1)[-1])
        if m:
            mx = max(mx, int(m.group(1)))
    return mx


def assert_ids_unreferenced(ids):
    """Fail-closed: none of the removed ids may be referenced anywhere."""
    if not ids:
        return
    needles = list(ids)
    hits = []
    for f in sorted(EQ.glob('*/spec_point_map.json')):
        txt = f.read_text()
        hits += [(f.name, n) for n in needles if n in txt]
    for f in sorted(EQ.glob('*/spec_point_index.json')):
        txt = f.read_text()
        hits += [(f.name, n) for n in needles if n in txt]
    for f in sorted(LINKS.glob('*.json')):
        txt = f.read_text()
        hits += [(f.name, n) for n in needles if n in txt]
    if hits:
        raise SystemExit(f'FAIL: removed ids still referenced: {hits[:5]}')


# ------------------------------------------------------- ial-maths repair ----

def ial_left_col_text(doc, kill, page, code):
    """Extract the left-column ('What students need to learn') text for one
    N.M code row on a two-column IAL maths unit-content page."""
    spans = [s for s in page_spans(doc[page - 1]) if not kill(s)]
    lines = visual_lines(spans)
    collecting = False
    parts = []
    oy = None
    for L in lines:
        t = norm(L['text'])
        if not t:
            continue
        m = re.match(r'^(\d{1,2}\.\d{1,2})\s*(.*)$', t)
        is_code_line = m is not None and L['x0'] < 100
        if is_code_line:
            if m.group(1) == code:
                collecting = True
                oy = round(L['oy'], 1)
                # left-column spans only: the Guidance column shares the line
                first = ' '.join(s['text'] for s in L['spans']
                                 if 75 <= s['x0'] < 272)
                first = norm(first) or m.group(2)
                if first:
                    parts.append(first)
                continue
            if collecting:
                break
        if collecting:
            if L['bold'] and re.match(r'^\d{1,2}\.\s', t):
                break
            if t.startswith('What students need to learn'):
                break
            left = ' '.join(s['text'] for s in L['spans'] if s['x0'] < 272)
            left = norm(left)
            if left:
                parts.append(left)
    return clean_punct(' '.join(parts)), oy


def repair_ial_maths():
    qual, stem = 'ial-maths', 'international-a-level-maths-spec'
    v1 = load_v1(qual, stem)
    rows = v1['spec_points']

    # 1. drop the Appendix-7 notation rows wrongly scoped to D1
    removed = [sp for sp in rows
               if sp.get('scope') == 'D1' and sp['page'] >= 93]
    if len(removed) != 119:
        raise SystemExit(f'FAIL: expected 119 notation rows, found {len(removed)}')
    removed_ids = {sp['id'] for sp in removed}
    assert_ids_unreferenced(removed_ids)
    keep = [sp for sp in rows if sp['id'] not in removed_ids]
    REPORT['ial_maths']['removed'] = sorted(removed_ids)

    # 2. patch the interleaved rows from the PDF left column
    pdf = pymupdf.open(SPEC / qual / f'{stem}.pdf')
    kill = strip_running_text(pdf)
    fixes = [  # (id, code, page, expect_substrings)
        ('IAL_MATHS:D1-2.1', '2.1', 70, ['minimum spanning tree', 'Kruskal']),
        ('IAL_MATHS:S2-4.6', '4.6', 65, ['binomial distribution', 'Poisson']),
    ]
    by_id = {sp['id']: sp for sp in keep}
    for rid, code, page, expects in fixes:
        text, oy = ial_left_col_text(pdf, kill, page, code)
        for ex in expects:
            if ex.lower() not in text.lower():
                raise SystemExit(f'FAIL: {rid} extraction missing {ex!r}: {text!r}')
        sp = by_id[rid]
        before = {'text': sp['text'], 'page': sp['page'], 'oy': sp.get('oy'),
                  'sub_items': sp.get('sub_items')}
        sp['text'] = text
        sp['page'] = page
        sp['oy'] = oy
        if rid == 'IAL_MATHS:S2-4.6':
            sp['sub_items'] = []          # assessment-copy pollution removed
        flags = sp.get('flags') or []
        if FLAG not in flags:
            flags.append(FLAG)
        sp['flags'] = flags
        REPORT['ial_maths']['patched'].append({'id': rid, 'before': before,
                                               'after': {'text': text,
                                                         'page': page,
                                                         'oy': oy}})

    # 3. re-add the three real D1 rows whose code slots the notation rows
    #    shadowed during the original parse (ids preserved, texts restored)
    readds = [  # (id, code, page, sibling-topic-id, expect_substrings)
        ('IAL_MATHS:D1-3.4', '3.4', 70, 'IAL_MATHS:D1-3.3', ['nearest neighbour']),
        ('IAL_MATHS:D1-4.2', '4.2', 71, 'IAL_MATHS:D1-4.1', ['precedence table']),
        ('IAL_MATHS:D1-4.4', '4.4', 71, 'IAL_MATHS:D1-4.3',
         ['Total float', 'Gantt', 'Scheduling']),
    ]
    for rid, code, page, sibling, expects in readds:
        text, oy = ial_left_col_text(pdf, kill, page, code)
        for ex in expects:
            if ex.lower() not in text.lower():
                raise SystemExit(f'FAIL: {rid} extraction missing {ex!r}: {text!r}')
        sib = by_id[sibling]
        new_row = {
            'official_code': code, 'scope': 'D1', 'suffix': '',
            'text': text, 'page': page, 'oy': oy,
            'topic': json.loads(json.dumps(sib.get('topic'))),
            'subsection': None, 'sub_items': [], 'practical': False,
            'flags': [FLAG], 'id': rid,
        }
        # insert after the last real D1 content row to keep page order
        last_d1 = max(i for i, sp in enumerate(keep)
                      if sp.get('scope') == 'D1' and sp['page'] <= 72)
        keep.insert(last_d1 + 1, new_row)
        REPORT['ial_maths']['patched'].append(
            {'id': rid, 'before': None,
             'after': {'text': text, 'page': page, 'oy': oy}})
    pdf.close()

    v1['spec_points'] = keep
    v1['counts']['spec_points'] = len(keep)
    save_v1(qual, stem, v1)
    print(f'ial-maths: -{len(removed)} notation rows, {len(fixes)} rows patched, '
          f'{len(keep)} rows remain')


# ---------------------------------------------------- column streams ---------

def column_lines(doc, kill, pno, x_split):
    """Per-page two-column visual lines: returns (left_lines, right_lines),
    each sorted by origin-y. Span-level x split because key-code rows and the
    first lettered statement share the same baseline in these tables."""
    spans = [s for s in page_spans(doc[pno - 1]) if not kill(s)]
    left = [s for s in spans if s['x0'] < x_split]
    right = [s for s in spans if s['x0'] >= x_split]
    ll = [L for L in visual_lines(left) if norm(L['text'])]
    rr = [L for L in visual_lines(right) if norm(L['text'])]
    ll.sort(key=lambda L: L['oy'])
    rr.sort(key=lambda L: L['oy'])
    return ll, rr


def fkey(L):
    return (round(L['oy'], 1), 0 if L['x0'] < 205 else 1)


# ---------------------------------------------------- geography repair -------

GEOG_STEM = '9781446958360-int-gcse-geog-issue-3'
GEO_STOP_HEADERS = re.compile(
    r'^(?:\d{1,2}\.\d{1,2}\s+)?'
    r'(Assessment of fieldwork skills|Subject content|Assessment objectives'
    r'|Assessment information|Assessment requirements)', re.I)
GEO_COL_HEADERS = {'What students need to learn', 'Key idea', 'Key ideas',
                   'Detailed content', 'Integrated skills'}
GEO_PAGES = range(15, 38)          # content region; stops inside ranges below
BAND_TOL = 3.0                     # baseline jitter between the two columns


def banded_merge(events):
    """events: (oy, col, line). Group lines whose baselines sit within
    BAND_TOL of the band start (two-column tables share baselines with
    sub-point jitter); inside a band left-column events come first so a
    key-idea code row precedes the lettered statement it introduces."""
    events = sorted(events, key=lambda e: e[0])
    bands, cur, start = [], [], None
    for e in events:
        if start is None or e[0] - start <= BAND_TOL:
            cur.append(e)
            if start is None:
                start = e[0]
        else:
            bands.append(cur)
            cur, start = [e], e[0]
    if cur:
        bands.append(cur)
    out = []
    for band in bands:
        band.sort(key=lambda e: (0 if e[1] == 'L' else 1, e[0]))
        out.extend(band)
    return out


def repair_geography():
    qual, stem = 'igcse-geography', GEOG_STEM
    v1 = load_v1(qual, stem)
    rows = v1['spec_points']
    counter = max_synth_counter(rows)
    qual_prefix = 'IGCSE_GEOGRAPHY'
    topic_rows = {}
    for t in v1['topics']:
        topic_rows.setdefault(t['number'], t)   # first row per number (real hdr)

    doc = pymupdf.open(SPEC / qual / f'{stem}.pdf')
    kill = strip_running_text(doc)
    cur_topic = cur_key = cur_stmt = None
    added, sub_rows = [], []
    seen_sub = set()
    for pno in GEO_PAGES:
        stopped = False
        left, right = column_lines(doc, kill, pno, x_split=205)
        all_spans = [s for s in page_spans(doc[pno - 1]) if not kill(s)]
        full = [L for L in visual_lines(all_spans) if norm(L['text'])]
        full.sort(key=lambda L: L['oy'])
        # full-width case-study rows: left edge, regular, reach into the
        # detailed-content column; footnotes/codes/headers excluded
        case_lines = []
        case_oys = []
        for L in full:
            t = norm(L['text'])
            x0 = L['x0']
            if x0 >= 80 or L['bold']:
                continue
            if re.match(r'^\d{1,2}\.\d{1,2}', t) or re.match(r'^\(\d+\)', t):
                continue
            if t in GEO_COL_HEADERS or GEO_STOP_HEADERS.match(t) or TOPIC_RE.match(t):
                continue
            x1 = max(s['x1'] for s in L['spans'])
            if x1 > 300:
                case_lines.append(L)
                case_oys.append(L['oy'])
        def in_case_band(oy):
            return any(abs(oy - c) <= BAND_TOL for c in case_oys)
        events = ([(L['oy'], 'L', L) for L in left]
                  + [(L['oy'], 'R', L) for L in right]
                  + [(L['oy'], 'C', L) for L in case_lines])
        for oy, col, L in banded_merge(events):
            t = norm(L['text'])
            x0, bold, sizes = L['x0'], L['bold'], L['sizes'] or [10]
            if col == 'C':
                if stopped or cur_topic is None:
                    continue
                if bold and t in GEO_COL_HEADERS:
                    continue
                cur_stmt = {'letter': None, 'text': t, 'sub_items': [],
                            'page': pno, 'oy': round(L['oy'], 1),
                            'topic': dict(cur_topic),
                            'key': dict(cur_key) if cur_key else None}
                added.append(cur_stmt)
                continue
            if col == 'L':
                if bold and max(sizes) >= 13 and x0 < 130 \
                        and GEO_STOP_HEADERS.match(t):
                    cur_topic = None
                    stopped = True
                    continue
                if bold and 12 <= max(sizes) < 13 and x0 < 70:
                    m = TOPIC_RE.match(t)
                    if m:
                        cur_topic = {'number': m.group(1),
                                     'title': m.group(2).strip(),
                                     'page': pno, 'oy': round(L['oy'])}
                        cur_key = cur_stmt = None
                        stopped = False
                        continue
                if stopped or cur_topic is None:
                    continue
                if bold and t in GEO_COL_HEADERS:
                    if t == 'Integrated skills':
                        stopped = True
                    continue
                if bold and max(sizes) >= 13:
                    continue
                if in_case_band(L['oy']) or re.match(r'^\(\d+\)', t):
                    continue        # handled by the full-width event / furniture
                m = re.match(r'^(\d{1,2}\.\d{1,2})(?:\s+(.*))?$', t) if x0 < 75 else None
                if m:
                    cur_key = {'code': m.group(1), 'title': (m.group(2) or '').strip(),
                               'page': pno, 'oy': round(L['oy'], 1)}
                    cur_stmt = None
                    continue
                # case-study continuation (full-width line wraps)
                if cur_stmt is not None and cur_stmt['letter'] is None and x0 < 80 \
                        and not bold:
                    cur_stmt['text'] = clean_punct(cur_stmt['text'] + ' ' + t)
                    continue
                # key-idea title continuation
                if cur_key is not None and 85 <= x0 < 205 and not bold:
                    cur_key['title'] = norm(cur_key['title'] + ' ' + t)
                continue
            # ---- right column ----
            if stopped or cur_topic is None:
                continue
            if bold or in_case_band(L['oy']):
                continue
            m = re.match(r'^([a-z])\)\s*(.*)$', t) if x0 < 236 else None
            if m:
                cur_stmt = {'letter': m.group(1), 'text': m.group(2).strip(),
                            'sub_items': [], 'page': pno,
                            'oy': round(L['oy'], 1),
                            'topic': dict(cur_topic),
                            'key': dict(cur_key) if cur_key else None}
                added.append(cur_stmt)
                continue
            if cur_stmt is not None and cur_stmt['letter'] is not None:
                cur_stmt['text'] = clean_punct(cur_stmt['text'] + ' ' + t)
    doc.close()

    # sanity + id assignment
    by_topic = {}
    for st in added:
        by_topic.setdefault(st['topic']['number'], []).append(st)
    if sorted(by_topic) != [str(i) for i in range(1, 10)]:
        raise SystemExit(f'FAIL: geography topics covered: {sorted(by_topic)}')
    for num, sts in sorted(by_topic.items()):
        if len(sts) < 8:
            raise SystemExit(f'FAIL: geography topic {num} only {len(sts)} statements')

    for st in added:
        if st['key'] and st['key']['title']:
            sk = (st['key']['code'], st['key']['title'], st['key']['page'])
            if sk not in seen_sub:
                seen_sub.add(sk)
                sub_rows.append({'code': st['key']['code'],
                                 'title': st['key']['title'],
                                 'page': st['key']['page'],
                                 'oy': st['key']['oy']})
    new_rows = []
    for st in added:
        counter += 1
        tnum = st['topic']['number']
        trow = topic_rows.get(tnum) or {
            'number': tnum, 'title': st['topic']['title'],
            'page': st['topic']['page'], 'oy': st['topic']['oy']}
        topic_dict = {'number': trow['number'], 'title': trow['title'],
                      'page': trow['page'], 'oy': trow.get('oy')}
        sub_dict = None
        if st['key'] and st['key']['title']:
            sub_dict = {'code': st['key']['code'], 'title': st['key']['title'],
                        'page': st['key']['page'], 'oy': st['key']['oy']}
        flags = [FLAG] + (['statement-letter: ' + st['letter']] if st['letter'] else [])
        new_rows.append({
            'official_code': None,
            'text': st['text'],
            'page': st['page'], 'oy': st['oy'],
            'topic': topic_dict, 'subsection': sub_dict,
            'sub_items': [], 'practical': False, 'flags': flags,
            'id': synth_id(qual_prefix, tnum, counter),
        })

    have_ids = {r['id'] for r in rows}
    for nr in new_rows:
        if nr['id'] in have_ids:
            raise SystemExit(f'FAIL: id collision {nr["id"]}')
    v1['spec_points'] = rows + new_rows
    v1['subsections'] = v1['subsections'] + sub_rows
    v1['counts']['spec_points'] = len(v1['spec_points'])
    save_v1(qual, stem, v1)
    REPORT['igcse_geography']['added'] = [
        {'id': r['id'], 'text': r['text'], 'page': r['page'], 'oy': r['oy'],
         'topic': r['topic']['number'],
         'subsection': (r['subsection'] or {}).get('code')} for r in new_rows]
    REPORT['igcse_geography']['subsections_added'] = len(sub_rows)
    print(f'geography: +{len(new_rows)} statements, +{len(sub_rows)} key-idea '
          f'subsections (counter {max_synth_counter(rows)} -> {counter})')


# --------------------------------------------------- accounting repair -------

ACCT_STEM = 'ig-accountancy-spec'
ACCT_PAGES = range(19, 31)


def repair_accounting():
    qual, stem = 'igcse-accounting', ACCT_STEM
    v1 = load_v1(qual, stem)
    rows = v1['spec_points']
    counter = max_synth_counter(rows)
    if counter != 118:
        raise SystemExit(f'FAIL: accounting counter expected 118, got {counter}')
    qual_prefix = 'IGCSE_ACCOUNTING'
    real_topics = {}
    for t in v1['topics']:
        if t['page'] in (19, 21, 23, 27, 29) and t.get('oy') == 85:
            real_topics[t['number']] = t

    doc = pymupdf.open(SPEC / qual / f'{stem}.pdf')
    kill = strip_running_text(doc)
    cur_topic = cur_sub = cur_stmt = None
    in_walk = False
    added, sub_rows = [], []
    seen_sub = set()
    for pno in ACCT_PAGES:
        left, right = column_lines(doc, kill, pno, x_split=185)
        events = ([(L['oy'], 'L', L) for L in left]
                  + [(L['oy'], 'R', L) for L in right])
        for oy, col, L in banded_merge(events):
            t = norm(L['text'])
            x0, bold, sizes = L['x0'], L['bold'], L['sizes'] or [10]
            if col == 'L':
                if bold and max(sizes) >= 16 and x0 < 70:
                    m = TOPIC_RE.match(t)
                    if m:
                        cur_topic = {'number': m.group(1),
                                     'title': m.group(2).strip(),
                                     'page': pno, 'oy': round(L['oy'])}
                        cur_sub = cur_stmt = None
                        in_walk = True
                        continue
                if not in_walk or cur_topic is None:
                    continue
                m = re.match(r'^(\d{1,2})(?:\s+(.*))?$', t) if x0 < 75 and bold else None
                if m:
                    cur_sub = {'code': m.group(1), 'title': (m.group(2) or '').strip(),
                               'page': pno, 'oy': round(L['oy'], 1)}
                    cur_stmt = None
                    continue
                if cur_sub is not None and 74 <= x0 < 185 and bold and cur_stmt is None:
                    cur_sub['title'] = norm(cur_sub['title'] + ' ' + t)
                continue
            # ---- right column ----
            if not in_walk or cur_topic is None:
                continue
            m = re.match(r'^([a-z])\)\s*(.*)$', t) if x0 < 212 else None
            if m:
                cur_stmt = {'letter': m.group(1), 'text': m.group(2).strip(),
                            'sub_items': [], 'page': pno,
                            'oy': round(L['oy'], 1),
                            'topic': dict(cur_topic),
                            'sub': dict(cur_sub) if cur_sub else None,
                            'in_bullets': False}
                added.append(cur_stmt)
                continue
            if cur_stmt is None:
                continue
            if t.startswith('\u2022'):
                cur_stmt['sub_items'].append(clean_punct(t.lstrip('\u2022 ').strip()))
                cur_stmt['in_bullets'] = True
                continue
            if cur_stmt['in_bullets'] and x0 >= 225:
                if cur_stmt['sub_items']:
                    cur_stmt['sub_items'][-1] = clean_punct(
                        cur_stmt['sub_items'][-1] + ' ' + t)
                continue
            if not cur_stmt['in_bullets']:
                cur_stmt['text'] = clean_punct(cur_stmt['text'] + ' ' + t)
    doc.close()

    by_topic = {}
    for st in added:
        by_topic.setdefault(st['topic']['number'], []).append(st)
    if sorted(by_topic) != ['1', '2', '3', '4', '5']:
        raise SystemExit(f'FAIL: accounting topics covered: {sorted(by_topic)}')
    for num, sts in sorted(by_topic.items()):
        if len(sts) < 6:
            raise SystemExit(f'FAIL: accounting topic {num} only {len(sts)} statements')

    for st in added:
        if st['sub'] and st['sub']['title']:
            sk = (st['topic']['number'], st['sub']['code'], st['sub']['title'],
                  st['sub']['page'])
            if sk not in seen_sub:
                seen_sub.add(sk)
                sub_rows.append({'code': st['sub']['code'],
                                 'title': st['sub']['title'],
                                 'page': st['sub']['page'],
                                 'oy': st['sub']['oy']})
    new_rows = []
    for st in added:
        counter += 1
        tnum = st['topic']['number']
        trow = real_topics.get(tnum) or st['topic']
        topic_dict = {'number': trow['number'], 'title': trow['title'],
                      'page': trow['page'], 'oy': trow.get('oy')}
        sub_dict = None
        if st['sub'] and st['sub']['title']:
            sub_dict = {'code': st['sub']['code'], 'title': st['sub']['title'],
                        'page': st['sub']['page'], 'oy': st['sub']['oy']}
        new_rows.append({
            'official_code': None,
            'text': st['text'],
            'page': st['page'], 'oy': st['oy'],
            'topic': topic_dict, 'subsection': sub_dict,
            'sub_items': st['sub_items'], 'practical': False,
            'flags': [FLAG, 'statement-letter: ' + st['letter']],
            'id': synth_id(qual_prefix, tnum, counter),
        })

    have_ids = {r['id'] for r in rows}
    for nr in new_rows:
        if nr['id'] in have_ids:
            raise SystemExit(f'FAIL: id collision {nr["id"]}')
    v1['spec_points'] = rows + new_rows
    v1['subsections'] = v1['subsections'] + sub_rows
    v1['counts']['spec_points'] = len(v1['spec_points'])
    save_v1(qual, stem, v1)
    REPORT['igcse_accounting']['added'] = [
        {'id': r['id'], 'text': r['text'], 'page': r['page'], 'oy': r['oy'],
         'topic': r['topic']['number'],
         'subsection': (r['subsection'] or {}).get('code'),
         'sub_items': len(r['sub_items'])} for r in new_rows]
    REPORT['igcse_accounting']['subsections_added'] = len(sub_rows)
    print(f'accounting: +{len(new_rows)} statements, +{len(sub_rows)} '
          f'subsections (counter 118 -> {counter})')


def main():
    repair_ial_maths()
    repair_geography()
    repair_accounting()
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / 'T_SPEC_8_PARSE_REPAIR.json').write_text(
        json.dumps(REPORT, indent=1, ensure_ascii=False) + '\n')
    print('report -> graph/reports/T_SPEC_8_PARSE_REPAIR.json')


if __name__ == '__main__':
    main()
