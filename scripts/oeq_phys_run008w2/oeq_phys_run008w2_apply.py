#!/usr/bin/env python3
"""run-008 W2 executor — T-OEQ-PHYS-FORMAT-1 (F129).

R1+R3 in the resources corpus, page-evidence law, questions.md regen rides.
Phases: preflight | apply | regen | gates | report
Run from /tmp/rrepo on branch t-oeq-phys-format-1-run008-w2.
"""
import json, sys, re, hashlib, shutil
from pathlib import Path

ROOT = Path('/tmp/rrepo')
TRANS = json.load(open('/home/z/my-project/scripts/run008/w2_transforms.json'))
OLD_BLOCKS = json.load(open('/home/z/my-project/scripts/run008/r1_old_blocks.json'))
PLANE_VALS = json.load(open('/home/z/my-project/scripts/run008/r4_plane_values.json'))
REPORT = {'preflight': {}, 'applied': [], 'regen': [], 'gates': {}, 'pins': []}

def sha(b): return hashlib.sha256(b).hexdigest()

def g3_ok(s):
    for ch in s:
        o = ord(ch)
        if 0xE000 <= o <= 0xF8FF: return False
        if o == 0xFFFD: return False
        if o < 0x20 and o not in (0x09, 0x0A, 0x0D): return False
        if o == 0x7F: return False
    return True

def t1_dumps(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False)

SME_PREFIX = 'SME-ExamQuestion/igcse-physics-19/'

def load_topic(rel):
    if not rel.startswith(('SME-', 'Official-')):
        rel = SME_PREFIX + rel
    p = ROOT / rel
    return json.loads(p.read_text(encoding='utf-8')), p

def write_topic(p, topic):
    p.write_text(t1_dumps(topic), encoding='utf-8')  # T1: no trailing newline

def find_sme_part(rel, pid):
    topic, p = load_topic(rel)
    for q in topic['questions']:
        for part in q['parts']:
            if part['id'] == pid:
                return topic, p, q, part
    raise SystemExit(f'FATAL: pid {pid} not found in {rel}')

# ---------------- preflight ----------------
def preflight():
    ok = True
    # T1 round-trip on every touched topic.json
    targets = sorted(SME_PREFIX + t['file'] for t in TRANS['transforms']['sme_r1'])
    r4_files = []
    # locate R4 files
    for rel in ROOT.glob('SME-ExamQuestion/igcse-physics-19/*/*/topic.json'):
        s = None
    for pid in ('qstnprt_JHSpcZfPW7RxDt6t', 'qstnprt_qq3VPGgCZtyWTqzV'):
        hit = None
        for tj in ROOT.glob('SME-ExamQuestion/igcse-physics-19/*/*/topic.json'):
            if pid in tj.read_text(encoding='utf-8'):
                hit = SME_PREFIX + str(tj.relative_to(ROOT / SME_PREFIX)); break
        if not hit: raise SystemExit(f'R4 pid {pid} not found in corpus')
        r4_files.append(hit)
    REPORT['preflight']['r4_files'] = r4_files
    all_files = sorted(set(targets + r4_files))
    for rel in all_files:
        raw = (ROOT / rel).read_bytes()
        rt = t1_dumps(json.loads(raw)).encode('utf-8')
        good = rt == raw
        REPORT['preflight'][f't1:{rel}'] = good
        if not good:
            ok = False
            print(f'T1 FAIL: {rel}')
    # official T1
    off_files = sorted({t['file'] for t in TRANS['transforms']['official_r3']})
    for rel in off_files:
        raw = (ROOT / rel).read_bytes()
        rt = t1_dumps(json.loads(raw)).encode('utf-8')
        good = rt == raw
        REPORT['preflight'][f't1:{rel}'] = good
        if not good: ok = False; print(f'T1 FAIL: {rel}')
    # old blocks present & unique in fields and questions.md
    for t in TRANS['transforms']['sme_r1']:
        pid = t['pid']
        olds = OLD_BLOCKS[pid]
        rel = SME_PREFIX + t['file']
        _, _, _, part = find_sme_part(rel, pid)
        field = part['problem_md']
        for i, blk in enumerate(olds):
            n = field.count('\n'.join(blk))
            if n != 1:
                ok = False; print(f'BLOCK COUNT {n} for {pid} blk{i} in field')
        qmd = (ROOT / rel).parent / 'questions.md'
        qtext = qmd.read_text(encoding='utf-8')
        for i, blk in enumerate(olds):
            n = qtext.count('\n'.join(blk))
            if n != 1:
                ok = False; print(f'QMD BLOCK COUNT {n} for {pid} blk{i}')
    REPORT['preflight']['ok'] = ok
    print('PREFLIGHT', 'OK' if ok else 'FAILED')
    return ok

