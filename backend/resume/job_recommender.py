# import math
# import re
# from collections import Counter
# from typing import Dict, List


# # ============================================================
# # DOMAIN ALIAS MAP
# # Maps the domains your resume parser produces  ──►  the
# # canonical domain names used in JOB_PROFILES below.
# # ============================================================
# DOMAIN_ALIAS_MAP: Dict[str, str] = {
#     # languages
#     "languages":          "python",
#     "python":             "python",
#     "javascript":         "javascript",
#     "java":               "java",
#     "c_cpp":              "c_cpp",
#     "kotlin":             "kotlin",
#     "swift":              "swift",
#     "scala":              "scala",
#     "r_language":         "r_language",
#     "shell":              "shell",
#     # web / frameworks
#     "web":                "web_development",
#     "web_development":    "web_development",
#     "frameworks":         "web_development",
#     # data / ML
#     "ai_ml":              "machine_learning",
#     "machine_learning":   "machine_learning",
#     "data_science":       "data_science",
#     "data":               "data_science",
#     "data_engineering":   "data_engineering",
#     "ml_frameworks":      "ml_frameworks",
#     "libraries":          "ml_frameworks",
#     # databases
#     "databases":          "databases",
#     "sql":                "sql",
#     # infra / cloud
#     "devops":             "devops",
#     "cloud":              "cloud",
#     "tools":              "devops",
#     # specialties
#     "security":           "security",
#     "embedded":           "embedded",
#     "design":             "design",
#     "finance":            "finance",
#     "marketing":          "marketing",
#     "project_management": "project_management",
#     "healthcare":         "healthcare",
#     "core_cs":            "web_development",
# }


# # ============================================================
# # DOMAIN SKILL CATALOGUE
# # Canonical skill lists per domain. Used to compute
# # "missing skills" = catalogue skills NOT in the resume.
# # ============================================================
# DOMAIN_SKILL_CATALOGUE: Dict[str, List[str]] = {
#     "python":           ["Python", "OOP", "Virtual Environments", "pip", "Poetry"],
#     "javascript":       ["JavaScript", "TypeScript", "Node.js", "ES6+", "npm"],
#     "java":             ["Java", "Spring Boot", "Maven", "JUnit", "Gradle"],
#     "c_cpp":            ["C", "C++", "CMake", "GDB", "Valgrind"],
#     "kotlin":           ["Kotlin", "Android SDK", "Jetpack Compose", "Gradle"],
#     "swift":            ["Swift", "SwiftUI", "Xcode", "CocoaPods", "UIKit"],
#     "scala":            ["Scala", "Akka", "sbt", "Functional Programming"],
#     "r_language":       ["R", "ggplot2", "dplyr", "tidyr", "RMarkdown"],
#     "shell":            ["Bash", "Zsh", "Shell Scripting", "AWK", "sed", "cron"],

#     "web_development":  ["REST API", "HTML", "CSS", "HTTP/HTTPS", "GraphQL",
#                          "WebSockets", "OAuth2", "JWT", "Swagger/OpenAPI"],

#     "machine_learning": ["Supervised Learning", "Unsupervised Learning",
#                          "Reinforcement Learning", "Model Evaluation",
#                          "Hyperparameter Tuning", "Cross-Validation",
#                          "Feature Engineering", "Gradient Boosting", "XGBoost"],

#     "ml_frameworks":    ["TensorFlow", "PyTorch", "Scikit-learn", "Keras",
#                          "Hugging Face", "ONNX", "MLflow", "Weights & Biases"],

#     "data_science":     ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly",
#                          "Statistics", "Hypothesis Testing", "A/B Testing",
#                          "Data Wrangling", "EDA"],

#     "data_engineering": ["Apache Spark", "Apache Kafka", "Apache Airflow",
#                          "dbt", "Snowflake", "BigQuery", "Redshift",
#                          "ETL Pipelines", "Data Lake", "Data Warehouse"],

#     "sql":              ["SQL", "PostgreSQL", "MySQL", "Query Optimization",
#                          "Joins", "Window Functions", "Stored Procedures",
#                          "Indexing", "Transactions"],

#     "databases":        ["MongoDB", "Redis", "Cassandra", "Elasticsearch",
#                          "Database Design", "ORM", "Connection Pooling"],

#     "devops":           ["Docker", "Kubernetes", "CI/CD", "Jenkins",
#                          "GitHub Actions", "Terraform", "Ansible",
#                          "Helm", "ArgoCD", "Prometheus", "Grafana"],

#     "cloud":            ["AWS", "Azure", "GCP", "S3", "EC2", "Lambda",
#                          "Cloud IAM", "VPC", "Load Balancing", "Auto Scaling"],

#     "security":         ["OWASP Top 10", "Penetration Testing", "SIEM", "Splunk",
#                          "Nmap", "Wireshark", "Metasploit", "Burp Suite",
#                          "Vulnerability Assessment", "Incident Response"],

#     "embedded":         ["C/C++ for Embedded", "RTOS", "Microcontrollers",
#                          "Arduino", "Raspberry Pi", "UART", "SPI", "I2C",
#                          "FPGA", "PCB Design"],

#     "design":           ["Figma", "Adobe XD", "Wireframing", "Prototyping",
#                          "User Research", "Usability Testing", "Design Systems",
#                          "Information Architecture", "Accessibility (WCAG)"],

#     "finance":          ["Financial Modeling", "Excel", "Bloomberg Terminal",
#                          "DCF Valuation", "Portfolio Management", "CFA",
#                          "Risk Management", "Derivatives"],

#     "marketing":        ["Google Analytics", "Google Ads", "SEO", "SEM",
#                          "HubSpot", "Salesforce", "Email Campaigns",
#                          "Social Media Marketing", "A/B Testing"],

#     "project_management": ["Agile", "Scrum", "Kanban", "Jira", "Confluence",
#                             "Stakeholder Management", "Risk Management",
#                             "Sprint Planning", "PMP", "Roadmapping"],

#     "healthcare":       ["HL7 / FHIR", "HIPAA Compliance", "EHR Systems",
#                          "Epic / Cerner", "Clinical Data Analysis",
#                          "ICD Coding", "Bioinformatics"],
# }


