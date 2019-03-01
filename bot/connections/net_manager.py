import requests

BOT_ID = "725490953"
BOT_TOKEN = "AAF79oRlrKI6SqZNCqjOLRtRwzmOF7A-Yt4"
URL = "https://api.telegram.org/bot" + BOT_ID + ":" + BOT_TOKEN + "/"


def send_message(answer, telegram_id):
    message = f"{URL}sendMessage?chat_id={telegram_id}&text={answer}"
    try:
        requests.get(message)
        return {'result': "ok"}
    except Exception as e:
        print(e)
        return {'result': "error"}