# ---------------- apply ----------------
def apply():
    n = 0
    # SME R1
    for t in TRANS['transforms']['sme_r1']:
        pid = t['pid']; rel = SME_PREFIX + t['file']
        topic, p, q, part = find_sme_part(rel, pid)
        field = part['problem_md']
        before = sha(field.encode())
        olds = OLD_BLOCKS[pid]
        news = [t[k] for k in ('new', 'new2', 'new3') if k in t]
        assert len(news) == len(olds), f'{pid}: {len(news)} new vs {len(olds)} old'
        done = all('\n'.join(blk) not in field for blk in olds) and all(x in field for x in news)
        if done:
            continue  # idempotent re-entry: already applied in a prior pass
        for blk, new in zip(olds, news):
            old_txt = '\n'.join(blk)
            assert field.count(old_txt) == 1, f'{pid} field count'
            field = field.replace(old_txt, new)
        assert g3_ok(field), f'G3 fail {pid}'
        part['problem_md'] = field
        write_topic(p, topic)
        REPORT['applied'].append({'pid': pid, 'file': rel, 'field': 'problem_md',
                                  'before': before, 'after': sha(field.encode())})
        n += 1
    # SME R4 mirror
    for t in TRANS['transforms']['sme_r4_mirror']:
        pid = t['pid']
        rel = None
        for tj in ROOT.glob('SME-ExamQuestion/igcse-physics-19/*/*/topic.json'):
            if pid in tj.read_text(encoding='utf-8'):
                rel = SME_PREFIX + str(tj.relative_to(ROOT / SME_PREFIX)); break
        topic, p, q, part = find_sme_part(rel, pid)
        field = part['problem_md']
        before = sha(field.encode())
        target = PLANE_VALS[pid]
        if field == target:
            continue  # already mirrored
        if pid == 'qstnprt_JHSpcZfPW7RxDt6t':
            old_row = '| `U _ 92 ^ 234` | `U _ 92 ^ 235` | $Pu_{94}^{238}$ | $Am_{95}^{238}$ |'
            new_row = next(l for l in target.split('\n') if l.startswith('| ${'))  # the KaTeX table row
            assert field.count(old_row) == 1
            cand = field.replace(old_row, new_row)
        else:
            assert field.count('$\\text{square}$') == 1
            cand = field.replace('$\\text{square}$', '$\\square$')
        if cand != target:
            # show first divergence for diagnosis, then fail-closed
            for i, (a, b) in enumerate(zip(cand, target)):
                if a != b:
                    print(f'R4 MISMATCH at {i}: {cand[i-40:i+40]!r} vs {target[i-40:i+40]!r}')
                    break
            raise SystemExit(f'FATAL: R4 mirror does not reconcile for {pid}')
        assert g3_ok(cand)
        part['problem_md'] = cand
        write_topic(p, topic)
        REPORT['applied'].append({'pid': pid, 'file': rel, 'field': 'problem_md (R4 mirror)',
                                  'before': before, 'after': sha(cand.encode())})
        n += 1
    # Official R3
    OFF = {
      'offp_2024-06_1p_2-a': ('Official-ExamQuestion/igcse-physics-19/2024-06/4PH1-1P/topic.json', 2, '2(a)'),
      'offp_2021-11_2p_1-b': ('Official-ExamQuestion/igcse-physics-19/2021-11/4PH1-2P/topic.json', 1, '1(b)'),
      'offp_2022-01_1p_1-a': ('Official-ExamQuestion/igcse-physics-19/2022-01/4PH1-1P/topic.json', 1, '1(a)'),
    }
    for pid, (rel, qn, pnum) in OFF.items():
        t = next(x for x in TRANS['transforms']['official_r3'] if x['part'] == pid)
        topic, p = load_topic(rel)
        q = next(q for q in topic['questions'] if q['question_number'] == qn)
        part = next(x for x in q['parts'] if x['part_number'] == pnum)
        before = sha((part['problem_md'] or '').encode())
        if part['problem_md'] == t['problem_md']:
            continue  # already applied
        part['problem_md'] = t['problem_md']
        for c in part.get('choices') or []:
            c['text_md'] = ''
        act = t['assets']
        if act == 'drop':
            removed = [a for a in (part.get('assets') or []) if a.get('id') == 'asset_2_a_table']
            assert len(removed) == 1, f'{pid}: asset entry not found'
            part['assets'] = [a for a in part.get('assets') or [] if a.get('id') != 'asset_2_a_table']
            REPORT['applied'].append({'part': pid, 'asset_dropped': 'asset_2_a_table (file kept on disk)'})
        elif act == 'add':
            crop_src = Path('/tmp/physrun/off/crop_final.png')
            assert crop_src.exists(), 'final crop missing'
            adir = (ROOT / rel).parent / 'assets'
            shutil.copy(crop_src, adir / 'asset_1_a_diagram_choices.png')
            part['assets'] = [{
                'id': 'asset_1_a_diagram_choices', 'kind': 'crop',
                'mention': 'magnetic field diagrams — options A to D',
                'source': 'qp.pdf', 'page': 3, 'review': False,
                'path': 'assets/asset_1_a_diagram_choices.png',
                'render': 'raster', 'text_coverage': 0.0,
                'manual_crop': True, 'review_verdict': 'run008-w2 page-evidenced',
                'shared': False, 'ref_part': 'asset_1_a_diagram_choices'}]
        part['edit_status'] = 'repaired:run008-w2-f129'
        vt = part.get('value_trace') or {}
        vt['table'] = 'run008-w2 page-evidenced (qp.pdf print, eyes-on)'
        vt['choices'] = 'letter-only: option content lives in the stem (table/diagrams); labels+key unchanged'
        part['value_trace'] = vt
        for fld in ('problem_md',):
            assert g3_ok(part[fld]), f'G3 fail {pid}'
        write_topic(p, topic)
        REPORT['applied'].append({'part': pid, 'file': rel, 'field': 'problem_md+choices+assets+edit_status',
                                  'before': before, 'after': sha(part['problem_md'].encode())})
        n += 1
    print(f'APPLIED {n} edits')

