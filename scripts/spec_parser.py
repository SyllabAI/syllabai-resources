#!/usr/bin/env python3
"""SyllabAI official specification parser v1.0 — PDF-direct, deterministic.

Family strategies:
  code_column     IGCSE sciences (linear+modular), SDA, IAL sciences/maths
                  statement code (N.M[BCHP]?) in left column, text right/inline
  triplet_table   Business, ICT, Economics: N.M topic rows + N.M.K statements
  heading_bullets Geography, Accounting:
                  bold headings + bullet statements (synthesized IDs)
  further_maths   Further Pure Maths (4PM1): numbered sections (14pt bold
                  'N Title'), bold single-letter statements A-Z in left col
                  (x<316), Notes col (x>=316) excluded. Code = '<sec><letter>'.
  english_lit     English Lit (4ET1): 'Component N:' topics, strand points
                  (Section/Assignment A-C), set-text rows (title + author),
                  skills bullets. No printed codes -> synthesized C<N> ids.
  maths_table     Maths A linear + modular: 3-column content tables
                  (left: AO/section/subsection codes+titles, mid: lettered
                  statements A-Z, right: Notes excluded). Linear = Foundation
                  walk (scope None) + Higher-additions walk (scope 'H');
                  modular = per-unit walks (scope U1F..U2H). Letters restart
                  per walk/subsection in Higher walks -> walk scope disambiguates.

Every statement carries page + span provenance. Flags list notation risks.
Output: Official-Specifications/parsed/<qual>/<pdf-stem>.parsed.json
        Official-Specifications/parsed/<qual>/parse_report.json
"""
import glob, hashlib, json, os, re, sys, datetime
import pymupdf

BASE = '/home/z/my-project/download/syllabai-resources/Official-Specifications'
OUT_BASE = f'{BASE}/parsed'
PARSER_VERSION = 'spec-parser-1.0'

CODE_ALONE = re.compile(r'^(\d{1,2}\.\d{1,2})([A-Z]{0,2})$')
CODE_START = re.compile(r'^(\d{1,2}\.\d{1,2})([A-Z]{0,2})\b\s*(.*)$')
TRIPLET_START = re.compile(r'^(\d{1,2}\.\d{1,2}\.\d{1,2})\b\s*(.*)$')
TRIPLET_ALONE = re.compile(r'^(\d{1,2}\.\d{1,2}\.\d{1,2})$')
SEC_NUM = re.compile(r'^(\d{1,2})\.\s+([A-Z].+)$')
SUBSEC = re.compile(r'^\(([a-z])\)\s+(.+)$')
TOPIC_HDR = re.compile(r'^(Topic|UNIT)\s+(\d+)\s*[:\-\u2013]?\s*(.*)$', re.I)
ROMAN = re.compile(r'^(i{1,3}|iv|v|vi{0,3}|ix|x)$')
PRACTICAL_RE = re.compile(r'\bpractical\s*:', re.I)

FAMILY = {
    'igcse-chemistry': 'code_column', 'igcse-biology': 'code_column',
    'igcse-physics': 'code_column', 'igcse-science-double-award': 'code_column',
    'igcse-chemistry-modular': 'code_column', 'igcse-biology-modular': 'code_column',
    'igcse-physics-modular': 'code_column',
    'ial-biology': 'code_column', 'ial-chemistry': 'code_column',
    'ial-maths': 'code_column',
    'ial-physics': 'bare_int',
    'igcse-business': 'triplet_table', 'igcse-ict': 'triplet_table',
    'igcse-economics': 'lettered_table',
    'igcse-maths-a': 'maths_table', 'igcse-maths-a-modular': 'maths_table',
    'igcse-geography': 'heading_bullets', 'igcse-accounting': 'heading_bullets',
    'igcse-english-literature': 'english_lit', 'igcse-further-maths': 'further_maths',
    # T-SME-11 (2026-09-19): the three missing quals. SDA Modular reuses the
    # single-science code_column layout (plain N.M statements under topic
    # headers, per-science sections); Maths B (4MB1) uses the Further Pure
    # layout (numbered sections, lettered statements, Notes column);
    # English Language A (4EA1) is component/anthology/skills like English Lit.
    'igcse-science-double-award-modular': 'code_column',
    'igcse-maths-b': 'further_maths',
    'igcse-english-language-a': 'english_lang_a',
}
UNIT_HDR = re.compile(r'^([A-Z]{1,2}\d{1,2})\.\d+\s+Unit content')
SCI_HDR = re.compile(r'^(Biology|Chemistry|Physics)\s+content$', re.I)

# ------------------------------------------------------------------ spans ----

def page_spans(page):
    out = []
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for s in line['spans']:
                if s['text'].strip():
                    out.append({
                        'text': s['text'], 'x0': s['bbox'][0], 'x1': s['bbox'][2],
                        'y0': s['bbox'][1], 'y1': s['bbox'][3], 'oy': s['origin'][1],
                        'size': round(s['size'], 1), 'font': s['font'],
                    })
    return out

def strip_running_text(doc):
    """Spans whose text repeats on >40% of pages near top/bottom -> header/footer."""
    n = doc.page_count
    bands = {}
    for pno in range(n):
        for s in page_spans(doc[pno]):
            if s['y0'] < 55 or s['y0'] > 770:
                key = re.sub(r'\s+', ' ', s['text']).strip()[:60]
                bands.setdefault(key, set()).add(pno)
    kill = {k for k, ps in bands.items() if len(ps) > max(4, 0.4 * n)}
    # page-number-only spans also killed by position later
    def is_killed(s):
        key = re.sub(r'\s+', ' ', s['text']).strip()[:60]
        if key in kill:
            return True
        if re.fullmatch(r'\d{1,3}', s['text'].strip()) and (s['y0'] > 770 or s['y0'] < 55):
            return True
        return s['y0'] < 30 or s['y0'] > 820
    return is_killed

def visual_lines(spans, tol=3.5):
    """Group spans into visual lines by origin-y, sort by x.
    tol=7 catches sub/superscript satellites (dH, Rf, dm3) whose baselines
    sit a few pt off; body lines are 12+pt apart so no false merges."""
    lines = []
    for s in sorted(spans, key=lambda s: (s['oy'], s['x0'])):
        for L in lines:
            if abs(L['oy'] - s['oy']) < tol:
                L['spans'].append(s)
                break
        else:
            lines.append({'oy': s['oy'], 'spans': [s]})
    for L in lines:
        L['spans'].sort(key=lambda s: s['x0'])
        # gap-aware join: insert a space ONLY where the print shows one
        # (x-gap >= 25% of the glyph size). The previous unconditional
        # ' '.join fabricated spaces inside tight multi-span constructs —
        # '(Ar)' parsed as '( A r )', '(propan-1-ol only)' as
        # '( propan-1-ol only )' — 501 estate-wide artifacts (T-C24).
        parts = []
        prev = None
        for s in L['spans']:
            t = s['text'].strip()
            if not t:
                continue
            if prev is not None:
                gap = s['x0'] - prev['x1']
                if gap >= 0.25 * max(prev['size'], s['size']):
                    parts.append(' ')
            parts.append(t)
            prev = s
        L['text'] = re.sub(r'\s+', ' ', ''.join(parts)).strip()
        L['text'] = re.sub(r'\s+', ' ', L['text']).strip()
        L['x0'] = min(s['x0'] for s in L['spans'])
        L['bold'] = all('Bold' in s['font'] for s in L['spans'] if s['text'].strip())
        L['sizes'] = [s['size'] for s in L['spans']]
    lines.sort(key=lambda L: L['oy'])
    return lines

