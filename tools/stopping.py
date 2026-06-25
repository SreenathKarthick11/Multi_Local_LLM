from state import DebateState


def answers_similar(a: str, b: str):
    
    a = a.lower().strip()
    b = b.lower().strip()

    return a == b


def should_stop(state: DebateState):

    latest_a = state["history_a"][-1]
    latest_b = state["history_b"][-1]

    critique_a = state["critique_a"]
    critique_b = state["critique_b"]

    round_number = state["round_number"]

    max_rounds = state["max_rounds"]

    # Rule 1

    if answers_similar(
        latest_a.answer,
        latest_b.answer
    ):
        return {
            "stop": True,
            "reason": "answers_converged"
        }

    # Rule 2

    if (
        critique_a.hallucination_risk <= 2
        and
        critique_b.hallucination_risk <= 2
        and
        round_number >= 2
    ):
        return {
            "stop": True,
            "reason": "low_hallucination_risk"
        }

    # Rule 3

    if round_number >= max_rounds:
        return {
            "stop": True,
            "reason": "max_rounds"
        }

    return {
        "stop": False,
        "reason": None
    }