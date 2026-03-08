"""Retriever utilities for the RAG flow."""

from __future__ import annotations

from dataclasses import dataclass

from ai_knowledge_assistant.rag.embedding import embed_text


@dataclass(frozen=True)
class RetrievedChunk:
    """A chunk with relevance score."""

    text: str
    score: float


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Compute cosine similarity for normalized vectors."""
    if len(vec_a) != len(vec_b):
        raise ValueError("vectors must have the same dimensions")
    return sum(a * b for a, b in zip(vec_a, vec_b))


def retrieve_top_k(query: str, chunks: list[str], k: int = 3) -> list[RetrievedChunk]:
    """Return top-k relevant chunks for the query."""
    if k <= 0:
        raise ValueError("k must be positive")

    query_vec = embed_text(query)
    scored = [
        RetrievedChunk(text=chunk, score=cosine_similarity(query_vec, embed_text(chunk)))
        for chunk in chunks
    ]
    scored.sort(key=lambda item: item.score, reverse=True)
    return scored[:k]
