from ai_knowledge_assistant.llm.llm_client import LLMClient


class RAGPipeline:
    # 注入向量检索模块，并初始化 LLM 客户端。
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = LLMClient()

    # 把检索上下文和问题拼接成一个受约束提示词。
    def build_prompt(self, query: str, contexts: list[str]):
        context_text = "\n\n".join(contexts)

        prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the context below.

Context:
{context_text}

Question:
{query}

Answer:
"""

        return prompt

    # 完整 RAG 流程：检索 -> 构造提示词 -> 调用 LLM -> 返回答案和上下文。
    def ask(self, query: str, top_k: int = 3):
        contexts = self.vector_store.search(query, top_k)

        prompt = self.build_prompt(query, contexts)

        answer = self.llm.ask(prompt)

        return answer, contexts