from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answer(user_answer, correct_answer):
    emb1 = model.encode(user_answer, convert_to_tensor=True)
    emb2 = model.encode(correct_answer, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2)
    score = float(similarity[0][0]) * 100

    return round(score, 2)
