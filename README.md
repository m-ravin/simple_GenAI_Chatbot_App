# simple_GenAI_Chatbot_App
Code repo for GenAI Chatbot app

A hands-on repository demonstrating how to build GenAI-powered chatbot applications using LangChain, OpenAI, and Ollama. The project includes both Jupyter notebooks for experimentation and a Streamlit app for interactive chatbot experiences.

---

## Project Structure

```
.env
.gitignore
README.md
requirements.txt
1-OpenAI/
    1-OpenAI/1.1-GettingStarted.ipynb
    1-OpenAI/1.2-simpleapp.ipynb
2-Ollama/
    2-Ollama/app.py
3-LCEL/
    3-LCEL/3.1-SimpleLCEL.ipynb
    3-LCEL/app.py
    3-LCEL/README.md
    3-LCEL/serve.py   
4-ChatbotwithConversationHistory/
    4-ChatbotwithConversationHistory/4.1-Chatbot.ipynb  
```

---

## Features

- **LangChain + OpenAI Notebooks**:  
  - 1-OpenAI/1.1-GettingStarted.ipynb:  
    Step-by-step guide to using LangChain with OpenAI, covering prompt templates, models, output parsers, and tracing.
  - 1-OpenAI/1.2-simpleapp.ipynb:  
    Example of a GenAI app that ingests web data, splits documents, embeds them, stores them in a vector database (FAISS), and performs similarity search.

- **Ollama + LangChain Streamlit App**:  
  - 2-Ollama/app.py:  
    Streamlit web app using LangChain with Ollama's Gemma model. Users can interact with the chatbot via a simple UI.

- **Groq+ LCEL + LangChain +LangServe App**:
  - small demo apps demonstrating how to compose, run, and serve simple LangChain-like chains and local execution flows.
  
-- **Chatbot with Conversation History Notebook**:  
  - Demonstrates how to build a chatbot that maintains conversation history using LangChain's RunnableWithMessageHistory, allowing for context-aware interactions.
---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/simple_GenAI_Chatbot_App.git
cd simple_GenAI_Chatbot_App
```

### 2. Install Dependencies

All required Python packages are listed in requirements.txt:

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory (already included in this repo).  
Set your API keys and project name:

```
OPENAI_API_KEY="your-openai-key"
LANGCHAIN_API_KEY="your-langchain-key"
LANGCHAIN_PROJECT="your-project-name"
```

---

## Usage

### 1. Jupyter Notebooks

- Open 1-OpenAI/1.1-GettingStarted.ipynb or 1-OpenAI/1.2-simpleapp.ipynb in Jupyter or VS Code.
- Follow the cells to experiment with LangChain, OpenAI, document loading, embeddings, and vector search.

### 2. Streamlit Chatbot App (Ollama)

- Make sure Ollama is installed and running locally with the Gemma model available.
- Run the app:

```sh
streamlit run 2-Ollama/app.py
```

- Open the provided local URL in your browser and interact with the chatbot.

---

## Key Technologies

- **LangChain**: Framework for developing applications powered by large language models.
- **OpenAI**: Access to GPT models for chat and embeddings.
- **Ollama**: Local LLM serving (Gemma model).
- **FAISS**: Vector database for similarity search.
- **Streamlit**: Rapid prototyping of web apps.
- **dotenv**: Secure management of environment variables.

---

## Example Workflows

### LangChain + OpenAI (Notebook)

- Load environment variables.
- Initialize LangChain and OpenAI API keys.
- Create prompt templates and chains.
- Load and chunk documents from the web.
- Embed documents and store in FAISS.
- Perform similarity search and retrieve relevant content.

### LangChain + Ollama (Streamlit App)

- Load environment variables.
- Set up a prompt template for the chatbot.
- Use Ollama's Gemma model via LangChain.
- Parse and display responses interactively in a web UI.

### LangChain + LCEL + Groq (FASTAPI App)

- Load environment variables.
- Initialize LangChain and OpenAI API keys.
- Create prompt templates and chains.
- Use Groq to run opensource LLM models.
- Use Ollama's llama-3.1-8b-instant via LangChain.
- Parse and display responses interactively in a web UI.

---

## References

- [LangChain Documentation](https://docs.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [Ollama Documentation](https://ollama.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/)

---

