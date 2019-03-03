from model.logger import log
from mlengine.context_manager import ContextManager
import requests

"""Message goes to context if it doesn't understand, goes to classifier if it
doesn't understand sends to user context answer"""

context_manager = ContextManager()


def process_message(data):
    log('Context Engine: Context processing started')
    # message = text_normalization(data['message'])
    message = data['message']
    user = data['user']
    json = {'text': message}
    res = requests.post('http://localhost:30000/classify',
                        json=json)
    return res.json['intent']


def process_welcome(data):
    log('Context Engine: Welcome process')
    # message = text_normalization(data['message'])
    message = data['message']
    user = data['user']

    context = context_manager.get_context()
    if context:
        if context_manager.check_freshness(context):
            print()

    else:
        context_manager.create_context(data, welcome_process=True)

# Structure how to store context and log in interaction log
