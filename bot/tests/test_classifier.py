import unittest
import os
import tempfile
from mlengine import classifier

class TestClassifier(unittest.TestCase):

    def setUp(self):
        classifier.app.testing = True
        self.app = classifier.app.test_client()

    def test_classify(self):
        tests = [
            ('hello', 'salute'),
            ('good morning', 'salute'),
            ('hi sam', 'salute'),
            ('good afternoon', 'salute'),
            ('good bye', 'bye'),
            ('bye sam', 'bye'),
            ('see you later', 'bye'),
            ('that will be all', 'bye'),
            ('I need help', 'help'),
            ('what can i do', 'help'),
            ('what commands can i say', 'help'),
            ('help', 'help'),
            ('remind me to mesasure at 8 in the morning', 'measurement_reminder'),
            ('when do i have to measure myself', 'measurement_reminder'),
            ('set a reminder to weigh myself at 18 in the afternoon', 'measurement_reminder'),
            ('when should i weigh myself', 'measurement_reminder'),
            ('configure a new table for me', 'table'),
            ('when will i have my new table', 'table'),
            ('what do i have to do today', 'table'),
            ('can you send me my table?', 'table'),
            ("lets's start training", 'training'),
            ('rest 5 minutes', 'training'),
            ('5 minute break', 'training'),
            ('start training session', 'training')
        ]

        for value, expected in tests:

            with self.subTest(value=value):
                rv = self.app.post('/classify', json=dict(
                    text=value
                ))
                intent_result = json.loads(rv.text)
                intent = intent_result["action_name"]
                self.assertEqual(intent, expected)

    def test_retrain(self):

        rv = self.app.GET('/retrain')
        data = json.loads(rv.text)
        result = data["result"]
        self.assertEqual(result, 'ok')





if __name__ == '__main__':
    unittest.main()
