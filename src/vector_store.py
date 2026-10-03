import faiss
import numpy as np
import pickle


class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunks = []

    def add(self, embeddings, chunks):
        """
        Store embeddings + corresponding text
        """
        self.index.add(np.array(embeddings).astype('float32'))
        self.text_chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        """
        Search similar chunks
        """
        query_embedding = np.array(query_embedding).astype('float32').reshape(1, -1)

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.text_chunks[idx])

        return results

    def save(self, path="vector_store.pkl"):
        with open(path, "wb") as f:
            pickle.dump((self.index, self.text_chunks), f)

    def load(self, path="vector_store.pkl"):
        with open(path, "rb") as f:
            self.index, self.text_chunks = pickle.load(f)
  