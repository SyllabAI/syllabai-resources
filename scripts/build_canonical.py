#!/usr/bin/env python3
"""SyllabAI canonical specification bundle builder (v2.0).

Takes the v1.0 parsed.json per qualification and emits the canonical 7-file
bundle + derived graph YAMLs (loader contract), all zero-LLM deterministic:

  parsed/<qual>/spec_points.json            canonical spec points + applicability
  parsed/<qual>/topics.json                 topic/subtopic tree (PART_OF)
  parsed/<qual>/practicals.json             required/suggested practicals
  parsed/<qual>/equations.json              appendix equations (span-geometry)
  parsed/<qual>/assessment_objectives.json  AO statements + weightings
  parsed/<qual>/command_words.json          command-word taxonomy tables
  parsed/<qual>/parse_report.json           gates + oracle checks (updated)
  parsed/_derived/graph/<qual>/*.yaml       loader-contract Layer-A YAMLs
  parsed/_derived/graph/igcse-chemistry/DIFF_VS_RATIFIED.json

Reuses spec_parser.py helpers (page_spans, strip_running_text, sha1_of).
"""
import glob, json, os, re, sys, datetime
import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_parser import (BASE, OUT_BASE, page_spans, strip_running_text,
                         sha1_of, FAMILY)
from spec_assembly_guards import apply_guards, page_lines_from_doc

PARSER_VERSION = 'canonical-builder-2.0'
TODAY = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
DERIVED = f'{OUT_BASE}/_derived/graph'

# ------------------------------------------------------------- qual config ----
# equations sections: (label, title_regex)
EQ_SECTIONS = {
    'igcse-physics':            [('physics_formulae', r'Appendix 7: Physics formulae for relationships')],
    'igcse-physics-modular':    [('physics_formulae', r'Appendix 6: Physics formulae for relationships')],
    'igcse-science-double-award': [('physics_formulae', r'Appendix 8: Physics formulae for relationships')],
    'ial-physics':              [('equations', r'Appendix 7: Equations'),
                                 ('data_sheet', r'Appendix 8: Data sheet')],
    'igcse-maths-a':            [('formulae_foundation', r'Appendix 4: Foundation Tier formulae sheet'),
                                 ('formulae_higher', r'Appendix 5: Higher Tier formulae sheet')],
    'igcse-maths-a-modular':    [('formulae_foundation', r'Appendix 3: Foundation Tier formulae sheet'),
                                 ('formulae_higher', r'Appendix 4: Higher Tier formulae sheet')],
    'igcse-further-maths':      [('formulae_exam', r'Appendix 4: Formulae sheet for examinations'),
                                 ('formulae_learn', r'Appendix 5: Formulae to learn')],
    'igcse-business':           [('business_formulae', r'Appendix 4: Formulae')],
    'ial-chemistry':            [('data_booklet', r'Appendix 9: Data ?booklet')],
}

PAPER_LETTER = {'igcse-chemistry': 'C', 'igcse-biology': 'B', 'igcse-physics': 'P'}

# T-KG-14: modular science twins — topic-number -> unit mapping, from the
# printed 'Content and assessment overview' unit content summaries
# (chem pp.15-17, bio pp.15-16, phys pp.15-17 of the modular specifications).
# Closes the linear-vs-modular applicability asymmetry (audit §5.1).
MODULAR_UNIT_MAPS = {
    'igcse-chemistry-modular': {
        'U1': {'topics': {'1', '2', '3', '4'}, 'code': '4WCH1/1C', 'pages': '15-16'},
        'U2': {'topics': {'5', '6', '7', '8'}, 'code': '4WCH2/1C', 'pages': '17'},
    },
    'igcse-biology-modular': {
        'U1': {'topics': {'1', '2'}, 'code': '4WBI1/1B', 'pages': '15'},
        'U2': {'topics': {'3', '4', '5', '6'}, 'code': '4WBI2/1B', 'pages': '16'},
    },
    'igcse-physics-modular': {
        'U1': {'topics': {'1', '2', '3', '4'}, 'code': '4WPH1/1P', 'pages': '15-16'},
        'U2': {'topics': {'5', '6', '7', '8', '9'}, 'code': '4WPH2/1P', 'pages': '17'},
    },
}
COVER_CODE = {}   # filled from spec.json per qual

def load_spec_meta(slug):
    p = f'{BASE}/{slug}/spec.json'
    if os.path.exists(p):
        return json.load(open(p))
    return {}

# ---------------------------------------------------------- page utilities ----

def clean_lines(page, kill, y_min=55, y_max=778):
    """Visual lines as dicts, header/footer stripped."""
    spans = [s for s in page_spans(page) if not kill(s) and y_min < s['oy'] < y_max]
    lines = []
    for s in sorted(spans, key=lambda s: (s['oy'], s['x0'])):
        for L in lines:
            if abs(L['oy'] - s['oy']) < 3.5:
                L['spans'].append(s)
                break
        else:
            lines.append({'oy': s['oy'], 'spans': [s]})
    for L in lines:
        L['spans'].sort(key=lambda s: s['x0'])
        L['text'] = re.sub(r'\s+', ' ', ' '.join(s['text'] for s in L['spans'])).strip()
        L['x0'] = min(s['x0'] for s in L['spans'])
        L['x1'] = max(s['x1'] for s in L['spans'])
    lines.sort(key=lambda L: L['oy'])
    return lines

