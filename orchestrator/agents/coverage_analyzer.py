from pathlib import Path
import xml.etree.ElementTree as ET
import os

JACOCO_XML = Path("../java-app/target/site/jacoco/jacoco.xml")
JACOCO_HTML = Path("../java-app/target/site/jacoco/index.html")

def coverage_analyzer_agent(state):
    if not JACOCO_XML.exists():
        return {
            "coverage": 0.0,
            "coverage_summary": "JaCoCo report not found"
        }

    tree = ET.parse(JACOCO_XML)
    root = tree.getroot()

    covered = 0
    missed = 0

    for counter in root.findall(".//counter"):
        if counter.attrib["type"] == "LINE":
            covered = int(counter.attrib["covered"])
            missed = int(counter.attrib["missed"])

    total = covered + missed
    coverage = (covered / total) * 100 if total else 0.0

    summary = f"""
COVERAGE SUMMARY:
Line Coverage : {coverage:.2f}%
Covered Lines: {covered}
Missed Lines : {missed}

JACOCO REPORT:
HTML: {JACOCO_HTML.resolve()}
XML : {JACOCO_XML.resolve()}
""".strip()

    return {
        "coverage": round(coverage, 2),
        "coverage_summary": summary,
        "jacoco_html": str(JACOCO_HTML.resolve())
    }
