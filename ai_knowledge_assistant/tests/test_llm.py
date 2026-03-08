from ai_knowledge_assistant.llm.llm_client import LLMClient


def main():
    # 初始化 LLM 客户端并发起一次最小请求。
    llm = LLMClient()

    answer = llm.ask("什么是 RAG？")

    print("\nAI 回答:")
    print(answer)


if __name__ == "__main__":
    main()