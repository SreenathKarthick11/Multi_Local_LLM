# agents/controller.py

# barrier node function
def pass_through(state):
    return {}

def debate_controller(state):

    return {
        "round_number":
            state["round_number"] + 1
    }

def should_continue(state):

    if state["round_number"] >= state["max_rounds"]:
        return "judge"

    return "continue"