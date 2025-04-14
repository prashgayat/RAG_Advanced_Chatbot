# After loading documents and setting up retriever and reranker...

query = st.text_input("Ask a question about the documents:")

if query and uploaded_docs:
    docs = hybrid_retriever.retrieve(query)
    
    # If reranking is enabled
    if rerank_results and docs:
        docs = rerank_results(query, docs)
    
    # Hallucination prevention check
    if not docs or len(docs) == 0:
        st.warning("❗ Sorry, I couldn’t find enough information to answer that question based on the uploaded documents.")
    else:
        context = "\n\n".join([doc.page_content for doc in docs[:3]])  # Use top 3 relevant chunks
        prompt = f"""You are a helpful assistant. Use the below context to answer the question.
If you cannot find the answer in the context, say you don’t know.

Context:
{context}

Question: {query}
Answer:"""

        response = llm.invoke(prompt)
        st.success(response)
