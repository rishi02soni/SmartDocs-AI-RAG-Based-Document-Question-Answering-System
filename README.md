# SmartDocs AI - RAG Based Document Chatbot

SmartDocs AI is a Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload PDF or TXT documents and ask questions directly from their content.

Built using:

- Python
- Streamlit
- LangChain
- FAISS Vector Database
- HuggingFace Embeddings
- Ollama (Llama3)

---

# Features

- Upload PDF documents
- Upload TXT files
- Ask questions from uploaded files
- Fast semantic search using FAISS
- Local LLM support with Ollama
- Clean Streamlit UI
- No paid API required

---

# Project Structure
```
smartdocs-ai/
│── app.py
│── requirements.txt
│── README.md
│── data/

```
# Installation
> 1 Clone Repository
```
git clone https://github.com/yourusername/smartdocs-ai.git
cd smartdocs-ai
```
> 2 Install Dependencies
```
pip install -r requirements.txt
```
> 3 Install Ollama

### Download Ollama:
```
https://ollama.com
```
### Then install model:
```
ollama pull llama3
```
# Run Project
```
streamlit run app.py
```
# How It Works
- User uploads a file
- Text is extracted from document
- Content is split into chunks
- Embeddings are created
- Stored in FAISS vector DB
- User asks question
- Relevant chunks retrieved
- LLM generates final answer

# Future Improvements
- Chat memory
- Multi-document support
- Authentication
- Dark mode UI
- Deployment on cloud
- Export answers

# Author
```
rishi02soni
```
