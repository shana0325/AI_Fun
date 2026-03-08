from ai_knowledge_assistant.llm.llm_client import LLMClient


class RAGPipeline:

    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = LLMClient()

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

    def ask(self, query: str, top_k: int = 3):
        contexts = self.vector_store.search(query, top_k)

        prompt = self.build_prompt(query, contexts)

        answer = self.llm.ask(prompt)

        return answer, contexts
