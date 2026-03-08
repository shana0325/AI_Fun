from pathlib import Path

from ai_knowledge_assistant.service.qa_service import QAService


def main():

    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / "data" / "example.txt"

    service = QAService()

    service.build_index(str(file_path))

    question = "What is RAG?"

    answer, contexts = service.ask(question)

    print("\nQuestion:", question)

    print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()