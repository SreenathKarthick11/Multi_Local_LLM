from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(folder: str = "documents"):
    folder = Path(folder)
    folder.mkdir(exist_ok=True)
    
    docs = []

    for pdf in Path(folder).rglob("*.pdf"):
        loader = PyPDFLoader(str(pdf))
        docs.extend(loader.load())

    return docs


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    return splitter.split_documents(documents)