# # Per-job curated key skills — the most critical ones recruiters look for.
# # Missing skills from this list are surfaced as "critical".
# JOB_KEY_SKILLS: Dict[str, List[str]] = {
#     "Backend Software Engineer":
#         ["REST API", "Docker", "PostgreSQL", "Redis", "CI/CD"],
#     "Frontend Developer":
#         ["TypeScript", "React", "CSS", "Webpack/Vite", "Accessibility (WCAG)"],
#     "Full Stack Developer":
#         ["React", "Node.js", "PostgreSQL", "Docker", "CI/CD"],
#     "Mobile App Developer (Android/iOS)":
#         ["Kotlin", "Swift", "Firebase", "Jetpack Compose", "SwiftUI"],
#     "DevOps / Cloud Engineer":
#         ["Kubernetes", "Terraform", "AWS", "CI/CD", "Prometheus"],
#     "Site Reliability Engineer (SRE)":
#         ["Kubernetes", "Prometheus", "Grafana", "Incident Response", "SLO/SLA"],
#     "Data Scientist":
#         ["Scikit-learn", "Statistics", "A/B Testing", "Feature Engineering", "SQL"],
#     "Machine Learning Engineer":
#         ["MLflow", "Kubernetes", "ONNX", "CI/CD", "GPU/CUDA"],
#     "Data Analyst":
#         ["SQL", "Tableau/Power BI", "Statistics", "Excel", "A/B Testing"],
#     "Data Engineer":
#         ["Apache Spark", "Apache Airflow", "dbt", "Snowflake", "Kafka"],
#     "NLP Engineer":
#         ["Hugging Face", "Transformers", "BERT/GPT", "spaCy", "LLM Fine-tuning"],
#     "Computer Vision Engineer":
#         ["OpenCV", "YOLO", "CNN Architectures", "ONNX", "GPU/CUDA"],
#     "AI Research Scientist":
#         ["Research Papers/LaTeX", "Reinforcement Learning",
#          "Diffusion Models", "PhD-level Math", "LLM Pre-training"],
#     "Cybersecurity Analyst":
#         ["SIEM/Splunk", "OWASP Top 10", "Incident Response",
#          "Firewalls", "Threat Hunting"],
#     "Penetration Tester":
#         ["Metasploit", "Burp Suite", "OSCP", "Nmap", "Exploit Development"],
#     "UI/UX Designer":
#         ["Figma", "User Research", "Prototyping",
#          "Design Systems", "Accessibility (WCAG)"],
#     "Embedded Systems Engineer":
#         ["RTOS", "UART/SPI/I2C", "FPGA", "PCB Design", "ARM Cortex"],
#     "Financial Analyst":
#         ["Financial Modeling", "DCF Valuation",
#          "Bloomberg Terminal", "CFA", "Excel"],
#     "Quantitative Analyst (Quant)":
#         ["Stochastic Calculus", "Derivatives Pricing",
#          "Time Series", "Backtesting", "R"],
#     "Digital Marketing Analyst":
#         ["Google Analytics", "Google Ads", "SEO", "HubSpot", "A/B Testing"],
#     "Technical Project Manager":
#         ["Jira", "Agile/Scrum", "Stakeholder Management",
#          "Risk Management", "PMP"],
#     "Product Manager":
#         ["Roadmapping", "User Stories", "A/B Testing",
#          "KPI Metrics", "Go-to-Market Strategy"],
#     "Health Informatics / Clinical Data Analyst":
#         ["HL7/FHIR", "HIPAA Compliance", "Epic/Cerner",
#          "SQL", "Clinical Trials"],
#     "Software Quality Assurance (QA) Engineer":
#         ["Selenium", "pytest", "API Testing", "CI/CD", "Test Automation"],
#     "Database Administrator (DBA)":
#         ["Query Optimization", "Replication", "High Availability",
#          "Backup & Recovery", "Oracle/MSSQL"],
# }


# JOB_PROFILES: List[Dict] = [
#     # ── Software Engineering ──────────────────────────────────
#     {
#         "title": "Backend Software Engineer",
#         "required_domains": ["python", "web_development"],
#         "preferred_domains": ["devops", "cloud", "databases", "sql"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "python django flask fastapi rest api microservices sql postgresql "
#             "mysql database design backend server side development git linux "
#             "docker api integration unit testing"
#         ),
#     },
#     {
#         "title": "Frontend Developer",
#         "required_domains": ["javascript", "web_development"],
#         "preferred_domains": ["design"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "javascript react angular vue html css typescript frontend ui "
#             "responsive design browser api state management redux rest api "
#             "webpack vite performance optimization accessibility"
#         ),
#     },
#     {
#         "title": "Full Stack Developer",
#         "required_domains": ["javascript", "web_development"],
#         "preferred_domains": ["python", "sql", "devops"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "full stack javascript react nodejs express python django rest api "
#             "html css sql mongodb postgresql git docker deployment "
#             "frontend backend integration ci cd agile"
#         ),
#     },
#     {
#         "title": "Mobile App Developer (Android/iOS)",
#         "required_domains": ["kotlin", "swift"],
#         "preferred_domains": ["java", "javascript"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "android kotlin java ios swift swiftui mobile development "
#             "flutter react native app store play store api integration "
#             "firebase mobile ui push notifications"
#         ),
#     },
#     {
#         "title": "DevOps / Cloud Engineer",
#         "required_domains": ["devops", "cloud"],
#         "preferred_domains": ["python", "shell"],
#         "min_experience": 1,
#         "min_education": "bachelors",
#         "description": (
#             "devops aws azure gcp docker kubernetes helm ci cd jenkins "
#             "github actions terraform ansible infrastructure as code "
#             "linux bash scripting monitoring prometheus grafana site reliability"
#         ),
#     },
#     {
#         "title": "Site Reliability Engineer (SRE)",
#         "required_domains": ["devops", "cloud", "shell"],
#         "preferred_domains": ["python", "databases"],
#         "min_experience": 2,
#         "min_education": "bachelors",
#         "description": (
#             "sre site reliability engineering kubernetes docker monitoring "
#             "alerting on call incident management linux bash python automation "
#             "availability scalability latency performance distributed systems"
#         ),
#     },

