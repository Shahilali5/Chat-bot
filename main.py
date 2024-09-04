import os
import json
import traceback
from bot import TGBot

def main():
    token = os.getenv("TELEGRAM_API_KEY")  # Bot Token
    api = os.getenv("OPENAI_API_KEY")  # OpenAI API Key

    if not token or not api:
        raise EnvironmentError("TELEGRAM_API_KEY or OPENAI_API_KEY not set")

    bot = TGBot(token, api)  # Create bot object

    try:
        response = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()  # Load response as JSON

        if 'result' in data and len(data['result']) > 0:
            message = data['result'][-1]['message']
            text = message.get('text', '')

            # Getting User Name And ID
            firstname = message.get('from', {}).get('first_name', 'User')
            chat_id = message.get('from', {}).get('id', 0)

            # Checking The Message And Sending Reply
            if text == '/start':
                image_url = 'https://i.ibb.co/sJ9w2zR/20240904-123746.jpg'  # URL to your image
                caption = f"<b>Hello {firstname}! Welcome To Devil Chat Ai\n\nThis Bot Created By @Shahil44 & @D3VIL_BOY\n\nUse /ask command to ask questions</b>"
                bot.send_photo(chat_id, image_url, caption, "html")
            elif text.startswith('/ask '):
                msg = text.split("/ask ", 1)
                if len(msg) > 1:
                    prompt = msg[1]
                    if prompt:
                        answer = bot.get_answer(prompt)
                        bot.send_message(chat_id, answer, "html")
                    else:
                        bot.send_message(chat_id, "<b>Send like this /ask your question</b>", "html")
                else:
                    bot.send_message(chat_id, "<b>Send like this /ask your question</b>", "html")
        else:
            bot.send_message(chat_id, "No new messages.")
    except Exception as e:
        bot.send_message(chat_id, f"Error in main script: {str(e)}")
        traceback.print_exc()  # Print traceback to console


if __name__ == "__main__":
    main()
