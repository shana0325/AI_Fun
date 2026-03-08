"""Chunking utilities for the RAG flow."""

from __future__ import annotations


def chunk_text(text: str, chunk_size: int = 160, overlap: int = 20) -> list[str]:
    """Split text into overlapping chunks.

    Args:
        text: Raw text to split.
        chunk_size: Max characters in each chunk.
        overlap: Characters to overlap between consecutive chunks.

    Returns:
        A list of non-empty chunks.
    """
    normalized = " ".join(text.split())
    if not normalized:
        return []
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and < chunk_size")

    step = chunk_size - overlap
    chunks: list[str] = []

    for start in range(0, len(normalized), step):
        chunk = normalized[start : start + chunk_size].strip()
        if chunk:
            chunks.append(chunk)

    return chunks
