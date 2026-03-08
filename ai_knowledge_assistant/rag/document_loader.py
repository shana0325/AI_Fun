"""Document loading utilities for RAG."""

# 历史版本的示例实现保留在注释中，便于对比演进。
# from __future__ import annotations
#
# from pathlib import Path
#
#
# def load_text_file(file_path: str) -> str:
#     """Load UTF-8 text from a local file path."""
#     path = Path(file_path)
#     if not path.exists():
#         raise FileNotFoundError(f"file not found: {file_path}")
#     if not path.is_file():
#         raise ValueError(f"path is not a file: {file_path}")
#     return path.read_text(encoding="utf-8")
#
#
# def load_documents(paths: list[str]) -> list[str]:
#     """Load multiple text documents and return raw text list."""
#     return [load_text_file(path) for path in paths]

from pathlib import Path
from pypdf import PdfReader


class DocumentLoader:
    # 读取 txt 文件并返回全文字符串。
    def load_txt(self, file_path: str) -> str:
        """
        读取 txt 文件
        """
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    # 逐页读取 PDF，并把每页文本拼接为一个字符串。
    def load_pdf(self, file_path: str) -> str:
        """
        读取 PDF 文件
        """
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        return text

    # 按文件后缀自动分发到对应加载函数。
    def load(self, file_path: str) -> str:
        """
        自动识别文件类型
        """
        path = Path(file_path)

        if path.suffix == ".txt":
            return self.load_txt(file_path)

        elif path.suffix == ".pdf":
            return self.load_pdf(file_path)

        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")