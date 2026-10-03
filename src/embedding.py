from sentence_transformers import SentenceTransformer
import numpy as np

# Load pretrained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embeddings(chunks):
    """
    Convert text chunks into vector embeddings
    """

    embeddings = model.encode(chunks, show_progress_bar=True)

    return np.array(embeddings)


def embed_single_text(text):
    """
    Embed a single string
    """
    return model.encode(text)


