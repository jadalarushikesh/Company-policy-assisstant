from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langgraph.graph import StateGraph
from typing import TypedDict
import os
from dotenv import load_dotenv

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv()

# ---------------------------
# Embeddings
# ---------------------------
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------
# Vector Store
# ---------------------------
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# ---------------------------
# LLM (Groq - stable model)
# ---------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ latest working model
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------
# State Definition
# ---------------------------
class State(TypedDict):
    question: str
    answer: str
    sources: list

# ---------------------------
# RAG Node
# ---------------------------
def rag_node(state: State):

    try:
        # Retrieve documents
        docs = retriever.invoke(state["question"])

        if not docs:
            return {
                "answer": "⚠️ No relevant documents found.",
                "sources": []
            }

        # Prepare context
        context = "\n\n".join([doc.page_content for doc in docs])
        sources = [doc.metadata.get("source", "Unknown") for doc in docs]

        # Prompt
        prompt = f"""
You are a professional company policy assistant.

Use the context below to answer the question clearly.

Context:
{context}

Question:
{state['question']}

Answer:
"""

        # LLM call
        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": sources
        }

    except Exception as e:
        return {
            "answer": f"⚠️ Error occurred: {str(e)}",
            "sources": []
        }

# ---------------------------
# Build Graph
# ---------------------------
builder = StateGraph(State)

builder.add_node("rag_node", rag_node)
builder.set_entry_point("rag_node")
builder.set_finish_point("rag_node")

rag_graph = builder.compile()