import requests

import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN_TELEGRAM')
chat_id = int(os.getenv('MY_ID'))

def send_video(file_path, caption):
    url = f"https://api.telegram.org/bot{token}/sendVideo"
    data = {
        'chat_id':chat_id,
        'caption':caption
    }
    video = {'video': open(file_path, 'rb')}

    try:
        resp = requests.post(url, data=data, files=video, timeout=60)
        if not resp.status_code == 200:
            print(f"Erreur - return telegram: {resp}")
    except Exception as e:
        print(f"Erreur: {e}")

send_video(file_path='',caption='')
