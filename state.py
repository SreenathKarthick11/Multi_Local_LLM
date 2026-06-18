from typing import TypedDict

from models import AgentResponse, CritiqueResponse


class DebateState(TypedDict):
    question: str

    answer_a: AgentResponse | None
    answer_b: AgentResponse | None

    critique_a: CritiqueResponse | None
    critique_b: CritiqueResponse | None

    revised_answer_a: AgentResponse | None
    revised_answer_b: AgentResponse | None

    final_answer: str