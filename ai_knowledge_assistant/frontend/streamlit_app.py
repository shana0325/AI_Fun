# """Streamlit frontend entrypoint."""
#
# from __future__ import annotations
#
# import streamlit as st
#
# from ai_knowledge_assistant.app.main import build_executor, load_default_knowledge_text
#
#
# def run() -> None:
#     st.set_page_config(page_title="AI Knowledge Assistant", layout="centered")
#     st.title("AI Knowledge Assistant (MVP)")
#
#     knowledge_text = st.text_area("Knowledge text", value=load_default_knowledge_text(), height=180)
#     question = st.text_input("Your question", value="What is the core RAG flow?")
#     top_k = st.slider("Top-K", min_value=1, max_value=8, value=3)
#
#     if st.button("Generate answer", type="primary"):
#         executor = build_executor(knowledge_text=knowledge_text)
#         answer = executor.run(question=question, top_k=top_k)
#         st.subheader("Answer")
#         st.text(answer)
#
#
# if __name__ == "__main__":
#     run()