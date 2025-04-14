
# 🧠 Domain-Specific RAG Chatbot (Multi-Format, Robust, Streamlit Ready)

## 🎯 Goal
Build a domain-specific chatbot using Retrieval-Augmented Generation (RAG) that supports:
- Multiple file types (PDF, DOCX, TXT, XLSX)
- Hybrid retrieval (keyword + semantic)
- Semantic re-ranking
- Structured prompting with hallucination safeguards

## 🚀 Features
✅ Multi-format File Support  
✅ Semantic Chunking  
✅ Hybrid Search (BM25 + FAISS)  
✅ Re-ranking (CrossEncoder)  
✅ Structured Prompting with Guardrails  
✅ Disclaimer for Missing Info  
✅ Streamlit UI (Cloud Ready)

## 🛠 Setup
Install & run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
```

To deploy on [Streamlit Cloud](https://streamlit.io/cloud):
1. Push to GitHub
2. Set OPENAI_API_KEY in Secrets
3. Deploy with `app.py` as entrypoint
