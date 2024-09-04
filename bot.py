import requests
import json

class TGBot:
    def __init__(self, token, api):
        self.token = token
        self.apikey = api

    def open_url(self, url, method, data=None):
        if method == 'POST':
            response = requests.post(url, data=data)
        else:
            response = requests.get(url)
        return response.text

    def control_api(self, method, data=None):
        return self.open_url(f"https://api.telegram.org/bot{self.token}{method}", "POST", data)

    def send_message(self, to, text, parse_mode="HTML"):
        data = {
            'chat_id': to,
            'text': text,
            'parse_mode': parse_mode
        }
        return self.control_api("/sendMessage", data)

    def send_photo(self, to, photo_url, caption="", parse_mode="HTML"):
        data = {
            'chat_id': to,
            'photo': photo_url,
            'caption': caption,
            'parse_mode': parse_mode
        }
        return self.control_api("/sendPhoto", data)

    def get_answer(self, q):
        url = 'https://api.openai.com/v1/engines/text-davinci-003/completions'
        data = {
            'prompt': q,
            'max_tokens': 1024,
            'temperature': 0.5,
            'n': 1,
            'stop': None,
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.apikey}',
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code != 200:
            print('Error retrieving response:', response.text)
            return 'Error retrieving response'

        res = response.json()
        if 'choices' in res and len(res['choices']) > 0 and 'text' in res['choices'][0]:
            return res['choices'][0]['text'].strip()
        else:
            print('Unexpected response format:', res)
            return 'Unexpected response format'
