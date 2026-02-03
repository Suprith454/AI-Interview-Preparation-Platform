from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf, extract_skills
from utils.ats_scoring import ats_score
from utils.interview_ai import evaluate_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume = request.files["resume"]

        text = extract_text_from_pdf(resume)
        skills = extract_skills(text)
        score = ats_score(skills)

        return render_template(
            "result.html",
            skills=skills,
            score=score
        )

    return render_template("index.html")


@app.route("/interview", methods=["POST"])
def interview():
    user_answer = request.form["answer"]

    correct_answer = (
        "Machine learning is a subset of artificial intelligence "
        "that enables systems to learn from data and improve "
        "performance without explicit programming."
    )

    score = evaluate_answer(user_answer, correct_answer)

    return f"Interview Answer Score: {score}%"


if __name__ == "__main__":
    app.run(debug=True)
