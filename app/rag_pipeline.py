# app/rag_pipeline.py

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from app.utils import get_api_key
from app.vector_store import load_vector_store, SimpleListEmbedder


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=get_api_key(),
        temperature=0.2,
        convert_system_message_to_human=True  # ✅ Final fix applied here
    )


def build_qa_chain():
    # Dummy embedder to satisfy FAISS requirement
    dummy_embedder = SimpleListEmbedder([[0.0] * 768])
    vectorstore = load_vector_store("data/vector_store", embedder=dummy_embedder)
    retriever = vectorstore.as_retriever()
    llm = get_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


def answer_question(query: str) -> str:
    chain = build_qa_chain()
    return chain.invoke(query)
