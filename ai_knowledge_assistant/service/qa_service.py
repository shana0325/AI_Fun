from pathlib import Path

from ai_knowledge_assistant.rag.document_loader import DocumentLoader
from ai_knowledge_assistant.rag.text_splitter import TextSplitter
from ai_knowledge_assistant.rag.vector_store import VectorStore
from ai_knowledge_assistant.rag.rag_pipeline import RAGPipeline


class QAService:
    # 负责串联“加载文档 -> 切块 -> 建索引 -> 问答”的服务层。
    def __init__(self):
        # 文档读取器：支持按文件类型读取内容。
        self.loader = DocumentLoader()
        # 文本切分器：控制 chunk 大小和重叠，提升召回效果。
        self.splitter = TextSplitter(chunk_size=500, chunk_overlap=100)

        # 向量检索存储。
        self.vector_store = VectorStore()
        # RAG 主流程（检索 + 生成）。
        self.rag = RAGPipeline(self.vector_store)

        # 标记索引是否已构建，防止未建索引直接提问。
        self.index_ready = False

    # 从指定文件构建向量索引。
    def build_index(self, file_path: str):
        print("Loading document...")

        # 1) 读取原始文本。
        text = self.loader.load(file_path)

        print("Splitting document...")

        # 2) 文本切块。
        chunks = self.splitter.split_text(text)

        print(f"Chunks created: {len(chunks)}")

        # 3) 建立向量索引，供后续检索。
        self.vector_store.build_index(chunks)

        self.index_ready = True

    # 对外问答接口：先检索上下文，再调用 LLM 回答。
    def ask(self, question: str):
        if not self.index_ready:
            raise RuntimeError("Index not built yet")

        answer, contexts = self.rag.ask(question)

        return answer, contexts