#     # ── Data / AI ─────────────────────────────────────────────
#     {
#         "title": "Data Scientist",
#         "required_domains": ["data_science", "machine_learning"],
#         "preferred_domains": ["python", "sql", "ml_frameworks"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "data science machine learning statistics python pandas numpy "
#             "scikit-learn model building evaluation feature engineering "
#             "exploratory data analysis visualization matplotlib seaborn "
#             "hypothesis testing regression classification clustering"
#         ),
#     },
#     {
#         "title": "Machine Learning Engineer",
#         "required_domains": ["machine_learning", "ml_frameworks"],
#         "preferred_domains": ["python", "data_engineering", "cloud"],
#         "min_experience": 1,
#         "min_education": "bachelors",
#         "description": (
#             "machine learning engineer mlops tensorflow pytorch deep learning "
#             "model deployment model serving api production pipeline feature store "
#             "training infrastructure gpu cuda distributed training"
#         ),
#     },
#     {
#         "title": "Data Analyst",
#         "required_domains": ["data_science", "sql"],
#         "preferred_domains": ["python", "r_language"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "data analyst sql excel power bi tableau data visualization "
#             "business intelligence reporting dashboards kpi metrics "
#             "data cleaning data wrangling python pandas statistics"
#         ),
#     },
#     {
#         "title": "Data Engineer",
#         "required_domains": ["data_engineering", "sql"],
#         "preferred_domains": ["python", "cloud", "scala"],
#         "min_experience": 1,
#         "min_education": "bachelors",
#         "description": (
#             "data engineer etl pipeline apache spark kafka airflow hadoop "
#             "sql python scala data warehouse data lake snowflake bigquery "
#             "redshift dbt streaming batch processing"
#         ),
#     },
#     {
#         "title": "NLP Engineer",
#         "required_domains": ["machine_learning", "ml_frameworks"],
#         "preferred_domains": ["python", "data_science"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "nlp natural language processing text mining bert gpt transformers "
#             "hugging face spacy nltk gensim text classification ner "
#             "sentiment analysis information extraction llm fine tuning"
#         ),
#     },
#     {
#         "title": "Computer Vision Engineer",
#         "required_domains": ["machine_learning", "ml_frameworks"],
#         "preferred_domains": ["python", "embedded"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "computer vision opencv pytorch tensorflow image processing "
#             "object detection segmentation cnn feature extraction yolo "
#             "video analytics image classification deep learning"
#         ),
#     },
#     {
#         "title": "AI Research Scientist",
#         "required_domains": ["machine_learning", "ml_frameworks", "data_science"],
#         "preferred_domains": ["python", "r_language"],
#         "min_experience": 2,
#         "min_education": "masters",
#         "description": (
#             "research scientist deep learning reinforcement learning generative models "
#             "gans diffusion models llm pretraining finetuning arxiv publications "
#             "pytorch tensorflow statistical learning theory phd"
#         ),
#     },

#     # ── Cybersecurity ─────────────────────────────────────────
#     {
#         "title": "Cybersecurity Analyst",
#         "required_domains": ["security"],
#         "preferred_domains": ["devops", "shell"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "cybersecurity soc analyst siem splunk threat detection incident response "
#             "vulnerability scanning penetration testing network security "
#             "firewall ids ips owasp ethical hacking"
#         ),
#     },
#     {
#         "title": "Penetration Tester",
#         "required_domains": ["security", "shell"],
#         "preferred_domains": ["c_cpp", "python"],
#         "min_experience": 1,
#         "min_education": "bachelors",
#         "description": (
#             "penetration testing ethical hacking red team metasploit burp suite "
#             "nmap wireshark exploit development vulnerability assessment "
#             "ceh oscp ctf linux bash python web application security"
#         ),
#     },

#     # ── Design / UX ───────────────────────────────────────────
#     {
#         "title": "UI/UX Designer",
#         "required_domains": ["design"],
#         "preferred_domains": ["javascript", "web_development"],
#         "min_experience": None,
#         "min_education": None,
#         "description": (
#             "ui ux design figma sketch adobe xd wireframing prototyping "
#             "user research usability testing design system component library "
#             "interaction design information architecture accessibility"
#         ),
#     },

#     # ── Embedded / Hardware ───────────────────────────────────
#     {
#         "title": "Embedded Systems Engineer",
#         "required_domains": ["embedded"],
#         "preferred_domains": ["c_cpp", "shell"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "embedded systems firmware c c++ rtos microcontroller arduino "
#             "raspberry pi iot fpga verilog vhdl pcb circuit design "
#             "uart spi i2c real time operating system"
#         ),
#     },

#     # ── Finance / Quant ───────────────────────────────────────
#     {
#         "title": "Financial Analyst",
#         "required_domains": ["finance"],
#         "preferred_domains": ["data_science", "sql"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "financial analyst excel financial modeling valuation dcf lbo "
#             "bloomberg equity research portfolio management investment banking "
#             "accounting cfa chartered financial analyst reporting"
#         ),
#     },
#     {
#         "title": "Quantitative Analyst (Quant)",
#         "required_domains": ["finance", "machine_learning"],
#         "preferred_domains": ["python", "r_language", "data_science"],
#         "min_experience": None,
#         "min_education": "masters",
#         "description": (
#             "quantitative analyst quant python r stochastic calculus "
#             "derivatives pricing risk management algorithmic trading "
#             "statistics time series mathematical finance"
#         ),
#     },

#     # ── Marketing / Growth ────────────────────────────────────
#     {
#         "title": "Digital Marketing Analyst",
#         "required_domains": ["marketing"],
#         "preferred_domains": ["data_science", "sql"],
#         "min_experience": None,
#         "min_education": None,
#         "description": (
#             "digital marketing seo sem google analytics google ads "
#             "facebook ads social media marketing content strategy "
#             "email campaigns crm hubspot salesforce marketing analytics"
#         ),
#     },

#     # ── Project Management ────────────────────────────────────
#     {
#         "title": "Technical Project Manager",
#         "required_domains": ["project_management"],
#         "preferred_domains": ["devops", "web_development"],
#         "min_experience": 2,
#         "min_education": None,
#         "description": (
#             "project manager agile scrum kanban jira confluence "
#             "stakeholder management sprint planning roadmap delivery "
#             "risk management technical team budget tracking pmp"
#         ),
#     },
#     {
#         "title": "Product Manager",
#         "required_domains": ["project_management"],
#         "preferred_domains": ["data_science", "marketing"],
#         "min_experience": 2,
#         "min_education": "bachelors",
#         "description": (
#             "product manager product roadmap user stories backlog "
#             "agile scrum stakeholder alignment go to market strategy "
#             "kpi metrics product analytics a/b testing customer research"
#         ),
#     },

#     # ── Healthcare / Bio ──────────────────────────────────────
#     {
#         "title": "Health Informatics / Clinical Data Analyst",
#         "required_domains": ["healthcare"],
#         "preferred_domains": ["data_science", "sql"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "health informatics ehr fhir hl7 hipaa clinical data "
#             "medical records patient data sql python healthcare analytics "
#             "epic cerner clinical trials bioinformatics"
#         ),
#     },

#     # ── General Software Roles ────────────────────────────────
#     {
#         "title": "Software Quality Assurance (QA) Engineer",
#         "required_domains": ["web_development"],
#         "preferred_domains": ["python", "javascript", "devops"],
#         "min_experience": None,
#         "min_education": "bachelors",
#         "description": (
#             "qa engineer software testing manual testing automated testing "
#             "selenium pytest junit test cases regression testing "
#             "api testing postman jira bug tracking agile"
#         ),
#     },
#     {
#         "title": "Database Administrator (DBA)",
#         "required_domains": ["sql", "databases"],
#         "preferred_domains": ["shell", "devops"],
#         "min_experience": 1,
#         "min_education": "bachelors",
#         "description": (
#             "database administrator dba postgresql mysql oracle mssql "
#             "performance tuning query optimization backup recovery "
#             "replication high availability indexing stored procedures"
#         ),
#     },
# ]