# ------------------------------------------------------------- statements ----

def is_noise(line):
    t = line['text']
    if not t or len(t) < 2:
        return True
    if t in ('Subject content', 'What learners need to study', 'Students should:',
             'Students will be assessed on their ability to:',
             'Students should be taught to:'):
        return True
    return False

def parse_code_column(doc, kill):
    """Left-column code (N.M / N.M.B) statements: IGCSE/IAL sciences, IAL maths."""
    statements, topics, subsecs = [], [], []
    cur_topic, cur_subsec = None, None
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        for L in visual_lines(spans):
            t = L['text']
            m_topic = TOPIC_HDR.match(t)
            m_sub = SUBSEC.match(t)
            m_sec = SEC_NUM.match(t)
            m_code = CODE_START.match(t)
            if m_topic:
                cur_topic = {'number': m_topic.group(2), 'title': (m_topic.group(3) or '').strip(),
                             'page': pno + 1, 'source_page_oy': round(L['oy'])}
                topics.append(cur_topic)
                cur_subsec = None
                continue
            if m_sub and L['bold']:
                cur_subsec = {'letter': m_sub.group(1), 'title': m_sub.group(2).strip(),
                              'page': pno + 1, 'source_page_oy': round(L['oy'])}
                subsecs.append(cur_subsec)
                continue
            if m_sec and L['bold'] and not m_code:
                cur_topic = {'number': m_sec.group(1), 'title': m_sec.group(2).strip(),
                             'page': pno + 1, 'source_page_oy': round(L['oy'])}
                topics.append(cur_topic)
                continue
            if not m_code:
                continue
            code, suffix, rest = m_code.group(1), m_code.group(2) or '', m_code.group(3)
            # absorb continuation lines
            parts = [rest] if rest else []
            if not rest:
                # statement text lives in same y-band to the right (separate line
                # entry would have merged by oy; a standalone code line means the
                # text follows on subsequent lines)
                pass
            statements.append({
                'official_code': code + suffix, 'code_num': code, 'suffix': suffix,
                'text': '', 'page': pno + 1, 'oy': round(L['oy'], 1),
                'topic': dict(cur_topic) if cur_topic else None,
                'subsection': dict(cur_subsec) if cur_subsec else None,
                'sub_items': [], '_parts': parts,
            })
        # attach same-band right-side text for standalone codes: handled below
    return merge_continuations(statements, doc, kill)

def parse_code_column_bands(doc, kill):
    """v3 of code_column: row-band assembly per page, scope-aware.
    Scope = unit code (IAL maths 'M1') or science part (SDA 'Biology')."""
    statements, topics, subsecs = [], [], []
    cur_topic = cur_subsec = None
    scope = None
    cur = None          # open row carries across page boundaries
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        lines = visual_lines(spans, tol=7.0)   # science: catch sub/sup satellites
        rows = []
        for L in lines:
            t = L['text']
            m_topic = TOPIC_HDR.match(t)
            m_sub = SUBSEC.match(t)
            m_sec = SEC_NUM.match(t)
            m_unit = UNIT_HDR.match(t)
            m_sci = (L['bold'] and max(L['sizes']) >= 13 and SCI_HDR.match(t))
            if m_unit:
                scope = m_unit.group(1)
            if m_sci:
                scope = m_sci.group(1)
                cur_topic = {'number': scope, 'title': scope,
                             'page': pno + 1, 'oy': round(L['oy'])}
                topics.append(cur_topic)
                cur_subsec = None
                cur = None
                continue
            m_bigsec = None
            if L['bold'] and max(L['sizes']) >= 13:
                cand = re.match(r'^(\d{1,2})\s+([A-Z].+)$', t)
                # reject trailing page-number-like lines, but keep real titles
                # ending in a number (e.g. modular '…: Part 1' headers — the
                # old guard dropped all 13 of them; T-C24)
                if cand and (not re.search(r'\s\d{1,3}$', t)
                             or len(re.findall(r'[A-Za-z]{3,}', t)) >= 3):
                    m_bigsec = cand
            m_code = CODE_START.match(t)
            if m_topic or m_bigsec or (m_sec and L['bold'] and not m_code):
                if m_topic:
                    cur_topic = {'number': m_topic.group(2),
                                 'title': (m_topic.group(3) or '').strip()}
                elif m_bigsec:
                    cur_topic = {'number': m_bigsec.group(1), 'title': m_bigsec.group(2).strip()}
                else:
                    cur_topic = {'number': m_sec.group(1), 'title': m_sec.group(2).strip()}
                cur_topic.update({'page': pno + 1, 'oy': round(L['oy'])})
                topics.append(cur_topic)
                cur_subsec = None
                cur = None
                continue
            if m_sub and L['bold']:
                cur_subsec = {'letter': m_sub.group(1), 'title': m_sub.group(2).strip(),
                              'page': pno + 1, 'oy': round(L['oy'])}
                subsecs.append(cur_subsec)
                cur = None
                continue
            if m_code:
                code, suffix, rest = m_code.groups()
                cur = {'code': code, 'suffix': suffix or '', 'page': pno + 1,
                       'oy': round(L['oy'], 1), 'parts': [rest] if rest else [],
                       'bullets': [], 'pending_bullet': None, 'scope': scope,
                       '_tail': 'parts',
                       # snapshot header context AT CAPTURE — the finalizer
                       # previously reused the page-final cur_topic/cur_subsec
                       # for every statement on the page (T-C24: 488 statements
                       # across the bands family attached to a header that
                       # prints BELOW them)
                       'topic_ref': dict(cur_topic) if cur_topic else None,
                       'subsec_ref': dict(cur_subsec) if cur_subsec else None}
                rows.append(cur)
                continue
            if cur is None:
                continue
            first = L['spans'][0]
            is_bullet = t.startswith('\u2022')
            if ROMAN.match(t) or is_bullet or (first['x0'] >= 92 and not CODE_START.match(t)):
                content = t.lstrip('\u2022').strip()
                if is_bullet and not content:
                    cur['pending_bullet'] = True
                    cur['_tail'] = 'pending'
                elif cur.get('pending_bullet'):
                    cur['bullets'].append(content)
                    cur['pending_bullet'] = None
                    cur['_tail'] = ('b', len(cur['bullets']) - 1)
                elif ROMAN.match(t):
                    cur['bullets'].append(t)
                    cur['_tail'] = ('b', len(cur['bullets']) - 1)
                elif is_bullet:
                    cur['bullets'].append(content)
                    cur['_tail'] = ('b', len(cur['bullets']) - 1)
                else:
                    tail = cur.get('_tail')
                    if tail and tail != 'pending' and tail[0] == 'b':
                        cur['bullets'][tail[1]] += ' ' + t
                    else:
                        cur['parts'].append(t)
        for r in rows:
            oc = r['code'] + r['suffix']
            statements.append({
                'official_code': oc, 'scope': r['scope'],
                'suffix': r['suffix'], 'text': ' '.join(r['parts']),
                'page': r['page'], 'oy': r['oy'],
                'topic': r.get('topic_ref'),
                'subsection': r.get('subsec_ref'),
                'sub_items': r['bullets'],
            })
    return dedupe_codes(statements), topics, subsecs


