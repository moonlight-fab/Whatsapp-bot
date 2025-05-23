from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")

@app.route("/")
def home():
    return "Welcome to the WhatsApp Bot Server! 🚀"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    response = MessagingResponse()
    msg = response.message()

    if not incoming_msg:
        msg.body("I didn't receive a message. Please try again.")
        return str(response)

    try:
        chat_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": incoming_msg}]
        )
        reply_text = chat_response.choices[0].message.content
        msg.body(reply_text)
    except Exception as e:
        msg.body("Sorry, something went wrong.")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