# # ============================================================
# # TF-IDF HELPERS
# # ============================================================

# def _tokenize(text: str) -> List[str]:
#     return re.findall(r"[a-z0-9]+", text.lower())


# def _tf(tokens):
#     counts = Counter(tokens)
#     total = len(tokens) or 1
#     return {t: c / total for t, c in counts.items()}


# def _idf(corpus):
#     N = len(corpus)
#     df = {}
#     for doc in corpus:
#         for term in set(doc):
#             df[term] = df.get(term, 0) + 1
#     return {t: math.log((N + 1) / (d + 1)) + 1 for t, d in df.items()}


# def _tfidf(tokens, idf):
#     tf = _tf(tokens)
#     return {t: tf[t] * idf.get(t, 1.0) for t in tf}


# def _cosine(v1, v2):
#     common = set(v1) & set(v2)
#     if not common:
#         return 0.0
#     dot = sum(v1[t] * v2[t] for t in common)
#     mag1 = math.sqrt(sum(x * x for x in v1.values()))
#     mag2 = math.sqrt(sum(x * x for x in v2.values()))
#     if mag1 == 0 or mag2 == 0:
#         return 0.0
#     return dot / (mag1 * mag2)


# # ============================================================
# # DOMAIN NORMALISATION
# # ============================================================

# def _normalize_domains(raw_domains: List[str]) -> List[str]:
#     canonical = set()
#     for d in raw_domains:
#         mapped = DOMAIN_ALIAS_MAP.get(d.lower())
#         canonical.add(mapped if mapped else d.lower())
#     return list(canonical)


# # ============================================================
# # MISSING SKILLS DETECTION
# # ============================================================

# def _get_missing_skills(
#     job: Dict,
#     candidate_domains: List[str],
#     candidate_skills_flat: List[str],
# ) -> Dict[str, List[str]]:
#     """
#     Returns:
#       "critical"    – high-priority skills from JOB_KEY_SKILLS not on resume
#       "recommended" – catalogue skills from domains the candidate doesn't cover
#     Skills already present in the resume (case-insensitive) are excluded.
#     """
#     resume_lower = {s.lower() for s in candidate_skills_flat}

#     def _missing(skill: str) -> bool:
#         return skill.lower() not in resume_lower

#     # ── Critical: job's must-have skills not on resume ───────
#     critical_missing = [
#         s for s in JOB_KEY_SKILLS.get(job["title"], []) if _missing(s)
#     ]

#     # ── Recommended: catalogue skills for domains the candidate
#     #    doesn't have at all (both required + preferred) ──────
#     all_job_domains = (
#         set(job["required_domains"]) | set(job.get("preferred_domains", []))
#     )
#     uncovered_domains = all_job_domains - set(candidate_domains)

#     recommended_missing = []
#     for domain in sorted(uncovered_domains):
#         for skill in DOMAIN_SKILL_CATALOGUE.get(domain, []):
#             if _missing(skill) and skill not in critical_missing:
#                 recommended_missing.append(skill)

#     return {
#         "critical":    critical_missing[:8],
#         "recommended": recommended_missing[:10],
#     }


# # ============================================================
# # MAIN FUNCTION
# # ============================================================

# def recommend_jobs(features: Dict, top_n: int = 5) -> List[Dict]:
#     """
#     features must contain:
#       - "cleaned_text"  : full resume text (str)
#       - "skill_domains" : list of domain strings from your parser
#       - "skills"        : dict mapping domain → list of skill strings
#     """
#     text        = features["cleaned_text"]
#     raw_domains = features["skill_domains"]
#     skills      = features["skills"]

#     # ── 1. Normalise domains & skills ────────────────────────
#     domains = _normalize_domains(raw_domains)

#     normalised_skills: Dict[str, List[str]] = {}
#     for raw_d, skill_list in skills.items():
#         canonical_d = DOMAIN_ALIAS_MAP.get(raw_d.lower(), raw_d.lower())
#         normalised_skills.setdefault(canonical_d, []).extend(skill_list)

#     # Flat list of every skill the candidate has (for missing-skill lookup)
#     all_candidate_skills: List[str] = [
#         s for lst in normalised_skills.values() for s in lst
#     ]

#     # ── 2. Build TF-IDF vectors ───────────────────────────────
#     resume_tokens = _tokenize(text)
#     job_tokens    = [_tokenize(j["description"]) for j in JOB_PROFILES]
#     corpus        = [resume_tokens] + job_tokens
#     idf           = _idf(corpus)
#     resume_vec    = _tfidf(resume_tokens, idf)
#     job_vecs      = [_tfidf(t, idf) for t in job_tokens]

#     # ── 3. Score every job ────────────────────────────────────
#     results = []

#     for i, job in enumerate(JOB_PROFILES):
#         req  = set(job["required_domains"])
#         pref = set(job.get("preferred_domains", []))

#         matched_req  = req  & set(domains)
#         matched_pref = pref & set(domains)

#         # Hard filter: must cover ≥ 1 required domain
#         if not matched_req:
#             continue

#         req_coverage  = len(matched_req)  / len(req)
#         pref_coverage = len(matched_pref) / max(len(pref), 1)
#         domain_score  = (4 * req_coverage + pref_coverage) / 5
#         tfidf_score   = _cosine(resume_vec, job_vecs[i])
#         score         = 0.75 * domain_score + 0.25 * tfidf_score

#         # Matched skills (what the candidate already has for this job)
#         matched_skills = []
#         for d in matched_req | matched_pref:
#             matched_skills.extend(normalised_skills.get(d, []))

#         # Missing skills
#         missing = _get_missing_skills(job, domains, all_candidate_skills)

#         results.append({
#             "title":          job["title"],
#             "score":          round(score * 100, 1),
#             "matched_skills": list(set(matched_skills))[:10],
#             "missing_skills": {
#                 "critical":    missing["critical"],
#                 "recommended": missing["recommended"],
#             },
#             # Domain debug info
#             "matched_required":  list(matched_req),
#             "matched_preferred": list(matched_pref),
#         })

#     # ── 4. Sort and return top-N ──────────────────────────────
#     results.sort(key=lambda x: x["score"], reverse=True)
#     return results[:top_n]


