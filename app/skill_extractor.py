SKILLS = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "TypeScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Express",
    "MongoDB",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Git",
    "GitHub",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "NLP",
    "Data Science",
    "Data Analysis",
    "Power BI",
    "Tableau",
    "Flask",
    "FastAPI",
    "Docker",
    "AWS"
]


def extract_skills(text):

    detected_skills = []

    text_lower = text.lower()

    for skill in SKILLS:

        if skill.lower() in text_lower:
            detected_skills.append(skill)

    return detected_skills