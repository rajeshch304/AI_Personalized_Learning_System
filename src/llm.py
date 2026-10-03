import os
from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)
model_name = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


def get_answer(context, question):
    prompt = f"""
You are a helpful assistant.

Context:
{context}

Question:
{question}

Answer clearly and simply.
"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content