# ---------------- regen ----------------
def write_questions_md_official(topic, path):
    out = [f"# {topic['paper_info']['code']} — {topic['source']['series']} (official extraction)",
           "", f"> schema `{topic['schema']}` · paper_id `{topic['paper_id']}` · "
               f"qp sha256 `{topic['source']['qp_sha256'][:16]}…` · extraction is the disclosed baseline (ADR-039)", ""]
    for q in topic["questions"]:
        out.append(f"## Question {q['question_number']} ({q['total_marks']} marks)")
        if q["stem_md"]:
            out += ["", q["stem_md"], ""]
        for g, gv in (q.get("groups") or {}).items():
            if gv.get("group_stem_md"):
                out += [f"**({g})** {gv['group_stem_md']}", ""]
            if gv.get("option_list"):
                out += [f"- {lab}" for lab in gv["option_list"]] + [""]
        for p in q["parts"]:
            marks = f"[{p['marks']}]" if p.get("marks") is not None else "[?]"
            out.append(f"### {p['part_number']} {marks}")
            out += ["", p["problem_md"], ""]
            if p.get("choices"):
                out += [f"- **({c['label']})** {c['text_md']}" + ("  ✔" if c.get("is_correct") else "")
                        for c in p["choices"]] + [""]
            for a in p.get("assets") or []:
                if a.get("kind") == "crop" and a.get("path"):
                    cap = f"{a['mention']} — official paper figure (qp.pdf p.{a['page']})"
                    if a.get("shared"):
                        cap += f" — shared with {a.get('ref_part', '?')}"
                    out += [f"![{cap}]({a['path']})", ""]
                else:
                    out += [f"> 🖼 crop required: {a['mention']} (qp.pdf p.{a['page']})", ""]
            if p.get("solution_md"):
                out += ["", "**Mark scheme answer**", ""]
                out += ["> " + ln for ln in p["solution_md"].splitlines()]
                out += [""]
                for pt in p.get("mark_points") or []:
                    out += [f"- **({pt['marks']})** {pt['text_md'].splitlines()[0]}"]
                out += [""]
        out.append("")
    path.write_text("\n".join(out))

