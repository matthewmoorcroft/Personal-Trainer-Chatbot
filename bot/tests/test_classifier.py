import unittest
from mlengine import classifier
import json


class TestClassifier(unittest.TestCase):

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
            ('i would like to measure myself',
                'get_measurements'),
            ('i want to measure myself', 'get_measurements'),
            ('i want to weigh myself',
                'get_measurements'),
            ('new measurements', 'get_measurements'),
            ('configure a new table for me', 'new_table'),
            ('create new table', 'new_table'),
            ('i want a new table', 'new_table'),
            ('can you send me a new table?', 'new_table'),
            ("let's start training", 'start_training'),
            ("i want to train", 'start_training'),
            ('time to train', 'start_training'),
            ('start training session', 'start_training')
        ]

        for value, expected in tests:

            with self.subTest(value=value):
                # add call to classify funtion
                result = json.loads(classifier.classify({'text': value}))
                intent = result['intent']
                self.assertEqual(intent, expected)

    def test_retrain(self):

        answer = json.loads(classifier.retrain())
        result = answer["result"]
        self.assertEqual(result, 'ok')


if __name__ == '__main__':
    unittest.main()
