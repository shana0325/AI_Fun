from pathlib import Path

from ai_knowledge_assistant.rag.document_loader import DocumentLoader
from ai_knowledge_assistant.rag.text_splitter import TextSplitter
from ai_knowledge_assistant.rag.vector_store import VectorStore


def main():
    # 读取并切分文档。
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "example.txt"

    loader = DocumentLoader()
    text = loader.load(str(file_path))

    splitter = TextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)

    # 建立向量索引并执行检索。
    vector_store = VectorStore()
    vector_store.build_index(chunks)

    results = vector_store.search("What is RAG?", top_k=3)

    print("\nSearch Results:")

    for r in results:
        print("\n", r)


if __name__ == "__main__":
    main()