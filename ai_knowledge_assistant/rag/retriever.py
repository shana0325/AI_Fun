"""Retriever utilities for RAG."""

from __future__ import annotations

from dataclasses import dataclass

from ai_knowledge_assistant.rag.embedding import cosine_similarity, hash_embedding


@dataclass(frozen=True)
class RetrievalResult:
    text: str
    score: float


class SimpleRetriever:
    def __init__(self, chunks: list[str], dims: int = 128) -> None:
        self._chunks = chunks
        self._dims = dims
        self._embeddings = [hash_embedding(chunk, dims=dims) for chunk in chunks]

    def search(self, query: str, top_k: int = 3) -> list[RetrievalResult]:
        if top_k <= 0:
            raise ValueError("top_k must be > 0")
        if not self._chunks:
            return []

        query_vec = hash_embedding(query, dims=self._dims)
        scored = [
            RetrievalResult(text=chunk, score=cosine_similarity(query_vec, emb))
            for chunk, emb in zip(self._chunks, self._embeddings)
        ]
        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:top_k]