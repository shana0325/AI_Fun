# """In-memory vector store for RAG."""
#
# from __future__ import annotations
#
# from dataclasses import dataclass
#
# from ai_knowledge_assistant.rag.embedding import cosine_similarity, hash_embedding
#
#
# @dataclass(frozen=True)
# class VectorSearchResult:
#     text: str
#     score: float
#
#
# class InMemoryVectorStore:
#     """Simple vector store using hash embedding and cosine similarity."""
#
#     def __init__(self, dims: int = 128) -> None:
#         if dims <= 0:
#             raise ValueError("dims must be > 0")
#         self._dims = dims
#         self._texts: list[str] = []
#         self._vectors: list[list[float]] = []
#
#     def add_texts(self, texts: list[str]) -> None:
#         for text in texts:
#             self._texts.append(text)
#             self._vectors.append(hash_embedding(text, dims=self._dims))
#
#     def similarity_search(self, query: str, top_k: int = 3) -> list[VectorSearchResult]:
#         if top_k <= 0:
#             raise ValueError("top_k must be > 0")
#         if not self._texts:
#             return []
#
#         query_vec = hash_embedding(query, dims=self._dims)
#         scored = [
#             VectorSearchResult(text=text, score=cosine_similarity(query_vec, vec))
#             for text, vec in zip(self._texts, self._vectors)
#         ]
#         scored.sort(key=lambda item: item.score, reverse=True)
#         return scored[:top_k]

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorStore:
    # 加载 embedding 模型，并初始化向量索引容器。
    def __init__(self, model_name="BAAI/bge-base-en-v1.5"):

        print("Loading embedding model...")

        self.model = SentenceTransformer(model_name)

        self.index = None
        self.chunks = []

    # 为 chunks 生成向量，并构建 FAISS 索引。
    def build_index(self, chunks: list[str]):
        """
        构建向量索引
        """

        self.chunks = chunks

        print("Generating embeddings...")

        embeddings = self.model.encode(chunks)

        embeddings = np.array(embeddings).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        print(f"Index built with {len(chunks)} chunks")

    # 对查询做向量检索，返回最相关的 top_k 原文片段。
    def search(self, query: str, top_k: int = 3):
        """
        语义检索
        """

        query_embedding = self.model.encode([query])

        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results