import { fetchAnswer } from "./api.js";
import { showAnswer, hideAnswer } from "./utils.js";

document.getElementById("ask-button").addEventListener("click", async () => {
  const question = document.getElementById("question").value;
  const answerElement = document.getElementById("answer");
  const answerContainer = document.getElementById("answer-container");

  hideAnswer(answerElement);

  if (!question.trim()) {
    showAnswer(answerElement, "Παρακαλώ εισάγετε μια ερώτηση.");
    return;
  }

  showAnswer(answerElement, "Παρακαλώ περιμένετε...");

  try {
    const data = await fetchAnswer(question);
    showAnswer(answerElement, data.answer || "Δεν υπάρχει απάντηση.");
  } catch (error) {
    showAnswer(answerElement, "Παρουσιάστηκε σφάλμα. Παρακαλώ προσπαθήστε ξανά.");
    console.error(error);
  }
});
