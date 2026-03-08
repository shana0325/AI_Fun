from pathlib import Path
from ai_knowledge_assistant.rag.document_loader import DocumentLoader


def main():

    loader = DocumentLoader()

    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "example.txt"

    text = loader.load(str(file_path))

    print("文档内容：")
    print(text[:500])


if __name__ == "__main__":
    main()