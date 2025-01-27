export function showAnswer(element, content) {
  element.textContent = content;
  element.parentElement.classList.remove("hidden");
}

export function hideAnswer(element) {
  element.textContent = "";
  element.parentElement.classList.add("hidden");
}
