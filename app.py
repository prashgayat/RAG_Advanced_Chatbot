import streamlit as st
from file_utils import file_loader
from llm_answer import embed_and_store, get_qa_chain

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🧠 Domain-Specific RAG Chatbot")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_path = f"./{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        docs = file_loader(file_path)
        if not docs:
            st.error("❗ No text chunks created. Please check the document format or content.")
        else:
            st.success(f"✅ Loaded {len(docs)} chunks.")
            vs = embed_and_store(docs)
            qa_chain = get_qa_chain(vs)

            query = st.text_input("Ask a question from the document:")
            if query:
                response = qa_chain.run(query)
                st.markdown("**💬 Response:**")
                st.write(response)

    except Exception as e:
        st.error(f"🔥 Error: {e}")