def parse_bare_int(doc, kill):
    """IAL physics: statements numbered by bare sequential integers (1..N)
    at the left margin, inside 'Candidates will be assessed' sections."""
    statements, topics, subsecs = [], [], []
    cur_topic = cur_subsec = None
    in_assessed = False
    cur = None          # carries across pages
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        for L in visual_lines(spans, tol=7.0):
            t = L['text']
            if re.match(r'^(Candidates|Students) will be assessed on their ability', t):
                in_assessed = True
                cur = None
                continue
            m_code = re.match(r'^(\d{1,2}\.\d{1,2})\s+([A-Z].+)$', t)
            first = L['spans'][0]
            m_int_m = re.fullmatch(r'(\d{1,3})', first['text'].strip())
            m_int = bool(m_int_m and 'Bold' in first['font'] and first['x0'] < 75)
            if m_code and L['bold']:
                cur_topic = {'number': m_code.group(1), 'title': m_code.group(2).strip(),
                             'page': pno + 1, 'oy': round(L['oy'])}
                topics.append(cur_topic)
                in_assessed = False
                cur = None
                continue
            if m_int and in_assessed:
                rest = L['text'][len(first['text']):].strip()
                cur = {'official_code': m_int_m.group(1), 'page': pno + 1,
                       'oy': round(L['oy'], 1), 'parts': [rest] if rest else [],
                       'bullets': [], 'pending_bullet': None, '_tail': 'parts',
                       # snapshot the header context AT CAPTURE (the finalizer
                       # previously reused the walk-final cur_topic for every
                       # statement — all ial-physics points claimed '6.5 Analysis')
                       'topic_ref': dict(cur_topic) if cur_topic else None,
                       'subsec_ref': dict(cur_subsec) if cur_subsec else None}
                statements.append(cur)
                continue
            if cur is None:
                continue
            first = L['spans'][0]
            is_bullet = t.startswith('\u2022')
            if ROMAN.match(t) or is_bullet or (first['x0'] >= 92 and not re.match(r'^\d', t)):
                content = t.lstrip('\u2022').strip()
                if is_bullet and not content:
                    cur['pending_bullet'] = True
                    cur['_tail'] = 'pending'
                elif cur.get('pending_bullet'):
                    cur['bullets'].append(content)
                    cur['pending_bullet'] = None
                    cur['_tail'] = ('b', len(cur['bullets']) - 1)
                elif ROMAN.match(t):
                    cur['bullets'].append(t)
                    cur['_tail'] = ('b', len(cur['bullets']) - 1)
                elif is_bullet:
                    cur['bullets'].append(content)
                    cur['_tail'] = ('b', len(cur['bullets']) - 1)
                else:
                    tail = cur.get('_tail')
                    if tail and tail != 'pending' and tail[0] == 'b':
                        cur['bullets'][tail[1]] += ' ' + t
                    else:
                        cur['parts'].append(t)
    out = []
    for s in statements:
        out.append({
            'official_code': s['official_code'], 'scope': None, 'suffix': '',
            'text': ' '.join(s['parts']), 'page': s['page'], 'oy': s['oy'],
            'topic': s.get('topic_ref'),
            'subsection': s.get('subsec_ref'),
            'sub_items': s['bullets'],
        })
    return out, topics, subsecs


def parse_lettered_table(doc, kill):
    """Economics: N.M.K topic rows + lettered statements (a) b) ...) with
    bullets, in a three-column table layout."""
    statements, topics, subsecs = [], [], []
    cur_topic = cur_subtopic = None
    cur = None
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        for L in visual_lines(spans):
            t = L['text']
            first = L['spans'][0]
            m_t3 = TRIPLET_START.match(t) or TRIPLET_ALONE.match(t)
            m_let = re.match(r'^([a-z])\)\s*(.*)$', t)
            if m_t3 and first['x0'] < 90:
                cur_subtopic = {'code': m_t3.group(1),
                                'title': (m_t3.group(2) if m_t3.lastindex > 1 else '') or '',
                                'page': pno + 1, 'oy': round(L['oy'])}
                subsecs.append(cur_subtopic)
                cur = None
                continue
            m_t2 = re.match(r'^(\d{1,2}\.\d{1,2})$', t)
            if m_t2 and first['x0'] < 90:
                cur_topic = {'number': m_t2.group(1), 'title': '',
                             'page': pno + 1, 'oy': round(L['oy'])}
                topics.append(cur_topic)
                cur = None
                continue
            if m_let and first['x0'] > 180:
                cur = {'official_code': f"{cur_subtopic['code']}{m_let.group(1)}" if cur_subtopic else m_let.group(1),
                       'page': pno + 1, 'oy': round(L['oy'], 1),
                       'parts': [m_let.group(2)] if m_let.group(2) else [],
                       'bullets': [], 'pending_bullet': None,
                       # snapshot at capture (T-C24: whole-document-final bug —
                       # 94/108 economics statements claimed the doc's LAST
                       # subtopic header)
                       'topic_ref': dict(cur_topic) if cur_topic else None,
                       'subsec_ref': dict(cur_subtopic) if cur_subtopic else None}
                statements.append(cur)
                continue
            if cur is None:
                if cur_subtopic is not None and first['x0'] > 250:
                    cur_subtopic['title'] = (cur_subtopic['title'] + ' ' + t).strip()
                continue
            is_bullet = t.startswith('\u2022')
            if is_bullet or first['x0'] > 245:
                content = t.lstrip('\u2022').strip()
                if is_bullet and not content:
                    cur['pending_bullet'] = True
                elif cur.get('pending_bullet'):
                    cur['bullets'].append(content)
                    cur['pending_bullet'] = None
                elif is_bullet:
                    cur['bullets'].append(content)
                else:
                    cur['parts'].append(t)
    out = []
    for s in statements:
        out.append({
            'official_code': s['official_code'], 'scope': None, 'suffix': '',
            'text': ' '.join(s['parts']), 'page': s['page'], 'oy': s['oy'],
            'topic': s.get('topic_ref'),
            'subsection': s.get('subsec_ref'),
            'sub_items': s['bullets'],
        })
    return dedupe_codes(out), topics, subsecs

def dedupe_codes(statements):
    """Dedupe by (scope, code): same numeric code repeats across units/sciences."""
    seen, out = {}, []
    for st in statements:
        k = (st.get('scope'), st['official_code'])
        if k in seen:
            old = seen[k]
            if len(st['text']) > len(old['text']):
                out[out.index(old)] = st
                seen[k] = st
            continue
        seen[k] = st
        out.append(st)
    return out

def merge_continuations(statements, doc, kill):
    """Join wrapped continuation text across rows for standalone codes (v1)."""
    return statements

