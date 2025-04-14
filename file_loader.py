
import os
import tempfile
from langchain.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, UnstructuredExcelLoader

def load_documents(uploaded_files):
    documents = []
    for file in uploaded_files:
        try:
            suffix = os.path.splitext(file.name)[-1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name

            if suffix == ".pdf":
                loader = PyPDFLoader(tmp_path)
            elif suffix == ".txt":
                loader = TextLoader(tmp_path)
            elif suffix == ".docx":
                loader = Docx2txtLoader(tmp_path)
            elif suffix == ".xlsx":
                loader = UnstructuredExcelLoader(tmp_path)
            else:
                continue

            documents.extend(loader.load())
            os.remove(tmp_path)
        except Exception as e:
            print(f"Error loading {file.name}: {str(e)}")
    return documents