def find_section_pages(doc, title_re):
    """Pages where the appendix title is a heading (not the TOC listing)."""
    hits = []
    for pno in range(doc.page_count):
        text = doc[pno].get_text()
        if not re.search(title_re, text, re.I):
            continue
        # TOC pages list 3+ different 'Appendix N:' titles; section pages don't
        n_titles = len(re.findall(r'Appendix\s+\d+\s*:', text))
        if n_titles >= 3:
            continue
        # title should appear in the top half of the page as a heading line
        for L in text.splitlines()[:12]:
            if re.search(title_re, L, re.I):
                hits.append(pno)
                break
    return hits

def section_end(doc, start_pno):
    """Walk forward until a new 'Appendix N:' heading appears."""
    end = doc.page_count - 1
    for pno in range(start_pno + 1, doc.page_count):
        head = [L for L in doc[pno].get_text().splitlines()[:10] if L.strip()]
        for L in head:
            if re.match(r'^\s*Appendix\s+\d+\s*:', L):
                return pno - 1
    return end

# ------------------------------------------------------------- equations ------

def x_over(a, b):
    return min(a['x1'], b['x1']) - max(a['x0'], b['x0'])

def center(s):
    return (s['x0'] + s['x1']) / 2

MATHISH_BAD = re.compile(r'(relationship|following|listed|provided|rearranged|candidates|exemplification|:\s*$|\.\s*$)', re.I)

JOIN_OPS = set('=+\u2212\u2013\u00d7/\u00f7\u00b1')

def _smart_join(items):
    """items: (span, raw_text, display_text) in x order.
    - non-touching spans -> single space (original behavior)
    - touching spans glue ONLY when fonts differ AND the PDF encodes no
      boundary whitespace in the RAW span texts (kerning/font-change splits
      like 'V'(regular)+'olume'(italic)); explicit space chars always win;
      operator boundaries always take a space."""
    out, prev_sp, prev_raw = '', None, ''
    for sp, raw, disp in items:
        t = disp.strip()
        if not t:
            continue
        glue = False
        if prev_sp is not None and sp['x0'] <= prev_sp['x1'] + 0.3 \
                and prev_sp.get('font') != sp.get('font') \
                and not prev_raw[-1:].isspace() and not raw[:1].isspace() \
                and prev_raw[-1:] not in JOIN_OPS and t[:1] not in JOIN_OPS:
            glue = True
        if glue:
            out += t
        else:
            out += (' ' if out else '') + t
        prev_sp, prev_raw = sp, raw
    return re.sub(r'\s+', ' ', out).strip()

def build_clusters(spans, tol=3.5):
    clusters = []
    for s in sorted(spans, key=lambda s: s['oy']):
        for c in clusters:
            if abs(c['oy'] - s['oy']) < tol:
                c['spans'].append(s)
                break
        else:
            clusters.append({'oy': s['oy'], 'spans': [s]})
    for c in clusters:
        c['spans'].sort(key=lambda s: s['x0'])
        c['text'] = _smart_join([(s, s['text'], s['text']) for s in c['spans']])
        c['has_eq'] = any('=' in s['text'] for s in c['spans'])
        c['eq_span'] = next((s for s in c['spans'] if '=' in s['text']), None)
    clusters.sort(key=lambda c: c['oy'])
    return clusters

def near_spans(cluster, ref_t, ref_u):
    """Spans of cluster whose centers sit within the pair x-window (ext 60%);
    sub/superscript satellites (size<=8pt) excluded unless they are the pair."""
    lo = min(ref_t['x0'], ref_u['x0'])
    hi = max(ref_t['x1'], ref_u['x1'])
    w = hi - lo
    ext = min(0.6 * w + 2, 14)
    lo2, hi2 = lo - ext, hi + ext
    out = []
    for s in cluster['spans']:
        if s is ref_t or s is ref_u:
            out.append(s)
        elif s['size'] > 8.0 and lo2 <= center(s) <= hi2:
            out.append(s)
    return out

