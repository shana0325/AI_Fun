from pathlib import Path
from ai_knowledge_assistant.rag.document_loader import DocumentLoader


def main():
    # 创建文档加载器实例。
    loader = DocumentLoader()

    # 计算示例文本路径（相对项目根目录）。
    project_root = Path(__file__).resolve().parents[2]
    file_path = project_root / "data" / "example.txt"

    # 读取文档并打印前 500 字用于人工检查。
    text = loader.load(str(file_path))

    print("文档内容:")
    print(text[:500])


if __name__ == "__main__":
    main()