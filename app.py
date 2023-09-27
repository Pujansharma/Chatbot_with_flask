from flask import Flask, render_template, request, jsonify
import openai
from decouple import config
app = Flask(__name__)

# Configure your OpenAI API key
openai.api_key = config("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form.get("user_input")
    
    # Initialize a conversation with a system message
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]

    # Continue the conversation with the user's message
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=50  # Adjust as needed
    )

    # Extract the chatbot's response
    chatbot_response = response.choices[0].message["content"]

    return jsonify({"chatbot_response": chatbot_response})

if __name__ == "__main__":
    app.run(debug=True)