def extract_equation_page(page, kill):
    """Composite-assembly equation extraction for one appendix page.
    Handles: L1 subject+'=' between numerator/denominator rows; L2 '=' on the
    denominator row; twin-fraction rows (transformer); tiny stacked pairs (1/2);
    satellite sup/sub (size<=8pt); plain '=' lines. Verbatim, zero-LLM."""
    spans = [s for s in page_spans(page) if not kill(s) and 55 < s['oy'] < 778]
    if not spans:
        return []
    # two-pass clustering: mains cluster tightly (tol 2.0 keeps fraction halves
    # separate from '=' rows); small spans (<=8pt sup/sub) join the nearest
    # main cluster within dy 5.0 so subscripts stay with their base row
    mains = [s for s in spans if s['size'] > 8.0]
    small = [s for s in spans if s['size'] <= 8.0]
    clusters = build_clusters(mains, tol=2.0)
    for sm in small:
        if clusters:
            best = min(clusters, key=lambda c: abs(c['oy'] - sm['oy']))
            if abs(best['oy'] - sm['oy']) < 5.0:
                best['spans'].append(sm)
                continue
        clusters.append({'oy': sm['oy'], 'spans': [sm]})
    for c in clusters:
        c['spans'].sort(key=lambda s: s['x0'])
        c['text'] = _smart_join([(s, s['text'], s['text']) for s in c['spans']])
        c['has_eq'] = any('=' in s['text'] for s in c['spans'])
        c['eq_span'] = next((s for s in c['spans'] if '=' in s['text']), None)
    clusters.sort(key=lambda c: c['oy'])
    consumed = set()

    # ---- fraction pair discovery (grouped by anchor cluster) ----
    pair_recs = []
    for i, ci in enumerate(clusters):
        for j, cj in enumerate(clusters):
            if j <= i:
                continue
            gap = cj['oy'] - ci['oy']
            if not (4.5 < gap < 26):
                continue
            cands = []
            for t in ci['spans']:
                if '=' in t['text'] or MATHISH_BAD.search(t['text']):
                    continue
                for u in cj['spans']:
                    if '=' in u['text'] or MATHISH_BAD.search(u['text']):
                        continue
                    if abs(t['size'] - u['size']) > 1.0:
                        continue
                    if abs(center(t) - center(u)) > 80:
                        continue
                    ov = x_over(t, u)
                    tiny = len(t['text'].strip()) <= 2 and len(u['text'].strip()) <= 2
                    if ov > 0.55 * min(t['x1'] - t['x0'], u['x1'] - u['x0']) or (
                            tiny and ov > -1.5 and 4 < gap < 14):
                        cands.append((t, u, ov))
            if not cands:
                continue
            # greedy: accept x-disjoint pairs left-to-right (twin fractions)
            accepted = []
            for t, u, ov in sorted(cands, key=lambda c: c[0]['x0']):
                if any(not (t['x1'] < a[1]['x0'] - 2 or u['x1'] < a[0]['x0'] - 2
                            or a[0]['x1'] < t['x0'] - 2 or a[1]['x1'] < u['x0'] - 2)
                       for a in accepted):
                    continue
                accepted.append((t, u, ov))
            if not accepted:
                continue
            anchors = [c for c in clusters if c['has_eq']
                       and ci['oy'] - 1 <= c['oy'] <= cj['oy'] + 1
                       and abs(c['oy'] - ci['oy']) > 1.0]
            if not anchors:
                continue
            a = min(anchors, key=lambda c: abs(c['oy'] - (ci['oy'] + cj['oy']) / 2))
            if a is ci:
                continue
            for t, u, ov in accepted:
                pair_recs.append({'ci': ci, 'cj': cj, 't': t, 'u': u, 'a': a})

    # ---- render one composite line per anchor cluster ----
    lines = []
    by_anchor = {}
    for rec in pair_recs:
        by_anchor.setdefault(id(rec['a']), {'a': rec['a'], 'pairs': []})['pairs'].append(rec)

    for grp in by_anchor.values():
        a = grp['a']
        eq_span = a['eq_span']
        eq_txt = eq_span['text']
        left_txt, right_txt = (eq_txt.split('=', 1) if '=' in eq_txt else ('', eq_txt))
        left_txt, right_txt = left_txt.strip(), right_txt.strip()
        parts = []  # (x, text)
        used_spans = [eq_span]
        used_ids = {id(x) for x in used_spans}
        subj_spans = [sp for sp in a['spans']
                      if sp is not eq_span and sp['x1'] <= eq_span['x0'] + 0.5
                      and id(sp) not in used_ids]
        for sp in subj_spans:
            parts.append((sp['x0'], sp['text'].strip()))
            used_spans.append(sp)
            used_ids.add(id(sp))
        if left_txt:
            parts.append((eq_span['x0'], left_txt))
        parts.append((eq_span['x0'], '='))
        ranges = []
        for rec in sorted(grp['pairs'], key=lambda r: min(r['t']['x0'], r['u']['x0'])):
            ci, cj, t, u = rec['ci'], rec['cj'], rec['t'], rec['u']
            eq_x0, eq_x1 = eq_span['x0'], eq_span['x1']
            num = near_spans(ci, t, u)
            if a['oy'] == cj['oy']:                      # L2: '=' on denominator row
                den = [s for s in cj['spans'] if s['x0'] > eq_x1 - 0.5
                       and center(s) <= max(t['x1'], u['x1']) + 0.6 * (t['x1'] - t['x0']) + 8]
            else:                                        # L1/L3: '=' between rows
                den = near_spans(cj, t, u)
            if not num or not den:
                continue
            frac = f"({join_x(num)})/({join_x(den)})"
            fx = min(s['x0'] for s in num)
            parts.append((fx, frac))
            used_spans += num + den
            ranges.append((ci['oy'], cj['oy']))
        if right_txt:
            parts.append((eq_span['x1'], right_txt))
        trail = [s for s in a['spans'] if s is not eq_span
                 and s['x0'] > eq_span['x1'] + 0.5 and id(s) not in used_ids]
        for s in trail:
            parts.append((s['x0'], s['text'].strip()))
            used_spans.append(s)
        if len(parts) < 2:
            continue
        parts.sort(key=lambda p: p[0])
        # dedupe consecutive identical '=' parts (twin fractions share one anchor)
        seen_eq = False
        txt_parts = []
        for x, p in parts:
            if p == '=':
                if seen_eq:
                    continue
                seen_eq = True
            txt_parts.append(p)
        txt = re.sub(r'\s+', ' ', ' '.join(txt_parts)).strip()
        lo = min(r[0] for r in ranges) if ranges else a['oy']
        hi = max(r[1] for r in ranges) if ranges else a['oy']
        lines.append({'oy': a['oy'], 'x0': min(p[0] for p in parts),
                      'x1': max(s['x1'] for s in used_spans), 'text': txt,
                      'range': (lo, hi)})
        for s in used_spans:
            consumed.add(id(s))

    # ---- live remainder rows: merge into composites when inside their range ----
    merged = []
    for c in clusters:
        live = [s for s in c['spans'] if id(s) not in consumed]
        if not live:
            continue
        host = None
        for L in lines:
            lo, hi = L.get('range', (1e9, -1e9))
            if lo - 1 <= c['oy'] <= hi + 1:
                if host is None or abs(L['oy'] - c['oy']) < abs(host['oy'] - c['oy']):
                    host = L
        if host is not None:
            mains = [s for s in live if s['size'] > 8.0]
            sats = [s for s in live if s['size'] <= 8.0]
            host['text'] += ' ' + attach_sats(mains, sats)
            host['x1'] = max(host['x1'], max(s['x1'] for s in live))
            for s in live:
                consumed.add(id(s))
        else:
            merged.append((c, live))
    # ---- satellite sup/sub attachment on remaining rows ----
    final = [(L['oy'], L['x0'], L['text']) for L in lines]
    for c, live in merged:
        mains = [s for s in live if s['size'] > 8.0]
        sats = [s for s in live if s['size'] <= 8.0]
        txt = attach_sats(mains, sats)
        if txt.strip() and txt.strip() != '=':
            final.append((c['oy'], min(s['x0'] for s in live), txt))
    final.sort(key=lambda r: (r[0], r[1]))
    return [{'oy': oy, 'x0': x0, 'text': t} for oy, x0, t in final]

