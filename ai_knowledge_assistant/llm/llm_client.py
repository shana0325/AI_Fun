"""LLM client abstraction used by the agent."""

from __future__ import annotations


class SimpleLLMClient:
    """A tiny local stub that formats a final answer.

    This is intentionally deterministic and does not call external APIs,
    making the starter project runnable out of the box.
    """

    def generate_answer(self, query: str, contexts: list[str]) -> str:
        """Generate a simple answer from retrieved contexts."""
        if not contexts:
            return f"未找到相关知识。你的问题是：{query}"

        bullets = "\n".join(f"- {text}" for text in contexts[:3])
        return (
            f"问题：{query}\n"
            "根据检索到的知识，我建议你先关注以下内容：\n"
            f"{bullets}"
        )
