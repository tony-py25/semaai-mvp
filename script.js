function showDemoResponse() {
  const prompt = document.getElementById("prompt").value.trim();
  const responseText = document.getElementById("responseText");

  if (prompt === "") {
    responseText.textContent = "Tafadhali andika ombi lako kwanza.";
    return;
  }

  responseText.textContent =
    "Asante! SemaAI imepokea ombi lako: " + prompt;
}
