"""Basic tests for the MVP RAG flow."""

from ai_knowledge_assistant.agent.agent_executor import AgentExecutor
from ai_knowledge_assistant.rag.chunking import chunk_text
from ai_knowledge_assistant.rag.retriever import retrieve_top_k


def test_chunk_text_splits_content() -> None:
    chunks = chunk_text("abcdefghijklmnopqrstuvwxyz", chunk_size=10, overlap=2)
    assert len(chunks) >= 3


def test_retrieve_top_k_returns_ranked_results() -> None:
    chunks = ["python is great", "cats and dogs", "python typing hints"]
    result = retrieve_top_k("python", chunks, k=2)
    assert len(result) == 2
    assert result[0].score >= result[1].score


def test_agent_executor_produces_answer() -> None:
    docs = ["RAG includes chunking and retrieval", "Streamlit helps build demos"]
    agent = AgentExecutor(documents=docs)
    answer = agent.run("What is RAG?", top_k=2)
    assert "问题" in answer
