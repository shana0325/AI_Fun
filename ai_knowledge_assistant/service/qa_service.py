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

        self.documents = []

    def add_document(self, file_path):
        # 读取文档
        text = self.loader.load(file_path)

        # 文本切分
        chunks = self.splitter.split_text(text)

        # 添加到向量库
        self.vector_store.add_chunks(chunks, file_path)

        # 记录文档
        self.documents.append(file_path)

    def ask(self, question):

        return self.rag.ask(question)