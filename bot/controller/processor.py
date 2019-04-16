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

    telegram_id = raw_message['from']['id']
    message = text_normalization(raw_message['text'])

    # Temporary solution
    json = {'text': message}
    res = requests.post('http://localhost:5089/classify',
                        json=json)
    # Future functionality
    # try:
    #     user = User()
    #
    #     json = {'user': user, 'message': message}
    #
    #     res = requests.post('http://localhost:30000/process_message',
    #                         json=json)
    #
    # except TypeError:
    #     log("Processing new user")
    #     json = {'new_user_id': f'new{telegram_id}', 'message': message}
    #     res = requests.post('http://localhost:30000/process_welcome',
    #                         json=json)

    # Future functionality
    # res = action()
    # answer = res.json['message']
    # answer = json.loads(res.text)['intent']
    answer = json.loads(res.text)['intent']
    net_manager.send_message(answer,    telegram_id)
