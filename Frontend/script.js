document.getElementById("ask-button").addEventListener("click", async () => {
  const question = document.getElementById("question").value;
  const answerElement = document.getElementById("answer");
  const answerContainer = document.getElementById("answer-container");

  // Reset visibility and answer content
  answerContainer.classList.add("hidden");
  answerElement.textContent = "";

  if (!question.trim()) {
    answerElement.textContent = "Please enter a question.";
    answerContainer.classList.remove("hidden");
    return;
  }

  // Simulate loading state
  answerElement.textContent = "Thinking...";
  answerContainer.classList.remove("hidden");

  try {
    const response = await fetch("http://127.0.0.1:5000/answer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: question }),
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data = await response.json();
    answerElement.textContent = data.answer || "No answer available.";
  } catch (error) {
    answerElement.textContent = "An error occurred. Please try again.";
    console.error(error);
  }
});
