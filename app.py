from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

DEMO_RESPONSES = {
    "translate": "Translation mode: Enter your Kiswahili or English text and SemaAI will help translate it.",
    "message": "Message mode: Tell SemaAI who the message is for and what you want to say.",
    "letter": "Letter mode: Tell SemaAI the recipient, purpose, and key points for your letter.",
    "explain": "Explain mode: Enter a word, concept, or topic and SemaAI will explain it simply.",
    "swahili": "Kiswahili improvement mode: Enter your sentence and SemaAI will suggest clearer, more natural Kiswahili."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    mode = data.get("mode", "chat")

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    # MVP demo response. Replace this function with your chosen AI API later.
    if mode in DEMO_RESPONSES:
        response = f"{DEMO_RESPONSES[mode]}\n\nYour request: {message}"
    else:
        response = (
            "Karibu SemaAI! Hii ni MVP ya majaribio. "
            "Ujumbe wako umepokelewa:\n\n" + message +
            "\n\nHatua inayofuata ni kuunganisha AI model halisi ili SemaAI itoe majibu ya akili."
        )

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
