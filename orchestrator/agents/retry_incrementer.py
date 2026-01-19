def retry_incrementer(state):
    return {"retry_count": state["retry_count"] + 1}
