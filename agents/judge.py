from llm import judge_llm
from state import DebateState


def judge(state: DebateState):

    answer_a = state["history_a"][-1]
    answer_b = state["history_b"][-1]

    critique_a = state["critique_a"]
    critique_b = state["critique_b"]

    tools_a = "\n\n".join(
        f"""
        Tool: {tool.tool_name}
        Input: {tool.tool_input}
        Output: {tool.output}
        """
        for tool in state["tool_bank_a"]
    ) or "None"

    tools_b = "\n\n".join(
        f"""
        Tool: {tool.tool_name}
        Input: {tool.tool_input}
        Output: {tool.output}
        """
        for tool in state["tool_bank_b"]
    ) or "None"

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
        {chr(10).join(critique_b.weaknesses)}

        Hallucination Risk:
        {critique_b.hallucination_risk}/5

        Evidence:
        {chr(10).join(state["evidence_bank_a"][-3:])}

        Tools Used:
        {tools_a}

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
        {chr(10).join(critique_a.weaknesses)}

        Hallucination Risk:
        {critique_a.hallucination_risk}/5

        Evidence:
        {chr(10).join(state["evidence_bank_b"][-3:])}

        Tools Used:
        {tools_b}

        =====================

        Debate stopped because:
        {state["stop_reason"]}

        Evaluation Priority:

        1. Factual correctness
        2. Correct use of tool outputs
        3. Evidence support
        4. Logical reasoning
        5. Lower hallucination risk
        6. Confidence calibration

        Treat calculator and other deterministic tool outputs as highly reliable.

        Choose exactly one winner.

        Return:
        - winner (A or B)
        - confidence
        - reasoning
        """

    response = judge_llm.invoke(prompt)

    return {
        "judge_result": response
    }