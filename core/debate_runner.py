"""
core/debate_runner.py

Thin wrapper around the LangGraph debate.

The UI never calls graph.invoke() directly.
Everything goes through this module.
"""

from typing import Optional

from graph import graph
from state import DebateState


def create_initial_state(
    question: str,
    max_rounds: int = 3,
) -> DebateState:
    """
    Construct the initial DebateState.
    """

    return DebateState(
        question=question,

        round_number=1,
        max_rounds=max_rounds,

        search_used_a=False,
        search_used_b=False,

        rag_used_a=False,
        rag_used_b=False,

        resource_bank_a=[],
        resource_bank_b=[],

        history_a=[],
        history_b=[],

        critique_a=None,
        critique_b=None,

        judge_result=None,

        stop_reason=None,
    )


def run_debate(
    question: str,
    *,
    max_rounds: int = 3,
) -> DebateState:
    """
    Execute one complete debate.

    Returns the final DebateState.
    """

    initial_state = create_initial_state(
        question=question,
        max_rounds=max_rounds,
    )

    final_state = graph.invoke(initial_state)

    return final_state


def resume_debate(state: DebateState) -> DebateState:
    """
    Continue a paused debate.

    Useful later for replay/streaming.
    """

    return graph.invoke(state)


def run_and_measure(
    question: str,
    *,
    max_rounds: int = 3,
):
    """
    Convenience function used by the UI.

    Returns

        final_state
    """

    state = run_debate(
        question,
        max_rounds=max_rounds,
    )

    return state