
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.retrievers import BM25Retriever
from langchain.text_splitter import RecursiveCharacterTextSplitter

def prepare_retrievers(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    faiss_store = FAISS.from_documents(chunks, embeddings)
    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = 5

    return faiss_store, bm25, chunks
