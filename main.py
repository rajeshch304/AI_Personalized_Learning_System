'''from extract_text import text
from chunking import chunking
from embedding import get_embeddings,embed_single_text
from vector_store import VectorStore
# Step 1: chunk text
chunks = chunking(text, chunksize=1000, overlap=100)

print("Chunks:", len(chunks))

# Step 2: embeddings
embeddings = get_embeddings(chunks)

print("Embedding shape:", embeddings.shape)

# 3. Store in vector DB
store = VectorStore(dim=embeddings.shape[1])
store.add(embeddings, chunks)

print("Vector store ready!")'''
import streamlit as st
from src.extract_text import text
from src.chunking import chunking
from src.embedding import get_embeddings, embed_single_text
from src.vector_store import VectorStore
from src.llm import get_answer

# ---------------- INIT (runs once) ----------------
@st.cache_resource
def load_system():
    chunks = chunking(text, chunksize=1000, overlap=100)
    embeddings = get_embeddings(chunks)

    store = VectorStore(dim=embeddings.shape[1])
    store.add(embeddings, chunks)

    return store


store = load_system()

# ---------------- UI ----------------
st.set_page_config(page_title="PDF Chatbot", layout="wide")

st.title("AI Personlized Learning ")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_question = st.text_input("Ask a question from the PDF:")

if st.button("Ask"):
    if user_question:

        # 1. embed query
        query_embedding = embed_single_text(user_question)

        # 2. retrieve relevant chunks
        results = store.search(query_embedding, top_k=3)

        context = "\n\n".join(results)

        # 3. get answer from Groq
        answer = get_answer(context, user_question)

        # save history
        st.session_state.chat_history.append((user_question, answer))

# ---------------- CHAT DISPLAY ----------------
for q, a in reversed(st.session_state.chat_history):
    st.markdown(f"### 🧑 You: {q}")
    st.markdown(f"### 🤖 Bot: {a}")
    st.divider()