# # ============================================================
# # QUICK TEST
# # ============================================================
# if __name__ == "__main__":
#     mock_features = {
#         "cleaned_text": (
#             "python machine learning deep learning tensorflow pytorch pandas numpy "
#             "scikit-learn mongodb sql flask react javascript docker git "
#             "data science nlp computer vision web development backend api"
#         ),
#         "skill_domains": [
#             "languages", "web", "frameworks", "libraries",
#             "databases", "tools", "core_cs", "ai_ml", "data"
#         ],
#         "skills": {
#             "languages":   ["Python", "JavaScript"],
#             "web":         ["React", "Flask"],
#             "frameworks":  ["Django", "FastAPI"],
#             "libraries":   ["TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn"],
#             "databases":   ["MongoDB", "PostgreSQL"],
#             "tools":       ["Docker", "Git"],
#             "core_cs":     ["Algorithms", "Data Structures"],
#             "ai_ml":       ["Deep Learning", "NLP", "Computer Vision"],
#             "data":        ["Data Analysis", "Feature Engineering"],
#         },
#     }

#     print("Normalised domains:", _normalize_domains(mock_features["skill_domains"]))
#     print()

#     jobs = recommend_jobs(mock_features, top_n=5)

#     print("🎯 TOP JOB RECOMMENDATIONS")
#     print("=" * 60)
#     for idx, j in enumerate(jobs, 1):
#         print(f"\n#{idx}  {j['title']}")
#         print(f"    Match Score       : {j['score']}%")
#         print(f"    ✅ Your Skills    : {j['matched_skills']}")
#         print(f"    ⚠️  Critical Missing : {j['missing_skills']['critical']}")
#         print(f"    💡 Also Learn     : {j['missing_skills']['recommended']}")
#         print("-" * 60)




import math
import re
from collections import Counter
from typing import Dict, List


# ============================================================
# DOMAIN ALIAS MAP  —  parser domains  ──►  canonical domains
# ============================================================
DOMAIN_ALIAS_MAP: Dict[str, str] = {
    "languages":          "python",
    "python":             "python",
    "javascript":         "javascript",
    "java":               "java",
    "c_cpp":              "c_cpp",
    "kotlin":             "kotlin",
    "swift":              "swift",
    "scala":              "scala",
    "r_language":         "r_language",
    "shell":              "shell",
    "web":                "web_development",
    "web_development":    "web_development",
    "frameworks":         "web_development",
    "ai_ml":              "machine_learning",
    "machine_learning":   "machine_learning",
    "data_science":       "data_science",
    "data":               "data_science",
    "data_engineering":   "data_engineering",
    "ml_frameworks":      "ml_frameworks",
    "libraries":          "ml_frameworks",
    "databases":          "databases",
    "sql":                "sql",
    "devops":             "devops",
    "cloud":              "cloud",
    "tools":              "devops",
    "security":           "security",
    "embedded":           "embedded",
    "design":             "design",
    "finance":            "finance",
    "marketing":          "marketing",
    "project_management": "project_management",
    "healthcare":         "healthcare",
    "core_cs":            "web_development",
}


# ============================================================
# DOMAIN SKILL CATALOGUE  —  all learnable skills per domain
# ============================================================
DOMAIN_SKILL_CATALOGUE: Dict[str, List[str]] = {
    "python":             ["Python", "OOP", "Virtual Environments", "pip", "Poetry"],
    "javascript":         ["JavaScript", "TypeScript", "Node.js", "ES6+", "npm"],
    "java":               ["Java", "Spring Boot", "Maven", "JUnit", "Gradle"],
    "c_cpp":              ["C", "C++", "CMake", "GDB", "Valgrind"],
    "kotlin":             ["Kotlin", "Android SDK", "Jetpack Compose", "Gradle"],
    "swift":              ["Swift", "SwiftUI", "Xcode", "CocoaPods", "UIKit"],
    "scala":              ["Scala", "Akka", "sbt", "Functional Programming"],
    "r_language":         ["R", "ggplot2", "dplyr", "tidyr", "RMarkdown"],
    "shell":              ["Bash", "Zsh", "Shell Scripting", "AWK", "sed", "cron"],
    "web_development":    ["REST API", "HTML", "CSS", "HTTP/HTTPS", "GraphQL",
                           "WebSockets", "OAuth2", "JWT", "Swagger/OpenAPI"],
    "machine_learning":   ["Supervised Learning", "Unsupervised Learning",
                           "Reinforcement Learning", "Model Evaluation",
                           "Hyperparameter Tuning", "Cross-Validation",
                           "Gradient Boosting", "XGBoost", "Feature Selection"],
    "ml_frameworks":      ["TensorFlow", "PyTorch", "Scikit-learn", "Keras",
                           "Hugging Face", "ONNX", "MLflow", "Weights & Biases"],
    "data_science":       ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly",
                           "Statistics", "Hypothesis Testing", "A/B Testing",
                           "Data Wrangling", "EDA"],
    "data_engineering":   ["Apache Spark", "Apache Kafka", "Apache Airflow",
                           "dbt", "Snowflake", "BigQuery", "Redshift",
                           "ETL Pipelines", "Data Lake", "Data Warehouse"],
    "sql":                ["SQL", "PostgreSQL", "MySQL", "Query Optimization",
                           "Joins", "Window Functions", "Stored Procedures",
                           "Indexing", "Transactions"],
    "databases":          ["MongoDB", "Redis", "Cassandra", "Elasticsearch",
                           "Database Design", "ORM", "Connection Pooling"],
    "devops":             ["Docker", "Kubernetes", "CI/CD", "Jenkins",
                           "GitHub Actions", "Terraform", "Ansible",
                           "Helm", "ArgoCD", "Prometheus", "Grafana"],
    "cloud":              ["AWS", "Azure", "GCP", "S3", "EC2", "Lambda",
                           "Cloud IAM", "VPC", "Load Balancing", "Auto Scaling"],
    "security":           ["OWASP Top 10", "Penetration Testing", "SIEM", "Splunk",
                           "Nmap", "Wireshark", "Metasploit", "Burp Suite",
                           "Vulnerability Assessment", "Incident Response"],
    "embedded":           ["C/C++ for Embedded", "RTOS", "Microcontrollers",
                           "Arduino", "Raspberry Pi", "UART", "SPI", "I2C",
                           "FPGA", "PCB Design"],
    "design":             ["Figma", "Adobe XD", "Wireframing", "Prototyping",
                           "User Research", "Usability Testing", "Design Systems",
                           "Information Architecture", "Accessibility (WCAG)"],
    "finance":            ["Financial Modeling", "Excel", "Bloomberg Terminal",
                           "DCF Valuation", "Portfolio Management", "CFA",
                           "Risk Management", "Derivatives"],
    "marketing":          ["Google Analytics", "Google Ads", "SEO", "SEM",
                           "HubSpot", "Salesforce", "Email Campaigns",
                           "Social Media Marketing", "A/B Testing"],
    "project_management": ["Agile", "Scrum", "Kanban", "Jira", "Confluence",
                           "Stakeholder Management", "Risk Management",
                           "Sprint Planning", "PMP", "Roadmapping"],
    "healthcare":         ["HL7/FHIR", "HIPAA Compliance", "EHR Systems",
                           "Epic/Cerner", "Clinical Data Analysis",
                           "ICD Coding", "Bioinformatics"],
}


