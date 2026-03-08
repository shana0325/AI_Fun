# """Text splitter utilities for RAG."""
#
# from __future__ import annotations
#
#
# def split_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
#     """Split text into overlapped character chunks."""
#     if chunk_size <= 0:
#         raise ValueError("chunk_size must be > 0")
#     if overlap < 0:
#         raise ValueError("overlap must be >= 0")
#     if overlap >= chunk_size:
#         raise ValueError("overlap must be smaller than chunk_size")
#
#     normalized = " ".join(text.split())
#     if not normalized:
#         return []
#
#     chunks: list[str] = []
#     step = chunk_size - overlap
#     start = 0
#     while start < len(normalized):
#         end = min(start + chunk_size, len(normalized))
#         chunks.append(normalized[start:end])
#         if end >= len(normalized):
#             break
#         start += step
#     return chunks
#
#
# def split_documents(documents: list[str], chunk_size: int = 300, overlap: int = 50) -> list[str]:
#     """Split multiple documents and flatten chunks into one list."""
#     chunks: list[str] = []
#     for doc in documents:
#         chunks.extend(split_text(doc, chunk_size=chunk_size, overlap=overlap))
#     return chunks


class TextSplitter:
    # 初始化切块参数：每块长度 + 相邻块重叠长度。
    def __init__(self, chunk_size=500, chunk_overlap=100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    # 按固定窗口切分文本，输出用于向量化检索的 chunks。
    def split_text(self, text: str):

        chunks = []

        start = 0
        text_length = len(text)

        while start < text_length:
            # 当前窗口结束位置。
            end = start + self.chunk_size

            # 切出一个 chunk。
            chunk = text[start:end]

            chunks.append(chunk)

            # 下一个窗口起点 = 当前起点 + 有效步长（考虑 overlap）。
            start += self.chunk_size - self.chunk_overlap

        return chunks