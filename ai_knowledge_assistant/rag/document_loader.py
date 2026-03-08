from pathlib import Path
from pypdf import PdfReader


class DocumentLoader:

    # 读取 txt 文件并返回全文字符串
    def load_txt(self, file_path: str) -> str:
        """
        读取 txt 文件
        为了兼容 Windows txt 文件，尝试多种编码
        """

        # 常见文本编码
        encodings = ["utf-8", "gbk", "latin-1"]

        for encoding in encodings:

            try:
                with open(file_path, "r", encoding=encoding) as f:
                    return f.read()

            except UnicodeDecodeError:
                # 如果当前编码失败，尝试下一种
                continue

        # 所有编码都失败
        raise ValueError(f"Cannot decode txt file: {file_path}")

    # 逐页读取 PDF，并把每页文本拼接为一个字符串
    def load_pdf(self, file_path: str) -> str:
        """
        读取 PDF 文件
        """

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            # 有些 PDF 页面可能没有文本
            if page_text:
                text += page_text + "\n"

        return text

    # 根据文件后缀自动选择加载方式
    def load(self, file_path: str) -> str:
        """
        自动识别文件类型并调用对应加载函数
        """

        path = Path(file_path)

        # 统一小写，防止 .PDF / .Txt
        suffix = path.suffix.lower()

        if suffix == ".txt":
            return self.load_txt(file_path)

        elif suffix == ".pdf":
            return self.load_pdf(file_path)

        else:
            raise ValueError(f"Unsupported file type: {suffix}")