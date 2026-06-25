from llm import judge_llm
from state import DebateState

def judge(state:DebateState):

    answer_a = state["history_a"][-1]
    answer_b = state["history_b"][-1]

    critique_a = state["critique_a"]
    critique_b = state["critique_b"]

    prompt = f"""
        You are an impartial debate judge.

        Question:
        {state["question"]}

        =====================
        DEBATER A
        =====================

        Answer:
        {answer_a.answer}

        Confidence:
        {answer_a.confidence}

        Reasoning:
        {answer_a.reasoning}

        Critique:
        {critique_b.weaknesses}

        Hallucination Risk:
        {critique_b.hallucination_risk}/5

        Evidence:
        {chr(10).join(state["evidence_bank_a"][-3:])}

        =====================
        DEBATER B
        =====================

        Answer:
        {answer_b.answer}

        Confidence:
        {answer_b.confidence}

        Reasoning:
        {answer_b.reasoning}

        Critique:
        {critique_a.weaknesses}

        Hallucination Risk:
        {critique_a.hallucination_risk}/5

        Evidence:
        {chr(10).join(state["evidence_bank_b"][-3:])}

        Debate stopped because:
        {state["stop_reason"]}

        Choose exactly one winner.

        Evaluation order:

        1. Factual correctness
        2. Evidence support
        3. Logical reasoning
        4. Hallucination avoidance
        5. Confidence calibration

        Do NOT choose a tie.

        Return:
        - winner (A or B)
        - confidence
        - reasoning
        """

    response = judge_llm.invoke(prompt)

    return {
        "judge_result": response
    }