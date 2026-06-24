# tools/search_helper.py
from llm import search_llm
from tools.search import search_web

def get_evidence(question: str):

    decision = search_llm.invoke(
        f"""
        Question:
        {question}

        Decide whether web search is necessary.

        Search only if:
        - factual information is needed
        - current information is needed
        - uncertainty is high

        Do not search for:
        - simple math
        - common definitions
        - trivial reasoning

        Return:
        need_search
        search_query
        confidence
        reason
        """
    )

    should_search = (
        decision.need_search
        or decision.confidence < 0.6
    )

    if not should_search:
        return "", decision


    try:
        evidence = search_web(
            decision.search_query
        )
        return evidence, decision

    except Exception:
        return "", decision