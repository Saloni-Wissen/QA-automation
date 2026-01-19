from typing import TypedDict

class TestGenState(TypedDict):
    java_code: str
    generated_test: str
    test_run_output: str
    verdict: str
