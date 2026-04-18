import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

# 🔥 List of free models (priority order)
FREE_MODELS = [
    "meta-llama/llama-3-8b-instruct:free",
    "mistralai/mistral-7b-instruct:free",
    "google/gemma-7b-it:free"
]

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "http://localhost:8501",
    "X-Title": "InterviewPrepAI",
    "Content-Type": "application/json"
}


def call_llm(prompt):
    for model in FREE_MODELS:
        try:
            data = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are an expert interview assistant."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }

            response = requests.post(URL, headers=HEADERS, json=data)

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            else:
                print(f"Model failed: {model}")

        except Exception as e:
            print(f"Error with {model}: {e}")

    return "⚠️ All free models failed. Try again later."