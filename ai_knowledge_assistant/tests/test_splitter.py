from pathlib import Path

from ai_knowledge_assistant.rag.document_loader import DocumentLoader
from ai_knowledge_assistant.rag.text_splitter import TextSplitter


def main():
    # 读取示例文本。
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "example.txt"

    loader = DocumentLoader()
    text = loader.load(str(file_path))

    # 配置切块参数并执行切分。
    splitter = TextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)

    # 打印切块结果，便于肉眼确认分块效果。
    print("Chunk 数量:", len(chunks))

    for i, chunk in enumerate(chunks[:3]):
        print("\nChunk", i)
        print(chunk)


if __name__ == "__main__":
    main()