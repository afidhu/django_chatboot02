
import requests
import numpy as np
from .models import DocumentChunk

OLLAMA_URL = "http://localhost:11434"

def get_embedding(text):
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )
    return response.json()["embedding"]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_relevant_chunks(question, top_k=3):
    question_embedding = get_embedding(question)
    chunks = DocumentChunk.objects.all()

    scored = []
    for chunk in chunks:
        score = cosine_similarity(
            question_embedding,
            chunk.embedding
        )
        scored.append((score, chunk.content))

    scored.sort(reverse=True)
    return [content for _, content in scored[:top_k]]