def regen():
    # fidelity test on an untouched official paper
    probe = ROOT / 'Official-ExamQuestion/igcse-physics-19/2019-06/4PH1-1P'
    topic = json.loads((probe / 'topic.json').read_text(encoding='utf-8'))
    rendered = "\n".join([])  # placeholder
    import io
    from contextlib import redirect_stdout
    # render to temp path
    tmp = Path('/tmp/physrun/render_probe.md')
    class P:
        def write_text(self, s, encoding=None): tmp.write_text(s, encoding='utf-8')
    write_questions_md_official(topic, P())
    head = probe / 'questions.md'
    same = tmp.read_text(encoding='utf-8') == head.read_text(encoding='utf-8')
    REPORT['regen'].append({'official_renderer_fidelity_2019-06_1P': same})
    print('official renderer fidelity (untouched 2019-06 1P):', same)
    if not same:
        # diff head
        a = head.read_text(encoding='utf-8').splitlines()
        b = tmp.read_text(encoding='utf-8').splitlines()
        import difflib
        d = list(difflib.unified_diff(a, b, lineterm=''))[:30]
        print('\n'.join(d))
        raise SystemExit('FATAL: official renderer not byte-faithful — surgical fallback required (not implemented; aborting)')
    for rel in ['Official-ExamQuestion/igcse-physics-19/2024-06/4PH1-1P',
                'Official-ExamQuestion/igcse-physics-19/2021-11/4PH1-2P',
                'Official-ExamQuestion/igcse-physics-19/2022-01/4PH1-1P']:
        d = ROOT / rel
        topic = json.loads((d / 'topic.json').read_text(encoding='utf-8'))
        before = sha((d / 'questions.md').read_bytes())
        write_questions_md_official(topic, d / 'questions.md')
        after = sha((d / 'questions.md').read_bytes())
        REPORT['regen'].append({'file': f'{rel}/questions.md', 'before': before, 'after': after})
        print('regen', rel)
    # SME surgical
    for t in TRANS['transforms']['sme_r1']:
        rel = SME_PREFIX + t['file']; pid = t['pid']
        olds = OLD_BLOCKS[pid]
        news = [t[k] for k in ('new', 'new2', 'new3') if k in t]
        qmd = (ROOT / rel).parent / 'questions.md'
        txt = qmd.read_text(encoding='utf-8')
        before = sha(txt.encode())
        done = all('\n'.join(blk) not in txt for blk in olds) and all(x in txt for x in news)
        if not done:
            for blk, new in zip(olds, news):
                old_txt = '\n'.join(blk)
                assert txt.count(old_txt) == 1, f'qmd count fail {pid}'
                txt = txt.replace(old_txt, new)
            qmd.write_text(txt, encoding='utf-8')
            REPORT['regen'].append({'file': f'{rel.replace("topic.json","questions.md")}', 'pid': pid,
                                    'mode': 'surgical', 'before': before, 'after': sha(txt.encode())})
    for t in TRANS['transforms']['sme_r4_mirror']:
        pid = t['pid']
        # locate file
        rel = None
        for tj in ROOT.glob('SME-ExamQuestion/igcse-physics-19/*/*/topic.json'):
            if pid in tj.read_text(encoding='utf-8'):
                rel = SME_PREFIX + str(tj.relative_to(ROOT / SME_PREFIX)); break
        qmd = (ROOT / rel).parent / 'questions.md'
        txt = qmd.read_text(encoding='utf-8')
        before = sha(txt.encode())
        if pid == 'qstnprt_JHSpcZfPW7RxDt6t':
            old_row = '| `U _ 92 ^ 234` | `U _ 92 ^ 235` | $Pu_{94}^{238}$ | $Am_{95}^{238}$ |'
            new_row = next(l for l in PLANE_VALS[pid].split('\n') if l.startswith('| ${'))
            if old_row in txt:
                assert txt.count(old_row) == 1
                txt = txt.replace(old_row, new_row)
                qmd.write_text(txt, encoding='utf-8')
        else:
            if '$\\text{square}$' in txt:
                assert txt.count('$\\text{square}$') == 1
                txt = txt.replace('$\\text{square}$', '$\\square$')
                qmd.write_text(txt, encoding='utf-8')
        REPORT['regen'].append({'file': f'{rel.replace("topic.json","questions.md")}', 'pid': pid,
                                'mode': 'surgical-r4', 'before': before, 'after': sha(txt.encode())})
    print('REGEN done')

# ---------------- gates ----------------
PIPE_ROW = re.compile(r'^\s*\|.*\|\s*$')
def is_delim(line):
    body = line.strip().strip('|')
    if body == '' and '|' not in line.strip(): return False
    for cell in body.split('|'):
        c = cell.strip().replace('<br>', '').replace('<br/>', '')
        if re.search(r'[a-zA-Z0-9]', c): return False
        if not re.fullmatch(r':?-+:?', c): return False
    return True
