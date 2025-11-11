# simple_GenAI_Chatbot_App

A comprehensive repository demonstrating how to build GenAI-powered chatbot applications using LangChain, OpenAI, Ollama, and Groq. This project includes Jupyter notebooks for experimentation, Streamlit apps, and FastAPI services for interactive chatbot experiences and RAG (Retrieval-Augmented Generation) systems.

---

## Project Structure

```
.
├── main.py                              # Main entry point
├── pyproject.toml                       # Project configuration (uv package manager)
├── .env                                 # Environment variables (create your own)
├── .gitignore                           # Git ignore rules
├── README.md                            # This file
│
├── 1-OpenAI/                            # OpenAI + LangChain Notebooks
│   ├── 1.1-GettingStarted.ipynb        # LangChain + OpenAI fundamentals
│   └── 1.2-simpleapp.ipynb             # Document ingestion & vector search
│
├── 2-Ollama/                            # Ollama + LangChain Streamlit App
│   └── app.py                           # Streamlit chatbot with Ollama
│
├── 3-LCEL/                              # LangChain Expression Language (LCEL)
│   ├── 3.1-SimpleLCEL.ipynb            # LCEL concepts and examples
│   ├── app.py                           # Streamlit app with LCEL chains
│   ├── serve.py                         # Lightweight HTTP server
│   └── README.md                        # Detailed documentation
│
├── 4-ChatbotwithConversationHistory/    # Conversation History Chatbot
│   └── 4.1-Chatbot.ipynb               # Chatbot with memory/context
│
├── 5-Conversation_QA_Chatbot/           # Q&A with Conversation Memory
│   └── 5.1-conversationqa.ipynb        # Q&A system with history
│
├── 6-Q&A_Chatbot/                       # Simple Q&A Chatbot
│   └── openai_app.py                    # Streamlit Q&A app with OpenAI
│
└── 7-RAG_Q&A_withPDF/                   # RAG System with PDF Support
    └── app.py                           # Advanced RAG chatbot with Groq
```

---

## Project Descriptions

### 1️⃣ **1-OpenAI** - LangChain + OpenAI Notebooks
Introduction to LangChain and OpenAI integration with two progressive notebooks:
- **1.1-GettingStarted.ipynb**: Learn LangChain fundamentals including prompt templates, chat models, output parsers, and LangSmith tracing.
- **1.2-simpleapp.ipynb**: Build a complete GenAI app that loads web content, chunks documents, creates embeddings, stores them in FAISS vector DB, and performs semantic similarity search.

**Technologies**: LangChain, OpenAI, FAISS, BeautifulSoup  
**Use Case**: Document-based semantic search and retrieval

---

### 2️⃣ **2-Ollama** - Streamlit Chatbot with Ollama
A simple yet powerful Streamlit web application that demonstrates real-time chatbot interaction using a local LLM.
- Uses Ollama's lightweight Gemma model (can be swapped with other models like Llama, Mistral, etc.)
- Interactive chat interface for users to ask questions and receive instant responses
- No API costs since it runs locally

**Technologies**: Streamlit, Ollama, LangChain  
**Use Case**: Local, cost-free chatbot for offline deployments

---

### 3️⃣ **3-LCEL** - LangChain Expression Language (LCEL)
Comprehensive guide to LangChain's composable LCEL chains with minimal examples:
- **3.1-SimpleLCEL.ipynb**: Step-by-step exploration of LCEL syntax, chaining patterns, and composition
- **app.py**: Streamlit application demonstrating LCEL chains in action with Groq models
- **serve.py**: Lightweight HTTP server wrapper for serving LCEL chains as a long-running service

**Technologies**: LangChain, LCEL, Groq, FastAPI  
**Use Case**: Building composable, reusable LLM chains for production use

---

### 4️⃣ **4-ChatbotwithConversationHistory** - Conversation Memory Chatbot
Demonstrates stateful chatbot design with memory management:
- Maintains conversation history across multiple turns
- Uses LangChain's `RunnableWithMessageHistory` for context-aware responses
- Enables the chatbot to reference previous messages and maintain coherent dialogues

**Technologies**: LangChain, Message History, RunnableWithMessageHistory  
**Use Case**: Building chatbots that understand context and maintain conversation flow

---

### 5️⃣ **5-Conversation_QA_Chatbot** - Q&A with Conversation Memory
An advanced question-answering system that combines semantic search with conversation history:
- Uses vector similarity for question-document matching
- Maintains chat history for context-aware answer generation
- Ideal for multi-turn Q&A sessions over knowledge bases

**Technologies**: LangChain, Vector Search, Chat History  
**Use Case**: Knowledge base Q&A with conversational context

---

### 6️⃣ **6-Q&A_Chatbot** - Simple Q&A with OpenAI
A streamlined Streamlit application for direct Q&A with OpenAI models:
- User-friendly sidebar controls for model selection, temperature, and token limits
- Direct OpenAI API integration for production-grade responses
- Configurable parameters to fine-tune model behavior

**Technologies**: Streamlit, OpenAI API (GPT-3.5-turbo, GPT-4)  
**Use Case**: Quick Q&A application with full OpenAI model capabilities

---

### 7️⃣ **7-RAG_Q&A_withPDF** - Advanced RAG System
State-of-the-art Retrieval-Augmented Generation chatbot with PDF support:
- Upload single or multiple PDF documents
- Automatic document chunking and semantic embedding
- Context-aware retrieval for accurate answers
- Maintains full chat history with document context
- Uses Groq's fast inference for real-time responses

