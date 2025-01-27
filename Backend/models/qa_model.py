import json
from sentence_transformers import SentenceTransformer, util

class QAModel:
    def __init__(self, dataset_path, model_name="paraphrase-multilingual-MiniLM-L12-v2"):
        # Load the QA dataset
        with open(dataset_path, "r", encoding="utf-8") as f:
            qa_data = json.load(f)

        self.questions = [item["question"] for item in qa_data]
        self.answers = [item["answer"] for item in qa_data]

        # Load the SentenceTransformer model
        self.model = SentenceTransformer(model_name)

        # Encode all questions
        self.question_embeddings = self.model.encode(self.questions, convert_to_tensor=True)

    def get_combined_answers(self, input_question, threshold=0.8):
        # Encode the input question
        input_embedding = self.model.encode(input_question, convert_to_tensor=True)

        # Compute cosine similarities with all questions
        similarities = util.cos_sim(input_embedding, self.question_embeddings)[0]  # [0] for 1D tensor

        # Find indices of questions above the threshold
        similar_indices = (similarities > threshold).nonzero(as_tuple=True)[0]

        # Combine answers from all similar questions
        combined_answers = [self.answers[idx] for idx in similar_indices]

        return " | ".join(combined_answers) if combined_answers else "No relevant answers found."
