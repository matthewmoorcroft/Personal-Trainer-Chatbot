from model.user import User
from connections import net_manager
import requests
from model.logger import log


def text_normalization(text):
    try:
        return text.lower()
    except TypeError:
        return text


def process_message(raw_message):

    telegram_id = raw_message['message']['from']['id']
    message = text_normalization(raw_message['message']['text'])

    try:
        user = User()

        json = {'user': user, 'message': message}
        res = requests.post('http://localhost:30000/process_message',
                            json=json)
    except TypeError:
        log("Processing new user")
        json = {'new_user_id': f'new{telegram_id}', 'message': message}
        res = requests.post('http://localhost:30000/process_welcome',
                            json=json)

    answer = res.json['message']
    net_manager.send_message(answer, user.telegram_id)
