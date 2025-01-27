import { API_BASE_URL } from "./constants.js";

// Function to fetch the answer from the API
export async function fetchAnswer(question) {
  const response = await fetch(`${API_BASE_URL}/answer`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }

  return response.json();
}
