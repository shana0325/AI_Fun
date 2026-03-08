from pathlib import Path

from ai_knowledge_assistant.rag.document_loader import DocumentLoader
from ai_knowledge_assistant.rag.text_splitter import TextSplitter
from ai_knowledge_assistant.rag.vector_store import VectorStore
from ai_knowledge_assistant.rag.rag_pipeline import RAGPipeline


class QAService:

    def __init__(self):

        self.loader = DocumentLoader()
        self.splitter = TextSplitter(chunk_size=500, chunk_overlap=100)

        self.vector_store = VectorStore()

        self.rag = RAGPipeline(self.vector_store)

        self.index_ready = False

    def build_index(self, file_path: str):

        print("Loading document...")

        text = self.loader.load(file_path)

        print("Splitting document...")

        chunks = self.splitter.split_text(text)

        print(f"Chunks created: {len(chunks)}")

        self.vector_store.build_index(chunks)

        self.index_ready = True

    def ask(self, question: str):

        if not self.index_ready:
            raise RuntimeError("Index not built yet")

        answer, contexts = self.rag.ask(question)

        return answer, contexts