import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text.lower()


def extract_skills(text):
    skills_list = [
        "python",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "ai",
        "nlp",
        "data science",
        "flask",
        "sql"
    ]

    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
