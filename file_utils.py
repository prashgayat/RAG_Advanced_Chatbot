from langchain.document_loaders import UnstructuredFileLoader
from semantic_text_splitter import TextSplitter
from langchain.docstore.document import Document

def file_loader(file_path):
    # Load content from uploaded document
    loader = UnstructuredFileLoader(file_path)
    documents = loader.load()

    # Merge into a single raw string
    full_text = "\n".join([doc.page_content for doc in documents])

    # Use semantic chunking for intelligent splits
    splitter = TextSplitter(
        chunk_size=300,               # adjust based on your use case
        chunk_overlap=50,
        model_name="all-MiniLM-L6-v2" # lightweight & fast
    )
    chunks = splitter.split_text(full_text)

    # Wrap back into LangChain Document objects
    return [Document(page_content=chunk) for chunk in chunks]
