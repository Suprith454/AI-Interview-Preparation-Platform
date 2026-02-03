from sentence_transformers import SentenceTransformer, util

# Load model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_answer(user_answer, correct_answer):
    user_embedding = model.encode(user_answer, convert_to_tensor=True)
    correct_embedding = model.encode(correct_answer, convert_to_tensor=True)

    similarity = util.cos_sim(user_embedding, correct_embedding)
    score = float(similarity[0][0]) * 100

    return round(score, 2)
