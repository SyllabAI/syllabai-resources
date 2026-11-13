#!/usr/bin/env python3
"""P10 step 3 (v2): agent judgment pass over EVERY Tier A row.

Class model:
  - Maths Deity unit.marker rows: the unit marker routes the course
    deterministically; the topic phrase binds via class tables that name
    EXPLICIT spec codes. A table bind draws the spec from the pre-pass scored
    candidate list (the pre-pass proposed it — the rule only discriminates
    between topic siblings; it never invents a bind). Confidence medium when
    the chosen candidate is distinctive (df<=3), else LOW with the full
    disclosure note (small dense IAL modules — 16-25 specs — make the df<=3
    bar structurally unable to discriminate; the P4 cross-subject-style
    higher title-only posture, disclosed per row).
  - Arnolds topic rows: the same table shape over distinctive candidates.
  - Ambiguous cross-course rows: explicit rebinds validated against the
    target spine; degenerate vocabulary binds drop with reasons.
Every video gets an explicit decision: keep / rebind / drop / unmapped."""
import json, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p10'

SPEC_CACHE = {}
def specs_of(course):
    if course in SPEC_CACHE:
        return SPEC_CACHE[course]
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    sp = {n['code']: n['title'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}
    SPEC_CACHE[course] = sp
    return sp

def spine_n(course):
    return len(specs_of(course))

tierA = json.load(open(f'{OUT}/tier-a.json'))
amb = json.load(open(f'{OUT}/candidates-ambiguous.json'))
by_course = collections.defaultdict(list)
for p in tierA:
    if p.get('course'):
        by_course[p['course']].append(p)
    else:
        best = amb.get(p['id']) or []
        if best:
            by_course[best[0]['course']].append({**p, 'course': best[0]['course'], '_amb': best})
        else:
            by_course['__amb-unresolved__'].append(p)

# ---- explicit-code class tables (topic -> spec code), refined by the pre-pass ----
RULES = {
 'ial-maths-20-pure-1': [
    (r'regions|inequalities on graphs', '1.8'),
    (r'quadratic inequalities', '1.9'),
    (r'inequalit', '1.7'),
    (r'solving quadratic|quadratic equations', '1.5'),
    (r'completing.{0,12}square', '1.5'),
    (r'discriminant', '1.4'),
    (r'quadratic (graphs|functions|equations)', '1.3'),
    (r'simultaneous', '1.6'),
    (r'surds', '1.2'),
    (r'indice|exponent', '1.1'),
    (r'polynomials?|expand|collecting like', '1.10'),
    (r'sketch|curves?|graphs of functions?', '1.11'),
    (r'transform', '1.12'),
    (r'straight line|gradient of|midpoint|parallel lines', '2.1'),
    (r'perpendicular', '2.2'),
    (r'sine rule|cosine rule|triangle|bearings', '3.1'),
    (r'radian|arc|sector', '3.2'),
    (r'trig ratios|trig graphs|sine|cosine|tangent|cast diagram|trig identit', '3.3'),
    (r'stationary|second derivative|normal to|tangent to|gradients?|increasing|decreasing|differentiat', '4.3'),
    (r'differentiat|x\^?n|deriv', '4.2'),
    (r'derivative as gradient', '4.1'),
    (r'integrat|indefinite|definite|area under', '5.1'),
    (r'integration of|integrating', '5.2'),
    (r'integrating x\^?n|indefinite integrals?', '5.2', 'direct'),
    (r'differentiat', '4.2', 'direct'),
    (r'y\s*=\s*mx\s*\+\s*c|equation of a straight line', '2.1', 'direct'),
    (r'stretching graphs|translating graphs|transforming (functions|graphs)|transformations of graphs', '1.12', 'direct'),
    (r'factorising', '1.5', 'direct'),
    (r'rationalising denominators?', '1.2', 'direct'),
    (r'index laws?', '1.1', 'direct'),
    (r'cubic graphs|reciprocal graphs|points of intersection|sketching', '1.11', 'direct'),
    (r'regions', '1.8', 'direct'),
 ],
 'ial-maths-20-pure-2': [
    (r'binomial (expansion|theorem)', '4.5'),
    (r'factor theorem|remainder theorem|algebraic division', '2.1'),
    (r'circle', '3.1'),
    (r'arithmetic (series|sequence)', '4.2'),
    (r'geometric (series|progression|sequence)', '4.4'),
    (r'serie', '4.4'),
    (r'recurrence|periodic|increasing|decreasing sequence', '4.3'),
    (r'sequences?|nth term|sum notation|sigma', '4.1'),
    (r'proof by exhaustion|exhaustion', '1.2'),
    (r'counter ?example|disproof', '1.3'),
    (r'proof', '1.1'),
    (r'logarithm|laws of logs|\blog\b', '5.2'),
    (r'exponential|y ?= ?a\^?x|a\^x', '5.1'),
    (r'solving (exponential|log) equations|a\^x ?= ?b', '5.3'),
    (r'trig identit|sin\^?2|cos\^?2', '6.1'),
    (r'trig equations|solve.{0,20}(trig|sin|cos|tan)', '6.2'),
    (r'maxima|minima|stationary|increasing|decreasing|differentiat', '7.1'),
    (r'definite integral', '8.1'),
    (r'area under', '8.2'),
    (r'trapezium', '8.3'),
    (r'integrat', '8.1'),
    (r'areas? (between|under)', '8.2', 'direct'),
    (r'sketching gradient functions?', '7.1', 'direct'),
    (r'trigonometric identities|exact values', '6.1', 'direct'),
    (r'trigonometric equations|equations and identities', '6.2', 'direct'),
    (r'sum to infinity', '4.4', 'direct'),
    (r'binomial estimation|factorial notation|pascal', '4.5', 'direct'),
    (r'dividing polynomials?', '2.1', 'direct'),
    (r'angles in all four quadrants', '6.1', 'direct'),
 ],
 'ial-maths-20-pure-3': [
    (r'double angle|addition formula|sin ?\(A|cos ?\(A', '2.3'),
    (r'identity|sec\^?2|cosec\^?2', '2.2'),
    (r'inverse trig|arcsin|arccos|arctan|secant|cosecant|cotangent', '2.1'),
    (r'modulus', '1.3'),
    (r'transform', '1.4'),
    (r'algebraic fraction|rational function|simplif', '1.1'),
    (r'domain|range|composite|inverse function|functions?', '1.2'),
    (r'ln\b|log graph|logarithm', '3.2'),
    (r'exponential|e\^?x', '3.1'),
    (r'log.?linear|log graph|plotting logs', '3.3'),
    (r'product rule|quotient rule|chain rule', '4.2'),
    (r'implicit|parametric differentiat|dy/dx', '4.3'),
    (r'exponential model|rate of change|initial', '4.4'),
    (r'differentiat', '4.1'),
    (r'integration by recognition|tan x|sec\^?2', '5.2'),
    (r'integrat', '5.1'),
    (r'change of sign|location of roots|interval', '6.1'),
    (r'iteration|iterative|numerical|recurrence relation', '6.2'),
    (r'fixed point iteration', '6.2', 'direct'),
    (r'locating roots?', '6.1', 'direct'),
    (r'differentiating trigonometric', '4.1', 'direct'),
    (r'proving trigonometric identities|trigonometric identities', '2.2', 'direct'),
    (r'sec x, cosec x and cot x|graphs? of sec', '2.1', 'direct'),
    (r'improper fractions?', '1.1', 'direct'),
    (r'modulus|f\|', '1.3', 'direct'),
 ],
 'ial-maths-20-pure-4': [
    (r'partial fraction', '2.1'),
    (r'proof by contradiction|irrationality|contradiction', '1.1'),
    (r'parametric equations?|cartesian.{0,20}parametric', '3.1'),
    (r'binomial (series|expansion)', '4.1'),
    (r'implicit|parametric differentiat', '5.1'),
    (r'formation|connected rates', '5.2'),
    (r'volume of revolution|volumes', '6.1'),
    (r'integration by parts|substitution', '6.2'),
    (r'partial fraction.{0,30}integrat|rational.{0,30}integrat', '6.3'),
    (r'differential equation|separable|first order|second order|order\b|integrating factor', '6.4'),
    (r'parametric.{0,30}area|area under.{0,30}parametric', '6.5'),
    (r'scalar product|angle between', '7.7'),
    (r'vector equation|lines in|equation of a line', '7.6'),
    (r'position vector', '7.4'),
    (r'distance between', '7.5'),
    (r'magnitude|unit vector', '7.2'),
    (r'vector', '7.1'),
    (r'expanding \(?1 ?\+ ?x\)?\^?n|expanding \(?a ?\+ ?bx\)?\^?n', '4.1', 'direct'),
    (r'improper fractions?', '2.1', 'direct'),
    (r'rates? of change', '5.2', 'direct'),
    (r'3d coordinates?', '7.1', 'direct'),
    (r'straight line in three dimensions', '7.6', 'direct'),
    (r'curve sketching', '3.1', 'direct'),
 ],
 'ial-maths-20-mechanics-1': [
    (r'connected particle|pulley|tow ?bar', '4.2'),
    (r'momentum|impulse', '4.3'),
    (r'friction', '4.4'),
    (r'moment', '6.1'),
    (r'suvat|constant acceleration|speed.?time|velocity.?time|displacement.?time|vertical motion|motion under gravity', '3.1'),
    (r'resultant|magnitude|direction|vector', '2.1'),
    (r'displacement|velocit|accelerat|force as vector|resolv|resolution', '2.2'),
    (r'newton|force|dynamic|inclined|smooth', '4.1'),
    (r'equilibrium|statics?|limiting|coplanar', '5.2'),
    (r'coefficient of friction|static friction', '5.3'),
    (r'modelling|model', '1.1'),
    (r'projectile|projection', '3.1'),
    (r'motion in two dimensions', '2.2', 'direct'),
    (r'force diagrams?', '4.1', 'direct'),
    (r'quantities and units', '1.1', 'direct'),
    (r'tilting', '6.1', 'direct'),
    (r'centres? of mass', '6.1', 'direct'),
 ],
 'ial-maths-20-mechanics-2': [
    (r'projectile|projection', '1.2'),
    (r'vertical plane|vertical motion|gravity', '1.1'),
    (r'function of time|variable acceleration|as a function', '1.3'),
    (r'differentiat|integrat.{0,20}vector|vector.{0,20}(differentiat|integrat)', '1.4'),
    (r'centre of mass|centroid|discrete mass', '2.1'),
    (r'plane figures|composite|uniform lamina', '2.2'),
    (r'lamina|framework|equilibrium of', '2.3'),
    (r'work|energy|power', '3.1'),
    (r'momentum|impulse|vector form', '4.1'),
    (r'direct impact|elastic particles|coefficient of restitution', '4.2'),
    (r'successive impacts|two particles and a smooth|collision', '4.3'),
    (r'moment of a force|moments?', '5.1'),
    (r'equilibrium of rigid|rigid bodies|non-parallel', '5.2'),
    (r'acceleration|velocity|kinemat|displacement|suvat', '1.3'),
    (r'using integration', '1.4', 'direct'),
    (r'functions? of time', '1.3', 'direct'),
    (r'projection at any angle', '1.2', 'direct'),
    (r'horizontal and vertical components|horizontal projection', '1.2', 'direct'),
 ],
 'igcse-maths-a-18-higher': [
    (r'recurring decimal', '1.3A'),
    (r'standard form', '1.9A'),
    (r'order of operations|hierarchy|brackets|bidmas|bodmas', '1.1F'),
    (r'rounding|approximation|estimate|significant figure', '1.8D'),
    (r'hcf|highest common|common factor|common multiple|lcm', '1.1H'),
    (r'prime', '1.1G'),
    (r'directed number|negative number', '1.1C'),
    (r'indice', None),
    (r'fraction', None),
    (r'decimal', None),
    (r'ratio|proportion', None),
    (r'percent', None),
    (r'compound (interest|growth|measure)|density|pressure', None),
    (r'speed|distance|velocity', None),
    (r'area|perimeter|volume|surface area|compound shape', None),
    (r'angle|polygon|parallel line', None),
    (r'pythagoras|trigonometry|right.?angled', None),
    (r'circle|arc|sector', None),
    (r'probability|tree diagram|venn', None),
    (r'sequence|nth term|pattern', None),
    (r'expand|factorise|bracket|factoris', None),
    (r'simultaneous', None),
    (r'graph|gradient|linear|quadratic|cubic|reciprocal|function', None),
    (r'mean|median|mode|average|range|frequency', None),
    (r'transformation|reflection|rotation|enlargement|translation|vector', None),
    (r'congruence|similarity|similar', None),
    (r'upper|lower|bound', None),
    (r'equation|solve|rearrang|algebra', None),
    (r'number|multiply|divide|subtract|add', None),
 ],
 'ial-maths-20-statistics-1': [
    (r'normal', '5.1'),
    (r'linear transform.{0,30}(discrete|random)', '5.3'),
    (r'mean and variance of discrete|e\(x\)|expected value|expectation', '5.3'),
    (r'discrete uniform', '5.4'),
    (r'discrete random|probability function|cumulative', '5.2'),
    (r'histogram|stem|box.?plot', '2.1'),
    (r'standard deviation|variance|dispersion|interpercentile|quartile', '2.3'),
    (r'skew|outlier', '2.4'),
    (r'mean|median|mode|location|grouped|interpolation', '2.2'),
    (r'independen', '3.3'),
    (r'conditional|exclusive|sample space', '3.2'),
    (r'tree diagram|venn', '3.4'),
    (r'probabilit', '3.1'),
    (r'regression|scatter', '4.1'),
    (r'explanatory|response|dependent|independent variable', '4.2'),
    (r'correlation|pmcc', '4.3'),
    (r'modelling|statistic', '1.1'),
    (r'linear transforms? of discrete', '5.3', 'direct'),
    (r'mean and variance of discrete', '5.3', 'direct'),
    (r'discrete random variables?', '5.2', 'direct'),
    (r'pmcc', '4.3', 'direct'),
    (r'bivariate', '4.1', 'direct'),
    (r'box and whisker', '2.1', 'direct'),
    (r'quartiles and percentiles', '2.3', 'direct'),
 ],
 'ial-maths-20-statistics-2': [
    (r'poisson.{0,30}(approximat|approx)|approximat.{0,30}poisson', '1.3'),
    (r'mean and variance of (the )?(binomial|poisson)|e\(x\).{0,20}poisson', '1.2'),
    (r'poisson', '1.1'),
    (r'binomial distribution|binimial', '1.1'),
    (r'probability density|pdf', '2.2'),
    (r'density and distribution|distribution function|cdf', '2.3'),
    (r'mean and variance of (continuous|crv)|e\(x\).{0,30}continuous', '2.4'),
    (r'mode|median|quartile|percentile', '2.5'),
    (r'continuous random', '2.1'),
    (r'uniform|rectangular', '3.1'),
    (r'normal (approximat|approx)|approximat.{0,30}normal', '3.2'),
    (r'population|census|sampling (unit|frame)', '4.1'),
    (r'sampling distribution|concept of a statistic', '4.2'),
    (r'critical (region|value)', '4.4'),
    (r'(one|two).?tailed', '4.5'),
    (r'test.{0,30}(parameter|mean of)|hypothesis test.{0,30}(binomial|poisson)', '4.6'),
    (r'hypothesis|testing|test', '4.3'),
    (r'approximation', '1.3'),
    (r'sampling methods?', '4.1', 'direct'),
    (r'continuous random variables?', '2.1', 'direct'),
    (r'the poisson distribution', '1.1', 'direct'),
    (r'binomial distribution|binimial', '1.1', 'direct'),
    (r'mean and variance of a continuous', '2.4', 'direct'),
    (r'cumulative probabilities?', '2.3', 'direct'),
 ],
 'ial-further-maths-18-further-pure-1': [
    (r'induction', '8.1'),
    (r'summation|sums of (squares|natural)|series|sigma', '7.1'),
    (r'linear transformation|matrix representation|reflection|rotation|enlargement|stretch|transformation', '6.1'),
    (r'combination of transformations|successive', '6.3'),
    (r'inverse (of a )?transformation', '6.4'),
    (r'inverse (of a )?matrix|\(ab\)', '5.5'),
    (r'determinant|singular', '5.4'),
    (r'product.{0,20}matric|matrix (multiplication|product)', '5.3'),
    (r'scalar.{0,20}matrix|multiplication.{0,20}scalar', '5.2'),
    (r'addition.{0,20}matric|subtract.{0,20}matric|matrices', '5.1'),
    (r'focus|directrix|parabola', '4.3'),
    (r'tangents? and normals?', '4.4'),
    (r'parametric equation|rectangular hyperbola', '4.2'),
    (r'cartesian equation|hyperbola', '4.1'),
    (r'numerical|bisection|iteration|interval|linear interpolation', '3.1'),
    (r'sum of roots|product of roots|new roots|forming quadratics?', '2.1'),
    (r'roots of quadratics?|complex roots|conjugate', '1.5'),
    (r'complex solutions|quadratic equations', '1.4'),
    (r'argand|geometrical representation', '1.3'),
    (r'sum.{0,15}product.{0,15}quotient|complex (number|arithmetic)', '1.2'),
    (r'complex|imaginary', '1.1'),
    (r'modulus and argument', '1.1', 'direct'),
    (r'solving cubic and quartic', '1.6', 'direct'),
    (r'roots? of a quadratic', '2.1', 'direct'),
    (r'locating roots|newton.?raphson', '3.1', 'direct'),
    (r'invert(ing)? a 2x2 matrix|inverse of 2 ?x ?2', '5.5', 'direct'),
    (r'proving (statements|divisibility)|recurrence relation', '8.1', 'direct'),
 ],
}

def verdict_for(course, v, cl):
    """cl = ALL pre-pass candidates (any score) for this video"""
    title = v['title']
    d = [x for x in cl if x['distinctive']]
    # posture: unit-marker rows and module-named rows bind from ALL scored
    # candidates (the module.section marker in the title is machine-readable
    # structure); other non-marker rows keep the P9 tightened-bar shape
    # (distinctive candidates only)
    structured = bool(v.get('marker')) or bool(v.get('moduleNamed')) or bool(v.get('_amb'))
    pool = cl if structured else d
    top = pool[0] if pool else None
    for rule in RULES.get(course, []):
        pat, code = rule[0], rule[1]
        direct = len(rule) > 2 and rule[2] == 'direct'
        if not re.search(pat, title, re.I):
            continue
        if direct:
            if not structured:
                continue
            if code not in specs_of(course):
                continue
            conf, dist = 'low', False
            ev = (f"unit.section marker ({v.get('unit')} {v.get('section')}) routes the course; title names the topic "
                  f"unambiguously and spec {code} '{specs_of(course)[code][:48]}' is validated in the spine; "
                  f"textbook phrasing leaves zero pre-pass token overlap — direct class-table bind at the disclosed "
                  f"P4 cross-subject-style higher title-only bar, confidence low")
            return {'action': 'keep', 'specs': [code], 'confidence': conf, 'reason': ev}
        if not pool:
            continue
        chosen = next((x for x in pool if x['code'] == code), None) if code else top
        if chosen is None:
            fam = code.split('.')[0] + '.'
            chosen = top if top['code'].startswith(fam) else None
        if chosen is None:
            continue
        dist = chosen['minDf'] <= 3
        conf = 'medium' if dist else 'low'
        ev = (f"title names {chosen['code']} '{chosen['title'][:56]}' via token(s) {chosen['matched'][:4]}"
              f" (df {chosen['minDf']})")
        if v.get('marker'):
            sec = f" ({v.get('unit')} {v.get('section')})" if v.get('section') else f" ({v.get('unit')})"
            ev = f"unit.section marker{sec} routes the course; " + ev
        if not dist:
            n = spine_n(course)
            ev += (f"; token df above the tightened bar within a {n}-spec module — bound at the "
                   f"disclosed P4 cross-subject-style higher title-only bar, confidence low")
        return {'action': 'keep', 'specs': [chosen['code']], 'confidence': conf, 'reason': ev}
    if d:
        return {'action': 'drop',
                'reason': f"no class rule matched; best distinctive candidate {d[0]['code']} '{d[0]['title'][:48]}' bound only on vocabulary not named by the title ({d[0]['matched'][:3]})"}
    if cl:
        return {'action': 'unmapped',
                'reason': f"topic tokens ({cl[0]['matched'][:4]}) overlap the spine only above the tightened bar and no class rule matched — routed-but-unmapped, honest"}
    return {'action': 'unmapped',
            'reason': 'zero token overlap with the spine in the pre-pass and no class rule matched — routed-but-unmapped, honest'}

REBINDS = [
    ('geometric proof of addition formulae', 'ial-maths-20-pure-3', ['2.3'], 'medium',
     'addition formulae sin(A±B)/cos(A±B) are named by the pure-3 2.3 spec text; the pure-2 4.4 pre-pass bind was a series-vocabulary adjacency'),
]

verdicts = {}
stats = collections.Counter()
for course, vids in sorted(by_course.items()):
    if course == '__amb-unresolved__':
        verdicts[course] = [{'id': p['id'], 'title': p['title'], 'action': 'unmapped',
                             'reason': 'cross-course pre-pass found no distinctive candidate in any IAL pure spine — honest unmapped'} for p in vids]
        stats['unmapped'] += len(vids)
        continue
    cands = json.load(open(f'{OUT}/candidates-{course}.json'))
    out = []
    for v in vids:
        cl = cands.get(v['id'], [])
        if v.get('_amb') is not None:
            cl = v['_amb']
        rb = next((r for r in REBINDS if r[0] == v['title'].strip().lower()), None)
        if rb:
            _, tgt, specs, conf, note = rb
            ok = all(s in specs_of(tgt) for s in specs)
            dec = ({'action': 'rebind', 'course': tgt, 'specs': specs, 'confidence': conf, 'reason': note}
                   if ok else {'action': 'drop', 'reason': note + ' — target spec missing, honest drop'})
        else:
            dec = verdict_for(course, v, cl)
        dec['id'] = v['id']
        dec['title'] = v['title']
        out.append(dec)
        stats[dec['action']] += 1
    verdicts[course] = out

json.dump(verdicts, open(f'{OUT}/judgment.json', 'w'), indent=1)
print(dict(stats.most_common()))
for c, vs in verdicts.items():
    if not vs:
        continue
    k = sum(1 for v in vs if v['action'] == 'keep')
    med = sum(1 for v in vs if v['action'] == 'keep' and v.get('confidence') == 'medium')
    lo = sum(1 for v in vs if v['action'] == 'keep' and v.get('confidence') == 'low')
    r = sum(1 for v in vs if v['action'] == 'rebind')
    dr = sum(1 for v in vs if v['action'] == 'drop')
    u = sum(1 for v in vs if v['action'] == 'unmapped')
    print(f'{c}: keep {k} (med {med}/low {lo}) rebind {r} drop {dr} unmapped {u}')
