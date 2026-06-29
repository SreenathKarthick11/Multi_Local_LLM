from llm import debate_llm,critique_llm
from state import DebateState
from tools.resource_manager import get_resources,format_resource

def debater_a(state: DebateState):

    context,descision,retrive_descision = get_resources(state["question"])

    prompt = f"""
        You are Debater A.

        Your goal:
        - Answer accurately.
        - Use evidence when available.
        - Avoid speculation.
        - If evidence is insufficient, explicitly state uncertainty.
        -   When retrieved documents are available,
            base your answer primarily on them.
            Quote or summarize them directly.
            Do not ignore retrieved evidence.

        Question:
        {state["question"]}

        Web Search Used:
        {descision.need_search}

        Tool Results:
        {context.tools}

        Web Search Results:
        {context.web_evidence}

        Retrive from Documents:
        {retrive_descision.use_rag}

        Retrieved Documents:
        {context.rag_evidence}

        Return:
        - answer
        - confidence (0-1)
        - reasoning

        Be concise but accurate.
        """

    response = debate_llm.invoke(prompt)

    return {
        "search_used_a": descision.need_search,
        "rag_used_a" : retrive_descision.use_rag,
        "resource_bank_a" : [context],
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
        {format_resource(state["resource_bank_a"][-1])}

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