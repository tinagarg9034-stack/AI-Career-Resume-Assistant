def generate_advice(target_role, matched_skills, missing_skills):
    advice = []

    advice.append(
        f"Your target role is {target_role}."
    )

    if matched_skills:
        advice.append(
            "You already have experience with: "
            + ", ".join(matched_skills)
            + "."
        )

    if missing_skills:
        advice.append(
            "You should focus on learning: "
            + ", ".join(missing_skills)
            + "."
        )

        advice.append(
            "Start with the high-priority missing skills "
            "and build small projects to practice them."
        )

    else:
        advice.append(
            "Your detected skills cover the major requirements "
            "for this role. Focus on projects and interview preparation."
        )

    return advice