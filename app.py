from flask import Flask ,request,jsonify,render_template
import random
import nltk
nltk.download('punkt_tab')
app=Flask(__name__)

responses={
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "admission": ["Our admission fee is $500.", "Admissions are open till June 30."],
}

def bot_ans(user_input):
    tokens=nltk.word_tokenize(user_input.lower())
    for key in responses:
        if key in tokens:
            return random.choice(responses[key])
    return "I'm not sure, but I can find out for you!"

@app.route("/chat",methods=['POST'])
def chat():
    user_message = request.json.get("message", "")  # Get user input safely
    if not user_message:  # If empty, return an error response
        return jsonify({"error": "User input is missing!"}), 400

    bot_reply = bot_ans(user_message)  # ✅ Pass input to function
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(port=5000,debug=True)