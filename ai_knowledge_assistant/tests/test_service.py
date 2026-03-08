from pathlib import Path

from ai_knowledge_assistant.service.qa_service import QAService


def main():
    # 计算项目根目录下示例数据路径。
    project_root = Path(__file__).resolve().parents[2]
    file_path = project_root / "data" / "example.txt"

    # 初始化服务并构建索引。
    service = QAService()
    service.build_index(str(file_path))

    # 发起一个最小问答请求。
    question = "What is RAG?"

    answer, contexts = service.ask(question)

    # 打印问题与回答，用于手工验证链路是否跑通。
    print("\nQuestion:", question)
    print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()