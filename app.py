import streamlit as st
from file_utils import load_documents
from retriever_utils import prepare_retrievers
from reranker import rerank_results
from llm_answer import llm_answer

st.set_page_config(page_title="Robust RAG Chatbot with Hybrid Search + Re-ranking")
st.title("📚 Robust RAG Chatbot with Hybrid Search + Re-ranking")

# File upload UI
uploaded_files = st.file_uploader(
    "Upload documents", accept_multiple_files=True, type=["pdf", "txt", "docx", "xlsx"]
)

# Load and process uploaded files
if uploaded_files:
    uploaded_docs = load_documents(uploaded_files)

    try:
        hybrid_retriever, keyword_retriever, chunks = prepare_retrievers(uploaded_docs)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    # Query input
    query = st.text_input("Ask a question about the documents:")

    if query:
        # Hybrid retrieval (combine both)
        docs = hybrid_retriever.similarity_search(query)
        docs += keyword_retriever.get_relevant_documents(query)

        # Optional re-ranking
        if rerank_results and docs:
            docs = rerank_results(query, docs)

        # Hallucination guard
        if not docs or len(docs) == 0:
            st.warning("❗ Sorry, I couldn't find enough information to answer that question based on the uploaded files.")
        else:
            answer = llm_answer(query, docs)
            st.write(answer)
else:
    st.info("📁 Please upload documents to begin.")



