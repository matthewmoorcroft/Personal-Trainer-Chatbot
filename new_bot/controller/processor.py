from connections.database import Database
from model.user import User
from connections import net_manager
import requests


def text_normalization(text):
    try:
        return text.lower()
    except:
        return text


def process_message(raw_message):
    db = Database.get_instance()

    telegram_id = raw_message['message']['from']['id']
    first_name = raw_message['message']['from']['first_name']
    message = text_normalization(raw_message['message']['text'])
    user = db.check_user(telegram_id)

    if user is None:
        # db.add_log(id_from = telegram_id, id_to = 'Sam', message, intent = welcome)
        #
        if first_name is not None:
            user = User(name=first_name, telegram_id=telegram_id)
        else:
            user = User(telegram_id)
        # answer = context_engine.welcome(user, message)
        json = {'user': user, 'message': message}
        res = requests.post('http://localhost:30000/process_welcome',
                            json=json)

    else:
        # db.add_log(id_from = user['id'], id_to = 'Sam', message, )
        json = {'user': user, 'message': message}
        res = requests.post('http://localhost:30000/process_message',
                            json=json)
        # answer = context_engine.process(user, message)
    # send to intent
    answer = res.json['message']
    net_manager.send_message(answer, user.telegram_id)
