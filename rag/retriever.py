from langchain_core.documents import Document

from .vector_store import get_vector_store

def retrieve(query: str, k: int = 5, threshold: float = 0.5):

    db = get_vector_store()

    results = db.similarity_search_with_relevance_scores(query, k=5)

    if not results:
        return []

    best = results[0][1]

    docs = [
        doc
        for doc, score in results
        if score >= max(threshold, best - 0.1)
    ]

    return docs


def retrieve_text(query: str, k: int = 5, threshold: float = 0.7):

    docs = retrieve(query, k, threshold)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )