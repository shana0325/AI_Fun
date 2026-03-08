from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class VectorStore:

    def __init__(self, model_name="BAAI/bge-base-en-v1.5"):

        self.model = SentenceTransformer(model_name)

        self.index = None
        self.chunks = []

    def add_chunks(self, chunks, source):

        # 生成 embedding
        embeddings = self.model.encode(chunks)

        embeddings = np.array(embeddings).astype("float32")

        # 如果 index 不存在就初始化
        if self.index is None:
            dimension = embeddings.shape[1]

            self.index = faiss.IndexFlatL2(dimension)

        # 添加向量
        self.index.add(embeddings)

        # 保存 chunk + 来源
        for chunk in chunks:
            self.chunks.append({
                "text": chunk,
                "source": source
            })

    def search(self, query, top_k=3):

        query_embedding = self.model.encode([query])

        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results