from backend.ai.llm_client import call_llm


def generate_hr_questions(user_input):
    prompt = f"""
You are an expert HR interviewer.

User request:
{user_input}

Instructions:
- If user asks only questions → return only questions
- If user asks for answers → include answers in STAR format
- Keep answers concise and structured
- Generate realistic interview questions

Return in this format:

1. Question
   Answer (if required):
   - Situation:
   - Task:
   - Action:
   - Result:
"""

    response = call_llm(prompt)
    return response