from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

def test_generator_agent(state):
    uncovered = state.get("uncovered_lines", [])

    coverage_hint = ""
    if uncovered:
        coverage_hint = f"""
        The following lines are NOT covered by tests:
        {chr(10).join(uncovered)}

        Generate additional JUnit tests that specifically execute these lines.
        """

    prompt = f"""
    You are a senior Java QA engineer.

    Generate a JUnit 5 test class for the following Java code.

    Requirements:
    - Package: com.example.math
    - Use org.junit.jupiter.api.Test
    - Use assertions from org.junit.jupiter.api.Assertions
    - Tests must be deterministic

    {coverage_hint}

    Java code:
    {state['java_code']}
    """

    response = llm.invoke(prompt)
    return {"generated_test": response.content}

