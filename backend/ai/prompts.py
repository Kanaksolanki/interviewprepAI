def hr_prompt(user_input):
    return f"""
You are a professional HR interviewer.

User request:
{user_input}

Instructions:
- Understand the user's intent carefully.
- If user asks ONLY for questions → return only questions.
- If user asks for answers → include answers in STAR format.
- Questions must be realistic and commonly asked in interviews.
- Keep answers concise and structured.
- Avoid generic or repetitive questions.

Output format:

1. Question
   Answer (if required):
   - Situation:
   - Task:
   - Action:
   - Result:

Generate high-quality content.
"""

def skill_extraction_prompt(resume_text):
    return f"""
You are an AI resume analyzer.

Extract all relevant technical and soft skills from the resume below.

Resume:
{resume_text}

Instructions:
- Return ONLY a list of skills.
- No explanation.
- Include programming languages, tools, frameworks, and soft skills.
- Avoid duplicates.

Output format:
["Python", "Machine Learning", "SQL", "Communication"]
"""

def skill_gap_prompt(user_skills, target_role):
    return f"""
You are a career advisor.

User skills:
{user_skills}

Target role:
{target_role}

Instructions:
- Identify missing important skills required for the target role.
- Be specific and relevant.
- Do not repeat existing skills.

Output format:
["System Design", "Graph Algorithms", "Docker"]
"""

def job_match_prompt(user_skills):
    return f"""
You are a career recommendation system.

User skills:
{user_skills}

Instructions:
- Suggest 3–5 suitable job roles.
- Give a match score (0–100%) for each role.
- Keep it realistic.

Output format:
[
  {{"role": "Software Engineer", "match": 80}},
  {{"role": "Data Analyst", "match": 65}}
]
"""

def course_prompt(skill_gap):
    return f"""
You are an AI career mentor.

Skill gaps:
{skill_gap}

Instructions:
- Recommend 3–5 courses to fill these gaps.
- Keep suggestions practical and beginner-friendly.

Output format:
[
  "Course Name - Platform",
  "Course Name - Platform"
]
"""

def project_prompt(role):
    return f"""
You are a tech mentor.

Target role:
{role}

Instructions:
- Suggest 3 practical projects.
- Each project should improve job readiness.
- Keep them resume-worthy.

Output format:
[
  "Project Name - short description",
  "Project Name - short description"
]
"""