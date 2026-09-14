#!/usr/bin/env python3
"""
T-C12 — hybrid question<->spec-point tagger (Gemini improvement #5, approved backlog 3).

Two-stage hybrid tagging of question units against the 4CH1 specification
registry, then a machine-checked decision file:

  1. `prefilter` (deterministic, zero-LLM, zero-network): IDF-weighted token
     overlap ranks the top-K candidate spec points per question unit. This
     stage prepares and gates inputs; it decides nothing authoritative
     (c10_worksheets.py philosophy).
  2. `verify` (LLM, requires ZAI_API_KEY): a scripted structured-output pass
     asks GLM to pick the primary/secondary spec points and command word from
     the prefiltered candidates. Every response is revalidated against the
     registries and a strict Pydantic schema; every emitted record is
     AI_SUGGESTED + SUGGESTED/REVIEW_REQUIRED, never HUMAN_VALIDATED
     (anti-forgery hard-fail, C11_ARCHITECTURE.md section 7).
     `verify --from-raw TRACE.json` replays a recorded raw trace through the
     same assembly + gates with zero network and no key (audit/replay path —
     usable with any LLM source, including offline or local models).
  3. `check` (validator): schema, registry membership, provenance
     completeness, queue consistency and the section-7 machine rules for a
     decisions file. Negative-tested by c12_negative_test.py.

Honesty rules honoured (AGENT.md / Master Spec section 7 / reconciliation D4-D6):
  - generation emits SUGGESTED/REVIEW_REQUIRED only; the generator hard-fails
    if any record or raw model output contains HUMAN_VALIDATED;
  - unmatched questions are reported into the manual-review queue with an
    ambiguity note — coverage is never manufactured through semantic
    similarity (AGENT.md rule 3);
  - out-of-curriculum input can never reach the high-confidence queue: the
    prefilter marks sub-anchor candidate sets `weak: true`, the verify prompt
    instructs abstention, and sub-threshold confidence forces REVIEW_REQUIRED
    (real June-2025 WPH11 physics question is the committed adversarial control);
  - the LLM stage is inherently non-deterministic across runs even at
    temperature 0: decision records pin the run date and extraction_pass so
    any pass is auditable; `prefilter` and `check` are fully deterministic.

Backends: no third-party HTTP client — urllib only (ocr_batch.py pattern).
Env keys accepted: ZAI_API_KEY, ZHIPU_API_KEY, GLM_API_KEY.

Usage:
  python3 scripts/c12_spec_tagger.py from-paper paper.json -o questions.json
  python3 scripts/c12_spec_tagger.py prefilter questions.json -o prefilter.json
  python3 scripts/c12_spec_tagger.py verify questions.json -o decisions.yaml \
      [--pass-id pass-1] [--model glm-4.6] [--threshold 0.75] [--date 2026-09-14]
  python3 scripts/c12_spec_tagger.py verify questions.json --from-raw trace.json \
      -o decisions.yaml [--model-label "GLM (Super Z agent, z.ai)"]
  python3 scripts/c12_spec_tagger.py check decisions.yaml
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml
from pydantic import BaseModel, Field, ValidationError

REPO = Path(__file__).resolve().parent.parent
GRAPH = REPO / "graph"

TOOL_NAME = "c12_spec_tagger"
CURRICULUM = "4CH1-2017"
DEFAULT_MODEL = "glm-4.6"
API_URL = "https://api.z.ai/api/paas/v4/chat/completions"
ENV_KEY_NAMES = ("ZAI_API_KEY", "ZHIPU_API_KEY", "GLM_API_KEY")

TOP_K = 5
SCORE_FLOOR = 0.08
WEAK_SCORE = 0.3  # max candidate score below this -> unit marked weak (no anchored match)
DEFAULT_THRESHOLD = 0.75

FORBIDDEN_STATE = "HUMAN_VALIDATED"  # anti-forgery: generation may never emit this

STOPWORDS = frozenset("""
a an and are as at be been being but by can could do does for from had has have
how in into is it its may might must of on or our shall should so some such than
that the their them then there these they this those to under up use used using
was were what when where which while who why will with would you your each other
between during before after above below out off over only own same very just
also give given state stated explain explained describe described calculate
""".split())

_TOKEN_RE = re.compile(r"[a-z][a-z0-9]+(?:-[a-z0-9]+)*")
_LATEX_RE = re.compile(r"\$[^$]*\$|\\[a-zA-Z]+|\{|\}|\^\{-?\d+\}|_*\{?\d+\}?(?:\s*(?:dm|mol|m|g|s|cm|k))?\s*(?:\^|~)?")
_MD_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)|\[[^\]]*\]\([^)]*\)|[#>*_`|]+")


# ── registries ────────────────────────────────────────────────────────────────

def load_registries(graph_dir: Path = GRAPH) -> dict:
    """Load the c09-generated registries. Hard-fail if the universe is wrong."""
    sps = yaml.safe_load((graph_dir / "specification_points.yaml").read_text(encoding="utf-8"))
    cws = yaml.safe_load((graph_dir / "command_words.yaml").read_text(encoding="utf-8"))
    topics = yaml.safe_load((graph_dir / "topics.yaml").read_text(encoding="utf-8"))
    try:
        kinds = yaml.safe_load((graph_dir / "spec_command_kinds.yaml").read_text(encoding="utf-8"))
    except FileNotFoundError:
        kinds = {"command_kinds": []}

    points = {}
    for p in sps["specification_points"]:
        points[p["code"]] = p
    if len(points) != sps["meta"]["counts"]["spec_points"]:
        raise SystemExit("FATAL: SP registry count mismatch — refusing to run")
    sub_titles = {}
    for st in topics.get("subtopics", []):
        sub_titles[st["code"]] = (st.get("title") or st.get("title_md") or "").strip()
    command_words = {}
    for cw in cws["command_words"]:
        command_words[_norm_word(cw["command_word"])] = cw
    demanded = {k["code"]: k.get("demanded_substance") or "" for k in kinds.get("command_kinds", [])}
    return {
        "points": points,
        "sub_titles": sub_titles,
        "command_words": command_words,
        "demanded": demanded,
        "graph_dir": graph_dir,
    }


def _norm_word(w: str) -> str:
    return re.sub(r"\s+", " ", (w or "").strip()).lower()


def sp_document(code: str, p: dict, reg: dict) -> str:
    """Text document representing one SP for matching (registry wording only)."""
    parts = [p.get("official_wording") or ""]
    sub = p.get("subsection")
    if sub and sub in reg["sub_titles"]:
        parts.append(reg["sub_titles"][sub])
    verb = p.get("leading_verb")
    if verb:
        parts.append(str(verb))
    dem = reg["demanded"].get(code)
    if dem:
        parts.append(dem)
    return " ".join(parts)


# ── tokenisation + deterministic scoring ──────────────────────────────────────

def clean_text(text: str) -> str:
    text = _LATEX_RE.sub(" ", text or "")
    text = _MD_RE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def tokenize(text: str) -> list[str]:
    return [t for t in _TOKEN_RE.findall(clean_text(text)) if len(t) >= 3 and t not in STOPWORDS]


class Prefilter:
    """IDF-weighted overlap scorer over the 182-point registry. Deterministic."""

    def __init__(self, reg: dict):
        self.reg = reg
        docs = {code: tokenize(sp_document(code, p, reg)) for code, p in reg["points"].items()}
        self.docs = docs
        df: dict[str, int] = {}
        for toks in docs.values():
            for t in set(toks):
                df[t] = df.get(t, 0) + 1
        self.n_docs = len(docs)
        self.df = df

    def _idf(self, tok: str) -> float:
        return math.log((self.n_docs + 1) / (self.df.get(tok, 0) + 1)) + 1.0

    def score(self, q_tokens: list[str], code: str) -> float:
        doc = self.docs[code]
        tf: dict[str, int] = {}
        for t in doc:
            tf[t] = tf.get(t, 0) + 1
        num = 0.0
        for t in set(q_tokens):
            if t in tf:
                num += self._idf(t) * (1.0 + math.log(tf[t]))
        denom = sum(self._idf(t) for t in set(q_tokens)) or 1.0
        return num / denom

    def rank(self, text: str, top_k: int = TOP_K, floor: float = SCORE_FLOOR) -> list[dict]:
        q_tokens = tokenize(text)
        if not q_tokens:
            return []
        scored = [(code, self.score(q_tokens, code)) for code in self.reg["points"]]
        scored = [(c, s) for c, s in scored if s >= floor]
        scored.sort(key=lambda cs: (-cs[1], cs[0]))
        out = []
        for code, s in scored[:top_k]:
            p = self.reg["points"][code]
            out.append({"code": code, "score": round(s, 4),
                        "wording": p.get("official_wording"),
                        "leading_verb": p.get("leading_verb")})
        return out


# ── question loading ──────────────────────────────────────────────────────────

def load_questions(path: Path) -> list[dict]:
    """Generic questions JSON: [{"id","text","marks"?,"source"?}, ...]."""
    data = json.loads(path.read_text(encoding="utf-8"))
    units = data["questions"] if isinstance(data, dict) and "questions" in data else data
    if not isinstance(units, list):
        raise SystemExit("FATAL: questions file must be a list or {\"questions\": [...]}, got %s"
                         % type(units).__name__)
    out, seen = [], set()
    for i, u in enumerate(units):
        if not isinstance(u, dict) or not u.get("text") or not u.get("id"):
            raise SystemExit("FATAL: question unit %d needs at least 'id' and 'text'" % i)
        if u["id"] in seen:
            raise SystemExit("FATAL: duplicate question id %r" % u["id"])
        seen.add(u["id"])
        out.append({"id": str(u["id"]), "text": str(u["text"]),
                    "marks": u.get("marks"), "source": u.get("source")})
    if not out:
        raise SystemExit("FATAL: no question units found")
    return out


def from_paper(paper_path: Path) -> list[dict]:
    """Adapter: syllabai-parser atomizer paper.json -> taggable question units.

    One unit per part (renderedPrompt is self-contained by construction); a
    partless question (e.g. MCQ) becomes one unit from its stem. All data is
    read verbatim — this adapter never rewrites question content.
    """
    paper = json.loads(paper_path.read_text(encoding="utf-8"))
    if paper.get("tool") != "glmocr-atomize":
        raise SystemExit("FATAL: not an atomizer paper.json (tool=%r) — refusing to guess the shape"
                         % paper.get("tool"))
    units = []
    for q in paper.get("questions", []):
        qid = q.get("questionId") or "Q%s" % q.get("number")
        parts = q.get("parts") or []
        if parts:
            for p in parts:
                text = p.get("renderedPrompt") or " ".join(
                    x for x in [q.get("stem"), p.get("text")] if x)
                units.append({"id": "%s:%s" % (qid, p.get("label")), "text": text,
                              "marks": p.get("marks"),
                              "source": "%s (part %s)" % (paper_path.name, p.get("msLabel"))})
        elif q.get("stem"):
            units.append({"id": qid, "text": q["stem"], "marks": q.get("marks"),
                          "source": paper_path.name})
    return units


def text_hash(text: str) -> str:
    return hashlib.sha256(clean_text(text).encode("utf-8")).hexdigest()

# ── strict decision-record schema (Pydantic) ─────────────────────────────────

class Mapping(BaseModel):
    primary_spec_point: str
    secondary_spec_points: list[str] = Field(default_factory=list)
    command_word: str
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str = Field(min_length=1)


class Provenance(BaseModel):
    tier: str
    model_version: str = Field(min_length=1)
    extraction_pass: str = Field(min_length=1)
    derivation_method: str = Field(min_length=1)
    derivation_notes: str = Field(min_length=1)
    upstream: str = Field(min_length=1)
    generated_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")


class DecisionRecord(BaseModel):
    question_id: str
    unit_text_hash: str = Field(pattern=r"^[0-9a-f]{64}$")
    mapping: Mapping | None = None
    provenance: Provenance
    validation_status: str
    ambiguity_note: str | None = None
    version: int = 1


class DecisionsMeta(BaseModel):
    task: str
    extraction_pass: str
    curriculum_code: str
    generated_date: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    model_version: str
    high_confidence_threshold: float = Field(ge=0.0, le=1.0)
    source_questions: str
    registries: dict = Field(default_factory=dict)
    queues: dict = Field(default_factory=dict)
    counts: dict = Field(default_factory=dict)


class DecisionsFile(BaseModel):
    meta: DecisionsMeta
    decisions: list[DecisionRecord]


# ── LLM backend (urllib only — ocr_batch.py pattern) ─────────────────────────

def resolve_api_key(cli_value: str | None) -> str:
    if cli_value:
        return cli_value
    for name in ENV_KEY_NAMES:
        v = os.environ.get(name)
        if v:
            return v
    raise SystemExit("FATAL: no API key — set one of %s (or --api-key). "
                     "The verify stage is optional; prefilter/check run offline." % ", ".join(ENV_KEY_NAMES))


def http_post_json(url: str, payload: dict, headers: dict, timeout: float = 120.0,
                   attempts: int = 3) -> dict:
    last: Exception | None = None
    for attempt in range(attempts):
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=body, method="POST",
                                     headers={"Content-Type": "application/json", **headers})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = ""
            try:
                detail = exc.read().decode("utf-8")[:300]
            except Exception:
                pass
            last = RuntimeError("HTTP %s: %s" % (exc.code, detail))
            if exc.code < 500 and exc.code != 429:
                raise last
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
    raise RuntimeError("LLM call failed after %d attempts: %s" % (attempts, last))


def extract_json_object(raw: str) -> dict:
    """Robust parse: strip fences, take the first balanced {...} block."""
    text = (raw or "").strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    start = text.find("{")
    if start < 0:
        raise ValueError("no JSON object in model response")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unbalanced JSON object in model response")


VERIFY_SYSTEM = (
    "You are a chemistry curriculum tagging assistant for the Pearson Edexcel "
    "International GCSE (9-1) Chemistry 4CH1 specification. You PROPOSE "
    "specification-point mappings and a command word for exam questions. You "
    "never validate, approve or promote anything. You abstain when the text is "
    "not chemistry-4CH1 content or no candidate fits. Reply with ONLY one JSON "
    "object, no prose, matching exactly:"
    ' {"primary_spec_point": "<4CH1-X.YZ or null>",'
    '  "secondary_spec_points": ["<4CH1-X.YZ", ...],'
    '  "command_word": "<command word from the provided list, or null>",'
    '  "confidence": <0.0-1.0>,'
    '  "rationale": "<one sentence citing the matching wording>",'
    '  "ambiguous": <true|false>}'
)


def build_verify_prompt(unit: dict, candidates: list[dict], reg: dict) -> str:
    cand = "\n".join("- %s (verb: %s): %s" % (c["code"], c["leading_verb"], c["wording"])
                     for c in candidates) or "(no candidates scored above the floor)"
    words = ", ".join(sorted(w["command_word"] for w in reg["command_words"].values()))
    return (
        "Command words:\n%s\n\nCandidate specification points (ranked by a keyword prefilter):\n%s\n\n"
        "Question unit %s:\n\"\"\"\n%s\n\"\"\"\n\n"
        "Pick the primary spec point the question assesses (secondary points only if the "
        "question genuinely assesses them too). If the text is outside this specification "
        "or no candidate fits, set primary_spec_point to null and confidence low. "
        "Use the exact command word string from the list." % (words, cand, unit["id"], unit["text"]))


def call_llm(unit: dict, candidates: list[dict], reg: dict, api_key: str,
             model: str) -> tuple[dict, str]:
    prompt = build_verify_prompt(unit, candidates, reg)
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": VERIFY_SYSTEM},
                     {"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 2048,
        "response_format": {"type": "json_object"},
    }
    resp = http_post_json(API_URL, payload,
                          {"Authorization": "Bearer %s" % api_key})
    raw = ((resp.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    return extract_json_object(raw), raw


# ── record assembly + the section-7 machine rules ─────────────────────────────

def _provenance(model: str, pass_id: str, notes: str, run_date: str) -> Provenance:
    return Provenance(
        tier="AI_SUGGESTED",
        model_version=model,
        extraction_pass=pass_id,
        derivation_method="LLM_VERIFIED_CANDIDATES",
        derivation_notes=notes,
        upstream="prefilter c12 (IDF token overlap) over graph/specification_points.yaml (c09 registry)",
        generated_date=run_date)


def assemble_record(unit: dict, raw: dict, model: str, pass_id: str, run_date: str,
                    threshold: float) -> DecisionRecord:
    """Registry-validate one raw LLM response and build the decision record."""
    if FORBIDDEN_STATE in json.dumps(raw):
        raise SystemExit("FATAL: model response for %s contains %s — anti-forgery abort"
                         % (unit["id"], FORBIDDEN_STATE))
    mapping = None
    note = None
    if raw.get("primary_spec_point"):
        mapping = Mapping(
            primary_spec_point=str(raw["primary_spec_point"]),
            secondary_spec_points=[str(s) for s in (raw.get("secondary_spec_points") or [])],
            command_word=str(raw.get("command_word") or ""),
            confidence=float(raw.get("confidence") or 0.0),
            rationale=str(raw.get("rationale") or "").strip())
    reasons = []
    if mapping is None:
        reasons.append("no primary spec point proposed (abstention or out-of-curriculum text)")
    else:
        if mapping.confidence < threshold:
            reasons.append("confidence %.2f below threshold %.2f" % (mapping.confidence, threshold))
        if str(raw.get("ambiguous") or "").lower() == "true" or raw.get("ambiguous") is True:
            reasons.append("model marked the mapping ambiguous")
    if reasons:
        note = "; ".join(reasons)
    status = "REVIEW_REQUIRED" if note else "SUGGESTED"
    return DecisionRecord(
        question_id=unit["id"],
        unit_text_hash=text_hash(unit["text"]),
        mapping=mapping,
        provenance=_provenance("GLM %s (scripted structured output, z.ai)" % model, pass_id,
                               (mapping.rationale if mapping else "abstained"), run_date),
        validation_status=status,
        ambiguity_note=note,
        version=1)


def hard_errors(record: DecisionRecord, reg: dict) -> list[str]:
    """Violations that make a record unacceptable in ANY emitted file (check always
    fails): anti-forgery, tier/status rules, referential integrity, missing notes."""
    errs = []
    if record.provenance.tier != "AI_SUGGESTED":
        errs.append("tier must be AI_SUGGESTED, got %r" % record.provenance.tier)
    if FORBIDDEN_STATE in json.dumps(record.model_dump()):
        errs.append("%s found in record (anti-forgery)" % FORBIDDEN_STATE)
    if record.validation_status not in ("SUGGESTED", "REVIEW_REQUIRED"):
        errs.append("generation may only emit SUGGESTED/REVIEW_REQUIRED, got %r"
                    % record.validation_status)
    if record.mapping is None:
        if record.validation_status != "REVIEW_REQUIRED":
            errs.append("unmatched record must be REVIEW_REQUIRED")
        if not record.ambiguity_note:
            errs.append("unmatched record needs ambiguity_note")
    else:
        m = record.mapping
        if m.primary_spec_point not in reg["points"]:
            errs.append("primary %s not in the %s registry" % (m.primary_spec_point, CURRICULUM))
        for s in m.secondary_spec_points:
            if s not in reg["points"]:
                errs.append("secondary %s not in the %s registry" % (s, CURRICULUM))
    if record.validation_status == "REVIEW_REQUIRED" and not record.ambiguity_note:
        errs.append("REVIEW_REQUIRED needs ambiguity_note")
    return errs


def demotable_errors(record: DecisionRecord, reg: dict, threshold: float) -> list[str]:
    """Violations that disqualify SUGGESTED but may stand in a REVIEW_REQUIRED
    record WHEN the ambiguity_note documents them verbatim (the demotion path
    writes these exact strings, so honest demotion round-trips through check)."""
    errs = []
    if record.mapping is not None:
        m = record.mapping
        if _norm_word(m.command_word) not in reg["command_words"]:
            errs.append("command_word %r not in the command-word registry" % m.command_word)
        if m.confidence < threshold:
            errs.append("confidence %.2f below threshold %.2f" % (m.confidence, threshold))
        for s in m.secondary_spec_points:
            if s == m.primary_spec_point:
                errs.append("secondary %s duplicates primary" % s)
        if record.validation_status == "SUGGESTED" and not m.rationale.strip():
            errs.append("SUGGESTED needs a non-empty rationale")
    return errs


def registry_errors(record: DecisionRecord, reg: dict, threshold: float) -> list[str]:
    """All violations for a record as-emitted (hard + demotable)."""
    return hard_errors(record, reg) + demotable_errors(record, reg, threshold)


# ── stages ────────────────────────────────────────────────────────────────────

def stage_prefilter(args) -> int:
    reg = load_registries(Path(args.graph)) if args.graph else load_registries()
    units = load_questions(Path(args.questions))
    pf = Prefilter(reg)
    report = {
        "tool": TOOL_NAME, "stage": "prefilter", "deterministic": True,
        "top_k": TOP_K, "score_floor": SCORE_FLOOR, "weak_score": WEAK_SCORE,
        "units": [{"id": u["id"],
                   "text_hash": text_hash(u["text"]),
                   "abstained": True,
                   "weak": False,
                   "max_score": 0.0,
                   "candidates": []} for u in units],
    }
    for entry, unit in zip(report["units"], units):
        cand = pf.rank(unit["text"])
        entry["candidates"] = cand
        entry["abstained"] = not cand
        entry["max_score"] = cand[0]["score"] if cand else 0.0
        entry["weak"] = bool(cand) and entry["max_score"] < WEAK_SCORE
    out = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    n_abstain = sum(1 for e in report["units"] if e["abstained"])
    n_weak = sum(1 for e in report["units"] if e["weak"])
    print("prefilter: %d units, %d with candidates, %d weak, %d abstained" %
          (len(report["units"]), len(report["units"]) - n_abstain, n_weak, n_abstain),
          file=sys.stderr)
    return 0


def _finalize(records, raw_trace, reg, args, model_label, pass_id) -> dict:
    """Queue split + decisions doc assembly shared by live and replay paths."""
    high = [r.question_id for r in records if r.validation_status == "SUGGESTED"]
    review = [r.question_id for r in records if r.validation_status != "SUGGESTED"]
    return {
        "meta": {
            "task": "T-C12",
            "extraction_pass": pass_id,
            "curriculum_code": CURRICULUM,
            "generated_date": args.date,
            "model_version": model_label,
            "high_confidence_threshold": args.threshold,
            "source_questions": str(Path(args.questions).resolve()),
            "registries": {"spec_points": len(reg["points"]),
                           "command_words": len(reg["command_words"]),
                           "graph_dir": str(reg["graph_dir"])},
            "queues": {"highConfidence": high, "manualReview": review},
            "counts": {"units": len(records), "suggested": len(high),
                       "reviewRequired": len(review)},
        },
        "decisions": [r.model_dump() for r in records],
    }


def _demote_or_keep(rec, errs):
    if errs:
        print("record %s failed registry validation (%s) -> demoting to REVIEW_REQUIRED"
              % (rec.question_id, "; ".join(errs)), file=sys.stderr)
        rec.validation_status = "REVIEW_REQUIRED"
        rec.ambiguity_note = ("registry validation: %s" % "; ".join(errs))[:400]
    return rec


def _write_out(text: str, out: str | None) -> None:
    if out:
        Path(out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def stage_verify(args) -> int:
    reg = load_registries(Path(args.graph)) if args.graph else load_registries()
    units = load_questions(Path(args.questions))
    run_date = args.date
    pass_id = "c12-%s" % args.pass_id
    pf = Prefilter(reg)
    replay = bool(getattr(args, "from_raw", None))
    model_label = args.model_label or "GLM %s (scripted structured output, z.ai)" % args.model

    records, raw_trace = [], []
    if replay:
        # Replay: re-assemble decisions from a recorded raw trace (audit path,
        # zero network). Same assembly, same gates, same demotion rules as live.
        trace_path = Path(args.from_raw)
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
        by_qid = {}
        for entry in trace:
            qid = entry.get("question_id")
            if qid not in by_qid:
                by_qid[qid] = entry.get("raw_response")
            else:
                raise SystemExit("FATAL: trace has duplicate entries for %s" % qid)
        orphans = sorted(set(by_qid) - {u["id"] for u in units})
        if orphans:
            raise SystemExit("FATAL: trace entries for unknown questions: %s" % orphans)
        for u in units:
            if u["id"] not in by_qid:
                raise SystemExit("FATAL: no trace entry for %s — refusing to improvise" % u["id"])
        for u in units:
            raw = by_qid[u["id"]]
            rec = assemble_record(u, raw, model_label, pass_id, run_date, args.threshold)
            _demote_or_keep(rec, registry_errors(rec, reg, args.threshold))
            records.append(rec)
            raw_trace.append({"question_id": u["id"], "raw_response": raw})
    else:
        api_key = resolve_api_key(args.api_key)
        for u in units:
            cand = pf.rank(u["text"])
            raw, raw_text = call_llm(u, cand, reg, api_key, args.model)
            rec = assemble_record(u, raw, model_label, pass_id, run_date, args.threshold)
            _demote_or_keep(rec, registry_errors(rec, reg, args.threshold))
            records.append(rec)
            raw_trace.append({"question_id": u["id"], "raw_response": raw})

    doc = _finalize(records, raw_trace, reg, args, model_label, pass_id)
    out = yaml.safe_dump(doc, sort_keys=True, allow_unicode=True, width=100)
    _write_out(out, args.out)
    if args.raw_trace:
        Path(args.raw_trace).write_text(
            json.dumps(raw_trace, indent=2, ensure_ascii=False), encoding="utf-8")
    print("verify%s: %d SUGGESTED, %d REVIEW_REQUIRED" %
          (" (replay)" if replay else "", len(doc["meta"]["queues"]["highConfidence"]),
           len(doc["meta"]["queues"]["manualReview"])), file=sys.stderr)
    return 0


def stage_check(args) -> int:
    data = yaml.safe_load(Path(args.decisions).read_text(encoding="utf-8"))
    try:
        doc = DecisionsFile.model_validate(data)
    except ValidationError as exc:
        print("FATAL: decisions file fails the strict schema:\n%s" % exc, file=sys.stderr)
        return 1
    reg = load_registries(Path(args.graph)) if args.graph else load_registries()
    errs: list[str] = []
    seen = set()
    for rec in doc.decisions:
        if rec.question_id in seen:
            errs.append("duplicate question_id %s" % rec.question_id)
        seen.add(rec.question_id)
        # hard violations always fail; demotable ones fail on SUGGESTED and are
        # tolerated on REVIEW_REQUIRED only when the ambiguity note documents
        # them (the demotion path writes these exact strings).
        rec_errs = hard_errors(rec, reg)
        if rec.validation_status == "SUGGESTED":
            rec_errs += demotable_errors(rec, reg, doc.meta.high_confidence_threshold)
        else:
            rec_errs += [d for d in demotable_errors(rec, reg, doc.meta.high_confidence_threshold)
                         if d not in (rec.ambiguity_note or "")]
        errs += ["%s: %s" % (rec.question_id, e) for e in rec_errs]
    # queue consistency
    high = [r.question_id for r in doc.decisions if r.validation_status == "SUGGESTED"]
    review = [r.question_id for r in doc.decisions if r.validation_status == "REVIEW_REQUIRED"]
    if sorted(doc.meta.queues.get("highConfidence", [])) != sorted(high):
        errs.append("meta.queues.highConfidence does not match SUGGESTED records")
    if sorted(doc.meta.queues.get("manualReview", [])) != sorted(review):
        errs.append("meta.queues.manualReview does not match REVIEW_REQUIRED records")
    if sorted(doc.meta.queues.get("highConfidence", []) + doc.meta.queues.get("manualReview", [])) \
            != sorted(r.question_id for r in doc.decisions):
        errs.append("every decision must appear in exactly one queue")
    if errs:
        print("FAIL: %d problem(s):" % len(errs), file=sys.stderr)
        for e in errs:
            print("  - %s" % e, file=sys.stderr)
        return 1
    print("check: OK — %d records (%d SUGGESTED / %d REVIEW_REQUIRED), all registry gates passed"
          % (len(doc.decisions), len(high), len(review)))
    return 0


def stage_from_paper(args) -> int:
    units = from_paper(Path(args.paper))
    out = json.dumps({"questions": units}, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    print("from-paper: %d units" % len(units), file=sys.stderr)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog=TOOL_NAME, description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("from-paper", help="atomizer paper.json -> generic questions JSON")
    p.add_argument("paper"); p.add_argument("-o", "--out"); p.set_defaults(fn=stage_from_paper)

    p = sub.add_parser("prefilter", help="deterministic candidate ranking (zero-LLM)")
    p.add_argument("questions"); p.add_argument("-o", "--out")
    p.add_argument("--graph", help="alternate graph dir (default: repo graph/)")
    p.set_defaults(fn=stage_prefilter)

    p = sub.add_parser("verify", help="LLM structured-output pass -> decisions YAML (key OR --from-raw)")
    p.add_argument("questions"); p.add_argument("-o", "--out")
    p.add_argument("--graph"); p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument("--api-key"); p.add_argument("--pass-id", default="pass-1")
    p.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    p.add_argument("--date", help="pinned run date (default: today UTC)")
    p.add_argument("--raw-trace", help="write raw model responses here for audit")
    p.add_argument("--from-raw", metavar="TRACE.json",
                   help="replay a recorded raw trace through assembly + gates instead of "
                        "calling the API (zero network, no key; audit/replay path)")
    p.add_argument("--model-label", help="override the provenance model_version string")
    p.set_defaults(fn=stage_verify)

    p = sub.add_parser("check", help="validate a decisions YAML against registries + rules")
    p.add_argument("decisions"); p.add_argument("--graph")
    p.set_defaults(fn=stage_check)

    args = ap.parse_args(argv)
    if getattr(args, "fn", None) is stage_verify and not args.date:
        import datetime
        args.date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
