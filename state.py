from operator import add
from typing import TypedDict,Annotated
from models import AgentResponse, CritiqueResponse


class DebateState(TypedDict):
    question: str

    round_number: int
    max_rounds: int

    evidence_a: str
    evidence_b: str

    # answer_a: AgentResponse | None
    # answer_b: AgentResponse | None

    critique_a: CritiqueResponse | None
    critique_b: CritiqueResponse | None

    # revised_answer_a: AgentResponse | None
    # revised_answer_b: AgentResponse | None

    history_a: Annotated[list[AgentResponse],add]
    history_b: Annotated[list[AgentResponse],add]

    final_answer: str