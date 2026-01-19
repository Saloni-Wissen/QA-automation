# AI-Driven Test Generation & Verification POC (Java + LangGraph)

This repository demonstrates a **production-shaped proof of concept** for using **LangChain + LangGraph** as an **intelligent test orchestration layer** over a Java codebase.

The POC shows how AI can:
- Read Java source code
- Generate valid JUnit tests
- Write them into a real Maven project
- Execute the tests
- Produce a deterministic PASS / FAIL verdict

This is designed to mirror how AI-driven testing systems fit into **enterprise CI/CD pipelines**, not as a replacement for JUnit or Maven, but as an **intelligence layer on top of them**.

---

## 📌 What this POC proves

- AI can safely generate **real JUnit tests** for Java code
- LangGraph can orchestrate **multi-step testing workflows**
- Failures are **deterministic, inspectable, and recoverable**
- The solution is **CI/CD ready**
- Java code remains unchanged — AI acts as a control plane

---

## 🏗️ Architecture Overview

```
Java Code (Calculator.java)
        ↓
LangGraph Orchestrator (Python)
        ↓
AI Test Generator (LangChain)
        ↓
JUnit Test Written to Disk
        ↓
Maven Test Execution
        ↓
Verdict (PASS / FAIL)
```

### Key Design Principle

> **LangChain provides intelligence, LangGraph provides control.**

---

## 📁 Repository Structure

```
qa_poc/
├── java-app/                    # Java application under test
│   ├── pom.xml
│   └── src/
│       ├── main/java/...        # Calculator.java
│       └── test/java/...        # AI-generated tests
│
└── orchestrator/                # AI orchestration layer
    ├── agents/
    │   ├── code_reader.py       # Reads Java source
    │   ├── test_generator.py    # Generates JUnit tests (LLM)
    │   ├── test_writer.py       # Sanitizes & writes tests
    │   ├── test_runner.py       # Runs Maven
    │   └── judge.py             # Produces verdict
    ├── state.py                 # Shared LangGraph state
    ├── graph.py                 # LangGraph workflow
    ├── run.py                   # Entry point
    └── requirements.txt
```

---

## ⚙️ Prerequisites

- Java **17**
- Maven **3.8+**
- Python **3.10+** (3.11 recommended)
- OpenAI API key (or compatible LLM provider)

```powershell
setx OPENAI_API_KEY "your-api-key"
```

---

## 🚀 How to Run the POC

### 1️⃣ Verify Java project (Phase 1)

```powershell
cd java-app
mvn test
```

Expected result:

```
BUILD SUCCESS
```

### 2️⃣ Set up the orchestrator

```powershell
cd orchestrator
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the AI-driven test workflow

```powershell
python run.py
```

---

## ✅ Expected Output

```
JAVA_CODE:
(public class Calculator {...})

GENERATED_TEST:
(public class CalculatorTest {...})

TEST_RUN_OUTPUT:
[INFO] BUILD SUCCESS

VERDICT:
PASS
```

If the test generation is invalid, the verdict will be:

```
VERDICT:
FAIL
```

---

## 🧠 Why LangChain + LangGraph?

### LangChain
- Handles LLM interaction
- Generates JUnit tests
- Abstracts model providers
- Enables future test critics, repair agents, and evaluators

### LangGraph
- Orchestrates multi-step workflows
- Maintains explicit, testable state
- Enables retries, branching, and safety checks
- Makes AI behavior deterministic and CI-safe

**This separation is essential for production use.**

---

## 🔐 Production Safety Measures Included

- Markdown sanitization before writing Java files
- Deterministic verdict logic
- No direct modification of production code
- Clear failure boundaries per agent

---

## 🧪 What This Is (and Is Not)

### ✅ This IS
- A realistic enterprise POC
- CI/CD compatible
- Language-agnostic at the orchestration layer
- Extensible to APIs, services, and microservices

### ❌ This is NOT
- A replacement for JUnit or Maven
- A "Zero QA" silver bullet
- Auto-fixing production code (by design)

---

## 🔮 Next Extensions (Planned / Possible)

- Retry loop on failure (LangGraph branching)
- Test quality critic agent
- Coverage enforcement (JaCoCo)
- GitHub Actions / Jenkins integration
- Support for API and integration tests
- Parallel test generation agents

---

## 🏁 Conclusion

This POC demonstrates how AI-driven testing can be introduced safely and incrementally into a Java ecosystem using LangChain and LangGraph.

It provides a clear path from experimentation to production without disrupting existing development practices.

**Author**: POC for AI-Driven Testing Orchestration  
**Status**: Working prototype
