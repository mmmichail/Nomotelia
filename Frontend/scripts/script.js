import { fetchAnswer } from "./api.js";
import { showAnswer, hideAnswer } from "./utils.js";

document.getElementById("ask-button").addEventListener("click", async () => {
  const question = document.getElementById("question").value;
  const answerElement = document.getElementById("answer");
  const answerContainer = document.getElementById("answer-container");

  hideAnswer(answerElement);

  if (!question.trim()) {
    showAnswer(answerElement, "Please enter a question.");
    return;
  }

  showAnswer(answerElement, "Thinking...");

  try {
    const data = await fetchAnswer(question);
    showAnswer(answerElement, data.answer || "No answer available.");
  } catch (error) {
    showAnswer(answerElement, "An error occurred. Please try again.");
    console.error(error);
  }
});
