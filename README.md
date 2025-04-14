# 🤖 Robust RAG Chatbot — Hybrid Search, Hallucination Prevention, Re-ranking

This is a domain-specific RAG (Retrieval-Augmented Generation) chatbot designed for high-accuracy question answering over user-uploaded documents using hybrid retrieval and hallucination safeguards.

---

## 🎯 Key Features

✅ **Multi-format Upload Support**  
Supports `.pdf`, `.docx`, `.txt`, and `.xlsx` formats.

✅ **Semantic Chunking**  
Uses Recursive Character Text Splitter for meaningful chunk formation.

✅ **Hybrid Search (Keyword + Semantic)**  
Combines keyword-based search (BM25-style) and semantic embeddings (HuggingFace) to improve recall and precision.

✅ **Re-ranking**  
Ranks retrieved results using a cross-encoder model (`sentence-transformers`).

✅ **Hallucination Prevention**  
Detects when no reliable context is retrieved and shows a fallback message instead of allowing the LLM to guess.

✅ **Clean UI**  
Built with Streamlit for fast local testing, currently deployed via GitHub Codespaces.

✅ **Modular Design**  
Clearly separated files: `file_utils.py`, `retriever_utils.py`, `llm_answer.py`, `reranker.py`, and `app.py`.

---

## ⚙️ Tech Stack

- `LangChain` for retrieval pipeline
- `HuggingFace` for semantic embeddings
- `sentence-transformers` for re-ranking
- `OpenRouter` (Zephyr 7B) as the LLM interface
- `Streamlit` for UI

---

## 🚀 Setup (GitHub Codespaces Recommended)

1. Fork the repo and open in GitHub Codespaces.
2. Run the following in terminal:

```bash
pip install --force-reinstall -r requirements.txt
streamlit run app.py
```

3. Paste the external URL provided by Streamlit.
4. Upload your documents, type a query, and view answers with reliability fallback.

---

## 🛡️ Hallucination Guard

If no reliable documents are retrieved for a query, the app will **not** forward the question to the LLM. Instead, it will show:

```
⚠️ Sorry, I couldn't find enough information to answer that question based on the uploaded files.
```

---

## 🔐 API

Requires OpenRouter API key (free tier available). Add it inside `.streamlit/secrets.toml` like:

```toml
OPENROUTER_API_KEY = "your-key-here"
```

> Do **NOT** commit secrets to GitHub. Add it manually in Codespaces only.

---

## 🧩 File Structure

```bash
├── app.py                 # Streamlit UI
├── file_utils.py          # Handles file loading + chunking
├── retriever_utils.py     # Hybrid retriever setup
├── reranker.py            # Cross-encoder based re-ranking
├── llm_answer.py          # Generates final LLM answer
├── requirements.txt
├── .streamlit/secrets.toml
└── README.md
```

---

## ✅ Final Notes

- Avoids hallucinations with proper fallbacks
- Updated to handle all recent LangChain deprecations
- Easy to port to Streamlit Community Cloud post-Codespaces testing

---

Happy RAGging 🎓🚀

