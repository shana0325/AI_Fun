# AI Knowledge Assistant -- System Architecture Design

## 1. Project Goal

The goal of this project is to build a **modular AI Knowledge Assistant
system** based on LLM APIs and RAG (Retrieval-Augmented Generation).\
The system is designed with clear engineering architecture to
demonstrate practical **LLM application engineering capabilities**.

Core capabilities:

1.  Document-based knowledge retrieval (RAG)
2.  Multi-document question answering
3.  Unified LLM API abstraction layer
4.  Extensible agent tools for advanced tasks

The emphasis of this project is **system architecture and modular
design**, rather than a simple demo script.

------------------------------------------------------------------------

# 2. Overall System Architecture

The system is divided into **five layers**:

User Layer\
↓\
API Layer\
↓\
Application Layer\
↓\
RAG Layer\
↓\
LLM Layer

Each layer has a clear responsibility and can be extended independently.

------------------------------------------------------------------------

# 3. Layer Responsibilities

## 3.1 User Layer

This layer represents how users interact with the system.

Possible interfaces:

-   Web UI
-   CLI
-   API

In this project, the primary interface will be:

-   Streamlit Web UI

Responsibilities:

-   Accept user queries
-   Display answers
-   Show document references

------------------------------------------------------------------------

## 3.2 API Layer

The API layer provides service endpoints for external interaction.

Typical responsibilities:

-   Request routing
-   Input validation
-   Calling application services

Example endpoints:

-   ask_question
-   upload_document

Recommended framework:

-   FastAPI

------------------------------------------------------------------------

## 3.3 Application Layer

This layer contains the **core business logic**.

Responsibilities:

-   Coordinate system workflow
-   Decide whether to use RAG or tools
-   Manage request processing

Example service:

QuestionAnswerService

Workflow example:

User Question\
↓\
Call RAG Engine\
↓\
Construct Prompt\
↓\
Call LLM\
↓\
Return Answer

------------------------------------------------------------------------

## 3.4 RAG Layer

This layer handles **knowledge retrieval and document processing**.

Main responsibilities:

-   Document ingestion
-   Text chunking
-   Embedding generation
-   Vector search
-   Context construction

Modules inside the RAG layer:

-   document_loader
-   text_splitter
-   vector_store
-   retriever

Typical pipeline:

Document\
↓\
Loader\
↓\
Text Splitter\
↓\
Embedding\
↓\
Vector Store\
↓\
Retriever\
↓\
Context Builder\
↓\
LLM

------------------------------------------------------------------------

## 3.5 LLM Layer

This layer provides a **unified abstraction for LLM access**.

Responsibilities:

-   Encapsulate DeepSeek API calls
-   Manage prompt requests
-   Enable future model replacement

Example component:

LLMClient

Advantages of abstraction:

-   Easy model switching
-   Centralized prompt management
-   Cleaner application logic

------------------------------------------------------------------------

# 4. System Architecture Diagram

System workflow:

User\
↓\
Frontend (Streamlit)\
↓\
API Server\
↓\
Application Service\
↓\
RAG Engine\
↓\
Vector Store\
↓\
LLM Client\
↓\
Answer Returned to User

------------------------------------------------------------------------

# 5. Project Module Structure

The code structure reflects the layered architecture.

ai-knowledge-assistant

├── agent\
│ ├── tools.py\
│ └── agent_executor.py

├── rag\
│ ├── document_loader.py\
│ ├── text_splitter.py\
│ └── vector_store.py

├── llm\
│ └── llm_client.py

├── frontend\
│ └── app.py

├── data

├── test

├── requirements.txt

└── README.md

------------------------------------------------------------------------

# 6. Development Roadmap

Development will proceed **from bottom layer to top layer**.

Step 1 -- LLM Layer\
Implement LLMClient for DeepSeek API access.

Step 2 -- RAG Layer\
Implement document loading, chunking, embeddings, and vector search.

Step 3 -- Application Layer\
Implement QuestionAnswerService.

Step 4 -- API Layer\
Create FastAPI endpoints.

Step 5 -- Frontend Layer\
Build Streamlit user interface.

------------------------------------------------------------------------

# 7. Final System Capabilities

When the system is complete, users will be able to:

1.  Upload documents
2.  Ask questions about the documents
3.  Receive AI-generated answers
4.  See cited document sources

Example:

Q: What is RAG?\
A: ...\
Source: document chunk reference

------------------------------------------------------------------------

This document serves as the **architecture reference** for the AI
Knowledge Assistant project.
