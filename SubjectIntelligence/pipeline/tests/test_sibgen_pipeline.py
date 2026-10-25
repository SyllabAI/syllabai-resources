"""Fixture-driven tests for the SIB-GEN pipeline modules (no network, no model calls).

Covers: source resolver (resolve / checksum verify / mismatch fail-closed /
missing repo fail-closed / placeholder glob), evidence pack (bounds, identity,
fail-closed on missing primary), run manifest (deterministic run ids, outcome
recording), generate_artifact (emit pins + ingest accept/reject laws).
Run: python3 -m unittest discover SubjectIntelligence/pipeline/tests -v
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PIPELINE))

import evidence_pack as ep  # noqa: E402
import generate_artifact as ga  # noqa: E402
import run_manifest as rm  # noqa: E402
import source_resolver as sr  # noqa: E402


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="sibgen-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        # fake canonical repos
        self.res = self.tmp / "syllabai-resources"
        self.pp = self.tmp / "syllabai-pastpapers"
        (self.res / "Official-Specifications/igcse-chemistry").mkdir(parents=True)
        (self.res / "books/chem").mkdir(parents=True)
        (self.pp / "past-papers/4ch1/2019-06/4CH1-1C").mkdir(parents=True)
        self.spec = self.res / "Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf"
        self.spec.write_bytes(b"%PDF-1.7 fake-spec-bytes")
        self.specjson = self.res / "Official-Specifications/igcse-chemistry/spec.json"
        self.specjson.write_text(json.dumps(
            {"spec_points": [{"code": "1.4", "text": "recall that …"}] * 3}))
        self.book = self.res / "books/chem/chapter-01.json"
        self.book.write_text(json.dumps({"chunks": [{"id": "c001", "text": "…"}]}))
        self.er = self.pp / "past-papers/4ch1/2019-06/4CH1-1C/er.pdf"
        self.er.write_bytes(b"%PDF-1.7 fake-er-bytes")
        # fake library
        self.lib = self.tmp / "SubjectIntelligence/CHEMISTRY_4CH1"
        (self.lib / "runs").mkdir(parents=True)
        self._write_manifest()
        self._write_policy()
        self.repo_roots = {"resources": self.res, "pastpapers": self.pp}

    def _write_manifest(self):
        (self.lib / "source_manifest.yaml").write_text(f"""
manifest_version: "1.0"
sources:
  - id: SRC-SPEC
    classification: CURRENT — AUTHORITATIVE
    paths:
      - syllabai-resources@Official-Specifications/igcse-chemistry/
    identifiers:
      sha256_spec: "{_sha(self.spec)}"
  - id: SRC-BOOK
    classification: CURRENT — AUTHORITATIVE
    paths:
      - syllabai-resources@books/chem/chapter-01.json
    identifiers: {{}}
  - id: SRC-ER
    classification: CURRENT — ASSESSMENT EVIDENCE
    paths:
      - syllabai-pastpapers@past-papers/4ch1/<session>/4CH1-1C/er.pdf
    identifiers: {{}}
  - id: SRC-ABSENT
    classification: SUPPLEMENTARY
    paths:
      - syllabai-resources@nowhere/missing.pdf
    identifiers: {{}}
""")

    def _write_policy(self, primary=None):
        (self.lib / "evidence_policy.yaml").write_text(f"""
policy_version: "1.0"
course: CHEMISTRY_4CH1
families:
  CUR:
    primary_sources: {primary or ['SRC-SPEC']}
    optional_sources: [SRC-BOOK, SRC-ABSENT]
    restrictions: [test restriction law]
    max_items: 8
    max_excerpt_chars: 2000
