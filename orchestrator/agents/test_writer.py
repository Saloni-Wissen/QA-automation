from pathlib import Path
import re

TEST_FILE = Path(
    "../java-app/src/test/java/com/example/math/CalculatorTest.java"
)

def strip_markdown(code: str) -> str:
    # Remove ```java ... ``` or ``` ... ```
    code = re.sub(r"^```[a-zA-Z]*\n", "", code.strip())
    code = re.sub(r"\n```$", "", code.strip())
    return code.strip()

def test_writer_agent(state):
    raw_test = state["generated_test"]
    clean_test = strip_markdown(raw_test)

    TEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    TEST_FILE.write_text(clean_test)

    return {}