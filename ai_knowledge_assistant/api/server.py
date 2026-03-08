from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from pathlib import Path

from ai_knowledge_assistant.service.qa_service import QAService

# FastAPI 应用实例。
app = FastAPI()

# 复用一个 QA 服务实例，负责建索引和问答。
qa_service = QAService()


# /ask 接口的请求体结构。
class AskRequest(BaseModel):
    question: str


# 健康检查接口。
@app.get("/")
def root():
    return {"message": "AI Knowledge Assistant API running"}


# 文档上传接口：保存文件并立即构建索引。
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    # 项目根目录：.../New project
    project_root = Path(__file__).resolve().parent.parent.parent
    data_dir = project_root / "data"

    # 确保 data 目录存在。
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / file.filename

    # 以二进制方式写入上传文件。
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # 上传后立刻重建索引。
    # qa_service.build_index(str(file_path))

    # 上传后不重建而是增加索引。
    qa_service.add_document(file_path)

    return {"status": "document uploaded and indexed"}


# 问答接口：基于已构建索引进行 RAG 回答
@app.post("/ask")
def ask_question(request: AskRequest):

    # 调用 QAService 执行 RAG 问答
    # answer：LLM生成的回答
    # contexts：检索到的文本片段（包含 source 信息）
    answer, contexts = qa_service.ask(request.question)

    # 返回回答 + 来源信息
    return {
        "question": request.question,
        "answer": answer,
        "sources": contexts
    }