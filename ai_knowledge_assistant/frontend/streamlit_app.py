"""Streamlit frontend entrypoint."""

from __future__ import annotations

import streamlit as st

from ai_knowledge_assistant.agent.agent_executor import AgentExecutor

SAMPLE_DOCUMENTS = [
    "RAG 的核心流程包括：文档切分、向量化、相似度检索、结合上下文生成答案。",
    "搭建最小 AI 助手时，先保证可运行闭环，再逐步替换为真实模型和向量数据库。",
    "Streamlit 可以快速搭建对话界面，适合原型验证。",
]


def run_app() -> None:
    """Render the Streamlit demo page."""
    st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🤖")
    st.title("AI Knowledge Assistant (MVP)")
    st.caption("最小可运行版本：RAG + Agent + LLM Stub")

    question = st.text_input("请输入你的问题", value="RAG 的核心流程是什么？")
    top_k = st.slider("检索段落数量", min_value=1, max_value=5, value=3)

    if st.button("提问"):
        agent = AgentExecutor(documents=SAMPLE_DOCUMENTS)
        answer = agent.run(query=question, top_k=top_k)
        st.markdown("### 回答")
        st.write(answer)


if __name__ == "__main__":
    run_app()
