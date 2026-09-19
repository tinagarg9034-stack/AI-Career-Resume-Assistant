from flask import Flask, render_template, request
import os

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

        return f"Resume uploaded successfully: {file.filename}"

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)