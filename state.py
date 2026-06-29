from operator import add,or_
from typing import TypedDict,Annotated
from models import AgentResponse, CritiqueResponse,JudgeResponse, ResourceContext


class DebateState(TypedDict):
    question: str

    round_number: int
    max_rounds: int

    search_used_a: Annotated[bool,or_]
    search_used_b: Annotated[bool,or_]

    rag_used_a : Annotated[bool,or_]
    rag_used_b : Annotated[bool,or_]

    resource_bank_a: Annotated[list[ResourceContext], add]
    resource_bank_b: Annotated[list[ResourceContext], add]

    critique_a: CritiqueResponse | None
    critique_b: CritiqueResponse | None

    history_a: Annotated[list[AgentResponse],add]
    history_b: Annotated[list[AgentResponse],add]

    judge_result: JudgeResponse | None

    stop_reason: str | None