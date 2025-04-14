from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.retrievers import BM25Retriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import EnsembleRetriever

def prepare_retrievers(docs):
    # Chunk documents
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Embedding model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Vector store retriever (semantic)
    faiss_store = FAISS.from_documents(chunks, embeddings)
    faiss_retriever = faiss_store.as_retriever(search_kwargs={"k": 5})

    # BM25 retriever (keyword)
    bm25 = BM25Retriever.from_documents(chunks)
    bm25.k = 5

    # Combine both using EnsembleRetriever
    hybrid_retriever = EnsembleRetriever(
        retrievers=[faiss_retriever, bm25],
        weights=[0.5, 0.5]
    )

    return hybrid_retriever



