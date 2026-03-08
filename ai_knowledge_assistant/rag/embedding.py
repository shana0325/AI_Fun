"""Embedding utilities for the RAG flow."""

from __future__ import annotations

import math
import re

TOKEN_PATTERN = re.compile(r"\b[a-zA-Z0-9_]+\b")


def tokenize(text: str) -> list[str]:
    """Lower-case alphanumeric tokenizer."""
    return TOKEN_PATTERN.findall(text.lower())


def embed_text(text: str, dimensions: int = 64) -> list[float]:
    """Create a deterministic hash-based embedding vector.

    This keeps the project dependency-light while still being runnable.
    """
    if dimensions <= 0:
        raise ValueError("dimensions must be positive")

    vector = [0.0] * dimensions
    tokens = tokenize(text)
    if not tokens:
        return vector

    for token in tokens:
        vector[hash(token) % dimensions] += 1.0

    norm = math.sqrt(sum(v * v for v in vector))
    if norm == 0:
        return vector
    return [v / norm for v in vector]
