# Here is how to send a picture via your telegram bot using requests

import requests
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN_TELEGRAM')
chat_id = int(os.getenv('MY_ID'))

def send_photo(file_path, caption):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    data = {
        'chat_id':chat_id,
        'caption':caption
    }
    image = {'photo': open(file_path, 'rb')}  # rb = binaire

    try:
        resp = requests.post(url, data=data, files=image, timeout=10)
        if not resp.status_code == 200:
            print(f"Erreur - return telegram: {resp}")
    except Exception as e:
        print(f"Erreur: {e}")

send_photo(file_path='',caption='')
