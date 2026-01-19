from langgraph.graph import StateGraph, END
from state import TestGenState

from agents.code_reader import code_reader_agent
from agents.test_generator import test_generator_agent
from agents.test_writer import test_writer_agent
from agents.test_runner import test_runner_agent
from agents.coverage_analyzer import coverage_analyzer_agent
from agents.judge import judge_agent
from agents.retry_incrementer import retry_incrementer

MAX_RETRIES = 2


def route_after_judge(state):
    """
    Routing logic after judge decision
    """
    if state["verdict"] == "PASS":
        return END

    if state["verdict"] == "RETRY" and state["retry_count"] < MAX_RETRIES:
        return "increment_retry"

    return END  # FAIL or retry limit exceeded


# -------------------------
# Build graph
# -------------------------

graph = StateGraph(TestGenState)

# Nodes
graph.add_node("read_code", code_reader_agent)
graph.add_node("generate_test", test_generator_agent)
graph.add_node("write_test", test_writer_agent)
graph.add_node("run_tests", test_runner_agent)
graph.add_node("analyze_coverage", coverage_analyzer_agent)
graph.add_node("judge", judge_agent)
graph.add_node("increment_retry", retry_incrementer)

# Entry point
graph.set_entry_point("read_code")

# Linear flow
graph.add_edge("read_code", "generate_test")
graph.add_edge("generate_test", "write_test")
graph.add_edge("write_test", "run_tests")

# 🔑 Critical missing link (THIS FIXES YOUR ISSUE)
graph.add_edge("run_tests", "analyze_coverage")

graph.add_edge("analyze_coverage", "judge")

# Conditional routing after judge
graph.add_conditional_edges(
    "judge",
    route_after_judge,
    {
        "increment_retry": "increment_retry",
        END: END,
    }
)

# Retry loop
graph.add_edge("increment_retry", "generate_test")

# Compile
test_graph = graph.compile()
