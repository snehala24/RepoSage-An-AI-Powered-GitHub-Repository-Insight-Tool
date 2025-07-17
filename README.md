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

## 🗂️ Folder Structure


RepoSage-An-AI-Powered-GitHub-Repository-Insight-Tool/
│
├── app/
│ ├── init.py
│ ├── pipeline.py # Main function to handle repo processing and response
│ ├── llm_suggester.py # Gemini 1.5 Flash prompt handling
│ └── vector_store.py # Embedding & FAISS vector database logic
│
├── static/
│ └── assets/ # Optional icons, images, and styles
│
├── templates/
│ └── index.html # Frontend HTML form
│
├── .env # Store Gemini API Key securely
├── requirements.txt # All dependencies listed
├── streamlit_app.py # Optional Streamlit frontend for testing
└── main.py # FastAPI app with endpoints


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

-'''
2. Create Virtual Environment

python -m venv venv
source venv/bin/activate        # For Linux/macOS
.\venv\Scripts\activate         # For Windows

3. Install Requirements

pip install -r requirements.txt

4. Add Your Gemini API Key

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here

5. Run the FastAPI App

uvicorn main:app --reload

Visit: http://127.0.0.1:8000
🔄 (Optional) Run Streamlit Frontend

streamlit run streamlit_app.py

⚙️ How It Works
🧾 Input

    User submits a GitHub repository URL

    User types any natural language question (e.g. "What does this repo do?")

🧪 Processing

    Repository is cloned locally

    .py, .md, .txt, etc. files are parsed and chunked

    FAISS vector store is built using Gemini embeddings

🔍 Querying

    User's question is embedded

    Relevant chunks are retrieved from FAISS

    Gemini 1.5 Flash generates the final answer via LangChain prompts

📤 Output

    Final answer is displayed on the UI (HTML or Streamlit)
