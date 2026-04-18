import json
from typing import List


def find_skill_gap(user_skills: List[str], role: str):
    with open("data/roles.json") as f:
        roles = json.load(f)

    if role not in roles:
        return {"error": "Role not found"}

    required_skills = roles[role]

    user_skills_lower = [s.lower() for s in user_skills]

    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in user_skills_lower
    ]

    match_count = sum(
        1 for skill in required_skills
        if skill.lower() in user_skills_lower
    )

    match_percentage = (
        (match_count / len(required_skills)) * 100
        if required_skills else 0
    )

    return {
        "role": role,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }