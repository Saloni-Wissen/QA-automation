from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

def test_generator_agent(state):
    prompt = f"""
    Given the following Java class, generate a JUnit 5 test class.

    Requirements:
    - Use @Test
    - Test positive numbers
    - Test negative numbers
    - Test zero
    - Class name: CalculatorTest

    Java code:
    {state['java_code']}
    """

    response = llm.invoke(prompt)
    return {"generated_test": response.content}
