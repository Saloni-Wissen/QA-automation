def judge_agent(state):
    output = state["test_run_output"]

    if "BUILD SUCCESS" in output:
        return {"verdict": "PASS"}

    if "COMPILATION ERROR" in output or "illegal character" in output:
        return {"verdict": "RETRY"}

    return {"verdict": "FAIL"}
