# 🧠 Memory-Augmented AI Chatbot  
**Local • Free • Production-Style AI System**

A full-stack, memory-augmented AI chatbot built with a **local LLM (Ollama)**, **FastAPI backend**, and a **modern React + Vite + Tailwind frontend**.  
Designed and structured like a real AI SaaS product — not a demo.

> ✅ No paid APIs  
> ✅ Runs fully on your machine  
> ✅ Resume & portfolio ready  
> ✅ Industry-grade architecture  

---

## ✨ Key Features

- 🧠 **Persistent Memory**
  - Short-term conversational context
  - Long-term vector memory using FAISS
- 🤖 **Local LLM Inference**
  - Powered by Ollama (no OpenAI, no cost)
- ⚡ **FastAPI Backend**
  - Clean API design
  - Modular, scalable structure
- 🎨 **Professional Frontend**
  - React + Vite + TypeScript
  - Tailwind CSS (Dark SaaS UI with gradient accents)
- 🔄 **Model-Agnostic**
  - Easily switch between models like `phi3`, `mistral`
- 🛠️ **Real Engineering Practices**
  - Environment isolation
  - Version-pinned dependencies
  - Production-style startup flow

---

## 🏗️ Tech Stack

### Backend
- Python 3.10
- FastAPI
- FAISS (vector search)
- Sentence Transformers
- Ollama (local LLM runtime)

### Frontend
- React + Vite
- TypeScript
- Tailwind CSS (v3)
- Framer Motion (animations)

### LLM Runtime
- Ollama  
  - Recommended dev model: **phi3**
  - Optional quality model: **mistral**

---

## 📁 Project Structure

```
Memory-Augmented-AI-Chatbot/
│
├── chatbot/                  # Backend (FastAPI)
│   ├── app/
│   │   ├── api/              # API routes
│   │   ├── core/             # LLM & config
│   │   ├── memory/           # Short & long-term memory
│   │   └── main.py           # FastAPI entry
│   │
│   └── data/
│       └── faiss_index/      # Vector memory storage
│
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.tsx
│   └── index.css
│
├── venv310/                  # Python virtual environment
└── README.md
```

---

## 🚀 Getting Started

Follow these steps **in order**.

---

## 1️⃣ Install Ollama

Download and install Ollama from:

👉 https://ollama.com

Verify installation:

```bash
ollama --version
```

---

## 2️⃣ Start Ollama Server

Open **Terminal 1** and keep it running:

```bash
ollama serve
```

---

## 3️⃣ Pull an LLM Model

Recommended for development (fast & lightweight):

```bash
ollama pull phi3
```

Optional higher-quality model:

```bash
ollama pull mistral
```

Warm the model once:

```bash
ollama run phi3
Hello
```

Exit with `Ctrl + D`.

---

## 4️⃣ Backend Setup (FastAPI)

### Create & activate Python environment

```bash
python3.10 -m venv venv310
source venv310/bin/activate
```

### Install backend dependencies

```bash
pip install --upgrade pip
pip install fastapi uvicorn requests sentence-transformers faiss-cpu==1.7.4
```

---

## 5️⃣ Start Backend Server

Open **Terminal 2**:

```bash
cd chatbot
source ../venv310/bin/activate
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Verify backend:

```bash
curl http://127.0.0.1:8000/
```

Expected output:

```json
{"status":"running"}
```

---

## 6️⃣ Frontend Setup (React + Vite)

### Install Node.js
Use **Node 20+** (recommended via `nvm`):

```bash
nvm install 20
nvm use 20
```

---

### Install frontend dependencies

Open **Terminal 3**:

```bash
cd frontend
npm install
```

---

## 7️⃣ Start Frontend

```bash
npm run dev
```

Open in browser:

```
http://localhost:5173
```

🎉 The chatbot UI is now live.

---

## 🧪 Quick Test

In the chat UI, try:

```
Remember that I prefer Python for ML.
```

Then:

```
What language do I prefer?
```

If it answers **Python**, memory is working correctly.

---

## 🔁 Switching Models

Edit:

```
chatbot/app/core/config.py
```

Change:

```python
MODEL_NAME = "phi3"
```

To:

```python
MODEL_NAME = "mistral"
```

Restart backend to apply.

---

## 🧠 Why This Project Is Different

- No shortcuts (no Streamlit demo UI)
- Real frontend stack
- Real memory system
- Real infra debugging experience
- Mirrors how **actual AI products** are built

This is **not a tutorial toy** — it’s a **mini AI platform**.

---

## 🛣️ Future Improvements

- 🔄 Streaming token responses
- 👤 Multi-user memory (sessions)
- 📊 Memory inspector panel
- 🔐 Auth & user profiles
- 🐳 Dockerized deployment

---

## 🙌 Author

Built with persistence, debugging, and a real-world engineering mindset.

If you’re a recruiter or reviewer:
> This project demonstrates **backend + ML + frontend + infra skills** in one system.
