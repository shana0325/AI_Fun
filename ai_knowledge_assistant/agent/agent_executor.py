"""Agent execution orchestration."""

from __future__ import annotations

from ai_knowledge_assistant.agent.tools import search_knowledge
from ai_knowledge_assistant.llm.llm_client import SimpleLLMClient


class AgentExecutor:
    """Minimal agent pipeline: retrieve, then answer."""

    def __init__(self, documents: list[str], llm_client: SimpleLLMClient | None = None) -> None:
        self.documents = documents
        self.llm_client = llm_client or SimpleLLMClient()

    def run(self, query: str, top_k: int = 3) -> str:
        """Run retrieval + answer generation."""
        retrieved = search_knowledge(query=query, documents=self.documents, k=top_k)
        contexts = [item.text for item in retrieved]
        return self.llm_client.generate_answer(query=query, contexts=contexts)
