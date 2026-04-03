from src.chunk import chunk_documents
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def build_vector_db():

    if os.path.exists("chroma_db"):
        print("Vector DB already exists")
        return

    print("Creating new Vector DB...")

    chunks = chunk_documents("default_policies")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    db.persist()
    print("DB created successfully!")

if __name__ == "__main__":
    build_vector_db()