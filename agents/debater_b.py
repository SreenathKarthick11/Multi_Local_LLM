from llm import debate_llm,critique_llm
from state import DebateState
from tools.search import search_web
from tools.search_helper import get_evidence

def debater_b(state: DebateState):


    evidence, decision = get_evidence(state["question"]+" different viewpoints")

    prompt = f"""
        You are Debater B.

        Your role is to challenge common assumptions.

        Consider:
        - alternative explanations
        - edge cases
        - hidden assumptions
        - counterarguments

        Question:
        {state["question"]}

        Web Search Used:
        {decision.need_search}

        Evidence:
        {evidence}

        Return:
        - answer
        - confidence
        - reasoning

        Be concise but critical.
        """

    response = debate_llm.invoke(prompt)

    return {
        "history_b": [response],
        "search_used_b": decision.need_search,
        "evidence_bank_b": [evidence]
    }

def critique_b(state: DebateState):

    my_answer=state["history_b"][-1]
    opponent_answer=state["history_a"][-1]

    prompt = f"""
        You are Debater B.

        Question:
        {state["question"]}

        Your Recent Evidence:
        {state["evidence_bank_b"][-1]}

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
        "critique_b": response
    }

def revise_b(state:DebateState):

    critique=state["critique_a"]
    latest=state["history_b"][-1]

    prompt = f"""
        You are Debater B.

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
        {len(state["history_b"])}

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
        "history_b":[response]
    }