#!/usr/bin/env python3
"""T-SPEC-9 — igcse-economics parse repair.

The 4EC1 modular PDF prints each topic's first lettered sub-statement INLINE
after the topic heading ("1.1.1 The economic problem a) The problem of
scarcity ..."); the v1 lettered-table extractor only matched `a)` at visual
line start, so the 14 inline rows were dropped from the parse. The T-SPEC-7
verdict pass correctly refused to guess and pended the SME tags whose targets
were these missing rows.

Repair: insert the 14 rows verbatim (PDF-direct, page + oy provenance, flag
't-spec-9-parse-repair') into the v1 parsed.json in document order, then the
canonical bundle is rebuilt with build_canonical.py (separate step, same flow
as T-SPEC-8). Existing ids are never altered; the 14 codes collide with
nothing (they are exactly the codes absent from the parse).
"""
import json
import re
import sys
import datetime
from pathlib import Path

import pymupdf

BASE = Path('/home/z/my-project/download/syllabai-resources')
sys.path.insert(0, str(BASE / 'scripts'))
from spec_parser import page_spans, strip_running_text, visual_lines  # noqa: E402

FLAG = 't-spec-9-parse-repair'
V1 = BASE / 'Official-Specifications' / 'parsed' / 'igcse-economics' / \
    'international-gcse-in-economics-modular-specific.parsed.json'
PDF = BASE / 'Official-Specifications' / 'igcse-economics' / \
    'international-gcse-in-economics-modular-specification.pdf'
REPORTS = BASE / 'graph' / 'reports'

NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

