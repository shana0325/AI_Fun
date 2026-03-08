"""Agent tool definitions."""

from __future__ import annotations

from ai_knowledge_assistant.rag.retriever import RetrievalResult, SimpleRetriever


def search_knowledge(query: str, retriever: SimpleRetriever, top_k: int = 3) -> list[RetrievalResult]:
    """Tool: retrieve top-k relevant chunks."""
    return retriever.search(query=query, top_k=top_k)