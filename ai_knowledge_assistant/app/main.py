"""Application entrypoint for CLI demo."""

from __future__ import annotations

import argparse

from ai_knowledge_assistant.agent.agent_executor import AgentExecutor

SAMPLE_DOCUMENTS = [
    "RAG 的核心流程包括：文档切分、向量化、相似度检索、结合上下文生成答案。",
    "搭建最小 AI 助手时，先保证可运行闭环，再逐步替换为真实模型和向量数据库。",
    "Streamlit 可以快速搭建对话界面，适合原型验证。",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI Knowledge Assistant demo")
    parser.add_argument("query", help="Question to ask the assistant")
    parser.add_argument("--top-k", type=int, default=3, help="Number of retrieved chunks")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = AgentExecutor(documents=SAMPLE_DOCUMENTS)
    print(agent.run(query=args.query, top_k=args.top_k))


if __name__ == "__main__":
    main()