**Technologies**: Streamlit, Groq, LangChain, ChromaDB, HuggingFace Embeddings, PyPDF  
**Use Case**: Document-based Q&A with conversational AI (e.g., customer support, document analysis)

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/m-ravin/simple_GenAI_Chatbot_App.git
cd simple_GenAI_Chatbot_App
```

### 2. Install Dependencies with `uv`

This project uses `uv` for fast, reliable Python dependency management. Install `uv` first:

```sh
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (using PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install project dependencies:

```sh
uv sync
```

Or with venv:
```sh
uv venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
uv pip install -r pyproject.toml
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with your API keys:

```sh
# OpenAI (for 1-OpenAI, 6-Q&A_Chatbot)
OPENAI_API_KEY="your-openai-api-key"

# LangChain/LangSmith (optional, for tracing)
LANGCHAIN_API_KEY="your-langchain-api-key"
LANGCHAIN_PROJECT="your-project-name"

# Groq (for 3-LCEL, 7-RAG_Q&A_withPDF)
GROQ_API_KEY="your-groq-api-key"

# HuggingFace (for embeddings in 7-RAG_Q&A_withPDF)
HF_TOKEN="your-huggingface-token"
```

### 4. Optional: Install Ollama

For running the Ollama chatbot (2-Ollama/app.py), install Ollama:

```sh
# Download from https://ollama.ai
# Then pull a model:
ollama pull gemma:2b
```

---

## Usage Guide

### 📓 Jupyter Notebooks
Open notebooks in VS Code or Jupyter:
```sh
jupyter notebook
```

### 🤖 Ollama Chatbot (Local, No API Costs)
```sh
ollama serve  # In a separate terminal
uv run streamlit run 2-Ollama/app.py
```

### 🎯 Simple Q&A with OpenAI
```sh
uv run streamlit run 6-Q&A_Chatbot/openai_app.py
```

### 📄 RAG Chatbot with PDFs
```sh
uv run streamlit run 7-RAG_Q&A_withPDF/app.py
```

### 🔗 LCEL App
```sh
uv run streamlit run 3-LCEL/app.py
```

### 🚀 LCEL HTTP Server
```sh
uv run python 3-LCEL/serve.py
```

---

## Key Technologies

| Technology | Purpose |
|---|---|
| **LangChain** | Framework for building LLM applications with composable chains |
| **OpenAI** | Access to GPT-3.5-turbo and GPT-4 models |
| **Groq** | Fast inference API for open-source LLMs |
| **Ollama** | Local LLM serving and inference |
| **FAISS** | Vector database for semantic similarity search |
| **ChromaDB** | Lightweight vector database for embeddings |
| **HuggingFace** | Pre-trained embeddings and models |
| **Streamlit** | Rapid web app prototyping and deployment |
| **PyPDF** | PDF document processing and parsing |
| **FastAPI** | Lightweight async web framework |
| **uvicorn** | ASGI server for FastAPI |
| **dotenv** | Environment variable management |

---

## API Keys Required

| Service | Purpose | Link |
|---|---|---|
| OpenAI | GPT models (required for projects 1, 6) | [platform.openai.com](https://platform.openai.com) |
| Groq | Fast LLM inference (required for projects 3, 7) | [console.groq.com](https://console.groq.com) |
| HuggingFace | Embeddings (required for project 7) | [huggingface.co](https://huggingface.co) |
| LangChain | Tracing & debugging (optional) | [smith.langchain.com](https://smith.langchain.com) |

---

## Learning Path

**Beginners**:
1. Start with **1-OpenAI/1.1-GettingStarted.ipynb** to learn LangChain basics
2. Try **2-Ollama/app.py** for a quick local chatbot
3. Explore **6-Q&A_Chatbot/openai_app.py** for a simple production-ready Q&A app

**Intermediate**:
1. Study **3-LCEL/3.1-SimpleLCEL.ipynb** to master chain composition
2. Build with **4-ChatbotwithConversationHistory** to add memory
3. Enhance with **5-Conversation_QA_Chatbot** for hybrid retrieval + conversation

**Advanced**:
1. Dive into **7-RAG_Q&A_withPDF/app.py** for production RAG systems
2. Understand **3-LCEL/serve.py** for API deployment patterns
3. Combine multiple concepts for your own applications

---

## Troubleshooting

| Issue | Solution |
|---|---|
| `ModuleNotFoundError` | Run `uv sync` to install all dependencies |
| OpenAI API errors | Check `OPENAI_API_KEY` in `.env` file |
| Groq API errors | Check `GROQ_API_KEY` in `.env` file |
| Ollama not connecting | Ensure `ollama serve` is running in another terminal |
| FAISS import error | Run `uv pip install faiss-cpu` |
| PDF parsing fails | Ensure PDF file is valid; try `uv pip install --upgrade pypdf` |

---

## References

- [LangChain Documentation](https://docs.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [Ollama Documentation](https://ollama.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Groq Documentation](https://console.groq.com/docs)
- [uv Documentation](https://docs.astral.sh/uv/)

---

## Contributing

Feel free to fork this repository, submit issues, and open pull requests. Contributions are welcome!

---

## License

This project is open source. See LICENSE for more details.

---

**Last Updated**: November 2025  
**Maintainer**: [m-ravin](https://github.com/m-ravin)