# ============================================================
# CRITICAL (MUST-HAVE) SKILLS PER JOB  —  recruiter checklist
# ============================================================
JOB_KEY_SKILLS: Dict[str, List[str]] = {
    "Backend Software Engineer":
        ["REST API", "Docker", "PostgreSQL", "Redis", "CI/CD", "Unit Testing"],
    "Frontend Developer":
        ["TypeScript", "React", "CSS", "Webpack/Vite", "Accessibility (WCAG)"],
    "Full Stack Developer":
        ["React", "Node.js", "PostgreSQL", "Docker", "CI/CD"],
    "Mobile App Developer (Android/iOS)":
        ["Kotlin", "Swift", "Firebase", "Jetpack Compose", "SwiftUI"],
    "DevOps / Cloud Engineer":
        ["Kubernetes", "Terraform", "AWS", "CI/CD", "Prometheus", "Grafana"],
    "Site Reliability Engineer (SRE)":
        ["Kubernetes", "Prometheus", "Grafana", "Incident Response", "SLO/SLA"],
    "Data Scientist":
        ["Scikit-learn", "Statistics", "A/B Testing", "Feature Engineering", "SQL", "EDA"],
    "Machine Learning Engineer":
        ["MLflow", "Kubernetes", "ONNX", "CI/CD", "GPU/CUDA", "Model Serving"],
    "Data Analyst":
        ["SQL", "Tableau/Power BI", "Statistics", "Excel", "A/B Testing"],
    "Data Engineer":
        ["Apache Spark", "Apache Airflow", "dbt", "Snowflake", "Apache Kafka"],
    "NLP Engineer":
        ["Hugging Face", "Transformers", "BERT/GPT", "spaCy", "LLM Fine-tuning", "NLTK"],
    "Computer Vision Engineer":
        ["OpenCV", "YOLO", "CNN Architectures", "ONNX", "GPU/CUDA"],
    "AI Research Scientist":
        ["Reinforcement Learning", "Diffusion Models", "LLM Pre-training",
         "Research Papers/LaTeX", "PhD-level Math"],
    "Cybersecurity Analyst":
        ["SIEM/Splunk", "OWASP Top 10", "Incident Response", "Firewalls", "Threat Hunting"],
    "Penetration Tester":
        ["Metasploit", "Burp Suite", "OSCP", "Nmap", "Exploit Development"],
    "UI/UX Designer":
        ["Figma", "User Research", "Prototyping", "Design Systems", "Accessibility (WCAG)"],
    "Embedded Systems Engineer":
        ["RTOS", "UART/SPI/I2C", "FPGA", "PCB Design", "ARM Cortex"],
    "Financial Analyst":
        ["Financial Modeling", "DCF Valuation", "Bloomberg Terminal", "CFA", "Excel"],
    "Quantitative Analyst (Quant)":
        ["Stochastic Calculus", "Derivatives Pricing", "Time Series", "Backtesting", "R"],
    "Digital Marketing Analyst":
        ["Google Analytics", "Google Ads", "SEO", "HubSpot", "A/B Testing"],
    "Technical Project Manager":
        ["Jira", "Agile/Scrum", "Stakeholder Management", "Risk Management", "PMP"],
    "Product Manager":
        ["Roadmapping", "User Stories", "A/B Testing", "KPI Metrics", "Go-to-Market Strategy"],
    "Health Informatics / Clinical Data Analyst":
        ["HL7/FHIR", "HIPAA Compliance", "Epic/Cerner", "SQL", "Clinical Trials"],
    "Software Quality Assurance (QA) Engineer":
        ["Selenium", "pytest", "API Testing", "CI/CD", "Test Automation", "Postman"],
    "Database Administrator (DBA)":
        ["Query Optimization", "Replication", "High Availability",
         "Backup & Recovery", "Oracle/MSSQL"],
}


