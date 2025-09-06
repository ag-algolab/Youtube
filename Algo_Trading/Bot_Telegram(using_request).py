import requests

def send_message(message):
  id = int()
  token = str()
  url =  f'https://api.telegram.org/bot{token}/sendMessage'
  data = {'chat_id': id, 'text': message}
  try:
    requests.post(url, data=data, timeout=10)
  except Exception as e:
    print("Erreur Telegram :", e)

send_message("Hello world")
