#!/usr/bin/env python3
"""Derived graph emitter: canonical JSON -> loader-contract Layer-A YAMLs.

Emits Official-Specifications/parsed/_derived/graph/<qual>/{specification_points,
topics, relationships, practicals}.yaml in the syllabai-core
ConceptGraphSnapshotLoader field contract (mirrors graph/*.yaml shapes).
Chemistry output is additionally diffed against the operator-ratified
graph/ store -> DIFF_VS_RATIFIED.json. Zero-LLM, deterministic.
"""
import glob, json, os, re, sys, datetime
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from spec_parser import OUT_BASE
from build_canonical import qid, load_spec_meta

TODAY = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
GRAPH_DIR = f'{OUT_BASE}/_derived/graph'
RATIFIED = '/home/z/my-project/download/syllabai-resources/graph'
EDGE_VOCAB = ('live V2 knowledge_edges enum (V2__curriculum_knowledge.sql): '
              'PART_OF, REQUIRES_PREREQUISITE, RELATED_TO, MISCONCEPTION_OF, '
              'EXPLAINED_BY, REMEDIATED_BY')

def dump_yaml(path, obj):
    with open(path, 'w') as f:
        yaml.safe_dump(obj, f, sort_keys=False, allow_unicode=True, width=100)

def emit(slug):
    sp = json.load(open(f'{OUT_BASE}/{slug}/spec_points.json'))
    tp = json.load(open(f'{OUT_BASE}/{slug}/topics.json'))
    pr = json.load(open(f'{OUT_BASE}/{slug}/practicals.json'))
    meta_src = load_spec_meta(slug)
    cover = meta_src.get('cover_code') or qid(slug)
    out = f'{GRAPH_DIR}/{slug}'
    os.makedirs(out, exist_ok=True)

    # topic / subsection codes (4CH1-S1 style when cover code available)
    topic_code = {i: f"{cover}-S{i}" for i in range(1, len(tp['topics']) + 1)}
    if not topic_code:
        topic_code = {1: f"{cover}-S1"}   # families with no printed topic headings
    sub_code = {i: f"{cover}-SUB{i}" for i in range(1, len(tp['subsections']) + 1)}
    # attach each subsection to the topic whose page/oy precedes it
    sub_parent = {}
    topics_sorted = sorted(tp['topics'], key=lambda t: (t['provenance']['page'], t['provenance'].get('oy') or 0))
    for i, s in enumerate(tp['subsections'], 1):
        parent = None
        for j, t in enumerate(topics_sorted, 1):
            tp_page = t['provenance']['page']
            s_page = s['page']
            if (tp_page, t['provenance'].get('oy') or 0) <= (s_page, s.get('provenance', {}).get('page') or s['page']):
                if tp_page <= s_page:
                    parent = j
        sub_parent[i] = parent or 1

    common_meta = {
        'curriculum_code': cover,
        'qualification': meta_src.get('issue') and
            f"{meta_src.get('slug','')} (Issue {meta_src['issue']})" or meta_src.get('slug'),
        'phase': 1,
        'node_families': ['TOPIC', 'SUBTOPIC', 'SPEC_POINT'],
        'graph_format_version': 1,
        'source_documents': [{
            'file': sp['source']['pdf'], 'role': 'official-pdf-direct-parse',
            'sha1': sp['source']['pdf_sha1'],
        }],
        'edge_vocabulary': EDGE_VOCAB,
        'provenance_default': 'RULE_DERIVED',
        'generator': 'scripts/emit_graph.py (from parsed/<qual>/spec_points.json)',
        'generated': TODAY,
    }

    # ---- specification_points.yaml ----
    points = []
    for p in sp['spec_points']:
        points.append({
            'code': p['id'],
            'official_code': p['official_code'],
            'official_wording': p['text'],
            'section': topic_code.get(_topic_index(tp, p), None),
            'subsection': None,
            'ordering': p['ordering'],
            'global_order': p['ordering'],
            'practical': p['practical'],
            'scope': p['scope'],
            'applicability': p['applicability'],
            'leading_verb': p['leading_verb'],
            'validation_status': 'RULE_DERIVED',
            'confidence': 1.0,
            'version': 1,
            'provenance': {
                'tier': 'RULE_DERIVED',
                'source_file': sp['source']['pdf'],
                'spec_issue': sp.get('issue'),
                'extraction_method': 'pdf-span-geometry (zero-LLM)',
                'generated_by': 'scripts/emit_graph.py',
                'generated_date': TODAY,
                'pdf_page': p['provenance']['page'],
                'pdf_oy': p['provenance']['oy'],
                'pdf_sha1': sp['source']['pdf_sha1'],
            },
            'damage_flags': p['flags'],
        })
    common_meta['counts'] = {'spec_points': len(points), 'topics': len(tp['topics']),
                             'subsections': len(tp['subsections']),
                             'practicals': pr['counts']['practicals']}
    dump_yaml(f'{out}/specification_points.yaml',
              {**common_meta, 'specification_points': points})

    # ---- topics.yaml ----
    topic_rows = [{
        'code': topic_code[i], 'title': t['title'], 'ordering': i,
        'validation_status': 'RULE_DERIVED', 'confidence': 1.0, 'version': 1,
        'provenance': {'tier': 'RULE_DERIVED', 'extraction_method': 'pdf-span-geometry',
                       'pdf_page': t['provenance']['page'], 'pdf_sha1': sp['source']['pdf_sha1']},
        'damage_flags': [],
    } for i, t in enumerate(tp['topics'], 1)]
    sub_rows = [{
        'code': sub_code[i], 'letter': s.get('letter'), 'title': s['title'],
        'parent_topic': topic_code[sub_parent[i]],
        'provenance': {'tier': 'RULE_DERIVED', 'pdf_page': s['page']},
    } for i, s in enumerate(tp['subsections'], 1)]
    dump_yaml(f'{out}/topics.yaml', {**common_meta, 'topics': topic_rows,
                                     'subsections': sub_rows})

    # ---- relationships.yaml (PART_OF structure edges) ----
    edges = []
    for i, s in enumerate(tp['subsections'], 1):
        edges.append({'from': sub_code[i], 'relation': 'PART_OF',
                      'to': topic_code[sub_parent[i]],
                      'validation_status': 'RULE_DERIVED', 'confidence': 1.0, 'version': 1,
                      'provenance': {'tier': 'RULE_DERIVED',
                                     'extraction_method': 'topic-tree derivation',
                                     'pdf_page': s['page']}})
    for p in sp['spec_points']:
        edges.append({'from': p['id'], 'relation': 'PART_OF',
                      'to': topic_code.get(_topic_index(tp, p)),
                      'validation_status': 'RULE_DERIVED', 'confidence': 1.0, 'version': 1,
                      'provenance': {'tier': 'RULE_DERIVED',
                                     'extraction_method': 'statement-topic association',
                                     'pdf_page': p['provenance']['page']}})
    dump_yaml(f'{out}/relationships.yaml', {**common_meta, 'edges': edges})

    # ---- practicals.yaml ----
    dump_yaml(f'{out}/practicals.yaml', {**common_meta, 'practicals': pr['practicals']})
    return len(points), len(edges)

