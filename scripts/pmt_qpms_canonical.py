#!/usr/bin/env python3
"""
Batch driver: PMT IGCSE Chemistry QP/MS -> canonical JSON via syllabai-parser.

For each QP PDF under `Unit N/Questions/Paper M/`, pairs it with the matching
`Unit N/Mark Schemes/Paper M/<same base> MS.pdf` (may be absent: Chemical
Tests 1), runs syllabai-parser ParserCli QP, and writes to
`Unit N/Canonical (JSON)/Paper M/<topic-slug>/`:
  canonical-qp.json, canonical-ms.json (if paired), past-paper-draft.json

Resume: skips pairs whose past-paper-draft.json already exists.
Toolchain note: JAVA/JAR/CP paths are environment-specific (JDK 25 + mvn -q package; see syllabai-parser README).
Usage: pmt_qpms_canonical.py [substring-filter ...]
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

JAVA = "/home/z/my-project/toolchain/jdk25/bin/java"
JAR = "/home/z/my-project/repos/syllabai-parser/target/syllabai-parser-0.1.0-SNAPSHOT.jar"
CP = Path("/home/z/my-project/toolchain/cp.txt").read_text().strip()
RES = Path("/home/z/my-project/repos/syllabai-resources/PMT Edexcel IGCSE Chemistry Resources")
OUT_NAME = "Canonical (JSON)"


def slugify(name):
    s = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)[:80]


def main():
    filters = sys.argv[1:]
    qp_files = sorted(RES.glob("Unit */Questions/Paper */*.pdf"))
    if filters:
        qp_files = [p for p in qp_files if any(f in str(p) for f in filters)]
    print(f"{len(qp_files)} QP files in scope")

    rows, t0 = [], time.time()
    for i, qp in enumerate(qp_files, 1):
        unit, paper = qp.parents[2].name, qp.parent.name  # Unit N / Paper M
        topic = re.sub(r"\s+QP\.pdf$", "", qp.name)
        ms = RES / unit / "Mark Schemes" / paper / f"{topic} MS.pdf"
        out_dir = RES / unit / OUT_NAME / paper / slugify(topic)
        row = {"unit": unit, "paper": paper, "topic": topic,
               "msPaired": ms.exists(),
               "outDir": str(out_dir.relative_to(RES))}
        if (out_dir / "past-paper-draft.json").exists():
            row["status"] = "skipped (exists)"
            rows.append(row)
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        cmd = [JAVA, "-cp", f"{JAR}:{CP}", "com.syllabai.parser.ParserCli", "QP",
               str(qp), str(out_dir),
               str(ms) if ms.exists() else "",
               f"--paper=Edexcel|IGCSE|Chemistry|{paper}|PMT Questions by Topic ({topic})|4CH1"]
        t1 = time.time()
        r = subprocess.run(cmd, capture_output=True, text=True)
        m = re.search(r"questions: (\d+)(?:; mark points: (\d+))?", r.stdout)
        row["status"] = "ok" if r.returncode == 0 else "FAIL"
        row["questions"] = int(m.group(1)) if m else None
        row["markPoints"] = int(m.group(2)) if m and m.group(2) else None
        row["secs"] = round(time.time() - t1, 1)
        if r.returncode != 0:
            row["error"] = (r.stderr or r.stdout)[-400:]
            print(f"  !! FAIL {qp.name}: {row['error'][:160]}")
        rows.append(row)
        print(f"  [{i}/{len(qp_files)}] {unit}/{paper}/{topic}: "
              f"q={row.get('questions')} mp={row.get('markPoints')} "
              f"ms={'Y' if ms.exists() else 'N'} {row['secs']}s")

    ok = [r for r in rows if r["status"] == "ok"]
    report = {
        "total": len(rows), "ok": len(ok),
        "failed": [r for r in rows if r["status"] == "FAIL"],
        "qpOnly": [r["topic"] for r in rows if not r["msPaired"]],
        "totalQuestions": sum(r.get("questions") or 0 for r in ok),
        "totalMarkPoints": sum(r.get("markPoints") or 0 for r in ok),
        "secs": round(time.time() - t0, 1),
    }
    print(json.dumps({k: v for k, v in report.items() if k != "failed"}, indent=2))
    Path("/home/z/my-project/pmt_qpms_batch_report.json").write_text(
        json.dumps({"report": report, "rows": rows}, indent=2, ensure_ascii=False))
    if report["failed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
