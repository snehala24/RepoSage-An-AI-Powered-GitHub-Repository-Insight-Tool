import streamlit as st
from app.github_loader import download_repo
from app.chunker import load_files_from_repo, chunk_files
from app.embedder import get_embedder, embed_chunks
from app.vector_store import create_vector_store, save_vector_store
from app.rag_pipeline import answer_question


st.set_page_config(page_title="GitHub Repo Assistant", layout="wide")
st.title("🤖 GitHub Repository Assistant")
st.markdown("Enter a GitHub repository URL and ask a question about its codebase.")

with st.form("repo_form"):
    repo_url = st.text_input("🔗 GitHub Repository URL", placeholder="https://github.com/user/repo")
    question = st.text_input("❓ Ask a question about the repo", placeholder="What does the main.py file do?")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not repo_url or not question:
        st.warning("Please fill in both fields.")
    else:
        try:
            with st.spinner("📦 Downloading and processing repo..."):
                repo_path = download_repo(repo_url, download_root="data/raw_repos")
                files = load_files_from_repo(repo_path)
                chunks = chunk_files(files)

                if not chunks:
                    st.error("No valid content found in the repository.")
                    st.stop()

                docs = embed_chunks(chunks)
                embedder = get_embedder()
                vectors = embedder.embed_documents([doc.page_content for doc in docs])
                vectorstore = create_vector_store(docs, vectors)
                save_vector_store(vectorstore, persist_path="data/vector_store")

            with st.spinner("💬 Answering your question..."):
                answer = answer_question(question)

            st.success("✅ Answer:")
            st.markdown(f"**{answer}**")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
