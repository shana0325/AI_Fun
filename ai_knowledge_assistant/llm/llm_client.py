"""LLM client abstraction."""

from __future__ import annotations

from ai_knowledge_assistant.rag.retriever import RetrievalResult


class SimpleLLMClient:
    """Local deterministic LLM stub that synthesizes an answer from context."""

    def generate_answer(self, question: str, contexts: list[RetrievalResult]) -> str:
        if not contexts:
            return f"Question: {question}\n\nNo relevant knowledge was retrieved."

        lines = [f"Question: {question}", "", "Based on retrieved knowledge:"]
        for idx, ctx in enumerate(contexts, start=1):
            lines.append(f"{idx}. (score={ctx.score:.3f}) {ctx.text}")
        lines.append("")
        lines.append("Conclusion: these are the most relevant chunks for this question.")
        return "\n".join(lines)