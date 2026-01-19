from langgraph.graph import StateGraph, END
from state import TestGenState

from agents.code_reader import code_reader_agent
from agents.test_generator import test_generator_agent
from agents.test_writer import test_writer_agent
from agents.test_runner import test_runner_agent
from agents.judge import judge_agent

graph = StateGraph(TestGenState)

graph.add_node("read_code", code_reader_agent)
graph.add_node("generate_test", test_generator_agent)
graph.add_node("write_test", test_writer_agent)
graph.add_node("run_tests", test_runner_agent)
graph.add_node("judge", judge_agent)

graph.set_entry_point("read_code")

graph.add_edge("read_code", "generate_test")
graph.add_edge("generate_test", "write_test")
graph.add_edge("write_test", "run_tests")
graph.add_edge("run_tests", "judge")
graph.add_edge("judge", END)

test_graph = graph.compile()
