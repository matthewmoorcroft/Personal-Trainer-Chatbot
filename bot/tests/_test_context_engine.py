import unittest
from mlengine.context_engine import process_message, process_welcome


class TestContextEngine(unittest.TestCase):

    def test_process_message(self):
        # test every process case
        id = 1234
        test_salute = {
            'id': id,
            'text': 'hello'
        }
        result_salute = {
            'intent': 'salute',
            'variables': '',
            'response': ['Hi $name$ how can I help you'],
            'finished': True
        }

        test_bye = {
            'id': id,
            'text': 'bye'
        }
        result_bye = {
            'intent': 'bye',
            'variables': '',
            'response': ['See ya, I will be here if you need anything'],
            'finished': True
        }

        test_help = {
            'id': id,
            'text': 'i need help'
        }
        result_help = {
            'intent': 'help',
            'variables': '',
            'response': ['These are the things I can help you out with'],
            'finished': True
        }

        test_get_measurement = {
            'id': id,
            'text': 'Here are my new measurements, 85.2 Kg'
        }
        result_get_measurement = {
            'intent': 'get_measurements',
            'variables': {
                'weight': 85.2
            },
            'response': ['Great I have taken note of the new measurements'],
            'finished': True
        }

        test_new_table = {
            'id': id,
            'text': """i want a new table to gain
                                muscle with a 5 day routine"""
        }
        result_new_table = {
            'intent': 'new_table',
            'variables': {
                'type': 'gain',
                'days': 4
            },
            'response': ['Here is your new table'],
            'finished': True
        }

        test_start_training = {
            'id': id,
            'text': 'i would like to start training'
        }
        result_start_training = {
            'intent': 'start_training',
            'variables': '',
            'response': ["Great let's get started"],
            'finished': True
        }

        tests = [
            (test_salute, result_salute),
            (test_bye, result_bye),
            (test_help, result_help),
            (test_get_measurement, result_get_measurement),
            (test_new_table, result_new_table),
            (test_start_training, result_start_training)
        ]
        for value, expected in tests:
            with self.subTest(value=value):

                result = process_message(value)
                if not result['finished']:
                    confirmation = {
                        'id': id,
                        'text': 'yes'
                    }
                    result = process_message(confirmation)

                self.assertEqual(result['intent'], expected['intent'])
                self.assertEqual(result['variables'], expected['variables'])
                self.assertEqual(result['finished'], expected['finished'])

    def test_process_welcome(self):
        test_welcome_step1 = {
            'text': '/start'
        }
        result_welcome_step1 = {
            'intent': 'welcome',
            'variables': '',
            'response': ["""Hey, I don't seem to know you. Do you want me to
                            help you out with your training?"""],
            'finished': False
        }
        test_welcome_step2 = {
            'text': 'yes'
        }
        result_welcome_step2 = {
            'intent': 'welcome',
            'variables': '',
            'response': ["""Great, nice to meet you, by what name
                            would you like me to talk to you."""],
            'finished': False
        }
        test_welcome_step3 = {
            'text': 'matthew'
        }
        result_welcome_step3 = {
            'intent': 'welcome',
            'variables': {
                'name': 'matthew'
            },
            'response': [
                """So $name$, nice name. Let's get started, before
                    anything I'll give you a tour of what we are going
                    to be doing.""",
                """Before anything what are you looking to do. Muscle
                    toning (Muscle gain), Loose Weight or Definition"""
            ],
            'finished': False
        }
        test_welcome_step4 = {
            'text': 'muscle toning'
        }
        result_welcome_step4 = {
            'intent': 'welcome',
            'variables': {
                'name': 'matthew',
                'training_option': 'muscle_toning'
            },
            'response': [
                """Great to know, I will do everything in my power to
                         assist you in completing your objectives.""",
                """Do you want me to help you out with what routines
                         to follow?"""
            ],
            'finished': False
        }
        test_welcome_step5 = {
            'text': 'yes'
        }
        result_welcome_step5 = {
            'intent': 'welcome',
            'variables': {
                'name': 'matthew',
                'training_option': 'muscle_toning',
                'table_management': True
            },
            'response': [
                """Perfect, every month I will provide a rutine for
                         you to follow."""
                """Do you want me to track your progress?"""
            ],
            'finished': False
        }
        test_welcome_step6 = {
            'text': 'yes'
        }
        result_welcome_step6 = {
            'intent': 'welcome',
            'variables': {
                'name': 'matthew',
                'training_option': 'muscle_toning',
                'table_management': True,
                'track_progress': True
            },
            'response': ["""To have an idea of how to track you I need to
                         to know if you are a male or female person"""
                         ],
            'finished': False
        }
        test_welcome_step7 = {
            'text': 'male'
        }
        result_welcome_step7 = {
            'intent': 'welcome',
            'variables': {
                'name': 'matthew',
                'training_option': 'muscle_toning',
                'table_management': True,
                'track_progress': True,
                'gender': 'male'
            },
            'response': ["""Ok, let's start with some measurements, we will
                         begin with how much do you weigh"""
                         ],
            'finished': False
        }
        test_welcome_step8 = {
            'text': 'i weigh 84.25 kg'
        }
        result_welcome_step8 = {
            'intent': 'welcome',
            'variables': {
                'name': 'matthew',
                'training_option': 'muscle_toning',
                'table_management': True,
                'track_progress': True,
                'gender': 'male',
                'measurements': {
                    'weight': 84.25
                }
            },
            'response': ["""Great, that will be all I need for now, if you
                         need anything just ask"""],
            'finished': True
        }
        tests = [
            (test_welcome_step1, result_welcome_step1),
            (test_welcome_step2, result_welcome_step2),
            (test_welcome_step3, result_welcome_step3),
            (test_welcome_step4, result_welcome_step4),
            (test_welcome_step5, result_welcome_step5),
            (test_welcome_step6, result_welcome_step6),
            (test_welcome_step7, result_welcome_step7),
            (test_welcome_step8, result_welcome_step8)
        ]

        for value, expected in tests:
            with self.subTest(value=value):

                result = process_welcome(value)

                self.assertEqual(result['intent'], expected['intent'])
                self.assertEqual(result['variables'], expected['variables'])
                self.assertEqual(result['finished'], expected['finished'])
