import PyPDF2
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def extract_skills(text):
    skills = [
        "python", "machine learning", "deep learning", "ai",
        "nlp", "flask", "sql", "data science"
    ]
    found_skills = [skill for skill in skills if skill in text]
    return found_skills
