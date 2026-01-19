def judge_agent(state):
    if "BUILD SUCCESS" in state["test_run_output"]:
        return {"verdict": "PASS"}
    return {"verdict": "FAIL"}
