"""Application entrypoint."""

from __future__ import annotations

import argparse
from pathlib import Path

from ai_knowledge_assistant.agent.agent_executor import AgentExecutor
from ai_knowledge_assistant.rag.chunking import chunk_text
from ai_knowledge_assistant.rag.retriever import SimpleRetriever

DEFAULT_KNOWLEDGE_FILE = Path(__file__).resolve().parents[2] / "data" / "knowledge.txt"


def build_executor(knowledge_text: str, chunk_size: int = 180, overlap: int = 30, dims: int = 128) -> AgentExecutor:
    chunks = chunk_text(knowledge_text, chunk_size=chunk_size, overlap=overlap)
    retriever = SimpleRetriever(chunks=chunks, dims=dims)
    return AgentExecutor(retriever=retriever)


def load_default_knowledge_text() -> str:
    if not DEFAULT_KNOWLEDGE_FILE.exists():
        raise FileNotFoundError(f"default knowledge file not found: {DEFAULT_KNOWLEDGE_FILE}")
    return DEFAULT_KNOWLEDGE_FILE.read_text(encoding="utf-8")


def load_knowledge_text(file_path: str | None) -> str:
    if not file_path:
        return load_default_knowledge_text()
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"knowledge file not found: {file_path}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Knowledge Assistant MVP")
    parser.add_argument("--question", required=True, help="User question")
    parser.add_argument("--knowledge-file", help="Path to local text knowledge file")
    parser.add_argument("--top-k", type=int, default=3, help="Top-K retrieval results")
    parser.add_argument("--chunk-size", type=int, default=180, help="Chunk size")
    parser.add_argument("--overlap", type=int, default=30, help="Chunk overlap")
    args = parser.parse_args()

    knowledge_text = load_knowledge_text(args.knowledge_file)
    executor = build_executor(
        knowledge_text=knowledge_text,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
    )
    answer = executor.run(question=args.question, top_k=args.top_k)
    print(answer)


if __name__ == "__main__":
    main()