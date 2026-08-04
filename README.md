# 🚀 Enterprise AI Customer Support Platform

An enterprise-grade AI-powered customer support platform built using **FastAPI**, **LangChain**, **ChromaDB**, **PostgreSQL**, and **Groq LLM**. The platform enables authenticated users to upload company documents, build a personalized knowledge base, and ask questions using Retrieval-Augmented Generation (RAG).

---

# ✨ Features

- 🔐 JWT Authentication (Register/Login)
- 👤 Multi-user Architecture
- 📄 PDF Upload
- 📚 Automatic Document Loading & Chunking
- 🧠 HuggingFace Embeddings
- 🗄️ Chroma Vector Database
- 🤖 AI Question Answering using Groq LLM
- 💬 Chat History Storage
- 👍 Feedback System
- 📝 Application Logging
- ⚠️ Global Exception Handling
- 🐘 PostgreSQL Database

---

# 🏗️ System Architecture

```
                 User
                   │
                   ▼
        FastAPI REST APIs
                   │
     ┌─────────────┼──────────────┐
     ▼             ▼              ▼
 PostgreSQL    ChromaDB       Groq LLM
     │             ▲
     │             │
     └──── RAG Pipeline ────────┘
                   ▲
                   │
         Uploaded PDF Documents
```

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## Authentication

- JWT
- Passlib (bcrypt)

## AI / RAG

- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM
- PyPDF

## Database

- PostgreSQL

## Logging

- Python Logging Module

---

# 📂 Project Structure

```
app/
│
├── api/
├── auth/
├── core/
├── database/
├── exceptions/
├── llm/
├── rag/
├── schemas/
├── services/
├── utils/
├── main.py
│
storage/
│
logs/
│
README.md
requirements.txt
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/abhisheksingh667/Enterprise-AI-Customer-Support-Platform.git

cd Enterprise-AI-Customer-Support-Platform
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```
DATABASE_URL=your_postgres_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

GROQ_API_KEY=your_groq_api_key
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🔄 Workflow

1. Register
2. Login
3. Upload PDF
4. Load Documents
5. Create Vector Database
6. Ask Questions
7. Save Chat History
8. Submit Feedback

---

# 📚 API Endpoints

## Authentication

```
POST /api/v1/auth/register

POST /api/v1/auth/login
```

## Upload

```
POST /api/v1/upload/
```

## Load Documents

```
POST /api/v1/load/
```

## Chat

```
POST /api/v1/chat/
```

## History

```
GET /api/v1/history/
```

## Feedback

```
POST /api/v1/feedback/
```

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing using bcrypt
- User Isolation
- Separate ChromaDB per User
- Separate Storage per User

---

# 📈 Future Enhancements

- Docker Support
- CI/CD Pipeline
- Redis Cache
- Role-Based Access Control (RBAC)
- Conversation Memory
- Streaming Responses
- Cloud Deployment

---

# 👨‍💻 Author

**Abhishek Singh**

GitHub:
https://github.com/abhisheksingh667

LinkedIn:
www.linkedin.com/in/abhishek-singh-8bb62221b

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.
