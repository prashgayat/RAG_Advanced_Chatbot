import streamlit as st
from file_utils import load_documents
from retriever_utils import prepare_retrievers
from reranker import rerank_results
from llm_answer import llm_answer  # Make sure this function exists and handles empty input

st.set_page_config(page_title="Robust RAG Chatbot with Hybrid Search + Re-ranking")

st.title("📚 Robust RAG Chatbot with Hybrid Search + Re-ranking")

# Upload documents
uploaded_files = st.file_uploader(
    "Upload documents", accept_multiple_files=True, type=["pdf", "txt", "docx", "xlsx"]
)

if uploaded_files:
    docs = load_documents(uploaded_files)

    # Create hybrid retriever
    hybrid_retriever = prepare_retrievers(docs)

    # User query input
    query = st.text_input("Ask a question about the documents:")

    if query:
        # Hybrid retrieval
        retrieved_docs = hybrid_retriever.get_relevant_documents(query)

        # Re-ranking
        if rerank_results and retrieved_docs:
            retrieved_docs = rerank_results(query, retrieved_docs)

        # Hallucination prevention
        if not retrieved_docs or len(retrieved_docs) == 0:
            st.warning("❗ I couldn't find enough relevant information to answer your question from the uploaded documents.")
        else:
            # Get answer from LLM
            answer = llm_answer(query, retrieved_docs)
            st.success(answer)
else:
    st.info("📁 Please upload documents to begin.")