def join_x(spans):
    parts = sorted(spans, key=lambda s: s['x0'])
    out = ''
    prev = None
    for s in parts:
        t = s['text'].strip()
        if not t:
            continue
        if prev is not None and s['x0'] - prev['x1'] < 1.2 and out and not out.endswith(' '):
            out += t          # kerning split: no visual gap
        else:
            out += (' ' if out else '') + t
        prev = s
    return re.sub(r'\s+', ' ', out).strip()

def attach_sats(mains, sats):
    """Assemble mains (+operators) in x order; small spans (<=8pt) attach as
    ^sup (small glyph at/above baseline) or _sub (below), else inline.
    Satellite host = narrowest span containing it, else closest preceding
    span (exponents/subscripts follow their base) — fixes πr²h attaching
    ^2 to π instead of r."""
    OPS = {'=', '\u00d7', '+', '\u2212', '-', '/', '\u00f7', '\u00b1'}

    assign = {}
    for t in sats:
        cands = [m for m in mains
                 if abs(m['oy'] - t['oy']) < 15
                 and (m['x0'] <= center(t) <= m['x1']
                      or max(m['x0'], t['x0']) - min(m['x1'], t['x1']) < 5)]
        if not cands:
            continue
        inside = [m for m in cands if m['x0'] <= center(t) <= m['x1']]
        if inside:
            best = min(inside, key=lambda m: m['x1'] - m['x0'])
        else:
            # exponent/subscript follows its base: closest preceding span wins
            prev = [m for m in cands if m['x1'] <= t['x0'] + 0.5]
            if prev:
                best = max(prev, key=lambda m: m['x1'])
            else:
                best = min(cands, key=lambda m: (abs(m['x0'] - t['x0']), m['x0']))
        assign.setdefault(id(best), []).append(t)
    parts = sorted([(m['x0'], m['text'].strip(), m) for m in mains], key=lambda p: p[0])
    out = []
    for x, txt, m in parts:
        s_txt = txt
        mine = assign.get(id(m), [])
        is_op = txt in OPS
        sup, sub, inline = [], [], []
        for t in mine:
            ratio = t['size'] / max(m['size'], 0.1)
            if not is_op and ratio <= 0.8:
                if t['oy'] < m['oy'] + 1.0:
                    sup.append(t['text'].strip())
                else:
                    sub.append(t['text'].strip())
            else:
                inline.append((t['x0'], t['text'].strip(), t))
        for x2 in sup:
            s_txt += f"^{x2}"
        for x2 in sub:
            s_txt += f"_{x2}"
        out.append((x, s_txt, m))
        for ix, itxt, isp in inline:
            out.append((ix, itxt, isp))
    out.sort(key=lambda p: p[0])
    return _smart_join([(sp, sp['text'], t) for _, t, sp in out])

NUM_START = re.compile(r'^\((\d{1,2})\)\s*(.*)$')

