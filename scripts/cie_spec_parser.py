#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-1 — deterministic parse of the 33 CIE syllabus PDFs into the
parsed/<cie-slug>/ registry (SCHEMA v1.0 shape + the documented CIE extension:
per-point 'tier'/'number' fields and 'code-assembled'/'synthesized-ordinal' flags).

Zero-LLM: every statement comes from the PDF text layer with page+oy provenance,
same span primitives and conventions as scripts/spec_parser.py (Edexcel,
spec-parser-1.0). Family map frozen from scripts/cie_parse_autodetect.py +
scripts/cie_samples/ reconnaissance (2026-10-19).
"""
import glob, hashlib, json, os, re, sys, datetime
import pymupdf

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSDIR = os.path.join(BASE, 'Official-Specifications')
OUT_BASE = os.path.join(OSDIR, 'parsed')
PARSER_VERSION = 'cie-spec-parser-1.0'
SCHEMA = 'syllabai.parsed-specification/1.0'

# ---------------------------------------------------------------- families ----
# 5 tier_columns + 13 int_statements + 7 nmk_outcomes + 2 ce_codes
# + 1 lettered_items + 5 heading_bullets = 33
FAMILY = {
    'cie-igcse-biology-2023-2025': 'tier_columns',
    'cie-igcse-chemistry-2023-2025': 'tier_columns',
    'cie-igcse-physics-2023-2025': 'tier_columns',
    'cie-igcse-science-combined-science-2023-2024': 'tier_columns',
    'cie-igcse-science-co-ordinated-sciences-double-award-2025-2027': 'tier_columns',

    'cie-a-level-biology-2025-2027': 'int_statements',      # outcomes_right layout
    'cie-a-level-chemistry-2025-2027': 'int_statements',    # single column
    'cie-a-level-physics-2025-2027': 'int_statements',      # single column
    'cie-a-level-computer-science-2024-2025': 'int_statements',
    'cie-a-level-maths-2023-2025': 'int_statements',
    'cie-igcse-computer-science-2023-2025': 'int_statements',  # notes_right
    'cie-igcse-ict-2023-2025': 'int_statements',               # notes_right
    'cie-igcse-accounting-2023-2025': 'int_statements',
    'cie-igcse-accounting-2027-2029': 'int_statements',
    'cie-igcse-economics-2023-2025': 'nmk_outcomes',   # rows print 'N.M.K.' with trailing dot
    'cie-igcse-geography-2025-2026': 'int_statements',
    'cie-igcse-further-maths-additional-maths-2025-2027': 'int_statements',  # notes_right
    'cie-as-environmental-management-2025-2027': 'int_statements',

    'cie-a-level-accounting-2023-2025': 'nmk_outcomes',
    'cie-a-level-business-2023-2025': 'nmk_outcomes',
    'cie-a-level-economics-2023-2025': 'nmk_outcomes',
    'cie-igcse-business-2023-2025': 'nmk_outcomes',
    'cie-igcse-business-2027-2029': 'nmk_outcomes',
    'cie-igcse-economics-2027-2029': 'nmk_outcomes',
    'cie-igcse-environmental-management-2027-2029': 'nmk_outcomes',

    'cie-igcse-maths-2025-2027': 'ce_codes',
    'cie-igcse-maths-international-maths-2025-2027': 'ce_codes',

    'cie-igcse-religious-studies-2025-2027': 'lettered_items',

    'cie-igcse-english-language-2024-2026': 'heading_bullets',
    'cie-igcse-english-language-2027-2029': 'heading_bullets',
    'cie-igcse-english-literature-2023-2025': 'heading_bullets',
    'cie-igcse-history-2024-2026': 'heading_bullets',
    'cie-as-english-general-paper-2028-2030': 'heading_bullets',

    # T-SPECS-9696-4HI1 (2026-10-28, operator order: import the official spec
    # PDFs, parse them, save them): 9696 AS & A Level Geography 2025-2026 is
    # the one CIE qual whose parse was pending (parsed/ dir existed empty).
    # Layout: numbered topics '1. Title' (DOT after the number, unlike 9709),
    # N.M subheads, unnumbered sentence statements directly under subheads (no
    # 'Candidates...' marker line), Paper headers '3.1 Paper 1 ...' to exclude.
    'cie-a-level-geography-2025-2026': 'int_statements',
}

# --- 9696 per-qual adapter (same pattern as OUTCOMES_RIGHT / LIST_CAPTURE) ---
# topic heads print 'N. Title' (dot after the number)
TOPIC_DOT = {'cie-a-level-geography-2025-2026'}
# statements begin immediately under a subhead with no marker line -> arm on
# the subhead event
ARM_ON_SUBHEAD = {'cie-a-level-geography-2025-2026'}
# unnumbered sentence statements at normal line spacing: split a new statement
# when the previous statement text ends with terminal punctuation and this line
# starts capitalised (deterministic, text-layer-faithful; replaces the gap
# heuristic which assumed spaced phrase rows)
SENTENCE_SPLIT = {'cie-a-level-geography-2025-2026'}
# '3.1 Paper 1 Core Physical Geography' section heads: NOT content subtopics
PAPER_HEAD = re.compile(r'^\d{1,2}\.\d{1,2}\s+Paper\s+\d', re.I)
PAPER_HEAD_QUALS = {'cie-a-level-geography-2025-2026'}

# 9700 AL biology: two-column table, subtopic titles LEFT, outcomes RIGHT.
OUTCOMES_RIGHT = {'cie-a-level-biology-2025-2027'}
# 0475: set-text list rows are unbulleted short lines under Set-texts heads.
LIST_CAPTURE = {'cie-igcse-english-literature-2023-2025'}

TIER_COL_CODES = re.compile(r'^([A-Z]?\d{1,2}\.\d{1,2})\s+(.+)$')      # 1.3 / C1.1
TOPIC_INT = re.compile(r'^(\d{1,2})\s+([A-Z].+)$')                     # 2 Organisation...
SUBJ_SECTION = re.compile(r'^(Biology|Chemistry|Physics)$')
SCOPE_BAND = re.compile(r'^(AS|A) Level(?: subject)? content\s*$')
SCOPE_SUFFIX = re.compile(r'\s*\((AS Level|A Level)\)\s*$')
NMK = re.compile(r'^(\d{1,2}\.\d{1,2}\.\d{1,2})\.?\s+(.+)$')
CE_CODE = re.compile(r'^([CE]\d{1,2}\.\d{1,2})\s+(.*)$')
LETT_ITEM = re.compile(r'^\(([a-z])\)\s+(.+)$')
INT_LED = re.compile(r'^(\d{1,2})\s+(.+)$')
BULLET_LED = re.compile(r'^[•–—-]\s+(.*)$')
CONTINUED = re.compile(r'\s*\(?continued\)?\s*$', re.I)
MARKERS = re.compile(
    r'^(Candidates should be able to:|Candidates should know and understand:'
    r'|Learning outcomes|Notes and guidance|Notes and Guidance|Notes and examples'
    r'|Focus points|Specified content|Suggested areas to explore:?'
    r'|Topic|Content|Further guidance|Guidance)\s*$')
TOPIC_DENY = {'Subject content', 'Syllabus content', 'Contents', 'Introduction'}
BOILERPLATE_RX = re.compile(
    r'^(Subject content|Syllabus content|This syllabus gives you|Where appropriate you'
    r'|The mathematical content|Information about calculator|Notes and examples are'
    r'|All candidates should be taught|Scientific subjects are|Practical work helps'
    r'|Knowledge of the content of|Cambridge IGCSE material which|tested directly but'
    r'|Proofs of results will not|Candidates will be expected to be familiar'
    r'|A List of formulas is provided|Formulas for:|Teachers and students are encouraged'
    r'|In all of the following|Candidates should be able to make simple|provided\.'
    r'|Pure Mathematics|Mechanics$|Probability & Statistics)')

def _clean_title(t):
    t = CONTINUED.sub('', t).strip(' \t')
    return t

HEADER_HINT = re.compile(r'\.\s*(Subject content|Syllabus content)')

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
    """Header/footer spans: text repeating on >40% of pages in the edge bands."""
    n = doc.page_count
    bands = {}
    for pno in range(n):
        for s in page_spans(doc[pno]):
            if s['y0'] < 60 or s['y0'] > 760:
                key = re.sub(r'\s+', ' ', s['text']).strip()[:60]
                bands.setdefault(key, set()).add(pno)
    kill = {k for k, ps in bands.items() if len(ps) > max(4, 0.4 * n)}

    def is_killed(s):
        key = re.sub(r'\s+', ' ', s['text']).strip()[:60]
        if key in kill:
            return True
        if re.fullmatch(r'\d{1,3}', s['text'].strip()) and (s['y0'] > 760 or s['y0'] < 60):
            return True
        if s['text'].strip() in ('Back to contents page',) or 'cambridgeinternational.org' in s['text']:
            return True
        return s['y0'] < 25 or s['y0'] > 830
    return is_killed

def _is_bold(font):
    return 'Bold' in font or font.endswith('Bd') or '-Bd' in font

def visual_lines(spans, tol=3.5):
    """Group spans into visual lines by origin-y; gap-aware space join."""
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
        parts, prev = [], None
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
        L['text'] = re.sub(r'\s+', ' ', ' '.join(parts)).strip()
        L['x0'] = min(s['x0'] for s in L['spans'])
        L['x1'] = max(s['x1'] for s in L['spans'])
        L['bold'] = all(_is_bold(s['font']) for s in L['spans'] if s['text'].strip())
        L['sizes'] = [s['size'] for s in L['spans']]
    lines.sort(key=lambda L: L['oy'])
    return lines

def is_noise(line):
    t = line['text']
    return (not t) or len(t) < 2 or MARKERS.match(t) is not None

def sha1_of(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def notation_flags(text):
    flags = []
    if re.search(r'[a-z]{1,4}-(?:\d{1,2})\b', text):
        flags.append('possible-superscript-loss')
    if re.search(r'\b\d{1,2}\.\d{1,2}\.\d{1,2}\.\d{1,2}\b', text):
        flags.append('deep-numbering-in-text')
    return flags

# --------------------------------------------------------- content region ----

DIVIDER_TITLE = re.compile(r'^\d{1,2}\.?\s+(?:Subject|Syllabus) content\s*$')

def content_pages(doc):
    """Pages whose running header names the subject/syllabus content section.
    The section often opens with a divider page (big 'N Subject content'
    title, no section span in the running header) -> extend one page back
    when that page carries the divider title. Falls back to all pages when
    the header bands are too few."""
    hits = []
    for pno in range(doc.page_count):
        txt = ' '.join(s['text'] for s in page_spans(doc[pno]) if s['y0'] < 60)
        if HEADER_HINT.search(re.sub(r'\s+', ' ', txt).strip()):
            hits.append(pno)
    if len(hits) >= 3:
        region = set(hits)
        first = min(hits)
        if first > 0 and (first - 1) not in region:
            lines = visual_lines([s for s in page_spans(doc[first - 1])])
            if any(DIVIDER_TITLE.match(L['text']) and L['bold'] for L in lines):
                region.add(first - 1)
        return region
    return set(range(doc.page_count))

# ------------------------------------------------------------ column bands ----

def col_split(page_spans_list, rx):
    """x0 of the first span matching rx (column divider anchor)."""
    for s in sorted(page_spans_list, key=lambda s: (s['y0'], s['x0'])):
        if re.fullmatch(rx, s['text'].strip()):
            return s['x0']
    return None

def band_lines(spans, lo, hi, tol=3.5):
    """visual lines for spans with lo <= span.x0 < hi (statement bands)."""
    return visual_lines([s for s in spans if lo <= s['x0'] < hi], tol=tol)

# ------------------------------------------------------------- statements ----

def _mk(st, code, text, pno, oy, topic, subsec, scope, tier, number, flags):
    st.append({
        'official_code': code, 'scope': scope, 'tier': tier, 'number': number,
        'text': text, 'page': pno + 1, 'oy': round(oy, 1),
        'topic': topic, 'subsection': subsec,
        'sub_items': [], 'flags': sorted(set(flags)),
    })
    return st[-1]

def _snap(obj):
    return dict(obj) if obj else None

# ------------------------------------------------- family: tier_columns ----
# 0610/0620/0625 (plain N.M codes) + 0653/0973 (subject-letter codes B/C/P).
# Core|Supplement two-column tables; printed per-topic integer statements,
# numbering continuous across the tier columns within a subtopic.

def parse_tier_columns(doc, kill):
    """Core|Supplement two-column tables (0610/0620/0625/0653/0973).
    Heads switch by y-order inside each band walk (a page's later subsec head
    must not claim the earlier statements)."""
    st, topics, subsecs = [], [], []
    scope_subj = None
    carry = {'topic': None, 'sub': None}
    for pno in sorted(content_pages(doc)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        if not spans:
            continue
        full = visual_lines(spans)
        split = None
        for L in full:
            if re.fullmatch(r'Core\s+Supplement(?:al)?|Core\s+Extended', L['text']):
                supp = [s for s in L['spans'] if re.match(r'^Supp', s['text'].strip())
                        or s['text'].strip() == 'Extended']
                if supp:
                    split = min(s['x0'] for s in supp) - 4
                break
        left = band_lines(spans, 0, split) if split else full
        right = band_lines(spans, split, 10000) if split else []
        events = []
        cur_subj = scope_subj
        for L in full:
            t = L['text']
            oy = round(L['oy'], 1)
            if SUBJ_SECTION.fullmatch(t) and L['bold']:
                cur_subj = t
                events.append((oy, 'subj', t))
                continue
            if SCOPE_BAND.match(t):
                continue
            m = re.match(r'^([A-Z]?)(\d{1,2})\s+([A-Z].+)$', t)
            if m and L['bold'] and not re.match(r'^\d+\.\d', t):
                title = _clean_title(m.group(3))
                if title not in TOPIC_DENY and not (
                        topics and topics[-1]['number'] == m.group(2)
                        and topics[-1]['title'] == title):
                    tp = {'number': m.group(2), 'title': title, 'page': pno + 1,
                          'oy': oy, **({'scope': cur_subj} if cur_subj else {})}
                    topics.append(tp)
                    events.append((oy, 'topic', tp))
            m2 = TIER_COL_CODES.match(t)
            if m2 and L['bold'] and '.' in m2.group(1):
                sp = {'code': m2.group(1), 'title': m2.group(2).strip(),
                      'page': pno + 1, 'oy': oy}
                subsecs.append(sp)
                events.append((oy, 'sub', sp))
        events.sort(key=lambda e: e[0])

        def apply_heads(line_oy, state, events=events, pno=pno):
            while state['ei'] < len(events) and events[state['ei']][0] <= line_oy - 0.1:
                ev = events[state['ei']]
                state['ei'] += 1
                if ev[1] == 'subj':
                    state['subj'] = ev[2]
                elif ev[1] == 'topic':
                    state['topic'] = ev[2]
                    state['sub'] = None
                    state['expect'] = None
                elif ev[1] == 'sub':
                    state['sub'] = ev[2]
                    state['expect'] = None

        for band, tier in ((left, 'Core'), (right, 'Supplement')):
            if not band:
                continue
            state = {'ei': 0, 'topic': carry['topic'], 'sub': carry['sub'],
                     'expect': None, 'subj': scope_subj}
            last = None
            prev_oy = prev_size = None
            for L in band:
                t = L['text']
                if not t:
                    continue
                apply_heads(L['oy'], state)
                scope_subj = state['subj'] or scope_subj
                if MARKERS.match(t) or re.fullmatch(r'Core|Supplement(?:al)?|Extended', t):
                    continue
                if any(abs(L['oy'] - h[0]) < 2.0 for h in events):
                    continue
                cur_sub, cur_topic = state['sub'], state['topic']
                m_ord = INT_LED.match(t)
                if m_ord and cur_sub is not None:
                    n = int(m_ord.group(1))
                    if (state['expect'] is None or n == state['expect'] or n == 1) \
                            and m_ord.group(2).strip() not in TOPIC_DENY \
                            and not BOILERPLATE_RX.match(m_ord.group(2).strip()):
                        code = f"{cur_sub['code']}.{n}"
                        last = _mk(st, code, m_ord.group(2).strip(), pno, L['oy'],
                                   _snap(cur_topic), _snap(cur_sub), state['subj'], tier, n,
                                   ['code-assembled'])
                        state['expect'] = n + 1
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                        continue
                m_b = BULLET_LED.match(t)
                if m_b and last is not None:
                    last['sub_items'].append(m_b.group(1).strip())
                    prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    continue
                m_l = LETT_ITEM.match(t)
                if m_l and last is not None:
                    last['sub_items'].append(f"({m_l.group(1)}) {m_l.group(2).strip()}")
                    prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    continue
                if last is not None and not m_ord and not L['bold'] \
                        and len(t) > 2 and re.search(r'[A-Za-z]', t) \
                        and re.search(r'[aeiou]', t.lower()) and re.search(r'[a-z]{2}', t.lower()):
                    same_page = last['page'] == pno + 1 and (prev_oy is None or L['oy'] > prev_oy)
                    next_page = last['page'] == pno and t[:1].islower()
                    if same_page or next_page:
                        last['text'] = (last['text'] + ' ' + t).strip()
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
        carry['topic'] = state['topic'] or carry['topic']
        carry['sub'] = state['sub'] or carry['sub']
    letter_subj = {'B': 'Biology', 'C': 'Chemistry', 'P': 'Physics'}
    for s in st:
        m = re.match(r'^([BCP])\d', s['official_code'])
        if m and s['scope'] in (None, 'Core', 'Supplement'):
            s['scope'] = letter_subj[m.group(1)]
    return st, topics, subsecs

# ---------------------------------------------- family: int_statements ----
# N.M subtopic heads + "Candidates should be able to:"-style marker + printed
# integer statements (or synthesized ordinals for bullet/phrase rows).
# Layout knobs: notes_right (notes column excluded via split x), outcomes_right
# (9700: subtopic titles LEFT, outcomes RIGHT), single column (default).

def parse_int_statements(doc, kill, qual_slug=None):
    """N.M subtopic heads + marker line + printed integer statements (or
    synthesized ordinals for unnumbered phrase rows). Heads switch by
    y-order; the phrase branch is marker-gated and gap-discriminated."""
    st, topics, subsecs = [], [], []
    scope_band = None
    outcomes_right = qual_slug in OUTCOMES_RIGHT
    carry = {'topic': None, 'sub': None}
    for pno in sorted(content_pages(doc)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        if not spans:
            continue
        full = visual_lines(spans)
        split = col_split(spans, r'Notes and (?:guidance|Guidance|examples)|Further guidance|Guidance')
        if outcomes_right:
            split = col_split(spans, r'Learning outcomes') or split
        head_src = band_lines(spans, 0, split) if (outcomes_right and split) else full
        events = []
        state_scope = [scope_band]
        for L in head_src:
            t = L['text']
            oy = round(L['oy'], 1)
            m_band = SCOPE_BAND.match(t)
            if m_band:
                state_scope[0] = 'AS Level' if m_band.group(1) == 'AS' else 'A Level'
                events.append((oy, 'scope', state_scope[0]))
                continue
            m_theme = re.match(r'^(?:Theme|Topic)\s*(\d{1,2})[:.]?\s+([A-Z].+)$', t)
            if m_theme and len(t) > 14 and L['x0'] < 200:
                tp = {'number': m_theme.group(1), 'title': m_theme.group(2).strip(),
                      'page': pno + 1, 'oy': oy}
                if state_scope[0]:
                    tp['scope'] = state_scope[0]
                topics.append(tp)
                events.append((oy, 'topic', tp))
                continue
            m_t = re.match(r'^(\d{1,2})\.?\s+([A-Z].+)$', t) if qual_slug in TOPIC_DOT \
                else re.match(r'^(\d{1,2})\s+([A-Z].+)$', t)
            # 9696: bold flags are absent from the PDF font table; hierarchy is
            # font-SIZE encoded (topic heads 14pt vs body 10pt)
            head_evidence = L['bold'] or (qual_slug in TOPIC_DOT
                                          and max(L['sizes'] or [0]) >= 12.5)
            if m_t and head_evidence and not re.match(r'^\d+\.\d', t) and L['x0'] < 200:
                title = _clean_title(m_t.group(2))
                if title not in TOPIC_DENY and not (
                        topics and topics[-1]['number'] == m_t.group(1)
                        and topics[-1]['title'] == title):
                    tp = {'number': m_t.group(1), 'title': title, 'page': pno + 1,
                          'oy': oy}
                    if state_scope[0]:
                        tp['scope'] = state_scope[0]
                    topics.append(tp)
                    events.append((oy, 'topic', tp))
                continue
            m_s = re.match(r'^(\d{1,2}\.\d{1,2})\s+(.+)$', t)
            if m_s and len(m_s.group(2).strip()) > 1 and not NMK.match(t) \
                    and not INT_LED.match(t) and L['x0'] < 200 \
                    and not (qual_slug in PAPER_HEAD_QUALS and PAPER_HEAD.match(t)):
                title_s = _clean_title(m_s.group(2))
                dup = any(s['code'] == m_s.group(1) and s['title'] == title_s
                          for s in subsecs[-4:])
                if not dup:
                    sp = {'code': m_s.group(1), 'title': title_s,
                          'page': pno + 1, 'oy': oy}
                    subsecs.append(sp)
                    events.append((oy, 'sub', sp))
                else:
                    events.append((oy, 'sub', subsecs[-1]))
        events.sort(key=lambda e: e[0])

        def apply_heads(line_oy, state, events=events, pno=pno):
            while state['ei'] < len(events) and events[state['ei']][0] <= line_oy - 0.1:
                ev = events[state['ei']]
                state['ei'] += 1
                if ev[1] == 'scope':
                    state['scope'] = ev[2]
                elif ev[1] == 'topic':
                    state['topic'] = ev[2]
                    state['sub'] = None
                    state['expect'] = None
                    state['armed'] = False
                elif ev[1] == 'sub':
                    state['sub'] = ev[2]
                    state['expect'] = None
                    # 9696: statements begin directly under the subhead (no
                    # marker line) -> arm on the subhead event
                    state['armed'] = qual_slug in ARM_ON_SUBHEAD

        if outcomes_right and split:
            bands = ((split, 10000),)
        elif split:
            bands = ((0, split),)
        else:
            bands = ((0, 10000),)
        for lo, hi in bands:
            state = {'ei': 0, 'topic': carry['topic'], 'sub': carry['sub'],
                     'expect': None, 'scope': scope_band, 'armed': False}
            last = None
            prev_oy = prev_size = None
            colx = None
            for L in band_lines(spans, lo, hi):
                t = L['text']
                if not t:
                    continue
                _sub_before = id(state['sub'])
                apply_heads(L['oy'], state)
                if id(state['sub']) != _sub_before:
                    colx = None
                    last = None
                scope_band = state['scope'] or scope_band
                if MARKERS.match(t) or SCOPE_BAND.match(t) \
                        or re.fullmatch(r'Core|Supplement(?:al)?|Extended', t):
                    if MARKERS.match(t):
                        state['armed'] = True
                    continue
                if any(abs(L['oy'] - h[0]) < 2.0 for h in events):
                    continue
                if qual_slug in TOPIC_DOT and max(L['sizes'] or [0]) >= 12.5 \
                        and state['topic'] is not None and state['sub'] is None \
                        and topics and state['topic'] is topics[-1]:
                    # 9696: a >12pt line that is neither topic nor subhead while
                    # the topic is open and no subhead has applied = title
                    # continuation (deterministic)
                    topics[-1]['title'] = (topics[-1]['title'].rstrip() + ' ' + t.strip()).strip()
                    continue
                cur_sub, cur_topic = state['sub'], state['topic']
                m_ord = INT_LED.match(t)
                if m_ord and cur_sub is not None:
                    n = int(m_ord.group(1))
                    if (state['expect'] is None or n == state['expect'] or n == 1) \
                            and m_ord.group(2).strip() not in TOPIC_DENY \
                            and not BOILERPLATE_RX.match(m_ord.group(2).strip()) \
                            and not CONTINUED.search(m_ord.group(2)) \
                            and not re.search(r'\(for Paper \d\)', m_ord.group(2)):
                        code = f"{cur_sub['code']}.{n}"
                        last = _mk(st, code, m_ord.group(2).strip(), pno, L['oy'],
                                   _snap(cur_topic), _snap(cur_sub), state['scope'], None, n,
                                   ['code-assembled'])
                        state['expect'] = n + 1
                        state['armed'] = True
                        colx = L['x0']
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                        continue
                m_b = BULLET_LED.match(t)
                if m_b and cur_sub is not None:
                    at_col = colx is None or abs(L['x0'] - colx) < 6
                    if at_col:
                        # statement-level sibling bullet (0452 style): the row
                        # sits at the statement column, not under a statement
                        n = state['expect'] or 1
                        code = f"{cur_sub['code']}.{n}"
                        last = _mk(st, code, m_b.group(1).strip(), pno, L['oy'],
                                   _snap(cur_topic), _snap(cur_sub), state['scope'], None, n,
                                   ['synthesized-ordinal', 'bullet-row'])
                        state['expect'] = n + 1
                        state['armed'] = True
                        colx = L['x0']
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    elif last is not None:
                        last['sub_items'].append(m_b.group(1).strip())
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    continue
                m_l = LETT_ITEM.match(t)
                if m_l and last is not None:
                    last['sub_items'].append(f"({m_l.group(1)}) {m_l.group(2).strip()}")
                    prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    continue
                if cur_sub is not None and len(t) > 2 and re.search(r'[A-Za-z]', t) \
                        and re.search(r'[aeiou]', t.lower()) and not L['bold'] \
                        and not BOILERPLATE_RX.match(t):
                    if last is None:
                        if not state['armed']:
                            continue
                        n = state['expect'] or 1
                        code = f"{cur_sub['code']}.{n}"
                        last = _mk(st, code, t, pno, L['oy'],
                                   _snap(cur_topic), _snap(cur_sub), state['scope'], None, n,
                                   ['synthesized-ordinal'])
                        state['expect'] = n + 1
                        colx = L['x0']
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    else:
                        gap_ok = prev_oy is not None and (L['oy'] - prev_oy) > max(14.0, 1.5 * (prev_size or 10))
                        starts_new = state['armed'] and t[:1].isupper() and (
                            gap_ok or (qual_slug in SENTENCE_SPLIT and last is not None
                                       and last['text'].rstrip().endswith(('.', '?'))))
                        joins = t[:1].islower() or not starts_new
                        if joins:
                            last['text'] = (last['text'] + ' ' + t).strip()
                            prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                        elif state['armed']:
                            n = state['expect'] or 1
                            code = f"{cur_sub['code']}.{n}"
                            last = _mk(st, code, t, pno, L['oy'],
                                       _snap(cur_topic), _snap(cur_sub), state['scope'], None, n,
                                       ['synthesized-ordinal'])
                            state['expect'] = n + 1
                            colx = L['x0']
                            prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
        carry['topic'] = state['topic'] or carry['topic']
        carry['sub'] = state['sub'] or carry['sub']
    return st, topics, subsecs

# ------------------------------------------------ family: nmk_outcomes ----
# Printed N.M.K outcome rows under N.M subtopics under N topics (9708/9609/
# 9706/0450/0264/0455-27/0680); optional (AS|A Level) scope suffix on topics.

def parse_nmk_outcomes(doc, kill):
    st, topics, subsecs = [], [], []
    cur_topic = cur_sub = None
    topic_scope = None
    sub_expect = None
    for pno in sorted(content_pages(doc)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        gsplit = col_split(spans, r'Guidance')
        lines = band_lines(spans, 0, gsplit) if gsplit else visual_lines(spans)
        for L in lines:
            t = L['text']
            if not t or len(t) < 2:
                continue
            m = re.match(r'^(\d{1,2})\s+([A-Z].+)$', t)
            if m and L['bold'] and not re.match(r'^\d+\.\d', t):
                title = _clean_title(m.group(2))
                if title in TOPIC_DENY:
                    continue
                topic_scope = None
                mm = SCOPE_SUFFIX.search(title)
                if mm:
                    topic_scope = mm.group(1)
                cur_topic = {'number': m.group(1), 'title': title,
                             'page': pno + 1, 'oy': round(L['oy'], 1)}
                if topic_scope:
                    cur_topic['scope'] = topic_scope
                topics.append(cur_topic)
                cur_sub = None
                sub_expect = None
                continue
            m2 = re.match(r'^(\d{1,2}\.\d{1,2})\s+(.+)$', t)
            if m2 and ('.' in m2.group(1)):
                title2 = m2.group(2).strip()
                if len(title2) > 1 and not NMK.match(t):
                    cur_sub = {'code': m2.group(1), 'title': title2,
                               'page': pno + 1, 'oy': round(L['oy'], 1)}
                    subsecs.append(cur_sub)
                    sub_expect = None
                    continue
            m3 = NMK.match(t)
            if m3 and cur_sub is not None and m3.group(1).startswith(cur_sub['code'] + '.'):
                k = int(m3.group(1).rsplit('.', 1)[1])
                if sub_expect is None or k == sub_expect or k == 1:
                    _mk(st, m3.group(1), m3.group(2).strip(), pno, L['oy'],
                        _snap(cur_topic), _snap(cur_sub), topic_scope, None, None, [])
                    sub_expect = k + 1
                continue
            m_b = BULLET_LED.match(t)
            if m_b and st:
                st[-1]['sub_items'].append(m_b.group(1).strip())
                continue
            m_l = LETT_ITEM.match(t)
            if m_l and st:
                st[-1]['sub_items'].append(f"({m_l.group(1)}) {m_l.group(2).strip()}")
    return st, topics, subsecs

# ---------------------------------------------------- family: ce_codes ----
# 0580/0607: C/E-prefixed printed codes (tier in the code letter), statements
# + "Notes and examples" column.

def parse_ce_codes(doc, kill):
    """0580/0607: C/E-prefixed printed codes (tier in the code letter),
    statements + Notes-and-examples column; heads switch by y-order."""
    st, topics, subsecs = [], [], []
    carry = {'topic': None, 'sub': None}
    for pno in sorted(content_pages(doc)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        if not spans:
            continue
        full = visual_lines(spans)
        split = col_split(spans, r'Notes and examples')
        events = []
        for L in full:
            t = L['text']
            oy = round(L['oy'], 1)
            if not L['bold']:
                continue
            m_t = re.match(r'^(\d{1,2})\s+([A-Z].+)$', t)
            if m_t and not re.match(r'^\d+\.\d', t) and not CE_CODE.match(t):
                title = _clean_title(m_t.group(2))
                if title not in TOPIC_DENY:
                    tp = {'number': m_t.group(1), 'title': title, 'page': pno + 1,
                          'oy': oy}
                    topics.append(tp)
                    events.append((oy, 'topic', tp))
                continue
            m_c = CE_CODE.match(t)
            if m_c:
                tier = 'Core' if m_c.group(1)[0] == 'C' else 'Extended'
                sp = {'code': m_c.group(1), 'title': m_c.group(2).strip(),
                      'page': pno + 1, 'oy': oy, 'tier': tier}
                subsecs.append(sp)
                events.append((oy, 'sub', sp))
        events.sort(key=lambda e: e[0])

        def apply_heads(line_oy, state, events=events, pno=pno):
            while state['ei'] < len(events) and events[state['ei']][0] <= line_oy - 0.1:
                ev = events[state['ei']]
                state['ei'] += 1
                if ev[1] == 'topic':
                    state['topic'] = ev[2]
                    state['sub'] = None
                    state['expect'] = None
                    state['armed'] = False
                elif ev[1] == 'sub':
                    state['sub'] = ev[2]
                    state['expect'] = None
                    state['armed'] = True   # 0580/0607: no marker lines; prose rows are primary

        lo, hi = (0, split) if split else (0, 10000)
        state = {'ei': 0, 'topic': carry['topic'], 'sub': carry['sub'],
                 'expect': None, 'armed': False}
        last = None
        prev_oy = prev_size = None
        for L in band_lines(spans, lo, hi):
            t = L['text']
            if not t:
                continue
            apply_heads(L['oy'], state)
            if MARKERS.match(t) or re.fullmatch(r'Core|Extended', t):
                state['armed'] = True
                continue
            if any(abs(L['oy'] - h[0]) < 2.0 for h in events):
                continue
            cur_sub, cur_topic = state['sub'], state['topic']
            if cur_sub is None:
                continue
            tier = 'Core' if cur_sub['code'][0] == 'C' else 'Extended'
            m_ord = INT_LED.match(t)
            if m_ord:
                n = int(m_ord.group(1))
                if state['expect'] is None or n == state['expect'] or n == 1:
                    code = f"{cur_sub['code']}.{n}"
                    last = _mk(st, code, m_ord.group(2).strip(), pno, L['oy'],
                               _snap(cur_topic), _snap(cur_sub), None, tier, n,
                               ['code-assembled'])
                    state['expect'] = n + 1
                    state['armed'] = True
                    prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    continue
            m_b = BULLET_LED.match(t)
            if m_b:
                if last is not None:
                    last['sub_items'].append(m_b.group(1).strip())
                    prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                continue
            if len(t) > 2 and re.search(r'[A-Za-z]', t) \
                    and re.search(r'[aeiou]', t.lower()) and not L['bold'] \
                    and not BOILERPLATE_RX.match(t):
                if last is None:
                    if not state['armed']:
                        continue
                    n = state['expect'] or 1
                    code = f"{cur_sub['code']}.{n}"
                    last = _mk(st, code, t, pno, L['oy'],
                               _snap(cur_topic), _snap(cur_sub), None, tier, n,
                               ['synthesized-ordinal'])
                    state['expect'] = n + 1
                    prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                else:
                    gap_ok = prev_oy is not None and (L['oy'] - prev_oy) > max(14.0, 1.5 * (prev_size or 10))
                    starts_new = t[:1].isupper() and gap_ok
                    if not starts_new:
                        last['text'] = (last['text'] + ' ' + t).strip()
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
                    elif state['armed']:
                        n = state['expect'] or 1
                        code = f"{cur_sub['code']}.{n}"
                        last = _mk(st, code, t, pno, L['oy'],
                                   _snap(cur_topic), _snap(cur_sub), None, tier, n,
                                   ['synthesized-ordinal'])
                        state['expect'] = n + 1
                        prev_oy, prev_size = L['oy'], max(L['sizes'] or [10])
    return st, topics, subsecs

# ------------------------------------------------ family: lettered_items ----
# 0490 RS: theme-lettered codes (C2.1) + printed (a)(b)(c) statement rows.

def parse_lettered_items(doc, kill):
    """0490 RS: theme-lettered codes (C2.1) + printed (a)(b)(c) statement rows.
    Heads are weight-light (not bold) -> shape-only detection; everything
    between heads glues into the current item."""
    st, topics, subsecs = [], [], []
    cur_topic = cur_sub = None
    for pno in sorted(content_pages(doc)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        for L in visual_lines(spans):
            t = L['text']
            if not t or len(t) < 2 or MARKERS.match(t):
                continue
            m_t = re.match(r'^([A-Z]?)(\d{1,2})\s+([A-Z].+)$', t)
            m_s = re.match(r'^([A-Z]?\d{1,2}\.\d{1,2})\s+(.+)$', t)
            if m_t and L['bold'] and not m_s:
                title = _clean_title(m_t.group(3))
                if title in TOPIC_DENY:
                    continue
                cur_topic = {'number': m_t.group(2), 'title': title,
                             'page': pno + 1, 'oy': round(L['oy'], 1)}
                topics.append(cur_topic)
                cur_sub = None
                continue
            if m_s and not LETT_ITEM.match(t) and len(m_s.group(2).strip()) > 1:
                cur_sub = {'code': m_s.group(1), 'title': m_s.group(2).strip(),
                           'page': pno + 1, 'oy': round(L['oy'], 1)}
                subsecs.append(cur_sub)
                continue
            m_l = LETT_ITEM.match(t)
            if m_l and cur_sub is not None:
                code = f"{cur_sub['code']}{m_l.group(1)}"
                _mk(st, code, m_l.group(2).strip(), pno, L['oy'],
                    _snap(cur_topic), _snap(cur_sub), None, None, m_l.group(1), [])
                continue
            if st and len(t) > 2 and re.search(r'[A-Za-z]', t) \
                    and re.search(r'[aeiou]', t.lower()) and not L['bold']:
                st[-1]['text'] = (st[-1]['text'] + ' ' + t).strip()
    return st, topics, subsecs

# ------------------------------------------------ family: heading_bullets ----
# 0475/0500/0470/8021: no printed statement codes. Bold section/topic heads
# (numbered where printed) + bullet rows -> synthesized S-ids.

def parse_heading_bullets(doc, kill, qual_slug=None):
    st, topics, subsecs = [], [], []
    cur_topic = None
    useq = 0          # global sequence for unnumbered heads
    pending_bullet = False   # a lone bullet glyph line arms the next text line
    list_capture = qual_slug in LIST_CAPTURE
    lines = None
    for pno in sorted(content_pages(doc)):
        spans = [s for s in page_spans(doc[pno]) if not kill(s)]
        lines = visual_lines(spans)
        for li, L in enumerate(lines):
            t = L['text']
            if not t or len(t) < 2 or MARKERS.match(t) or SCOPE_BAND.match(t):
                if t and re.fullmatch(r'[•\u2013\u2014-]', t):
                    pending_bullet = True
                continue
            m_num = re.match(r'^(\d{1,2})\.?\s+([A-Z].{9,})$', t)
            m_lst = (re.match(r'^(Set texts|Section [A-Z]|Prescribed|Texts|Component \d)', t)
                     if list_capture else None)
            is_head = False
            if m_lst and len(t) < 70:
                useq += 1
                cur_topic = {'number': None, 'title': _clean_title(t),
                             'page': pno + 1, 'oy': round(L['oy'], 1)}
                topics.append(cur_topic)
                is_head = True
            elif m_num and (L['bold'] or len(t) > 14):
                title = _clean_title(m_num.group(2))
                if title not in TOPIC_DENY:
                    if not (cur_topic and cur_topic['number'] == m_num.group(1)):
                        cur_topic = {'number': m_num.group(1), 'title': title,
                                     'page': pno + 1, 'oy': round(L['oy'], 1)}
                        topics.append(cur_topic)
                    is_head = True
            if L['bold']:
                pending_bullet = False
                if is_head:
                    continue
                # unnumbered bold head: keep only when a bullet row follows
                # within 2 lines (0500 skill domains; kills table-cell junk)
                nxt = [lines[k]['text'] for k in range(li + 1, min(li + 3, len(lines)))]
                if len(t) < 60 and t not in TOPIC_DENY and (list_capture or
                        any(BULLET_LED.match(x) or x.strip() in ('•', '–') for x in nxt)):
                    useq += 1
                    cur_topic = {'number': None, 'title': t,
                                 'page': pno + 1, 'oy': round(L['oy'], 1)}
                    topics.append(cur_topic)
                    continue
                if len(t) < 60:
                    continue
            if is_head:
                pending_bullet = False
                continue
            m_b = BULLET_LED.match(t)
            if m_b and cur_topic is not None:
                tnum = cur_topic['number'] if cur_topic['number'] else str(useq)
                code = f"S{tnum}.{len([s for s in st if s['official_code'].startswith(f'S{tnum}.')]) + 1:03d}"
                _mk(st, code, m_b.group(1).strip(), pno, L['oy'],
                    _snap(cur_topic), None, None, None, None, ['synthesized-id'])
                pending_bullet = False
                continue
            if cur_topic is not None and pending_bullet and len(t) > 2 \
                    and re.search(r'[A-Za-z]', t) and not L['bold']:
                tnum = cur_topic['number'] if cur_topic['number'] else str(useq)
                code = f"S{tnum}.{len([s for s in st if s['official_code'].startswith(f'S{tnum}.')]) + 1:03d}"
                _mk(st, code, t, pno, L['oy'],
                    _snap(cur_topic), None, None, None, None,
                    ['synthesized-id', 'bullet-glyph-split'])
                pending_bullet = False
                continue
            if not L['bold'] and len(t) > 2 and re.search(r'[A-Za-z]', t):
                if t[:1].islower() and st:
                    st[-1]['text'] = (st[-1]['text'] + ' ' + t).strip()
                    continue
                if list_capture and len(t) <= 100 and cur_topic is not None \
                        and t[:1].isupper():
                    tnum = cur_topic['number'] if cur_topic['number'] else str(useq)
                    code = f"S{tnum}.{len([s for s in st if s['official_code'].startswith(f'S{tnum}.')]) + 1:03d}"
                    _mk(st, code, t, pno, L['oy'],
                        _snap(cur_topic), None, None, None, None, ['synthesized-id'])
                # capitalised prose (descriptions, venue notes) intentionally
                # not captured: v1.0 keeps statements only (documented)
    return st, topics, subsecs

# -------------------------------------------------------------- finalize ----

def build_report(qual_slug, fam, pdf_path, res):
    points = res['spec_points']
    qual_id = qual_slug.replace('-', '_').upper()
    g2 = len({p['id'] for p in points}) == len(points)
    g3 = all(isinstance(p.get('page'), int) and isinstance(p.get('oy'), (int, float))
             for p in points)
    g4 = all(p['id'].startswith(qual_id + ':') for p in points)
    dupes = {}
    for p in points:
        dupes.setdefault(p['id'], 0)
        dupes[p['id']] += 1
    dup_ids = sorted(k for k, v in dupes.items() if v > 1)
    return {
        'qual': qual_slug, 'family': fam,
        'pdf': os.path.basename(pdf_path), 'pdf_sha1': res['source']['pdf_sha1'],
        'counts': res['counts'],
        'gates': {
            'G1_schema_present': res.get('schema') == SCHEMA,
            'G2_ids_unique': g2, 'G3_provenance_complete': g3,
            'G4_id_prefix_valid': g4,
        },
        'duplicate_ids': dup_ids,
        'gates_all_pass': (res.get('schema') == SCHEMA and g2 and g3 and g4),
    }

def parse_pdf(pdf_path, qual_slug):
    doc = pymupdf.open(pdf_path)
    kill = strip_running_text(doc)
    fam = FAMILY[qual_slug]
    if fam == 'tier_columns':
        statements, topics, subsecs = parse_tier_columns(doc, kill)
    elif fam == 'int_statements':
        statements, topics, subsecs = parse_int_statements(doc, kill, qual_slug)
    elif fam == 'nmk_outcomes':
        statements, topics, subsecs = parse_nmk_outcomes(doc, kill)
    elif fam == 'ce_codes':
        statements, topics, subsecs = parse_ce_codes(doc, kill)
    elif fam == 'lettered_items':
        statements, topics, subsecs = parse_lettered_items(doc, kill)
    else:
        statements, topics, subsecs = parse_heading_bullets(doc, kill, qual_slug)
    if qual_slug in SENTENCE_SPLIT:
        # 9696: the PDF text layer embeds control glyphs (\x07) where the print
        # layout used indent markers -> strip them (fleet parses carry none)
        # and disclose via the 'control-glyph-stripped' flag. A glyph followed
        # by a space strands the space at the text edge once the glyph is gone
        # (1.4.1 emitted ' Modifications...' — T-SPEC-CORPUS-WS-1) -> also
        # strip that stranded edge whitespace, disclosed via
        # 'edge-whitespace-stripped'.
        for s in statements:
            raw = s['text']
            cleaned = re.sub(r'[\x00-\x08\x0b-\x1f\x7f]', '', raw)
            trimmed = cleaned.strip()
            if trimmed != cleaned:
                s['flags'] = sorted(set(s['flags'] + ['edge-whitespace-stripped']))
            if trimmed != raw:
                s['text'] = trimmed
                s['flags'] = sorted(set(s['flags'] + ['control-glyph-stripped']))
            s['sub_items'] = [re.sub(r'[\x00-\x08\x0b-\x1f\x7f]', '', x).strip()
                              for x in s.get('sub_items', [])]
    # finalize: subsection dicts -> printed-shape rows; ids; flags
    for sub in subsecs:
        if 'code' in sub:
            code = sub.pop('code')
            sub['official_code'] = code
            if 'tier' in sub:
                sub['tier'] = sub.pop('tier')
    qual_id = qual_slug.replace('-', '_').upper()
    seen = {}
    for s in statements:
        s['practical'] = False
        base = f"{qual_id}:{s['official_code']}"
        seen[base] = seen.get(base, 0) + 1
        s['id'] = base if seen[base] == 1 else f"{base}-dup{seen[base]}"
        s['flags'] = sorted(set(s['flags'] + notation_flags(s['text'])))
        s.setdefault('scope', None)
    result = {
        'schema': SCHEMA,
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
            'practicals': 0,
            'topics': len(topics),
            'subsections': len(subsecs),
            'flagged': sum(1 for s in statements if s['flags']),
        },
    }
    doc.close()
    return result

def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else sorted(FAMILY)
    debug = '--debug' in only
    only = [a for a in only if not a.startswith('--')] or sorted(FAMILY)
    summary = []
    for slug in only:
        fam = FAMILY.get(slug)
        if not fam:
            print(f"SKIP {slug} (not in FAMILY)")
            continue
        pdfs = sorted(glob.glob(f'{OSDIR}/{slug}/*.pdf'))
        if not pdfs:
            print(f"FAIL {slug}: no pdf")
            continue
        os.makedirs(f'{OUT_BASE}/{slug}', exist_ok=True)
        pdf = pdfs[0]
        try:
            res = parse_pdf(pdf, slug)
            stem = os.path.splitext(os.path.basename(pdf))[0][:48]
            outp = f'{OUT_BASE}/{slug}/{stem}.parsed.json'
            with open(outp, 'w') as f:
                json.dump(res, f, indent=1, ensure_ascii=False)
            rep = build_report(slug, fam, pdf, res)
            with open(f'{OUT_BASE}/{slug}/parse_report.json', 'w') as f:
                json.dump(rep, f, indent=1, ensure_ascii=False)
            summary.append({'qual': slug, 'pdf': stem[:30], 'counts': res['counts'],
                            'gates_all_pass': rep['gates_all_pass']})
            print(f"OK {slug}/{stem[:34]}: {res['counts']}"
                  f"{'' if rep['gates_all_pass'] else '  GATES: ' + str(rep['gates']) + ' dup=' + str(len(rep['duplicate_ids']))}")
            if debug:
                for p in res['spec_points'][:6]:
                    print('   ', json.dumps(p, ensure_ascii=False)[:200])
        except Exception as e:
            import traceback
            print(f"FAIL {slug}: {type(e).__name__}: {e}")
            traceback.print_exc()
    if summary and '--no-summary' not in sys.argv:
        sump = f'{OUT_BASE}/_summary.json'
        old = json.load(open(sump)) if os.path.exists(sump) else []
        kept = [r for r in old if not str(r.get('qual', '')).startswith('cie-')]
        n_ed = len(kept)
        merged = kept + summary
        with open(sump, 'w') as f:
            json.dump(merged, f, indent=1, ensure_ascii=False)
        print(f"_summary.json: {n_ed} existing rows preserved + {len(summary)} CIE rows appended")

if __name__ == '__main__':
    main()
