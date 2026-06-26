from llm import debate_llm,critique_llm
from state import DebateState
from tools.search_helper import get_evidence
from tools.tool_helper import get_tool

def debater_a(state: DebateState):

    evidence, decision = get_evidence(state["question"])
    tool = get_tool(state["question"])

    prompt = f"""
        You are Debater A.

        Your goal:
        - Answer accurately.
        - Use evidence when available.
        - Avoid speculation.
        - If evidence is insufficient, explicitly state uncertainty.

        Question:
        {state["question"]}

        Web Search Used:
        {decision.need_search}

        Tool Results:
        {tool.output if tool else "None"}

        Search Results:
        {evidence}

        Return:
        - answer
        - confidence (0-1)
        - reasoning

        Be concise but accurate.
        """

    response = debate_llm.invoke(prompt)

    return {
        "evidence_bank_a": [evidence],
        "search_used_a": decision.need_search,
        "tool_bank_a": [tool] if tool else [],
        "history_a":[response]
    }

def critique_a(state: DebateState):

    my_answer=state["history_a"][-1]
    opponent_answer=state["history_b"][-1]

    prompt = f"""
        You are Debater A.

        Question:
        {state["question"]}

        Your Recent Evidence:
        {state["evidence_bank_a"][-1]}

        Your latest answer:
        {my_answer.answer}

        Opponent answer:
        {opponent_answer.answer}

        Opponent reasoning:
        {opponent_answer.reasoning}

        Analyze ONLY the opponent answer.

        Find:

        1. Factual mistakes.
        2. Unsupported assumptions.
        3. Weak reasoning.
        4. Possible hallucinations.

        Do not repeat the answer.

        Return:
        - weaknesses
        - hallucination_risk (1-5)
        - suspected_hallucinations
        """

    response = critique_llm.invoke(prompt)

    return {
        "critique_a": response
    }

def revise_a(state:DebateState):

    critique=state["critique_b"]
    latest=state["history_a"][-1]

    prompt = f"""
        You are Debater A.

        Question:
        {state["question"]}

        Your previous answer:
        {latest.answer}

        Your reasoning:
        {latest.reasoning}

        Critique received:
        {chr(10).join("- " + w for w in critique.weaknesses)}

        Possible hallucinations:
        {chr(10).join("- " + h for h in critique.suspected_hallucinations)}

        Hallucination risk:
        {critique.hallucination_risk}/5

        Previous debate rounds:
        {len(state["history_a"])}

        Task:

        - Keep correct parts.
        - Fix weaknesses if valid.
        - Remove unsupported claims.
        - Increase factual accuracy.
        - Do not change the answer unless justified.

        Return:
        - answer
        - confidence
        - reasoning
        """

    response = debate_llm.invoke(prompt)

    return {
        "history_a":[response]
    }