# bot.py
import requests

class TgBot:
    def __init__(self, token, apikey):
        self.token = token
        self.apikey = apikey

    def open_url(self, url, method='POST', data=None):
        """Send an HTTP request to a given URL."""
        if method == 'POST':
            response = requests.post(url, data=data)
        else:
            response = requests.get(url, params=data)
        return response.json()  # Assuming the API returns a JSON response

    def control_api(self, method, data=None):
        """Send a request to the Telegram Bot API."""
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        return self.open_url(url, 'POST', data)

    def send_message(self, to, text, parse_mode='Markdown'):
        """Send a message to a Telegram chat."""
        data = {
            'chat_id': to,
            'text': text,
            'parse_mode': parse_mode
        }
        return self.control_api('sendMessage', data)

# Example usage (Replace 'your-telegram-bot-api-key' with actual key):
# bot = TgBot('your-telegram-bot-api-key', 'your-openai-api-key')
# response = bot.send_message('chat_id', 'Hello World!')
# print(response)