""")

    def _resolve(self, ids=None):
        return sr.resolve_course(self.lib, self.repo_roots, ids)


class TestResolver(Base):
    def test_all_resolved_with_checksum_verified(self):
        rec = self._resolve()
        self.assertTrue(rec["ok"], json.dumps(rec, indent=2))
        by = {s["source_id"]: s for s in rec["sources"]}
        self.assertEqual(by["SRC-SPEC"]["paths"][0]["result"], "RESOLVED_DIR")
        checks = {c["identifier"]: c["result"] for c in by["SRC-SPEC"]["identity_checks"]}
        self.assertEqual(checks["sha256_spec"], "VERIFIED")

    def test_placeholder_glob_expands(self):
        rec = self._resolve(["SRC-ER"])
        self.assertTrue(rec["ok"])
        by = {s["source_id"]: s for s in rec["sources"]}
        self.assertEqual(by["SRC-ER"]["paths"][0]["result"], "RESOLVED_FILE")
        self.assertIn("er.pdf", by["SRC-ER"]["paths"][0]["file"])

    def test_supplementary_absence_disclosed_not_fatal(self):
        # course-wide mode: a missing SUPPLEMENTARY source is disclosed (required=False),
        # never fabricated — and does not sink the resolution
        rec = self._resolve(["SRC-ABSENT"])
        by = {s["source_id"]: s for s in rec["sources"]}
        self.assertFalse(by["SRC-ABSENT"]["ok"])
        self.assertFalse(by["SRC-ABSENT"]["required"])
        self.assertTrue(rec["ok"])

    def test_current_class_absence_fails_closed_by_default(self):
        # an absent CURRENT-class source with no repo root: default fatal law
        rec = sr.resolve_course(self.lib, {}, ["SRC-ER"])
        self.assertFalse(rec["ok"])

    def test_unknown_id_fails_closed(self):
        rec = self._resolve(["SRC-DOES-NOT-EXIST"])
        self.assertFalse(rec["ok"])
        self.assertEqual(rec["sources"][0]["paths"][0]["result"], "MISSING")

    def test_checksum_mismatch_fails_closed(self):
        m = self.lib / "source_manifest.yaml"
        m.write_text(m.read_text().replace(_sha(self.spec), "0" * 64))
        rec = self._resolve(["SRC-SPEC"])
        self.assertFalse(rec["ok"])
        by = {s["source_id"]: s for s in rec["sources"]}
        self.assertIn("MISMATCH", {c["result"] for c in by["SRC-SPEC"]["identity_checks"]})

    def test_missing_repo_root_fails_closed(self):
        rec = sr.resolve_course(self.lib, {"resources": self.res}, ["SRC-ER"])
        self.assertFalse(rec["ok"])


class TestEvidencePack(Base):
    def _pack(self, artifact="CUR-01", ids=None):
        resolution = self._resolve(ids)
        return ep.build_pack(self.lib, artifact, resolution), resolution

    def test_pack_identity_and_bounds(self):
        pack, _ = self._pack()
        self.assertEqual(pack["family"], "CUR")
        ids = {i["source_id"] for i in pack["items"]}
        self.assertIn("SRC-SPEC", ids)
        spec_item = next(i for i in pack["items"] if i["source_id"] == "SRC-SPEC"
                         and i["path"].endswith("spec.json"))
        self.assertEqual(spec_item["sha256"], _sha(self.specjson))
        self.assertLessEqual(spec_item["excerpt_chars"], 2000)
        pdf_item = next(i for i in pack["items"] if str(i["path"]).endswith("specification.pdf"))
        self.assertIsNone(pdf_item["excerpt"])  # binary: identity + locator only
        self.assertTrue(pack["pack_sha256"])

    def test_optional_absent_disclosed_not_fatal(self):
        pack, _ = self._pack()
        self.assertIn("SRC-ABSENT", pack["unresolved_optional"])
        disc = next(i for i in pack["items"] if i["source_id"] == "SRC-ABSENT")
        self.assertEqual(disc["status"], "UNRESOLVED")
        self.assertIn("never fabricated", disc["disclosure"])

    def test_missing_primary_fails_closed(self):
        self._write_policy(primary=["SRC-DOES-NOT-EXIST"])
        with self.assertRaises(SystemExit):
            self._pack()

    def test_unknown_family_fails_closed(self):
        resolution = self._resolve()
        with self.assertRaises(SystemExit):
            ep.build_pack(self.lib, "ZZZ-99", resolution)


class TestRunManifest(Base):
    def test_run_ids_deterministic_sequence(self):
        self.assertEqual(rm.next_run_id(self.lib, "CHEMISTRY_4CH1", "CUR-01"),
                         "SIB-CHEMISTRY_4CH1-CUR-01-RUN-001")
        (self.lib / "runs" / "SIB-CHEMISTRY_4CH1-CUR-01-RUN-001").mkdir()
        (self.lib / "runs" / "SIB-CHEMISTRY_4CH1-CUR-01-RUN-004").mkdir()
        self.assertEqual(rm.next_run_id(self.lib, "CHEMISTRY_4CH1", "CUR-01"),
                         "SIB-CHEMISTRY_4CH1-CUR-01-RUN-005")

    def test_open_record_close_roundtrip(self):
        import yaml
        resolution = self._resolve(["SRC-SPEC"])
        pack, _ = TestEvidencePack._pack(self, ids=["SRC-SPEC"])
        run = rm.open_run(self.lib, "CHEMISTRY_4CH1", ["CUR-01"], resolution,
                          {"CUR-01": pack},
                          {"provider": "z.ai", "model": "glm-test"})
        rm.attach_resolution(run, resolution)
        rm.attach_pack(run, "CUR-01", pack)
        rm.record_outcome(run, "CUR-01", "LANDED", artifact_file="artifacts/x.md")
        rm.close_run(run, "test receipt")
        back = yaml.safe_load((run["run_dir"] / "run_manifest.yaml").read_text())
        self.assertEqual(back["run_id"], run["run_id"])
        self.assertEqual(back["outcomes"]["CUR-01"]["state"], "LANDED")
        self.assertEqual(back["generator"]["provider"], "z.ai")
        self.assertTrue((run["run_dir"] / "evidence" / "CUR-01.pack.json").is_file())

    def test_refuses_batch_runs(self):
        with self.assertRaises(SystemExit):
            rm.open_run(self.lib, "CHEMISTRY_4CH1", ["CUR-01", "CUR-02"],
                        self._resolve(["SRC-SPEC"]), {}, {})

    def test_refuses_existing_run_dir(self):
        import unittest.mock
        rid = "SIB-CHEMISTRY_4CH1-CUR-01-RUN-001"
        (self.lib / "runs" / rid).mkdir()
        with unittest.mock.patch.object(rm, "next_run_id", lambda *a, **k: rid):
            with self.assertRaises(SystemExit):
                rm.open_run(self.lib, "CHEMISTRY_4CH1", ["CUR-01"],
                            self._resolve(["SRC-SPEC"]), {}, {})


V2_FRONT = """---
sib_protocol: SIB-1.0
artifact_id: {aid}
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"
research_family: curriculum_intelligence
applicability: REQUIRED
temporal_scope:
  current: true
  legacy: false
