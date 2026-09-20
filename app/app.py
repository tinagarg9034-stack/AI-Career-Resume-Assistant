from flask import Flask, render_template, request
import os
import sys

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
from data.job_roles import JOB_ROLES

from pdf_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from career_matcher import calculate_match
from career_roadmap import generate_roadmap
from career_advisor import generate_advice

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

UPLOAD_FOLDER = "../uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload_resume():

    if request.method == "POST":

        if "resume" not in request.files:
            return "No resume selected."

        file = request.files["resume"]
        job_role = request.form.get("job_role")

        if file.filename == "":
            return "No resume selected."

        if not file.filename.lower().endswith(".pdf"):
            return "Please upload a PDF file."

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(file_path)

        extracted_text = extract_text_from_pdf(file_path)

        detected_skills=extract_skills(extracted_text)
        required_skills = JOB_ROLES.get(job_role, [])

        matched_skills, missing_skills, match_percentage = calculate_match(
            detected_skills,
            required_skills
        )
        advice=generate_advice(
                job_role,
                matched_skills,
                missing_skills
            )
        

        roadmap=generate_roadmap(missing_skills)

        matched_html = ""

        for skill in matched_skills:
            matched_html += f"<li>✓ {skill}</li>"


        missing_html = ""

        for skill in missing_skills:
            missing_html += f"<li>✗ {skill}</li>"


        return render_template(
        "result.html",
        job_role=job_role,
        match_percentage=match_percentage,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        roadmap=roadmap,
        advice=advice
    )

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)