import requests

'''
video [en]: https://youtu.be/nzejSoiGrd8?si=_TTxCgEVeNPSzZND
video [fr]: https://youtu.be/nzejSoiGrd8?si=QCPm59Rxoiq-abS_
'''
# WARNING:
# This is a minimal educational example.
# Never hardcode your TOKEN or CHAT_ID in public repositories.
# Always use environment variables (.env file) for security.

def send_message(message):
  id = int(XXXXXXXX)    
  token = str(XXXXXXXX)
  url =  f'https://api.telegram.org/bot{token}/sendMessage'
  data = {'chat_id': id, 'text': message}
  try:
    requests.post(url, data=data, timeout=10)
  except Exception as e:
    print("Erreur Telegram :", e)

send_message("Hello world")