def extract_equations(doc, kill, label, title_re, meta):
    pages = find_section_pages(doc, title_re)
    if not pages:
        return None
    p0 = pages[-1]
    p1 = section_end(doc, p0)
    note = None
    entries, cur = [], None
    def flush():
        nonlocal cur
        if cur and cur['equations']:
            entries.append(cur)
        cur = None
    for pno in range(p0, p1 + 1):
        for L in extract_equation_page(doc[pno], kill):
            txt_in = L['text'].strip()
            m = NUM_START.match(txt_in)
            if m:
                flush()
                cur = {'number': int(m.group(1)),
                       'description': m.group(2).strip().rstrip(':') or None,
                       'equations': [], 'page': pno + 1, 'oy': round(L['oy'], 1)}
                continue
            txt = txt_in.rstrip(':').strip() if not txt_in.endswith(':') else txt_in
            if not txt or re.match(r'^Appendix\s+\d+\s*:', txt):
                continue
            if '=' in txt or '/' in txt:
                if cur is None:
                    cur = {'number': None, 'description': None,
                           'equations': [], 'page': pno + 1, 'oy': round(L['oy'], 1)}
                if cur['equations'] and cur['equations'][-1].endswith('='):
                    cur['equations'][-1] += ' ' + txt   # line ending '=' continuation
                else:
                    cur['equations'].append(txt)
                if cur['number'] is None:
                    flush()                              # unnumbered: 1 equation/entry
            else:
                bare = txt_in.rstrip(':').strip()
                if cur is None:
                    if note is None:
                        note = bare
                    continue
                if cur['description'] is None:
                    cur['description'] = bare or None
                elif not cur['equations'] and (txt_in.endswith(':') or len(bare) < 30):
                    cur['description'] = (cur['description'] + ' ' + bare).strip()
                elif bare.lower().startswith(('where', 'for', 'given')):
                    cur['note_for'] = bare
                else:
                    cur['equations'].append(bare)
    flush()
    entries = [e for e in entries if e['equations'] or e['description']]
    return {
        'label': label,
        'title': re.search(title_re, doc[p0].get_text(), re.I).group(0).strip(),
        'pages': [p0 + 1, p1 + 1],
        'note': note,
        'entries': entries,
    }

# ---------------------------------------------------- assessment objectives ----

AO_ROW = re.compile(r'^AO\s?\d[a-b]?(\(a\)|\(b\))?$', re.I)
NUM_RANGE = re.compile(r'^\d{1,3}(\.\d+)?(\s*[–\-]\s*\d{1,3}(\.\d+)?)?$')

def _ao_junk(desc):
    """Unit-table header/body artifacts that masquerade as AO descriptors."""
    toks = desc.split()
    if not toks:
        return True
    if all(AO_ROW.match(t) or NUM_RANGE.match(t) for t in toks):
        return True
    if re.match(r'^(Unit|Paper|Component)\b', desc) and (
            sum(1 for t in toks if NUM_RANGE.match(t)) >= 1
            or re.search(r'number\s*$', desc, re.I)):
        return True
    if sum(1 for t in toks if NUM_RANGE.match(t)) >= 2:
        return True
    return False

def extract_aos(doc, kill, slug):
    pages = find_section_pages(doc, r'Assessment objectives and weightings')
    if not pages:
        pages = find_section_pages(doc, r'Relationship of assessment objectives to units')
    if not pages:
        pages = find_section_pages(doc, r'^Assessment objectives')
    if not pages:
        return None, ['ao-section-not-found']
    flags = []
    # section pages may be disjoint (IAL IAS + IA2 tables) -> walk each cluster
    sections = []
    for p0 in pages:
        p1 = section_end(doc, p0)
        sections.append((p0, p1))
    merged = []
    for p0, p1 in sorted(sections):
        if merged and p0 <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], p1))
        else:
            merged.append((p0, p1))
    statements, unit_rows = [], []
    for p0, p1 in merged:
      for pno in range(p0, p1 + 1):
        page = doc[pno]
        text = page.get_text()
        # AO statements: 'AO1' ... prose ... (with % weightings on same rows)
        tabs = page.find_tables()
        for t in tabs.tables:
            rows = t.extract()
            flat = [[(c or '').replace('\n', ' ').strip() for c in r] for r in rows]
            is_unit_tbl = any(re.match(r'unit', (c or ''), re.I) for c in flat[0])
            if is_unit_tbl:
                tbl_title = next((L for L in text.splitlines()
                                  if re.search(r'relationship of assessment objectives', L, re.I)), '')
                for r in flat[1:]:
                    name = next((c for c in r if c and not AO_ROW.match(c)
                                 and not NUM_RANGE.match(c)), None)
                    if not name:
                        continue
                    vals = [c for c in r if c and (NUM_RANGE.match(c) or '%' in c)]
                    if vals:
                        unit_rows.append({'unit': name, 'weightings': vals,
                                          'table_title': tbl_title or None, 'page': pno + 1})
                continue
            for r in flat:
                ao = next((c for c in r if AO_ROW.match(c) or re.match(r'^AO\s?\d[a-b]?\)?', c)), None)
                if not ao:
                    continue
                desc = next((c for c in r if len(c) > 15 and c != ao and '%' not in c), '')
                pct = next((c for c in r if '%' in c), None)
                if desc and not _ao_junk(desc) and (ao, desc) not in {(x['ao'], x['description']) for x in statements}:
                    statements.append({'ao': ao.replace(' ', ''), 'description': desc,
                                       'weighting_overall': pct, 'page': pno + 1})
        # text fallback for statements if tables gave nothing
        if not statements:
            lines = [L for L in text.splitlines() if L.strip()]
            cur_ao, buf = None, []
            for L in lines:
                m = re.match(r'^\s*(AO\s?\d)\s*$', L)
                if m:
                    if cur_ao:
                        _d = ' '.join(buf).strip()
                        if not _ao_junk(_d):
                            statements.append({'ao': cur_ao, 'description': _d,
                                               'weighting_overall': None, 'page': pno + 1})
                    cur_ao, buf = m.group(1).replace(' ', ''), []
                    continue
                if cur_ao:
                    if re.search(r'\d{1,3}(\u2013|-)?\d{0,3}(\.\d+)?\s*%|\b100%', L):
                        _d = ' '.join(buf).strip()
                        if not _ao_junk(_d):
                            statements.append({'ao': cur_ao, 'description': _d,
                                               'weighting_overall': L.strip(), 'page': pno + 1})
                        cur_ao, buf = None, []
                    else:
                        buf.append(L.strip())
            if cur_ao and buf:
                _d = ' '.join(buf).strip()
                if not _ao_junk(_d):
                    statements.append({'ao': cur_ao, 'description': _d,
                                       'weighting_overall': None, 'page': pno + 1})
    # overall weighting table fallback (AO1 x% ...) if pct missing
    if statements and all(s['weighting_overall'] is None for s in statements):
        m = re.findall(r'(AO\d)\D{0,80}?(\d{1,3}(?:\u2013|-|\s)\d{1,3}(?:\.\d+)?%|\d{1,3}(?:\.\d+)?%)',
                       doc[p0].get_text())
        for ao, pct in m:
            for s in statements:
                if s['ao'] == ao and s['weighting_overall'] is None:
                    s['weighting_overall'] = pct
    for s in statements:
        if s['weighting_overall'] and re.match(r'^\d{1,3}\s+\d{1,3}(\.\d+)?%$', s['weighting_overall']):
            s['weighting_overall'] += ' (en-dash lost in source text layer)'
            if 'ao-dash-lost' not in flags:
                flags.append('ao-dash-lost')
    if len(statements) < 3:
        flags.append('ao-descriptors-not-printed-in-source' if unit_rows
                     else 'ao-incomplete')
    result = {
        'section_pages': [p0 + 1, p1 + 1],
        'statements': statements,
        'unit_weightings': unit_rows,
    }
    return result, flags

