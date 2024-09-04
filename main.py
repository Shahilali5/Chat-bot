
# index.py
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the bot with your tokens from environment variables
bot_token = os.getenv("TELEGRAM_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
bot = TgBot(bot_token, openai_api_key)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Extract chat ID and message text
    chat_id = data['message']['chat']['id']
    message_text = data['message']['text']

    # Process the message with your bot
    response_text = f"You said: {message_text}"
    bot.send_message(chat_id, response_text)

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
  
