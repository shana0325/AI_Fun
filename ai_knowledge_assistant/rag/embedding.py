"""Embedding utilities for RAG."""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter

_TOKEN_RE = re.compile(r"\w+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in _TOKEN_RE.findall(text)]


def hash_embedding(text: str, dims: int = 128) -> list[float]:
    """Create a deterministic sparse-ish embedding using hashing trick."""
    if dims <= 0:
        raise ValueError("dims must be > 0")

    vec = [0.0] * dims
    counts = Counter(tokenize(text))

    for token, tf in counts.items():
        digest = hashlib.md5(token.encode("utf-8")).hexdigest()
        index = int(digest[:8], 16) % dims
        sign = 1.0 if int(digest[8:10], 16) % 2 == 0 else -1.0
        vec[index] += sign * float(tf)

    norm = math.sqrt(sum(v * v for v in vec))
    if norm == 0:
        return vec
    return [v / norm for v in vec]


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    if len(vec_a) != len(vec_b):
        raise ValueError("vector dimensions do not match")
    return float(sum(a * b for a, b in zip(vec_a, vec_b)))