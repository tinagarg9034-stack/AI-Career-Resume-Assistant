from flask import Flask, render_template, request
import os

from pdf_parser import extract_text_from_pdf

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

        return f"""
        <h1>Resume Uploaded Successfully!</h1>

        <h2>Extracted Resume Text:</h2>

        <pre>{extracted_text}</pre>

        <br>

        <a href="/">Back to Home</a>
        """

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)