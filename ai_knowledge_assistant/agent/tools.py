"""Agent tools for knowledge search."""

from __future__ import annotations

from ai_knowledge_assistant.rag.chunking import chunk_text
from ai_knowledge_assistant.rag.retriever import RetrievedChunk, retrieve_top_k


def search_knowledge(query: str, documents: list[str], k: int = 3) -> list[RetrievedChunk]:
    """Search documents and return top-k chunks."""
    all_chunks: list[str] = []
    for doc in documents:
        all_chunks.extend(chunk_text(doc))
    return retrieve_top_k(query=query, chunks=all_chunks, k=k)
