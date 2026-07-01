# agents/debate_controller.py

from tools.stopping import should_stop

from ui.emitter import emit
from ui.events import RuntimeEvent
from ui.clock import elapsed

# barrier node function
def pass_through(state):
    return {}

def debate_controller(state):

    decision = should_stop(state)

    emit(RuntimeEvent(
        round_number=state["round_number"],
        max_rounds=state["max_rounds"],
        elapsed_seconds=elapsed(),
        stop_reason=decision["reason"] or "",
    ))
    
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