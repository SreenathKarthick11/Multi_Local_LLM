# tools/search_helper.py
from llm import search_llm
from tools.search import search_web

def get_evidence(question: str):

    decision = search_llm.invoke(
        f"""
        Question:
        {question}

        Determine whether web search would significantly improve answer quality.

        If the answer can be obtained completely
        from local retrieved documents,

        DO NOT search the web.

        Search is REQUIRED for:

        - current events
        - dates
        - statistics
        - people
        - companies
        - scientific facts
        - historical facts
        - geographic facts

        Search is NOT required for:

        - simple arithmetic
        - basic definitions
        - common knowledge
        - logic puzzles
        - reasoning tasks

        Return:

        - need_search
        - confidence
        - search_query
        - reason
        """
    )

    should_search = (
        decision.need_search
        or decision.confidence < 0.3
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