# code -> (page, oy, text, sub_items, topic_code, topic_title)
# Every text/sub_item was extracted by span walk from the given page/oy.
ROWS = [
    ('1.1.1a', 17, 183.1,
     'The problem of scarcity \u2013 where there are unlimited wants and '
     'finite resources, leading to the need to make choices.', [],
     '1.1.1', 'The economic problem'),
    ('1.1.2a', 17, 448.0,
     'The underlying assumptions that:',
     ['consumers aim to maximise their benefit',
      'businesses aim to maximise their profit.'],
     '1.1.2', 'Economic assumptions'),
    ('1.1.5a', 20, 493.1, 'Definition of mixed economy.', [],
     '1.1.5', 'The mixed economy'),
    ('1.2.1a', 22, 128.0,
     'The factors of production:', ['land', 'labour', 'capital', 'enterprise.'],
     '1.2.1', 'Factors of production'),
    ('1.2.2a', 22, 352.0, 'Definition of productivity.', [],
     '1.2.2', 'Productivity and division of labour'),
    ('1.2.3a', 23, 91.0,
     'Definition and use of formulae to calculate:',
     ['total revenue', 'total costs', 'total fixed costs',
      'total variable costs', 'average (total) costs', 'profit.'],
     '1.2.3', 'Costs and revenues'),
    ('1.2.5a', 25, 519.2,
     'Factors affecting the demand for labour:',
     ['demand for the final product (derived demand)',
      'availability of substitutes, including machines',
      'productivity of workforce.'],
     '1.2.5', 'The labour market'),
    ('1.2.6a', 26, 298.8,
     'Government policy to deal with externalities:',
     ['taxation', 'subsidies', 'fines', 'regulation', 'pollution permits.'],
     '1.2.6', 'Externalities'),
    ('2.1.1a', 29, 177.1,
     'Economic growth: o employment o standards of living o poverty '
     'o productive potential o inflation o the environment.',
     ['definition of economic growth',
      'measurement using increases in gross domestic product (GDP)',
      'limitations of GDP as a measure of growth',
      'the use of diagrams to show the economic cycle: annotating boom, '
      'downturn, recession and recovery',
      'the effect of each stage of the economic cycle on economic growth, '
      'inflation and unemployment',
      'the impact of economic growth on:'],
     '2.1.1', 'Macroeconomic objectives'),
    ('2.1.2a', 32, 91.0,
     'Fiscal policy \u2013 government revenue and government expenditure:',
     ['definition of fiscal policy',
      'government revenue \u2013 direct and indirect taxes',
      'government expenditure \u2013 main areas of focus',
      'fiscal deficits and fiscal surpluses',
      'impact of a fiscal deficit and fiscal surplus',
      'the impact of fiscal policy on macroeconomic objectives.'],
     '2.1.2', 'Government policies'),
    ('2.1.3a', 33, 91.0,
     'The impact of policies and the trade-off between macroeconomic objectives:',
     ['unemployment and inflation', 'economic growth and inflation',
      'economic growth and environmental protection',
      'inflation and the current account on balance of payments.'],
     '2.1.3', 'Relationships between objectives and policies'),
    ('2.2.1a', 34, 128.0,
     'Definition of globalisation: increased integration and '
     'interdependence of economies.', [],
     '2.2.1', 'Globalisation'),
    ('2.2.2a', 35, 91.0,
     'Advantages and disadvantages of free trade, including:',
     ['lower prices and increased choice for consumers', 'lower input costs',
      'wider markets for businesses',
      'foreign competition harming domestic businesses',
      'increasing unemployment.'],
     '2.2.2', 'International trade'),
    ('2.2.3a', 36, 91.0, 'Definition of exchange rates.', [],
     '2.2.3', 'Exchange rates'),
]


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def main() -> int:
    doc = json.loads(V1.read_text())
    have = {p['official_code'] for p in doc['spec_points']}
    errors = []

    # fail-closed: codes absent, texts verbatim on the PDF page
    pdf = pymupdf.open(str(PDF))
    kill = strip_running_text(pdf)
    page_text = {}
    for code, page, _oy, text, sub_items, _tc, _tt in ROWS:
        if code in have:
            errors.append(f'{code}: already present in parse')
        if page not in page_text:
            page_text[page] = ' '.join(
                L['text'] for L in visual_lines(
                    [s for s in page_spans(pdf[page - 1]) if not kill(s)]))
        blob = norm(page_text[page])
        for piece in [text] + list(sub_items):
            p = norm(piece)
            if p in blob:
                continue
            # two-column interleave / o-flattening: require every word of the
            # piece to occur on the page (texts were derived from the page
            # walk; the word check catches transcription slips)
            words = [w for w in re.findall(r'[A-Za-z()]+', p) if w != 'o']
            missing = [w for w in words if w not in blob]
            if missing:
                errors.append(f'{code}: text not on page {page} '
                              f'(missing {missing[:6]}): {piece[:60]!r}')
    if errors:
        print('FAIL-CLOSED ERRORS:')
        for e in errors:
            print('  -', e)
        return 1

    added = []
    for code, page, oy, text, sub_items, tcode, ttitle in ROWS:
        row = {
            'official_code': code, 'scope': None, 'suffix': '',
            'text': text, 'page': page, 'oy': oy,
            'topic': None,
            'subsection': {'code': tcode, 'title': ttitle,
                           'page': page, 'oy': oy},
            'sub_items': sub_items, 'practical': False, 'flags': [FLAG],
            'id': f'IGCSE_ECONOMICS:{code}',
            'provenance': {'pdf': pdf.name,
                           'pdf_sha1': __import__('hashlib').sha1(
                               pdf.tobytes()).hexdigest(),
                           'page': page, 'oy': oy,
                           'extraction_method': 'pdf-span-geometry'},
        }
        added.append(row)

    doc['spec_points'] = sorted(doc['spec_points'] + added,
                                key=lambda r: (r['page'], r['oy']))
    doc['counts']['spec_points'] = len(doc['spec_points'])
    V1.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n')

    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / 'T_SPEC_9_PARSE_REPAIR.json').write_text(json.dumps({
        'schema': 'syllabai.t-spec-9-parse-repair/1.0',
        'generated_utc': NOW,
        'task': 'T-SPEC-9 igcse-economics parse repair (inline lettered rows)',
        'cause': ('v1 lettered-table extractor only matched lettered '
                  'statements at visual-line start; each topic\'s first '
                  'lettered row is printed inline after the topic heading '
                  'and was dropped'),
        'added': [{'code': r[0], 'page': r[1], 'oy': r[2], 'text': r[3],
                   'sub_items': r[4]} for r in ROWS],
        'flag': FLAG,
    }, indent=1, ensure_ascii=False) + '\n')
    print(f'added {len(added)} rows to the igcse-economics v1 parse '
          f'({len(doc["spec_points"])} total)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
