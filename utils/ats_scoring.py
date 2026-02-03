def ats_score(skills_found):
    total_skills = 8
    score = (len(skills_found) / total_skills) * 100
    return round(score, 2)
