from ai_knowledge_assistant.llm.llm_client import LLMClient


class RAGPipeline:

    # 初始化 RAGPipeline
    # vector_store：向量检索模块（FAISS + embedding）
    def __init__(self, vector_store):

        # 保存向量检索实例
        self.vector_store = vector_store

        # 初始化大语言模型客户端（DeepSeek API）
        self.llm = LLMClient()

    # 构造 Prompt
    # query：用户问题
    # contexts：检索到的文本片段
    def build_prompt(self, query: str, contexts: list[dict]):

        # 从 contexts 中提取文本
        context_text = "\n\n".join([c["text"] for c in contexts])

        # Prompt 模板
        # 优先使用知识库内容，如果不足可以使用模型自身知识
        prompt = f"""
You are a helpful AI assistant.

Use the context below to answer the question.
If the context is insufficient, you may use your general knowledge.

Context:
{context_text}

Question:
{query}

Answer:
"""

        return prompt

    # RAG 主流程
    # 1. 向量检索
    # 2. 构造 Prompt
    # 3. 调用 LLM
    # 4. 返回答案 + sources
    def ask(self, query: str, top_k: int = 3):

        # Step1：语义检索
        # 返回 top_k 个最相关的文本片段
        contexts = self.vector_store.search(query, top_k)

        # Step2：构造 Prompt
        prompt = self.build_prompt(query, contexts)

        # Step3：调用 LLM 生成答案
        answer = self.llm.ask(prompt)

        # Step4：返回答案 + 上下文（用于显示 sources）
        return answer, contexts