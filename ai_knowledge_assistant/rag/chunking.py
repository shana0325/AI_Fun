"""Chunking utilities for RAG."""

from __future__ import annotations


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """Split text into overlapped chunks by character length."""
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
    start = 0
    step = chunk_size - overlap
    length = len(normalized)

    while start < length:
        end = min(start + chunk_size, length)
        chunks.append(normalized[start:end].strip())
        if end >= length:
            break
        start += step

    return chunks