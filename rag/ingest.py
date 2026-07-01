# rag/ingest.py
from .splitter import load_documents, split_documents
from .vector_store import get_vector_store


def ingest_documents(folder: str = "documents") -> int:
    """
    Loads all PDFs in `folder`, chunks them, and (re)builds the vector store.
    Returns the number of chunks ingested (0 if no PDFs were found).
    """
    docs = load_documents(folder)

    if not docs:
        return 0

    chunks = split_documents(docs)

    db = get_vector_store()
    db.reset_collection()
    db.add_documents(chunks)

    return len(chunks)


def main():
    count = ingest_documents()
    if count == 0:
        print("No PDFs found in documents/")
    else:
        print(f"Ingested {count} chunks.")


if __name__ == "__main__":
    main()