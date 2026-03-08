# AI Knowledge Assistant

An AI-powered knowledge assistant built with **RAG (Retrieval-Augmented Generation)** and **LLM APIs**.
The system can ingest documents, retrieve relevant context using vector search, and generate grounded answers with a large language model.

This project demonstrates how to build a practical **LLM application system**, including document processing, semantic retrieval, and agent-based tool execution.

---

## Features

* Document question answering using RAG
* Multi-document knowledge retrieval
* Context-aware answer generation
* Modular architecture for LLM applications
* Extensible agent tools for advanced tasks

Current MVP also includes:

* Text chunking + hash embedding + cosine Top-K retrieval
* `search_knowledge` tool with `AgentExecutor` orchestration
* Streamlit demo page and CLI entrypoint
* Local `SimpleLLMClient` stub for offline runnable flow

---

## Architecture

The system follows a standard RAG pipeline:

User Query
-> Retriever (Vector Search)
-> Context Construction
-> LLM Generation
-> Final Answer

Future extensions will include richer tool-calling agents and expanded web interfaces.

---

## Tech Stack

* Python
* DeepSeek API (LLM)
* LangChain
* FAISS (Vector Database)
* Streamlit (Frontend)
* FastAPI (Backend)

---

## Project Structure

```text
ai_knowledge_assistant
|-- agent
|   |-- tools.py
|   `-- agent_executor.py
|-- rag
|   |-- document_loader.py
|   |-- text_splitter.py
|   `-- vector_store.py
|-- llm
|   `-- llm_client.py
|-- frontend
|   `-- streamlit_app.py
|-- app
|   `-- main.py
|-- data
|   `-- knowledge.txt
|-- tests
`-- requirements.txt
```

---

## Installation

Create a conda environment:

```bash
conda create -n ai-rag python=3.10
conda activate ai-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```bash
DEEPSEEK_API_KEY=your_api_key
```

---

## Usage

Run the main application (CLI):

```bash
python -m ai_knowledge_assistant.app.main --question "What is the core RAG flow?" --top-k 3
```

Run Streamlit UI:

```bash
streamlit run ai_knowledge_assistant/frontend/streamlit_app.py
```

---

## Roadmap

* [x] Basic RAG pipeline
* [x] Vector database-style retrieval flow (in-memory MVP)
* [x] Agent tool execution
* [x] Web interface (Streamlit MVP)
* [ ] Multi-document comparison
* [ ] DeepSeek API integration
* [ ] FastAPI backend service