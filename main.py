from app.rag_pipeline import answer_question

query = "What does the main Python file do in this repo?"
response = answer_question(query)
print("🤖 Answer:", response)