# ---------------------------------------------------------- command words ----

def extract_command_words(doc, kill):
    words, seen_pages = [], []
    for pno in range(doc.page_count):
        tabs = doc[pno].find_tables()
        for t in tabs.tables:
            rows = t.extract()
            flat = [[(c or '').replace('\n', ' ').strip() for c in r] for r in rows]
            if not flat:
                continue
            header = flat[0]
            if not any(re.match(r'^command words?$', c, re.I) for c in header if c):
                continue
            for r in flat[1:]:
                cells = [c for c in r if c]
                if not cells:
                    continue
                verb = cells[0]
                if re.match(r'^command words?$', verb, re.I) or len(verb.split()) > 6:
                    continue
                definition = ' '.join(cells[1:]) if len(cells) > 1 else None
                if not definition:
                    continue          # section-header row (e.g. 'Multiple choice questions')
                words.append({'command_word': verb, 'definition': definition,
                              'page': pno + 1})
                if pno + 1 not in seen_pages:
                    seen_pages.append(pno + 1)
    # de-dup (multi-page tables repeat nothing, but cross-table dupes possible)
    out, seen = [], set()
    for w in words:
        key = w['command_word'].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(w)
    return out, seen_pages

# --------------------------------------------------------- applicability ----

def applicability(slug, scope, official_code, topic_number=None):
    L = PAPER_LETTER.get(slug)
    if slug == 'igcse-maths-a':
        if scope == 'H':
            return {'tier': 'Higher', 'rule': 'Higher Tier addition: printed only in the '
                    'Higher Tier content walk; Foundation Tier statements are assumed '
                    'knowledge for Higher Tier papers'}
        return {'tier': 'Foundation', 'rule': 'printed in the Foundation Tier content walk; '
                'assumed knowledge for Higher Tier papers'}
    if L and slug in ('igcse-chemistry', 'igcse-biology', 'igcse-physics'):
        suffix = official_code[-1] if official_code and official_code[-1].isalpha() else None
        if suffix:
            return {'papers': [f'2{L}'], 'double_award_shared': False,
                    'rule': f'{suffix}-suffixed statements are {slug.split("-")[1]}-only '
                            f'content (not in Science Double Award 4SD0); assessed in Paper 2{L} only'}
        return {'papers': [f'1{L}', f'2{L}'], 'double_award_shared': True,
                'rule': 'non-suffixed statements are shared with Science Double Award 4SD0 '
                        f'and assessed in both Paper 1{L} and Paper 2{L}'}
    if slug == 'igcse-science-double-award':
        return {'papers': ['1', '2'], 'double_award_shared': True,
                'rule': 'all 4SD0 statements are double-award content assessed in both papers'}
    if slug in MODULAR_UNIT_MAPS:
        um = MODULAR_UNIT_MAPS[slug]
        tnum = str(topic_number) if topic_number is not None else None
        for unit, m in um.items():
            if tnum in m['topics']:
                others = ', '.join(sorted(m['topics'], key=int))
                return {'unit_scope': unit,
                        'rule': f'content sits in the printed {slug.split("-")[1].title()} '
                                f'{unit} content summary (topics {others}, '
                                f'spec pp.{m["pages"]}); assessed by the '
                                f'{unit.replace("U", "Unit ")} examination '
                                f'(unit code {m["code"]})'}
        return None
    if scope:
        if re.match(r'^U\d[FH]$', str(scope)):
            tier_lab = 'Foundation' if scope.endswith('F') else 'Higher'
            return {'unit_scope': scope,
                    'rule': f'content restated in the {scope} unit walk '
                            f'(Unit {scope[1]} {tier_lab}) of the modular specification'}
        return {'unit_scope': scope, 'rule': f'content belongs to unit {scope} (modular/IAL structure)'}
    return None

