import os
import tempfile

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader


def read_file(uploaded_file):
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        if file_extension == ".pdf":
            loader = PyPDFLoader(tmp_path)
        elif file_extension == ".docx":
            loader = Docx2txtLoader(tmp_path)
        else:
            raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")

        documents = loader.load()
        return "\n".join([doc.page_content for doc in documents])
    finally:
        os.unlink(tmp_path)