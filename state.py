from typing import TypedDict


class DebateState(TypedDict):
    question: str

    answer_a: str
    answer_b: str

    final_answer: str