def parse_triplet_table(doc, kill):
    """Business/ICT: three-column table. Span-band walk: N.M (bold, left) =
    topic row; N.M.K (x>200) = statement start; bullets attach."""
    statements, topics, subsecs = [], [], []
    cur_topic = cur_subsec = None
    cur = None
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        bands = {}
        for s in spans:
            for oy in bands:
                if abs(oy - s['oy']) < 4:
                    bands[oy].append(s)
                    break
            else:
                bands[s['oy']] = [s]
        for oy in sorted(bands):
            ss = sorted(bands[oy], key=lambda s: s['x0'])
            s0 = ss[0]
            t0 = s0['text'].strip()
            m_topic = re.fullmatch(r'(\d{1,2}\.\d{1,2})', t0)
            m_stmt = re.fullmatch(r'(\d{1,2}\.\d{1,2}\.\d{1,2})', t0)
            if m_topic and s0['x0'] < 90:
                stmt_span = next((s for s in ss
                                  if re.fullmatch(r'\d{1,2}\.\d{1,2}\.\d{1,2}', s['text'].strip())
                                  and s['x0'] > 150), None)
                title = ' '.join(s['text'].strip() for s in ss[1:]
                                 if s is not stmt_span and s['x0'] < 215
                                 and not re.fullmatch(r'\d{1,2}\.\d{1,2}\.\d{1,2}', s['text'].strip())
                                 and not re.fullmatch(r'\d{1,3}', s['text'].strip()))
                cur_topic = {'number': m_topic.group(1), 'title': title.strip(),
                             'page': pno + 1, 'oy': round(oy)}
                if cur_topic['title']:
                    topics.append(cur_topic)
                if stmt_span is not None:
                    rest = ' '.join(s['text'].strip() for s in ss
                                    if s['x0'] > stmt_span['x1'] - 2).strip()
                    cur = {'official_code': stmt_span['text'].strip(),
                           'page': pno + 1, 'oy': round(oy, 1),
                           'parts': [rest] if rest else [],
                           'bullets': [], 'pending_bullet': None,
                           # snapshot at capture (T-C24: whole-document-final
                           # bug — 58 business / 135 ICT statements claimed a
                           # late-document topic header)
                           'topic_ref': dict(cur_topic) if cur_topic else None,
                           'subsec_ref': dict(cur_subsec) if cur_subsec else None}
                    statements.append(cur)
                    cur['_last_x'] = stmt_span['x1']
                else:
                    cur = None
                continue
            if m_stmt and s0['x0'] > 150:
                rest = ' '.join(s['text'].strip() for s in ss[1:]
                                if s['x0'] > s0['x1'] - 2).strip()
                cur = {'official_code': m_stmt.group(1), 'page': pno + 1,
                       'oy': round(oy, 1), 'parts': [rest] if rest else [],
                       'bullets': [], 'pending_bullet': None,
                       'topic_ref': dict(cur_topic) if cur_topic else None,
                       'subsec_ref': dict(cur_subsec) if cur_subsec else None}
                statements.append(cur)
                cur['_last_x'] = s0['x1']
                continue
            if cur is None:
                # title continuation for topic rows (wrapped titles at x 90-215)
                if cur_topic is not None and not cur_topic['title'] and s0['x0'] > 90:
                    pass
                continue
            # continuation content for current statement
            line_txt = ' '.join(s['text'].strip() for s in ss if s['x0'] > cur.get('_last_x', 210) - 2)
            line_txt = line_txt.strip()
            if not line_txt:
                continue
            is_bullet = line_txt.startswith('\u2022')
            content = line_txt.lstrip('\u2022').strip()
            if is_bullet and not content:
                cur['pending_bullet'] = True
            elif cur.get('pending_bullet'):
                cur['bullets'].append(content)
                cur['pending_bullet'] = None
            elif is_bullet:
                cur['bullets'].append(content)
            else:
                cur['parts'].append(line_txt)
    out = []
    for s in statements:
        out.append({
            'official_code': s['official_code'], 'scope': None, 'suffix': '',
            'text': ' '.join(s['parts']), 'page': s['page'],
            'oy': s['oy'], 'topic': s.get('topic_ref'),
            'subsection': s.get('subsec_ref'),
            'sub_items': s['bullets'],
        })
    return dedupe_codes(out), topics, subsecs

def parse_heading_bullets(doc, kill):
    """Bold headings (N.M or N. Title) + bullet statements underneath.
    IDs synthesized: <qual>-S<sec>.<idx> in document order."""
    items, topics, subsecs = [], [], []
    cur_topic = cur_subsec = None
    stmt_idx = 0
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        cur = None
        for L in visual_lines(spans):
            t = L['text']
            m_topic = TOPIC_HDR.match(t)
            m_sec = SEC_NUM.match(t)
            m_pair = CODE_START.match(t)
            if m_topic:
                cur_topic = {'number': m_topic.group(2), 'title': (m_topic.group(3) or '').strip(),
                             'page': pno + 1, 'oy': round(L['oy'])}
                topics.append(cur_topic)
                cur_subsec = None
                cur = None
                continue
            if m_sec and L['bold']:
                cur_topic = {'number': m_sec.group(1), 'title': m_sec.group(2).strip(),
                             'page': pno + 1, 'oy': round(L['oy'])}
                topics.append(cur_topic)
                cur_subsec = None
                cur = None
                continue
            if m_pair and L['bold']:
                cur_subsec = {'code': m_pair.group(1), 'title': (m_pair.group(3) or t).strip(),
                              'page': pno + 1, 'oy': round(L['oy'])}
                subsecs.append(cur_subsec)
                cur = None
                continue
            if t.startswith('\u2022'):
                stmt_idx += 1
                code = f"S{cur_topic['number']}.{stmt_idx:03d}" if cur_topic else f"SX.{stmt_idx:03d}"
                item = {'official_code': None, 'synth_id': code,
                        'text': t.lstrip('\u2022 ').strip(), 'page': pno + 1,
                        'oy': round(L['oy'], 1),
                        'topic': dict(cur_topic) if cur_topic else None,
                        'subsection': dict(cur_subsec) if cur_subsec else None,
                        'sub_items': []}
                items.append(item)
                cur = item
                continue
            if cur is not None:
                # continuation of wrapped bullet text (indented, no bullet)
                if L['x0'] > 100 and not CODE_START.match(t):
                    cur['text'] += ' ' + t
    return items, topics, subsecs

# --------------------------------------------------------- maths_table ------

MATHS_UNIT_HDR = re.compile(r'^Unit (\d+): (Foundation|Higher) Tier$')
MATHS_TIER_INTRO = re.compile(r'^(Foundation|Higher) Tier$')
MATHS_AO_HDR = re.compile(r'^AO(\d+)\s+([A-Z].+)$')
MATHS_SECTION = re.compile(r'^(\d{1,2})\s+([A-Z].+)$')
MATHS_SUBCODE = re.compile(r'^(\d{1,2}\.\d{1,2})$')
MATHS_LETTER = re.compile(r'^[A-Z]$')
MATHS_HTO = 'Higher Tier only'
MATHS_LEFT_MAX = 130      # left column: codes + titles
MATHS_MID_MAX = 400       # mid column: statement letters + text; right = Notes
MATHS_LETTER_X = (125, 215)

