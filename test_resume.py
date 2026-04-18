# from backend.resume.parser import extract_text
# from backend.resume.skill_extractor import extract_skills
# from backend.resume.job_recommender import recommend_jobs


# file_path = r"C:\Users\kanak solanki\OneDrive\Desktop\KanakSolanki_08101172023(res).pdf"

# print("\n🔹 STEP 1: Extract text")

# with open(file_path, "rb") as f:
#     text = extract_text(f)

# if not text.strip():
#     print("❌ No text extracted")
#     exit()

# print("✅ Text extracted")

# # -------------------------

# print("\n🔹 STEP 2: Extract skills")

# skills_dict = extract_skills(text)

# print("Skills (categorized):")
# for k, v in skills_dict.items():
#     print(f"{k}: {v}")

# # -------------------------

# print("\n🔹 STEP 3: Prepare features")

# features = {
#     "cleaned_text": text,
#     "skill_domains": list(skills_dict.keys()),
#     "skills": skills_dict,
#     "education_level": "bachelors",
#     "years_experience": 0
# }

# print("Domains:", features["skill_domains"])

# # -------------------------

# print("\n🔹 STEP 4: Job Recommendation")

# jobs = recommend_jobs(features)

# print("\n🎯 TOP JOBS:")
# for job in jobs:
#     print("\n-------------------")
#     print("Role:", job["title"])
#     print("Score:", job["score"])
#     print("Matched Skills:", job["matched_skills"])
#     print("Missing Skills:", job["missing_skills"])

# print("\n✅ PIPELINE WORKING")


from backend.resume.parser import extract_text
from backend.resume.skill_extractor import extract_skills
from backend.resume.job_recommender import recommend_jobs, display_recommendations


file_path = r"C:\Users\kanak solanki\OneDrive\Desktop\KanakSolanki_08101172023(res).pdf"

print("\n🔹 STEP 1: Extract text")

with open(file_path, "rb") as f:
    text = extract_text(f)

if not text.strip():
    print("❌ No text extracted")
    exit()

print("✅ Text extracted")

# -------------------------

print("\n🔹 STEP 2: Extract skills")

skills_dict = extract_skills(text)

print("Skills (categorized):")
for k, v in skills_dict.items():
    print(f"  {k}: {v}")

# -------------------------

print("\n🔹 STEP 3: Prepare features")

features = {
    "cleaned_text": text,
    "skill_domains": list(skills_dict.keys()),
    "skills": skills_dict,
    "education_level": "bachelors",
    "years_experience": 0
}

print("Domains:", features["skill_domains"])

# -------------------------

print("\n🔹 STEP 4: Job Recommendation")

jobs = recommend_jobs(features)

# Option A: use the built-in display helper (recommended)
display_recommendations(jobs)

# Option B: manual print loop if you want custom formatting
# Uncomment the block below and comment out display_recommendations(jobs) above
#
# print("\n🎯 TOP JOBS:")
# for job in jobs:
#     print("\n-------------------")
#     print("Role:              ", job["title"])
#     print("Score:             ", job["score"])
#     print("Matched Skills:    ", job["matched_skills"])
#
#     missing = job["missing_skills"]
#     critical    = missing.get("critical", [])
#     recommended = missing.get("recommended", [])
#
#     if critical:
#         print("⚠️  Critical Missing:", critical)
#     else:
#         print("⚠️  Critical Missing: None — great coverage!")
#
#     if recommended:
#         print("💡 Also Learn:       ", recommended)
#     else:
#         print("💡 Also Learn:        None")

print("\n✅ PIPELINE WORKING")