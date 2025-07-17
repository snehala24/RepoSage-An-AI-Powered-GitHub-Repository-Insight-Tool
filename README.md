# RepoSage – An AI-Powered GitHub Repository Insight Tool 🔍

RepoSage is an AI-driven assistant that helps users quickly understand and explore any GitHub repository. By simply providing a GitHub repository URL and asking natural language questions, users can gain instant insights into the project’s structure, functionality, technologies used, and more.

> ⚡ Ideal for developers, recruiters, students, and tech enthusiasts who want to grasp unfamiliar codebases quickly.

---

## 🚀 Features

- 🔗 **GitHub Repo Analyzer**: Just paste a GitHub URL to begin exploration.
- 🤖 **LLM-Powered Q&A**: Ask any questions about the repository (e.g., “What is the purpose of this project?” or “Which libraries are used?”).
- 🧠 **Embeddings + Vector DB**: Semantic search over repository contents using FAISS.
- ⚡ **Gemini 1.5 Flash**: Cost-effective and fast large language model used for generating responses.
- 🖥️ **FastAPI Backend**: Robust and scalable API handling all logic and LLM workflows.
- 🌐 **Streamlit Frontend**: Clean and interactive UI for submitting repo links and questions.

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python
- **LLM**: Gemini 1.5 Flash (Google)
- **Frontend**: Streamlit / HTML (FastAPI templating)
- **Vector Store**: FAISS
- **Embeddings**: Gemini Embedding API
- **Utilities**: GitPython, PyMuPDF, langchain

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/snehala24/RepoSage-An-AI-Powered-GitHub-Repository-Insight-Tool.git
cd RepoSage-An-AI-Powered-GitHub-Repository-Insight-Tool

