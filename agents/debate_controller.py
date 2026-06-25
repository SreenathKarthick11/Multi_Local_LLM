# agents/debate_controller.py

from tools.stopping import should_stop

# barrier node function
def pass_through(state):
    return {}

def debate_controller(state):

    decision = should_stop(state)
    return {
        "round_number":
            state["round_number"] + 1,
        "stop_reason":
            decision["reason"]
    }

def should_continue(state):

    stop_result = should_stop(state)
    if stop_result["stop"]:
        return "judge"

    return "continue"