# -------------------------------------------------------- canonical emit ----

def qid(slug):
    return slug.replace('-', '_').upper()

def emit_canonical(slug, parsed, aos, cws, eqs, eq_flags):
    pdf_sha1 = parsed['source']['pdf_sha1']
    qual_id = qid(slug)
    meta_src = load_spec_meta(slug)

    # ---- spec_points.json ----
    points = []
    for i, sp in enumerate(parsed['spec_points'], 1):
        points.append({
            'id': sp['id'], 'official_code': sp.get('official_code'),
            'scope': sp.get('scope'), 'text': sp['text'],
            'topic': sp.get('topic'), 'subsection': sp.get('subsection'),
            'sub_items': sp.get('sub_items', []), 'practical': sp.get('practical', False),
            'applicability': applicability(slug, sp.get('scope'), sp.get('official_code'),
                                           (sp.get('topic') or {}).get('number')),
            'leading_verb': (sp['text'].split(' ', 1)[0].lower() if sp['text'] else None),
            'ordering': i,
            'provenance': {'pdf': parsed['source']['pdf'], 'pdf_sha1': pdf_sha1,
                           'page': sp['page'], 'oy': sp['oy'], 'extraction_method': 'pdf-span-geometry'},
            'flags': sp.get('flags', []),
        })
    spec_points_doc = {
        'schema': 'syllabai.spec-points/1.0', 'id': slug,
        'qualification': meta_src.get('cover_code'), 'spec_codes': meta_src.get('spec_codes'),
        'issue': meta_src.get('issue'), 'family': parsed['family'],
        'source': parsed['source'], 'spec_points': points,
        'counts': {'spec_points': len(points),
                   'practicals': sum(1 for p in points if p['practical']),
                   'flagged': sum(1 for p in points if p['flags'])},
    }

    # ---- topics.json ----
    topic_rows, subsec_rows = [], []
    tmap = {}
    src_topics = parsed['topics']
    if slug in ('ial-biology', 'ial-chemistry', 'ial-physics'):
        # T-PARSE-FIX: the topics capture mixed TOC rows and unit-divider rows
        # into the body-topic list (titles with glued page numbers/unit codes).
        # Keep only headers that real spec statements anchor to (page+oy match).
        used = {(p['topic']['page'], p['topic']['oy'])
                for p in parsed['spec_points'] if p.get('topic')}
        src_topics = [t for t in src_topics if (t['page'], t.get('oy')) in used]
    for i, t in enumerate(src_topics, 1):
        code = f"{meta_src.get('cover_code') or qual_id}-T{i}"
        tmap[i] = code
        topic_rows.append({'code': code, 'number': t.get('number'), 'title': t['title'],
                           'ordering': i, 'provenance': {'pdf_sha1': pdf_sha1,
                           'page': t['page'], 'oy': t.get('oy')}})
    for i, s in enumerate(parsed['subsections'], 1):
        subsec_rows.append({'code': f"{meta_src.get('cover_code') or qual_id}-SUB{i}",
                            'letter': s.get('letter') or s.get('code'), 'title': s['title'],
                            'page': s['page'], 'provenance': {'pdf_sha1': pdf_sha1, 'page': s['page']}})
    topics_doc = {
        'schema': 'syllabai.topics/1.0', 'id': slug, 'source': {'pdf_sha1': pdf_sha1},
        'topics': topic_rows, 'subsections': subsec_rows,
        'counts': {'topics': len(topic_rows), 'subsections': len(subsec_rows)},
    }

    # ---- practicals.json ----
    pracs = [p for p in points if p['practical']]
    practicals_doc = {
        'schema': 'syllabai.practicals/1.0', 'id': slug, 'source': {'pdf_sha1': pdf_sha1},
        'note': 'statements flagged by the practical: prefix rule (deterministic)',
        'practicals': [{'code': f"{qual_id}-PR-{i:02d}", 'spec_point': p['id'],
                        'summary': p['text'][:300], 'page': p['provenance']['page'],
                        'ordering': i} for i, p in enumerate(pracs, 1)],
        'counts': {'practicals': len(pracs)},
    }
    return spec_points_doc, topics_doc, practicals_doc

# ------------------------------------------------------------- main ----

