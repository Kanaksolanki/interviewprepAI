from backend.ai.llm_client import call_llm


def get_course_suggestions(skill_gap):
    prompt = f"""
You are a career mentor.

Missing skills:
{skill_gap["missing_skills"]}

Suggest 3–5 beginner-friendly courses.

Format:
- Course Name - Platform
"""

    return call_llm(prompt)