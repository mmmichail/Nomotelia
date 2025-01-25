from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
CORS(app)

# Load the QA Dataset
with open("qa_pairs_greek.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

questions = [item["question"] for item in qa_data]
answers = [item["answer"] for item in qa_data]

# Load the SentenceTransformer model
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Encode all questions
question_embeddings = model.encode(questions, convert_to_tensor=True)

# Function to find the best match and get the answer
def get_combined_answers(input_question, threshold=0.8):
    # Encode the input question
    input_embedding = model.encode(input_question, convert_to_tensor=True)

    # Compute cosine similarities with all questions
    similarities = util.cos_sim(input_embedding, question_embeddings)[0]  # [0] for 1D tensor

    # Find indices of questions above the threshold
    similar_indices = (similarities > threshold).nonzero(as_tuple=True)[0]

    # Combine answers from all similar questions
    combined_answers = [answers[idx] for idx in similar_indices]

    # Return the combined answers
    return " | ".join(combined_answers) if combined_answers else "No relevant answers found."

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    input_question = data.get("question", "")

    if not input_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        response = get_combined_answers(input_question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
