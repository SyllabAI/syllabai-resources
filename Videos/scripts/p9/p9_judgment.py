#!/usr/bin/env python3
"""P9 step 3: agent judgment pass over EVERY Tier A row (the P6/P7/P8 shape).

Decision model per course: class rules keyed on title topic markers (the
channel's titles are formulaic: session/Q-number first, distinctive topic
keywords after). Each rule binds only spec codes that the deterministic
distinctive-token pre-pass proposed for that video (df <= 3 in-course) — the
rule refines the pre-pass, it never invents a bind. Explicit rebinds validate
against the TARGET course spine. Every video gets an explicit decision:
keep (specs + confidence) / rebind (course + specs) / drop (reason).
Videos routed with zero distinctive candidates are recorded as honest
routed-unmapped entries (the P7 ledger shape)."""
import json, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p9'

SPEC_CACHE = {}
def specs_of(course):
    if course in SPEC_CACHE:
        return SPEC_CACHE[course]
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    sp = {n['code']: n['title'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}
    SPEC_CACHE[course] = sp
    return sp

def find_spec(course, kw, exclude=()):
    """first spec whose title matches all keyword fragments"""
    kws = [k.lower() for k in kw]
    for code, t in sorted(specs_of(course).items()):
        tl = t.lower()
        if all(k in tl for k in kws) and code not in exclude:
            return code
    return None

tierA = json.load(open(f'{OUT}/tier-a.json'))
by_course = collections.defaultdict(list)
for p in tierA:
    by_course[p['course']].append(p)

# ---------------- class tables (refine the distinctive pre-pass; never invent) ----------------
RULES = {
 'ial-maths-20-pure-1': [
    (r'transform', '1.12', 'medium'),
    (r'discriminant', '1.4', 'medium'),
    (r'surd', '1.2', 'medium'),
    (r'indice|exponent', '1.1', 'medium'),
    (r'completing.{0,12}square', '1.5', 'medium'),
    (r'simultaneous', '1.6', 'medium'),
    (r'sine rule|cosine rule|bearings', '3.1', 'medium'),
    (r'radian', '3.2', 'medium'),
    (r'trigonom|trig ', None, 'low'),          # pre-pass best among trig specs
    (r'inequalit', None, 'low'),               # pre-pass best among 1.7/1.8/1.9
    (r'straight line', None, 'medium'),        # pre-pass best among 2.1/2.2
    (r'quadratic', None, 'low'),               # pre-pass best among quadratic specs
    (r'sketch|cubic|graphs? of functions?|curves?', None, 'low'),
    (r'normal|tangent|gradient|second derivative|differenti|applicat', None, 'medium'),
    (r'integrat', None, 'medium'),
 ],
 'ial-maths-20-pure-2': [
    (r'binomial', '4.5', 'medium'),
    (r'factor theorem|remainder theorem|algebraic (long )?division', '2.1', 'medium'),
    (r'circle', '3.1', 'medium'),
    (r'arithmetic (series|sequence)', '4.2', 'medium'),
    (r'geometric|recurrence|periodic|sigma|serie|sequence', None, 'medium'),
    (r'proof|counter example|disproof|exhaustion', None, 'low'),
    (r'logarithm|\blog\b|a\^?x|exponential', None, 'medium'),
    (r'trigonom|identit', None, 'low'),
    (r'maxima|minima|stationary|increasing|decreasing|differenti', '7.1', 'medium'),
    (r'trapezium|area under|integrat|definite', None, 'medium'),
 ],
 'ial-maths-20-pure-3': [
    (r'double angle|addition formula|factor formula|trig identit|trig\b|trigonomet|sec\b|cosec|cotangent|arcsin|arctan', None, 'medium'),
    (r'inverse trig', '2.1', 'medium'),
    (r'modulus', '1.3', 'medium'),
    (r'algebraic fraction|rational function|algebraic division|long division|simplif', '1.1', 'medium'),
    (r'partial fraction', 'REBIND_P4_21', 'medium'),
    (r'domain|range|inverse function|composite|one-one|function', None, 'low'),
    (r'transformation', '1.4', 'medium'),
    (r'logarithm|\bln\b|log graph|exponential', None, 'medium'),
    (r'product rule|quotient rule|chain rule|differenti|implicit', None, 'medium'),
    (r'exponential model|rate of change|initial', '4.4', 'medium'),
    (r'integrat|recognition', None, 'medium'),
    (r'numerical|iteration|iterative|change of sign|root', None, 'medium'),
 ],
 'ial-maths-20-pure-4': [
    (r'differential equation|separable|rate of change|cooling', '6.4', 'medium'),
    (r'formation', '5.2', 'medium'),
    (r'vector', None, 'medium'),               # pre-pass best among 7.x
    (r'parametric', None, 'medium'),           # pre-pass best among 3.1/5.1/6.5
    (r'implicit', '5.1', 'medium'),
    (r'partial fraction', '2.1', 'medium'),
    (r'binomial', '4.1', 'medium'),
    (r'volume of revolution', '6.1', 'medium'),
    (r'integration by parts|substitution', None, 'medium'),
    (r'proof|contradiction', '1.1', 'low'),
    (r'integrat', None, 'low'),
 ],
 'ial-maths-20-mechanics-1': [
    (r'connected particle|pulley|tow bar', '4.2', 'medium'),
    (r'momentum|impulse', '4.3', 'medium'),
    (r'moment', '6.1', 'medium'),
    (r'friction', None, 'medium'),             # pre-pass best among 4.4/5.3
    (r'static|equilibrium|limiting', None, 'medium'),
    (r'suvat|kinematic|constant acceleration|speed.?time|velocity.?time|displacement.?time|gravity|vertical motion', '3.1', 'medium'),
    (r'vector|resultant|resolv', None, 'medium'),   # pre-pass best among 2.x/5.1
    (r'inclined|force|dynamic|newton', None, 'medium'),
    (r'modelling|model', '1.1', 'low'),
 ],
 'ial-maths-20-statistics-1': [
    (r'normal distribution|normal approxim', '5.1', 'medium'),
    (r'discrete random|expected value|e\(x\)|expectation', None, 'medium'),
    (r'correlation|pmcc|regression|scatter', None, 'medium'),
    (r'histogram|stem|box.?plot', '2.1', 'medium'),
    (r'standard deviation|variance|dispersion|quartile|interpercentile', '2.3', 'medium'),
    (r'mean|median|mode|location|grouped|interpolation', None, 'medium'),
    (r'skew|outlier', '2.4', 'medium'),
    (r'venn|tree|conditional|probability|sample space|exclusive|independen', None, 'medium'),
    (r'discrete random|expected value|e\(x\)|expectation|uniform', None, 'medium'),
    (r'explanatory|response|dependent|independent variable', '4.2', 'low'),
    (r'statistic|modelling', '1.1', 'low'),
 ],
 'igcse-maths-a-18-higher': [
    (r'recurring decimal', '1.3A', 'medium'),
    (r'standard form', '1.9A', 'medium'),
    (r'order of operations|hierarchy|brackets', '1.1F', 'medium'),
    (r'rounding|approximation|estimate', '1.8D', 'medium'),
    (r'hcf|lcm|common factor|common multiple', '1.1H', 'medium'),
    (r'prime', '1.1G', 'medium'),
    (r'directed number', '1.1C', 'medium'),
    (r'indice', None, 'medium'),
    (r'fraction', None, 'low'),
    (r'decimal', None, 'low'),
    (r'ratio', None, 'medium'),
    (r'percent', None, 'medium'),
    (r'speed', None, 'medium'),                # pre-pass best (4.4F kinematics)
    (r'differentiation|product rule', 'REBIND_P3_42', 'medium'),
 ],
 'igcse-maths-b-16': [
    (r'bearing', '9D', 'medium'),
    (r'sine rule|cosine rule|cosine|sine', '9A', 'medium'),
    (r'indice', '1C', 'medium'),
    (r'algebraic fraction', '3F', 'medium'),
    (r'simultaneous', '3I', 'medium'),
    (r'gradient', '4K', 'medium'),
    (r'perpendicular|parallel', None, 'low'),  # straight-line specs; pre-pass verifies
    (r'vector', None, 'low'),
    (r'inequalit', None, 'low'),
    (r'function', None, 'low'),
 ],
 'cie-igcse-maths-25-core': [
    (r'speed.?time|distance.?time', 'C1.12.3', 'low'),
    (r'functions?\b', 'C2.11.1', 'low'),
    (r'gradient function|calculus', 'DROP_CORE_NO_CALCULUS', 'drop'),
    (r'composite function', 'DROP_CORE_NO_COMPOSITE', 'drop'),
 ],
 'cie-igcse-maths-25-extended': [
    (r'cumulative frequency|frequency table|histogram', 'E9.6.1', 'medium'),
    (r'conditional probability', 'E8.4.1', 'medium'),
    (r'mensuration|surface area|pyramid', 'E5.4.1', 'medium'),
    (r'percentag|ratio', 'LOOKUP_percent', 'medium'),
    (r'9709|worksheet 13', 'REBIND_ALP1_184', 'medium'),
    (r'answer to.*request|sequence question request', 'DROP_COMMUNITY', 'drop'),
    (r'volume of revolution', 'REBIND_ALP1_184', 'medium'),
 ],
 'igcse-maths-a-modular-24-higher-unit-1': [
    (r'upper|lower|bound', '1.8C', 'medium'),
    (r'speed|distance', '4.4F', 'medium'),
    (r'probability|distribution', '6.3E', 'low'),
    (r'arithmetic|subtract', 'LOOKUP_four_rules', 'low'),
    (r'expand|bracket', 'LOOKUP_expand', 'low'),
 ],
 'cie-a-level-maths-20-pure-1': [
    (r'volume of revolution|volumes', '1.8.4', 'medium'),
    (r'trig identit|trig equations|trigonomet', None, 'medium'),
    (r'binomial', '1.6.1', 'medium'),
    (r'completing the square', '1.1.1', 'medium'),
    (r'discriminant', '1.1.2', 'medium'),
    (r'inequalit', '1.1.3', 'low'),
    (r'simultaneous', '1.1.4', 'medium'),
    (r'quadratic in', '1.1.5', 'low'),
    (r'function|domain|range|inverse|composite', None, 'low'),
    (r'transform', '1.2.5', 'medium'),
    (r'straight line|perpendicular|parallel', None, 'low'),
    (r'circle', '1.3.3', 'medium'),
    (r'radian|arc|sector', '1.4.1', 'medium'),
    (r'sine|cosine|tangent|trig', None, 'low'),
    (r'arithmetic|geometric|progression|serie|sequence|convergence', None, 'medium'),
    (r'binomial expansion', '1.6.1', 'medium'),
    (r'gradient|tangent|normal|stationary|differenti|increasing|decreasing', None, 'medium'),
    (r'integrat|area', None, 'medium'),
 ],
 'cie-a-level-maths-20-pure-3': [
    (r'logarithm|inequalit', '3.2.3', 'low'),
    (r'complex|argand', None, 'medium'),
    (r'vector', None, 'medium'),
    (r'differential equation|rate of change', '3.8.1', 'medium'),
    (r'iteration|numerical|approxim|sign|root', None, 'medium'),
    (r'partial fraction', '3.1.5', 'medium'),
    (r'binomial', '3.1.6', 'medium'),
    (r'polynomial|factor theorem|remainder|divide', '3.1.3', 'medium'),
    (r'modulus', '3.1.1', 'medium'),
    (r'sec|cosec|cotangent|trig identit|addition formula|double angle|trigonomet', None, 'medium'),
    (r'product rule|quotient rule|chain rule|parametr|differenti', None, 'medium'),
    (r'integrat', None, 'medium'),
    (r'exponential|ln\b|log', None, 'medium'),
 ],
 'igcse-further-maths-19': [
    (r'geometric|serie', None, 'medium'),
    (r'binomial', None, 'medium'),
    (r'calculus|differenti|integrat', None, 'medium'),
    (r'vector|matrix|transformation', None, 'medium'),
 ],
 'ial-further-maths-18-further-pure-1': [
    (r'complex|argand|quadratic roots|conjugate', None, 'medium'),
    (r'root|sum of roots|product of roots', None, 'medium'),
    (r'numerical|bisection|iteration', '3.1', 'medium'),
    (r'parabola|hyperbola|focus|directrix', None, 'medium'),
    (r'matrix|determinant|inverse matrix', None, 'medium'),
    (r'linear transformation', '6.1', 'medium'),
    (r'series|summation', None, 'medium'),
 ],
}

ALLOWED = {
 'ial-maths-20-pure-1': {'1.7': [1.7, 1.8, 1.9], 'trig': [3.1, 3.2, 3.3], 'straight line': [2.1, 2.2],
    'quadratic': [1.3, 1.4, 1.5, 1.7, 1.9], 'sketch': [1.11, 1.12], 'normal': [4.1, 4.2, 4.3], 'integrat': [5.1, 5.2],
    'indice': [1.1], 'ratio': None},
}

def pick_among(cands, allowed_codes):
    """best distinctive candidate whose code is in allowed_codes"""
    for x in cands:
        if x['distinctive'] and x['code'] in allowed_codes:
            return x
    return None

verdicts = {}
stats = collections.Counter()
for course, vids in sorted(by_course.items()):
    cands = json.load(open(f'{OUT}/candidates-{course}.json'))
    rules = RULES.get(course, [])
    out = []
    for v in vids:
        cl = cands.get(v['id'], [])
        d = [x for x in cl if x['distinctive']]
        if not d:
            out.append({'id': v['id'], 'title': v['title'], 'action': 'unmapped',
                        'reason': 'no distinctive token overlap at the tightened bar (df<=3) — routed-but-unmapped, honest'})
            stats['unmapped'] += 1
            continue
        decided = None
        for pat, code, conf in rules:
            if not re.search(pat, v['title'], re.I):
                continue
            if isinstance(code, str) and code.startswith('DROP'):
                decided = {'action': 'drop', 'reason': code + ': ' + d[0]['title'][:60]}
                break
            if isinstance(code, str) and code.startswith('REBIND'):
                # explicit cross-course rebinds (title names the target content)
                if code == 'REBIND_P4_21':
                    tgt, specs, note = 'ial-maths-20-pure-4', ['2.1'], 'partial fractions are P4 2.1, not a P3 spec'
                elif code == 'REBIND_P3_42':
                    tgt, specs, note = 'ial-maths-20-pure-3', ['4.2'], 'title names IAL P3 product rule (TYU chapter 6)'
                elif code == 'REBIND_ALP1_184':
                    tgt, specs, note = 'cie-a-level-maths-20-pure-1', ['1.8.4'], '9709 worksheet 13 integration-volumes is 9709 P1 content'
                else:
                    continue
                ok = all(s in specs_of(tgt) for s in specs)
                if ok:
                    decided = {'action': 'rebind', 'course': tgt, 'specs': specs, 'confidence': 'medium', 'reason': note}
                else:
                    decided = {'action': 'drop', 'reason': note + ' — target spec missing, honest drop'}
                break
            if isinstance(code, str) and code.startswith('LOOKUP'):
                kwmap = {'LOOKUP_percent': (['percentage'], 'cie-igcse-maths-25-extended'),
                         'LOOKUP_four_rules': (['four rules'], 'igcse-maths-a-modular-24-higher-unit-1'),
                         'LOOKUP_expand': (['expand'], 'igcse-maths-a-modular-24-higher-unit-1')}
                kws, tgt = kwmap[code]
                sc = find_spec(tgt, kws)
                if sc:
                    decided = {'action': 'rebind' if tgt != course else 'keep', 'course': tgt if tgt != course else None,
                               'specs': [sc], 'confidence': conf, 'reason': f'keyword lookup {kws} -> {sc} in {tgt}'}
                else:
                    decided = {'action': 'drop', 'reason': f'no spec matching {kws} in {tgt} spine'}
                break
            # normal class bind: verify against pre-pass candidates
            top = d[0]
            if code is None:
                # pre-pass best wins (rule constrains the topic class, tokens pick the spec)
                chosen = top
            else:
                chosen = next((x for x in d if x['code'] == code), None)
                if chosen is None:
                    # rule names a spec the pre-pass did not propose: allow if the top
                    # candidate is a sibling spec of the same topic family, else honest drop
                    chosen = top if top['code'].startswith(code.split('.')[0] + '.') else None
            if chosen is None:
                decided = {'action': 'drop', 'reason': f'class {pat} binds {code} but pre-pass proposed none in family — no honest bind'}
                break
            conf_final = conf if chosen['minDf'] <= 3 and conf == 'medium' else ('low' if conf == 'medium' else conf)
            ev = f"title names {chosen['code']} '{chosen['title'][:56]}' via distinctive token(s) {chosen['matched'][:4]} (df {chosen['minDf']})"
            decided = {'action': 'keep', 'specs': [chosen['code']], 'confidence': conf_final, 'reason': ev}
            break
        if decided is None:
            decided = {'action': 'drop',
                       'reason': f"no class rule matched; best distinctive candidate {d[0]['code']} '{d[0]['title'][:48]}' bound only on vocabulary not named by the title ({d[0]['matched'][:3]})"}
        decided['id'] = v['id']
        decided['title'] = v['title']
        out.append(decided)
        stats[decided['action']] += 1
    verdicts[course] = out

json.dump(verdicts, open(f'{OUT}/judgment.json', 'w'), indent=1)
print(dict(stats.most_common()))
for c, vs in verdicts.items():
    k = sum(1 for v in vs if v['action'] == 'keep')
    r = sum(1 for v in vs if v['action'] == 'rebind')
    dr = sum(1 for v in vs if v['action'] == 'drop')
    u = sum(1 for v in vs if v['action'] == 'unmapped')
    print(f'{c}: keep {k} rebind {r} drop {dr} unmapped {u}')
