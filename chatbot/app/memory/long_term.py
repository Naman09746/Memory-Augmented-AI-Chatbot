from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle
from typing import List


class LongTermMemory:
    def __init__(
        self,
        index_path: str = "data/faiss_index/index.faiss",
        store_path: str = "data/faiss_index/store.pkl",
        embedding_model: str = "all-MiniLM-L6-v2",
    ):
        # ✅ Initialize embedder ONCE
        self.embedder = SentenceTransformer(embedding_model)

        self.index_path = index_path
        self.store_path = store_path
        self.dim = self.embedder.get_sentence_embedding_dimension()

        os.makedirs(os.path.dirname(index_path), exist_ok=True)

        if os.path.exists(index_path) and os.path.exists(store_path):
            self.index = faiss.read_index(index_path)
            with open(store_path, "rb") as f:
                self.store = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dim)
            self.store = []

    def add(self, text: str):
        embedding = self.embedder.encode([text])
        self.index.add(embedding)
        self.store.append(text)

        faiss.write_index(self.index, self.index_path)
        with open(self.store_path, "wb") as f:
            pickle.dump(self.store, f)

    def search(self, query: str, k: int = 3) -> List[str]:
        if len(self.store) == 0:
            return []

        query_embedding = self.embedder.encode([query])
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.store):
                results.append(self.store[idx])

        return results