def cells_of(line): return [c.strip() for c in line.strip().strip('|').split('|')]
def classify(rows):
    delim = [i for i, r in enumerate(rows) if is_delim(r)]
    if not delim: return 'NO_DELIM'
    d = delim[0]
    if len(cells_of(rows[d])) == 1: return '1COL_DEGENERATE'
    if len(cells_of(rows[d])) != len(cells_of(rows[0])): return 'COLS_MISMATCH'
    return 'MULTI_COL_OK'
def census_text(text):
    out = []
    cur = []
    for ln in text.split('\n'):
        if PIPE_ROW.match(ln): cur.append(ln)
        else:
            if cur: out.append(classify(cur)); cur = []
    if cur: out.append(classify(cur))
    return out

def math_pipe(text):
    i, n = 0, len(text)
    while i < n:
        if text[i] == '$':
            if i+1 < n and text[i+1] == '$':
                j = text.find('$$', i+2); i = (j+2) if j != -1 else n; continue
            j = text.find('$', i+1)
            if j == -1: break
            if '|' in text[i+1:j]: return True
            i = j+1
        else: i += 1
    return False

def gates():
    from collections import Counter
    # SME corpus census
    cnt = Counter(); mp = 0
    for tj in ROOT.glob('SME-ExamQuestion/igcse-physics-19/*/*/topic.json'):
        t = json.loads(tj.read_text(encoding='utf-8'))
        for q in t['questions']:
            for p in q['parts']:
                for f in ('problem_md', 'solution_md'):
                    txt = p.get(f) or ''
                    if math_pipe(txt): mp += 1
                    for cls in census_text(txt): cnt[cls] += 1
    REPORT['gates']['sme_census'] = dict(cnt)
    REPORT['gates']['sme_math_pipe'] = mp
    exp = TRANS['post_gate_expectation']['sme_census']
    ok = cnt['1COL_DEGENERATE'] == exp['1COL_DEGENERATE_blocks'] and cnt['MULTI_COL_OK'] == exp['MULTI_COL_OK_blocks'] and mp == 0
    # official corpus census (3 touched papers + all)
    ocnt = Counter(); omp = 0
    for tj in ROOT.glob('Official-ExamQuestion/igcse-physics-19/*/*/topic.json'):
        t = json.loads(tj.read_text(encoding='utf-8'))
        for q in t['questions']:
            texts = [q.get('stem_md') or ''] + [p.get('problem_md') or '' for p in q['parts']]
            for txt in texts:
                if math_pipe(txt): omp += 1
                for cls in census_text(txt): ocnt[cls] += 1
    REPORT['gates']['official_census'] = dict(ocnt)
    REPORT['gates']['official_math_pipe'] = omp
    oexp = TRANS['post_gate_expectation']['official_corpus_census']
    ok = ok and ocnt['1COL_DEGENERATE'] == 0 and ocnt['MULTI_COL_OK'] == oexp['MULTI_COL_OK_blocks'] and omp == 0
    # G3 sweep over all written files
    g3 = True
    for rel in REPORT['preflight'].get('r4_files', []) + sorted({t['file'] for t in TRANS['transforms']['sme_r1']}):
        pass
    for tj in list(ROOT.glob('SME-ExamQuestion/igcse-physics-19/*/*/topic.json')) + \
              list(ROOT.glob('Official-ExamQuestion/igcse-physics-19/*/*/topic.json')):
        t = json.loads(tj.read_text(encoding='utf-8'))
        s = json.dumps(t, ensure_ascii=False)
        if not g3_ok(s): g3 = False; print('G3 FAIL', tj)
    REPORT['gates']['g3_all_values'] = g3
    ok = ok and g3
    # pins
    for a in REPORT['applied']:
        if 'pid' in a or 'part' in a:
            REPORT['pins'].append({'target': a.get('pid') or a.get('part'), 'file': a.get('file'),
                                   'before_sha256': a.get('before'), 'after_sha256': a.get('after')})
    REPORT['gates']['ok'] = ok
    print('GATES', 'GREEN' if ok else 'RED')
    return ok

if __name__ == '__main__':
    phase = sys.argv[1]
    if phase == 'preflight':
        sys.exit(0 if preflight() else 1)
    elif phase == 'apply':
        apply()
    elif phase == 'regen':
        regen()
    elif phase == 'gates':
        sys.exit(0 if gates() else 1)
    elif phase == 'report':
        Path('/tmp/physrun/w2_report.json').write_text(json.dumps(REPORT, indent=1, ensure_ascii=False))
        print(json.dumps({'gates': REPORT['gates'], 'applied_n': len(REPORT['applied']),
                          'regen_n': len(REPORT['regen'])}, indent=1))
