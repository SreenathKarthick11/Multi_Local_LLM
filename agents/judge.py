from llm import judge_llm
from state import DebateState
from tools.resource_manager import format_resources


from ui.emitter import emit
from ui.events import JudgeEvent

def judge(state: DebateState):

    answer_a = state["history_a"][-1]
    answer_b = state["history_b"][-1]

    critique_a = state["critique_a"]
    critique_b = state["critique_b"]

    web_a, rag_a, tools_a = format_resources(
        state["resource_bank_a"]
    )

    web_b, rag_b, tools_b = format_resources(
        state["resource_bank_b"]
    )

    prompt = f"""
        You are an impartial debate judge.

        Question:
        {state["question"]}

        ====================================================
        DEBATER A
        ====================================================

        Answer:
        {answer_a.answer}

        Confidence:
        {answer_a.confidence}

        Reasoning:
        {answer_a.reasoning}

        Critique:
        {chr(10).join("- " + weakness for weakness in critique_b.weaknesses)}

        Hallucination Risk:
        {critique_b.hallucination_risk}/5

        Web Evidence:
        {web_a}

        Retrieved Knowledge:
        {rag_a}

        Tool Outputs:
        {tools_a}

        ====================================================
        DEBATER B
        ====================================================

        Answer:
        {answer_b.answer}

        Confidence:
        {answer_b.confidence}

        Reasoning:
        {answer_b.reasoning}

        Critique:
        {chr(10).join("- " + weakness for weakness in critique_a.weaknesses)}

        Hallucination Risk:
        {critique_a.hallucination_risk}/5

        Web Evidence:
        {web_b}

        Retrieved Knowledge:
        {rag_b}

        Tool Outputs:
        {tools_b}

        ====================================================

        Debate stopped because:
        {state["stop_reason"]}

        Evaluation Priority:

        1. Factual correctness.
        2. Correct use of deterministic tool outputs.
        3. Correct use of retrieved knowledge.
        4. Correct use of web evidence.
        5. Logical reasoning.
        6. Lower hallucination risk.
        7. Confidence calibration.

        Guidelines:

        - Deterministic tool outputs (calculator, etc.) are highly reliable.
        - Retrieved knowledge should be treated as evidence from the user's document collection.
        - Web evidence should be used only when it supports the final answer.
        - Penalize unsupported claims or hallucinations.
        - Prefer answers that correctly combine multiple evidence sources.

        Choose exactly one winner.

        Return:
        - winner (A or B)
        - confidence
        - reasoning
        """

    response = judge_llm.invoke(prompt)

    emit(JudgeEvent(
        winner=response.winner,
        reasoning=response.reasoning,
        confidence=response.confidence,
    ))

    return {
        "judge_result": response
    }