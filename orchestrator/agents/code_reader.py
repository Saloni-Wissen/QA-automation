from pathlib import Path

JAVA_FILE = Path("../java-app/src/main/java/com/example/math/Calculator.java")

def code_reader_agent(state):
    code = JAVA_FILE.read_text()
    return {"java_code": code}
