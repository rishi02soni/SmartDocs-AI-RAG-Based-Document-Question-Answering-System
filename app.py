import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import Ollama
import os
 
st.set_page_config(page_title="SmartDocs AI", layout="wide")

st.title("📚 SmartDocs AI - RAG Chatbot")
st.write("Upload PDF or TXT files and ask questions.")

uploaded_file = st.file_uploader("Upload File", type=["pdf", "txt"])

if uploaded_file:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(uploaded_file.name)
    else:
        loader = TextLoader(uploaded_file.name)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(texts, embeddings)

    st.success("File processed successfully!")

    query = st.text_input("Ask a question:")

    if query:
        docs = db.similarity_search(query)

        llm = Ollama(model="llama3")

        chain = load_qa_chain(llm, chain_type="stuff")

        response = chain.run(input_documents=docs, question=query)

        st.subheader("Answer:")
        st.write(response)
