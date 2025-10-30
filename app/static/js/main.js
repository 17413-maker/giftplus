const form = document.getElementById("ai-test-form");
const responseArea = document.getElementById("ai_response");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    const response = await fetch("/test-ai", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    responseArea.textContent = JSON.stringify(data, null, 2);
});




















// JS placeholder
