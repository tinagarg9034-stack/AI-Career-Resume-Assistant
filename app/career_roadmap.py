SKILL_DETAILS = {

    "Python": {
        "priority": "High",
        "topics": [
            "Python basics",
            "Functions",
            "Lists and dictionaries",
            "File handling",
            "Object-oriented programming"
        ],
        "project": "Build a Python data analysis mini project"
    },

    "SQL": {
        "priority": "High",
        "topics": [
            "SELECT queries",
            "WHERE and ORDER BY",
            "GROUP BY",
            "JOINs",
            "Subqueries"
        ],
        "project": "Analyze a student or sales database using SQL"
    },

    "Statistics": {
        "priority": "High",
        "topics": [
            "Mean, median and mode",
            "Probability",
            "Distributions",
            "Correlation",
            "Hypothesis testing"
        ],
        "project": "Perform statistical analysis on a dataset"
    },

    "Data Visualization": {
        "priority": "Medium",
        "topics": [
            "Matplotlib",
            "Seaborn",
            "Bar charts",
            "Scatter plots",
            "Dashboards"
        ],
        "project": "Create a data visualization dashboard"
    },

    "Machine Learning": {
        "priority": "High",
        "topics": [
            "Supervised learning",
            "Regression",
            "Classification",
            "Model evaluation",
            "Feature engineering"
        ],
        "project": "Build a machine learning prediction model"
    },

    "Deep Learning": {
        "priority": "Medium",
        "topics": [
            "Neural networks",
            "Activation functions",
            "CNN",
            "Training and validation",
            "Model evaluation"
        ],
        "project": "Build an image classification project"
    },

    "Pandas": {
        "priority": "High",
        "topics": [
            "DataFrames",
            "Data cleaning",
            "Filtering",
            "Grouping",
            "Data analysis"
        ],
        "project": "Clean and analyze a real-world dataset"
    },

    "NumPy": {
        "priority": "Medium",
        "topics": [
            "Arrays",
            "Array operations",
            "Indexing",
            "Statistics",
            "Matrix operations"
        ],
        "project": "Perform numerical analysis using NumPy"
    }
}


def generate_roadmap(missing_skills):

    roadmap = []

    for index, skill in enumerate(missing_skills):

        details = SKILL_DETAILS.get(
            skill,
            {
                "priority": "Medium",
                "topics": [
                    f"Learn {skill} fundamentals",
                    f"Practice {skill}",
                    f"Build a small project using {skill}"
                ],
                "project": f"Build a mini project using {skill}"
            }
        )

        roadmap.append({
            "week": index + 1,
            "skill": skill,
            "priority": details["priority"],
            "topics": details["topics"],
            "project": details["project"]
        })

    return roadmap