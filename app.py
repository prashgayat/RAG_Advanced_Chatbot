
import streamlit as st
import gc
import os
from file_loader import load_documents
from retriever import prepare_retrievers
from reranker import rerank_results
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📚 Robust RAG Chatbot with Hybrid Search + Re-ranking")

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "txt", "docx", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Loading and indexing documents..."):
        docs = load_documents(uploaded_files)
        if not docs:
            st.warning("No readable text found in the uploaded documents.")
        else:
            faiss_store, bm25, chunks = prepare_retrievers(docs)
            st.session_state["faiss_store"] = faiss_store
            st.session_state["bm25"] = bm25
            st.session_state["chunks"] = chunks
            gc.collect()
            st.success("Documents processed successfully!")

query = st.text_input("Ask a question about the documents:")

api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API Key not found. Please set it in Streamlit secrets or your environment.")
    st.stop()

if query and "faiss_store" in st.session_state:
    with st.spinner("Retrieving relevant information..."):
        bm25_docs = st.session_state["bm25"].get_relevant_documents(query)
        faiss_docs = st.session_state["faiss_store"].similarity_search(query, k=5)
        combined_docs = bm25_docs + faiss_docs
        reranked_docs = rerank_results(query, combined_docs)

        if not reranked_docs:
            st.warning("The information regarding the given query does not exist in the document(s) provided.")
        else:
            llm = OpenAI(temperature=0)
            prompt_template = PromptTemplate(
                input_variables=["context", "question"],
                template=""""
You are a helpful assistant trained to answer questions strictly based on the provided documents.
If the answer is not in the documents, say:
"The information regarding the given query does not exist in the document(s) provided."

=== Documents ===
{context}

=== Question ===
{question}

Answer:
"""
            )
            chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)
            answer = chain.run(input_documents=reranked_docs, question=query)
            st.markdown(answer)
