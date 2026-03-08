from ai_knowledge_assistant.rag.retriever import SimpleRetriever


def test_retriever_ranks_relevant_chunk_first() -> None:
    chunks = [
        "apple banana fruit",
        "python code package",
        "soccer team goal",
    ]
    retriever = SimpleRetriever(chunks=chunks, dims=128)

    results = retriever.search("python package", top_k=2)

    assert len(results) == 2
    assert results[0].text == "python code package"
    assert results[0].score >= results[1].score