def _col_lines(spans, kill, x_min, x_max, tol=3.0):
    sel = [s for s in spans if not kill(s) and x_min <= s['x0'] < x_max]
    return visual_lines(sel, tol=tol)

def _maths_join(spans):
    """x-order join. Touching spans glue ONLY when fonts differ and the PDF
    encodes no boundary whitespace; explicit space chars in span texts win;
    operator boundaries always take a space."""
    out, prev_sp, prev_txt = '', None, ''
    for s in sorted(spans, key=lambda s: s['x0']):
        raw = s['text']
        t = raw.strip()
        if not t:
            continue
        glue = False
        if prev_sp is not None and s['x0'] <= prev_sp['x1'] + 0.3 \
                and prev_sp.get('font') != s.get('font') \
                and not prev_txt[-1:].isspace() and not raw[:1].isspace() \
                and prev_txt[-1:] not in '=+\u2212\u2013\u00d7/\u00f7\u00b1' \
                and t[:1] not in '=+\u2212\u2013\u00d7/\u00f7\u00b1':
            glue = True
        if glue:
            out += t
        else:
            out += (' ' if out else '') + t
        prev_sp, prev_txt = s, t
    return re.sub(r'\s+', ' ', out).strip()

def _maths_walk_pages(doc, kill, start, end_next):
    """Trim [start, end_next) to the last page carrying a bold N.M code or a
    statement letter line — drops trailing non-content pages inside range."""
    last = start - 1
    for pno in range(start, min(end_next, doc.page_count)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        hit = False
        for L in _col_lines(spans, kill, 0, MATHS_LEFT_MAX):
            if L['bold'] and (MATHS_SUBCODE.match(L['text']) or MATHS_SUBCODE.match(' '.join(L['text'].split()[:1]))):
                hit = True
        for L in _col_lines(spans, kill, MATHS_LETTER_X[0], MATHS_LETTER_X[1]):
            if L['spans'] and MATHS_LETTER.match(L['spans'][0]['text'].strip()) and L['spans'][0]['font'].endswith('Bold'):
                hit = True
        if hit:
            last = pno
    return last

def _maths_walks(doc, kill, modular):
    """Return [(scope, label, p_lo, p_hi)]. Linear: Foundation walk (scope
    None) from first AO page after the 'Foundation Tier' intro to the
    'Higher Tier' intro; Higher walk (scope 'H'). Modular: one walk per
    'Unit N: <Tier> Tier' header, scope U<N><F|H>."""
    walks = []
    if modular:
        starts = []
        for pno in range(doc.page_count):
            for L in _col_lines(page_spans(doc[pno]), kill, 0, MATHS_LEFT_MAX):
                m = MATHS_UNIT_HDR.match(L['text'])
                if m and L['bold'] and L['sizes'] and max(L['sizes']) > 14:
                    starts.append((pno, int(m.group(1)), m.group(2)))
        starts.sort()
        for i, (pno, no, tier) in enumerate(starts):
            nxt = starts[i + 1][0] if i + 1 < len(starts) else doc.page_count
            hi = _maths_walk_pages(doc, kill, pno, nxt)
            walks.append({'scope': f'U{no}{tier[0]}', 'label': f'Unit {no} {tier}',
                          'p_lo': pno, 'p_hi': hi})
    else:
        intros = []
        for pno in range(doc.page_count):
            for L in _col_lines(page_spans(doc[pno]), kill, 0, MATHS_LEFT_MAX):
                if L['bold'] and L['sizes'] and max(L['sizes']) > 13:
                    m = MATHS_TIER_INTRO.match(L['text'])
                    if m:
                        intros.append((pno, m.group(1)))
        intros.sort()
        if not intros:
            return walks
        first_content = None
        for pno in range(intros[0][0], doc.page_count):
            for L in _col_lines(page_spans(doc[pno]), kill, 0, MATHS_LEFT_MAX):
                if L['bold'] and MATHS_AO_HDR.match(L['text']) and L['sizes'] and max(L['sizes']) > 13:
                    first_content = pno
                    break
            if first_content is not None:
                break
        bounds = [p for p, _ in intros] + [doc.page_count]
        if first_content is not None:
            bounds[0] = first_content
        for i, (_, tier) in enumerate(intros):
            lo = bounds[i] if bounds[i] > (intros[i][0]) else intros[i][0]
            hi = _maths_walk_pages(doc, kill, lo, bounds[i + 1])
            if hi >= lo:
                walks.append({'scope': (None if i == 0 else 'H'), 'label': f'{tier} Tier walk',
                              'p_lo': lo, 'p_hi': hi})
    return walks

def _maths_frag_flags(text):
    """Math-dense statements assemble as span soup (sup/sub fragments, glued
    italics) — flag them so downstream treats wording as approximate."""
    if re.search(r'\b[A-Za-z] [A-Za-z] [A-Za-z]\b', text) or \
       re.search(r'\s\d(?:\s\d)+\s', ' ' + text + ' ') or \
       re.search(r'\(\s?[a-z]\s?\)', text) or \
       re.search(r'\s-1\b', text):
        return ['math-fragment-assembly']
    return []

def parse_maths_table(doc, kill):
    """IGCSE Maths A linear + modular content tables.
    Left col (x<130): AO headers, 'N Title' sections (12-14pt bold),
    'N.M' subsection codes with stacked bold titles, page furniture (ignored).
    Mid col (125<=x<400): bold single-letter statement rows + wrapped text;
    'Higher Tier only' markers. Right col (x>=400): Notes/examples, excluded.
    Cross-page statement continuation supported (columnar assembly)."""
    all_topics, all_subsecs, items = [], [], []
    seen = {}
    skipped_letters = 0
    walks = _maths_walks(doc, kill, modular=_has_unit_headers(doc, kill))
    for walk in walks:
        scope, label = walk['scope'], walk['label']
        cur_topic = cur_subsec = cur_stmt = None
        pending_hto = False
        for pno in range(walk['p_lo'], walk['p_hi'] + 1):
            page = doc[pno]
            spans = [s for s in page_spans(page) if not kill(s)]
            left = _col_lines(spans, kill, 0, MATHS_LEFT_MAX)
            mid = _col_lines(spans, kill, MATHS_LETTER_X[0], MATHS_MID_MAX)
            events = [(L['oy'], 0, 'L', L) for L in left] + [(L['oy'], 1, 'M', L) for L in mid]
            # half-point rounding: a statement letter printed 0.1pt above its
            # subsection code (same visual line) must not sort before it
            events.sort(key=lambda e: (round(e[0] * 2) / 2, e[1]))
            for oy, _, col, L in events:
                t = L['text']
                first = L['spans'][0]
                is_bold = first['font'].endswith('Bold')
                if col == 'L':
                    m_ao = MATHS_AO_HDR.match(t) if (is_bold and L['sizes'] and max(L['sizes']) > 13) else None
                    m_sec = MATHS_SECTION.match(t) if (is_bold and L['sizes'] and max(L['sizes']) > 11.5) else None
                    m_code = MATHS_SUBCODE.match(t.split('  ')[0].strip()) if is_bold else None
                    if m_ao:
                        cur_topic = {'number': f'AO{m_ao.group(1)}', 'title': m_ao.group(2).strip(),
                                     'page': pno + 1, 'oy': round(oy), 'scope': scope}
                        all_topics.append(cur_topic)
                        cur_subsec = None
                        cur_stmt = None
                    elif m_sec:
                        cur_topic = {'number': m_sec.group(1), 'title': m_sec.group(2).strip(),
                                     'page': pno + 1, 'oy': round(oy), 'scope': scope}
                        all_topics.append(cur_topic)
                        cur_subsec = None
                        cur_stmt = None
                    elif m_code:
                        code = m_code.group(1)
                        cur_subsec = {'code': code, 'title': '', 'page': pno + 1, 'oy': round(oy),
                                      'scope': scope, 'higher_only': pending_hto}
                        pending_hto = False
                        all_subsecs.append(cur_subsec)
                        cur_stmt = None
                    elif cur_subsec is not None and is_bold and not cur_subsec['title'] is None and \
                            not MATHS_LETTER.match(t) and t not in ('What learners need to study:',) and \
                            not t.startswith('Higher Tier only'):
                        # subsection title line(s), stacked under the code
                        if cur_stmt is None and L['bold']:
                            cur_subsec['title'] = (cur_subsec['title'] + ' ' + t).strip()
                    continue
                # mid column
                first_txt = first['text'].strip()
                if is_bold and MATHS_LETTER.match(first_txt) and MATHS_LETTER_X[0] <= first['x0'] < MATHS_LETTER_X[1]:
                    if cur_subsec is None:
                        skipped_letters += 1
                        print(f"    maths_table: letter line skipped p{pno + 1} y={oy:.0f} "
                              f"({first_txt}: {L['text'][:40]!r}) - no open subsection")
                        continue
                    text = _maths_join([s for s in L['spans'][1:] if s['x0'] > first['x0'] + 1])
                    cur_stmt = {'official_code': f"{cur_subsec['code']}{first_txt}",
                                'text': text, 'page': pno + 1, 'oy': round(oy, 1),
                                'topic': {k: cur_topic[k] for k in ('number', 'title', 'page', 'oy')} if cur_topic else None,
                                'subsection': {k: cur_subsec[k] for k in ('code', 'title', 'page', 'oy')},
                                'sub_items': [], 'scope': scope, 'walk': label}
                    items.append(cur_stmt)
                    continue
                if is_bold and t == MATHS_HTO:
                    if cur_subsec is not None and abs(cur_subsec['oy'] - round(oy)) <= 4:
                        cur_subsec['higher_only'] = True
                    else:
                        pending_hto = True
                    continue
                if cur_stmt is not None and not is_bold and t not in ('Notes',):
                    if is_noise(L):
                        continue
                    more = _maths_join(L['spans'])
                    if more:
                        cur_stmt['text'] = (cur_stmt['text'] + ' ' + more).strip()
        # dedupe within (scope, code): identical text -> first wins; else suffix
        deduped = []
        for st in items:
            if st.get('walk') != label:
                deduped.append(st)
                continue
            key = (st['scope'], st['official_code'])
            norm = re.sub(r'\s+', ' ', st['text']).strip().lower()
            if key in seen:
                if seen[key] == norm:
                    continue
                st['_dupn'] = 2 + sum(1 for d in deduped
                                      if (d['scope'], d['official_code']) == key and d.get('_dupn'))
                st['flags'] = ['duplicate-code-different-text']
            else:
                seen[key] = norm
            deduped.append(st)
        items = deduped
    if skipped_letters:
        print(f'    maths_table: {skipped_letters} letter lines skipped (no open subsection)')
    return items, all_topics, all_subsecs

def _has_unit_headers(doc, kill):
    for pno in range(doc.page_count):
        for L in _col_lines(page_spans(doc[pno]), kill, 0, MATHS_LEFT_MAX):
            if MATHS_UNIT_HDR.match(L['text']) and L['bold'] and L['sizes'] and max(L['sizes']) > 14:
                return True
    return False

# ----------------------------------------------------------- further_maths ---

FM_LEFT_MAX = 300        # content column; Notes column text starts x315.8
FM_SEC_MIN = 13.5        # section headers are 14pt bold

def parse_further_maths(doc, kill):
    """IGCSE Further Pure Maths (4PM1) content tables.
    Two-column layout: content (x<316) + Notes (x>=316, excluded).
    Section headers: 14pt bold 'N Title' lines. Statements: bold single
    letters A-Z at x62 with wrapped text below (10pt). official_code =
    '<section><letter>' (e.g. '1A') — the document's own hierarchy: the
    section number and the statement letter are both printed. Inline 12pt
    math spans assemble via _maths_join; sub/sup satellites sit ~4pt off
    baseline so some wording is span soup -> flagged, not guessed."""
    sec_first = last_page = None
    for pno in range(doc.page_count):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        lines = _col_lines(spans, kill, 0, FM_LEFT_MAX)
        has_tbl_hdr = any(L['text'] == 'What students need to learn' for L in lines)
        has_sec = any(L['bold'] and L['sizes'] and max(L['sizes']) > FM_SEC_MIN
                      and MATHS_SECTION.match(L['text']) for L in lines)
        if has_tbl_hdr and has_sec and sec_first is None:
            sec_first = pno
        for L in lines:
            f0 = L['spans'][0]
            if f0['font'].endswith('Bold') and MATHS_LETTER.match(f0['text'].strip()) \
                    and f0['x0'] < 75 and f0['size'] < 12 and max(L['sizes']) < 12.5:
                last_page = pno
    if sec_first is None or last_page is None or last_page < sec_first:
        return [], [], []
    all_topics, items, orphans = [], [], []
    cur_topic = cur_stmt = None
    for pno in range(sec_first, last_page + 1):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        for L in _col_lines(spans, kill, 0, FM_LEFT_MAX):
            t = L['text']
            first = L['spans'][0]
            is_bold = first['font'].endswith('Bold')
            if is_bold and L['sizes'] and max(L['sizes']) > FM_SEC_MIN \
                    and MATHS_SECTION.match(t):
                m = MATHS_SECTION.match(t)
                cur_topic = {'number': m.group(1), 'title': m.group(2).strip(),
                             'page': pno + 1, 'oy': round(L['oy'])}
                all_topics.append(cur_topic)
                cur_stmt = None
                orphans = []
                continue
            if is_bold and MATHS_LETTER.match(first['text'].strip()) \
                    and first['x0'] < 75 and first['size'] < 12:
                if cur_topic is None:
                    continue
                body = _maths_join([s for s in L['spans'] if s['x0'] > first['x0'] + 1])
                adopted = [o for o in orphans if o['oy'] >= L['oy'] - 8]
                flags = []
                if adopted:
                    body = (body + ' ' + ' '.join(o['text'] for o in adopted)).strip()
                    flags.append('floating-formula-adopted')
                orphans = []
                cur_stmt = {'official_code': f"{cur_topic['number']}{first['text'].strip()}",
                            'text': body, 'page': pno + 1, 'oy': round(L['oy'], 1),
                            'topic': {k: cur_topic[k] for k in ('number', 'title', 'page', 'oy')},
                            'subsection': None, 'sub_items': [],
                            'flags': flags}
                items.append(cur_stmt)
                continue
            if not is_bold and t not in ('What students need to learn', 'Notes'):
                if is_noise(L):
                    continue
                if cur_stmt is not None and L['oy'] >= cur_stmt['oy'] - 1:
                    more = _maths_join(L['spans'])
                    if more:
                        cur_stmt['text'] = (cur_stmt['text'] + ' ' + more).strip()
                else:
                    orphans = [o for o in orphans if L['oy'] - o['oy'] < 12]
                    orphans.append(L)
    # global dedupe on official_code (identical text -> first wins)
    seen, out = {}, []
    for st in items:
        norm = re.sub(r'\s+', ' ', st['text']).strip().lower()
        key = st['official_code']
        if key in seen:
            if seen[key] == norm:
                continue
            st['_dupn'] = 2 + sum(1 for d in out if d['official_code'] == key and d.get('_dupn'))
            st['flags'] = sorted(set(st.get('flags', []) + ['duplicate-code-different-text']))
        else:
            seen[key] = norm
        out.append(st)
    return out, all_topics, []

# ------------------------------------------------------------ english_lit ----

EL_HDR = re.compile(r'^Component (\d+):\s*(.*)$')
EL_STRAND = re.compile(r'^(?:Section|Assignment) ([A-C])\s*[\u2013:：]\s*(.+)$')
EL_AUTHOR_X = (272, 310)   # author column x-offsets (280/282 printed)
ELA_AUTHOR_X = (368, 440)  # ELA (4EA1) author column (x374 printed)
EL_TITLE_MAX = 265
ELA_TITLE_MAX = 360

def parse_english_lit(doc, kill, author_x=EL_AUTHOR_X, title_max=EL_TITLE_MAX):
    """IGCSE English Literature (4ET1) / English Language A (4EA1) content pages.
    Region: the numbered 18pt-bold section header whose title ends with
    'content' ('4 English Literature content' / '3 English Language
    (Specification A) content') .. the next numbered header.
    Topics = 'Component N: Title' (16pt bold, title may wrap to a second bold
    line at x>130). Points:
      - strands: 'Section/Assignment X – ...' focus paragraphs
      - set texts: rows with title at x62 + author at x280 under bold
        group labels ('Part 3 of the ... Anthology', 'A choice of one
        text from Modern Prose', ...) -> '<title> (<author>)'
      - skills bullets: '•' rows under bold skill headings
    No printed statement codes: official_code stays null; ids synthesized
    C<N>A<letter> / C<N>T<k> / C<N>S<k>. The PDF repeats the set-text lists
    in '3 Set texts at a glance' — excluded (duplicate region)."""
    start = end = None
    for pno in range(doc.page_count):
        for L in _col_lines(page_spans(doc[pno]), kill, 0, 200):
            if L['bold'] and L['sizes'] and max(L['sizes']) > 17 \
                    and re.match(r'^\d+ ', L['text']):
                if start is None:
                    if re.match(r'^\d+ .*\bcontent$', L['text'], re.I):
                        start = pno
                elif end is None:
                    end = pno
                    break
        if end is not None:
            break
    if start is None:
        return [], [], []
    if end is None:
        end = doc.page_count - 1
    all_topics, all_subsecs, items = [], [], []
    cur_topic = cur_subsec = cur_stmt = None
    ctr = {'A': 0, 'T': 0, 'S': 0}
    in_admin = False

    def author_present(L):
        return any(author_x[0] <= s['x0'] < author_x[1] and len(s['text'].strip()) > 2
                   for s in L['spans'])

    for pno in range(start, end):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        lines = _col_lines(spans, kill, 0, 380)
        i = 0
        while i < len(lines):
            L = lines[i]
            t = L['text']
            first = L['spans'][0]
            is_bold = L['bold']
            big = L['sizes'] and max(L['sizes']) >= 15
            if big and is_bold and EL_HDR.match(t) and first['x0'] < 100:
                m = EL_HDR.match(t)
                title = m.group(2).strip()
                j = i + 1
                while j < len(lines):
                    N = lines[j]
                    if N['bold'] and N['sizes'] and max(N['sizes']) >= 15 \
                            and N['spans'][0]['x0'] > 130 and N['oy'] - lines[j - 1]['oy'] < 40:
                        title = (title + ' ' + N['text']).strip()
                        j += 1
                    else:
                        break
                i = j
                cur_topic = {'number': m.group(1), 'title': title,
                             'page': pno + 1, 'oy': round(L['oy'])}
                all_topics.append(cur_topic)
                cur_subsec = cur_stmt = None
                in_admin = False
                ctr = {'A': 0, 'T': 0, 'S': 0}
                continue
            if in_admin:
                i += 1
                continue
            # assessment/admin sub-block: skip until next component header
            if is_bold and (t.startswith('Assessment overview')
                            or t in ('Assignment setting', 'Assignment taking',
                                     'Assignment marking', 'Setting the question',
                                     'Assessment of coursework', 'Authenticity',
                                     'Collaboration', 'Teacher feedback',
                                     'Presentation of the work', 'Word count',
                                     'Assessment criteria')):
                in_admin = True
                i += 1
                continue
            if is_bold and t.rstrip('.').lower().endswith('content') and first['x0'] < 100:
                i += 1
                continue
            if is_bold and first['x0'] < 100 and cur_topic is not None:
                # group label (set texts follow) vs skills heading (bullets follow)
                # wrapped heading rows (bold, x<100, <16pt below) extend the title
                prev = lines[i - 1] if i > 0 else None
                if prev is not None and prev['bold'] and cur_subsec is not None \
                        and cur_subsec.get('page') == pno + 1 \
                        and L['oy'] - prev['oy'] < 16 \
                        and prev['spans'][0]['x0'] < 100:
                    cur_subsec['title'] = (cur_subsec['title'] + ' ' + t).strip()
                    i += 1
                    continue
                nxt = lines[i + 1] if i + 1 < len(lines) else None
                sub_k = sum(1 for s in all_subsecs if s['code'].startswith(f'C{cur_topic["number"]}.')) + 1
                cur_subsec = {'code': f'C{cur_topic["number"]}.{sub_k}',
                              'title': t, 'page': pno + 1, 'oy': round(L['oy'])}
                all_subsecs.append(cur_subsec)
                cur_stmt = None
                i += 1
                continue
            m_str = EL_STRAND.match(t) if not is_bold else None
            if m_str and first['x0'] < 100 and cur_topic is not None:
                parts = [t]
                j = i + 1
                while j < len(lines):
                    N = lines[j]
                    if N['bold'] or N['spans'][0]['x0'] > 100 or author_present(N) \
                            or EL_STRAND.match(N['text']):
                        break
                    parts.append(N['text'])
                    j += 1
                i = j
                ctr['A'] += 1
                cur_stmt = {'synth_id': f'C{cur_topic["number"]}A{m_str.group(1)}',
                            'official_code': None,
                            'text': re.sub(r'\s+', ' ', ' '.join(parts)).strip(),
                            'page': pno + 1, 'oy': round(L['oy'], 1),
                            'topic': {k: cur_topic[k] for k in ('number', 'title', 'page', 'oy')},
                            'subsection': None, 'sub_items': []}
                items.append(cur_stmt)
                continue
            if not is_bold and first['x0'] < 70 and author_present(L) and cur_topic is not None:
                tspans = [s for s in L['spans'] if s['x0'] < title_max]
                aspans = [s for s in L['spans'] if author_x[0] <= s['x0'] < author_x[1]]
                title = re.sub(r'\s+', ' ', ' '.join(s['text'].strip() for s in tspans)).strip()
                author = re.sub(r'\s+', ' ', ' '.join(s['text'].strip() for s in aspans)).strip()
                j = i + 1
                if j < len(lines):
                    N = lines[j]
                    if not N['bold'] and not author_present(N) \
                            and N['spans'][0]['x0'] < 100 and not N['text'].startswith('\u2022') \
                            and not EL_STRAND.match(N['text']) \
                            and N['oy'] - L['oy'] < 20 and len(N['text']) < 60 \
                            and (j + 1 >= len(lines) or lines[j + 1]['oy'] - N['oy'] > 13):
                        title = (title + ' ' + N['text']).strip()
                        j += 1
                i = j
                ctr['T'] += 1
                text = f'{title} ({author})' if author else title
                cur_stmt = {'synth_id': f'C{cur_topic["number"]}T{ctr["T"]:02d}',
                            'official_code': None, 'text': text,
                            'page': pno + 1, 'oy': round(L['oy'], 1),
                            'topic': {k: cur_topic[k] for k in ('number', 'title', 'page', 'oy')},
                            'subsection': dict(cur_subsec) if cur_subsec else None,
                            'sub_items': []}
                items.append(cur_stmt)
                continue
            if not is_bold and first['x0'] >= 70 and first['x0'] < 100 \
                    and cur_stmt is not None and not author_present(L) \
                    and not t.startswith('\u2022'):
                # bullet continuation (indented x80 rows)
                cur_stmt['text'] = (cur_stmt['text'] + ' ' + t).strip()
                i += 1
                continue
            if not is_bold and any(s['text'].strip() == '\u2022' for s in L['spans'] if s['x0'] < 100) \
                    and cur_topic is not None:
                bspan = [s for s in L['spans'] if s['x0'] < 100 and s['text'].strip() == '\u2022'][0]
                body = _maths_join([s for s in L['spans'] if s['x0'] > bspan['x0'] + 1])
                ctr['S'] += 1
                cur_stmt = {'synth_id': f'C{cur_topic["number"]}S{ctr["S"]:02d}',
                            'official_code': None, 'text': body,
                            'page': pno + 1, 'oy': round(L['oy'], 1),
                            'topic': {k: cur_topic[k] for k in ('number', 'title', 'page', 'oy')},
                            'subsection': dict(cur_subsec) if cur_subsec else None,
                            'sub_items': []}
                items.append(cur_stmt)
                i += 1
                continue
            i += 1
    return items, all_topics, all_subsecs

# ------------------------------------------------------------------ main -----

def sha1_of(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()

def notation_flags(text):
    flags = []
    if re.search(r'[a-z]{1,4}-(?:\d{1,2})\b', text):   # dm-3, s-1 style superscript loss
        flags.append('possible-superscript-loss')
    if re.search(r'\b\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}\b', text):
        flags.append('deep-numbering-in-text')
    return flags

def parse_pdf(pdf_path, qual_slug):
    doc = pymupdf.open(pdf_path)
    kill = strip_running_text(doc)
    fam = FAMILY.get(qual_slug, 'code_column')
    if fam == 'triplet_table':
        statements, topics, subsecs = parse_triplet_table(doc, kill)
    elif fam == 'lettered_table':
        statements, topics, subsecs = parse_lettered_table(doc, kill)
    elif fam == 'bare_int':
        statements, topics, subsecs = parse_bare_int(doc, kill)
    elif fam == 'heading_bullets':
        statements, topics, subsecs = parse_heading_bullets(doc, kill)
    elif fam == 'maths_table':
        statements, topics, subsecs = parse_maths_table(doc, kill)
    elif fam == 'further_maths':
        statements, topics, subsecs = parse_further_maths(doc, kill)
    elif fam == 'english_lit':
        statements, topics, subsecs = parse_english_lit(doc, kill)
    elif fam == 'english_lang_a':
        statements, topics, subsecs = parse_english_lit(
            doc, kill, author_x=ELA_AUTHOR_X, title_max=ELA_TITLE_MAX)
    else:
        statements, topics, subsecs = parse_code_column_bands(doc, kill)
    # finalize
    for st in statements:
        st['practical'] = bool(PRACTICAL_RE.search(st['text']))
        extra = _maths_frag_flags(st['text']) if fam in ('maths_table', 'further_maths') else []
        st['flags'] = sorted(set(st.get('flags', []) + notation_flags(st['text']) + extra))
        st.pop('code_num', None)
        if 'synth_id' in st:
            st['id'] = f"{qual_slug.replace('-', '_').upper()}:{st.pop('synth_id')}"
        elif st.get('scope'):
            st['id'] = f"{qual_slug.replace('-', '_').upper()}:{st['scope']}-{st['official_code']}"
        else:
            st['id'] = f"{qual_slug.replace('-', '_').upper()}:{st['official_code']}"
        _dupn = st.pop('_dupn', None)
        if _dupn:
            st['id'] += f"-dup{_dupn}"
        if '_parts' in st:
            st['text'] = ' '.join(st['_parts']) or st['text']
            st.pop('_parts', None)
        if '_roman' in st:
            st.pop('_roman', None)
    result = {
        'schema': 'syllabai.parsed-specification/1.0',
        'id': qual_slug,
        'family': fam,
        'source': {
            'pdf': os.path.basename(pdf_path),
            'pdf_sha1': sha1_of(pdf_path),
            'pages': doc.page_count,
            'parser': PARSER_VERSION,
            'parsed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
        },
        'topics': topics,
        'subsections': subsecs,
        'spec_points': statements,
        'counts': {
            'spec_points': len(statements),
            'practicals': sum(1 for s in statements if s['practical']),
            'topics': len(topics),
            'subsections': len(subsecs),
            'flagged': sum(1 for s in statements if s['flags']),
        },
    }
    doc.close()
    return result

def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else sorted(FAMILY)
    summary = []
    for slug in only:
        fam = FAMILY.get(slug)
        if not fam:
            continue
        pdfs = sorted(glob.glob(f'{BASE}/{slug}/*.pdf'))
        os.makedirs(f'{OUT_BASE}/{slug}', exist_ok=True)
        for pdf in pdfs:
            try:
                res = parse_pdf(pdf, slug)
                stem = os.path.splitext(os.path.basename(pdf))[0][:48]
                outp = f'{OUT_BASE}/{slug}/{stem}.parsed.json'
                with open(outp, 'w') as f:
                    json.dump(res, f, indent=1, ensure_ascii=False)
                summary.append((slug, stem[:30], res['counts']))
                print(f"OK {slug}/{stem[:34]}: {res['counts']}")
            except Exception as e:
                print(f"FAIL {slug}: {type(e).__name__}: {e}")
    with open(f'{OUT_BASE}/_summary.json', 'w') as f:
        json.dump([{'qual': a, 'pdf': b, 'counts': c} for a, b, c in summary], f, indent=1)

if __name__ == '__main__':
    main()
