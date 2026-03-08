from pathlib import Path

from ai_knowledge_assistant.rag.document_loader import DocumentLoader
from ai_knowledge_assistant.rag.text_splitter import TextSplitter
from ai_knowledge_assistant.rag.vector_store import VectorStore
from ai_knowledge_assistant.rag.rag_pipeline import RAGPipeline


def main():
    # 数据准备：加载文本并切块。
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "example.txt"

    loader = DocumentLoader()
    text = loader.load(str(file_path))

    splitter = TextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)

    # 建索引并初始化 RAG 流水线。
    vector_store = VectorStore()
    vector_store.build_index(chunks)

    rag = RAGPipeline(vector_store)

    question = "What is RAG?"

    # 执行问答，拿到答案和检索到的上下文。
    answer, contexts = rag.ask(question)

    print("\nQuestion:", question)

    print("\nRetrieved Context:")

    for c in contexts:
        print("\n", c)

    print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()