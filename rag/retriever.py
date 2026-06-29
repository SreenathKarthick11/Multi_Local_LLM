from langchain_core.documents import Document

from .vector_store import get_vector_store


def retrieve(query: str, k: int = 3) -> list[Document]:

    db = get_vector_store()

    return db.similarity_search(
        query,
        k=k,
    )


def retrieve_text(query: str, k: int = 3) -> str:

    docs = retrieve(query, k)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )