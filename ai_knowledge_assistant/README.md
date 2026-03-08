# AI Knowledge Assistant (MVP)

这是一个“可运行最小版本”示例，覆盖了一个基础 AI 知识助手闭环：

1. 文本切分（`rag/chunking.py`）
2. 向量化（`rag/embedding.py`）
3. 检索（`rag/retriever.py`）
4. Agent 编排（`agent/agent_executor.py`）
5. 本地 LLM Stub 生成回答（`llm/llm_client.py`）
6. CLI 入口 + Streamlit 页面

## 目录

```text
ai_knowledge_assistant/
├── app/main.py
├── rag/{chunking.py,embedding.py,retriever.py}
├── agent/{tools.py,agent_executor.py}
├── llm/llm_client.py
├── frontend/streamlit_app.py
└── tests/test_rag_flow.py
```

## 快速开始

```bash
cd ai_knowledge_assistant
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 运行 CLI

```bash
PYTHONPATH=.. python app/main.py "RAG 的核心流程是什么？"
```

### 运行测试

```bash
PYTHONPATH=.. pytest -q
```

### 运行 Streamlit

```bash
PYTHONPATH=.. streamlit run frontend/streamlit_app.py
```
