from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DB_DIR = "vector_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

_vector_store = None


def get_vector_store():
    global _vector_store

    if _vector_store is None:
        _vector_store = Chroma(
            persist_directory=DB_DIR,
            embedding_function=embedding_model,
        )

    return _vector_store