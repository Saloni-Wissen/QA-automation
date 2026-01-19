from typing import TypedDict

class TestGenState(TypedDict, total=False):
    java_code: str
    generated_test: str
    test_run_output: str
    verdict: str
    retry_count: int
    coverage: float
    coverage_summary: str
    jacoco_html: str

