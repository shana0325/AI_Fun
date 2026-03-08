"""In-memory vector store for RAG."""

from __future__ import annotations

from dataclasses import dataclass

from ai_knowledge_assistant.rag.embedding import cosine_similarity, hash_embedding


@dataclass(frozen=True)
class VectorSearchResult:
    text: str
    score: float


class InMemoryVectorStore:
    """Simple vector store using hash embedding and cosine similarity."""

    def __init__(self, dims: int = 128) -> None:
        if dims <= 0:
            raise ValueError("dims must be > 0")
        self._dims = dims
        self._texts: list[str] = []
        self._vectors: list[list[float]] = []

    def add_texts(self, texts: list[str]) -> None:
        for text in texts:
            self._texts.append(text)
            self._vectors.append(hash_embedding(text, dims=self._dims))

    def similarity_search(self, query: str, top_k: int = 3) -> list[VectorSearchResult]:
        if top_k <= 0:
            raise ValueError("top_k must be > 0")
        if not self._texts:
            return []

        query_vec = hash_embedding(query, dims=self._dims)
        scored = [
            VectorSearchResult(text=text, score=cosine_similarity(query_vec, vec))
            for text, vec in zip(self._texts, self._vectors)
        ]
        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:top_k]