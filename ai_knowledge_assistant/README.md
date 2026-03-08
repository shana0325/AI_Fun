# AI Knowledge Assistant (MVP)

A runnable minimal RAG + Agent project that demonstrates:

- Text chunking
- Hash embedding
- Cosine-similarity retrieval with Top-K results
- Agent orchestration with `search_knowledge`
- Local LLM stub answer generation (no external model API)

## Install

```bash
pip install -r ai_knowledge_assistant/requirements.txt
```

## Default knowledge source

The project now uses `ai_knowledge_assistant/data/knowledge.txt` as the default knowledge base.

## CLI

```bash
python -m ai_knowledge_assistant.app.main --question "What is the core RAG flow?" --top-k 3
```

Optional flags:

- `--knowledge-file`: custom local text file path
- `--chunk-size`: chunk size (default: 180)
- `--overlap`: chunk overlap (default: 30)

## Streamlit UI

```bash
streamlit run ai_knowledge_assistant/frontend/streamlit_app.py
```

The page supports question input, Top-K selection, and answer display.

## Tests

```bash
pytest -q
```

Coverage includes:

- chunking behavior
- retriever ranking
- end-to-end agent output