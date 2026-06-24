from llm import debate_llm,critique_llm
from state import DebateState
from tools.search import search_web
from tools.search_helper import get_evidence

def debater_a(state: DebateState):

    evidence, decision = get_evidence(state["question"])

    prompt = f"""
        You are Debater A.

        Question:
        {state["question"]}

        Search Used:
        {decision.need_search}


        Search Results:
        {evidence}

        Answer the question using the search results.

        Return:
        - answer
        - confidence
        - reasoning
        """

    response = debate_llm.invoke(prompt)

    return {
        "evidence_bank_a": [evidence],
        "search_used_a": decision.need_search,
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

        Your Answer:
        {my_answer.answer}

        Opponent Answer:
        {opponent_answer.answer}

        Opponent Reasoning:
        {opponent_answer.reasoning}

        Analyze the opponent's answer.

        Identify:

        1. Weaknesses in reasoning.
        2. Statements that may be hallucinated,
        fabricated, or unsupported.
        3. Overall hallucination risk from 1 to 5.

        Be concise.
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

        Original Answer:
        {latest.answer}

        Original Reasoning:
        {latest.reasoning}

        Opponent Weaknesses:
        {chr(10).join("- " + w for w in critique.weaknesses)}

        Suspected Hallucinations:
        {chr(10).join("- " + h for h in critique.suspected_hallucinations)}

        Hallucination Risk:
        {critique.hallucination_risk}/5

        Revise your answer if necessary.

        Pay special attention to suspected hallucinations.

        Return:
        - answer
        - confidence
        - reasoning
        """

    response = debate_llm.invoke(prompt)

    return {
        "history_a":[response]
    }