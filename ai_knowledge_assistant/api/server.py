from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from pathlib import Path

from ai_knowledge_assistant.service.qa_service import QAService

app = FastAPI()

qa_service = QAService()


class AskRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "AI Knowledge Assistant API running"}


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    project_root = Path(__file__).resolve().parent.parent.parent
    data_dir = project_root / "data"

    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / file.filename

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    qa_service.build_index(str(file_path))

    return {"status": "document uploaded and indexed"}


@app.post("/ask")
def ask_question(request: AskRequest):

    answer, contexts = qa_service.ask(request.question)

    return {
        "question": request.question,
        "answer": answer,
        "contexts": contexts
    }