from pathlib import Path

from ai_knowledge_assistant.rag.document_loader import DocumentLoader
from ai_knowledge_assistant.rag.text_splitter import TextSplitter
from ai_knowledge_assistant.rag.vector_store import VectorStore
from ai_knowledge_assistant.rag.rag_pipeline import RAGPipeline


def main():

    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / "data" / "example.txt"

    loader = DocumentLoader()
    text = loader.load(str(file_path))

    splitter = TextSplitter(chunk_size=100, chunk_overlap=20)

    chunks = splitter.split_text(text)

    vector_store = VectorStore()
    vector_store.build_index(chunks)

    rag = RAGPipeline(vector_store)

    question = "What is RAG?"

    answer, contexts = rag.ask(question)

    print("\nQuestion:", question)

    print("\nRetrieved Context:")

    for c in contexts:
        print("\n", c)

    print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()