# ============================================================
# JOB PROFILES
# ============================================================
JOB_PROFILES: List[Dict] = [
    {
        "title": "Backend Software Engineer",
        "required_domains": ["python", "web_development"],
        "preferred_domains": ["devops", "cloud", "databases", "sql"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "python django flask fastapi rest api microservices sql postgresql "
            "mysql database design backend server side development git linux "
            "docker api integration unit testing"
        ),
    },
    {
        "title": "Frontend Developer",
        "required_domains": ["javascript", "web_development"],
        "preferred_domains": ["design"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "javascript react angular vue html css typescript frontend ui "
            "responsive design browser api state management redux rest api "
            "webpack vite performance optimization accessibility"
        ),
    },
    {
        "title": "Full Stack Developer",
        "required_domains": ["javascript", "web_development"],
        "preferred_domains": ["python", "sql", "devops"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "full stack javascript react nodejs express python django rest api "
            "html css sql mongodb postgresql git docker deployment "
            "frontend backend integration ci cd agile"
        ),
    },
    {
        "title": "Mobile App Developer (Android/iOS)",
        "required_domains": ["kotlin", "swift"],
        "preferred_domains": ["java", "javascript"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "android kotlin java ios swift swiftui mobile development "
            "flutter react native app store play store api integration "
            "firebase mobile ui push notifications"
        ),
    },
    {
        "title": "DevOps / Cloud Engineer",
        "required_domains": ["devops", "cloud"],
        "preferred_domains": ["python", "shell"],
        "min_experience": 1, "min_education": "bachelors",
        "description": (
            "devops aws azure gcp docker kubernetes helm ci cd jenkins "
            "github actions terraform ansible infrastructure as code "
            "linux bash scripting monitoring prometheus grafana site reliability"
        ),
    },
    {
        "title": "Site Reliability Engineer (SRE)",
        "required_domains": ["devops", "cloud", "shell"],
        "preferred_domains": ["python", "databases"],
        "min_experience": 2, "min_education": "bachelors",
        "description": (
            "sre site reliability engineering kubernetes docker monitoring "
            "alerting on call incident management linux bash python automation "
            "availability scalability latency performance distributed systems"
        ),
    },
    {
        "title": "Data Scientist",
        "required_domains": ["data_science", "machine_learning"],
        "preferred_domains": ["python", "sql", "ml_frameworks"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "data science machine learning statistics python pandas numpy "
            "scikit-learn model building evaluation feature engineering "
            "exploratory data analysis visualization matplotlib seaborn "
            "hypothesis testing regression classification clustering"
        ),
    },
    {
        "title": "Machine Learning Engineer",
        "required_domains": ["machine_learning", "ml_frameworks"],
        "preferred_domains": ["python", "data_engineering", "cloud"],
        "min_experience": 1, "min_education": "bachelors",
        "description": (
            "machine learning engineer mlops tensorflow pytorch deep learning "
            "model deployment model serving api production pipeline feature store "
            "training infrastructure gpu cuda distributed training"
        ),
    },
    {
        "title": "Data Analyst",
        "required_domains": ["data_science", "sql"],
        "preferred_domains": ["python", "r_language"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "data analyst sql excel power bi tableau data visualization "
            "business intelligence reporting dashboards kpi metrics "
            "data cleaning data wrangling python pandas statistics"
        ),
    },
    {
        "title": "Data Engineer",
        "required_domains": ["data_engineering", "sql"],
        "preferred_domains": ["python", "cloud", "scala"],
        "min_experience": 1, "min_education": "bachelors",
        "description": (
            "data engineer etl pipeline apache spark kafka airflow hadoop "
            "sql python scala data warehouse data lake snowflake bigquery "
            "redshift dbt streaming batch processing"
        ),
    },
    {
        "title": "NLP Engineer",
        "required_domains": ["machine_learning", "ml_frameworks"],
        "preferred_domains": ["python", "data_science"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "nlp natural language processing text mining bert gpt transformers "
            "hugging face spacy nltk gensim text classification ner "
            "sentiment analysis information extraction llm fine tuning"
        ),
    },
    {
        "title": "Computer Vision Engineer",
        "required_domains": ["machine_learning", "ml_frameworks"],
        "preferred_domains": ["python", "embedded"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "computer vision opencv pytorch tensorflow image processing "
            "object detection segmentation cnn feature extraction yolo "
            "video analytics image classification deep learning"
        ),
    },
    {
        "title": "AI Research Scientist",
        "required_domains": ["machine_learning", "ml_frameworks", "data_science"],
        "preferred_domains": ["python", "r_language"],
        "min_experience": 2, "min_education": "masters",
        "description": (
            "research scientist deep learning reinforcement learning generative models "
            "gans diffusion models llm pretraining finetuning arxiv publications "
            "pytorch tensorflow statistical learning theory phd"
        ),
    },
    {
        "title": "Cybersecurity Analyst",
        "required_domains": ["security"],
        "preferred_domains": ["devops", "shell"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "cybersecurity soc analyst siem splunk threat detection incident response "
            "vulnerability scanning penetration testing network security "
            "firewall ids ips owasp ethical hacking"
        ),
    },
    {
        "title": "Penetration Tester",
        "required_domains": ["security", "shell"],
        "preferred_domains": ["c_cpp", "python"],
        "min_experience": 1, "min_education": "bachelors",
        "description": (
            "penetration testing ethical hacking red team metasploit burp suite "
            "nmap wireshark exploit development vulnerability assessment "
            "ceh oscp ctf linux bash python web application security"
        ),
    },
    {
        "title": "UI/UX Designer",
        "required_domains": ["design"],
        "preferred_domains": ["javascript", "web_development"],
        "min_experience": None, "min_education": None,
        "description": (
            "ui ux design figma sketch adobe xd wireframing prototyping "
            "user research usability testing design system component library "
            "interaction design information architecture accessibility"
        ),
    },
    {
        "title": "Embedded Systems Engineer",
        "required_domains": ["embedded"],
        "preferred_domains": ["c_cpp", "shell"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "embedded systems firmware c c++ rtos microcontroller arduino "
            "raspberry pi iot fpga verilog vhdl pcb circuit design "
            "uart spi i2c real time operating system"
        ),
    },
    {
        "title": "Financial Analyst",
        "required_domains": ["finance"],
        "preferred_domains": ["data_science", "sql"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "financial analyst excel financial modeling valuation dcf lbo "
            "bloomberg equity research portfolio management investment banking "
            "accounting cfa chartered financial analyst reporting"
        ),
    },
    {
        "title": "Quantitative Analyst (Quant)",
        "required_domains": ["finance", "machine_learning"],
        "preferred_domains": ["python", "r_language", "data_science"],
        "min_experience": None, "min_education": "masters",
        "description": (
            "quantitative analyst quant python r stochastic calculus "
            "derivatives pricing risk management algorithmic trading "
            "statistics time series mathematical finance"
        ),
    },
    {
        "title": "Digital Marketing Analyst",
        "required_domains": ["marketing"],
        "preferred_domains": ["data_science", "sql"],
        "min_experience": None, "min_education": None,
        "description": (
            "digital marketing seo sem google analytics google ads "
            "facebook ads social media marketing content strategy "
            "email campaigns crm hubspot salesforce marketing analytics"
        ),
    },
    {
        "title": "Technical Project Manager",
        "required_domains": ["project_management"],
        "preferred_domains": ["devops", "web_development"],
        "min_experience": 2, "min_education": None,
        "description": (
            "project manager agile scrum kanban jira confluence "
            "stakeholder management sprint planning roadmap delivery "
            "risk management technical team budget tracking pmp"
        ),
    },
    {
        "title": "Product Manager",
        "required_domains": ["project_management"],
        "preferred_domains": ["data_science", "marketing"],
        "min_experience": 2, "min_education": "bachelors",
        "description": (
            "product manager product roadmap user stories backlog "
            "agile scrum stakeholder alignment go to market strategy "
            "kpi metrics product analytics a/b testing customer research"
        ),
    },
    {
        "title": "Health Informatics / Clinical Data Analyst",
        "required_domains": ["healthcare"],
        "preferred_domains": ["data_science", "sql"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "health informatics ehr fhir hl7 hipaa clinical data "
            "medical records patient data sql python healthcare analytics "
            "epic cerner clinical trials bioinformatics"
        ),
    },
    {
        "title": "Software Quality Assurance (QA) Engineer",
        "required_domains": ["web_development"],
        "preferred_domains": ["python", "javascript", "devops"],
        "min_experience": None, "min_education": "bachelors",
        "description": (
            "qa engineer software testing manual testing automated testing "
            "selenium pytest junit test cases regression testing "
            "api testing postman jira bug tracking agile"
        ),
    },
    {
        "title": "Database Administrator (DBA)",
        "required_domains": ["sql", "databases"],
        "preferred_domains": ["shell", "devops"],
        "min_experience": 1, "min_education": "bachelors",
        "description": (
            "database administrator dba postgresql mysql oracle mssql "
            "performance tuning query optimization backup recovery "
            "replication high availability indexing stored procedures"
        ),
    },
]


# ============================================================
# TF-IDF HELPERS
# ============================================================

def _tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

def _tf(tokens):
    counts = Counter(tokens)
    total = len(tokens) or 1
    return {t: c / total for t, c in counts.items()}

