from typing import Dict, List

SKILL_KEYWORDS: Dict[str, Dict[str, List[str]]] = {

    # 🔹 Programming Languages
    "languages": {
        "Python": ["python"],
        "Java": ["java"],
        "JavaScript": ["javascript", "js", "typescript", "ts"],
        "C++": ["c++", "cpp"],
        "C#": ["c#", "csharp", ".net", "dotnet"],
        "Go": ["golang", "go"],
        "Rust": ["rust"],
        "Kotlin": ["kotlin"],
        "Swift": ["swift"],
        "PHP": ["php"],
        "Ruby": ["ruby"],
    },

    # 🔹 Web / Frontend
    "web": {
        "HTML": ["html"],
        "CSS": ["css"],
        "Bootstrap": ["bootstrap"],
        "Tailwind": ["tailwind"],
        "Sass": ["sass", "scss"],
    },

    # 🔹 Frameworks
    "frameworks": {
        "React": ["react", "reactjs"],
        "Next.js": ["nextjs", "next.js"],
        "Angular": ["angular"],
        "Vue": ["vue", "vuejs"],
        "Node.js": ["node", "nodejs"],
        "Express": ["express"],
        "Django": ["django"],
        "Flask": ["flask"],
        "FastAPI": ["fastapi"],
        "Spring Boot": ["springboot", "spring"],
    },

    # 🔹 Libraries
    "libraries": {
        "Pandas": ["pandas"],
        "NumPy": ["numpy"],
        "Matplotlib": ["matplotlib"],
        "Seaborn": ["seaborn"],
        "NLTK": ["nltk"],
        "OpenCV": ["opencv"],
        "Scikit-learn": ["scikit-learn", "sklearn"],
        "TensorFlow": ["tensorflow"],
        "PyTorch": ["pytorch"],
    },

    # 🔹 Databases
    "databases": {
        "MySQL": ["mysql"],
        "PostgreSQL": ["postgresql", "postgres"],
        "MongoDB": ["mongodb"],
        "Redis": ["redis"],
        "SQLite": ["sqlite"],
        "Firebase": ["firebase"],
    },

    # 🔹 Tools & DevOps
    "tools": {
        "Git": ["git", "github"],
        "Docker": ["docker"],
        "Kubernetes": ["kubernetes", "k8s"],
        "Linux": ["linux"],
        "Bash": ["bash", "shell"],
        "Jenkins": ["jenkins"],
        "GitHub Actions": ["github actions"],
    },

    # 🔹 Cloud
    "cloud": {
        "AWS": ["aws", "amazon web services"],
        "Azure": ["azure"],
        "GCP": ["gcp", "google cloud"],
    },

    # 🔹 Core CS
    "core_cs": {
        "Data Structures": ["data structures", "dsa"],
        "Algorithms": ["algorithms"],
        "DBMS": ["dbms"],
        "Operating Systems": ["operating system", "os"],
        "Computer Networks": ["computer networks", "networking"],
        "OOP": ["oop", "object oriented programming"],
    },

    # 🔹 AI / ML
    "ai_ml": {
        "Machine Learning": ["machine learning", "ml"],
        "Deep Learning": ["deep learning"],
        "NLP": ["nlp", "natural language processing"],
        "Computer Vision": ["computer vision"],
        "LLMs": ["llm", "gpt", "bert"],
    },

    # 🔹 Data / Analytics
    "data": {
        "Data Analysis": ["data analysis", "analytics"],
        "Data Visualization": ["data visualization"],
        "Excel": ["excel"],
        "Power BI": ["power bi"],
        "Tableau": ["tableau"],
    }
}


# 🚀 Extract skills
def extract_skills(text: str) -> Dict[str, List[str]]:
    text_lower = text.lower()

    found = {category: set() for category in SKILL_KEYWORDS}

    for category, skills in SKILL_KEYWORDS.items():
        for skill_name, keywords in skills.items():
            for keyword in keywords:
                if keyword in text_lower:
                    found[category].add(skill_name)
                    break

    return {k: list(v) for k, v in found.items() if v}


# 🔹 Flatten skills
def flatten_skills(skill_dict: Dict[str, List[str]]) -> List[str]:
    flat = []
    for skills in skill_dict.values():
        flat.extend(skills)
    return flat


# # 🔹 Test
# if __name__ == "__main__":
#     sample = """
#     Python, React, Node.js, MongoDB, Machine Learning, Docker, AWS,
#     Data Structures, Algorithms, HTML, CSS
#     """

#     skills = extract_skills(sample)
#     print("Extracted:", skills)
#     print("Flattened:", flatten_skills(skills))