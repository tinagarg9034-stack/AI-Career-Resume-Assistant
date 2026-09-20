def calculate_match(user_skills, required_skills):

    user_skills_lower = {
        skill.lower()
        for skill in user_skills
    }

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in user_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) > 0:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0

    return (
        matched_skills,
        missing_skills,
        round(match_percentage, 2)
    )