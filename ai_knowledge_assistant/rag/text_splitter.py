"""Text splitter utilities for RAG."""

from __future__ import annotations


def split_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """Split text into overlapped character chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    normalized = " ".join(text.split())
    if not normalized:
        return []

    chunks: list[str] = []
    step = chunk_size - overlap
    start = 0
    while start < len(normalized):
        end = min(start + chunk_size, len(normalized))
        chunks.append(normalized[start:end])
        if end >= len(normalized):
            break
        start += step
    return chunks


def split_documents(documents: list[str], chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """Split multiple documents and flatten chunks into one list."""
    chunks: list[str] = []
    for doc in documents:
        chunks.extend(split_text(doc, chunk_size=chunk_size, overlap=overlap))
    return chunks