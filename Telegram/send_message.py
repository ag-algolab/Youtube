# Here is how to send a message via your telegram bot using python 
# It supposes you registered your Bot Token & Chat ID in a .env file 

import requests
import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN_TELEGRAM')
chat_id = int(os.getenv('MY_ID'))

def send_message(to_send):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        'chat_id':chat_id,
        'text':to_send
    }
    try:
        requests.post(url, data, timeout=10)
    except Exception as e:
        print(f"Erreur: {e}")

send_message('hello world')
