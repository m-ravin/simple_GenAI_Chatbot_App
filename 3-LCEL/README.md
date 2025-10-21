# 3-LCEL

Lightweight Chain Execution Layer (LCEL) examples and small demo apps demonstrating how to compose, run, and serve simple LangChain-like chains and local execution flows. This folder contains a notebook for experimentation, a minimal app, and a small serve script to run the example locally.

---

## Contents

- 3.1-SimpleLCEL.ipynb — Interactive Jupyter notebook demonstrating LCEL concepts, example chains, and step-by-step experiments.
- app.py — Example streamlit application that uses models from Grow and LCEL chain.
- serve.py — Minimal server wrapper to run the example app as a long-running service (Flask/FastAPI/other lightweight server).
- README.md — (this file) documentation and usage notes.

---

## Goals

- Show how to compose simple chains of steps.
- Provide a reproducible example for local experimentation without heavy infra.
- Demonstrate serving patterns for lightweight LLM-powered chains.

---

## Prerequisites

- Python 3.9+
- Basic Python packages listed in the repository `requirements.txt`
- Optional: OpenAI API key or a local LLM endpoint (Ollama) depending on which connectors you want to test.

Set environment variables in the project root `.env` as needed (examples):

```
OPENAI_API_KEY="your-openai-key"
OLLAMA_API_URL="http://localhost:11434"
```

---

## Installation

1. Create and activate a virtual environment (Windows):

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Install any additional dependencies if prompted by the notebook.

---

## Usage

Open the notebook
- Launch Jupyter or VS Code and open `3.1-SimpleLCEL.ipynb`.
- Run cells to explore the chain creation, prompt templates, and simple examples.

Run the example app
- Run locally to test the chain via the included app interface:

```powershell
python 3-LCEL\app.py
```

- If `app.py` starts a web server, note the printed URL and open it in the browser. If it is CLI-based, follow the prompts.

Run the serve script
- For long-running usage or testing as a service:

```powershell
python 3-LCEL\serve.py
```

- The script will start a lightweight HTTP endpoint (see output) that accepts requests and returns chain outputs.

---

## Implementation Notes

- The examples are intentionally minimal to focus on structure and local experimentation.
- Chains are composed of modular steps so you can replace prompt templates, models (OpenAI / local LLM), and retrievers with minimal changes.
- Persistence, advanced vector stores, and production-grade error handling are out of scope for this demo; the sample code highlights patterns to extend.

---

## Extending

- Swap the LLM connector: replace a dummy/local LLM with OpenAI or Ollama in the chain initializer.
- Add a vector store and a retriever step for retrieval-augmented generation.
- Add input validation, rate limiting, and logging in `serve.py` for production readiness.

---

## Troubleshooting

- If LLM requests fail: verify API keys and network access, and check model availability for local endpoints.
- Notebook errors: ensure required packages are installed and the virtual environment is active.


