"""Document loading utilities for RAG."""

from __future__ import annotations

from pathlib import Path


def load_text_file(file_path: str) -> str:
    """Load UTF-8 text from a local file path."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")
    if not path.is_file():
        raise ValueError(f"path is not a file: {file_path}")
    return path.read_text(encoding="utf-8")


def load_documents(paths: list[str]) -> list[str]:
    """Load multiple text documents and return raw text list."""
    return [load_text_file(path) for path in paths]