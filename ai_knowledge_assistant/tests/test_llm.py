
from ai_knowledge_assistant.llm.llm_client import LLMClient

def main():
    llm = LLMClient()

    answer = llm.ask("什么是RAG？")

    print("\nAI回答：")
    print(answer)


if __name__ == "__main__":
    main()