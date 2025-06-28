from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.utils import get_api_key


def embed_chunks(chunks):
    """
    Convert chunk dicts into LangChain Document objects.
    """
    return [
        Document(
            page_content=chunk["content"],
            metadata={
                "file_path": chunk["file_path"],
                "chunk_id": chunk["chunk_id"]
            }
        )
        for chunk in chunks
    ]


def get_embedder():
    """
    Returns a LangChain-compatible GoogleGenerativeAIEmbeddings instance.
    """
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=get_api_key()
    )
