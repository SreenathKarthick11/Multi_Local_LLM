from llm import debate_llm,critique_llm
from state import DebateState
from tools.search import search_web

def debater_b(state: DebateState):

    evidence = search_web(state["question"]+" different viewpoints",max_results=3)

    prompt = f"""
            You are Debater B.

            Consider alternative interpretations.

            Question:
            {state["question"]}

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
        "answer_b": response,
        "evidence_b": evidence
    }

def critique_b(state: DebateState):

    prompt = f"""
            You are Debater B.

            Question:
            {state["question"]}

            Your Evidence:
            {state['evidence_b']}

            Your Answer:
            {state["answer_b"].answer}

            Opponent Answer:
            {state["answer_a"].answer}

            Opponent Reasoning:
            {state["answer_a"].reasoning}

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
        "critique_b": response
    }

def revise_b(state:DebateState):

    critique=state["critique_a"]

    prompt = f"""
        You are Debater B.

        Original Answer:
        {state["answer_b"].answer}

        Original Reasoning:
        {state["answer_b"].reasoning}

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
        "revised_answer_b": response
    }