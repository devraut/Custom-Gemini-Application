document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("send-button");
    const userInput = document.getElementById("user-input");
    const chatbox = document.getElementById("chat-box");

    function appendMessage(content, type = "ai-message") {
        const div = document.createElement("div");
        div.className = type;
        div.innerHTML = `<p>${content}</p>`;
        chatbox.appendChild(div);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        // Append user message
        appendMessage(message, "user-message");
        userInput.value = "";

        // Typing indicator
        const typingDiv = document.createElement("div");
        typingDiv.className = "typing";
        typingDiv.innerText = "AI is typing...";
        chatbox.appendChild(typingDiv);
        chatbox.scrollTop = chatbox.scrollHeight;

        // Send to backend
        fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        })
            .then((response) => response.json())
            .then((data) => {
                typingDiv.remove();
                if (data.response) {
                    appendMessage(data.response, "ai-message");
                } else {
                    appendMessage(data.error || "Unknown error", "error-message");
                }
            })
            .catch((error) => {
                typingDiv.remove();
                console.error("Error:", error);
                appendMessage("Server error. Please try again.", "error-message");
            });
    }

    // Event listeners
    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});
