from .splitter import load_documents, split_documents
from .vector_store import get_vector_store


def main():

    docs = load_documents()

    if not docs:
        print("No PDFs found in documents/")
        return


    chunks = split_documents(docs)

    db = get_vector_store()

    # Remove old chunks during development.
    db.reset_collection()

    db.add_documents(chunks)



if __name__ == "__main__":
    main()