# 🤖 Robust RAG Chatbot — Hybrid Search, Hallucination Prevention, Re-ranking

This is a domain-specific RAG (Retrieval-Augmented Generation) chatbot designed for high-accuracy question answering over user-uploaded documents using hybrid retrieval and hallucination safeguards.

---

## 🎯 Key Features

### ✅ Multi-format Upload Support
- Supports `.pdf`, `.docx`, `.txt`, and `.xlsx` formats.

### ✅ Semantic Chunking
- Uses Recursive Character Text Splitter for meaningful chunk formation.

### ✅ Hybrid Search (Semantic + Keyword)
- Combines keyword-based (BM25) and semantic embedding search (HuggingFace) for improved recall and precision.

### ✅ Re-ranking
- Uses a cross-encoder model (`sentence-transformers`) to re-rank retrieved documents.

### ✅ Hallucination Prevention
- If no reliable context is found, the system prevents the LLM from generating an answer and shows a warning instead.

### ✅ Clean UI
- Built with Streamlit, fully functional inside GitHub Codespaces.

### ✅ Modular Design
- Organized code: `file_utils.py`, `retriever_utils.py`, `llm_answer.py`, `reranker.py`, and `app.py`.

---

## ⚙️ Tech Stack

| Component           | Technology / Model                                  |
|--------------------|-----------------------------------------------------|
| LLM                | **OpenAI GPT-3.5 Turbo** via OpenAI API              |
| Semantic Embedding | HuggingFace: `all-MiniLM-L6-v2`                      |
| Keyword Search     | BM25 (`BM25Retriever`)                               |
| Vector Store       | FAISS                                                |
| Re-ranking         | `sentence-transformers` CrossEncoder model          |
| UI Framework       | Streamlit                                            |
| Orchestration      | LangChain                                            |
| Dev Environment    | GitHub Codespaces                                    |

---

## 🚀 Setup (GitHub Codespaces Recommended)

1. Open the repo in GitHub Codespaces.
2. Install dependencies:
    ```bash
    pip install --force-reinstall -r requirements.txt
    ```
3. Run the app:
    ```bash
    streamlit run app.py
    ```
4. Copy the **external URL** to access the chatbot.

---

## 🔐 API Key Setup (OpenAI)

Create a file at `.streamlit/secrets.toml` (do **not** commit it):

```toml
OPENAI_API_KEY = "your-openai-key-here"
```

> ⚠️ Never push secrets to GitHub. Use Codespaces' secret management or manual entry.

---

## 🛡️ Hallucination Guard

If no meaningful context is retrieved from the uploaded documents, the app avoids calling the LLM and shows:

> ⚠️ Sorry, I couldn't find enough information to answer that question based on the uploaded files.

---

## 🧩 File Structure

```
├── app.py                 # Streamlit app logic
├── file_utils.py          # Handles upload and chunking
├── retriever_utils.py     # Hybrid retriever: FAISS + BM25
├── reranker.py            # Re-ranking via cross-encoder
├── llm_answer.py          # Final LLM answer generation
├── requirements.txt
├── .streamlit/secrets.toml
└── README.md
```

---

## ✅ Final Notes

- Prevents hallucinations with fallback messaging.
- Updated to support latest LangChain deprecations.
- Built for modularity and easy deployment.

---

🎓 Happy RAGging! 🚀