def _topic_index(tp, point):
    """Topic list index (1-based) for a spec point via topic ref."""
    tref = point.get('topic')
    if not tref:
        return None
    key_t = (tref.get('number'), tref.get('title'))
    for i, t in enumerate(tp['topics'], 1):
        if (t.get('number'), t.get('title')) == key_t:
            return i
    return None

def diff_chemistry():
    """Emitted candidate vs operator-ratified graph/specification_points.yaml."""
    out = f'{GRAPH_DIR}/igcse-chemistry/DIFF_VS_RATIFIED.json'
    rat = yaml.safe_load(open(f'{RATIFIED}/specification_points.yaml'))
    cand = yaml.safe_load(open(f'{GRAPH_DIR}/igcse-chemistry/specification_points.yaml'))
    rat_by_code = {r['official_code']: r for r in rat['specification_points']}
    cand_by_code = {}
    for c in cand['specification_points']:
        if c['official_code']:
            cand_by_code[c['official_code']] = c
    codes_rat, codes_cand = set(rat_by_code), set(cand_by_code)
    def norm(t):
        return re.sub(r'\s+', ' ', t.replace('\u2019', "'").replace('\u2018', "'")
                      .replace('\u201c', '"').replace('\u201d', '"')
                      .replace('\u2013', '-').replace('\u00a0', ' ')).strip().lower()
    same, diff = 0, []
    for code in sorted(codes_rat & codes_cand):
        if norm(rat_by_code[code]['official_wording']) == norm(cand_by_code[code]['official_wording']):
            same += 1
        else:
            diff.append({
                'code': code,
                'ratified': rat_by_code[code]['official_wording'],
                'candidate': cand_by_code[code]['official_wording'],
            })
    result = {
        'generated': TODAY,
        'ratified_store': 'syllabai-resources/graph/specification_points.yaml (operator-ratified, OCR-md source)',
        'candidate': 'parsed/_derived/graph/igcse-chemistry/specification_points.yaml (PDF-direct parse)',
        'codes_ratified': len(codes_rat), 'codes_candidate': len(codes_cand),
        'codes_equal': codes_rat == codes_cand,
        'codes_only_in_ratified': sorted(codes_rat - codes_cand),
        'codes_only_in_candidate': sorted(codes_cand - codes_rat),
        'wording_identical_normalized': same,
        'wording_diff_count': len(diff),
        'wording_diffs': diff,
        'note': ('Diff character expected: the ratified store preserves OCR-md artifacts '
                 '(LaTeX fragments, notation damage flagged in graph damage_flags); the '
                 'candidate is PDF-verbatim. Candidate is the cleaner source; ratified store '
                 'remains the Layer-B anchor.'),
    }
    with open(out, 'w') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
    return result

if __name__ == '__main__':
    import build_canonical
    only = sys.argv[1:] or sorted(build_canonical.FAMILY)
    for slug in only:
        n, e = emit(slug)
        print(f"EMIT {slug:32s} points={n:3d} edges={e:3d}")
    d = diff_chemistry()
    print(f"CHEM DIFF: codes_equal={d['codes_equal']} "
          f"identical={d['wording_identical_normalized']}/{d['codes_ratified']} "
          f"diffs={d['wording_diff_count']}")
