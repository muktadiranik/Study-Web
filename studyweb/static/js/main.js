var messages = document.getElementById("messages");

window.onload = () => {
  setTimeout(() => {
    messages.classList.add("hidden-messages");
  }, 1000);
};
