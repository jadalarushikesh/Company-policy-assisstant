# Company-policy-assisstant

# 🧠 Company Policy Assistant (RAG Project)

## 🚀 Overview

The **Company Policy Assistant** is an AI-powered chatbot built using **Retrieval-Augmented Generation (RAG)**.
It helps users quickly retrieve and understand company policies from documents instead of manually searching through files.

---

## 🎯 Problem Statement

Employees often struggle to find specific policy details from large documents.
This project solves that by enabling **intelligent search + AI-based answers** using company data.

---

## 🏗️ Architecture

```
User Question
     ↓
Embedding (Query)
     ↓
Vector Database (Chroma)
     ↓
Retrieve Relevant Chunks
     ↓
LLM (Groq - LLaMA 3.1)
     ↓
Final Answer
```

---

## ⚙️ Tech Stack

* 🐍 Python
* 🧠 LangChain & LangGraph
* 🔎 ChromaDB (Vector Database)
* 🤖 Groq LLM (LLaMA 3.1)
* 📄 python-docx (Document processing)
* 🖥️ Streamlit (Frontend UI)
* 🔢 Sentence Transformers (Embeddings)

---

## 📂 Project Structure

```
Agentic_RAG/
│
├── src/
│   ├── chunk.py
│   ├── vector_store.py
│   ├── rag_chat.py
│   └── file_processor.py
│
├── default_policies/   # Input documents
├── chroma_db/          # Vector database (ignored)
│
├── app.py              # Streamlit UI
├── requirements.txt
├── .env                # API keys (ignored)
├── .gitignore
└── README.md
```

---

## 🔄 Workflow

1. 📥 Load company policy documents (.docx)
2. ✂️ Split text into chunks
3. 🔢 Convert chunks into embeddings
4. 🗄️ Store embeddings in ChromaDB
5. ❓ User asks a question
6. 🔍 Retrieve relevant chunks
7. 🤖 Pass context to LLM (Groq)
8. 💬 Generate accurate answer

---

## 💡 Features

* ✅ Context-aware responses
* ✅ Real-time document search
* ✅ Fast inference using Groq
* ✅ Local vector database (Chroma)
* ✅ Interactive chat UI
* ✅ Supports multiple documents

---

## ⚠️ Challenges Faced

* Handling LangChain version changes
* Fixing import issues (new modules)
* Managing Groq model deprecations
* Securing API keys using `.env`
* Handling Windows environment setup

---

## 🔐 Security

* API keys stored in `.env`
* `.env` excluded using `.gitignore`
* Sensitive data not pushed to GitHub

---

## 🚀 How to Run

### 1. Clone Repository

```
git clone https://github.com/yourusername/company-policy-assistant.git
cd company-policy-assistant
```

---

### 2. Create Virtual Environment

```
py -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```
py -m pip install -r requirements.txt
```

---

### 4. Add API Key

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Create Vector Database

```
py -m src.vector_store
```

---

### 6. Run Application

```
py -m streamlit run app.py
```

---

## 🧪 Example Queries

* What is leave policy?
* What are company rules?
* What is HR policy?

---

## 🔮 Future Improvements

* Add file upload feature
* Implement chat memory
* Use FAISS / Pinecone for scalability
* Add authentication system
* Deploy on cloud

---

## 🎯 Key Learnings

* End-to-end RAG pipeline implementation
* Vector similarity search
* LLM integration with real data
* Handling production-level issues

---

## 👨‍💻 Author

**Rushikesh**
Aspiring AI & Data Scientist

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
