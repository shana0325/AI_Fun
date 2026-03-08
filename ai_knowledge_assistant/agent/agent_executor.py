"""Agent execution orchestration."""

from __future__ import annotations

from ai_knowledge_assistant.agent.tools import search_knowledge
from ai_knowledge_assistant.llm.llm_client import SimpleLLMClient
from ai_knowledge_assistant.rag.retriever import SimpleRetriever


class AgentExecutor:
    def __init__(self, retriever: SimpleRetriever, llm_client: SimpleLLMClient | None = None) -> None:
        self.retriever = retriever
        self.llm_client = llm_client or SimpleLLMClient()

    def run(self, question: str, top_k: int = 3) -> str:
        contexts = search_knowledge(query=question, retriever=self.retriever, top_k=top_k)
        return self.llm_client.generate_answer(question=question, contexts=contexts)