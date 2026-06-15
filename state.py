from typing import TypedDict

from models import AgentResponse


class DebateState(TypedDict):
    question: str

    answer_a: AgentResponse | None
    answer_b: AgentResponse | None

    final_answer: str