from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from sentence_transformers import SentenceTransformer, util

# Initialize Flask app and enable CORS
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
def get_answer(input_question):
    input_embedding = model.encode(input_question, convert_to_tensor=True)
    similarities = util.cos_sim(input_embedding, question_embeddings)
    best_match_idx = similarities.argmax().item()
    return answers[best_match_idx]

# API Endpoint to get an answer
@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    input_question = data.get("question", "")

    if not input_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Get the answer using the ML model
        response = get_answer(input_question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
