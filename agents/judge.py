from llm import judge_llm
from state import DebateState

def judge(state:DebateState):

    answer_a = state["history_a"][-1]
    answer_b = state["history_b"][-1]

    critique_a = state["critique_a"]
    critique_b = state["critique_b"]

    prompt = f"""
        Question:
        {state["question"]}

        Search Used A:
        {state["search_used_a"]}

        Answer A:
        {answer_a.answer}

        Confidence A:
        {answer_a.confidence}

        Reasoning A:
        {answer_a.reasoning}

        Critique of A:
        {critique_b.weaknesses}

        Hallucination Risk A:
        {critique_b.hallucination_risk}/5

        Search Used B:
        {state["search_used_b"]}

        Answer B:
        {answer_b.answer}

        Confidence B:
        {answer_b.confidence}

        Reasoning B:
        {answer_b.reasoning}

        Critique of B:
        {critique_a.weaknesses}

        Hallucination Risk B:
        {critique_a.hallucination_risk}/5

        Choose the better answer.

        Prioritize:
        0. Winner must be either A or B (don't choose a tie)
        1. Correctness
        2. Evidence support
        3. Lower hallucination risk
        4. Strong reasoning

        Explain briefly.
        """

    response = judge_llm.invoke(prompt)

    return {
        "judge_result": response
    }