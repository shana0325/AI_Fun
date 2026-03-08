"""LLM client abstraction."""

from __future__ import annotations

from ai_knowledge_assistant.rag.retriever import RetrievalResult

import os
from openai import OpenAI
from dotenv import load_dotenv


# 历史本地 Stub 实现保留在注释中，便于离线模式回退。
# class SimpleLLMClient:
#     """Local deterministic LLM stub that synthesizes an answer from context."""
#
#     def generate_answer(self, question: str, contexts: list[RetrievalResult]) -> str:
#         if not contexts:
#             return f"Question: {question}\n\nNo relevant knowledge was retrieved."
#
#         lines = [f"Question: {question}", "", "Based on retrieved knowledge:"]
#         for idx, ctx in enumerate(contexts, start=1):
#             lines.append(f"{idx}. (score={ctx.score:.3f}) {ctx.text}")
#         lines.append("")
#         lines.append("Conclusion: these are the most relevant chunks for this question.")
#         return "\n".join(lines)


class LLMClient:
    # 初始化：加载 .env，读取 DeepSeek Key，构造 OpenAI 兼容客户端。
    def __init__(self):
        # 加载环境变量
        load_dotenv()

        api_key = os.getenv("DEEPSEEK_API_KEY")

        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in .env")

        # 初始化 DeepSeek 客户端
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )

        self.model = "deepseek-chat"

    # 发送提示词到大模型并返回最终文本。
    def ask(self, prompt: str) -> str:
        """
        向 LLM 发送问题并返回回答
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content