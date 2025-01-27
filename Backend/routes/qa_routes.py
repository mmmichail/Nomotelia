from flask import Blueprint, request, jsonify
from models.qa_model import QAModel

# Initialize blueprint
qa_blueprint = Blueprint("qa", __name__)

# Initialize QAModel instance
qa_model = QAModel("qa_pairs_greek.json")

@qa_blueprint.route("/answer", methods=["POST"])
def answer():
    data = request.json
    input_question = data.get("question", "")

    if not input_question:
        return jsonify({"error": "No question provided"}), 400

    try:
        response = qa_model.get_combined_answers(input_question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
