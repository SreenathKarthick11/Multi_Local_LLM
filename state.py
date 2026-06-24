from operator import add,or_
from typing import TypedDict,Annotated
from models import AgentResponse, CritiqueResponse,JudgeResponse


class DebateState(TypedDict):
    question: str

    round_number: int
    max_rounds: int

    search_used_a: Annotated[bool,or_]
    search_used_b: Annotated[bool,or_]

    evidence_a: str
    evidence_b: str

    critique_a: CritiqueResponse | None
    critique_b: CritiqueResponse | None

    history_a: Annotated[list[AgentResponse],add]
    history_b: Annotated[list[AgentResponse],add]

    judge_result: JudgeResponse | None