source_scope:
  specification: true
  textbook: false
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: false
status: GENERATED
generated_by: zai_agent
generated_at: "2026-10-25"
provenance:
  source_manifest: "{smref}"
  generation_run_id: "{rid}"
  generator_provider: "{prov}"
  generator_model: "{model}"
  generator_agent_version: "SIB_ZAI_PROMPTS_V1"
---
## Purpose

x
## Scope

x
## Executive Summary

x
## Main Analysis

x
## Evidence / Source Basis

x
## Limitations / Coverage Gaps

x
## Research Status

GENERATED; not educational truth.
"""


def _v2_draft(aid="CUR-01", rid="SIB-CHEMISTRY_4CH1-CUR-01-RUN-001",
              smref="CHEMISTRY_4CH1 source_manifest.yaml v1.0",
              prov="z.ai", model="glm-test") -> str:
    return V2_FRONT.format(aid=aid, rid=rid, smref=smref, prov=prov, model=model)


class TestGenerateArtifact(Base):
    def _run(self, aid="CUR-01"):
        resolution = self._resolve(["SRC-SPEC"])
        pack, _ = TestEvidencePack._pack(self, artifact=aid, ids=["SRC-SPEC"])
        return rm.open_run(self.lib, "CHEMISTRY_4CH1", [aid], resolution,
                           {aid: pack},
                           {"provider": "z.ai", "model": "glm-test"})

    def test_emit_task_pins_provenance(self):
        run = self._run()
        pack, _ = TestEvidencePack._pack(self, ids=["SRC-SPEC"])
        task = ga.emit_task(run, "CUR-01", pack, self.lib)
        text = task.read_text()
        self.assertIn(run["run_id"], text)
        self.assertIn("z.ai", text)
        self.assertIn("glm-test", text)
        self.assertIn("SIB_ZAI_PROMPTS_V1", text)

    def test_ingest_lands_v2_draft(self):
        run = self._run()
        draft = self.tmp / "draft.md"
        draft.write_text(_v2_draft(rid=run["run_id"]))
        target = ga.ingest_draft(run, "CUR-01", draft, self.lib,
                                 "CHEMISTRY_4CH1 source_manifest.yaml v1.0")
        self.assertTrue(target.is_file())
        import yaml
        back = yaml.safe_load((run["run_dir"] / "run_manifest.yaml").read_text())
        self.assertEqual(back["outcomes"]["CUR-01"]["state"], "LANDED")

    def test_ingest_rejects_mismatched_run_id(self):
        run = self._run()
        draft = self.tmp / "draft.md"
        draft.write_text(_v2_draft(rid="SIB-CHEMISTRY_4CH1-CUR-01-RUN-999"))
        with self.assertRaises(SystemExit):
            ga.ingest_draft(run, "CUR-01", draft, self.lib, "ref")

    def test_ingest_rejects_placeholder_model(self):
        run = self._run()
        draft = self.tmp / "draft.md"
        draft.write_text(_v2_draft(rid=run["run_id"], model="<model identifier>"))
        with self.assertRaises(SystemExit):
            ga.ingest_draft(run, "CUR-01", draft, self.lib, "ref")

    def test_ingest_rejects_non_generated_status(self):
        run = self._run()
        draft = self.tmp / "draft.md"
        draft.write_text(_v2_draft(rid=run["run_id"]).replace(
            "status: GENERATED", "status: QA_PASSED"))
        with self.assertRaises(SystemExit):
            ga.ingest_draft(run, "CUR-01", draft, self.lib, "ref")

    def test_ingest_refuses_overwrite(self):
        run = self._run()
        draft = self.tmp / "draft.md"
        draft.write_text(_v2_draft(rid=run["run_id"]))
        ga.ingest_draft(run, "CUR-01", draft, self.lib, "ref")
        with self.assertRaises(SystemExit):
            ga.ingest_draft(run, "CUR-01", draft, self.lib, "ref")


if __name__ == "__main__":
    unittest.main()
