from urllib import response

from django.shortcuts import render

# Create your views here.

import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .rag import retrieve_relevant_chunks

OLLAMA_URL = "http://localhost:11434"

ALLOWED_KEYWORDS = [
    "registration",
    "course",
    "deadline",
    "fees",
    "documents",
    "academic"
]

@csrf_exempt
def chat(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"})

    body = json.loads(request.body)
    user_message = body.get("message", "")

    # ✅ LEVEL 3 — Keyword Filtering
    if not any(word in user_message.lower() for word in ALLOWED_KEYWORDS):
        return JsonResponse({
            "reply": "I only answer academic registration related questions."
        })

    # ✅ LEVEL 2 — Retrieve Relevant Context
    relevant_chunks = retrieve_relevant_chunks(user_message)

    if not relevant_chunks:
        return JsonResponse({
            "reply": "This question is outside academic registration scope."
        })

    context = "\n\n".join(relevant_chunks[:3])

    # ✅ LEVEL 1 — Strong System Prompt Restriction
    prompt = f"""
You are an Academic Registration Assistant.

Rules:
- Answer ONLY using the provided context.
- If answer is not in context, say:
  "The information is not available in the academic registration system."
- Do NOT use outside knowledge.
- Do NOT answer unrelated questions.

Context:
{context}

Question:
{user_message}

Answer:
"""

    response = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={
            "model": "smollm2:1.7b",
            "prompt": prompt,
            "max_tokens": 128,
            "context_length": 512,
            "stream": True
        },
        stream=True,
        timeout=180
    )

    full_reply = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line)          # each line is a separate JSON
            text = data.get("response", "")
            full_reply += text               # collect all text
            print(text, end="", flush=True)  # optional: print word by word

    return JsonResponse({"reply": full_reply})