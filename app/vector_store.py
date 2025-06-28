# app/vector_store.py

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from typing import List, Optional


class SimpleListEmbedder(Embeddings):
    def __init__(self, vectors: List[List[float]]):
        self.vectors = vectors
        self.i = 0

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        # Used for creating FAISS index
        return self.vectors

    def embed_query(self, text: str) -> List[float]:
        # Dummy implementation to satisfy abstract class
        return [0.0] * len(self.vectors[0])  # Match embedding dimension


def create_vector_store(documents: List[Document], vectors: List[List[float]]) -> FAISS:
    embedder = SimpleListEmbedder(vectors)
    return FAISS.from_documents(documents, embedding=embedder)


def save_vector_store(vectorstore: FAISS, persist_path: str):
    vectorstore.save_local(folder_path=persist_path)


def load_vector_store(persist_path: str, embedder: Optional[Embeddings]) -> FAISS:
    return FAISS.load_local(
        folder_path=persist_path,
        embeddings=embedder,
        allow_dangerous_deserialization=True
    )
