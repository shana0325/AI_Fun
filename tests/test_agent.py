from ai_knowledge_assistant.app.main import build_executor


def test_agent_executor_returns_local_answer() -> None:
    knowledge = "RAG combines retrieval with generation for grounded answers."
    executor = build_executor(knowledge_text=knowledge, chunk_size=80, overlap=10)

    output = executor.run("What is RAG?", top_k=1)

    assert "What is RAG?" in output
    assert "RAG combines retrieval" in output