def process(slug):
    pdfs = sorted(glob.glob(f'{BASE}/{slug}/*.pdf'))
    out_dir = f'{OUT_BASE}/{slug}'
    parsed_path = glob.glob(f'{out_dir}/*.parsed.json')[0]
    parsed = json.load(open(parsed_path))
    pdf_path = f'{BASE}/{slug}/{parsed["source"]["pdf"]}'
    doc = pymupdf.open(pdf_path)
    kill = strip_running_text(doc)
    # T-KG-14: assembly guards — re-join wrapped bullets, split lettered-lead
    # merges, flag two-column interleaves (PDF-verified repairs from T-KG-13
    # 14, generalised; guard tests: scripts/test_spec_assembly_guards.py)
    guard_stats = apply_guards(
        parsed['spec_points'],
        get_page_lines=lambda pg: page_lines_from_doc(doc, pg),
        families=parsed.get('family'))
    if guard_stats:
        print(f'  assembly guards: {len(guard_stats)} event(s) on {slug}')
    report = json.load(open(f'{out_dir}/parse_report.json')) if os.path.exists(f'{out_dir}/parse_report.json') else {}

    aos, ao_flags = extract_aos(doc, kill, slug)
    cws, cw_pages = extract_command_words(doc, kill)
    eq_sections, eq_flags = [], []
    if slug == 'ial-physics':
        eq_flags.append('ial-physics equations appendix: dense nested fraction layout, '
                        'reconstruction approximate; raw spans preserved, refine at consumption layer')
    if slug in ('igcse-further-maths', 'igcse-maths-a', 'igcse-maths-a-modular'):
        eq_flags.append('multi-column formulae sheets: fraction reconstruction approximate; '
                        'raw spans preserved, refine at consumption layer')
    for label, title_re in EQ_SECTIONS.get(slug, []):
        sec = extract_equations(doc, kill, label, title_re, load_spec_meta(slug))
        if sec is None:
            eq_flags.append(f'{label}: section not found')
        elif len(sec['entries']) < 2:
            eq_flags.append(f'{label}: <2 entries extracted (may be external reference)')
            eq_sections.append(sec)
        else:
            eq_sections.append(sec)
    doc.close()

    sp_doc, tp_doc, pr_doc = emit_canonical(slug, parsed, aos, cws, eq_sections, eq_flags)

    def w(path, obj):
        with open(path, 'w') as f:
            json.dump(obj, f, indent=1, ensure_ascii=False)
    w(f'{out_dir}/spec_points.json', sp_doc)
    w(f'{out_dir}/topics.json', tp_doc)
    w(f'{out_dir}/practicals.json', pr_doc)
    w(f'{out_dir}/equations.json', {
        'schema': 'syllabai.equations/1.0', 'id': slug,
        'source': {'pdf': parsed['source']['pdf'], 'pdf_sha1': parsed['source']['pdf_sha1'],
                   'parser': PARSER_VERSION, 'generated': TODAY},
        'method': 'span-geometry reconstruction: cross-cluster fraction pairing with "=" anchor, '
                  'satellite sup/sub attachment, verbatim-only (zero-LLM)',
        'sections': eq_sections,
        'counts': {'sections': len(eq_sections),
                   'entries': sum(len(s['entries']) for s in eq_sections),
                   'equations': sum(len(e['equations']) for s in eq_sections for e in s['entries'])},
    } if eq_sections else {'schema': 'syllabai.equations/1.0', 'id': slug,
                           'sections': [], 'counts': {'sections': 0, 'entries': 0, 'equations': 0},
                           'note': 'no equations/formulae appendix in source specification'})
    w(f'{out_dir}/assessment_objectives.json', {
        'schema': 'syllabai.assessment-objectives/1.0', 'id': slug,
        'source': {'pdf_sha1': parsed['source']['pdf_sha1']},
        **(aos or {'section_pages': [], 'statements': [], 'unit_weightings': []}),
        'counts': {'statements': len(aos['statements']) if aos else 0,
                   'unit_weightings': len(aos['unit_weightings']) if aos else 0},
        'flags': ao_flags,
    } if aos else {'schema': 'syllabai.assessment-objectives/1.0', 'id': slug,
                   'statements': [], 'unit_weightings': [], 'flags': ['ao-section-not-found'],
                   'counts': {'statements': 0, 'unit_weightings': 0}})
    w(f'{out_dir}/command_words.json', {
        'schema': 'syllabai.command-words/1.0', 'id': slug,
        'source': {'pdf_sha1': parsed['source']['pdf_sha1']},
        'pages': cw_pages,
        'command_words': cws,
        'counts': {'command_words': len(cws)},
        'note': None if cws else 'no command-word taxonomy table in source specification',
    })

    # update parse_report
    report['canonical_bundle'] = {
        'builder': PARSER_VERSION, 'generated': TODAY,
        'files': ['spec_points.json', 'topics.json', 'practicals.json', 'equations.json',
                  'assessment_objectives.json', 'command_words.json'],
        'counts': {
            'spec_points': sp_doc['counts']['spec_points'],
            'practicals': sp_doc['counts']['practicals'],
            'topics': tp_doc['counts']['topics'], 'subsections': tp_doc['counts']['subsections'],
            'equation_entries': sum(len(s['entries']) for s in eq_sections),
            'equations': sum(len(e['equations']) for s in eq_sections for e in s['entries']),
            'ao_statements': len(aos['statements']) if aos else 0,
            'command_words': len(cws),
        },
        'flags': sorted(set(ao_flags + eq_flags)),
    }
    w(f'{out_dir}/parse_report.json', report)
    c = report['canonical_bundle']['counts']
    print(f"OK {slug:32s} sp={c['spec_points']:3d} eq={c['equations']:3d} "
          f"ao={c['ao_statements']:2d} cw={c['command_words']:2d} "
          f"flags={len(report['canonical_bundle']['flags'])}")

if __name__ == '__main__':
    only = sys.argv[1:] if len(sys.argv) > 1 else sorted(FAMILY)
    for slug in only:
        try:
            process(slug)
        except Exception as e:
            import traceback
            print(f"FAIL {slug}: {type(e).__name__}: {e}")
            traceback.print_exc()