def _idf(corpus):
    N = len(corpus)
    df = {}
    for doc in corpus:
        for term in set(doc):
            df[term] = df.get(term, 0) + 1
    return {t: math.log((N + 1) / (d + 1)) + 1 for t, d in df.items()}

def _tfidf(tokens, idf):
    tf = _tf(tokens)
    return {t: tf[t] * idf.get(t, 1.0) for t in tf}

def _cosine(v1, v2):
    common = set(v1) & set(v2)
    if not common:
        return 0.0
    dot = sum(v1[t] * v2[t] for t in common)
    mag1 = math.sqrt(sum(x * x for x in v1.values()))
    mag2 = math.sqrt(sum(x * x for x in v2.values()))
    return 0.0 if (mag1 == 0 or mag2 == 0) else dot / (mag1 * mag2)


# ============================================================
# DOMAIN NORMALISATION
# ============================================================

def _normalize_domains(raw_domains: List[str]) -> List[str]:
    canonical = set()
    for d in raw_domains:
        mapped = DOMAIN_ALIAS_MAP.get(d.lower())
        canonical.add(mapped if mapped else d.lower())
    return list(canonical)


# ============================================================
# MISSING SKILLS DETECTION
# ============================================================

def _get_missing_skills(
    job: Dict,
    candidate_domains: List[str],
    candidate_skills_flat: List[str],
) -> Dict[str, List[str]]:
    """
    Returns two lists:
      critical    – must-have skills from JOB_KEY_SKILLS not found on resume
      recommended – catalogue skills from job domains the candidate doesn't cover
    """
    resume_lower = {s.lower() for s in candidate_skills_flat}

    def _absent(skill: str) -> bool:
        return skill.lower() not in resume_lower

    # Critical: key skills for this job that are missing
    critical = [s for s in JOB_KEY_SKILLS.get(job["title"], []) if _absent(s)]

    # Recommended: skills from uncovered domains (required + preferred)
    all_job_domains  = set(job["required_domains"]) | set(job.get("preferred_domains", []))
    missing_domains  = all_job_domains - set(candidate_domains)
    recommended = []
    for domain in sorted(missing_domains):
        for skill in DOMAIN_SKILL_CATALOGUE.get(domain, []):
            if _absent(skill) and skill not in critical:
                recommended.append(skill)

    return {
        "critical":    critical[:8],
        "recommended": recommended[:8],
    }


# ============================================================
# MAIN FUNCTION
# ============================================================

def recommend_jobs(features: Dict, top_n: int = 5) -> List[Dict]:
    """
    features must contain:
      - cleaned_text  : full resume text string
      - skill_domains : list of domain strings from your parser
      - skills        : dict  domain -> list[str]  of skill names
    """
    text        = features["cleaned_text"]
    raw_domains = features["skill_domains"]
    skills      = features["skills"]

    # 1. Normalise domains
    domains = _normalize_domains(raw_domains)

    # 2. Normalise skills dict keys  +  build flat candidate skill list
    norm_skills: Dict[str, List[str]] = {}
    for raw_d, skill_list in skills.items():
        canon = DOMAIN_ALIAS_MAP.get(raw_d.lower(), raw_d.lower())
        norm_skills.setdefault(canon, []).extend(skill_list)

    all_candidate_skills: List[str] = [s for lst in norm_skills.values() for s in lst]

    # 3. TF-IDF
    resume_tokens = _tokenize(text)
    job_tokens    = [_tokenize(j["description"]) for j in JOB_PROFILES]
    idf           = _idf([resume_tokens] + job_tokens)
    resume_vec    = _tfidf(resume_tokens, idf)
    job_vecs      = [_tfidf(t, idf) for t in job_tokens]

    # 4. Score
    results = []
    for i, job in enumerate(JOB_PROFILES):
        req  = set(job["required_domains"])
        pref = set(job.get("preferred_domains", []))

        matched_req  = req  & set(domains)
        matched_pref = pref & set(domains)

        if not matched_req:          # hard filter
            continue

        req_cov    = len(matched_req)  / len(req)
        pref_cov   = len(matched_pref) / max(len(pref), 1)
        dom_score  = (4 * req_cov + pref_cov) / 5
        tfidf_score = _cosine(resume_vec, job_vecs[i])
        score       = round((0.75 * dom_score + 0.25 * tfidf_score) * 100, 1)

        matched_skills = list({
            s for d in (matched_req | matched_pref)
            for s in norm_skills.get(d, [])
        })[:10]

        missing = _get_missing_skills(job, domains, all_candidate_skills)

        results.append({
            "title":          job["title"],
            "score":          score,
            "matched_skills": matched_skills,
            "missing_skills": missing,         # ← always present now
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_n]


# ============================================================
# DISPLAY HELPER  —  call this wherever you print results
# ============================================================

def display_recommendations(jobs: List[Dict]) -> None:
    """
    Prints job recommendations in the same format your app already uses,
    with Missing Skills added right below Matched Skills.
    """
    print("\n🎯 TOP JOBS:\n")
    for job in jobs:
        print("-------------------")
        print(f"Role:              {job['title']}")
        print(f"Score:             {job['score']}")
        print(f"Matched Skills:    {job['matched_skills']}")

        missing = job.get("missing_skills", {})
        critical    = missing.get("critical", [])
        recommended = missing.get("recommended", [])

        if critical:
            print(f"⚠️  Critical Missing: {critical}")
        else:
            print("⚠️  Critical Missing: None — great coverage!")

        if recommended:
            print(f"💡 Also Learn:       {recommended}")
        else:
            print("💡 Also Learn:       None")

        print()


# ============================================================
# QUICK TEST
# ============================================================
# if __name__ == "__main__":
#     mock_features = {
#         "cleaned_text": (
#             "python machine learning deep learning tensorflow pytorch pandas numpy "
#             "scikit-learn mongodb sql flask react javascript docker git nltk "
#             "data science nlp computer vision web development backend api machine learning"
#         ),
#         "skill_domains": [
#             "languages", "web", "frameworks", "libraries",
#             "databases", "tools", "core_cs", "ai_ml", "data"
#         ],
#         "skills": {
#             "languages":  ["Python", "JavaScript", "Java", "Go", "Excel"],
#             "web":        ["React", "Flask"],
#             "frameworks": ["Django", "FastAPI"],
#             "libraries":  ["TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn"],
#             "databases":  ["MongoDB", "PostgreSQL"],
#             "tools":      ["Docker", "Git"],
#             "core_cs":    ["Algorithms", "Data Structures"],
#             "ai_ml":      ["Deep Learning", "NLP", "Computer Vision", "Machine Learning"],
#             "data":       ["Data Analysis", "Feature Engineering"],
#         },
#     }

#     jobs = recommend_jobs(mock_features, top_n=5)
#     display_recommendations(jobs)